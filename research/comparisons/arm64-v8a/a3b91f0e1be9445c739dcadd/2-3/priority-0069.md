# v15.7.4 → v16.0.0 · 最優先の変更候補 (69)

[一覧の目次](README.md)

<a id="compare-3acdc1ffd8987c11238dee528e7ca2e5"></a>

### [`00b66584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md) → [`00bd5a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md) _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5aa0",
      "incomplete_value": false,
      "site": "00bd5aa4",
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
      "definition_site": "00b665a0",
      "incomplete_value": false,
      "site": "00b665a4",
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
      "definition_site": "00bd5ab0",
      "incomplete_value": true,
      "site": "00bd5abc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b665b0",
      "incomplete_value": true,
      "site": "00b665bc",
      "value": [
        "LOAD",
        "8",
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
      "00bd5aa0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd5ab0",
      "DATA",
      [
        "storage",
        "010a17d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd5aa0",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd5ab0",
      "DATA",
      [
        "storage",
        "011266e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b665a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md#insn-00b665a4) · [`00b6659c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md#insn-00b6659c) · [`00b665a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md#insn-00b665a0)
- 新版 `00bd5aa4`（命令位置の公開資料なし） · `00bd5a9c`（命令位置の公開資料なし） · `00bd5aa0`（命令位置の公開資料なし）

~~~diff
- 00b665a4 ["INT_ADD", "register:40f0:8", ["const:b665a4:8", "const:4:8"]]
- 00b665a4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd5aa4 ["INT_ADD", "register:40f0:8", ["const:bd5aa4:8", "const:4:8"]]
+ 00bd5aa4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b665a4 bytes f7de0194
+ 00bd5aa4 bytes 57140294
- 00b6659c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd5a9c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6659c bytes 80b9fff0
+ 00bd5a9c bytes a0b6ff90
- 00b665a0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b665a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b665a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b665a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd5aa0 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd5aa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5aa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5aa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b665a0 bytes 00c81791
+ 00bd5aa0 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff75a50127b5db5682b7342aa20dbbc"></a>

### [`00b665c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md) → [`00bd5ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b665c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b665c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b665c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b665c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b665c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5ad0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5ac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5ac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5ad0",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b665c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md#insn-00b665c0) · [`00b665c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md#insn-00b665c4) · [`00b665d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md#insn-00b665d4)
- 新版 `00bd5ad4`（命令位置の公開資料なし）

~~~diff
- 00b665c0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b665c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b665c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b665c0 bytes f30f1ef8
- 00b665c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b665c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b665c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b665c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b665c4 bytes fd7b01a9
- 00b665d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b665d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5ad4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5ad4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b665d4 bytes e80000b5
+ 00bd5ad4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0723f3ae9319f83012bdfb627266642a"></a>

### [`00b66600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md) → [`00bd5b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd5b2c",
      "incomplete_value": true,
      "site": "00bd5b2c",
      "value": [
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
    "old": {
      "definition_site": "00b6662c",
      "incomplete_value": true,
      "site": "00b6662c",
      "value": [
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
      "definition_site": "00bd5b14",
      "incomplete_value": true,
      "site": "00bd5b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66614",
      "incomplete_value": true,
      "site": "00b66614",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5b1c",
      "incomplete_value": false,
      "site": "00bd5b24",
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
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6661c",
      "incomplete_value": false,
      "site": "00b66624",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5b10",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5b1c",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00bd5b2c",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5b10",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5b1c",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5b2c",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md#insn-00b66624) · [`00b6662c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md#insn-00b6662c) · [`00b6660c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md#insn-00b6660c)
- 新版 `00bd5b24`（命令位置の公開資料なし） · `00bd5b2c`（命令位置の公開資料なし） · `00bd5b0c`（命令位置の公開資料なし）

~~~diff
- 00b66624 ["INT_ADD", "register:40f0:8", ["const:b66624:8", "const:4:8"]]
- 00b66624 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5b24 ["INT_ADD", "register:40f0:8", ["const:bd5b24:8", "const:4:8"]]
+ 00bd5b24 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66624 bytes 9bde0194
+ 00bd5b24 bytes fb130294
- 00b6662c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b6662c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5b2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00bd5b2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6662c bytes 60f203f9
+ 00bd5b2c bytes 607603f9
- 00b6660c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5b0c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6660c bytes d32900f0
+ 00bd5b0c bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2113aa8543134bf392dc55077d2e9e4"></a>

### [`00b66640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md) → [`00bd5b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5b70",
      "incomplete_value": true,
      "site": "00bd5b70",
      "value": [
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
    "old": {
      "definition_site": "00b66670",
      "incomplete_value": true,
      "site": "00b66670",
      "value": [
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
      "definition_site": "00bd5b54",
      "incomplete_value": true,
      "site": "00bd5b54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66654",
      "incomplete_value": true,
      "site": "00b66654",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5b60",
      "incomplete_value": false,
      "site": "00bd5b68",
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
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66660",
      "incomplete_value": false,
      "site": "00b66668",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5b50",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5b60",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00bd5b70",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5b50",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5b60",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5b70",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md#insn-00b66668) · [`00b66670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md#insn-00b66670) · [`00b6664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md#insn-00b6664c)
- 新版 `00bd5b68`（命令位置の公開資料なし） · `00bd5b70`（命令位置の公開資料なし） · `00bd5b4c`（命令位置の公開資料なし）

~~~diff
- 00b66668 ["INT_ADD", "register:40f0:8", ["const:b66668:8", "const:4:8"]]
- 00b66668 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5b68 ["INT_ADD", "register:40f0:8", ["const:bd5b68:8", "const:4:8"]]
+ 00bd5b68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66668 bytes 8ade0194
+ 00bd5b68 bytes ea130294
- 00b66670 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00bd5b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66670 bytes 60f203f9
+ 00bd5b70 bytes 607603f9
- 00b6664c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5b4c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6664c bytes d32900f0
+ 00bd5b4c bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f01d02db7d2f06f574f05386fabf85a"></a>

### [`00b66684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md) → [`00bd5b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 20.00% / 新版 33.33%

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
      "site": "00b666b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5bb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5b98",
      "incomplete_value": true,
      "site": "00bd5b98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66698",
      "incomplete_value": true,
      "site": "00b66698",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd5b94",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b666a0",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b666b4",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5b94",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5ba0",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5bb4",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md#insn-00b66698) · [`00b666ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md#insn-00b666ac) · [`00b666b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md#insn-00b666b4)
- 新版 `00bd5b98`（命令位置の公開資料なし） · `00bd5bac`（命令位置の公開資料なし）

~~~diff
- 00b66698 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b66698 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd5b98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5b98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66698 bytes 080100b5
+ 00bd5b98 bytes 080100b5
- 00b666ac ["INT_ADD", "register:40f0:8", ["const:b666ac:8", "const:4:8"]]
- 00b666ac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5bac ["INT_ADD", "register:40f0:8", ["const:bd5bac:8", "const:4:8"]]
+ 00bd5bac ["CALL", null, ["callee:00c5ab10:8"]]
- 00b666ac bytes 79de0194
+ 00bd5bac bytes d9130294
- 00b666b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b666b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b666b4 bytes 60f203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d970f2f924fe0d9c842e2de6582136c"></a>

### [`00b666d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md) → [`00bd5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md) _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b666d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b666d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b666d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b666d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b666d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b666dc",
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
      "00bd5bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd5bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5bdc",
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

- 旧版 [`00b666d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md#insn-00b666d4) · [`00b666d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md#insn-00b666d8) · [`00b666dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md#insn-00b666dc)

~~~diff
- 00b666d4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b666d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b666d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b666d4 bytes f50f1df8
- 00b666d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b666d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b666d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b666d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b666d8 bytes f44f01a9
- 00b666dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b666dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b666dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b666dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b666dc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8412ae48a7e62b751055fa25ecb0a5"></a>

### [`00b66740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md) → [`00bd5c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md) _ZN8firebase4auth13playgamescred12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd5c7c",
      "incomplete_value": true,
      "site": "00bd5c7c",
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
    "old": {
      "definition_site": "00b6677c",
      "incomplete_value": true,
      "site": "00b6677c",
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
      "definition_site": "00bd5c9c",
      "incomplete_value": true,
      "site": "00bd5c9c",
      "value": [
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
    "old": {
      "definition_site": "00b6679c",
      "incomplete_value": true,
      "site": "00b6679c",
      "value": [
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
      "definition_site": "00bd5c58",
      "incomplete_value": true,
      "site": "00bd5c58",
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
      "definition_site": "00b66758",
      "incomplete_value": true,
      "site": "00b66758",
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
      "00bd5c54",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5c60",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5c7c",
      "WRITE",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd5c54",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5c60",
      "READ",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5c7c",
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6677c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md#insn-00b6677c) · [`00b66798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md#insn-00b66798) · [`00b6679c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md#insn-00b6679c)
- 新版 `00bd5c7c`（命令位置の公開資料なし） · `00bd5c98`（命令位置の公開資料なし） · `00bd5c9c`（命令位置の公開資料なし）

~~~diff
- 00b6677c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6677c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6677c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
- 00b6677c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd5c7c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd5c7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd5c7c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
+ 00bd5c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6677c bytes bfa21f39
+ 00bd5c7c bytes bfc21b39
- 00b66798 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66798 ["INT_ADD", "register:40f0:8", ["const:b66798:8", "const:4:8"]]
- 00b66798 ["CALLIND", null, ["register:0:8"]]
+ 00bd5c98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5c98 ["INT_ADD", "register:40f0:8", ["const:bd5c98:8", "const:4:8"]]
+ 00bd5c98 ["CALLIND", null, ["register:0:8"]]
- 00b66798 bytes 00013fd6
+ 00bd5c98 bytes 00013fd6
- 00b6679c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b6679c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6679c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd5c9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00bd5c9c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd5c9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6679c bytes 9ff203f9
+ 00bd5c9c bytes 9f7603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b417d98797a49a00c2b8cedb612b568f"></a>

### [`00b667b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md) → [`00bd5cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md) _ZN8firebase4auth13playgamescred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5cf0",
      "incomplete_value": true,
      "site": "00bd5cf0",
      "value": [
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
    "old": {
      "definition_site": "00b667f0",
      "incomplete_value": true,
      "site": "00b667f0",
      "value": [
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
      "definition_site": "00bd5ccc",
      "incomplete_value": true,
      "site": "00bd5ccc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b667cc",
      "incomplete_value": true,
      "site": "00b667cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5cd4",
      "incomplete_value": false,
      "site": "00bd5ce8",
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
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b667d4",
      "incomplete_value": false,
      "site": "00b667e8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5cc4",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5cd4",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00bd5cf0",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5cc4",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5cd4",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5cf0",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b667e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md#insn-00b667e8) · [`00b667f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md#insn-00b667f0) · [`00b667bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md#insn-00b667bc)
- 新版 `00bd5ce8`（命令位置の公開資料なし） · `00bd5cf0`（命令位置の公開資料なし） · `00bd5cbc`（命令位置の公開資料なし）

~~~diff
- 00b667e8 ["INT_ADD", "register:40f0:8", ["const:b667e8:8", "const:4:8"]]
- 00b667e8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5ce8 ["INT_ADD", "register:40f0:8", ["const:bd5ce8:8", "const:4:8"]]
+ 00bd5ce8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b667e8 bytes 2ade0194
+ 00bd5ce8 bytes 8a130294
- 00b667f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b667f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5cf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00bd5cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b667f0 bytes 80f203f9
+ 00bd5cf0 bytes 807603f9
- 00b667bc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5cbc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b667bc bytes d42900f0
+ 00bd5cbc bytes 942a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9d05beb1068aaefe7a4fe247d271cec"></a>

### [`00b6685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md) → [`00bd5d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md) _ZN8firebase4auth13playgamescred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5d9c",
      "incomplete_value": true,
      "site": "00bd5d9c",
      "value": [
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
    "old": {
      "definition_site": "00b6689c",
      "incomplete_value": true,
      "site": "00b6689c",
      "value": [
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
      "definition_site": "00bd5d78",
      "incomplete_value": true,
      "site": "00bd5d78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66878",
      "incomplete_value": true,
      "site": "00b66878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5d80",
      "incomplete_value": false,
      "site": "00bd5d94",
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
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66880",
      "incomplete_value": false,
      "site": "00b66894",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5d70",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5d80",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00bd5d9c",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5d70",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5d80",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5d9c",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md#insn-00b66894) · [`00b6689c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md#insn-00b6689c) · [`00b66868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md#insn-00b66868)
- 新版 `00bd5d94`（命令位置の公開資料なし） · `00bd5d9c`（命令位置の公開資料なし） · `00bd5d68`（命令位置の公開資料なし）

~~~diff
- 00b66894 ["INT_ADD", "register:40f0:8", ["const:b66894:8", "const:4:8"]]
- 00b66894 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5d94 ["INT_ADD", "register:40f0:8", ["const:bd5d94:8", "const:4:8"]]
+ 00bd5d94 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66894 bytes ffdd0194
+ 00bd5d94 bytes 5f130294
- 00b6689c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b6689c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00bd5d9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6689c bytes 80f203f9
+ 00bd5d9c bytes 807603f9
- 00b66868 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5d68 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66868 bytes d42900f0
+ 00bd5d68 bytes 942a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76b472fcc6d42694e12344f4955ff3bf"></a>

### [`00b668cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md) → [`00bd5dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5de8",
      "incomplete_value": false,
      "site": "00bd5dec",
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
      "definition_site": "00b668e8",
      "incomplete_value": false,
      "site": "00b668ec",
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
      "definition_site": "00bd5df8",
      "incomplete_value": true,
      "site": "00bd5e04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b668f8",
      "incomplete_value": true,
      "site": "00b66904",
      "value": [
        "LOAD",
        "8",
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
      "00bd5de8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd5df8",
      "DATA",
      [
        "storage",
        "010a17f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd5de8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd5df8",
      "DATA",
      [
        "storage",
        "01126700",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b668ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md#insn-00b668ec) · [`00b668e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md#insn-00b668e4) · [`00b668e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md#insn-00b668e8)
- 新版 `00bd5dec`（命令位置の公開資料なし） · `00bd5de4`（命令位置の公開資料なし） · `00bd5de8`（命令位置の公開資料なし）

~~~diff
- 00b668ec ["INT_ADD", "register:40f0:8", ["const:b668ec:8", "const:4:8"]]
- 00b668ec ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd5dec ["INT_ADD", "register:40f0:8", ["const:bd5dec:8", "const:4:8"]]
+ 00bd5dec ["CALL", null, ["callee:00c5ac00:8"]]
- 00b668ec bytes 25de0194
+ 00bd5dec bytes 85130294
- 00b668e4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd5de4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b668e4 bytes 80b9fff0
+ 00bd5de4 bytes a0b6ff90
- 00b668e8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b668e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b668e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b668e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd5de8 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd5de8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5de8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5de8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b668e8 bytes 00c81791
+ 00bd5de8 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f342f6fd453c28408b10cbda6d194a68"></a>

### [`00b66908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md) → [`00bd5e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd5e34",
      "incomplete_value": true,
      "site": "00bd5e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66934",
      "incomplete_value": true,
      "site": "00b66934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd5e1c",
      "incomplete_value": true,
      "site": "00bd5e1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6691c",
      "incomplete_value": true,
      "site": "00b6691c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5e28",
      "incomplete_value": false,
      "site": "00bd5e2c",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66928",
      "incomplete_value": false,
      "site": "00b6692c",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5e18",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5e28",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00bd5e34",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5e18",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5e28",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd5e34",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6692c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md#insn-00b6692c) · [`00b66934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md#insn-00b66934) · [`00b66914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md#insn-00b66914)
- 新版 `00bd5e2c`（命令位置の公開資料なし） · `00bd5e34`（命令位置の公開資料なし） · `00bd5e14`（命令位置の公開資料なし）

~~~diff
- 00b6692c ["INT_ADD", "register:40f0:8", ["const:b6692c:8", "const:4:8"]]
- 00b6692c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5e2c ["INT_ADD", "register:40f0:8", ["const:bd5e2c:8", "const:4:8"]]
+ 00bd5e2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6692c bytes d9dd0194
+ 00bd5e2c bytes 39130294
- 00b66934 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b66934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
+ 00bd5e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66934 bytes 600204f9
+ 00bd5e34 bytes 608603f9
- 00b66914 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5e14 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66914 bytes d32900f0
+ 00bd5e14 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7053f2ba516d69a325d389f798ba7fcc"></a>

### [`00b66948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md) → [`00bd5e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd5e74",
      "incomplete_value": true,
      "site": "00bd5e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66974",
      "incomplete_value": true,
      "site": "00b66974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd5e5c",
      "incomplete_value": true,
      "site": "00bd5e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6695c",
      "incomplete_value": true,
      "site": "00b6695c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5e64",
      "incomplete_value": false,
      "site": "00bd5e6c",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66964",
      "incomplete_value": false,
      "site": "00b6696c",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5e58",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5e64",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00bd5e74",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5e58",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5e64",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd5e74",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6696c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md#insn-00b6696c) · [`00b66974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md#insn-00b66974) · [`00b66954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md#insn-00b66954)
- 新版 `00bd5e6c`（命令位置の公開資料なし） · `00bd5e74`（命令位置の公開資料なし） · `00bd5e54`（命令位置の公開資料なし）

~~~diff
- 00b6696c ["INT_ADD", "register:40f0:8", ["const:b6696c:8", "const:4:8"]]
- 00b6696c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5e6c ["INT_ADD", "register:40f0:8", ["const:bd5e6c:8", "const:4:8"]]
+ 00bd5e6c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6696c bytes c9dd0194
+ 00bd5e6c bytes 29130294
- 00b66974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b66974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
+ 00bd5e74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66974 bytes 600204f9
+ 00bd5e74 bytes 608603f9
- 00b66954 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5e54 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66954 bytes d32900f0
+ 00bd5e54 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9b2db2995158a908edbc96c471c840"></a>

### [`00b66988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md) → [`00bd5e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5eb8",
      "incomplete_value": true,
      "site": "00bd5eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669b8",
      "incomplete_value": true,
      "site": "00b669b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd5e9c",
      "incomplete_value": true,
      "site": "00bd5e9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6699c",
      "incomplete_value": true,
      "site": "00b6699c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5ea8",
      "incomplete_value": false,
      "site": "00bd5eb0",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669a8",
      "incomplete_value": false,
      "site": "00b669b0",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5e98",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5ea8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00bd5eb8",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5e98",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5ea8",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd5eb8",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md#insn-00b669b0) · [`00b669b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md#insn-00b669b8) · [`00b66994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md#insn-00b66994)
- 新版 `00bd5eb0`（命令位置の公開資料なし） · `00bd5eb8`（命令位置の公開資料なし） · `00bd5e94`（命令位置の公開資料なし）

~~~diff
- 00b669b0 ["INT_ADD", "register:40f0:8", ["const:b669b0:8", "const:4:8"]]
- 00b669b0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5eb0 ["INT_ADD", "register:40f0:8", ["const:bd5eb0:8", "const:4:8"]]
+ 00bd5eb0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b669b0 bytes b8dd0194
+ 00bd5eb0 bytes 18130294
- 00b669b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b669b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
+ 00bd5eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b669b8 bytes 600204f9
+ 00bd5eb8 bytes 608603f9
- 00b66994 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5e94 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66994 bytes d32900f0
+ 00bd5e94 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aee0a4a420981b66d3479cbe009e1a7e"></a>

### [`00b669cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md) → [`00bd5ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5efc",
      "incomplete_value": true,
      "site": "00bd5efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669fc",
      "incomplete_value": true,
      "site": "00b669fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd5ee0",
      "incomplete_value": true,
      "site": "00bd5ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669e0",
      "incomplete_value": true,
      "site": "00b669e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5ee8",
      "incomplete_value": false,
      "site": "00bd5ef4",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669e8",
      "incomplete_value": false,
      "site": "00b669f4",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5edc",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5ee8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00bd5efc",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5edc",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5ee8",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd5efc",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md#insn-00b669f4) · [`00b669fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md#insn-00b669fc) · [`00b669d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md#insn-00b669d8)
- 新版 `00bd5ef4`（命令位置の公開資料なし） · `00bd5efc`（命令位置の公開資料なし） · `00bd5ed8`（命令位置の公開資料なし）

~~~diff
- 00b669f4 ["INT_ADD", "register:40f0:8", ["const:b669f4:8", "const:4:8"]]
- 00b669f4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5ef4 ["INT_ADD", "register:40f0:8", ["const:bd5ef4:8", "const:4:8"]]
+ 00bd5ef4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b669f4 bytes a7dd0194
+ 00bd5ef4 bytes 07130294
- 00b669fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b669fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5efc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
+ 00bd5efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b669fc bytes 600204f9
+ 00bd5efc bytes 608603f9
- 00b669d8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5ed8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b669d8 bytes d32900f0
+ 00bd5ed8 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c045181acab6b302ca51a8f08b3c7e"></a>

### [`00b66a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md) → [`00bd5f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md) _ZN8firebase4auth11twittercred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd5f74",
      "incomplete_value": true,
      "site": "00bd5f74",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a74",
      "incomplete_value": true,
      "site": "00b66a74",
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
            "const:808:8"
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
      "definition_site": "00bd5f50",
      "incomplete_value": true,
      "site": "00bd5f5c",
      "value": [
        "LOAD",
        "8",
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
                "const:708:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a50",
      "incomplete_value": true,
      "site": "00b66a5c",
      "value": [
        "LOAD",
        "8",
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
                "const:800:8"
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
      "00bd5f30",
      "READ",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5f50",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f74",
      "WRITE",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd5f30",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5f50",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f74",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md#insn-00b66a5c) · [`00b66a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md#insn-00b66a74) · [`00b66a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md#insn-00b66a2c)
- 新版 `00bd5f5c`（命令位置の公開資料なし） · `00bd5f74`（命令位置の公開資料なし） · `00bd5f2c`（命令位置の公開資料なし）

~~~diff
- 00b66a5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66a5c ["INT_ADD", "register:40f0:8", ["const:b66a5c:8", "const:4:8"]]
- 00b66a5c ["CALLIND", null, ["register:0:8"]]
+ 00bd5f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5f5c ["INT_ADD", "register:40f0:8", ["const:bd5f5c:8", "const:4:8"]]
+ 00bd5f5c ["CALLIND", null, ["register:0:8"]]
- 00b66a5c bytes 00013fd6
+ 00bd5f5c bytes 00013fd6
- 00b66a74 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66a74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:808:8"]]
- 00b66a74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd5f74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd5f74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:710:8"]]
+ 00bd5f74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66a74 bytes a0222039
+ 00bd5f74 bytes a0421c39
- 00b66a2c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd5f2c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b66a2c bytes d52900f0
+ 00bd5f2c bytes 952a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da166d241286be2884d480e9beeaae60"></a>

### [`00b66a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md) → [`00bd5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md) _ZN8firebase4auth11twittercred12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd5fc4",
      "incomplete_value": true,
      "site": "00bd5fc4",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ac4",
      "incomplete_value": true,
      "site": "00b66ac4",
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
            "const:808:8"
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
      "definition_site": "00bd5fe4",
      "incomplete_value": true,
      "site": "00bd5fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ae4",
      "incomplete_value": true,
      "site": "00b66ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd5fa0",
      "incomplete_value": true,
      "site": "00bd5fa0",
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
      "definition_site": "00b66aa0",
      "incomplete_value": true,
      "site": "00b66aa0",
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
      "00bd5f9c",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5fa8",
      "READ",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5fc4",
      "WRITE",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd5f9c",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5fa8",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5fc4",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md#insn-00b66ac4) · [`00b66ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md#insn-00b66ae0) · [`00b66ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md#insn-00b66ae4)
- 新版 `00bd5fc4`（命令位置の公開資料なし） · `00bd5fe0`（命令位置の公開資料なし） · `00bd5fe4`（命令位置の公開資料なし）

~~~diff
- 00b66ac4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66ac4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66ac4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:808:8"]]
- 00b66ac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd5fc4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd5fc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd5fc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:710:8"]]
+ 00bd5fc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66ac4 bytes bf222039
+ 00bd5fc4 bytes bf421c39
- 00b66ae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66ae0 ["INT_ADD", "register:40f0:8", ["const:b66ae0:8", "const:4:8"]]
- 00b66ae0 ["CALLIND", null, ["register:0:8"]]
+ 00bd5fe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5fe0 ["INT_ADD", "register:40f0:8", ["const:bd5fe0:8", "const:4:8"]]
+ 00bd5fe0 ["CALLIND", null, ["register:0:8"]]
- 00b66ae0 bytes 00013fd6
+ 00bd5fe0 bytes 00013fd6
- 00b66ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00b66ae4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b66ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd5fe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
+ 00bd5fe4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd5fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b66ae4 bytes 9f0204f9
+ 00bd5fe4 bytes 9f8603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b11e2d93d8d09b00f4e57964f6c2696d"></a>

### [`00b66af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md) → [`00bd5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md) _ZN8firebase4auth11twittercred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b66b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6038"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66b14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66b0c",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd603c"
      ]
    ],
    [
      "unmatched:00b66b1c",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd600c",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd603c"
      ]
    ],
    [
      "00bd601c",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md#insn-00b66b14) · [`00b66b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md#insn-00b66b30) · [`00b66b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md#insn-00b66b38)
- 新版 `00bd6030`（命令位置の公開資料なし）

~~~diff
- 00b66b14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66b14 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66b14 bytes 410100b5
- 00b66b30 ["INT_ADD", "register:40f0:8", ["const:b66b30:8", "const:4:8"]]
- 00b66b30 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6030 ["INT_ADD", "register:40f0:8", ["const:bd6030:8", "const:4:8"]]
+ 00bd6030 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66b30 bytes 58dd0194
+ 00bd6030 bytes b8120294
- 00b66b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00b66b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66b38 bytes 800204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22f8a9b273238da2178690e2919b2c5b"></a>

### [`00b66b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md) → [`00bd6068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6068.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6084",
      "incomplete_value": false,
      "site": "00bd6088",
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
      "definition_site": "00b66b84",
      "incomplete_value": false,
      "site": "00b66b88",
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
      "definition_site": "00bd6094",
      "incomplete_value": true,
      "site": "00bd60a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66b94",
      "incomplete_value": true,
      "site": "00b66ba0",
      "value": [
        "LOAD",
        "8",
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
      "00bd6084",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd6094",
      "DATA",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6084",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd6094",
      "DATA",
      [
        "storage",
        "01126718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md#insn-00b66b88) · [`00b66b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md#insn-00b66b80) · [`00b66b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md#insn-00b66b84)
- 新版 `00bd6088`（命令位置の公開資料なし） · `00bd6080`（命令位置の公開資料なし） · `00bd6084`（命令位置の公開資料なし）

~~~diff
- 00b66b88 ["INT_ADD", "register:40f0:8", ["const:b66b88:8", "const:4:8"]]
- 00b66b88 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6088 ["INT_ADD", "register:40f0:8", ["const:bd6088:8", "const:4:8"]]
+ 00bd6088 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b66b88 bytes 7edd0194
+ 00bd6088 bytes de120294
- 00b66b80 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd6080 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b66b80 bytes 80b9ffd0
+ 00bd6080 bytes 80b6ffd0
- 00b66b84 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b66b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6084 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd6084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66b84 bytes 001c1591
+ 00bd6084 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b825c40ae40820d50369362252379c"></a>

### [`00b66ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md) → [`00bd60a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md) _ZN8firebase4auth11twittercred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd60e4",
      "incomplete_value": true,
      "site": "00bd60e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66be4",
      "incomplete_value": true,
      "site": "00b66be4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "definition_site": "00bd60c0",
      "incomplete_value": true,
      "site": "00bd60c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bc0",
      "incomplete_value": true,
      "site": "00b66bc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd60c8",
      "incomplete_value": false,
      "site": "00bd60dc",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bc8",
      "incomplete_value": false,
      "site": "00b66bdc",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd60b8",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd60c8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00bd60e4",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd60b8",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd60c8",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd60e4",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md#insn-00b66bdc) · [`00b66be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md#insn-00b66be4) · [`00b66bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md#insn-00b66bb0)
- 新版 `00bd60dc`（命令位置の公開資料なし） · `00bd60e4`（命令位置の公開資料なし） · `00bd60b0`（命令位置の公開資料なし）

~~~diff
- 00b66bdc ["INT_ADD", "register:40f0:8", ["const:b66bdc:8", "const:4:8"]]
- 00b66bdc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd60dc ["INT_ADD", "register:40f0:8", ["const:bd60dc:8", "const:4:8"]]
+ 00bd60dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66bdc bytes 2ddd0194
+ 00bd60dc bytes 8d120294
- 00b66be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00b66be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd60e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
+ 00bd60e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66be4 bytes 800204f9
+ 00bd60e4 bytes 808603f9
- 00b66bb0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd60b0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66bb0 bytes d42900f0
+ 00bd60b0 bytes 942a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84f562a221c2cd2d67e8b646c3b07f1e"></a>

### [`00b66c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md) → [`00bd6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6130",
      "incomplete_value": false,
      "site": "00bd6134",
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
      "definition_site": "00b66c30",
      "incomplete_value": false,
      "site": "00b66c34",
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
      "definition_site": "00bd6140",
      "incomplete_value": true,
      "site": "00bd614c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66c40",
      "incomplete_value": true,
      "site": "00b66c4c",
      "value": [
        "LOAD",
        "8",
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
      "00bd6130",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd6140",
      "DATA",
      [
        "storage",
        "010a1818",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6130",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd6140",
      "DATA",
      [
        "storage",
        "01126720",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md#insn-00b66c34) · [`00b66c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md#insn-00b66c2c) · [`00b66c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md#insn-00b66c30)
- 新版 `00bd6134`（命令位置の公開資料なし） · `00bd612c`（命令位置の公開資料なし） · `00bd6130`（命令位置の公開資料なし）

~~~diff
- 00b66c34 ["INT_ADD", "register:40f0:8", ["const:b66c34:8", "const:4:8"]]
- 00b66c34 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6134 ["INT_ADD", "register:40f0:8", ["const:bd6134:8", "const:4:8"]]
+ 00bd6134 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b66c34 bytes 53dd0194
+ 00bd6134 bytes b3120294
- 00b66c2c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd612c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b66c2c bytes 80b9fff0
+ 00bd612c bytes 80b6fff0
- 00b66c30 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b66c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6130 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd6130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66c30 bytes 00c81791
+ 00bd6130 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68227450f96fda15630903740f9e00d3"></a>

### [`00b66c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md) → [`00bd6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd617c",
      "incomplete_value": true,
      "site": "00bd617c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c7c",
      "incomplete_value": true,
      "site": "00b66c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00bd6164",
      "incomplete_value": true,
      "site": "00bd6164",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c64",
      "incomplete_value": true,
      "site": "00b66c64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6170",
      "incomplete_value": false,
      "site": "00bd6174",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c70",
      "incomplete_value": false,
      "site": "00b66c74",
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
            "const:71:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6160",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6170",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00bd617c",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6160",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6170",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      "00bd617c",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md#insn-00b66c74) · [`00b66c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md#insn-00b66c7c) · [`00b66c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md#insn-00b66c5c)
- 新版 `00bd6174`（命令位置の公開資料なし） · `00bd617c`（命令位置の公開資料なし） · `00bd615c`（命令位置の公開資料なし）

~~~diff
- 00b66c74 ["INT_ADD", "register:40f0:8", ["const:b66c74:8", "const:4:8"]]
- 00b66c74 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6174 ["INT_ADD", "register:40f0:8", ["const:bd6174:8", "const:4:8"]]
+ 00bd6174 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66c74 bytes 07dd0194
+ 00bd6174 bytes 67120294
- 00b66c7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00b66c7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd617c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bd617c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66c7c bytes 601204f9
+ 00bd617c bytes 609603f9
- 00b66c5c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd615c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66c5c bytes d32900f0
+ 00bd615c bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936dfbf4e1fb4da8ffc8d996983e6aaf"></a>

### [`00b66c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md) → [`00bd6190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd61bc",
      "incomplete_value": true,
      "site": "00bd61bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cbc",
      "incomplete_value": true,
      "site": "00b66cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00bd61a4",
      "incomplete_value": true,
      "site": "00bd61a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ca4",
      "incomplete_value": true,
      "site": "00b66ca4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd61ac",
      "incomplete_value": false,
      "site": "00bd61b4",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cac",
      "incomplete_value": false,
      "site": "00b66cb4",
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
            "const:71:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd61a0",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61ac",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00bd61bc",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd61a0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61ac",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      "00bd61bc",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md#insn-00b66cb4) · [`00b66cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md#insn-00b66cbc) · [`00b66c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md#insn-00b66c9c)
- 新版 `00bd61b4`（命令位置の公開資料なし） · `00bd61bc`（命令位置の公開資料なし） · `00bd619c`（命令位置の公開資料なし）

~~~diff
- 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
- 00b66cb4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd61b4 ["INT_ADD", "register:40f0:8", ["const:bd61b4:8", "const:4:8"]]
+ 00bd61b4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66cb4 bytes f7dc0194
+ 00bd61b4 bytes 57120294
- 00b66cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00b66cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd61bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bd61bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66cbc bytes 601204f9
+ 00bd61bc bytes 609603f9
- 00b66c9c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd619c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66c9c bytes d32900f0
+ 00bd619c bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a9f4f2dcdc6cfa3a455e75a0cc9867"></a>

### [`00b66cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md) → [`00bd61d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6200",
      "incomplete_value": true,
      "site": "00bd6200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d00",
      "incomplete_value": true,
      "site": "00b66d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00bd61e4",
      "incomplete_value": true,
      "site": "00bd61e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ce4",
      "incomplete_value": true,
      "site": "00b66ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd61f0",
      "incomplete_value": false,
      "site": "00bd61f8",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cf0",
      "incomplete_value": false,
      "site": "00b66cf8",
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
            "const:71:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd61e0",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61f0",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00bd6200",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd61e0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61f0",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      "00bd6200",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md#insn-00b66cf8) · [`00b66d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md#insn-00b66d00) · [`00b66cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md#insn-00b66cdc)
- 新版 `00bd61f8`（命令位置の公開資料なし） · `00bd6200`（命令位置の公開資料なし） · `00bd61dc`（命令位置の公開資料なし）

~~~diff
- 00b66cf8 ["INT_ADD", "register:40f0:8", ["const:b66cf8:8", "const:4:8"]]
- 00b66cf8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd61f8 ["INT_ADD", "register:40f0:8", ["const:bd61f8:8", "const:4:8"]]
+ 00bd61f8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66cf8 bytes e6dc0194
+ 00bd61f8 bytes 46120294
- 00b66d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00b66d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bd6200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66d00 bytes 601204f9
+ 00bd6200 bytes 609603f9
- 00b66cdc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd61dc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66cdc bytes d32900f0
+ 00bd61dc bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4903274a8bc960bfae917b1c0dbf64da"></a>

### [`00b66d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md) → [`00bd6214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6244",
      "incomplete_value": true,
      "site": "00bd6244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d44",
      "incomplete_value": true,
      "site": "00b66d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00bd6228",
      "incomplete_value": true,
      "site": "00bd6228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d28",
      "incomplete_value": true,
      "site": "00b66d28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6230",
      "incomplete_value": false,
      "site": "00bd623c",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d30",
      "incomplete_value": false,
      "site": "00b66d3c",
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
            "const:71:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6224",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6230",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00bd6244",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6224",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6230",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      "00bd6244",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md#insn-00b66d3c) · [`00b66d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md#insn-00b66d44) · [`00b66d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md#insn-00b66d20)
- 新版 `00bd623c`（命令位置の公開資料なし） · `00bd6244`（命令位置の公開資料なし） · `00bd6220`（命令位置の公開資料なし）

~~~diff
- 00b66d3c ["INT_ADD", "register:40f0:8", ["const:b66d3c:8", "const:4:8"]]
- 00b66d3c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd623c ["INT_ADD", "register:40f0:8", ["const:bd623c:8", "const:4:8"]]
+ 00bd623c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66d3c bytes d5dc0194
+ 00bd623c bytes 35120294
- 00b66d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00b66d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bd6244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66d44 bytes 601204f9
+ 00bd6244 bytes 609603f9
- 00b66d20 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6220 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66d20 bytes d32900f0
+ 00bd6220 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09782814a7367e720de6a44f659739af"></a>

### [`00b66d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md) → [`00bd6264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd62bc",
      "incomplete_value": true,
      "site": "00bd62bc",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66dbc",
      "incomplete_value": true,
      "site": "00b66dbc",
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
            "const:828:8"
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
      "definition_site": "00bd6298",
      "incomplete_value": true,
      "site": "00bd62a4",
      "value": [
        "LOAD",
        "8",
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d98",
      "incomplete_value": true,
      "site": "00b66da4",
      "value": [
        "LOAD",
        "8",
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
                "const:820:8"
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66dcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6278",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6284",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66dc0"
      ]
    ],
    [
      "00bd6298",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6278",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6284",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd62c0"
      ]
    ],
    [
      "00bd6298",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md#insn-00b66da4) · [`00b66dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md#insn-00b66dbc) · [`00b66dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md#insn-00b66dcc)
- 新版 `00bd62a4`（命令位置の公開資料なし） · `00bd62bc`（命令位置の公開資料なし）

~~~diff
- 00b66da4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66da4 ["INT_ADD", "register:40f0:8", ["const:b66da4:8", "const:4:8"]]
- 00b66da4 ["CALLIND", null, ["register:0:8"]]
+ 00bd62a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd62a4 ["INT_ADD", "register:40f0:8", ["const:bd62a4:8", "const:4:8"]]
+ 00bd62a4 ["CALLIND", null, ["register:0:8"]]
- 00b66da4 bytes 00013fd6
+ 00bd62a4 bytes 00013fd6
- 00b66dbc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66dbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:828:8"]]
- 00b66dbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd62bc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd62bc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:730:8"]]
+ 00bd62bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66dbc bytes a0a22039
+ 00bd62bc bytes a0c21c39
- 00b66dcc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b66dcc ["RETURN", null, ["register:0:8"]]
- 00b66dcc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0b288b79a23af2c0ac55f825046d2a3"></a>

### [`00b66dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md) → [`00bd62d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 32.14% / 新版 32.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66dd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66dd8",
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
      "00bd62d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd62d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd62d8",
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

- 旧版 [`00b66dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md#insn-00b66dd0) · [`00b66dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md#insn-00b66dd4) · [`00b66dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md#insn-00b66dd8)

~~~diff
- 00b66dd0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b66dd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b66dd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b66dd0 bytes f50f1df8
- 00b66dd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b66dd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b66dd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66dd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66dd4 bytes f44f01a9
- 00b66dd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66dd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66dd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b66dd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66dd8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef42ab41b90a7cb53bb218a8bd5ff525"></a>

### [`00b66e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md) → [`00bd6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b66e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66e44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66e54",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6340",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6344",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6354",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md#insn-00b66e40) · [`00b66e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md#insn-00b66e44) · [`00b66e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md#insn-00b66e5c)

~~~diff
- 00b66e40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b66e40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b66e40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b66e40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b66e40 bytes f44fbea9
- 00b66e44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66e44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66e44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66e44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66e44 bytes fd7b01a9
- 00b66e5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66e5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66e5c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a7d645ff642d0acaef7bea92b5c533d"></a>

### [`00b66eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md) → [`00bd63ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b66f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd642c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66f08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66f00",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6430"
      ]
    ],
    [
      "unmatched:00b66f10",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6400",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6430"
      ]
    ],
    [
      "00bd6410",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md#insn-00b66f08) · [`00b66f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md#insn-00b66f24) · [`00b66f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md#insn-00b66f2c)
- 新版 `00bd6424`（命令位置の公開資料なし）

~~~diff
- 00b66f08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66f08 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b66f08 bytes 410100b5
- 00b66f24 ["INT_ADD", "register:40f0:8", ["const:b66f24:8", "const:4:8"]]
- 00b66f24 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6424 ["INT_ADD", "register:40f0:8", ["const:bd6424:8", "const:4:8"]]
+ 00bd6424 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66f24 bytes 5bdc0194
+ 00bd6424 bytes bb110294
- 00b66f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
- 00b66f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66f2c bytes 801204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ca2225df716d1a8aefa9c2b166c782"></a>

### [`00b6705c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md) → [`00bd655c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b6705c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6705c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b67060",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd656c",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd655c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6560",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd656c",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6705c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md#insn-00b6705c) · [`00b67060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md#insn-00b67060) · [`00b67070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md#insn-00b67070)
- 新版 `00bd6570`（命令位置の公開資料なし）

~~~diff
- 00b6705c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6705c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6705c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6705c bytes f30f1ef8
- 00b67060 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b67060 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b67060 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b67060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b67060 bytes fd7b01a9
- 00b67070 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b67070 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd6570 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd6570 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b67070 bytes 080100b5
+ 00bd6570 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3236faccec2c894f875d735a7933ab59"></a>

### [`00b67188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md) → [`00bd6688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b671c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd66c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b671a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6719c",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b671a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd66cc"
      ]
    ],
    [
      "unmatched:00b671ac",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd669c",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd66a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd66cc"
      ]
    ],
    [
      "00bd66ac",
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b671a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md#insn-00b671a4) · [`00b671c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md#insn-00b671c0) · [`00b671c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md#insn-00b671c8)
- 新版 `00bd66c0`（命令位置の公開資料なし）

~~~diff
- 00b671a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b671a4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b671a4 bytes 410100b5
- 00b671c0 ["INT_ADD", "register:40f0:8", ["const:b671c0:8", "const:4:8"]]
- 00b671c0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd66c0 ["INT_ADD", "register:40f0:8", ["const:bd66c0:8", "const:4:8"]]
+ 00bd66c0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b671c0 bytes b4db0194
+ 00bd66c0 bytes 14110294
- 00b671c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00b671c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b671c8 bytes 802a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f35ef9cf6ed524d164a2a2cad97115"></a>

### [`00b67234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md) → [`00bd6734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b67234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b67234",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b67238",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b67248",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6734",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6738",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6748",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md#insn-00b67234) · [`00b67238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md#insn-00b67238) · [`00b67250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md#insn-00b67250)

~~~diff
- 00b67234 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b67234 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b67234 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b67234 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b67234 bytes f44fbea9
- 00b67238 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b67238 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b67238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b67238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b67238 bytes fd7b01a9
- 00b67250 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b67250 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67250 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84a8c4ba53e6e9349f19289d2478069"></a>

### [`00b672e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md) → [`00bd67e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b672e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b672e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b672e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b672e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b672e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd67f0",
      "READ",
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
      "00bd67e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd67e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd67f0",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b672e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md#insn-00b672e0) · [`00b672e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md#insn-00b672e4) · [`00b672f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md#insn-00b672f4)
- 新版 `00bd67f4`（命令位置の公開資料なし）

~~~diff
- 00b672e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b672e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b672e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b672e0 bytes f30f1ef8
- 00b672e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b672e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b672e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b672e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b672e4 bytes fd7b01a9
- 00b672f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b672f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd67f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd67f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b672f4 bytes e80000b5
+ 00bd67f4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed74c574def6bc5d199a72babead6d23"></a>

### [`00b67320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md) → [`00bd6820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "site": "00b67320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67324"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b67320",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b67324",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6830",
      "READ",
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
      "00bd6820",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6824",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6830",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md#insn-00b67320) · [`00b67324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md#insn-00b67324) · [`00b67334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md#insn-00b67334)
- 新版 `00bd6834`（命令位置の公開資料なし）

~~~diff
- 00b67320 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b67320 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b67320 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b67320 bytes f30f1ef8
- 00b67324 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b67324 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b67324 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b67324 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b67324 bytes fd7b01a9
- 00b67334 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b67334 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd6834 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd6834 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67334 bytes e80000b5
+ 00bd6834 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8dbc48f8717e1650de53099c5d357a4"></a>

### [`00b67360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md) → [`00bd6860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6890",
      "incomplete_value": true,
      "site": "00bd6890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:778:8"
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00bd6874",
      "incomplete_value": true,
      "site": "00bd6874",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6880",
      "incomplete_value": false,
      "site": "00bd6888",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67380",
      "incomplete_value": false,
      "site": "00b67388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6870",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6880",
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      "00bd6890",
      "WRITE",
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
      "00bd6870",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6880",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6890",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md#insn-00b67388) · [`00b67390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md#insn-00b67390) · [`00b6736c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md#insn-00b6736c)
- 新版 `00bd6888`（命令位置の公開資料なし） · `00bd6890`（命令位置の公開資料なし） · `00bd686c`（命令位置の公開資料なし）

~~~diff
- 00b67388 ["INT_ADD", "register:40f0:8", ["const:b67388:8", "const:4:8"]]
- 00b67388 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6888 ["INT_ADD", "register:40f0:8", ["const:bd6888:8", "const:4:8"]]
+ 00bd6888 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67388 bytes 42db0194
+ 00bd6888 bytes a2100294
- 00b67390 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00b67390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bd6890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67390 bytes 603a04f9
+ 00bd6890 bytes 60be03f9
- 00b6736c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd686c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6736c bytes d32900d0
+ 00bd686c bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d0511f48f6448abf14326189ff6cad"></a>

### [`00b673a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md) → [`00bd68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd68d4",
      "incomplete_value": true,
      "site": "00bd68d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673d4",
      "incomplete_value": true,
      "site": "00b673d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00bd68b8",
      "incomplete_value": true,
      "site": "00bd68b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673b8",
      "incomplete_value": true,
      "site": "00b673b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd68c0",
      "incomplete_value": false,
      "site": "00bd68cc",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673c0",
      "incomplete_value": false,
      "site": "00b673cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd68b4",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd68c0",
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      "00bd68d4",
      "WRITE",
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
      "00bd68b4",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd68c0",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd68d4",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b673cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md#insn-00b673cc) · [`00b673d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md#insn-00b673d4) · [`00b673b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md#insn-00b673b0)
- 新版 `00bd68cc`（命令位置の公開資料なし） · `00bd68d4`（命令位置の公開資料なし） · `00bd68b0`（命令位置の公開資料なし）

~~~diff
- 00b673cc ["INT_ADD", "register:40f0:8", ["const:b673cc:8", "const:4:8"]]
- 00b673cc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd68cc ["INT_ADD", "register:40f0:8", ["const:bd68cc:8", "const:4:8"]]
+ 00bd68cc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b673cc bytes 31db0194
+ 00bd68cc bytes 91100294
- 00b673d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00b673d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd68d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bd68d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b673d4 bytes 603a04f9
+ 00bd68d4 bytes 60be03f9
- 00b673b0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd68b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b673b0 bytes d32900d0
+ 00bd68b0 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d285fba594342ddfd161ceafef4d1b"></a>

### [`00b673f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md) → [`00bd68f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd694c",
      "incomplete_value": true,
      "site": "00bd694c",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6744c",
      "incomplete_value": true,
      "site": "00b6744c",
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
            "const:878:8"
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
      "definition_site": "00bd6928",
      "incomplete_value": true,
      "site": "00bd6934",
      "value": [
        "LOAD",
        "8",
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67428",
      "incomplete_value": true,
      "site": "00b67434",
      "value": [
        "LOAD",
        "8",
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
                "const:870:8"
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
      "00bd6908",
      "READ",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6928",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd694c",
      "WRITE",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6908",
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6928",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd694c",
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md#insn-00b67434) · [`00b6744c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md#insn-00b6744c) · [`00b67404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md#insn-00b67404)
- 新版 `00bd6934`（命令位置の公開資料なし） · `00bd694c`（命令位置の公開資料なし） · `00bd6904`（命令位置の公開資料なし）

~~~diff
- 00b67434 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67434 ["INT_ADD", "register:40f0:8", ["const:b67434:8", "const:4:8"]]
- 00b67434 ["CALLIND", null, ["register:0:8"]]
+ 00bd6934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6934 ["INT_ADD", "register:40f0:8", ["const:bd6934:8", "const:4:8"]]
+ 00bd6934 ["CALLIND", null, ["register:0:8"]]
- 00b67434 bytes 00013fd6
+ 00bd6934 bytes 00013fd6
- 00b6744c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6744c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:878:8"]]
- 00b6744c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd694c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd694c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:780:8"]]
+ 00bd694c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6744c bytes a0e22139
+ 00bd694c bytes a0021e39
- 00b67404 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd6904 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b67404 bytes d52900d0
+ 00bd6904 bytes 952a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-989975c6c2a3d39dd0faad6d4fb6c7e2"></a>

### [`00b67460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md) → [`00bd6960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd699c",
      "incomplete_value": true,
      "site": "00bd699c",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6749c",
      "incomplete_value": true,
      "site": "00b6749c",
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
            "const:878:8"
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
      "definition_site": "00bd69bc",
      "incomplete_value": true,
      "site": "00bd69bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674bc",
      "incomplete_value": true,
      "site": "00b674bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00bd6978",
      "incomplete_value": true,
      "site": "00bd6978",
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
      "definition_site": "00b67478",
      "incomplete_value": true,
      "site": "00b67478",
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
      "00bd6974",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6980",
      "READ",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd699c",
      "WRITE",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6974",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6980",
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd699c",
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md#insn-00b6749c) · [`00b674b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md#insn-00b674b8) · [`00b674bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md#insn-00b674bc)
- 新版 `00bd699c`（命令位置の公開資料なし） · `00bd69b8`（命令位置の公開資料なし） · `00bd69bc`（命令位置の公開資料なし）

~~~diff
- 00b6749c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6749c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6749c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:878:8"]]
- 00b6749c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd699c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd699c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd699c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:780:8"]]
+ 00bd699c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6749c bytes bfe22139
+ 00bd699c bytes bf021e39
- 00b674b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b674b8 ["INT_ADD", "register:40f0:8", ["const:b674b8:8", "const:4:8"]]
- 00b674b8 ["CALLIND", null, ["register:0:8"]]
+ 00bd69b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd69b8 ["INT_ADD", "register:40f0:8", ["const:bd69b8:8", "const:4:8"]]
+ 00bd69b8 ["CALLIND", null, ["register:0:8"]]
- 00b674b8 bytes 00013fd6
+ 00bd69b8 bytes 00013fd6
- 00b674bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
- 00b674bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b674bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd69bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00bd69bc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd69bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b674bc bytes 9f3a04f9
+ 00bd69bc bytes 9fbe03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9574294eb708ba87e185fa798d9adf75"></a>

### [`00b674d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md) → [`00bd69d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6a10",
      "incomplete_value": true,
      "site": "00bd6a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67510",
      "incomplete_value": true,
      "site": "00b67510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00bd69ec",
      "incomplete_value": true,
      "site": "00bd69ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674ec",
      "incomplete_value": true,
      "site": "00b674ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd69f4",
      "incomplete_value": false,
      "site": "00bd6a08",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674f4",
      "incomplete_value": false,
      "site": "00b67508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd69e4",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd69f4",
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      "00bd6a10",
      "WRITE",
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
      "00bd69e4",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd69f4",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6a10",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md#insn-00b67508) · [`00b67510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md#insn-00b67510) · [`00b674dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md#insn-00b674dc)
- 新版 `00bd6a08`（命令位置の公開資料なし） · `00bd6a10`（命令位置の公開資料なし） · `00bd69dc`（命令位置の公開資料なし）

~~~diff
- 00b67508 ["INT_ADD", "register:40f0:8", ["const:b67508:8", "const:4:8"]]
- 00b67508 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6a08 ["INT_ADD", "register:40f0:8", ["const:bd6a08:8", "const:4:8"]]
+ 00bd6a08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67508 bytes e2da0194
+ 00bd6a08 bytes 42100294
- 00b67510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
- 00b67510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6a10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00bd6a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67510 bytes 803a04f9
+ 00bd6a10 bytes 80be03f9
- 00b674dc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd69dc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b674dc bytes d42900d0
+ 00bd69dc bytes 942a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ba263c8673a6b7ea6231973c87fed8"></a>

### [`00b67540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md) → [`00bd6a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6a5c",
      "incomplete_value": false,
      "site": "00bd6a60",
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
      "definition_site": "00b6755c",
      "incomplete_value": false,
      "site": "00b67560",
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
      "definition_site": "00bd6a6c",
      "incomplete_value": true,
      "site": "00bd6a78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6756c",
      "incomplete_value": true,
      "site": "00b67578",
      "value": [
        "LOAD",
        "8",
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
      "00bd6a5c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd6a6c",
      "DATA",
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
      "00bd6a5c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd6a6c",
      "DATA",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md#insn-00b67560) · [`00b67558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md#insn-00b67558) · [`00b6755c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md#insn-00b6755c)
- 新版 `00bd6a60`（命令位置の公開資料なし） · `00bd6a58`（命令位置の公開資料なし） · `00bd6a5c`（命令位置の公開資料なし）

~~~diff
- 00b67560 ["INT_ADD", "register:40f0:8", ["const:b67560:8", "const:4:8"]]
- 00b67560 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6a60 ["INT_ADD", "register:40f0:8", ["const:bd6a60:8", "const:4:8"]]
+ 00bd6a60 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67560 bytes 08db0194
+ 00bd6a60 bytes 68100294
- 00b67558 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd6a58 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b67558 bytes 80b9ffb0
+ 00bd6a58 bytes 80b6ffd0
- 00b6755c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6755c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6755c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6755c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6a5c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd6a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6755c bytes 001c1591
+ 00bd6a5c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734afd74afb0a8e068271d90267ac394"></a>

### [`00b6757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md) → [`00bd6a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6abc",
      "incomplete_value": true,
      "site": "00bd6abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675bc",
      "incomplete_value": true,
      "site": "00b675bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00bd6a98",
      "incomplete_value": true,
      "site": "00bd6a98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67598",
      "incomplete_value": true,
      "site": "00b67598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6aa0",
      "incomplete_value": false,
      "site": "00bd6ab4",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675a0",
      "incomplete_value": false,
      "site": "00b675b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6a90",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6aa0",
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      "00bd6abc",
      "WRITE",
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
      "00bd6a90",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6aa0",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6abc",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b675b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md#insn-00b675b4) · [`00b675bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md#insn-00b675bc) · [`00b67588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md#insn-00b67588)
- 新版 `00bd6ab4`（命令位置の公開資料なし） · `00bd6abc`（命令位置の公開資料なし） · `00bd6a88`（命令位置の公開資料なし）

~~~diff
- 00b675b4 ["INT_ADD", "register:40f0:8", ["const:b675b4:8", "const:4:8"]]
- 00b675b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6ab4 ["INT_ADD", "register:40f0:8", ["const:bd6ab4:8", "const:4:8"]]
+ 00bd6ab4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b675b4 bytes b7da0194
+ 00bd6ab4 bytes 17100294
- 00b675bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
- 00b675bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6abc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00bd6abc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b675bc bytes 803a04f9
+ 00bd6abc bytes 80be03f9
- 00b67588 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6a88 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67588 bytes d42900d0
+ 00bd6a88 bytes 942a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214e3bfacb5138b9ef98ba29a2bbea49"></a>

### [`00b675ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md) → [`00bd6aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6aec.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6b08",
      "incomplete_value": false,
      "site": "00bd6b0c",
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
      "definition_site": "00b67608",
      "incomplete_value": false,
      "site": "00b6760c",
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
      "definition_site": "00bd6b18",
      "incomplete_value": true,
      "site": "00bd6b24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67618",
      "incomplete_value": true,
      "site": "00b67624",
      "value": [
        "LOAD",
        "8",
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
      "00bd6b08",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd6b18",
      "DATA",
      [
        "storage",
        "010a18c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6b08",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd6b18",
      "DATA",
      [
        "storage",
        "011267c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md#insn-00b6760c) · [`00b67604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md#insn-00b67604) · [`00b67608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md#insn-00b67608)
- 新版 `00bd6b0c`（命令位置の公開資料なし） · `00bd6b04`（命令位置の公開資料なし） · `00bd6b08`（命令位置の公開資料なし）

~~~diff
- 00b6760c ["INT_ADD", "register:40f0:8", ["const:b6760c:8", "const:4:8"]]
- 00b6760c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6b0c ["INT_ADD", "register:40f0:8", ["const:bd6b0c:8", "const:4:8"]]
+ 00bd6b0c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6760c bytes ddda0194
+ 00bd6b0c bytes 3d100294
- 00b67604 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd6b04 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b67604 bytes 80b9ffd0
+ 00bd6b04 bytes 80b6fff0
- 00b67608 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6b08 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd6b08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6b08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6b08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67608 bytes 00c81791
+ 00bd6b08 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359d6832d1a4e5f30df380de17488b98"></a>

### [`00b67628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md) → [`00bd6b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6b54",
      "incomplete_value": true,
      "site": "00bd6b54",
      "value": [
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
    "old": {
      "definition_site": "00b67654",
      "incomplete_value": true,
      "site": "00b67654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00bd6b3c",
      "incomplete_value": true,
      "site": "00bd6b3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6763c",
      "incomplete_value": true,
      "site": "00b6763c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6b48",
      "incomplete_value": false,
      "site": "00bd6b4c",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67648",
      "incomplete_value": false,
      "site": "00b6764c",
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
      "00bd6b38",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6b48",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00bd6b54",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6b38",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6b48",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6b54",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md#insn-00b6764c) · [`00b67654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md#insn-00b67654) · [`00b67634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md#insn-00b67634)
- 新版 `00bd6b4c`（命令位置の公開資料なし） · `00bd6b54`（命令位置の公開資料なし） · `00bd6b34`（命令位置の公開資料なし）

~~~diff
- 00b6764c ["INT_ADD", "register:40f0:8", ["const:b6764c:8", "const:4:8"]]
- 00b6764c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6b4c ["INT_ADD", "register:40f0:8", ["const:bd6b4c:8", "const:4:8"]]
+ 00bd6b4c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6764c bytes 91da0194
+ 00bd6b4c bytes f10f0294
- 00b67654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b67654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bd6b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67654 bytes 606604f9
+ 00bd6b54 bytes 60ea03f9
- 00b67634 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6b34 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67634 bytes d32900d0
+ 00bd6b34 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-564377de9b406abe081dde88e29cb414"></a>

### [`00b67668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md) → [`00bd6b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6b94",
      "incomplete_value": true,
      "site": "00bd6b94",
      "value": [
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
    "old": {
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
            "const:8c8:8"
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
      "definition_site": "00bd6b7c",
      "incomplete_value": true,
      "site": "00bd6b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6767c",
      "incomplete_value": true,
      "site": "00b6767c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6b84",
      "incomplete_value": false,
      "site": "00bd6b8c",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd6b78",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6b84",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00bd6b94",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6b78",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6b84",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6b94",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6768c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md#insn-00b6768c) · [`00b67694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md#insn-00b67694) · [`00b67674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md#insn-00b67674)
- 新版 `00bd6b8c`（命令位置の公開資料なし） · `00bd6b94`（命令位置の公開資料なし） · `00bd6b74`（命令位置の公開資料なし）

~~~diff
- 00b6768c ["INT_ADD", "register:40f0:8", ["const:b6768c:8", "const:4:8"]]
- 00b6768c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6b8c ["INT_ADD", "register:40f0:8", ["const:bd6b8c:8", "const:4:8"]]
+ 00bd6b8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6768c bytes 81da0194
+ 00bd6b8c bytes e10f0294
- 00b67694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b67694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bd6b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67694 bytes 606604f9
+ 00bd6b94 bytes 60ea03f9
- 00b67674 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6b74 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67674 bytes d32900d0
+ 00bd6b74 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acc1c865c3b7582870fb5fc5da17b22c"></a>

### [`00b676a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md) → [`00bd6ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6bd8",
      "incomplete_value": true,
      "site": "00bd6bd8",
      "value": [
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00bd6bbc",
      "incomplete_value": true,
      "site": "00bd6bbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6bc8",
      "incomplete_value": false,
      "site": "00bd6bd0",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676c8",
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
      "00bd6bb8",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6bc8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00bd6bd8",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6bb8",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6bc8",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6bd8",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b676d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md#insn-00b676d0) · [`00b676d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md#insn-00b676d8) · [`00b676b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md#insn-00b676b4)
- 新版 `00bd6bd0`（命令位置の公開資料なし） · `00bd6bd8`（命令位置の公開資料なし） · `00bd6bb4`（命令位置の公開資料なし）

~~~diff
- 00b676d0 ["INT_ADD", "register:40f0:8", ["const:b676d0:8", "const:4:8"]]
- 00b676d0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6bd0 ["INT_ADD", "register:40f0:8", ["const:bd6bd0:8", "const:4:8"]]
+ 00bd6bd0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b676d0 bytes 70da0194
+ 00bd6bd0 bytes d00f0294
- 00b676d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b676d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6bd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bd6bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b676d8 bytes 606604f9
+ 00bd6bd8 bytes 60ea03f9
- 00b676b4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6bb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b676b4 bytes d32900d0
+ 00bd6bb4 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-948d10a92bb9ee95652c2fba9f3bcc95"></a>

### [`00b676ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md) → [`00bd6bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6c1c",
      "incomplete_value": true,
      "site": "00bd6c1c",
      "value": [
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
    "old": {
      "definition_site": "00b6771c",
      "incomplete_value": true,
      "site": "00b6771c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00bd6c00",
      "incomplete_value": true,
      "site": "00bd6c00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67700",
      "incomplete_value": true,
      "site": "00b67700",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6c08",
      "incomplete_value": false,
      "site": "00bd6c14",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67708",
      "incomplete_value": false,
      "site": "00b67714",
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
      "00bd6bfc",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c08",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00bd6c1c",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6bfc",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c08",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6c1c",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md#insn-00b67714) · [`00b6771c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md#insn-00b6771c) · [`00b676f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md#insn-00b676f8)
- 新版 `00bd6c14`（命令位置の公開資料なし） · `00bd6c1c`（命令位置の公開資料なし） · `00bd6bf8`（命令位置の公開資料なし）

~~~diff
- 00b67714 ["INT_ADD", "register:40f0:8", ["const:b67714:8", "const:4:8"]]
- 00b67714 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6c14 ["INT_ADD", "register:40f0:8", ["const:bd6c14:8", "const:4:8"]]
+ 00bd6c14 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67714 bytes 5fda0194
+ 00bd6c14 bytes bf0f0294
- 00b6771c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b6771c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bd6c1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6771c bytes 606604f9
+ 00bd6c1c bytes 60ea03f9
- 00b676f8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6bf8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b676f8 bytes d32900d0
+ 00bd6bf8 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214817d6bfae2e35283e15b41b3530d1"></a>

### [`00b6773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md) → [`00bd6c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd6c94",
      "incomplete_value": true,
      "site": "00bd6c94",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67794",
      "incomplete_value": true,
      "site": "00b67794",
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
            "const:8d0:8"
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
      "definition_site": "00bd6c70",
      "incomplete_value": true,
      "site": "00bd6c7c",
      "value": [
        "LOAD",
        "8",
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67770",
      "incomplete_value": true,
      "site": "00b6777c",
      "value": [
        "LOAD",
        "8",
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
                "const:8c8:8"
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
      "00bd6c50",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6c70",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c94",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6c50",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6c70",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c94",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6777c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md#insn-00b6777c) · [`00b67794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md#insn-00b67794) · [`00b6774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md#insn-00b6774c)
- 新版 `00bd6c7c`（命令位置の公開資料なし） · `00bd6c94`（命令位置の公開資料なし） · `00bd6c4c`（命令位置の公開資料なし）

~~~diff
- 00b6777c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6777c ["INT_ADD", "register:40f0:8", ["const:b6777c:8", "const:4:8"]]
- 00b6777c ["CALLIND", null, ["register:0:8"]]
+ 00bd6c7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6c7c ["INT_ADD", "register:40f0:8", ["const:bd6c7c:8", "const:4:8"]]
+ 00bd6c7c ["CALLIND", null, ["register:0:8"]]
- 00b6777c bytes 00013fd6
+ 00bd6c7c bytes 00013fd6
- 00b67794 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67794 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
- 00b67794 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd6c94 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd6c94 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
+ 00bd6c94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67794 bytes a0422339
+ 00bd6c94 bytes a0621f39
- 00b6774c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd6c4c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b6774c bytes d52900d0
+ 00bd6c4c bytes 952a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a75c9dcc8d742c0bb162e21654498b8"></a>

### [`00b677a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md) → [`00bd6ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd6ce4",
      "incomplete_value": true,
      "site": "00bd6ce4",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677e4",
      "incomplete_value": true,
      "site": "00b677e4",
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
            "const:8d0:8"
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
      "definition_site": "00bd6d04",
      "incomplete_value": true,
      "site": "00bd6d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67804",
      "incomplete_value": true,
      "site": "00b67804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00bd6cc0",
      "incomplete_value": true,
      "site": "00bd6cc0",
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
      "definition_site": "00b677c0",
      "incomplete_value": true,
      "site": "00b677c0",
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
      "00bd6cbc",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6cc8",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6ce4",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6cbc",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6cc8",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6ce4",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b677e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md#insn-00b677e4) · [`00b67800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md#insn-00b67800) · [`00b67804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md#insn-00b67804)
- 新版 `00bd6ce4`（命令位置の公開資料なし） · `00bd6d00`（命令位置の公開資料なし） · `00bd6d04`（命令位置の公開資料なし）

~~~diff
- 00b677e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b677e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b677e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d0:8"]]
- 00b677e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd6ce4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd6ce4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd6ce4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d8:8"]]
+ 00bd6ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b677e4 bytes bf422339
+ 00bd6ce4 bytes bf621f39
- 00b67800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67800 ["INT_ADD", "register:40f0:8", ["const:b67800:8", "const:4:8"]]
- 00b67800 ["CALLIND", null, ["register:0:8"]]
+ 00bd6d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6d00 ["INT_ADD", "register:40f0:8", ["const:bd6d00:8", "const:4:8"]]
+ 00bd6d00 ["CALLIND", null, ["register:0:8"]]
- 00b67800 bytes 00013fd6
+ 00bd6d00 bytes 00013fd6
- 00b67804 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b67804 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b67804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd6d04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00bd6d04 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd6d04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b67804 bytes 9f6604f9
+ 00bd6d04 bytes 9fea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a24b21d6a534257ac03b5330a2a63699"></a>

### [`00b67818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md) → [`00bd6d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b67858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6d58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67834"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6782c",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b67834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6d5c"
      ]
    ],
    [
      "unmatched:00b6783c",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d2c",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6d5c"
      ]
    ],
    [
      "00bd6d3c",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md#insn-00b67834) · [`00b67850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md#insn-00b67850) · [`00b67858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md#insn-00b67858)
- 新版 `00bd6d50`（命令位置の公開資料なし）

~~~diff
- 00b67834 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b67834 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67834 bytes 410100b5
- 00b67850 ["INT_ADD", "register:40f0:8", ["const:b67850:8", "const:4:8"]]
- 00b67850 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6d50 ["INT_ADD", "register:40f0:8", ["const:bd6d50:8", "const:4:8"]]
+ 00bd6d50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67850 bytes 10da0194
+ 00bd6d50 bytes 700f0294
- 00b67858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b67858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67858 bytes 806604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad2e65d99bbd98b776a92fedc1357db"></a>

### [`00b67888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md) → [`00bd6d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6da4",
      "incomplete_value": false,
      "site": "00bd6da8",
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
      "definition_site": "00b678a4",
      "incomplete_value": false,
      "site": "00b678a8",
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
      "definition_site": "00bd6db4",
      "incomplete_value": true,
      "site": "00bd6dc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b678b4",
      "incomplete_value": true,
      "site": "00b678c0",
      "value": [
        "LOAD",
        "8",
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
      "00bd6da4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd6db4",
      "DATA",
      [
        "storage",
        "010a18d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6da4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd6db4",
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b678a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md#insn-00b678a8) · [`00b678a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md#insn-00b678a0) · [`00b678a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md#insn-00b678a4)
- 新版 `00bd6da8`（命令位置の公開資料なし） · `00bd6da0`（命令位置の公開資料なし） · `00bd6da4`（命令位置の公開資料なし）

~~~diff
- 00b678a8 ["INT_ADD", "register:40f0:8", ["const:b678a8:8", "const:4:8"]]
- 00b678a8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6da8 ["INT_ADD", "register:40f0:8", ["const:bd6da8:8", "const:4:8"]]
+ 00bd6da8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b678a8 bytes 36da0194
+ 00bd6da8 bytes 960f0294
- 00b678a0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd6da0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b678a0 bytes 80b9ffb0
+ 00bd6da0 bytes 80b6ffd0
- 00b678a4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b678a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b678a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b678a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6da4 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd6da4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6da4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6da4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b678a4 bytes 001c1591
+ 00bd6da4 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-718262dc989e0964ba9ce293fb221a74"></a>

### [`00b678c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md) → [`00bd6dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6e04",
      "incomplete_value": true,
      "site": "00bd6e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67904",
      "incomplete_value": true,
      "site": "00b67904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00bd6de0",
      "incomplete_value": true,
      "site": "00bd6de0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b678e0",
      "incomplete_value": true,
      "site": "00b678e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6de8",
      "incomplete_value": false,
      "site": "00bd6dfc",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b678e8",
      "incomplete_value": false,
      "site": "00b678fc",
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
      "00bd6dd8",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6de8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00bd6e04",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6dd8",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6de8",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6e04",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b678fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md#insn-00b678fc) · [`00b67904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md#insn-00b67904) · [`00b678d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md#insn-00b678d0)
- 新版 `00bd6dfc`（命令位置の公開資料なし） · `00bd6e04`（命令位置の公開資料なし） · `00bd6dd0`（命令位置の公開資料なし）

~~~diff
- 00b678fc ["INT_ADD", "register:40f0:8", ["const:b678fc:8", "const:4:8"]]
- 00b678fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6dfc ["INT_ADD", "register:40f0:8", ["const:bd6dfc:8", "const:4:8"]]
+ 00bd6dfc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b678fc bytes e5d90194
+ 00bd6dfc bytes 450f0294
- 00b67904 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b67904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6e04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00bd6e04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67904 bytes 806604f9
+ 00bd6e04 bytes 80ea03f9
- 00b678d0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6dd0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b678d0 bytes d42900d0
+ 00bd6dd0 bytes 942a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-379a64f4120819a32cc66e7e4ff11782"></a>

### [`00b67934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md) → [`00bd6e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6e50",
      "incomplete_value": false,
      "site": "00bd6e54",
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
      "definition_site": "00b67950",
      "incomplete_value": false,
      "site": "00b67954",
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
      "definition_site": "00bd6e60",
      "incomplete_value": true,
      "site": "00bd6e6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67960",
      "incomplete_value": true,
      "site": "00b6796c",
      "value": [
        "LOAD",
        "8",
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
      "00bd6e50",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd6e60",
      "DATA",
      [
        "storage",
        "010a18f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6e50",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd6e60",
      "DATA",
      [
        "storage",
        "011267f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md#insn-00b67954) · [`00b6794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md#insn-00b6794c) · [`00b67950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md#insn-00b67950)
- 新版 `00bd6e54`（命令位置の公開資料なし） · `00bd6e4c`（命令位置の公開資料なし） · `00bd6e50`（命令位置の公開資料なし）

~~~diff
- 00b67954 ["INT_ADD", "register:40f0:8", ["const:b67954:8", "const:4:8"]]
- 00b67954 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd6e54 ["INT_ADD", "register:40f0:8", ["const:bd6e54:8", "const:4:8"]]
+ 00bd6e54 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67954 bytes 0bda0194
+ 00bd6e54 bytes 6b0f0294
- 00b6794c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd6e4c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6794c bytes 80b9ffd0
+ 00bd6e4c bytes 80b6fff0
- 00b67950 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67950 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67950 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67950 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e50 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd6e50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67950 bytes 00c81791
+ 00bd6e50 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8561a7eb9f291c59f90bda562d846401"></a>

### [`00b67970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md) → [`00bd6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd6e9c",
      "incomplete_value": true,
      "site": "00bd6e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6799c",
      "incomplete_value": true,
      "site": "00b6799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd6e84",
      "incomplete_value": true,
      "site": "00bd6e84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67984",
      "incomplete_value": true,
      "site": "00b67984",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6e90",
      "incomplete_value": false,
      "site": "00bd6e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67990",
      "incomplete_value": false,
      "site": "00b67994",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6e80",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6e90",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd6e9c",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e80",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6e90",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd6e9c",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md#insn-00b67994) · [`00b6799c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md#insn-00b6799c) · [`00b6797c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md#insn-00b6797c)
- 新版 `00bd6e94`（命令位置の公開資料なし） · `00bd6e9c`（命令位置の公開資料なし） · `00bd6e7c`（命令位置の公開資料なし）

~~~diff
- 00b67994 ["INT_ADD", "register:40f0:8", ["const:b67994:8", "const:4:8"]]
- 00b67994 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6e94 ["INT_ADD", "register:40f0:8", ["const:bd6e94:8", "const:4:8"]]
+ 00bd6e94 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67994 bytes bfd90194
+ 00bd6e94 bytes 1f0f0294
- 00b6799c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6799c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd6e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6799c bytes 607e04f9
+ 00bd6e9c bytes 600204f9
- 00b6797c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6e7c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6797c bytes d32900d0
+ 00bd6e7c bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69fa77073a080fbcbeb6f021092ddb71"></a>

### [`00b679b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md) → [`00bd6eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd6edc",
      "incomplete_value": true,
      "site": "00bd6edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:8f8:8"
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
      "definition_site": "00bd6ec4",
      "incomplete_value": true,
      "site": "00bd6ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679c4",
      "incomplete_value": true,
      "site": "00b679c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6ecc",
      "incomplete_value": false,
      "site": "00bd6ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679cc",
      "incomplete_value": false,
      "site": "00b679d4",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6ec0",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ecc",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd6edc",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6ec0",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ecc",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd6edc",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b679d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md#insn-00b679d4) · [`00b679dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md#insn-00b679dc) · [`00b679bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md#insn-00b679bc)
- 新版 `00bd6ed4`（命令位置の公開資料なし） · `00bd6edc`（命令位置の公開資料なし） · `00bd6ebc`（命令位置の公開資料なし）

~~~diff
- 00b679d4 ["INT_ADD", "register:40f0:8", ["const:b679d4:8", "const:4:8"]]
- 00b679d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6ed4 ["INT_ADD", "register:40f0:8", ["const:bd6ed4:8", "const:4:8"]]
+ 00bd6ed4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b679d4 bytes afd90194
+ 00bd6ed4 bytes 0f0f0294
- 00b679dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b679dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd6edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b679dc bytes 607e04f9
+ 00bd6edc bytes 600204f9
- 00b679bc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6ebc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b679bc bytes d32900d0
+ 00bd6ebc bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f043ddb841aaf981e636dc686e637d"></a>

### [`00b679f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md) → [`00bd6ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6f20",
      "incomplete_value": true,
      "site": "00bd6f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd6f04",
      "incomplete_value": true,
      "site": "00bd6f04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6f10",
      "incomplete_value": false,
      "site": "00bd6f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a10",
      "incomplete_value": false,
      "site": "00b67a18",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6f00",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f10",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd6f20",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6f00",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f10",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd6f20",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md#insn-00b67a18) · [`00b67a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md#insn-00b67a20) · [`00b679fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md#insn-00b679fc)
- 新版 `00bd6f18`（命令位置の公開資料なし） · `00bd6f20`（命令位置の公開資料なし） · `00bd6efc`（命令位置の公開資料なし）

~~~diff
- 00b67a18 ["INT_ADD", "register:40f0:8", ["const:b67a18:8", "const:4:8"]]
- 00b67a18 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6f18 ["INT_ADD", "register:40f0:8", ["const:bd6f18:8", "const:4:8"]]
+ 00bd6f18 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67a18 bytes 9ed90194
+ 00bd6f18 bytes fe0e0294
- 00b67a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b67a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6f20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd6f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67a20 bytes 607e04f9
+ 00bd6f20 bytes 600204f9
- 00b679fc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6efc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b679fc bytes d32900d0
+ 00bd6efc bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d3e24e2273846bda2545e7f37ff580"></a>

### [`00b67a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a34.md) → [`00bd6f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f34.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6f64",
      "incomplete_value": true,
      "site": "00bd6f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a64",
      "incomplete_value": true,
      "site": "00b67a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd6f48",
      "incomplete_value": true,
      "site": "00bd6f48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a48",
      "incomplete_value": true,
      "site": "00b67a48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6f50",
      "incomplete_value": false,
      "site": "00bd6f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a50",
      "incomplete_value": false,
      "site": "00b67a5c",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6f44",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f50",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd6f64",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6f44",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f50",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd6f64",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a34.md#insn-00b67a5c) · [`00b67a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a34.md#insn-00b67a64) · [`00b67a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a34.md#insn-00b67a40)
- 新版 `00bd6f5c`（命令位置の公開資料なし） · `00bd6f64`（命令位置の公開資料なし） · `00bd6f40`（命令位置の公開資料なし）

~~~diff
- 00b67a5c ["INT_ADD", "register:40f0:8", ["const:b67a5c:8", "const:4:8"]]
- 00b67a5c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd6f5c ["INT_ADD", "register:40f0:8", ["const:bd6f5c:8", "const:4:8"]]
+ 00bd6f5c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67a5c bytes 8dd90194
+ 00bd6f5c bytes ed0e0294
- 00b67a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b67a64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6f64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd6f64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67a64 bytes 607e04f9
+ 00bd6f64 bytes 600204f9
- 00b67a40 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd6f40 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67a40 bytes d32900d0
+ 00bd6f40 bytes 932a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f39fc9e085a2967b1890df62983d79b"></a>

### [`00b67a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a84.md) → [`00bd6f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f84.md) _ZN8firebase4auth21oauthprovider_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd6fdc",
      "incomplete_value": true,
      "site": "00bd6fdc",
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
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67adc",
      "incomplete_value": true,
      "site": "00b67adc",
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
            "const:900:8"
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
      "definition_site": "00bd6fb8",
      "incomplete_value": true,
      "site": "00bd6fc4",
      "value": [
        "LOAD",
        "8",
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
                "const:800:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ab8",
      "incomplete_value": true,
      "site": "00b67ac4",
      "value": [
        "LOAD",
        "8",
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
                "const:8f8:8"
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
      "00bd6f98",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6fb8",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6fdc",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6f98",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6fb8",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6fdc",
      "WRITE",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a84.md#insn-00b67ac4) · [`00b67adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a84.md#insn-00b67adc) · [`00b67a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a84.md#insn-00b67a94)
- 新版 `00bd6fc4`（命令位置の公開資料なし） · `00bd6fdc`（命令位置の公開資料なし） · `00bd6f94`（命令位置の公開資料なし）

~~~diff
- 00b67ac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67ac4 ["INT_ADD", "register:40f0:8", ["const:b67ac4:8", "const:4:8"]]
- 00b67ac4 ["CALLIND", null, ["register:0:8"]]
+ 00bd6fc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6fc4 ["INT_ADD", "register:40f0:8", ["const:bd6fc4:8", "const:4:8"]]
+ 00bd6fc4 ["CALLIND", null, ["register:0:8"]]
- 00b67ac4 bytes 00013fd6
+ 00bd6fc4 bytes 00013fd6
- 00b67adc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67adc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:900:8"]]
- 00b67adc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd6fdc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd6fdc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:808:8"]]
+ 00bd6fdc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67adc bytes a0022439
+ 00bd6fdc bytes a0222039
- 00b67a94 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd6f94 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b67a94 bytes d52900d0
+ 00bd6f94 bytes 952a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6c3497c85135acb8ade15a8f14f7d09"></a>

### [`00b67af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67af0.md) → [`00bd6ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ff0.md) _ZN8firebase4auth21oauthprovider_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd702c",
      "incomplete_value": true,
      "site": "00bd702c",
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
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b2c",
      "incomplete_value": true,
      "site": "00b67b2c",
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
            "const:900:8"
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
      "definition_site": "00bd704c",
      "incomplete_value": true,
      "site": "00bd704c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b4c",
      "incomplete_value": true,
      "site": "00b67b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd7008",
      "incomplete_value": true,
      "site": "00bd7008",
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
      "definition_site": "00b67b08",
      "incomplete_value": true,
      "site": "00b67b08",
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
      "00bd7004",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7010",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd702c",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7004",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7010",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd702c",
      "WRITE",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67af0.md#insn-00b67b2c) · [`00b67b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67af0.md#insn-00b67b48) · [`00b67b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67af0.md#insn-00b67b4c)
- 新版 `00bd702c`（命令位置の公開資料なし） · `00bd7048`（命令位置の公開資料なし） · `00bd704c`（命令位置の公開資料なし）

~~~diff
- 00b67b2c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67b2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67b2c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
- 00b67b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd702c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd702c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd702c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:808:8"]]
+ 00bd702c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67b2c bytes bf022439
+ 00bd702c bytes bf222039
- 00b67b48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67b48 ["INT_ADD", "register:40f0:8", ["const:b67b48:8", "const:4:8"]]
- 00b67b48 ["CALLIND", null, ["register:0:8"]]
+ 00bd7048 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7048 ["INT_ADD", "register:40f0:8", ["const:bd7048:8", "const:4:8"]]
+ 00bd7048 ["CALLIND", null, ["register:0:8"]]
- 00b67b48 bytes 00013fd6
+ 00bd7048 bytes 00013fd6
- 00b67b4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b67b4c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b67b4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd704c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd704c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd704c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b67b4c bytes 9f7e04f9
+ 00bd704c bytes 9f0204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be309268179e0156c8fe3e9595f954be"></a>

### [`00b67b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67b60.md) → [`00bd7060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7060.md) _ZN8firebase4auth21oauthprovider_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd70a0",
      "incomplete_value": true,
      "site": "00bd70a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ba0",
      "incomplete_value": true,
      "site": "00b67ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd707c",
      "incomplete_value": true,
      "site": "00bd707c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b7c",
      "incomplete_value": true,
      "site": "00b67b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7084",
      "incomplete_value": false,
      "site": "00bd7098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b84",
      "incomplete_value": false,
      "site": "00b67b98",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7074",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7084",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd70a0",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7074",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7084",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd70a0",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67b60.md#insn-00b67b98) · [`00b67ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67b60.md#insn-00b67ba0) · [`00b67b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67b60.md#insn-00b67b6c)
- 新版 `00bd7098`（命令位置の公開資料なし） · `00bd70a0`（命令位置の公開資料なし） · `00bd706c`（命令位置の公開資料なし）

~~~diff
- 00b67b98 ["INT_ADD", "register:40f0:8", ["const:b67b98:8", "const:4:8"]]
- 00b67b98 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7098 ["INT_ADD", "register:40f0:8", ["const:bd7098:8", "const:4:8"]]
+ 00bd7098 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67b98 bytes 3ed90194
+ 00bd7098 bytes 9e0e0294
- 00b67ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b67ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd70a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd70a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ba0 bytes 807e04f9
+ 00bd70a0 bytes 800204f9
- 00b67b6c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd706c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67b6c bytes d42900d0
+ 00bd706c bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c524b05e03bae93288811bef8fbcb7"></a>

### [`00b67bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67bd0.md) → [`00bd70d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd70d0.md) _ZN8firebase4auth21oauthprovider_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd70ec",
      "incomplete_value": false,
      "site": "00bd70f0",
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
      "definition_site": "00b67bec",
      "incomplete_value": false,
      "site": "00b67bf0",
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
      "definition_site": "00bd70fc",
      "incomplete_value": true,
      "site": "00bd7108",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67bfc",
      "incomplete_value": true,
      "site": "00b67c08",
      "value": [
        "LOAD",
        "8",
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
      "00bd70ec",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd70fc",
      "DATA",
      [
        "storage",
        "010a1908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd70ec",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd70fc",
      "DATA",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67bd0.md#insn-00b67bf0) · [`00b67be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67bd0.md#insn-00b67be8) · [`00b67bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67bd0.md#insn-00b67bec)
- 新版 `00bd70f0`（命令位置の公開資料なし） · `00bd70e8`（命令位置の公開資料なし） · `00bd70ec`（命令位置の公開資料なし）

~~~diff
- 00b67bf0 ["INT_ADD", "register:40f0:8", ["const:b67bf0:8", "const:4:8"]]
- 00b67bf0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd70f0 ["INT_ADD", "register:40f0:8", ["const:bd70f0:8", "const:4:8"]]
+ 00bd70f0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67bf0 bytes 64d90194
+ 00bd70f0 bytes c40e0294
- 00b67be8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd70e8 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b67be8 bytes 80b9ffb0
+ 00bd70e8 bytes 80b6ffb0
- 00b67bec ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67bec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67bec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67bec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd70ec ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd70ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd70ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd70ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67bec bytes 001c1591
+ 00bd70ec bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bd187db56d3123e876e9806abd44a59"></a>

### [`00b67c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c0c.md) → [`00bd710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd710c.md) _ZN8firebase4auth21oauthprovider_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd714c",
      "incomplete_value": true,
      "site": "00bd714c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c4c",
      "incomplete_value": true,
      "site": "00b67c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "00bd7128",
      "incomplete_value": true,
      "site": "00bd7128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c28",
      "incomplete_value": true,
      "site": "00b67c28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7130",
      "incomplete_value": false,
      "site": "00bd7144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c30",
      "incomplete_value": false,
      "site": "00b67c44",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7120",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7130",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00bd714c",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7120",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7130",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd714c",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c0c.md#insn-00b67c44) · [`00b67c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c0c.md#insn-00b67c4c) · [`00b67c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c0c.md#insn-00b67c18)
- 新版 `00bd7144`（命令位置の公開資料なし） · `00bd714c`（命令位置の公開資料なし） · `00bd7118`（命令位置の公開資料なし）

~~~diff
- 00b67c44 ["INT_ADD", "register:40f0:8", ["const:b67c44:8", "const:4:8"]]
- 00b67c44 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7144 ["INT_ADD", "register:40f0:8", ["const:bd7144:8", "const:4:8"]]
+ 00bd7144 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67c44 bytes 13d90194
+ 00bd7144 bytes 730e0294
- 00b67c4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b67c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd714c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd714c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67c4c bytes 807e04f9
+ 00bd714c bytes 800204f9
- 00b67c18 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd7118 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67c18 bytes d42900d0
+ 00bd7118 bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf23a7f55d1238c250d09260bef8828"></a>

### [`00b67c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c7c.md) → [`00bd717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd717c.md) _ZN8firebase4auth21oauthprovider_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd7198",
      "incomplete_value": false,
      "site": "00bd719c",
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
      "definition_site": "00b67c98",
      "incomplete_value": false,
      "site": "00b67c9c",
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
      "definition_site": "00bd71a8",
      "incomplete_value": true,
      "site": "00bd71b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67ca8",
      "incomplete_value": true,
      "site": "00b67cb4",
      "value": [
        "LOAD",
        "8",
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
      "00bd7198",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd71a8",
      "DATA",
      [
        "storage",
        "010a1920",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7198",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd71a8",
      "DATA",
      [
        "storage",
        "01126828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c7c.md#insn-00b67c9c) · [`00b67c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c7c.md#insn-00b67c94) · [`00b67c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c7c.md#insn-00b67c98)
- 新版 `00bd719c`（命令位置の公開資料なし） · `00bd7194`（命令位置の公開資料なし） · `00bd7198`（命令位置の公開資料なし）

~~~diff
- 00b67c9c ["INT_ADD", "register:40f0:8", ["const:b67c9c:8", "const:4:8"]]
- 00b67c9c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd719c ["INT_ADD", "register:40f0:8", ["const:bd719c:8", "const:4:8"]]
+ 00bd719c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67c9c bytes 39d90194
+ 00bd719c bytes 990e0294
- 00b67c94 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd7194 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b67c94 bytes 80b9ffd0
+ 00bd7194 bytes 80b6ffd0
- 00b67c98 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67c98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67c98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67c98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7198 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd7198 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7198 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7198 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67c98 bytes 00c81791
+ 00bd7198 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e93c8eaa8ec609bc3eb122b47844c2"></a>

### [`00b67cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cb8.md) → [`00bd71b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71b8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bd71e4",
      "incomplete_value": true,
      "site": "00bd71e4",
      "value": [
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
      "definition_site": "00b67ce4",
      "incomplete_value": true,
      "site": "00b67ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "definition_site": "00bd71cc",
      "incomplete_value": true,
      "site": "00bd71cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ccc",
      "incomplete_value": true,
      "site": "00b67ccc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd71d8",
      "incomplete_value": false,
      "site": "00bd71dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67cd8",
      "incomplete_value": false,
      "site": "00b67cdc",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd71c8",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd71d8",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd71e4",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd71c8",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd71d8",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd71e4",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cb8.md#insn-00b67cdc) · [`00b67ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cb8.md#insn-00b67ce4) · [`00b67cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cb8.md#insn-00b67cc4)
- 新版 `00bd71dc`（命令位置の公開資料なし） · `00bd71e4`（命令位置の公開資料なし） · `00bd71c4`（命令位置の公開資料なし）

~~~diff
- 00b67cdc ["INT_ADD", "register:40f0:8", ["const:b67cdc:8", "const:4:8"]]
- 00b67cdc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd71dc ["INT_ADD", "register:40f0:8", ["const:bd71dc:8", "const:4:8"]]
+ 00bd71dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67cdc bytes edd80194
+ 00bd71dc bytes 4d0e0294
- 00b67ce4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
- 00b67ce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd71e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00bd71e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ce4 bytes 609604f9
+ 00bd71e4 bytes 601a04f9
- 00b67cc4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd71c4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67cc4 bytes d32900d0
+ 00bd71c4 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa900bc38644293986053af3d1682a37"></a>

### [`00b67cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cf8.md) → [`00bd71f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71f8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bd7224",
      "incomplete_value": true,
      "site": "00bd7224",
      "value": [
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
            "const:928:8"
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
      "definition_site": "00bd720c",
      "incomplete_value": true,
      "site": "00bd720c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d0c",
      "incomplete_value": true,
      "site": "00b67d0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7214",
      "incomplete_value": false,
      "site": "00bd721c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7208",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7214",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd7224",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7208",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7214",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd7224",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cf8.md#insn-00b67d1c) · [`00b67d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cf8.md#insn-00b67d24) · [`00b67d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cf8.md#insn-00b67d04)
- 新版 `00bd721c`（命令位置の公開資料なし） · `00bd7224`（命令位置の公開資料なし） · `00bd7204`（命令位置の公開資料なし）

~~~diff
- 00b67d1c ["INT_ADD", "register:40f0:8", ["const:b67d1c:8", "const:4:8"]]
- 00b67d1c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd721c ["INT_ADD", "register:40f0:8", ["const:bd721c:8", "const:4:8"]]
+ 00bd721c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67d1c bytes ddd80194
+ 00bd721c bytes 3d0e0294
- 00b67d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
- 00b67d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00bd7224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67d24 bytes 609604f9
+ 00bd7224 bytes 601a04f9
- 00b67d04 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7204 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67d04 bytes d32900d0
+ 00bd7204 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1752920345d05d933418d6ceaf864f"></a>

### [`00b67d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d38.md) → [`00bd7238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7238.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7268",
      "incomplete_value": true,
      "site": "00bd7268",
      "value": [
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
            "const:928:8"
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
      "definition_site": "00bd724c",
      "incomplete_value": true,
      "site": "00bd724c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7258",
      "incomplete_value": false,
      "site": "00bd7260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d58",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7248",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7258",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd7268",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7248",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7258",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd7268",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d38.md#insn-00b67d60) · [`00b67d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d38.md#insn-00b67d68) · [`00b67d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d38.md#insn-00b67d44)
- 新版 `00bd7260`（命令位置の公開資料なし） · `00bd7268`（命令位置の公開資料なし） · `00bd7244`（命令位置の公開資料なし）

~~~diff
- 00b67d60 ["INT_ADD", "register:40f0:8", ["const:b67d60:8", "const:4:8"]]
- 00b67d60 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7260 ["INT_ADD", "register:40f0:8", ["const:bd7260:8", "const:4:8"]]
+ 00bd7260 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67d60 bytes ccd80194
+ 00bd7260 bytes 2c0e0294
- 00b67d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
- 00b67d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00bd7268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67d68 bytes 609604f9
+ 00bd7268 bytes 601a04f9
- 00b67d44 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7244 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67d44 bytes d32900d0
+ 00bd7244 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d769182364cbd3c8eb74ef609202e50b"></a>

### [`00b67d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d7c.md) → [`00bd727c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd727c.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd72ac",
      "incomplete_value": true,
      "site": "00bd72ac",
      "value": [
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
      "definition_site": "00b67dac",
      "incomplete_value": true,
      "site": "00b67dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "definition_site": "00bd7290",
      "incomplete_value": true,
      "site": "00bd7290",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d90",
      "incomplete_value": true,
      "site": "00b67d90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7298",
      "incomplete_value": false,
      "site": "00bd72a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d98",
      "incomplete_value": false,
      "site": "00b67da4",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd728c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7298",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd72ac",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd728c",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7298",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd72ac",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d7c.md#insn-00b67da4) · [`00b67dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d7c.md#insn-00b67dac) · [`00b67d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d7c.md#insn-00b67d88)
- 新版 `00bd72a4`（命令位置の公開資料なし） · `00bd72ac`（命令位置の公開資料なし） · `00bd7288`（命令位置の公開資料なし）

~~~diff
- 00b67da4 ["INT_ADD", "register:40f0:8", ["const:b67da4:8", "const:4:8"]]
- 00b67da4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd72a4 ["INT_ADD", "register:40f0:8", ["const:bd72a4:8", "const:4:8"]]
+ 00bd72a4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67da4 bytes bbd80194
+ 00bd72a4 bytes 1b0e0294
- 00b67dac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
- 00b67dac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00bd72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67dac bytes 609604f9
+ 00bd72ac bytes 601a04f9
- 00b67d88 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7288 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b67d88 bytes d32900d0
+ 00bd7288 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7a31e1f53d156fa82ef1de2796e0ea5"></a>

### [`00b67dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67dcc.md) → [`00bd72cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd72cc.md) _ZN8firebase4auth31oauthprovider_credentialbuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd7324",
      "incomplete_value": true,
      "site": "00bd7324",
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
      "definition_site": "00b67e24",
      "incomplete_value": true,
      "site": "00b67e24",
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
            "const:930:8"
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
      "definition_site": "00bd7300",
      "incomplete_value": true,
      "site": "00bd730c",
      "value": [
        "LOAD",
        "8",
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e00",
      "incomplete_value": true,
      "site": "00b67e0c",
      "value": [
        "LOAD",
        "8",
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
                "const:928:8"
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
      "00bd72e0",
      "READ",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7300",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7324",
      "WRITE",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd72e0",
      "READ",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7300",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7324",
      "WRITE",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67dcc.md#insn-00b67e0c) · [`00b67e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67dcc.md#insn-00b67e24) · [`00b67ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67dcc.md#insn-00b67ddc)
- 新版 `00bd730c`（命令位置の公開資料なし） · `00bd7324`（命令位置の公開資料なし） · `00bd72dc`（命令位置の公開資料なし）

~~~diff
- 00b67e0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67e0c ["INT_ADD", "register:40f0:8", ["const:b67e0c:8", "const:4:8"]]
- 00b67e0c ["CALLIND", null, ["register:0:8"]]
+ 00bd730c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd730c ["INT_ADD", "register:40f0:8", ["const:bd730c:8", "const:4:8"]]
+ 00bd730c ["CALLIND", null, ["register:0:8"]]
- 00b67e0c bytes 00013fd6
+ 00bd730c bytes 00013fd6
- 00b67e24 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67e24 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:930:8"]]
- 00b67e24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd7324 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd7324 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
+ 00bd7324 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67e24 bytes a0c22439
+ 00bd7324 bytes a0e22039
- 00b67ddc ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd72dc ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b67ddc bytes d52900d0
+ 00bd72dc bytes 752a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a152f9f318e0f736168c1fdfdf30a5"></a>

### [`00b67e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67e38.md) → [`00bd7338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7338.md) _ZN8firebase4auth31oauthprovider_credentialbuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd7374",
      "incomplete_value": true,
      "site": "00bd7374",
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
      "definition_site": "00b67e74",
      "incomplete_value": true,
      "site": "00b67e74",
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
            "const:930:8"
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
      "definition_site": "00bd7394",
      "incomplete_value": true,
      "site": "00bd7394",
      "value": [
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
      "definition_site": "00b67e94",
      "incomplete_value": true,
      "site": "00b67e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "definition_site": "00bd7350",
      "incomplete_value": true,
      "site": "00bd7350",
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
      "definition_site": "00b67e50",
      "incomplete_value": true,
      "site": "00b67e50",
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
      "00bd734c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7358",
      "READ",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7374",
      "WRITE",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd734c",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7358",
      "READ",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7374",
      "WRITE",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67e38.md#insn-00b67e74) · [`00b67e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67e38.md#insn-00b67e90) · [`00b67e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67e38.md#insn-00b67e94)
- 新版 `00bd7374`（命令位置の公開資料なし） · `00bd7390`（命令位置の公開資料なし） · `00bd7394`（命令位置の公開資料なし）

~~~diff
- 00b67e74 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67e74 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67e74 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:930:8"]]
- 00b67e74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd7374 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd7374 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd7374 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
+ 00bd7374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67e74 bytes bfc22439
+ 00bd7374 bytes bfe22039
- 00b67e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67e90 ["INT_ADD", "register:40f0:8", ["const:b67e90:8", "const:4:8"]]
- 00b67e90 ["CALLIND", null, ["register:0:8"]]
+ 00bd7390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7390 ["INT_ADD", "register:40f0:8", ["const:bd7390:8", "const:4:8"]]
+ 00bd7390 ["CALLIND", null, ["register:0:8"]]
- 00b67e90 bytes 00013fd6
+ 00bd7390 bytes 00013fd6
- 00b67e94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
- 00b67e94 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b67e94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd7394 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00bd7394 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd7394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b67e94 bytes 9f9604f9
+ 00bd7394 bytes 9f1a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa8a2bc682a8d501a991dc412400195c"></a>

### [`00b67ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67ea8.md) → [`00bd73a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd73a8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd73e8",
      "incomplete_value": true,
      "site": "00bd73e8",
      "value": [
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
      "definition_site": "00b67ee8",
      "incomplete_value": true,
      "site": "00b67ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "definition_site": "00bd73c4",
      "incomplete_value": true,
      "site": "00bd73c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ec4",
      "incomplete_value": true,
      "site": "00b67ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd73cc",
      "incomplete_value": false,
      "site": "00bd73e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ecc",
      "incomplete_value": false,
      "site": "00b67ee0",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd73bc",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd73cc",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd73e8",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd73bc",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd73cc",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd73e8",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67ea8.md#insn-00b67ee0) · [`00b67ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67ea8.md#insn-00b67ee8) · [`00b67eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67ea8.md#insn-00b67eb4)
- 新版 `00bd73e0`（命令位置の公開資料なし） · `00bd73e8`（命令位置の公開資料なし） · `00bd73b4`（命令位置の公開資料なし）

~~~diff
- 00b67ee0 ["INT_ADD", "register:40f0:8", ["const:b67ee0:8", "const:4:8"]]
- 00b67ee0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd73e0 ["INT_ADD", "register:40f0:8", ["const:bd73e0:8", "const:4:8"]]
+ 00bd73e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67ee0 bytes 6cd80194
+ 00bd73e0 bytes cc0d0294
- 00b67ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
- 00b67ee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd73e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00bd73e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ee8 bytes 809604f9
+ 00bd73e8 bytes 801a04f9
- 00b67eb4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd73b4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67eb4 bytes d42900d0
+ 00bd73b4 bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ec1825a0551d68f8841ae352a794665"></a>

### [`00b67f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f18.md) → [`00bd7418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7418.md) _ZN8firebase4auth31oauthprovider_credentialbuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd7434",
      "incomplete_value": false,
      "site": "00bd7438",
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
      "definition_site": "00b67f34",
      "incomplete_value": false,
      "site": "00b67f38",
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
      "definition_site": "00bd7444",
      "incomplete_value": true,
      "site": "00bd7450",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67f44",
      "incomplete_value": true,
      "site": "00b67f50",
      "value": [
        "LOAD",
        "8",
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
      "00bd7434",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd7444",
      "DATA",
      [
        "storage",
        "010a1938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7434",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd7444",
      "DATA",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f18.md#insn-00b67f38) · [`00b67f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f18.md#insn-00b67f30) · [`00b67f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f18.md#insn-00b67f34)
- 新版 `00bd7438`（命令位置の公開資料なし） · `00bd7430`（命令位置の公開資料なし） · `00bd7434`（命令位置の公開資料なし）

~~~diff
- 00b67f38 ["INT_ADD", "register:40f0:8", ["const:b67f38:8", "const:4:8"]]
- 00b67f38 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd7438 ["INT_ADD", "register:40f0:8", ["const:bd7438:8", "const:4:8"]]
+ 00bd7438 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67f38 bytes 92d80194
+ 00bd7438 bytes f20d0294
- 00b67f30 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd7430 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b67f30 bytes 80b9ffb0
+ 00bd7430 bytes 80b6ffb0
- 00b67f34 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7434 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd7434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67f34 bytes 001c1591
+ 00bd7434 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4046e81fd2cd6e6fe1b20fe86197a0bb"></a>

### [`00b67f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f54.md) → [`00bd7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7454.md) _ZN8firebase4auth31oauthprovider_credentialbuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7494",
      "incomplete_value": true,
      "site": "00bd7494",
      "value": [
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
      "definition_site": "00b67f94",
      "incomplete_value": true,
      "site": "00b67f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "definition_site": "00bd7470",
      "incomplete_value": true,
      "site": "00bd7470",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f70",
      "incomplete_value": true,
      "site": "00b67f70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7478",
      "incomplete_value": false,
      "site": "00bd748c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f78",
      "incomplete_value": false,
      "site": "00b67f8c",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7468",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7478",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00bd7494",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7468",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7478",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd7494",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f54.md#insn-00b67f8c) · [`00b67f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f54.md#insn-00b67f94) · [`00b67f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f54.md#insn-00b67f60)
- 新版 `00bd748c`（命令位置の公開資料なし） · `00bd7494`（命令位置の公開資料なし） · `00bd7460`（命令位置の公開資料なし）

~~~diff
- 00b67f8c ["INT_ADD", "register:40f0:8", ["const:b67f8c:8", "const:4:8"]]
- 00b67f8c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd748c ["INT_ADD", "register:40f0:8", ["const:bd748c:8", "const:4:8"]]
+ 00bd748c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b67f8c bytes 41d80194
+ 00bd748c bytes a10d0294
- 00b67f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
- 00b67f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00bd7494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67f94 bytes 809604f9
+ 00bd7494 bytes 801a04f9
- 00b67f60 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd7460 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67f60 bytes d42900d0
+ 00bd7460 bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e848447fe43fdac4c2e0f164797c839"></a>

### [`00b67fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67fc4.md) → [`00bd74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd74c4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd74e0",
      "incomplete_value": false,
      "site": "00bd74e4",
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
      "definition_site": "00b67fe0",
      "incomplete_value": false,
      "site": "00b67fe4",
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
      "definition_site": "00bd74f0",
      "incomplete_value": true,
      "site": "00bd74fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67ff0",
      "incomplete_value": true,
      "site": "00b67ffc",
      "value": [
        "LOAD",
        "8",
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
      "00bd74e0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd74f0",
      "DATA",
      [
        "storage",
        "010a1958",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd74e0",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd74f0",
      "DATA",
      [
        "storage",
        "01126860",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67fc4.md#insn-00b67fe4) · [`00b67fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67fc4.md#insn-00b67fdc) · [`00b67fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67fc4.md#insn-00b67fe0)
- 新版 `00bd74e4`（命令位置の公開資料なし） · `00bd74dc`（命令位置の公開資料なし） · `00bd74e0`（命令位置の公開資料なし）

~~~diff
- 00b67fe4 ["INT_ADD", "register:40f0:8", ["const:b67fe4:8", "const:4:8"]]
- 00b67fe4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd74e4 ["INT_ADD", "register:40f0:8", ["const:bd74e4:8", "const:4:8"]]
+ 00bd74e4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b67fe4 bytes 67d80194
+ 00bd74e4 bytes c70d0294
- 00b67fdc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd74dc ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b67fdc bytes 80b9ffd0
+ 00bd74dc bytes 80b6ffd0
- 00b67fe0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd74e0 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd74e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd74e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd74e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67fe0 bytes 00c81791
+ 00bd74e0 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267563c71bd4b5726aa53baf11da74e5"></a>

### [`00b68000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68000.md) → [`00bd7500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7500.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bd752c",
      "incomplete_value": true,
      "site": "00bd752c",
      "value": [
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
    "old": {
      "definition_site": "00b6802c",
      "incomplete_value": true,
      "site": "00b6802c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00bd7514",
      "incomplete_value": true,
      "site": "00bd7514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68014",
      "incomplete_value": true,
      "site": "00b68014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7520",
      "incomplete_value": false,
      "site": "00bd7524",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68020",
      "incomplete_value": false,
      "site": "00b68024",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7510",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7520",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bd752c",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7510",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7520",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd752c",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68000.md#insn-00b68024) · [`00b6802c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68000.md#insn-00b6802c) · [`00b6800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68000.md#insn-00b6800c)
- 新版 `00bd7524`（命令位置の公開資料なし） · `00bd752c`（命令位置の公開資料なし） · `00bd750c`（命令位置の公開資料なし）

~~~diff
- 00b68024 ["INT_ADD", "register:40f0:8", ["const:b68024:8", "const:4:8"]]
- 00b68024 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7524 ["INT_ADD", "register:40f0:8", ["const:bd7524:8", "const:4:8"]]
+ 00bd7524 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68024 bytes 1bd80194
+ 00bd7524 bytes 7b0d0294
- 00b6802c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b6802c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd752c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00bd752c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6802c bytes 60b204f9
+ 00bd752c bytes 603604f9
- 00b6800c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd750c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6800c bytes d32900b0
+ 00bd750c bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2855f5c82d7ce0435aafa1e6d2eda1"></a>

### [`00b68040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68040.md) → [`00bd7540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7540.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd756c",
      "incomplete_value": true,
      "site": "00bd756c",
      "value": [
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
    "old": {
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
            "const:960:8"
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
      "definition_site": "00bd7554",
      "incomplete_value": true,
      "site": "00bd7554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68054",
      "incomplete_value": true,
      "site": "00b68054",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd755c",
      "incomplete_value": false,
      "site": "00bd7564",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7550",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd755c",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bd756c",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7550",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd755c",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd756c",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68040.md#insn-00b68064) · [`00b6806c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68040.md#insn-00b6806c) · [`00b6804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68040.md#insn-00b6804c)
- 新版 `00bd7564`（命令位置の公開資料なし） · `00bd756c`（命令位置の公開資料なし） · `00bd754c`（命令位置の公開資料なし）

~~~diff
- 00b68064 ["INT_ADD", "register:40f0:8", ["const:b68064:8", "const:4:8"]]
- 00b68064 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7564 ["INT_ADD", "register:40f0:8", ["const:bd7564:8", "const:4:8"]]
+ 00bd7564 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68064 bytes 0bd80194
+ 00bd7564 bytes 6b0d0294
- 00b6806c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b6806c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd756c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00bd756c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6806c bytes 60b204f9
+ 00bd756c bytes 603604f9
- 00b6804c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd754c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6804c bytes d32900b0
+ 00bd754c bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ac46385a1ef24f7e4fe7927ecc48f0"></a>

### [`00b68080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68080.md) → [`00bd7580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7580.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b680b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd75b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7594",
      "incomplete_value": true,
      "site": "00bd7594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7590",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b680b4"
      ]
    ],
    [
      "unmatched:00b680a0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7590",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd75b4"
      ]
    ],
    [
      "00bd75a0",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b680a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68080.md#insn-00b680a8) · [`00b680b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68080.md#insn-00b680b0) · [`00b680c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68080.md#insn-00b680c0)

~~~diff
- 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
- 00b680a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b680a8 bytes fad70194
- 00b680b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b680b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b680b0 bytes 60b204f9
- 00b680c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b680c0 ["RETURN", null, ["register:0:8"]]
- 00b680c0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44c1b7daee2c583586e851b17441fbaf"></a>

### [`00b680c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b680c4.md) → [`00bd75c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd75c4.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd75f4",
      "incomplete_value": true,
      "site": "00bd75f4",
      "value": [
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
    "old": {
      "definition_site": "00b680f4",
      "incomplete_value": true,
      "site": "00b680f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00bd75d8",
      "incomplete_value": true,
      "site": "00bd75d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b680d8",
      "incomplete_value": true,
      "site": "00b680d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd75e0",
      "incomplete_value": false,
      "site": "00bd75ec",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b680e0",
      "incomplete_value": false,
      "site": "00b680ec",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd75d4",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd75e0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bd75f4",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd75d4",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd75e0",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd75f4",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b680ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b680c4.md#insn-00b680ec) · [`00b680f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b680c4.md#insn-00b680f4) · [`00b680d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b680c4.md#insn-00b680d0)
- 新版 `00bd75ec`（命令位置の公開資料なし） · `00bd75f4`（命令位置の公開資料なし） · `00bd75d0`（命令位置の公開資料なし）

~~~diff
- 00b680ec ["INT_ADD", "register:40f0:8", ["const:b680ec:8", "const:4:8"]]
- 00b680ec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd75ec ["INT_ADD", "register:40f0:8", ["const:bd75ec:8", "const:4:8"]]
+ 00bd75ec ["CALL", null, ["callee:00c5ab10:8"]]
- 00b680ec bytes e9d70194
+ 00bd75ec bytes 490d0294
- 00b680f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b680f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd75f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00bd75f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b680f4 bytes 60b204f9
+ 00bd75f4 bytes 603604f9
- 00b680d0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd75d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b680d0 bytes d32900b0
+ 00bd75d0 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7a23b77f288410efdcc38e1319b22f"></a>

### [`00b68114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68114.md) → [`00bd7614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7614.md) _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68114",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68118",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6811c",
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
      "00bd7614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd7618",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd761c",
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

- 旧版 [`00b68114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68114.md#insn-00b68114) · [`00b68118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68114.md#insn-00b68118) · [`00b6811c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68114.md#insn-00b6811c)

~~~diff
- 00b68114 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b68114 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b68114 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b68114 bytes f50f1df8
- 00b68118 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b68118 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b68118 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b68118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b68118 bytes f44f01a9
- 00b6811c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6811c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6811c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6811c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6811c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-910676e0af9f67f379d053a7f130805f"></a>

### [`00b68180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68180.md) → [`00bd7680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7680.md) _ZN8firebase4auth8auth_idp12ReleaseClassEP7_JNIEnv

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
      "site": "00b681bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b681dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd76bc"
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
      "00bd7694",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd76a0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd76a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b681c0"
      ]
    ]
  ],
  "added": [
    [
      "00bd7694",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd76a0",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd76a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd76c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68180.md#insn-00b68198) · [`00b681bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68180.md#insn-00b681bc) · [`00b681c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68180.md#insn-00b681c4)
- 新版 `00bd7698`（命令位置の公開資料なし）

~~~diff
- 00b68198 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b68198 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd7698 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd7698 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b68198 bytes 410200b4
+ 00bd7698 bytes 410200b4
- 00b681bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b681bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b681bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
- 00b681bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b681bc bytes bfa22539
- 00b681c4 ["INT_ADD", "register:40f0:8", ["const:b681c4:8", "const:4:8"]]
- 00b681c4 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b681c4 bytes c7d70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1aca07bafa378af01bdeee55a332ec2"></a>

### [`00b681f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b681f0.md) → [`00bd76f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd76f0.md) _ZN8firebase4auth8auth_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7730",
      "incomplete_value": true,
      "site": "00bd7730",
      "value": [
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
    "old": {
      "definition_site": "00b68230",
      "incomplete_value": true,
      "site": "00b68230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00bd770c",
      "incomplete_value": true,
      "site": "00bd770c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6820c",
      "incomplete_value": true,
      "site": "00b6820c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7714",
      "incomplete_value": false,
      "site": "00bd7728",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68214",
      "incomplete_value": false,
      "site": "00b68228",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7704",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7714",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bd7730",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7704",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7714",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd7730",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b681f0.md#insn-00b68228) · [`00b68230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b681f0.md#insn-00b68230) · [`00b681fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b681f0.md#insn-00b681fc)
- 新版 `00bd7728`（命令位置の公開資料なし） · `00bd7730`（命令位置の公開資料なし） · `00bd76fc`（命令位置の公開資料なし）

~~~diff
- 00b68228 ["INT_ADD", "register:40f0:8", ["const:b68228:8", "const:4:8"]]
- 00b68228 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7728 ["INT_ADD", "register:40f0:8", ["const:bd7728:8", "const:4:8"]]
+ 00bd7728 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68228 bytes 9ad70194
+ 00bd7728 bytes fa0c0294
- 00b68230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b68230 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
+ 00bd7730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68230 bytes 80b204f9
+ 00bd7730 bytes 803604f9
- 00b681fc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd76fc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b681fc bytes d42900b0
+ 00bd76fc bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd35932399311a8e8205846846f575b4"></a>

### [`00b68260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68260.md) → [`00bd7760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7760.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd777c",
      "incomplete_value": false,
      "site": "00bd7780",
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
      "definition_site": "00b6827c",
      "incomplete_value": false,
      "site": "00b68280",
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
      "definition_site": "00bd778c",
      "incomplete_value": true,
      "site": "00bd7798",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6828c",
      "incomplete_value": true,
      "site": "00b68298",
      "value": [
        "LOAD",
        "8",
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
      "00bd777c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd778c",
      "DATA",
      [
        "storage",
        "010a1970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd777c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd778c",
      "DATA",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68260.md#insn-00b68280) · [`00b68278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68260.md#insn-00b68278) · [`00b6827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68260.md#insn-00b6827c)
- 新版 `00bd7780`（命令位置の公開資料なし） · `00bd7778`（命令位置の公開資料なし） · `00bd777c`（命令位置の公開資料なし）

~~~diff
- 00b68280 ["INT_ADD", "register:40f0:8", ["const:b68280:8", "const:4:8"]]
- 00b68280 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd7780 ["INT_ADD", "register:40f0:8", ["const:bd7780:8", "const:4:8"]]
+ 00bd7780 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b68280 bytes c0d70194
+ 00bd7780 bytes 200d0294
- 00b68278 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd7778 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b68278 bytes 80b9ff90
+ 00bd7778 bytes 80b6ffb0
- 00b6827c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6827c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6827c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6827c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd777c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd777c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd777c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd777c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6827c bytes 001c1591
+ 00bd777c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a98cdffead0895c5cb11bb0bff9060e"></a>

### [`00b6829c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6829c.md) → [`00bd779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd779c.md) _ZN8firebase4auth8auth_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd77dc",
      "incomplete_value": true,
      "site": "00bd77dc",
      "value": [
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
    "old": {
      "definition_site": "00b682dc",
      "incomplete_value": true,
      "site": "00b682dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00bd77b8",
      "incomplete_value": true,
      "site": "00bd77b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b682b8",
      "incomplete_value": true,
      "site": "00b682b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd77c0",
      "incomplete_value": false,
      "site": "00bd77d4",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b682c0",
      "incomplete_value": false,
      "site": "00b682d4",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd77b0",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd77c0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bd77dc",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd77b0",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd77c0",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd77dc",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b682d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6829c.md#insn-00b682d4) · [`00b682dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6829c.md#insn-00b682dc) · [`00b682a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6829c.md#insn-00b682a8)
- 新版 `00bd77d4`（命令位置の公開資料なし） · `00bd77dc`（命令位置の公開資料なし） · `00bd77a8`（命令位置の公開資料なし）

~~~diff
- 00b682d4 ["INT_ADD", "register:40f0:8", ["const:b682d4:8", "const:4:8"]]
- 00b682d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd77d4 ["INT_ADD", "register:40f0:8", ["const:bd77d4:8", "const:4:8"]]
+ 00bd77d4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b682d4 bytes 6fd70194
+ 00bd77d4 bytes cf0c0294
- 00b682dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b682dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd77dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
+ 00bd77dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b682dc bytes 80b204f9
+ 00bd77dc bytes 803604f9
- 00b682a8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd77a8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b682a8 bytes d42900b0
+ 00bd77a8 bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad11ecc043aa6eac8db2cbf117a97ed3"></a>

### [`00b6830c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6830c.md) → [`00bd780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd780c.md) _ZN8firebase4auth8auth_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd7828",
      "incomplete_value": false,
      "site": "00bd782c",
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
      "definition_site": "00b68328",
      "incomplete_value": false,
      "site": "00b6832c",
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
      "definition_site": "00bd7838",
      "incomplete_value": true,
      "site": "00bd7844",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68338",
      "incomplete_value": true,
      "site": "00b68344",
      "value": [
        "LOAD",
        "8",
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
      "00bd7828",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd7838",
      "DATA",
      [
        "storage",
        "010a1978",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7828",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd7838",
      "DATA",
      [
        "storage",
        "01126880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6832c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6830c.md#insn-00b6832c) · [`00b68324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6830c.md#insn-00b68324) · [`00b68328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6830c.md#insn-00b68328)
- 新版 `00bd782c`（命令位置の公開資料なし） · `00bd7824`（命令位置の公開資料なし） · `00bd7828`（命令位置の公開資料なし）

~~~diff
- 00b6832c ["INT_ADD", "register:40f0:8", ["const:b6832c:8", "const:4:8"]]
- 00b6832c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd782c ["INT_ADD", "register:40f0:8", ["const:bd782c:8", "const:4:8"]]
+ 00bd782c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6832c bytes 95d70194
+ 00bd782c bytes f50c0294
- 00b68324 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd7824 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b68324 bytes 80b9ffb0
+ 00bd7824 bytes 80b6ffd0
- 00b68328 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b68328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7828 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd7828 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7828 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7828 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68328 bytes 00c81791
+ 00bd7828 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba6bbbf8c256ece679e789eea582f767"></a>

### [`00b68348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68348.md) → [`00bd7848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7848.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bd7874",
      "incomplete_value": true,
      "site": "00bd7874",
      "value": [
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
      "definition_site": "00b68374",
      "incomplete_value": true,
      "site": "00b68374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00bd785c",
      "incomplete_value": true,
      "site": "00bd785c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6835c",
      "incomplete_value": true,
      "site": "00b6835c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7868",
      "incomplete_value": false,
      "site": "00bd786c",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68368",
      "incomplete_value": false,
      "site": "00b6836c",
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
      "00bd7858",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7868",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bd7874",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7858",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7868",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd7874",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6836c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68348.md#insn-00b6836c) · [`00b68374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68348.md#insn-00b68374) · [`00b68354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68348.md#insn-00b68354)
- 新版 `00bd786c`（命令位置の公開資料なし） · `00bd7874`（命令位置の公開資料なし） · `00bd7854`（命令位置の公開資料なし）

~~~diff
- 00b6836c ["INT_ADD", "register:40f0:8", ["const:b6836c:8", "const:4:8"]]
- 00b6836c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd786c ["INT_ADD", "register:40f0:8", ["const:bd786c:8", "const:4:8"]]
+ 00bd786c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6836c bytes 49d70194
+ 00bd786c bytes a90c0294
- 00b68374 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b68374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00bd7874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68374 bytes 60c204f9
+ 00bd7874 bytes 604604f9
- 00b68354 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7854 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68354 bytes d32900b0
+ 00bd7854 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e6f5ddefe0b36ecdb8704a9fc404d0"></a>

### [`00b68388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68388.md) → [`00bd7888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7888.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd78b4",
      "incomplete_value": true,
      "site": "00bd78b4",
      "value": [
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
            "const:980:8"
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
      "definition_site": "00bd789c",
      "incomplete_value": true,
      "site": "00bd789c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6839c",
      "incomplete_value": true,
      "site": "00b6839c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd78a4",
      "incomplete_value": false,
      "site": "00bd78ac",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7898",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78a4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bd78b4",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7898",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78a4",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd78b4",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68388.md#insn-00b683ac) · [`00b683b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68388.md#insn-00b683b4) · [`00b68394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68388.md#insn-00b68394)
- 新版 `00bd78ac`（命令位置の公開資料なし） · `00bd78b4`（命令位置の公開資料なし） · `00bd7894`（命令位置の公開資料なし）

~~~diff
- 00b683ac ["INT_ADD", "register:40f0:8", ["const:b683ac:8", "const:4:8"]]
- 00b683ac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd78ac ["INT_ADD", "register:40f0:8", ["const:bd78ac:8", "const:4:8"]]
+ 00bd78ac ["CALL", null, ["callee:00c5ab10:8"]]
- 00b683ac bytes 39d70194
+ 00bd78ac bytes 990c0294
- 00b683b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b683b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd78b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00bd78b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b683b4 bytes 60c204f9
+ 00bd78b4 bytes 604604f9
- 00b68394 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7894 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68394 bytes d32900b0
+ 00bd7894 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee50da9d1b84b0392b398dd91cb875ce"></a>

### [`00b683c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b683c8.md) → [`00bd78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd78c8.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd78f8",
      "incomplete_value": true,
      "site": "00bd78f8",
      "value": [
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
            "const:980:8"
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
      "definition_site": "00bd78dc",
      "incomplete_value": true,
      "site": "00bd78dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd78e8",
      "incomplete_value": false,
      "site": "00bd78f0",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683e8",
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
      "00bd78d8",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78e8",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bd78f8",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd78d8",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78e8",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd78f8",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b683c8.md#insn-00b683f0) · [`00b683f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b683c8.md#insn-00b683f8) · [`00b683d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b683c8.md#insn-00b683d4)
- 新版 `00bd78f0`（命令位置の公開資料なし） · `00bd78f8`（命令位置の公開資料なし） · `00bd78d4`（命令位置の公開資料なし）

~~~diff
- 00b683f0 ["INT_ADD", "register:40f0:8", ["const:b683f0:8", "const:4:8"]]
- 00b683f0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd78f0 ["INT_ADD", "register:40f0:8", ["const:bd78f0:8", "const:4:8"]]
+ 00bd78f0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b683f0 bytes 28d70194
+ 00bd78f0 bytes 880c0294
- 00b683f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b683f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd78f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00bd78f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b683f8 bytes 60c204f9
+ 00bd78f8 bytes 604604f9
- 00b683d4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd78d4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b683d4 bytes d32900b0
+ 00bd78d4 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512bf25ed8d45de3879696633ee79eaa"></a>

### [`00b6840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6840c.md) → [`00bd790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd790c.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd793c",
      "incomplete_value": true,
      "site": "00bd793c",
      "value": [
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
      "definition_site": "00b6843c",
      "incomplete_value": true,
      "site": "00b6843c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00bd7920",
      "incomplete_value": true,
      "site": "00bd7920",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68420",
      "incomplete_value": true,
      "site": "00b68420",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7928",
      "incomplete_value": false,
      "site": "00bd7934",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68428",
      "incomplete_value": false,
      "site": "00b68434",
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
      "00bd791c",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7928",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bd793c",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd791c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7928",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd793c",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6840c.md#insn-00b68434) · [`00b6843c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6840c.md#insn-00b6843c) · [`00b68418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6840c.md#insn-00b68418)
- 新版 `00bd7934`（命令位置の公開資料なし） · `00bd793c`（命令位置の公開資料なし） · `00bd7918`（命令位置の公開資料なし）

~~~diff
- 00b68434 ["INT_ADD", "register:40f0:8", ["const:b68434:8", "const:4:8"]]
- 00b68434 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7934 ["INT_ADD", "register:40f0:8", ["const:bd7934:8", "const:4:8"]]
+ 00bd7934 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68434 bytes 17d70194
+ 00bd7934 bytes 770c0294
- 00b6843c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b6843c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd793c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00bd793c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6843c bytes 60c204f9
+ 00bd793c bytes 604604f9
- 00b68418 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7918 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68418 bytes d32900b0
+ 00bd7918 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3cf062849500130fc859f94455e3e3"></a>

### [`00b684c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b684c8.md) → [`00bd79c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd79c8.md) _ZN8firebase4auth8user_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd7a04",
      "incomplete_value": true,
      "site": "00bd7a04",
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
      "definition_site": "00b68504",
      "incomplete_value": true,
      "site": "00b68504",
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
            "const:988:8"
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
      "definition_site": "00bd7a24",
      "incomplete_value": true,
      "site": "00bd7a24",
      "value": [
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
      "definition_site": "00b68524",
      "incomplete_value": true,
      "site": "00b68524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "00bd79e0",
      "incomplete_value": true,
      "site": "00bd79e0",
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
      "definition_site": "00b684e0",
      "incomplete_value": true,
      "site": "00b684e0",
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
      "00bd79dc",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd79e8",
      "READ",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7a04",
      "WRITE",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd79dc",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd79e8",
      "READ",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7a04",
      "WRITE",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b684c8.md#insn-00b68504) · [`00b68520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b684c8.md#insn-00b68520) · [`00b68524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b684c8.md#insn-00b68524)
- 新版 `00bd7a04`（命令位置の公開資料なし） · `00bd7a20`（命令位置の公開資料なし） · `00bd7a24`（命令位置の公開資料なし）

~~~diff
- 00b68504 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68504 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68504 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
- 00b68504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd7a04 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd7a04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd7a04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
+ 00bd7a04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68504 bytes bf222639
+ 00bd7a04 bytes bf422239
- 00b68520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68520 ["INT_ADD", "register:40f0:8", ["const:b68520:8", "const:4:8"]]
- 00b68520 ["CALLIND", null, ["register:0:8"]]
+ 00bd7a20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7a20 ["INT_ADD", "register:40f0:8", ["const:bd7a20:8", "const:4:8"]]
+ 00bd7a20 ["CALLIND", null, ["register:0:8"]]
- 00b68520 bytes 00013fd6
+ 00bd7a20 bytes 00013fd6
- 00b68524 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b68524 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b68524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd7a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00bd7a24 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd7a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b68524 bytes 9fc204f9
+ 00bd7a24 bytes 9f4604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47fc27bbc0ccd8313b1c3f49fde987ca"></a>

### [`00b68538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68538.md) → [`00bd7a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7a38.md) _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b68578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7a78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6854c",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b68554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7a7c"
      ]
    ],
    [
      "unmatched:00b6855c",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7a4c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7a54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7a7c"
      ]
    ],
    [
      "00bd7a5c",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68538.md#insn-00b68554) · [`00b68570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68538.md#insn-00b68570) · [`00b68578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68538.md#insn-00b68578)
- 新版 `00bd7a70`（命令位置の公開資料なし）

~~~diff
- 00b68554 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b68554 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b68554 bytes 410100b5
- 00b68570 ["INT_ADD", "register:40f0:8", ["const:b68570:8", "const:4:8"]]
- 00b68570 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7a70 ["INT_ADD", "register:40f0:8", ["const:bd7a70:8", "const:4:8"]]
+ 00bd7a70 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68570 bytes c8d60194
+ 00bd7a70 bytes 280c0294
- 00b68578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b68578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68578 bytes 80c204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ae526b971f0bbbc063977b6e831c37"></a>

### [`00b685a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685a8.md) → [`00bd7aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7aa8.md) _ZN8firebase4auth8user_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd7ac4",
      "incomplete_value": false,
      "site": "00bd7ac8",
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
      "definition_site": "00b685c4",
      "incomplete_value": false,
      "site": "00b685c8",
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
      "definition_site": "00bd7ad4",
      "incomplete_value": true,
      "site": "00bd7ae0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b685d4",
      "incomplete_value": true,
      "site": "00b685e0",
      "value": [
        "LOAD",
        "8",
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
      "00bd7ac4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd7ad4",
      "DATA",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7ac4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd7ad4",
      "DATA",
      [
        "storage",
        "01126898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b685c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685a8.md#insn-00b685c8) · [`00b685c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685a8.md#insn-00b685c0) · [`00b685c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685a8.md#insn-00b685c4)
- 新版 `00bd7ac8`（命令位置の公開資料なし） · `00bd7ac0`（命令位置の公開資料なし） · `00bd7ac4`（命令位置の公開資料なし）

~~~diff
- 00b685c8 ["INT_ADD", "register:40f0:8", ["const:b685c8:8", "const:4:8"]]
- 00b685c8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd7ac8 ["INT_ADD", "register:40f0:8", ["const:bd7ac8:8", "const:4:8"]]
+ 00bd7ac8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b685c8 bytes eed60194
+ 00bd7ac8 bytes 4e0c0294
- 00b685c0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd7ac0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b685c0 bytes 80b9ff90
+ 00bd7ac0 bytes 80b6ffb0
- 00b685c4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b685c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b685c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b685c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7ac4 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd7ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b685c4 bytes 001c1591
+ 00bd7ac4 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b7638d5a8f6c218f6a917d4da4b8d9"></a>

### [`00b685e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685e4.md) → [`00bd7ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ae4.md) _ZN8firebase4auth8user_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7b24",
      "incomplete_value": true,
      "site": "00bd7b24",
      "value": [
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
      "definition_site": "00b68624",
      "incomplete_value": true,
      "site": "00b68624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00bd7b00",
      "incomplete_value": true,
      "site": "00bd7b00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68600",
      "incomplete_value": true,
      "site": "00b68600",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7b08",
      "incomplete_value": false,
      "site": "00bd7b1c",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68608",
      "incomplete_value": false,
      "site": "00b6861c",
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
      "00bd7af8",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7b08",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bd7b24",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7af8",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7b08",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd7b24",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6861c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685e4.md#insn-00b6861c) · [`00b68624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685e4.md#insn-00b68624) · [`00b685f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685e4.md#insn-00b685f0)
- 新版 `00bd7b1c`（命令位置の公開資料なし） · `00bd7b24`（命令位置の公開資料なし） · `00bd7af0`（命令位置の公開資料なし）

~~~diff
- 00b6861c ["INT_ADD", "register:40f0:8", ["const:b6861c:8", "const:4:8"]]
- 00b6861c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7b1c ["INT_ADD", "register:40f0:8", ["const:bd7b1c:8", "const:4:8"]]
+ 00bd7b1c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6861c bytes 9dd60194
+ 00bd7b1c bytes fd0b0294
- 00b68624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b68624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7b24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00bd7b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68624 bytes 80c204f9
+ 00bd7b24 bytes 804604f9
- 00b685f0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd7af0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b685f0 bytes d42900b0
+ 00bd7af0 bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-979731d7e40740a2f2954655512d737e"></a>

### [`00b68690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68690.md) → [`00bd7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b90.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bd7bbc",
      "incomplete_value": true,
      "site": "00bd7bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686bc",
      "incomplete_value": true,
      "site": "00b686bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00bd7ba4",
      "incomplete_value": true,
      "site": "00bd7ba4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686a4",
      "incomplete_value": true,
      "site": "00b686a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7bb0",
      "incomplete_value": false,
      "site": "00bd7bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686b0",
      "incomplete_value": false,
      "site": "00b686b4",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7ba0",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7bb0",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00bd7bbc",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7ba0",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7bb0",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd7bbc",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b686b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68690.md#insn-00b686b4) · [`00b686bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68690.md#insn-00b686bc) · [`00b6869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68690.md#insn-00b6869c)
- 新版 `00bd7bb4`（命令位置の公開資料なし） · `00bd7bbc`（命令位置の公開資料なし） · `00bd7b9c`（命令位置の公開資料なし）

~~~diff
- 00b686b4 ["INT_ADD", "register:40f0:8", ["const:b686b4:8", "const:4:8"]]
- 00b686b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7bb4 ["INT_ADD", "register:40f0:8", ["const:bd7bb4:8", "const:4:8"]]
+ 00bd7bb4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b686b4 bytes 77d60194
+ 00bd7bb4 bytes d70b0294
- 00b686bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b686bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
+ 00bd7bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b686bc bytes 60d604f9
+ 00bd7bbc bytes 605a04f9
- 00b6869c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7b9c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6869c bytes d32900b0
+ 00bd7b9c bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287fb93c2bd873f6acbd801e2a5da3e5"></a>

### [`00b686d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b686d0.md) → [`00bd7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7bd0.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00b686d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b686d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b686d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b686d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b686d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7be0",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7bd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd7bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7be0",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b686d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b686d0.md#insn-00b686d0) · [`00b686d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b686d0.md#insn-00b686d4) · [`00b686e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b686d0.md#insn-00b686e4)
- 新版 `00bd7be4`（命令位置の公開資料なし）

~~~diff
- 00b686d0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b686d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b686d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b686d0 bytes f30f1ef8
- 00b686d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b686d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b686d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b686d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b686d4 bytes fd7b01a9
- 00b686e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b686e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd7be4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd7be4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b686e4 bytes e80000b5
+ 00bd7be4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23f5e2910b0515d2f591afd3f19c7018"></a>

### [`00b68710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68710.md) → [`00bd7c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c10.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7c40",
      "incomplete_value": true,
      "site": "00bd7c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00bd7c24",
      "incomplete_value": true,
      "site": "00bd7c24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7c30",
      "incomplete_value": false,
      "site": "00bd7c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68730",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7c20",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7c30",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00bd7c40",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7c20",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7c30",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd7c40",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68710.md#insn-00b68738) · [`00b68740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68710.md#insn-00b68740) · [`00b6871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68710.md#insn-00b6871c)
- 新版 `00bd7c38`（命令位置の公開資料なし） · `00bd7c40`（命令位置の公開資料なし） · `00bd7c1c`（命令位置の公開資料なし）

~~~diff
- 00b68738 ["INT_ADD", "register:40f0:8", ["const:b68738:8", "const:4:8"]]
- 00b68738 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7c38 ["INT_ADD", "register:40f0:8", ["const:bd7c38:8", "const:4:8"]]
+ 00bd7c38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68738 bytes 56d60194
+ 00bd7c38 bytes b60b0294
- 00b68740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b68740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7c40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
+ 00bd7c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68740 bytes 60d604f9
+ 00bd7c40 bytes 605a04f9
- 00b6871c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7c1c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6871c bytes d32900b0
+ 00bd7c1c bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590c0a3e13b5c399f98768922fabeea2"></a>

### [`00b68754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68754.md) → [`00bd7c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c54.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7c84",
      "incomplete_value": true,
      "site": "00bd7c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68784",
      "incomplete_value": true,
      "site": "00b68784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00bd7c68",
      "incomplete_value": true,
      "site": "00bd7c68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68768",
      "incomplete_value": true,
      "site": "00b68768",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7c70",
      "incomplete_value": false,
      "site": "00bd7c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68770",
      "incomplete_value": false,
      "site": "00b6877c",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7c64",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7c70",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00bd7c84",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7c64",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7c70",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd7c84",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6877c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68754.md#insn-00b6877c) · [`00b68784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68754.md#insn-00b68784) · [`00b68760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68754.md#insn-00b68760)
- 新版 `00bd7c7c`（命令位置の公開資料なし） · `00bd7c84`（命令位置の公開資料なし） · `00bd7c60`（命令位置の公開資料なし）

~~~diff
- 00b6877c ["INT_ADD", "register:40f0:8", ["const:b6877c:8", "const:4:8"]]
- 00b6877c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7c7c ["INT_ADD", "register:40f0:8", ["const:bd7c7c:8", "const:4:8"]]
+ 00bd7c7c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6877c bytes 45d60194
+ 00bd7c7c bytes a50b0294
- 00b68784 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b68784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7c84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
+ 00bd7c84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68784 bytes 60d604f9
+ 00bd7c84 bytes 605a04f9
- 00b68760 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7c60 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68760 bytes d32900b0
+ 00bd7c60 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789f4ddf59190816a26b222981a8e62e"></a>

### [`00b687a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b687a4.md) → [`00bd7ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ca4.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd7cfc",
      "incomplete_value": true,
      "site": "00bd7cfc",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b687fc",
      "incomplete_value": true,
      "site": "00b687fc",
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
            "const:9b0:8"
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
      "definition_site": "00bd7cd8",
      "incomplete_value": true,
      "site": "00bd7ce4",
      "value": [
        "LOAD",
        "8",
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
                "const:8b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b687d8",
      "incomplete_value": true,
      "site": "00b687e4",
      "value": [
        "LOAD",
        "8",
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
                "const:9a8:8"
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
      "00bd7cb8",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7cd8",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7cfc",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7cb8",
      "READ",
      [
        "storage",
        "011268b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7cd8",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7cfc",
      "WRITE",
      [
        "storage",
        "011268b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b687e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b687a4.md#insn-00b687e4) · [`00b687fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b687a4.md#insn-00b687fc) · [`00b687b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b687a4.md#insn-00b687b4)
- 新版 `00bd7ce4`（命令位置の公開資料なし） · `00bd7cfc`（命令位置の公開資料なし） · `00bd7cb4`（命令位置の公開資料なし）

~~~diff
- 00b687e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b687e4 ["INT_ADD", "register:40f0:8", ["const:b687e4:8", "const:4:8"]]
- 00b687e4 ["CALLIND", null, ["register:0:8"]]
+ 00bd7ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7ce4 ["INT_ADD", "register:40f0:8", ["const:bd7ce4:8", "const:4:8"]]
+ 00bd7ce4 ["CALLIND", null, ["register:0:8"]]
- 00b687e4 bytes 00013fd6
+ 00bd7ce4 bytes 00013fd6
- 00b687fc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b687fc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00b687fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd7cfc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd7cfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b8:8"]]
+ 00bd7cfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b687fc bytes a0c22639
+ 00bd7cfc bytes a0e22239
- 00b687b4 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd7cb4 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b687b4 bytes d52900b0
+ 00bd7cb4 bytes 752a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96fc2f05f1350ba71315f4b444ffd440"></a>

### [`00b68810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68810.md) → [`00bd7d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d10.md) _ZN8firebase4auth8jniphone12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd7d4c",
      "incomplete_value": true,
      "site": "00bd7d4c",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6884c",
      "incomplete_value": true,
      "site": "00b6884c",
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
            "const:9b0:8"
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
      "definition_site": "00bd7d6c",
      "incomplete_value": true,
      "site": "00bd7d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6886c",
      "incomplete_value": true,
      "site": "00b6886c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00bd7d28",
      "incomplete_value": true,
      "site": "00bd7d28",
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
      "definition_site": "00b68828",
      "incomplete_value": true,
      "site": "00b68828",
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
      "00bd7d24",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d30",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7d4c",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d24",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d30",
      "READ",
      [
        "storage",
        "011268b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7d4c",
      "WRITE",
      [
        "storage",
        "011268b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68810.md#insn-00b6884c) · [`00b68868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68810.md#insn-00b68868) · [`00b6886c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68810.md#insn-00b6886c)
- 新版 `00bd7d4c`（命令位置の公開資料なし） · `00bd7d68`（命令位置の公開資料なし） · `00bd7d6c`（命令位置の公開資料なし）

~~~diff
- 00b6884c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6884c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6884c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
- 00b6884c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd7d4c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd7d4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd7d4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b8:8"]]
+ 00bd7d4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6884c bytes bfc22639
+ 00bd7d4c bytes bfe22239
- 00b68868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68868 ["INT_ADD", "register:40f0:8", ["const:b68868:8", "const:4:8"]]
- 00b68868 ["CALLIND", null, ["register:0:8"]]
+ 00bd7d68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7d68 ["INT_ADD", "register:40f0:8", ["const:bd7d68:8", "const:4:8"]]
+ 00bd7d68 ["CALLIND", null, ["register:0:8"]]
- 00b68868 bytes 00013fd6
+ 00bd7d68 bytes 00013fd6
- 00b6886c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b6886c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6886c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd7d6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b0:8"]]
+ 00bd7d6c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd7d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6886c bytes 9fd604f9
+ 00bd7d6c bytes 9f5a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c36e9528259f9313c0a45e73dce16e6"></a>

### [`00b68880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68880.md) → [`00bd7d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d80.md) _ZN8firebase4auth8jniphone14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7dc0",
      "incomplete_value": true,
      "site": "00bd7dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b688c0",
      "incomplete_value": true,
      "site": "00b688c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00bd7d9c",
      "incomplete_value": true,
      "site": "00bd7d9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6889c",
      "incomplete_value": true,
      "site": "00b6889c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7da4",
      "incomplete_value": false,
      "site": "00bd7db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b688a4",
      "incomplete_value": false,
      "site": "00b688b8",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7d94",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7da4",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00bd7dc0",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d94",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7da4",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd7dc0",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b688b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68880.md#insn-00b688b8) · [`00b688c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68880.md#insn-00b688c0) · [`00b6888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68880.md#insn-00b6888c)
- 新版 `00bd7db8`（命令位置の公開資料なし） · `00bd7dc0`（命令位置の公開資料なし） · `00bd7d8c`（命令位置の公開資料なし）

~~~diff
- 00b688b8 ["INT_ADD", "register:40f0:8", ["const:b688b8:8", "const:4:8"]]
- 00b688b8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7db8 ["INT_ADD", "register:40f0:8", ["const:bd7db8:8", "const:4:8"]]
+ 00bd7db8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b688b8 bytes f6d50194
+ 00bd7db8 bytes 560b0294
- 00b688c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b688c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7dc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b0:8"]]
+ 00bd7dc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b688c0 bytes 80d604f9
+ 00bd7dc0 bytes 805a04f9
- 00b6888c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd7d8c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6888c bytes d42900b0
+ 00bd7d8c bytes 742a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac71f6897468ea66065864b7e6e246f5"></a>

### [`00b688f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b688f0.md) → [`00bd7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7df0.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd7e0c",
      "incomplete_value": false,
      "site": "00bd7e10",
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
      "definition_site": "00b6890c",
      "incomplete_value": false,
      "site": "00b68910",
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
      "definition_site": "00bd7e1c",
      "incomplete_value": true,
      "site": "00bd7e28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6891c",
      "incomplete_value": true,
      "site": "00b68928",
      "value": [
        "LOAD",
        "8",
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
      "00bd7e0c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd7e1c",
      "DATA",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e0c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd7e1c",
      "DATA",
      [
        "storage",
        "011268c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b688f0.md#insn-00b68910) · [`00b68908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b688f0.md#insn-00b68908) · [`00b6890c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b688f0.md#insn-00b6890c)
- 新版 `00bd7e10`（命令位置の公開資料なし） · `00bd7e08`（命令位置の公開資料なし） · `00bd7e0c`（命令位置の公開資料なし）

~~~diff
- 00b68910 ["INT_ADD", "register:40f0:8", ["const:b68910:8", "const:4:8"]]
- 00b68910 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd7e10 ["INT_ADD", "register:40f0:8", ["const:bd7e10:8", "const:4:8"]]
+ 00bd7e10 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b68910 bytes 1cd60194
+ 00bd7e10 bytes 7c0b0294
- 00b68908 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd7e08 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b68908 bytes 80b9ff90
+ 00bd7e08 bytes 80b6ffb0
- 00b6890c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6890c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6890c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6890c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7e0c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd7e0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7e0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7e0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6890c bytes 001c1591
+ 00bd7e0c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc02ce5c7a606cb5dd889902d5309158"></a>

### [`00b6892c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6892c.md) → [`00bd7e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e2c.md) _ZN8firebase4auth8jniphone13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b6896c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7e6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68940",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b68948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7e70"
      ]
    ],
    [
      "unmatched:00b68950",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e40",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7e70"
      ]
    ],
    [
      "00bd7e50",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6892c.md#insn-00b68948) · [`00b68964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6892c.md#insn-00b68964) · [`00b6896c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6892c.md#insn-00b6896c)
- 新版 `00bd7e64`（命令位置の公開資料なし）

~~~diff
- 00b68948 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b68948 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b68948 bytes 410100b5
- 00b68964 ["INT_ADD", "register:40f0:8", ["const:b68964:8", "const:4:8"]]
- 00b68964 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7e64 ["INT_ADD", "register:40f0:8", ["const:bd7e64:8", "const:4:8"]]
+ 00bd7e64 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68964 bytes cbd50194
+ 00bd7e64 bytes 2b0b0294
- 00b6896c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b6896c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6896c bytes 80d604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a56bdf5337e8526606fb73d1fd24797"></a>

### [`00b689d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b689d8.md) → [`00bd7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ed8.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00bd7f04",
      "incomplete_value": true,
      "site": "00bd7f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a04",
      "incomplete_value": true,
      "site": "00b68a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "definition_site": "00bd7eec",
      "incomplete_value": true,
      "site": "00bd7eec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689ec",
      "incomplete_value": true,
      "site": "00b689ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7ef8",
      "incomplete_value": false,
      "site": "00bd7efc",
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
            "const:cac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689f8",
      "incomplete_value": false,
      "site": "00b689fc",
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
            "const:27e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7ee8",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ef8",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00bd7f04",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7ee8",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ef8",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd7f04",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b689fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b689d8.md#insn-00b689fc) · [`00b68a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b689d8.md#insn-00b68a04) · [`00b689e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b689d8.md#insn-00b689e4)
- 新版 `00bd7efc`（命令位置の公開資料なし） · `00bd7f04`（命令位置の公開資料なし） · `00bd7ee4`（命令位置の公開資料なし）

~~~diff
- 00b689fc ["INT_ADD", "register:40f0:8", ["const:b689fc:8", "const:4:8"]]
- 00b689fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7efc ["INT_ADD", "register:40f0:8", ["const:bd7efc:8", "const:4:8"]]
+ 00bd7efc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b689fc bytes a5d50194
+ 00bd7efc bytes 050b0294
- 00b68a04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00b68a04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00bd7f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a04 bytes 60ea04f9
+ 00bd7f04 bytes 606e04f9
- 00b689e4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7ee4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b689e4 bytes d32900b0
+ 00bd7ee4 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdddde6fdbf080465851ee6ee352825"></a>

### [`00b68a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a18.md) → [`00bd7f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f18.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b68a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7f44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7f2c",
      "incomplete_value": true,
      "site": "00bd7f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a2c",
      "incomplete_value": true,
      "site": "00b68a2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd7f28",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b68a34",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b68a3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd7f28",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7f34",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd7f3c",
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

- 旧版 [`00b68a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a18.md#insn-00b68a2c) · [`00b68a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a18.md#insn-00b68a3c) · [`00b68a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a18.md#insn-00b68a44)
- 新版 `00bd7f2c`（命令位置の公開資料なし）

~~~diff
- 00b68a2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b68a2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd7f2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd7f2c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b68a2c bytes e80000b5
+ 00bd7f2c bytes e80000b5
- 00b68a3c ["INT_ADD", "register:40f0:8", ["const:b68a3c:8", "const:4:8"]]
- 00b68a3c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68a3c bytes 95d50194
- 00b68a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00b68a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a44 bytes 60ea04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

