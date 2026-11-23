# v15.7.4 → v16.0.0 · 最優先の変更候補 (59)

[一覧の目次](README.md)

<a id="compare-d821e4926b1a7f55cc737a61ddf53157"></a>

### [`00aeccfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md) → [`00b4ca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aeccfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeccfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecd00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeccfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecd00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecd10",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ca84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ca94",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeccfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aeccfc) · [`00aecd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aecd00) · [`00aecd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aecd18)

~~~diff
- 00aeccfc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeccfc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeccfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aeccfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeccfc bytes f44fbea9
- 00aecd00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aecd00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aecd00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aecd00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecd00 bytes fd7b01a9
- 00aecd18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aecd18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aecd18 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94d957a3a2c0a7cb9d7248a0669438d"></a>

### [`00aecd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md) → [`00b4caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4caf0.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aecd88",
      "incomplete_value": false,
      "site": "00aecd8c",
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
    "old": {
      "definition_site": "00aecd98",
      "incomplete_value": true,
      "site": "00aecda4",
      "value": [
        "LOAD",
        "8",
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
      "00b4cb0c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4cb1c",
      "DATA",
      [
        "storage",
        "010a09c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cb0c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4cb1c",
      "DATA",
      [
        "storage",
        "01125880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd8c) · [`00aecd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd84) · [`00aecd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd88)
- 新版 `00b4cb10`（命令位置の公開資料なし） · `00b4cb08`（命令位置の公開資料なし） · `00b4cb0c`（命令位置の公開資料なし）

~~~diff
- 00aecd8c ["INT_ADD", "register:40f0:8", ["const:aecd8c:8", "const:4:8"]]
- 00aecd8c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4cb10 ["INT_ADD", "register:40f0:8", ["const:b4cb10:8", "const:4:8"]]
+ 00b4cb10 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aecd8c bytes fdc40394
+ 00b4cb10 bytes 3c380494
- 00aecd84 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4cb08 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aecd84 bytes 60bdffb0
+ 00b4cb08 bytes e0baffb0
- 00aecd88 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aecd88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aecd88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aecd88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb0c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4cb0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aecd88 bytes 00c81791
+ 00b4cb0c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0d55da66137f1df26efb045d88bbda"></a>

### [`00aecda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md) → [`00b4cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
    "old": {
      "definition_site": "00aecdd4",
      "incomplete_value": true,
      "site": "00aecdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aecdbc",
      "incomplete_value": true,
      "site": "00aecdbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aecdc8",
      "incomplete_value": false,
      "site": "00aecdcc",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cb3c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb4c",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4cb58",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb3c",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb4c",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cb58",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdcc) · [`00aecdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdd4) · [`00aecdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdb4)
- 新版 `00b4cb50`（命令位置の公開資料なし） · `00b4cb58`（命令位置の公開資料なし） · `00b4cb38`（命令位置の公開資料なし）

~~~diff
- 00aecdcc ["INT_ADD", "register:40f0:8", ["const:aecdcc:8", "const:4:8"]]
- 00aecdcc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cb50 ["INT_ADD", "register:40f0:8", ["const:b4cb50:8", "const:4:8"]]
+ 00b4cb50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aecdcc bytes b1c40394
+ 00b4cb50 bytes f0370494
- 00aecdd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
- 00aecdd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cb58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b4cb58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecdd4 bytes 60e604f9
+ 00b4cb58 bytes 604604f9
- 00aecdb4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cb38 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aecdb4 bytes b32d0090
+ 00b4cb38 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8733c385b99c0aa350e3dd02284e52dd"></a>

### [`00aecde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md) → [`00b4cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb6c.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aece14",
      "incomplete_value": true,
      "site": "00aece14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aecdfc",
      "incomplete_value": true,
      "site": "00aecdfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aece04",
      "incomplete_value": false,
      "site": "00aece0c",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cb7c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb88",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4cb98",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb7c",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb88",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cb98",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aece0c) · [`00aece14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aece14) · [`00aecdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aecdf4)
- 新版 `00b4cb90`（命令位置の公開資料なし） · `00b4cb98`（命令位置の公開資料なし） · `00b4cb78`（命令位置の公開資料なし）

~~~diff
- 00aece0c ["INT_ADD", "register:40f0:8", ["const:aece0c:8", "const:4:8"]]
- 00aece0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cb90 ["INT_ADD", "register:40f0:8", ["const:b4cb90:8", "const:4:8"]]
+ 00b4cb90 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aece0c bytes a1c40394
+ 00b4cb90 bytes e0370494
- 00aece14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
- 00aece14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cb98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b4cb98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aece14 bytes 60e604f9
+ 00b4cb98 bytes 604604f9
- 00aecdf4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cb78 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aecdf4 bytes b32d0090
+ 00b4cb78 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98177213aead501d8ac4c26abe85981c"></a>

### [`00aece28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md) → [`00b4cbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbac.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aece58",
      "incomplete_value": true,
      "site": "00aece58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "definition_site": "00aece3c",
      "incomplete_value": true,
      "site": "00aece3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aece48",
      "incomplete_value": false,
      "site": "00aece50",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbcc",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4cbdc",
      "WRITE",
      [
        "storage",
        "010a09c8",
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
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbcc",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cbdc",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece50) · [`00aece58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece58) · [`00aece34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece34)
- 新版 `00b4cbd4`（命令位置の公開資料なし） · `00b4cbdc`（命令位置の公開資料なし） · `00b4cbb8`（命令位置の公開資料なし）

~~~diff
- 00aece50 ["INT_ADD", "register:40f0:8", ["const:aece50:8", "const:4:8"]]
- 00aece50 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cbd4 ["INT_ADD", "register:40f0:8", ["const:b4cbd4:8", "const:4:8"]]
+ 00b4cbd4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aece50 bytes 90c40394
+ 00b4cbd4 bytes cf370494
- 00aece58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
- 00aece58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cbdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b4cbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aece58 bytes 60e604f9
+ 00b4cbdc bytes 604604f9
- 00aece34 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cbb8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aece34 bytes b32d0090
+ 00b4cbb8 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2170dae78ab70e44ebc7b156b6d9604"></a>

### [`00aece6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece6c.md) → [`00b4cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aece9c",
      "incomplete_value": true,
      "site": "00aece9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aece80",
      "incomplete_value": true,
      "site": "00aece80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aece88",
      "incomplete_value": false,
      "site": "00aece94",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cc00",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc0c",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4cc20",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc00",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc0c",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cc20",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece6c.md#insn-00aece94) · [`00aece9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece6c.md#insn-00aece9c) · [`00aece78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece6c.md#insn-00aece78)
- 新版 `00b4cc18`（命令位置の公開資料なし） · `00b4cc20`（命令位置の公開資料なし） · `00b4cbfc`（命令位置の公開資料なし）

~~~diff
- 00aece94 ["INT_ADD", "register:40f0:8", ["const:aece94:8", "const:4:8"]]
- 00aece94 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cc18 ["INT_ADD", "register:40f0:8", ["const:b4cc18:8", "const:4:8"]]
+ 00b4cc18 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aece94 bytes 7fc40394
+ 00b4cc18 bytes be370494
- 00aece9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
- 00aece9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cc20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b4cc20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aece9c bytes 60e604f9
+ 00b4cc20 bytes 604604f9
- 00aece78 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cbfc ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aece78 bytes b32d0090
+ 00b4cbfc bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-626ae2f262859d3de644a37e9e4d4a8d"></a>

### [`00aecebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecebc.md) → [`00b4cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00aecf44",
      "incomplete_value": true,
      "site": "00aecf44",
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
            "const:9d0:8"
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
    "old": {
      "definition_site": "00aecef0",
      "incomplete_value": true,
      "site": "00aecefc",
      "value": [
        "LOAD",
        "8",
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
                "const:9c8:8"
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
      "00b4cc54",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cc74",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ccc8",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc54",
      "READ",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cc74",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ccc8",
      "WRITE",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecebc.md#insn-00aecefc) · [`00aecf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecebc.md#insn-00aecf44) · [`00aececc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecebc.md#insn-00aececc)
- 新版 `00b4cc80`（命令位置の公開資料なし） · `00b4ccc8`（命令位置の公開資料なし） · `00b4cc50`（命令位置の公開資料なし）

~~~diff
- 00aecefc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecefc ["INT_ADD", "register:40f0:8", ["const:aecefc:8", "const:4:8"]]
- 00aecefc ["CALLIND", null, ["register:0:8"]]
+ 00b4cc80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cc80 ["INT_ADD", "register:40f0:8", ["const:b4cc80:8", "const:4:8"]]
+ 00b4cc80 ["CALLIND", null, ["register:0:8"]]
- 00aecefc bytes 00013fd6
+ 00b4cc80 bytes 00013fd6
- 00aecf44 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aecf44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d0:8"]]
- 00aecf44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ccc8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ccc8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
+ 00b4ccc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aecf44 bytes a0422739
+ 00b4ccc8 bytes a0422239
- 00aececc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4cc50 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aececc bytes b52d0090
+ 00b4cc50 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8008af6fbddf34d069bf9ce540a729cb"></a>

### [`00aecf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md) → [`00b4ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ccdc.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00aecf94",
      "incomplete_value": true,
      "site": "00aecf94",
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
            "const:9d0:8"
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
    "old": {
      "definition_site": "00aecfe4",
      "incomplete_value": true,
      "site": "00aecfe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aecf70",
      "incomplete_value": true,
      "site": "00aecf70",
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
      "00b4ccf0",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ccfc",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cd18",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ccf0",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ccfc",
      "READ",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cd18",
      "WRITE",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md#insn-00aecf94) · [`00aecfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md#insn-00aecfe0) · [`00aecfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md#insn-00aecfe4)
- 新版 `00b4cd18`（命令位置の公開資料なし） · `00b4cd64`（命令位置の公開資料なし） · `00b4cd68`（命令位置の公開資料なし）

~~~diff
- 00aecf94 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aecf94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aecf94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d0:8"]]
- 00aecf94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4cd18 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4cd18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4cd18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
+ 00b4cd18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aecf94 bytes bf422739
+ 00b4cd18 bytes bf422239
- 00aecfe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecfe0 ["INT_ADD", "register:40f0:8", ["const:aecfe0:8", "const:4:8"]]
- 00aecfe0 ["CALLIND", null, ["register:0:8"]]
+ 00b4cd64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cd64 ["INT_ADD", "register:40f0:8", ["const:b4cd64:8", "const:4:8"]]
+ 00b4cd64 ["CALLIND", null, ["register:0:8"]]
- 00aecfe0 bytes 00013fd6
+ 00b4cd64 bytes 00013fd6
- 00aecfe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
- 00aecfe4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aecfe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4cd68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b4cd68 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4cd68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aecfe4 bytes 9fe604f9
+ 00b4cd68 bytes 9f4604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbbe481379aa6644a6cba0d56b17df87"></a>

### [`00aecff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md) → [`00b4cd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed038",
      "incomplete_value": true,
      "site": "00aed038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aed014",
      "incomplete_value": true,
      "site": "00aed014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed01c",
      "incomplete_value": false,
      "site": "00aed030",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cd90",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cda0",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4cdbc",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd90",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cda0",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cdbc",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md#insn-00aed030) · [`00aed038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md#insn-00aed038) · [`00aed004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md#insn-00aed004)
- 新版 `00b4cdb4`（命令位置の公開資料なし） · `00b4cdbc`（命令位置の公開資料なし） · `00b4cd88`（命令位置の公開資料なし）

~~~diff
- 00aed030 ["INT_ADD", "register:40f0:8", ["const:aed030:8", "const:4:8"]]
- 00aed030 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cdb4 ["INT_ADD", "register:40f0:8", ["const:b4cdb4:8", "const:4:8"]]
+ 00b4cdb4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed030 bytes 18c40394
+ 00b4cdb4 bytes 57370494
- 00aed038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
- 00aed038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cdbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b4cdbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed038 bytes 80e604f9
+ 00b4cdbc bytes 804604f9
- 00aed004 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4cd88 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed004 bytes 942d00f0
+ 00b4cd88 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c93a2b2601ac00a33bfa6539aeae7135"></a>

### [`00aed068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed068.md) → [`00b4cdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cdec.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde680.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b100.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00aed084",
      "incomplete_value": false,
      "site": "00aed088",
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
    "old": {
      "definition_site": "00aed094",
      "incomplete_value": true,
      "site": "00aed0a0",
      "value": [
        "LOAD",
        "8",
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
      "00b4ce08",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4ce18",
      "DATA",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce08",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4ce18",
      "DATA",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed068.md#insn-00aed088) · [`00aed080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed068.md#insn-00aed080) · [`00aed084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed068.md#insn-00aed084)
- 新版 `00b4ce0c`（命令位置の公開資料なし） · `00b4ce04`（命令位置の公開資料なし） · `00b4ce08`（命令位置の公開資料なし）

~~~diff
- 00aed088 ["INT_ADD", "register:40f0:8", ["const:aed088:8", "const:4:8"]]
- 00aed088 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4ce0c ["INT_ADD", "register:40f0:8", ["const:b4ce0c:8", "const:4:8"]]
+ 00b4ce0c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed088 bytes 3ec40394
+ 00b4ce0c bytes 7d370494
- 00aed080 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4ce04 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aed080 bytes 40bdfff0
+ 00b4ce04 bytes e0baff90
- 00aed084 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aed084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce08 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4ce08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed084 bytes 001c1591
+ 00b4ce08 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef3d15e3a807412773a8b905ee73653"></a>

### [`00aed0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed0a4.md) → [`00b4ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce28.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed0e4",
      "incomplete_value": true,
      "site": "00aed0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
    "old": {
      "definition_site": "00aed0c0",
      "incomplete_value": true,
      "site": "00aed0c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed0c8",
      "incomplete_value": false,
      "site": "00aed0dc",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ce3c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce4c",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00b4ce68",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce3c",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce4c",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4ce68",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed0a4.md#insn-00aed0dc) · [`00aed0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed0a4.md#insn-00aed0e4) · [`00aed0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed0a4.md#insn-00aed0b0)
- 新版 `00b4ce60`（命令位置の公開資料なし） · `00b4ce68`（命令位置の公開資料なし） · `00b4ce34`（命令位置の公開資料なし）

~~~diff
- 00aed0dc ["INT_ADD", "register:40f0:8", ["const:aed0dc:8", "const:4:8"]]
- 00aed0dc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ce60 ["INT_ADD", "register:40f0:8", ["const:b4ce60:8", "const:4:8"]]
+ 00b4ce60 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed0dc bytes edc30394
+ 00b4ce60 bytes 2c370494
- 00aed0e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
- 00aed0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ce68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b4ce68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed0e4 bytes 80e604f9
+ 00b4ce68 bytes 804604f9
- 00aed0b0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4ce34 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed0b0 bytes 942d00f0
+ 00b4ce34 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd64eb087bfcc2138a46a0ae9b49b78"></a>

### [`00aed114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed114.md) → [`00b4ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce98.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed130",
      "incomplete_value": false,
      "site": "00aed134",
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
    "old": {
      "definition_site": "00aed140",
      "incomplete_value": true,
      "site": "00aed14c",
      "value": [
        "LOAD",
        "8",
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
      "00b4ceb4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4cec4",
      "DATA",
      [
        "storage",
        "010a09e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ceb4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4cec4",
      "DATA",
      [
        "storage",
        "011258a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed114.md#insn-00aed134) · [`00aed12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed114.md#insn-00aed12c) · [`00aed130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed114.md#insn-00aed130)
- 新版 `00b4ceb8`（命令位置の公開資料なし） · `00b4ceb0`（命令位置の公開資料なし） · `00b4ceb4`（命令位置の公開資料なし）

~~~diff
- 00aed134 ["INT_ADD", "register:40f0:8", ["const:aed134:8", "const:4:8"]]
- 00aed134 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4ceb8 ["INT_ADD", "register:40f0:8", ["const:b4ceb8:8", "const:4:8"]]
+ 00b4ceb8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed134 bytes 13c40394
+ 00b4ceb8 bytes 52370494
- 00aed12c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4ceb0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aed12c bytes 60bdff90
+ 00b4ceb0 bytes e0baffb0
- 00aed130 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ceb4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4ceb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ceb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ceb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed130 bytes 00c81791
+ 00b4ceb4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4088fc238456c36a85e3eee71fadde54"></a>

### [`00aed150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed150.md) → [`00b4ced4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ced4.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed17c",
      "incomplete_value": true,
      "site": "00aed17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed164",
      "incomplete_value": true,
      "site": "00aed164",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed170",
      "incomplete_value": false,
      "site": "00aed174",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cee4",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cef4",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4cf00",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cee4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cef4",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4cf00",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed150.md#insn-00aed174) · [`00aed17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed150.md#insn-00aed17c) · [`00aed15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed150.md#insn-00aed15c)
- 新版 `00b4cef8`（命令位置の公開資料なし） · `00b4cf00`（命令位置の公開資料なし） · `00b4cee0`（命令位置の公開資料なし）

~~~diff
- 00aed174 ["INT_ADD", "register:40f0:8", ["const:aed174:8", "const:4:8"]]
- 00aed174 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cef8 ["INT_ADD", "register:40f0:8", ["const:b4cef8:8", "const:4:8"]]
+ 00b4cef8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed174 bytes c7c30394
+ 00b4cef8 bytes 06370494
- 00aed17c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
- 00aed17c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cf00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4cf00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed17c bytes 60f604f9
+ 00b4cf00 bytes 605604f9
- 00aed15c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cee0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed15c bytes 932d00f0
+ 00b4cee0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e733e77877ef827c708cb50ec52bb9e"></a>

### [`00aed190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed190.md) → [`00b4cf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf14.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed1bc",
      "incomplete_value": true,
      "site": "00aed1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed1a4",
      "incomplete_value": true,
      "site": "00aed1a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed1ac",
      "incomplete_value": false,
      "site": "00aed1b4",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cf24",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf30",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4cf40",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cf24",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf30",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4cf40",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed190.md#insn-00aed1b4) · [`00aed1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed190.md#insn-00aed1bc) · [`00aed19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed190.md#insn-00aed19c)
- 新版 `00b4cf38`（命令位置の公開資料なし） · `00b4cf40`（命令位置の公開資料なし） · `00b4cf20`（命令位置の公開資料なし）

~~~diff
- 00aed1b4 ["INT_ADD", "register:40f0:8", ["const:aed1b4:8", "const:4:8"]]
- 00aed1b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cf38 ["INT_ADD", "register:40f0:8", ["const:b4cf38:8", "const:4:8"]]
+ 00b4cf38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed1b4 bytes b7c30394
+ 00b4cf38 bytes f6360494
- 00aed1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
- 00aed1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cf40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4cf40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed1bc bytes 60f604f9
+ 00b4cf40 bytes 605604f9
- 00aed19c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cf20 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed19c bytes 932d00f0
+ 00b4cf20 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c368ba21aba1aafae37baa3099b7ff"></a>

### [`00aed1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed1d0.md) → [`00b4cf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf54.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aed200",
      "incomplete_value": true,
      "site": "00aed200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "definition_site": "00aed1e4",
      "incomplete_value": true,
      "site": "00aed1e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aed1f0",
      "incomplete_value": false,
      "site": "00aed1f8",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf74",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4cf84",
      "WRITE",
      [
        "storage",
        "010a09e8",
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
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf74",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4cf84",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed1d0.md#insn-00aed1f8) · [`00aed200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed1d0.md#insn-00aed200) · [`00aed1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed1d0.md#insn-00aed1dc)
- 新版 `00b4cf7c`（命令位置の公開資料なし） · `00b4cf84`（命令位置の公開資料なし） · `00b4cf60`（命令位置の公開資料なし）

~~~diff
- 00aed1f8 ["INT_ADD", "register:40f0:8", ["const:aed1f8:8", "const:4:8"]]
- 00aed1f8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cf7c ["INT_ADD", "register:40f0:8", ["const:b4cf7c:8", "const:4:8"]]
+ 00b4cf7c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed1f8 bytes a6c30394
+ 00b4cf7c bytes e5360494
- 00aed200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
- 00aed200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cf84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4cf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed200 bytes 60f604f9
+ 00b4cf84 bytes 605604f9
- 00aed1dc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cf60 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed1dc bytes 932d00f0
+ 00b4cf60 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2a4217a494b8115c4435f27e545a4d"></a>

### [`00aed214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed214.md) → [`00b4cf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf98.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed244",
      "incomplete_value": true,
      "site": "00aed244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed228",
      "incomplete_value": true,
      "site": "00aed228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed230",
      "incomplete_value": false,
      "site": "00aed23c",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cfa8",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cfb4",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4cfc8",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cfa8",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cfb4",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4cfc8",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed214.md#insn-00aed23c) · [`00aed244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed214.md#insn-00aed244) · [`00aed220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed214.md#insn-00aed220)
- 新版 `00b4cfc0`（命令位置の公開資料なし） · `00b4cfc8`（命令位置の公開資料なし） · `00b4cfa4`（命令位置の公開資料なし）

~~~diff
- 00aed23c ["INT_ADD", "register:40f0:8", ["const:aed23c:8", "const:4:8"]]
- 00aed23c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4cfc0 ["INT_ADD", "register:40f0:8", ["const:b4cfc0:8", "const:4:8"]]
+ 00b4cfc0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed23c bytes 95c30394
+ 00b4cfc0 bytes d4360494
- 00aed244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
- 00aed244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cfc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4cfc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed244 bytes 60f604f9
+ 00b4cfc8 bytes 605604f9
- 00aed220 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4cfa4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed220 bytes 932d00f0
+ 00b4cfa4 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97742dd9ef11dd709bf14cd8ad958d16"></a>

### [`00aed264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed264.md) → [`00b4cfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cfe8.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00aed2ec",
      "incomplete_value": true,
      "site": "00aed2ec",
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
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed298",
      "incomplete_value": true,
      "site": "00aed2a4",
      "value": [
        "LOAD",
        "8",
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
                "const:9e8:8"
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
      "00b4cffc",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d01c",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d070",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cffc",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d01c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d070",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed264.md#insn-00aed2a4) · [`00aed2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed264.md#insn-00aed2ec) · [`00aed274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed264.md#insn-00aed274)
- 新版 `00b4d028`（命令位置の公開資料なし） · `00b4d070`（命令位置の公開資料なし） · `00b4cff8`（命令位置の公開資料なし）

~~~diff
- 00aed2a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed2a4 ["INT_ADD", "register:40f0:8", ["const:aed2a4:8", "const:4:8"]]
- 00aed2a4 ["CALLIND", null, ["register:0:8"]]
+ 00b4d028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d028 ["INT_ADD", "register:40f0:8", ["const:b4d028:8", "const:4:8"]]
+ 00b4d028 ["CALLIND", null, ["register:0:8"]]
- 00aed2a4 bytes 00013fd6
+ 00b4d028 bytes 00013fd6
- 00aed2ec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed2ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f0:8"]]
- 00aed2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d070 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d070 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b4d070 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed2ec bytes a0c22739
+ 00b4d070 bytes a0c22239
- 00aed274 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4cff8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aed274 bytes 952d00f0
+ 00b4cff8 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e4d2f85f1ab2af58fff02222542762"></a>

### [`00aed300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md) → [`00b4d084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d084.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00aed33c",
      "incomplete_value": true,
      "site": "00aed33c",
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
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed38c",
      "incomplete_value": true,
      "site": "00aed38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed318",
      "incomplete_value": true,
      "site": "00aed318",
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
      "00b4d098",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0a4",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d0c0",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d098",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0a4",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d0c0",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md#insn-00aed33c) · [`00aed388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md#insn-00aed388) · [`00aed38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md#insn-00aed38c)
- 新版 `00b4d0c0`（命令位置の公開資料なし） · `00b4d10c`（命令位置の公開資料なし） · `00b4d110`（命令位置の公開資料なし）

~~~diff
- 00aed33c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed33c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed33c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9f0:8"]]
- 00aed33c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d0c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d0c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d0c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b4d0c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed33c bytes bfc22739
+ 00b4d0c0 bytes bfc22239
- 00aed388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed388 ["INT_ADD", "register:40f0:8", ["const:aed388:8", "const:4:8"]]
- 00aed388 ["CALLIND", null, ["register:0:8"]]
+ 00b4d10c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d10c ["INT_ADD", "register:40f0:8", ["const:b4d10c:8", "const:4:8"]]
+ 00b4d10c ["CALLIND", null, ["register:0:8"]]
- 00aed388 bytes 00013fd6
+ 00b4d10c bytes 00013fd6
- 00aed38c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
- 00aed38c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d110 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b4d110 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed38c bytes 9ff604f9
+ 00b4d110 bytes 9f5604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41e0955aec9f89d342e900739ad20a38"></a>

### [`00aed3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed3a0.md) → [`00b4d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d124.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed3e0",
      "incomplete_value": true,
      "site": "00aed3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed3bc",
      "incomplete_value": true,
      "site": "00aed3bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed3c4",
      "incomplete_value": false,
      "site": "00aed3d8",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d138",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d148",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4d164",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d138",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d148",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d164",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed3a0.md#insn-00aed3d8) · [`00aed3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed3a0.md#insn-00aed3e0) · [`00aed3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed3a0.md#insn-00aed3ac)
- 新版 `00b4d15c`（命令位置の公開資料なし） · `00b4d164`（命令位置の公開資料なし） · `00b4d130`（命令位置の公開資料なし）

~~~diff
- 00aed3d8 ["INT_ADD", "register:40f0:8", ["const:aed3d8:8", "const:4:8"]]
- 00aed3d8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d15c ["INT_ADD", "register:40f0:8", ["const:b4d15c:8", "const:4:8"]]
+ 00b4d15c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed3d8 bytes 2ec30394
+ 00b4d15c bytes 6d360494
- 00aed3e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
- 00aed3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b4d164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed3e0 bytes 80f604f9
+ 00b4d164 bytes 805604f9
- 00aed3ac ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4d130 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed3ac bytes 942d00f0
+ 00b4d130 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64c3e09166b5174d0b3fa4d46f5c1176"></a>

### [`00aed410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed410.md) → [`00b4d194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d194.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aed42c",
      "incomplete_value": false,
      "site": "00aed430",
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
    "old": {
      "definition_site": "00aed43c",
      "incomplete_value": true,
      "site": "00aed448",
      "value": [
        "LOAD",
        "8",
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
      "00b4d1b0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4d1c0",
      "DATA",
      [
        "storage",
        "010a09f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d1b0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d1c0",
      "DATA",
      [
        "storage",
        "011258b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed410.md#insn-00aed430) · [`00aed428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed410.md#insn-00aed428) · [`00aed42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed410.md#insn-00aed42c)
- 新版 `00b4d1b4`（命令位置の公開資料なし） · `00b4d1ac`（命令位置の公開資料なし） · `00b4d1b0`（命令位置の公開資料なし）

~~~diff
- 00aed430 ["INT_ADD", "register:40f0:8", ["const:aed430:8", "const:4:8"]]
- 00aed430 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d1b4 ["INT_ADD", "register:40f0:8", ["const:b4d1b4:8", "const:4:8"]]
+ 00b4d1b4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed430 bytes 54c30394
+ 00b4d1b4 bytes 93360494
- 00aed428 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4d1ac ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aed428 bytes 40bdfff0
+ 00b4d1ac bytes c0bafff0
- 00aed42c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aed42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d1b0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4d1b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d1b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d1b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed42c bytes 001c1591
+ 00b4d1b0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253cfb1b40bf4a29465410dced16f8a9"></a>

### [`00aed44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed44c.md) → [`00b4d1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d1d0.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed48c",
      "incomplete_value": true,
      "site": "00aed48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
    "old": {
      "definition_site": "00aed468",
      "incomplete_value": true,
      "site": "00aed468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed470",
      "incomplete_value": false,
      "site": "00aed484",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d1e4",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1f4",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00b4d210",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d1e4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1f4",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d210",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed44c.md#insn-00aed484) · [`00aed48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed44c.md#insn-00aed48c) · [`00aed458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed44c.md#insn-00aed458)
- 新版 `00b4d208`（命令位置の公開資料なし） · `00b4d210`（命令位置の公開資料なし） · `00b4d1dc`（命令位置の公開資料なし）

~~~diff
- 00aed484 ["INT_ADD", "register:40f0:8", ["const:aed484:8", "const:4:8"]]
- 00aed484 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d208 ["INT_ADD", "register:40f0:8", ["const:b4d208:8", "const:4:8"]]
+ 00b4d208 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed484 bytes 03c30394
+ 00b4d208 bytes 42360494
- 00aed48c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
- 00aed48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b4d210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed48c bytes 80f604f9
+ 00b4d210 bytes 805604f9
- 00aed458 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4d1dc ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed458 bytes 942d00f0
+ 00b4d1dc bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbb1ce9ba1a101e0733a5d361483bdc0"></a>

### [`00aed4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4bc.md) → [`00b4d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed4d8",
      "incomplete_value": false,
      "site": "00aed4dc",
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
    "old": {
      "definition_site": "00aed4e8",
      "incomplete_value": true,
      "site": "00aed4f4",
      "value": [
        "LOAD",
        "8",
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
      "00b4d25c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4d26c",
      "DATA",
      [
        "storage",
        "010a0a08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d25c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4d26c",
      "DATA",
      [
        "storage",
        "011258c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4bc.md#insn-00aed4dc) · [`00aed4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4bc.md#insn-00aed4d4) · [`00aed4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4bc.md#insn-00aed4d8)
- 新版 `00b4d260`（命令位置の公開資料なし） · `00b4d258`（命令位置の公開資料なし） · `00b4d25c`（命令位置の公開資料なし）

~~~diff
- 00aed4dc ["INT_ADD", "register:40f0:8", ["const:aed4dc:8", "const:4:8"]]
- 00aed4dc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d260 ["INT_ADD", "register:40f0:8", ["const:b4d260:8", "const:4:8"]]
+ 00b4d260 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed4dc bytes 29c30394
+ 00b4d260 bytes 68360494
- 00aed4d4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4d258 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aed4d4 bytes 60bdff90
+ 00b4d258 bytes e0baff90
- 00aed4d8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d25c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4d25c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d25c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d25c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed4d8 bytes 00c81791
+ 00b4d25c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac83064b6781dad237f308b2ab49bab2"></a>

### [`00aed4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4f8.md) → [`00b4d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d27c.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
    "old": {
      "definition_site": "00aed524",
      "incomplete_value": true,
      "site": "00aed524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed50c",
      "incomplete_value": true,
      "site": "00aed50c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed518",
      "incomplete_value": false,
      "site": "00aed51c",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d28c",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d29c",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d2a8",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d28c",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d29c",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d2a8",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4f8.md#insn-00aed51c) · [`00aed524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4f8.md#insn-00aed524) · [`00aed504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4f8.md#insn-00aed504)
- 新版 `00b4d2a0`（命令位置の公開資料なし） · `00b4d2a8`（命令位置の公開資料なし） · `00b4d288`（命令位置の公開資料なし）

~~~diff
- 00aed51c ["INT_ADD", "register:40f0:8", ["const:aed51c:8", "const:4:8"]]
- 00aed51c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d2a0 ["INT_ADD", "register:40f0:8", ["const:b4d2a0:8", "const:4:8"]]
+ 00b4d2a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed51c bytes ddc20394
+ 00b4d2a0 bytes 1c360494
- 00aed524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00aed524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d2a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00b4d2a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed524 bytes 600a05f9
+ 00b4d2a8 bytes 606a04f9
- 00aed504 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d288 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed504 bytes 932d00f0
+ 00b4d288 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5400f4029c66880d84e0f4754adcba88"></a>

### [`00aed538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed538.md) → [`00b4d2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2bc.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed564",
      "incomplete_value": true,
      "site": "00aed564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed54c",
      "incomplete_value": true,
      "site": "00aed54c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed554",
      "incomplete_value": false,
      "site": "00aed55c",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d2cc",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2d8",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d2e8",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d2cc",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2d8",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d2e8",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed538.md#insn-00aed55c) · [`00aed564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed538.md#insn-00aed564) · [`00aed544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed538.md#insn-00aed544)
- 新版 `00b4d2e0`（命令位置の公開資料なし） · `00b4d2e8`（命令位置の公開資料なし） · `00b4d2c8`（命令位置の公開資料なし）

~~~diff
- 00aed55c ["INT_ADD", "register:40f0:8", ["const:aed55c:8", "const:4:8"]]
- 00aed55c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d2e0 ["INT_ADD", "register:40f0:8", ["const:b4d2e0:8", "const:4:8"]]
+ 00b4d2e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed55c bytes cdc20394
+ 00b4d2e0 bytes 0c360494
- 00aed564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00aed564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d2e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00b4d2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed564 bytes 600a05f9
+ 00b4d2e8 bytes 606a04f9
- 00aed544 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d2c8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed544 bytes 932d00f0
+ 00b4d2c8 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-671488350f5e09c38a9a821956ade697"></a>

### [`00aed578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed578.md) → [`00b4d2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2fc.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aed5a8",
      "incomplete_value": true,
      "site": "00aed5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "definition_site": "00aed58c",
      "incomplete_value": true,
      "site": "00aed58c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aed598",
      "incomplete_value": false,
      "site": "00aed5a0",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d31c",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d32c",
      "WRITE",
      [
        "storage",
        "010a0a10",
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
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d31c",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d32c",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed578.md#insn-00aed5a0) · [`00aed5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed578.md#insn-00aed5a8) · [`00aed584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed578.md#insn-00aed584)
- 新版 `00b4d324`（命令位置の公開資料なし） · `00b4d32c`（命令位置の公開資料なし） · `00b4d308`（命令位置の公開資料なし）

~~~diff
- 00aed5a0 ["INT_ADD", "register:40f0:8", ["const:aed5a0:8", "const:4:8"]]
- 00aed5a0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d324 ["INT_ADD", "register:40f0:8", ["const:b4d324:8", "const:4:8"]]
+ 00b4d324 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed5a0 bytes bcc20394
+ 00b4d324 bytes fb350494
- 00aed5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00aed5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d32c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00b4d32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed5a8 bytes 600a05f9
+ 00b4d32c bytes 606a04f9
- 00aed584 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d308 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed584 bytes 932d00f0
+ 00b4d308 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a5b82c85ed685064c6d0b5b2eccfbd4"></a>

### [`00aed5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed5bc.md) → [`00b4d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed5ec",
      "incomplete_value": true,
      "site": "00aed5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed5d0",
      "incomplete_value": true,
      "site": "00aed5d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed5d8",
      "incomplete_value": false,
      "site": "00aed5e4",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d350",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d35c",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d370",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d350",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d35c",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d370",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed5bc.md#insn-00aed5e4) · [`00aed5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed5bc.md#insn-00aed5ec) · [`00aed5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed5bc.md#insn-00aed5c8)
- 新版 `00b4d368`（命令位置の公開資料なし） · `00b4d370`（命令位置の公開資料なし） · `00b4d34c`（命令位置の公開資料なし）

~~~diff
- 00aed5e4 ["INT_ADD", "register:40f0:8", ["const:aed5e4:8", "const:4:8"]]
- 00aed5e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d368 ["INT_ADD", "register:40f0:8", ["const:b4d368:8", "const:4:8"]]
+ 00b4d368 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed5e4 bytes abc20394
+ 00b4d368 bytes ea350494
- 00aed5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00aed5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00b4d370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed5ec bytes 600a05f9
+ 00b4d370 bytes 606a04f9
- 00aed5c8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d34c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed5c8 bytes 932d00f0
+ 00b4d34c bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b0b6133b281e5d7dfe28f97feb70675"></a>

### [`00aed60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed60c.md) → [`00b4d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d390.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00aed694",
      "incomplete_value": true,
      "site": "00aed694",
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
            "const:a18:8"
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
    "old": {
      "definition_site": "00aed640",
      "incomplete_value": true,
      "site": "00aed64c",
      "value": [
        "LOAD",
        "8",
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
                "const:a10:8"
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
      "00b4d3a4",
      "READ",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d3c4",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d418",
      "WRITE",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d3a4",
      "READ",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d3c4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d418",
      "WRITE",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed60c.md#insn-00aed64c) · [`00aed694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed60c.md#insn-00aed694) · [`00aed61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed60c.md#insn-00aed61c)
- 新版 `00b4d3d0`（命令位置の公開資料なし） · `00b4d418`（命令位置の公開資料なし） · `00b4d3a0`（命令位置の公開資料なし）

~~~diff
- 00aed64c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed64c ["INT_ADD", "register:40f0:8", ["const:aed64c:8", "const:4:8"]]
- 00aed64c ["CALLIND", null, ["register:0:8"]]
+ 00b4d3d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d3d0 ["INT_ADD", "register:40f0:8", ["const:b4d3d0:8", "const:4:8"]]
+ 00b4d3d0 ["CALLIND", null, ["register:0:8"]]
- 00aed64c bytes 00013fd6
+ 00b4d3d0 bytes 00013fd6
- 00aed694 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed694 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a18:8"]]
- 00aed694 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d418 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d418 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d8:8"]]
+ 00b4d418 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed694 bytes a0622839
+ 00b4d418 bytes a0622339
- 00aed61c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4d3a0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aed61c bytes 952d00f0
+ 00b4d3a0 bytes d52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a41559a78b7803f8e58ac838630ce6"></a>

### [`00aed6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed6a8.md) → [`00b4d42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d42c.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00aed6e4",
      "incomplete_value": true,
      "site": "00aed6e4",
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
            "const:a18:8"
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
    "old": {
      "definition_site": "00aed734",
      "incomplete_value": true,
      "site": "00aed734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed6c0",
      "incomplete_value": true,
      "site": "00aed6c0",
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
      "00b4d440",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d44c",
      "READ",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d468",
      "WRITE",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d440",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d44c",
      "READ",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d468",
      "WRITE",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed6a8.md#insn-00aed6e4) · [`00aed730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed6a8.md#insn-00aed730) · [`00aed734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed6a8.md#insn-00aed734)
- 新版 `00b4d468`（命令位置の公開資料なし） · `00b4d4b4`（命令位置の公開資料なし） · `00b4d4b8`（命令位置の公開資料なし）

~~~diff
- 00aed6e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed6e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed6e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a18:8"]]
- 00aed6e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d468 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d468 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d468 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d8:8"]]
+ 00b4d468 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed6e4 bytes bf622839
+ 00b4d468 bytes bf622339
- 00aed730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed730 ["INT_ADD", "register:40f0:8", ["const:aed730:8", "const:4:8"]]
- 00aed730 ["CALLIND", null, ["register:0:8"]]
+ 00b4d4b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d4b4 ["INT_ADD", "register:40f0:8", ["const:b4d4b4:8", "const:4:8"]]
+ 00b4d4b4 ["CALLIND", null, ["register:0:8"]]
- 00aed730 bytes 00013fd6
+ 00b4d4b4 bytes 00013fd6
- 00aed734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00aed734 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d4b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
+ 00b4d4b8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d4b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed734 bytes 9f0a05f9
+ 00b4d4b8 bytes 9f6a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3dfe51808daca6b8faff7bebcb1027d"></a>

### [`00aed748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed748.md) → [`00b4d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d4cc.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed788",
      "incomplete_value": true,
      "site": "00aed788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed764",
      "incomplete_value": true,
      "site": "00aed764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed76c",
      "incomplete_value": false,
      "site": "00aed780",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d4e0",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d4f0",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d50c",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d4e0",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d4f0",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d50c",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed748.md#insn-00aed780) · [`00aed788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed748.md#insn-00aed788) · [`00aed754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed748.md#insn-00aed754)
- 新版 `00b4d504`（命令位置の公開資料なし） · `00b4d50c`（命令位置の公開資料なし） · `00b4d4d8`（命令位置の公開資料なし）

~~~diff
- 00aed780 ["INT_ADD", "register:40f0:8", ["const:aed780:8", "const:4:8"]]
- 00aed780 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d504 ["INT_ADD", "register:40f0:8", ["const:b4d504:8", "const:4:8"]]
+ 00b4d504 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed780 bytes 44c20394
+ 00b4d504 bytes 83350494
- 00aed788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00aed788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d50c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
+ 00b4d50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed788 bytes 800a05f9
+ 00b4d50c bytes 806a04f9
- 00aed754 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4d4d8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed754 bytes 942d00f0
+ 00b4d4d8 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb11f4cbb3c5d3a8dac7e4697eb678bb"></a>

### [`00aed7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7b8.md) → [`00b4d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d53c.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aed7d4",
      "incomplete_value": false,
      "site": "00aed7d8",
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
    "old": {
      "definition_site": "00aed7e4",
      "incomplete_value": true,
      "site": "00aed7f0",
      "value": [
        "LOAD",
        "8",
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
      "00b4d558",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4d568",
      "DATA",
      [
        "storage",
        "010a0a20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d558",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d568",
      "DATA",
      [
        "storage",
        "011258e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7b8.md#insn-00aed7d8) · [`00aed7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7b8.md#insn-00aed7d0) · [`00aed7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7b8.md#insn-00aed7d4)
- 新版 `00b4d55c`（命令位置の公開資料なし） · `00b4d554`（命令位置の公開資料なし） · `00b4d558`（命令位置の公開資料なし）

~~~diff
- 00aed7d8 ["INT_ADD", "register:40f0:8", ["const:aed7d8:8", "const:4:8"]]
- 00aed7d8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d55c ["INT_ADD", "register:40f0:8", ["const:b4d55c:8", "const:4:8"]]
+ 00b4d55c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed7d8 bytes 6ac20394
+ 00b4d55c bytes a9350494
- 00aed7d0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4d554 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aed7d0 bytes 40bdfff0
+ 00b4d554 bytes c0bafff0
- 00aed7d4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aed7d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed7d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed7d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d558 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4d558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed7d4 bytes 001c1591
+ 00b4d558 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f902b93b05a17c79dea30e60bde66d8"></a>

### [`00aed7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7f4.md) → [`00b4d578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d578.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed834",
      "incomplete_value": true,
      "site": "00aed834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
    "old": {
      "definition_site": "00aed810",
      "incomplete_value": true,
      "site": "00aed810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed818",
      "incomplete_value": false,
      "site": "00aed82c",
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
            "const:6db:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d58c",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d59c",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00b4d5b8",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d58c",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d59c",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d5b8",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7f4.md#insn-00aed82c) · [`00aed834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7f4.md#insn-00aed834) · [`00aed800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7f4.md#insn-00aed800)
- 新版 `00b4d5b0`（命令位置の公開資料なし） · `00b4d5b8`（命令位置の公開資料なし） · `00b4d584`（命令位置の公開資料なし）

~~~diff
- 00aed82c ["INT_ADD", "register:40f0:8", ["const:aed82c:8", "const:4:8"]]
- 00aed82c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d5b0 ["INT_ADD", "register:40f0:8", ["const:b4d5b0:8", "const:4:8"]]
+ 00b4d5b0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed82c bytes 19c20394
+ 00b4d5b0 bytes 58350494
- 00aed834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00aed834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d5b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
+ 00b4d5b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed834 bytes 800a05f9
+ 00b4d5b8 bytes 806a04f9
- 00aed800 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4d584 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aed800 bytes 942d00f0
+ 00b4d584 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c177df9b585eba5ea23365b7492e519e"></a>

### [`00aed864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed864.md) → [`00b4d5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d5e8.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed880",
      "incomplete_value": false,
      "site": "00aed884",
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
    "old": {
      "definition_site": "00aed890",
      "incomplete_value": true,
      "site": "00aed89c",
      "value": [
        "LOAD",
        "8",
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
      "00b4d604",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4d614",
      "DATA",
      [
        "storage",
        "010a0a28",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d604",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4d614",
      "DATA",
      [
        "storage",
        "011258e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed864.md#insn-00aed884) · [`00aed87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed864.md#insn-00aed87c) · [`00aed880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed864.md#insn-00aed880)
- 新版 `00b4d608`（命令位置の公開資料なし） · `00b4d600`（命令位置の公開資料なし） · `00b4d604`（命令位置の公開資料なし）

~~~diff
- 00aed884 ["INT_ADD", "register:40f0:8", ["const:aed884:8", "const:4:8"]]
- 00aed884 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d608 ["INT_ADD", "register:40f0:8", ["const:b4d608:8", "const:4:8"]]
+ 00b4d608 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aed884 bytes 3fc20394
+ 00b4d608 bytes 7e350494
- 00aed87c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4d600 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aed87c bytes 60bdff90
+ 00b4d600 bytes e0baff90
- 00aed880 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d604 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4d604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed880 bytes 00c81791
+ 00b4d604 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59ab239f93cd5b5561e90ca8c12737f"></a>

### [`00aed8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8a0.md) → [`00b4d624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d624.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
    "old": {
      "definition_site": "00aed8cc",
      "incomplete_value": true,
      "site": "00aed8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
    "old": {
      "definition_site": "00aed8b4",
      "incomplete_value": true,
      "site": "00aed8b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed8c0",
      "incomplete_value": false,
      "site": "00aed8c4",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d634",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d644",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00b4d650",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d634",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d644",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4d650",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8a0.md#insn-00aed8c4) · [`00aed8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8a0.md#insn-00aed8cc) · [`00aed8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8a0.md#insn-00aed8ac)
- 新版 `00b4d648`（命令位置の公開資料なし） · `00b4d650`（命令位置の公開資料なし） · `00b4d630`（命令位置の公開資料なし）

~~~diff
- 00aed8c4 ["INT_ADD", "register:40f0:8", ["const:aed8c4:8", "const:4:8"]]
- 00aed8c4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d648 ["INT_ADD", "register:40f0:8", ["const:b4d648:8", "const:4:8"]]
+ 00b4d648 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed8c4 bytes f3c10394
+ 00b4d648 bytes 32350494
- 00aed8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00aed8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b4d650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed8cc bytes 601a05f9
+ 00b4d650 bytes 607a04f9
- 00aed8ac ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d630 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed8ac bytes 932d00f0
+ 00b4d630 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-934aa2fc9f4a1489ac51186312a701ee"></a>

### [`00aed8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8e0.md) → [`00b4d664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d664.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed90c",
      "incomplete_value": true,
      "site": "00aed90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
    "old": {
      "definition_site": "00aed8f4",
      "incomplete_value": true,
      "site": "00aed8f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed8fc",
      "incomplete_value": false,
      "site": "00aed904",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d674",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d680",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00b4d690",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d674",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d680",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4d690",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8e0.md#insn-00aed904) · [`00aed90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8e0.md#insn-00aed90c) · [`00aed8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8e0.md#insn-00aed8ec)
- 新版 `00b4d688`（命令位置の公開資料なし） · `00b4d690`（命令位置の公開資料なし） · `00b4d670`（命令位置の公開資料なし）

~~~diff
- 00aed904 ["INT_ADD", "register:40f0:8", ["const:aed904:8", "const:4:8"]]
- 00aed904 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d688 ["INT_ADD", "register:40f0:8", ["const:b4d688:8", "const:4:8"]]
+ 00b4d688 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed904 bytes e3c10394
+ 00b4d688 bytes 22350494
- 00aed90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00aed90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d690 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b4d690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed90c bytes 601a05f9
+ 00b4d690 bytes 607a04f9
- 00aed8ec ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d670 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed8ec bytes 932d00f0
+ 00b4d670 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d07afbbafbbd4c19538bbb5c1e3d05a2"></a>

### [`00aed920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md) → [`00b4d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aed950",
      "incomplete_value": true,
      "site": "00aed950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00aed934",
      "incomplete_value": true,
      "site": "00aed934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aed940",
      "incomplete_value": false,
      "site": "00aed948",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6c4",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d4",
      "WRITE",
      [
        "storage",
        "010a0a30",
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
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6c4",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d4",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md#insn-00aed948) · [`00aed950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md#insn-00aed950) · [`00aed92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md#insn-00aed92c)
- 新版 `00b4d6cc`（命令位置の公開資料なし） · `00b4d6d4`（命令位置の公開資料なし） · `00b4d6b0`（命令位置の公開資料なし）

~~~diff
- 00aed948 ["INT_ADD", "register:40f0:8", ["const:aed948:8", "const:4:8"]]
- 00aed948 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d6cc ["INT_ADD", "register:40f0:8", ["const:b4d6cc:8", "const:4:8"]]
+ 00b4d6cc ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed948 bytes d2c10394
+ 00b4d6cc bytes 11350494
- 00aed950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00aed950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d6d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b4d6d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed950 bytes 601a05f9
+ 00b4d6d4 bytes 607a04f9
- 00aed92c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d6b0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed92c bytes 932d00f0
+ 00b4d6b0 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ec986607ae4b7dae8101b6405fad3b"></a>

### [`00aed964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed964.md) → [`00b4d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6e8.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed994",
      "incomplete_value": true,
      "site": "00aed994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
    "old": {
      "definition_site": "00aed978",
      "incomplete_value": true,
      "site": "00aed978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed980",
      "incomplete_value": false,
      "site": "00aed98c",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d6f8",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d704",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00b4d718",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6f8",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d704",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4d718",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed964.md#insn-00aed98c) · [`00aed994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed964.md#insn-00aed994) · [`00aed970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed964.md#insn-00aed970)
- 新版 `00b4d710`（命令位置の公開資料なし） · `00b4d718`（命令位置の公開資料なし） · `00b4d6f4`（命令位置の公開資料なし）

~~~diff
- 00aed98c ["INT_ADD", "register:40f0:8", ["const:aed98c:8", "const:4:8"]]
- 00aed98c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d710 ["INT_ADD", "register:40f0:8", ["const:b4d710:8", "const:4:8"]]
+ 00b4d710 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aed98c bytes c1c10394
+ 00b4d710 bytes 00350494
- 00aed994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00aed994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d718 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b4d718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed994 bytes 601a05f9
+ 00b4d718 bytes 607a04f9
- 00aed970 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d6f4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aed970 bytes 932d00f0
+ 00b4d6f4 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4257e3c27b88f3647fb328defe45b2"></a>

### [`00aed9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed9b4.md) → [`00b4d738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d738.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00aeda3c",
      "incomplete_value": true,
      "site": "00aeda3c",
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
            "const:a38:8"
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
    "old": {
      "definition_site": "00aed9e8",
      "incomplete_value": true,
      "site": "00aed9f4",
      "value": [
        "LOAD",
        "8",
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
                "const:a30:8"
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
      "00b4d74c",
      "READ",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d76c",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7c0",
      "WRITE",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d74c",
      "READ",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d76c",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7c0",
      "WRITE",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed9b4.md#insn-00aed9f4) · [`00aeda3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed9b4.md#insn-00aeda3c) · [`00aed9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed9b4.md#insn-00aed9c4)
- 新版 `00b4d778`（命令位置の公開資料なし） · `00b4d7c0`（命令位置の公開資料なし） · `00b4d748`（命令位置の公開資料なし）

~~~diff
- 00aed9f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed9f4 ["INT_ADD", "register:40f0:8", ["const:aed9f4:8", "const:4:8"]]
- 00aed9f4 ["CALLIND", null, ["register:0:8"]]
+ 00b4d778 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d778 ["INT_ADD", "register:40f0:8", ["const:b4d778:8", "const:4:8"]]
+ 00b4d778 ["CALLIND", null, ["register:0:8"]]
- 00aed9f4 bytes 00013fd6
+ 00b4d778 bytes 00013fd6
- 00aeda3c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeda3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a38:8"]]
- 00aeda3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d7c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d7c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f8:8"]]
+ 00b4d7c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeda3c bytes a0e22839
+ 00b4d7c0 bytes a0e22339
- 00aed9c4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4d748 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aed9c4 bytes 952d00f0
+ 00b4d748 bytes d52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa44b55a59993f2a879d1347e1b6ce3b"></a>

### [`00aeda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md) → [`00b4d7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d7d4.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00aeda8c",
      "incomplete_value": true,
      "site": "00aeda8c",
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
            "const:a38:8"
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
    "old": {
      "definition_site": "00aedadc",
      "incomplete_value": true,
      "site": "00aedadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
    "old": {
      "definition_site": "00aeda68",
      "incomplete_value": true,
      "site": "00aeda68",
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
      "00b4d7e8",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7f4",
      "READ",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d810",
      "WRITE",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d7e8",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7f4",
      "READ",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d810",
      "WRITE",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeda8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md#insn-00aeda8c) · [`00aedad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md#insn-00aedad8) · [`00aedadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md#insn-00aedadc)
- 新版 `00b4d810`（命令位置の公開資料なし） · `00b4d85c`（命令位置の公開資料なし） · `00b4d860`（命令位置の公開資料なし）

~~~diff
- 00aeda8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeda8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeda8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a38:8"]]
- 00aeda8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d810 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d810 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d810 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f8:8"]]
+ 00b4d810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeda8c bytes bfe22839
+ 00b4d810 bytes bfe22339
- 00aedad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aedad8 ["INT_ADD", "register:40f0:8", ["const:aedad8:8", "const:4:8"]]
- 00aedad8 ["CALLIND", null, ["register:0:8"]]
+ 00b4d85c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d85c ["INT_ADD", "register:40f0:8", ["const:b4d85c:8", "const:4:8"]]
+ 00b4d85c ["CALLIND", null, ["register:0:8"]]
- 00aedad8 bytes 00013fd6
+ 00b4d85c bytes 00013fd6
- 00aedadc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00aedadc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aedadc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d860 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00b4d860 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aedadc bytes 9f1a05f9
+ 00b4d860 bytes 9f7a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b37f79c93ae820af7496704f248d50"></a>

### [`00aedaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md) → [`00b4d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aedaf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aedaf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aedaf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aedaf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aedaf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aedb04",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d874",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4d878",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4d888",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md#insn-00aedaf0) · [`00aedaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md#insn-00aedaf4) · [`00aedb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md#insn-00aedb0c)

~~~diff
- 00aedaf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aedaf0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aedaf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aedaf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aedaf0 bytes f44fbea9
- 00aedaf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aedaf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aedaf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aedaf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aedaf4 bytes fd7b01a9
- 00aedb0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aedb0c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aedb0c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f824ff0798686ef1dcaa0265dd3f62ca"></a>

### [`00aedb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb60.md) → [`00b4d8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d8e4.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aedb7c",
      "incomplete_value": false,
      "site": "00aedb80",
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
    "old": {
      "definition_site": "00aedb8c",
      "incomplete_value": true,
      "site": "00aedb98",
      "value": [
        "LOAD",
        "8",
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
      "00b4d900",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4d910",
      "DATA",
      [
        "storage",
        "010a0a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d900",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d910",
      "DATA",
      [
        "storage",
        "01125900",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb60.md#insn-00aedb80) · [`00aedb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb60.md#insn-00aedb78) · [`00aedb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb60.md#insn-00aedb7c)
- 新版 `00b4d904`（命令位置の公開資料なし） · `00b4d8fc`（命令位置の公開資料なし） · `00b4d900`（命令位置の公開資料なし）

~~~diff
- 00aedb80 ["INT_ADD", "register:40f0:8", ["const:aedb80:8", "const:4:8"]]
- 00aedb80 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d904 ["INT_ADD", "register:40f0:8", ["const:b4d904:8", "const:4:8"]]
+ 00b4d904 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aedb80 bytes 80c10394
+ 00b4d904 bytes bf340494
- 00aedb78 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4d8fc ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aedb78 bytes 40bdfff0
+ 00b4d8fc bytes c0bafff0
- 00aedb7c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aedb7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d900 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4d900 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d900 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d900 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedb7c bytes 001c1591
+ 00b4d900 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-623d8f1b0f89c58ad32418a7b5d9afb6"></a>

### [`00aedb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb9c.md) → [`00b4d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aedbdc",
      "incomplete_value": true,
      "site": "00aedbdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
    "old": {
      "definition_site": "00aedbb8",
      "incomplete_value": true,
      "site": "00aedbb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedbc0",
      "incomplete_value": false,
      "site": "00aedbd4",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d934",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d944",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00b4d960",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d934",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d944",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4d960",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb9c.md#insn-00aedbd4) · [`00aedbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb9c.md#insn-00aedbdc) · [`00aedba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb9c.md#insn-00aedba8)
- 新版 `00b4d958`（命令位置の公開資料なし） · `00b4d960`（命令位置の公開資料なし） · `00b4d92c`（命令位置の公開資料なし）

~~~diff
- 00aedbd4 ["INT_ADD", "register:40f0:8", ["const:aedbd4:8", "const:4:8"]]
- 00aedbd4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d958 ["INT_ADD", "register:40f0:8", ["const:b4d958:8", "const:4:8"]]
+ 00b4d958 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedbd4 bytes 2fc10394
+ 00b4d958 bytes 6e340494
- 00aedbdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00aedbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00b4d960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedbdc bytes 801a05f9
+ 00b4d960 bytes 807a04f9
- 00aedba8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4d92c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aedba8 bytes 942d00f0
+ 00b4d92c bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baaf46de9e573c84afeb327fd9f7c78f"></a>

### [`00aedc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md) → [`00b4d990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d990.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aedc28",
      "incomplete_value": false,
      "site": "00aedc2c",
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
    "old": {
      "definition_site": "00aedc38",
      "incomplete_value": true,
      "site": "00aedc44",
      "value": [
        "LOAD",
        "8",
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
      "00b4d9ac",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4d9bc",
      "DATA",
      [
        "storage",
        "010a0a58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d9ac",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4d9bc",
      "DATA",
      [
        "storage",
        "01125918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md#insn-00aedc2c) · [`00aedc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md#insn-00aedc24) · [`00aedc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md#insn-00aedc28)
- 新版 `00b4d9b0`（命令位置の公開資料なし） · `00b4d9a8`（命令位置の公開資料なし） · `00b4d9ac`（命令位置の公開資料なし）

~~~diff
- 00aedc2c ["INT_ADD", "register:40f0:8", ["const:aedc2c:8", "const:4:8"]]
- 00aedc2c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4d9b0 ["INT_ADD", "register:40f0:8", ["const:b4d9b0:8", "const:4:8"]]
+ 00b4d9b0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aedc2c bytes 55c10394
+ 00b4d9b0 bytes 94340494
- 00aedc24 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4d9a8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aedc24 bytes 60bdff90
+ 00b4d9a8 bytes e0baff90
- 00aedc28 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aedc28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedc28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedc28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d9ac ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4d9ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d9ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d9ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedc28 bytes 00c81791
+ 00b4d9ac bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90ef9d9c86ea5c15840eb2cd29f5bee6"></a>

### [`00aedc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc48.md) → [`00b4d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d9cc.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
    "old": {
      "definition_site": "00aedc74",
      "incomplete_value": true,
      "site": "00aedc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aedc5c",
      "incomplete_value": true,
      "site": "00aedc5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedc68",
      "incomplete_value": false,
      "site": "00aedc6c",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d9dc",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9ec",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4d9f8",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d9dc",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9ec",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4d9f8",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc48.md#insn-00aedc6c) · [`00aedc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc48.md#insn-00aedc74) · [`00aedc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc48.md#insn-00aedc54)
- 新版 `00b4d9f0`（命令位置の公開資料なし） · `00b4d9f8`（命令位置の公開資料なし） · `00b4d9d8`（命令位置の公開資料なし）

~~~diff
- 00aedc6c ["INT_ADD", "register:40f0:8", ["const:aedc6c:8", "const:4:8"]]
- 00aedc6c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4d9f0 ["INT_ADD", "register:40f0:8", ["const:b4d9f0:8", "const:4:8"]]
+ 00b4d9f0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedc6c bytes 09c10394
+ 00b4d9f0 bytes 48340494
- 00aedc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
- 00aedc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d9f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b4d9f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedc74 bytes 603205f9
+ 00b4d9f8 bytes 609204f9
- 00aedc54 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4d9d8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aedc54 bytes 932d00f0
+ 00b4d9d8 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddad00fd1f820b90d870c3dae2d06f5e"></a>

### [`00aedc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc88.md) → [`00b4da0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da0c.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aedcb4",
      "incomplete_value": true,
      "site": "00aedcb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aedc9c",
      "incomplete_value": true,
      "site": "00aedc9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedca4",
      "incomplete_value": false,
      "site": "00aedcac",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4da1c",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da28",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4da38",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4da1c",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da28",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4da38",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc88.md#insn-00aedcac) · [`00aedcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc88.md#insn-00aedcb4) · [`00aedc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc88.md#insn-00aedc94)
- 新版 `00b4da30`（命令位置の公開資料なし） · `00b4da38`（命令位置の公開資料なし） · `00b4da18`（命令位置の公開資料なし）

~~~diff
- 00aedcac ["INT_ADD", "register:40f0:8", ["const:aedcac:8", "const:4:8"]]
- 00aedcac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4da30 ["INT_ADD", "register:40f0:8", ["const:b4da30:8", "const:4:8"]]
+ 00b4da30 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedcac bytes f9c00394
+ 00b4da30 bytes 38340494
- 00aedcb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
- 00aedcb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4da38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b4da38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedcb4 bytes 603205f9
+ 00b4da38 bytes 609204f9
- 00aedc94 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4da18 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aedc94 bytes 932d00f0
+ 00b4da18 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42792b15258806b92bfa4529d7c4f100"></a>

### [`00aedcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedcc8.md) → [`00b4da4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aedcf8",
      "incomplete_value": true,
      "site": "00aedcf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "definition_site": "00aedcdc",
      "incomplete_value": true,
      "site": "00aedcdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aedce8",
      "incomplete_value": false,
      "site": "00aedcf0",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da6c",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4da7c",
      "WRITE",
      [
        "storage",
        "010a0a60",
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
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da6c",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4da7c",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedcc8.md#insn-00aedcf0) · [`00aedcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedcc8.md#insn-00aedcf8) · [`00aedcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedcc8.md#insn-00aedcd4)
- 新版 `00b4da74`（命令位置の公開資料なし） · `00b4da7c`（命令位置の公開資料なし） · `00b4da58`（命令位置の公開資料なし）

~~~diff
- 00aedcf0 ["INT_ADD", "register:40f0:8", ["const:aedcf0:8", "const:4:8"]]
- 00aedcf0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4da74 ["INT_ADD", "register:40f0:8", ["const:b4da74:8", "const:4:8"]]
+ 00b4da74 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedcf0 bytes e8c00394
+ 00b4da74 bytes 27340494
- 00aedcf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
- 00aedcf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4da7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b4da7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedcf8 bytes 603205f9
+ 00b4da7c bytes 609204f9
- 00aedcd4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4da58 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aedcd4 bytes 932d00f0
+ 00b4da58 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-420be1f8d82646e771913ef87d54c2d0"></a>

### [`00aedd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md) → [`00b4da90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aedd3c",
      "incomplete_value": true,
      "site": "00aedd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aedd20",
      "incomplete_value": true,
      "site": "00aedd20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedd28",
      "incomplete_value": false,
      "site": "00aedd34",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4daa0",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daac",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4dac0",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4daa0",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daac",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4dac0",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md#insn-00aedd34) · [`00aedd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md#insn-00aedd3c) · [`00aedd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md#insn-00aedd18)
- 新版 `00b4dab8`（命令位置の公開資料なし） · `00b4dac0`（命令位置の公開資料なし） · `00b4da9c`（命令位置の公開資料なし）

~~~diff
- 00aedd34 ["INT_ADD", "register:40f0:8", ["const:aedd34:8", "const:4:8"]]
- 00aedd34 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4dab8 ["INT_ADD", "register:40f0:8", ["const:b4dab8:8", "const:4:8"]]
+ 00b4dab8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedd34 bytes d7c00394
+ 00b4dab8 bytes 16340494
- 00aedd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
- 00aedd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dac0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b4dac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedd3c bytes 603205f9
+ 00b4dac0 bytes 609204f9
- 00aedd18 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4da9c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aedd18 bytes 932d00f0
+ 00b4da9c bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42bd8ec937d74c9559df2767d03654a0"></a>

### [`00aedd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd5c.md) → [`00b4dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00aedde4",
      "incomplete_value": true,
      "site": "00aedde4",
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
            "const:a68:8"
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
    "old": {
      "definition_site": "00aedd90",
      "incomplete_value": true,
      "site": "00aedd9c",
      "value": [
        "LOAD",
        "8",
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
                "const:a60:8"
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
      "00b4daf4",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4db14",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db68",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4daf4",
      "READ",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4db14",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db68",
      "WRITE",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd5c.md#insn-00aedd9c) · [`00aedde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd5c.md#insn-00aedde4) · [`00aedd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd5c.md#insn-00aedd6c)
- 新版 `00b4db20`（命令位置の公開資料なし） · `00b4db68`（命令位置の公開資料なし） · `00b4daf0`（命令位置の公開資料なし）

~~~diff
- 00aedd9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aedd9c ["INT_ADD", "register:40f0:8", ["const:aedd9c:8", "const:4:8"]]
- 00aedd9c ["CALLIND", null, ["register:0:8"]]
+ 00b4db20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4db20 ["INT_ADD", "register:40f0:8", ["const:b4db20:8", "const:4:8"]]
+ 00b4db20 ["CALLIND", null, ["register:0:8"]]
- 00aedd9c bytes 00013fd6
+ 00b4db20 bytes 00013fd6
- 00aedde4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aedde4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a68:8"]]
- 00aedde4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4db68 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4db68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
+ 00b4db68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aedde4 bytes a0a22939
+ 00b4db68 bytes a0a22439
- 00aedd6c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4daf0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aedd6c bytes 952d00f0
+ 00b4daf0 bytes d52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3e378bf12803b9c9f6bc03f2c93077"></a>

### [`00aeddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md) → [`00b4db7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00aede34",
      "incomplete_value": true,
      "site": "00aede34",
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
            "const:a68:8"
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
    "old": {
      "definition_site": "00aede84",
      "incomplete_value": true,
      "site": "00aede84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aede10",
      "incomplete_value": true,
      "site": "00aede10",
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
      "00b4db90",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db9c",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dbb8",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4db90",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db9c",
      "READ",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dbb8",
      "WRITE",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aede34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md#insn-00aede34) · [`00aede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md#insn-00aede80) · [`00aede84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md#insn-00aede84)
- 新版 `00b4dbb8`（命令位置の公開資料なし） · `00b4dc04`（命令位置の公開資料なし） · `00b4dc08`（命令位置の公開資料なし）

~~~diff
- 00aede34 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aede34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aede34 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a68:8"]]
- 00aede34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4dbb8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4dbb8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4dbb8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
+ 00b4dbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aede34 bytes bfa22939
+ 00b4dbb8 bytes bfa22439
- 00aede80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aede80 ["INT_ADD", "register:40f0:8", ["const:aede80:8", "const:4:8"]]
- 00aede80 ["CALLIND", null, ["register:0:8"]]
+ 00b4dc04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dc04 ["INT_ADD", "register:40f0:8", ["const:b4dc04:8", "const:4:8"]]
+ 00b4dc04 ["CALLIND", null, ["register:0:8"]]
- 00aede80 bytes 00013fd6
+ 00b4dc04 bytes 00013fd6
- 00aede84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
- 00aede84 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aede84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4dc08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b4dc08 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4dc08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aede84 bytes 9f3205f9
+ 00b4dc08 bytes 9f9204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7515b3b20489c28e527f4af9ff9581a"></a>

### [`00aede98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aede98.md) → [`00b4dc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc1c.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aeded8",
      "incomplete_value": true,
      "site": "00aeded8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aedeb4",
      "incomplete_value": true,
      "site": "00aedeb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedebc",
      "incomplete_value": false,
      "site": "00aeded0",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dc30",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc40",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4dc5c",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dc30",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc40",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4dc5c",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aede98.md#insn-00aeded0) · [`00aeded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aede98.md#insn-00aeded8) · [`00aedea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aede98.md#insn-00aedea4)
- 新版 `00b4dc54`（命令位置の公開資料なし） · `00b4dc5c`（命令位置の公開資料なし） · `00b4dc28`（命令位置の公開資料なし）

~~~diff
- 00aeded0 ["INT_ADD", "register:40f0:8", ["const:aeded0:8", "const:4:8"]]
- 00aeded0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4dc54 ["INT_ADD", "register:40f0:8", ["const:b4dc54:8", "const:4:8"]]
+ 00b4dc54 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeded0 bytes 70c00394
+ 00b4dc54 bytes af330494
- 00aeded8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
- 00aeded8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dc5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b4dc5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeded8 bytes 803205f9
+ 00b4dc5c bytes 809204f9
- 00aedea4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4dc28 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aedea4 bytes 942d00f0
+ 00b4dc28 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff2d63c8158167bbca2b26c9bcdf6dc"></a>

### [`00aedf08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md) → [`00b4dc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc8c.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aedf24",
      "incomplete_value": false,
      "site": "00aedf28",
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
    "old": {
      "definition_site": "00aedf34",
      "incomplete_value": true,
      "site": "00aedf40",
      "value": [
        "LOAD",
        "8",
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
      "00b4dca8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4dcb8",
      "DATA",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dca8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4dcb8",
      "DATA",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md#insn-00aedf28) · [`00aedf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md#insn-00aedf20) · [`00aedf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md#insn-00aedf24)
- 新版 `00b4dcac`（命令位置の公開資料なし） · `00b4dca4`（命令位置の公開資料なし） · `00b4dca8`（命令位置の公開資料なし）

~~~diff
- 00aedf28 ["INT_ADD", "register:40f0:8", ["const:aedf28:8", "const:4:8"]]
- 00aedf28 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4dcac ["INT_ADD", "register:40f0:8", ["const:b4dcac:8", "const:4:8"]]
+ 00b4dcac ["CALL", null, ["callee:00c5ac00:8"]]
- 00aedf28 bytes 96c00394
+ 00b4dcac bytes d5330494
- 00aedf20 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4dca4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aedf20 bytes 40bdfff0
+ 00b4dca4 bytes c0bafff0
- 00aedf24 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aedf24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedf24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedf24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dca8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4dca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedf24 bytes 001c1591
+ 00b4dca8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ef6a8946bb7b53dc664e4f5b2d4ea0e"></a>

### [`00aedf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf44.md) → [`00b4dcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dcc8.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aedf84",
      "incomplete_value": true,
      "site": "00aedf84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
    "old": {
      "definition_site": "00aedf60",
      "incomplete_value": true,
      "site": "00aedf60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedf68",
      "incomplete_value": false,
      "site": "00aedf7c",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dcdc",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcec",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00b4dd08",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dcdc",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcec",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4dd08",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf44.md#insn-00aedf7c) · [`00aedf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf44.md#insn-00aedf84) · [`00aedf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf44.md#insn-00aedf50)
- 新版 `00b4dd00`（命令位置の公開資料なし） · `00b4dd08`（命令位置の公開資料なし） · `00b4dcd4`（命令位置の公開資料なし）

~~~diff
- 00aedf7c ["INT_ADD", "register:40f0:8", ["const:aedf7c:8", "const:4:8"]]
- 00aedf7c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4dd00 ["INT_ADD", "register:40f0:8", ["const:b4dd00:8", "const:4:8"]]
+ 00b4dd00 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aedf7c bytes 45c00394
+ 00b4dd00 bytes 84330494
- 00aedf84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
- 00aedf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dd08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b4dd08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedf84 bytes 803205f9
+ 00b4dd08 bytes 809204f9
- 00aedf50 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4dcd4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aedf50 bytes 942d00f0
+ 00b4dcd4 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c44f014c1f5f7015ecdbed7cd4b602e"></a>

### [`00aedfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedfb4.md) → [`00b4dd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aedfd0",
      "incomplete_value": false,
      "site": "00aedfd4",
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
    "old": {
      "definition_site": "00aedfe0",
      "incomplete_value": true,
      "site": "00aedfec",
      "value": [
        "LOAD",
        "8",
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
      "00b4dd54",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4dd64",
      "DATA",
      [
        "storage",
        "010a0a80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4dd54",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4dd64",
      "DATA",
      [
        "storage",
        "01125940",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedfb4.md#insn-00aedfd4) · [`00aedfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedfb4.md#insn-00aedfcc) · [`00aedfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedfb4.md#insn-00aedfd0)
- 新版 `00b4dd58`（命令位置の公開資料なし） · `00b4dd50`（命令位置の公開資料なし） · `00b4dd54`（命令位置の公開資料なし）

~~~diff
- 00aedfd4 ["INT_ADD", "register:40f0:8", ["const:aedfd4:8", "const:4:8"]]
- 00aedfd4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4dd58 ["INT_ADD", "register:40f0:8", ["const:b4dd58:8", "const:4:8"]]
+ 00b4dd58 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aedfd4 bytes 6bc00394
+ 00b4dd58 bytes aa330494
- 00aedfcc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4dd50 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aedfcc bytes 60bdff90
+ 00b4dd50 bytes e0baff90
- 00aedfd0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aedfd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedfd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedfd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd54 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4dd54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedfd0 bytes 00c81791
+ 00b4dd54 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d845c69d79a0846f4ab343a4cb2e507"></a>

### [`00aedff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md) → [`00b4dd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
    "old": {
      "definition_site": "00aee01c",
      "incomplete_value": true,
      "site": "00aee01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
    "old": {
      "definition_site": "00aee004",
      "incomplete_value": true,
      "site": "00aee004",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee010",
      "incomplete_value": false,
      "site": "00aee014",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dd84",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd94",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4dda0",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd84",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd94",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4dda0",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md#insn-00aee014) · [`00aee01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md#insn-00aee01c) · [`00aedffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md#insn-00aedffc)
- 新版 `00b4dd98`（命令位置の公開資料なし） · `00b4dda0`（命令位置の公開資料なし） · `00b4dd80`（命令位置の公開資料なし）

~~~diff
- 00aee014 ["INT_ADD", "register:40f0:8", ["const:aee014:8", "const:4:8"]]
- 00aee014 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4dd98 ["INT_ADD", "register:40f0:8", ["const:b4dd98:8", "const:4:8"]]
+ 00b4dd98 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee014 bytes 1fc00394
+ 00b4dd98 bytes 5e330494
- 00aee01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
- 00aee01c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dda0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00b4dda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee01c bytes 604605f9
+ 00b4dda0 bytes 60a604f9
- 00aedffc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4dd80 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aedffc bytes 932d00f0
+ 00b4dd80 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30e557318c79e88a1dc8a1c4fc55082"></a>

### [`00aee030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md) → [`00b4ddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddb4.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aee05c",
      "incomplete_value": true,
      "site": "00aee05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
    "old": {
      "definition_site": "00aee044",
      "incomplete_value": true,
      "site": "00aee044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee04c",
      "incomplete_value": false,
      "site": "00aee054",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ddc4",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddd0",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4dde0",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ddc4",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddd0",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4dde0",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md#insn-00aee054) · [`00aee05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md#insn-00aee05c) · [`00aee03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md#insn-00aee03c)
- 新版 `00b4ddd8`（命令位置の公開資料なし） · `00b4dde0`（命令位置の公開資料なし） · `00b4ddc0`（命令位置の公開資料なし）

~~~diff
- 00aee054 ["INT_ADD", "register:40f0:8", ["const:aee054:8", "const:4:8"]]
- 00aee054 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ddd8 ["INT_ADD", "register:40f0:8", ["const:b4ddd8:8", "const:4:8"]]
+ 00b4ddd8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee054 bytes 0fc00394
+ 00b4ddd8 bytes 4e330494
- 00aee05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
- 00aee05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dde0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00b4dde0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee05c bytes 604605f9
+ 00b4dde0 bytes 60a604f9
- 00aee03c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4ddc0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aee03c bytes 932d00d0
+ 00b4ddc0 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7e6162f99533ae391a9a360e8906af6"></a>

### [`00aee070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee070.md) → [`00b4ddf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddf4.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aee0a0",
      "incomplete_value": true,
      "site": "00aee0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00aee084",
      "incomplete_value": true,
      "site": "00aee084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00aee090",
      "incomplete_value": false,
      "site": "00aee098",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de14",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4de24",
      "WRITE",
      [
        "storage",
        "010a0a88",
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
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de14",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4de24",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee070.md#insn-00aee098) · [`00aee0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee070.md#insn-00aee0a0) · [`00aee07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee070.md#insn-00aee07c)
- 新版 `00b4de1c`（命令位置の公開資料なし） · `00b4de24`（命令位置の公開資料なし） · `00b4de00`（命令位置の公開資料なし）

~~~diff
- 00aee098 ["INT_ADD", "register:40f0:8", ["const:aee098:8", "const:4:8"]]
- 00aee098 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4de1c ["INT_ADD", "register:40f0:8", ["const:b4de1c:8", "const:4:8"]]
+ 00b4de1c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee098 bytes febf0394
+ 00b4de1c bytes 3d330494
- 00aee0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
- 00aee0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4de24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00b4de24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee0a0 bytes 604605f9
+ 00b4de24 bytes 60a604f9
- 00aee07c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4de00 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aee07c bytes 932d00d0
+ 00b4de00 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d49cc27f477e77956698e305f7ad5d6"></a>

### [`00aee0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee0b4.md) → [`00b4de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de38.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aee0e4",
      "incomplete_value": true,
      "site": "00aee0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
    "old": {
      "definition_site": "00aee0c8",
      "incomplete_value": true,
      "site": "00aee0c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee0d0",
      "incomplete_value": false,
      "site": "00aee0dc",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4de48",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de54",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4de68",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4de48",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de54",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4de68",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee0b4.md#insn-00aee0dc) · [`00aee0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee0b4.md#insn-00aee0e4) · [`00aee0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee0b4.md#insn-00aee0c0)
- 新版 `00b4de60`（命令位置の公開資料なし） · `00b4de68`（命令位置の公開資料なし） · `00b4de44`（命令位置の公開資料なし）

~~~diff
- 00aee0dc ["INT_ADD", "register:40f0:8", ["const:aee0dc:8", "const:4:8"]]
- 00aee0dc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4de60 ["INT_ADD", "register:40f0:8", ["const:b4de60:8", "const:4:8"]]
+ 00b4de60 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee0dc bytes edbf0394
+ 00b4de60 bytes 2c330494
- 00aee0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
- 00aee0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4de68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00b4de68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee0e4 bytes 604605f9
+ 00b4de68 bytes 60a604f9
- 00aee0c0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4de44 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aee0c0 bytes 932d00d0
+ 00b4de44 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ce6fb89f7ba525fdb4e346230322bf"></a>

### [`00aee104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md) → [`00b4de88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de88.md) _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4df10",
      "incomplete_value": true,
      "site": "00b4df10",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee18c",
      "incomplete_value": true,
      "site": "00aee18c",
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
            "const:a90:8"
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
    "old": {
      "definition_site": "00aee138",
      "incomplete_value": true,
      "site": "00aee144",
      "value": [
        "LOAD",
        "8",
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
                "const:a88:8"
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
      "00b4de9c",
      "READ",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4debc",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df10",
      "WRITE",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4de9c",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4debc",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df10",
      "WRITE",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md#insn-00aee144) · [`00aee18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md#insn-00aee18c) · [`00aee114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md#insn-00aee114)
- 新版 `00b4dec8`（命令位置の公開資料なし） · `00b4df10`（命令位置の公開資料なし） · `00b4de98`（命令位置の公開資料なし）

~~~diff
- 00aee144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee144 ["INT_ADD", "register:40f0:8", ["const:aee144:8", "const:4:8"]]
- 00aee144 ["CALLIND", null, ["register:0:8"]]
+ 00b4dec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dec8 ["INT_ADD", "register:40f0:8", ["const:b4dec8:8", "const:4:8"]]
+ 00b4dec8 ["CALLIND", null, ["register:0:8"]]
- 00aee144 bytes 00013fd6
+ 00b4dec8 bytes 00013fd6
- 00aee18c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aee18c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a90:8"]]
- 00aee18c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4df10 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4df10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:950:8"]]
+ 00b4df10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aee18c bytes a0422a39
+ 00b4df10 bytes a0422539
- 00aee114 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4de98 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aee114 bytes 952d00d0
+ 00b4de98 bytes d52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053275fc146a279f428d7a0c6fe9ab16"></a>

### [`00aee1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee1a0.md) → [`00b4df24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4df24.md) _ZN8firebase4util6object12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4df60",
      "incomplete_value": true,
      "site": "00b4df60",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee1dc",
      "incomplete_value": true,
      "site": "00aee1dc",
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
            "const:a90:8"
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
    "old": {
      "definition_site": "00aee22c",
      "incomplete_value": true,
      "site": "00aee22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00b4df3c",
      "incomplete_value": true,
      "site": "00b4df3c",
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
      "definition_site": "00aee1b8",
      "incomplete_value": true,
      "site": "00aee1b8",
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
      "00b4df38",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df44",
      "READ",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4df60",
      "WRITE",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4df38",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df44",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4df60",
      "WRITE",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee1a0.md#insn-00aee1dc) · [`00aee228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee1a0.md#insn-00aee228) · [`00aee22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee1a0.md#insn-00aee22c)
- 新版 `00b4df60`（命令位置の公開資料なし） · `00b4dfac`（命令位置の公開資料なし） · `00b4dfb0`（命令位置の公開資料なし）

~~~diff
- 00aee1dc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee1dc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee1dc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a90:8"]]
- 00aee1dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4df60 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4df60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4df60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:950:8"]]
+ 00b4df60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee1dc bytes bf422a39
+ 00b4df60 bytes bf422539
- 00aee228 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee228 ["INT_ADD", "register:40f0:8", ["const:aee228:8", "const:4:8"]]
- 00aee228 ["CALLIND", null, ["register:0:8"]]
+ 00b4dfac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dfac ["INT_ADD", "register:40f0:8", ["const:b4dfac:8", "const:4:8"]]
+ 00b4dfac ["CALLIND", null, ["register:0:8"]]
- 00aee228 bytes 00013fd6
+ 00b4dfac bytes 00013fd6
- 00aee22c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
- 00aee22c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee22c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4dfb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00b4dfb0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4dfb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee22c bytes 9f4605f9
+ 00b4dfb0 bytes 9fa604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd5b53d8584c0ee6d653f7201b0040ae"></a>

### [`00aee240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md) → [`00b4dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dfc4.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e004",
      "incomplete_value": true,
      "site": "00b4e004",
      "value": [
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
    "old": {
      "definition_site": "00aee280",
      "incomplete_value": true,
      "site": "00aee280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00b4dfe0",
      "incomplete_value": true,
      "site": "00b4dfe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee25c",
      "incomplete_value": true,
      "site": "00aee25c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4dfe8",
      "incomplete_value": false,
      "site": "00b4dffc",
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
    "old": {
      "definition_site": "00aee264",
      "incomplete_value": false,
      "site": "00aee278",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dfd8",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dfe8",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4e004",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dfd8",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dfe8",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e004",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md#insn-00aee278) · [`00aee280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md#insn-00aee280) · [`00aee24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md#insn-00aee24c)
- 新版 `00b4dffc`（命令位置の公開資料なし） · `00b4e004`（命令位置の公開資料なし） · `00b4dfd0`（命令位置の公開資料なし）

~~~diff
- 00aee278 ["INT_ADD", "register:40f0:8", ["const:aee278:8", "const:4:8"]]
- 00aee278 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4dffc ["INT_ADD", "register:40f0:8", ["const:b4dffc:8", "const:4:8"]]
+ 00b4dffc ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee278 bytes 86bf0394
+ 00b4dffc bytes c5320494
- 00aee280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
- 00aee280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e004 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00b4e004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee280 bytes 804605f9
+ 00b4e004 bytes 80a604f9
- 00aee24c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4dfd0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aee24c bytes 942d00d0
+ 00b4dfd0 bytes d42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a03786dff5dea94649a6fbdbcccdd574"></a>

### [`00aee2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2b0.md) → [`00b4e034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e034.md) _ZN8firebase4util6object11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4e050",
      "incomplete_value": false,
      "site": "00b4e054",
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
      "definition_site": "00aee2cc",
      "incomplete_value": false,
      "site": "00aee2d0",
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
      "definition_site": "00b4e060",
      "incomplete_value": true,
      "site": "00b4e06c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aee2dc",
      "incomplete_value": true,
      "site": "00aee2e8",
      "value": [
        "LOAD",
        "8",
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
      "00b4e050",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4e060",
      "DATA",
      [
        "storage",
        "010a0a98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e050",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4e060",
      "DATA",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2b0.md#insn-00aee2d0) · [`00aee2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2b0.md#insn-00aee2c8) · [`00aee2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2b0.md#insn-00aee2cc)
- 新版 `00b4e054`（命令位置の公開資料なし） · `00b4e04c`（命令位置の公開資料なし） · `00b4e050`（命令位置の公開資料なし）

~~~diff
- 00aee2d0 ["INT_ADD", "register:40f0:8", ["const:aee2d0:8", "const:4:8"]]
- 00aee2d0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4e054 ["INT_ADD", "register:40f0:8", ["const:b4e054:8", "const:4:8"]]
+ 00b4e054 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aee2d0 bytes acbf0394
+ 00b4e054 bytes eb320494
- 00aee2c8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4e04c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aee2c8 bytes 40bdffd0
+ 00b4e04c bytes c0baffd0
- 00aee2cc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aee2cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aee2cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aee2cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4e050 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4e050 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e050 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e050 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aee2cc bytes 001c1591
+ 00b4e050 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-374c11379917cfef7b472ce0d94b6a51"></a>

### [`00aee2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2ec.md) → [`00b4e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e0b0",
      "incomplete_value": true,
      "site": "00b4e0b0",
      "value": [
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
    "old": {
      "definition_site": "00aee32c",
      "incomplete_value": true,
      "site": "00aee32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00b4e08c",
      "incomplete_value": true,
      "site": "00b4e08c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee308",
      "incomplete_value": true,
      "site": "00aee308",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e094",
      "incomplete_value": false,
      "site": "00b4e0a8",
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
    "old": {
      "definition_site": "00aee310",
      "incomplete_value": false,
      "site": "00aee324",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e084",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e094",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00b4e0b0",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e084",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e094",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e0b0",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2ec.md#insn-00aee324) · [`00aee32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2ec.md#insn-00aee32c) · [`00aee2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2ec.md#insn-00aee2f8)
- 新版 `00b4e0a8`（命令位置の公開資料なし） · `00b4e0b0`（命令位置の公開資料なし） · `00b4e07c`（命令位置の公開資料なし）

~~~diff
- 00aee324 ["INT_ADD", "register:40f0:8", ["const:aee324:8", "const:4:8"]]
- 00aee324 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4e0a8 ["INT_ADD", "register:40f0:8", ["const:b4e0a8:8", "const:4:8"]]
+ 00b4e0a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aee324 bytes 5bbf0394
+ 00b4e0a8 bytes 9a320494
- 00aee32c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
- 00aee32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e0b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00b4e0b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee32c bytes 804605f9
+ 00b4e0b0 bytes 80a604f9
- 00aee2f8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4e07c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aee2f8 bytes 942d00d0
+ 00b4e07c bytes b42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ecf60cf3b0fbb38b699ca0bb05a6c3"></a>

### [`00aee398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md) → [`00b4e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde670.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00aee908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0f0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b4e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.25% / 新版 46.25%

CFGの説明率　旧版 35.82% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee460"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee3b8",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00aee3c4",
      "WRITE",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00aee3dc",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e13c",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e148",
      "WRITE",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e160",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md#insn-00aee3c4) · [`00aee3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md#insn-00aee3e4) · [`00aee408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md#insn-00aee408)

~~~diff
- 00aee3c4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:aa8:8"]]
- 00aee3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee3c4 bytes e8aa0ab9
- 00aee3e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aee3e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aee3e4 bytes 410100b5
- 00aee408 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:508:8"]]
- 00aee408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee408 bytes c08602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d04bcb6c654c9b4d0a127d9d45a29c"></a>

### [`00aee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee758.md) → [`00b4e4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e4dc.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde660.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0e0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e510",
      "incomplete_value": true,
      "site": "00b4e510",
      "value": [
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
      "definition_site": "00aee78c",
      "incomplete_value": true,
      "site": "00aee78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4e540",
      "incomplete_value": true,
      "site": "00b4e540",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee7bc",
      "incomplete_value": true,
      "site": "00aee7bc",
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
            "const:510:8"
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
      "definition_site": "00b4e590",
      "incomplete_value": true,
      "site": "00b4e590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee80c",
      "incomplete_value": true,
      "site": "00aee80c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00b4e4f0",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e500",
      "PARAM",
      [
        "storage",
        "002ac133",
        null,
        "string"
      ]
    ],
    [
      "00b4e508",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b4e4f0",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e500",
      "PARAM",
      [
        "storage",
        "002bd0be",
        null,
        "string"
      ]
    ],
    [
      "00b4e508",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee758.md#insn-00aee780) · [`00aee78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee758.md#insn-00aee78c) · [`00aee7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee758.md#insn-00aee7bc)
- 新版 `00b4e504`（命令位置の公開資料なし） · `00b4e510`（命令位置の公開資料なし） · `00b4e540`（命令位置の公開資料なし）

~~~diff
- 00aee780 ["INT_ADD", "register:40f0:8", ["const:aee780:8", "const:4:8"]]
- 00aee780 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4e504 ["INT_ADD", "register:40f0:8", ["const:b4e504:8", "const:4:8"]]
+ 00b4e504 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aee780 bytes 80be0394
+ 00b4e504 bytes bf310494
- 00aee78c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00aee78c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b4e510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b4e510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee78c bytes 88aa0ab9
+ 00b4e510 bytes 886a09b9
- 00aee7bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee7bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee7bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
- 00aee7bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4e540 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4e540 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4e540 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3d0:8"]]
+ 00b4e540 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee7bc bytes bf421439
+ 00b4e540 bytes bf420f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a56e577c373d0534894b794fcaa50eff"></a>

### [`00aee908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md) → [`00b4e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md) FUN_00b4e68c

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00aee398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b4e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 83.33% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aee984",
      "incomplete_value": true,
      "site": "00aee984",
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
            "const:ab0:8"
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
    "old": {
      "definition_site": "00aee92c",
      "incomplete_value": true,
      "site": "00aee930",
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
    "old": {
      "definition_site": "00aee958",
      "incomplete_value": true,
      "site": "00aee958",
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
      "00b4e6a0",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e6d0",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e708",
      "WRITE",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e6a0",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e6d0",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e708",
      "WRITE",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md#insn-00aee984) · [`00aee918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md#insn-00aee918) · [`00aee91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md#insn-00aee91c)
- 新版 `00b4e708`（命令位置の公開資料なし） · `00b4e69c`（命令位置の公開資料なし） · `00b4e6a0`（命令位置の公開資料なし）

~~~diff
- 00aee984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
- 00aee984 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4e708 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
+ 00b4e708 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee984 bytes bf5a05f9
+ 00b4e708 bytes bfba04f9
- 00aee918 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4e69c ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aee918 bytes 952d00d0
+ 00b4e69c bytes b52e00f0
- 00aee91c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
- 00aee91c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e6a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
+ 00b4e6a0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee91c bytes b35a45f9
+ 00b4e6a0 bytes b3ba44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a66a6f125a0c2200d60ce3537aa2cff"></a>

### [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) → [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md) · 呼出先 13件 [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md) · 呼出先 13件 [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 24.50% / 新版 24.50%

CFGの説明率　旧版 19.68% / 新版 16.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 34件, `store_condition` 3件, `store_destination` 11件, `unresolved_branch_alignment` 66件, `unresolved_call_alignment` 66件, `unresolved_store_alignment` 34件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aee9c8",
      "incomplete_value": true,
      "site": "00aee9c8",
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
            "const:ab8:8"
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
      "site": "00aeea10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeea68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e740",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e74c",
      "WRITE",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e76c",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e740",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e74c",
      "WRITE",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e76c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md#insn-00aee9c8) · [`00aeea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md#insn-00aeea10) · [`00aeea68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md#insn-00aeea68)
- 新版 `00b4e74c`（命令位置の公開資料なし）

~~~diff
- 00aee9c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
- 00aee9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b4e74c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 00b4e74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee9c8 bytes a8ba0ab9
+ 00b4e74c bytes a87a09b9
- 00aeea10 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:570:8"]]
- 00aeea10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeea10 bytes c0ba02f9
- 00aeea68 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:5a0:8"]]
- 00aeea68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeea68 bytes c0d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7865d65be6c7ad553e75ccb789679269"></a>

### [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) → [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) FUN_00b4f798

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) · 呼出先 1件 [`00bde500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde500.md)
- 新版 呼出元 2件 [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) · 呼出先 1件 [`00c5af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af80.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 7.67% / 新版 7.67%

CFGの説明率　旧版 5.36% / 新版 5.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 101件, `unresolved_call_alignment` 175件, `unresolved_store_alignment` 71件

アドレスに依存する影響 `branch_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefaa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefacc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4f7ac",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4f7b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aefaa4"
      ]
    ],
    [
      "00b4f7bc",
      "READ",
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
      "00b4f7ac",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4f7b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4f828"
      ]
    ],
    [
      "00b4f7bc",
      "READ",
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

- 旧版 [`00aefa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md#insn-00aefa50) · [`00aefaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md#insn-00aefaa0) · [`00aefacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md#insn-00aefacc)

~~~diff
- 00aefa50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aefa50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aefa50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
- 00aefa50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aefa50 bytes bfa21639
- 00aefaa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00aefaa0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aefaa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aefaa0 bytes 9fd202f9
- 00aefacc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aefacc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aefacc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:578:8"]]
- 00aefacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aefacc bytes bfe21539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02b367e33a95f1a621fe2f2d0d4bd6f"></a>

### [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) → [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) _ZN8firebase4util9TerminateEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) · 呼出先 10件 [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)
- 新版 呼出元 2件 [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) · 呼出先 10件 [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)

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
    "old": {
      "definition_site": "00af0c6c",
      "incomplete_value": true,
      "site": "00af0c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
    "old": {
      "definition_site": "00af0cd0",
      "incomplete_value": true,
      "site": "00af0cd0",
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
            "const:ac0:8"
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
    "old": {
      "definition_site": "00af0c8c",
      "incomplete_value": true,
      "site": "00af0c8c",
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
      "00b509d0",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b509e0",
      "PARAM",
      [
        "storage",
        "0029143c",
        null,
        "string"
      ]
    ],
    [
      "00b509e8",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b509d0",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b509e0",
      "PARAM",
      [
        "storage",
        "002a09eb",
        null,
        "string"
      ]
    ],
    [
      "00b509e8",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md#insn-00af0c60) · [`00af0c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md#insn-00af0c6c) · [`00af0ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md#insn-00af0ca4)
- 新版 `00b509e4`（命令位置の公開資料なし） · `00b509f0`（命令位置の公開資料なし） · `00b50a28`（命令位置の公開資料なし）

~~~diff
- 00af0c60 ["INT_ADD", "register:40f0:8", ["const:af0c60:8", "const:4:8"]]
- 00af0c60 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b509e4 ["INT_ADD", "register:40f0:8", ["const:b509e4:8", "const:4:8"]]
+ 00b509e4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00af0c60 bytes 48b50394
+ 00b509e4 bytes 87280494
- 00af0c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00af0c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b509f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00b509f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00af0c6c bytes 88ba0ab9
+ 00b509f0 bytes 887a09b9
- 00af0ca4 ["INT_ADD", "register:40f0:8", ["const:af0ca4:8", "const:4:8"]]
- 00af0ca4 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00b50a28 ["INT_ADD", "register:40f0:8", ["const:b50a28:8", "const:4:8"]]
+ 00b50a28 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00af0ca4 bytes dfb60394
+ 00b50a28 bytes 1e2a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74eca650c9aa6d2b9a651468e2899156"></a>

### [`00af0d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0d50.md) → [`00b50ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50ad4.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde520.md) · 呼出先 6件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)
- 新版 呼出元 1件 [`00c5afa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afa0.md) · 呼出先 6件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 56.08% / 新版 56.08%

CFGの説明率　旧版 4.84% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 27件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0e94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0d74",
      "READ",
      [
        "storage",
        "010a0520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af0d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50b40"
      ]
    ],
    [
      "unmatched:00af0dd4",
      "PARAM",
      [
        "storage",
        "002a2d66",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b50af8",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b50b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50b40"
      ]
    ],
    [
      "00b50b58",
      "PARAM",
      [
        "storage",
        "002b346e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0d50.md#insn-00af0d7c) · [`00af0d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0d50.md#insn-00af0d90) · [`00af0d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0d50.md#insn-00af0d98)
- 新版 `00b50b00`（命令位置の公開資料なし）

~~~diff
- 00af0d7c ["INT_ADD", "register:40f0:8", ["const:af0d7c:8", "const:4:8"]]
- 00af0d7c ["CALL", null, ["callee:004977f4:8"]]
+ 00b50b00 ["INT_ADD", "register:40f0:8", ["const:b50b00:8", "const:4:8"]]
+ 00b50b00 ["CALL", null, ["callee:004977f4:8"]]
- 00af0d7c bytes f80ee697
+ 00b50b00 bytes 3d1be597
- 00af0d90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af0d90 ["INT_ADD", "register:40f0:8", ["const:af0d90:8", "const:4:8"]]
- 00af0d90 ["CALLIND", null, ["register:0:8"]]
- 00af0d90 bytes 00013fd6
- 00af0d98 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00af0d98 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1246cc2851c2f624e4727a30f4f44377"></a>

### [`00af11f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af11f0.md) → [`00b50f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50f74.md) _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4d0.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af50.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.52% / 新版 64.52%

CFGの説明率　旧版 50.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af123c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00af12dc",
      "incomplete_value": true,
      "site": "00af12dc",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1328"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af120c",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af1218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50fc8"
      ]
    ],
    [
      "unmatched:00af1220",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b50f90",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b50f9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50fc8"
      ]
    ],
    [
      "00b50fa4",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af11f0.md#insn-00af1218) · [`00af1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af11f0.md#insn-00af1234) · [`00af123c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af11f0.md#insn-00af123c)

~~~diff
- 00af1218 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00af1218 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00af1218 bytes 610100b5
- 00af1234 ["INT_ADD", "register:40f0:8", ["const:af1234:8", "const:4:8"]]
- 00af1234 ["CALL", null, ["callee:00c5ab10:8"]]
- 00af1234 bytes 97b30394
- 00af123c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3b8:8"]]
- 00af123c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00af123c bytes c0de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbf2f606070d716811323a951958406"></a>

### [`00af1364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md) → [`00b510e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md) _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bde780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde780.md)
- 新版 呼出元 1件 [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b200.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.80% / 新版 92.80%

CFGの説明率　旧版 80.49% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af139c",
      "incomplete_value": true,
      "site": "00af13a0",
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
            "const:317:8"
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
    "old": {
      "definition_site": "00af14e8",
      "incomplete_value": true,
      "site": "00af14f4",
      "value": [
        "LOAD",
        "8",
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
                "const:3a8:8"
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
      "00b5111c",
      "PARAM",
      [
        "storage",
        "002ac150",
        null,
        "string"
      ]
    ],
    [
      "00b51120",
      "PARAM",
      [
        "storage",
        "002ae317",
        null,
        "string"
      ]
    ],
    [
      "00b51150",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5111c",
      "PARAM",
      [
        "storage",
        "002bd0db",
        null,
        "string"
      ]
    ],
    [
      "00b51120",
      "PARAM",
      [
        "storage",
        "002bf75c",
        null,
        "string"
      ]
    ],
    [
      "00b51150",
      "PARAM",
      [
        "storage",
        "01125988",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af13a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md#insn-00af13a0) · [`00af14f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md#insn-00af14f4) · [`00af1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md#insn-00af1380)
- 新版 `00b51124`（命令位置の公開資料なし） · `00b51278`（命令位置の公開資料なし） · `00b51104`（命令位置の公開資料なし）

~~~diff
- 00af13a0 ["INT_ADD", "register:40f0:8", ["const:af13a0:8", "const:4:8"]]
- 00af13a0 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b51124 ["INT_ADD", "register:40f0:8", ["const:b51124:8", "const:4:8"]]
+ 00b51124 ["CALL", null, ["callee:00c5ad30:8"]]
- 00af13a0 bytes c4b30394
+ 00b51124 bytes 03270494
- 00af14f4 ["INT_ADD", "register:40f0:8", ["const:af14f4:8", "const:4:8"]]
- 00af14f4 ["CALL", null, ["callee:00574cac:8"]]
+ 00b51278 ["INT_ADD", "register:40f0:8", ["const:b51278:8", "const:4:8"]]
+ 00b51278 ["CALL", null, ["callee:00574cac:8"]]
- 00af14f4 bytes 4882e997
+ 00b51278 bytes 8d8ee897
- 00af1380 ["COPY", "register:4040:8", ["const:2ac000:8"]]
+ 00b51104 ["COPY", "register:4040:8", ["const:2bd000:8"]]
- 00af1380 bytes c8bdfff0
+ 00b51104 bytes 68bbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66a19737a63088b14c3246711a03fa61"></a>

### [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) → [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) FUN_00b51378

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ae4b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md) [`00ae4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md)
- 新版 呼出元 2件 [`00b4491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md) [`00b44c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af164c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1648",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af164c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af1650",
      "READ",
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
      "00b513cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b513d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b513d4",
      "READ",
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

- 旧版 [`00af1648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md#insn-00af1648) · [`00af164c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md#insn-00af164c) · [`00af1660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md#insn-00af1660)

~~~diff
- 00af1648 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00af1648 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00af1648 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00af1648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af1648 bytes abab3ca9
- 00af164c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af164c ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00af164c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00af164c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af164c bytes a9b33da9
- 00af1660 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00af1660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00af1660 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00af1660 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00af1660 bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1bbfc0d68b0d243991a6458b9e60b3"></a>

### [`00af168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af168c.md) → [`00b51410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51410.md) _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5a0.md) · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)
- 新版 呼出元 1件 [`00c5b020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b020.md) · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)

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
    "old": {
      "definition_site": "00af16b0",
      "incomplete_value": true,
      "site": "00af16bc",
      "value": [
        "LOAD",
        "8",
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
                "const:570:8"
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
    "old": {
      "definition_site": "00af16b4",
      "incomplete_value": true,
      "site": "00af16bc",
      "value": [
        "LOAD",
        "8",
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
                "const:580:8"
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
      "00b51434",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51438",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51454",
      "READ",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51434",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51438",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51454",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af16bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af168c.md#insn-00af16bc) · [`00af16a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af168c.md#insn-00af16a0) · [`00af16a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af168c.md#insn-00af16a4)
- 新版 `00b51440`（命令位置の公開資料なし） · `00b51424`（命令位置の公開資料なし） · `00b51428`（命令位置の公開資料なし）

~~~diff
- 00af16bc ["INT_ADD", "register:40f0:8", ["const:af16bc:8", "const:4:8"]]
- 00af16bc ["CALL", null, ["callee:005896b4:8"]]
+ 00b51440 ["INT_ADD", "register:40f0:8", ["const:b51440:8", "const:4:8"]]
+ 00b51440 ["CALL", null, ["callee:005896b4:8"]]
- 00af16bc bytes 58d4e997
+ 00b51440 bytes 9de0e897
- 00af16a0 ["COPY", "register:40b0:8", ["const:10a0000:8"]]
+ 00b51424 ["COPY", "register:40b0:8", ["const:1125000:8"]]
- 00af16a0 bytes 762d00f0
+ 00b51424 bytes b62e0090
- 00af16a4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b51428 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00af16a4 bytes 682d00f0
+ 00b51428 bytes a82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba71f9901d1dcd117560242c49421a2b"></a>

### [`00af1794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1794.md) → [`00b51518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51518.md) _ZN8firebase4util25StdUnorderedSetToJavaListEP7_JNIEnvRKNSt6__ndk113unordered_setINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 12.50% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af17b8",
      "incomplete_value": true,
      "site": "00af17c4",
      "value": [
        "LOAD",
        "8",
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
                "const:570:8"
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
    "new": null,
    "old": {
      "definition_site": "00af17bc",
      "incomplete_value": true,
      "site": "00af17c4",
      "value": [
        "LOAD",
        "8",
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
                "const:580:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af181c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af17b8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af17bc",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51558",
      "READ",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5153c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51540",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51558",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af17c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1794.md#insn-00af17c4) · [`00af181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1794.md#insn-00af181c) · [`00af1834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1794.md#insn-00af1834)
- 新版 `00b51548`（命令位置の公開資料なし） · `00b515b8`（命令位置の公開資料なし）

~~~diff
- 00af17c4 ["INT_ADD", "register:40f0:8", ["const:af17c4:8", "const:4:8"]]
- 00af17c4 ["CALL", null, ["callee:005896b4:8"]]
+ 00b51548 ["INT_ADD", "register:40f0:8", ["const:b51548:8", "const:4:8"]]
+ 00b51548 ["CALL", null, ["callee:005896b4:8"]]
- 00af17c4 bytes 16d4e997
+ 00b51548 bytes 5be0e897
- 00af181c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af181c ["INT_ADD", "register:40f0:8", ["const:af181c:8", "const:4:8"]]
- 00af181c ["CALLIND", null, ["register:0:8"]]
- 00af181c bytes 00013fd6
- 00af1834 ["INT_ADD", "register:40f0:8", ["const:af1834:8", "const:4:8"]]
- 00af1834 ["CALL", null, ["callee:00497a08:8"]]
+ 00b515b8 ["INT_ADD", "register:40f0:8", ["const:b515b8:8", "const:4:8"]]
+ 00b515b8 ["CALL", null, ["callee:00497a08:8"]]
- 00af1834 bytes cf0ce697
+ 00b515b8 bytes 1419e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e4efd68f4bb9957d8fb77070afa643"></a>

### [`00af188c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af188c.md) → [`00b51610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51610.md) _ZN8firebase4util19VariantMapToJavaMapEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5b0.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5c0.md)
- 新版 呼出元 1件 [`00c5b030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b030.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 72.04% / 新版 72.04%

CFGの説明率　旧版 16.67% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af19c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b51748"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": null,
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
      "unmatched:00af18b0",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af18b4",
      "READ",
      [
        "storage",
        "010a0860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51648",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51634",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51638",
      "READ",
      [
        "storage",
        "01125720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51648",
      "READ",
      [
        "storage",
        "01125848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af18bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af188c.md#insn-00af18bc) · [`00af1900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af188c.md#insn-00af1900) · [`00af191c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af188c.md#insn-00af191c)
- 新版 `00b51640`（命令位置の公開資料なし） · `00b51684`（命令位置の公開資料なし） · `00b516a0`（命令位置の公開資料なし）

~~~diff
- 00af18bc ["INT_ADD", "register:40f0:8", ["const:af18bc:8", "const:4:8"]]
- 00af18bc ["CALL", null, ["callee:005896b4:8"]]
+ 00b51640 ["INT_ADD", "register:40f0:8", ["const:b51640:8", "const:4:8"]]
+ 00b51640 ["CALL", null, ["callee:005896b4:8"]]
- 00af18bc bytes d8d3e997
+ 00b51640 bytes 1de0e897
- 00af1900 ["INT_ADD", "register:40f0:8", ["const:af1900:8", "const:4:8"]]
- 00af1900 ["CALL", null, ["callee:00c5b040:8"]]
+ 00b51684 ["INT_ADD", "register:40f0:8", ["const:b51684:8", "const:4:8"]]
+ 00b51684 ["CALL", null, ["callee:00c5b040:8"]]
- 00af1900 bytes 30b30394
+ 00b51684 bytes 6f260494
- 00af191c ["INT_ADD", "register:40f0:8", ["const:af191c:8", "const:4:8"]]
- 00af191c ["CALL", null, ["callee:004977f4:8"]]
+ 00b516a0 ["INT_ADD", "register:40f0:8", ["const:b516a0:8", "const:4:8"]]
+ 00b516a0 ["CALL", null, ["callee:004977f4:8"]]
- 00af191c bytes 100ce697
+ 00b516a0 bytes 5518e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4de8ba8d448703712555486075633c"></a>

### [`00af1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1a00.md) → [`00b51784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51784.md) _ZN8firebase4util19VariantToJavaObjectEP7_JNIEnvRKNS_7VariantE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5c0.md) · 呼出先 7件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) [`00bddcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcd0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5b0.md)
- 新版 呼出元 1件 [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md) · 呼出先 7件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md) [`00c5a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5b030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 32.61% / 新版 57.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51814",
      "incomplete_value": true,
      "site": "00b51818",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51810",
      "incomplete_value": false,
      "site": "00b51818",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1b10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b517b4",
      "DATA",
      [
        "storage",
        "002f5a4a",
        "switchD_00af1a3c::switchdataD_002f5a4a",
        "byte"
      ]
    ],
    [
      "00b517c0",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00af1b18"
      ]
    ],
    [
      "unmatched:00af1a84",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b517b4",
      "DATA",
      [
        "storage",
        "0030b5ba",
        "switchD_00b517c0::switchdataD_0030b5ba",
        "byte"
      ]
    ],
    [
      "00b517c0",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b5189c"
      ]
    ],
    [
      "00b51808",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1a00.md#insn-00af1a94) · [`00af1b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1a00.md#insn-00af1b10) · [`00af1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1a00.md#insn-00af1b30)
- 新版 `00b51818`（命令位置の公開資料なし） · `00b518b4`（命令位置の公開資料なし）

~~~diff
- 00af1a94 ["INT_ADD", "register:40f0:8", ["const:af1a94:8", "const:4:8"]]
- 00af1a94 ["CALL", null, ["callee:00c5a700:8"]]
+ 00b51818 ["INT_ADD", "register:40f0:8", ["const:b51818:8", "const:4:8"]]
+ 00b51818 ["CALL", null, ["callee:00c5a700:8"]]
- 00af1a94 bytes 87b00394
+ 00b51818 bytes ba230494
- 00af1b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1b10 ["INT_ADD", "register:40f0:8", ["const:af1b10:8", "const:4:8"]]
- 00af1b10 ["CALLIND", null, ["register:0:8"]]
- 00af1b10 bytes 00013fd6
- 00af1b30 ["INT_ADD", "register:40f0:8", ["const:af1b30:8", "const:4:8"]]
- 00af1b30 ["CALL", null, ["callee:00c5a700:8"]]
+ 00b518b4 ["INT_ADD", "register:40f0:8", ["const:b518b4:8", "const:4:8"]]
+ 00b518b4 ["CALL", null, ["callee:00c5a700:8"]]
- 00af1b30 bytes 60b00394
+ 00b518b4 bytes 93230494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f7796414aab457abce9f7c049f2703"></a>

### [`00af1f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1f2c.md) → [`00b51cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51cb0.md) _ZN8firebase4util15JavaMapToStdMapEP7_JNIEnvPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4lessISA_EEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.74% / 新版 92.74%

CFGの説明率　旧版 84.72% / 新版 83.56%

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
      "site": "00af20bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b51e40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af1f6c",
      "incomplete_value": true,
      "site": "00af1f74",
      "value": [
        "LOAD",
        "8",
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
                "const:998:8"
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
      "00b51cf0",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51d3c",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51d8c",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51cf0",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51d3c",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51d8c",
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

- 旧版 [`00af1f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1f2c.md#insn-00af1f74) · [`00af1fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1f2c.md#insn-00af1fc4) · [`00af2018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1f2c.md#insn-00af2018)
- 新版 `00b51cf8`（命令位置の公開資料なし） · `00b51d48`（命令位置の公開資料なし） · `00b51d9c`（命令位置の公開資料なし）

~~~diff
- 00af1f74 ["INT_ADD", "register:40f0:8", ["const:af1f74:8", "const:4:8"]]
- 00af1f74 ["CALL", null, ["callee:004977f4:8"]]
+ 00b51cf8 ["INT_ADD", "register:40f0:8", ["const:b51cf8:8", "const:4:8"]]
+ 00b51cf8 ["CALL", null, ["callee:004977f4:8"]]
- 00af1f74 bytes 7a0ae697
+ 00b51cf8 bytes bf16e597
- 00af1fc4 ["INT_ADD", "register:40f0:8", ["const:af1fc4:8", "const:4:8"]]
- 00af1fc4 ["CALL", null, ["callee:004977f4:8"]]
+ 00b51d48 ["INT_ADD", "register:40f0:8", ["const:b51d48:8", "const:4:8"]]
+ 00b51d48 ["CALL", null, ["callee:004977f4:8"]]
- 00af1fc4 bytes 660ae697
+ 00b51d48 bytes ab16e597
- 00af2018 ["INT_ADD", "register:40f0:8", ["const:af2018:8", "const:4:8"]]
- 00af2018 ["CALL", null, ["callee:00497a08:8"]]
+ 00b51d9c ["INT_ADD", "register:40f0:8", ["const:b51d9c:8", "const:4:8"]]
+ 00b51d9c ["CALL", null, ["callee:00497a08:8"]]
- 00af2018 bytes d60ae697
+ 00b51d9c bytes 1b17e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecc0b55da73bb5e636d84ec205ac8fe8"></a>

### [`00af2504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2504.md) → [`00b52288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52288.md) FUN_00b52288

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af2500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2500.md) [`00af2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md)
- 新版 呼出元 2件 [`00b52284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52284.md) [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.08% / 新版 88.08%

CFGの説明率　旧版 72.73% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2734"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b524b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b522c8",
      "incomplete_value": true,
      "site": "00b522d0",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00af2544",
      "incomplete_value": true,
      "site": "00af254c",
      "value": [
        "LOAD",
        "8",
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
                "const:998:8"
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
      "00b522c8",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52314",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52364",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b522c8",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52314",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52364",
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

- 旧版 [`00af254c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2504.md#insn-00af254c) · [`00af259c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2504.md#insn-00af259c) · [`00af25f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2504.md#insn-00af25f0)
- 新版 `00b522d0`（命令位置の公開資料なし） · `00b52320`（命令位置の公開資料なし） · `00b52374`（命令位置の公開資料なし）

~~~diff
- 00af254c ["INT_ADD", "register:40f0:8", ["const:af254c:8", "const:4:8"]]
- 00af254c ["CALL", null, ["callee:004977f4:8"]]
+ 00b522d0 ["INT_ADD", "register:40f0:8", ["const:b522d0:8", "const:4:8"]]
+ 00b522d0 ["CALL", null, ["callee:004977f4:8"]]
- 00af254c bytes 0409e697
+ 00b522d0 bytes 4915e597
- 00af259c ["INT_ADD", "register:40f0:8", ["const:af259c:8", "const:4:8"]]
- 00af259c ["CALL", null, ["callee:004977f4:8"]]
+ 00b52320 ["INT_ADD", "register:40f0:8", ["const:b52320:8", "const:4:8"]]
+ 00b52320 ["CALL", null, ["callee:004977f4:8"]]
- 00af259c bytes f008e697
+ 00b52320 bytes 3515e597
- 00af25f0 ["INT_ADD", "register:40f0:8", ["const:af25f0:8", "const:4:8"]]
- 00af25f0 ["CALL", null, ["callee:00497a08:8"]]
+ 00b52374 ["INT_ADD", "register:40f0:8", ["const:b52374:8", "const:4:8"]]
+ 00b52374 ["CALL", null, ["callee:00497a08:8"]]
- 00af25f0 bytes 6009e697
+ 00b52374 bytes a515e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6456d9c3cfe9156003b8d730f95ba5"></a>

### [`00af2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md) → [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) _ZN8firebase4util19JavaObjectToVariantEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde590.md) · 呼出先 19件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md)
- 新版 呼出元 1件 [`00c5b010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b010.md) · 呼出先 19件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 82.35% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b52a68"
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
      "00b525c4",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52620",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52640",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b525c4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52620",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52640",
      "READ",
      [
        "storage",
        "01125630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md#insn-00af2850) · [`00af28ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md#insn-00af28ac) · [`00af2938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md#insn-00af2938)
- 新版 `00b525d4`（命令位置の公開資料なし） · `00b52630`（命令位置の公開資料なし） · `00b526bc`（命令位置の公開資料なし）

~~~diff
- 00af2850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af2850 ["INT_ADD", "register:40f0:8", ["const:af2850:8", "const:4:8"]]
- 00af2850 ["CALLIND", null, ["register:0:8"]]
+ 00b525d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b525d4 ["INT_ADD", "register:40f0:8", ["const:b525d4:8", "const:4:8"]]
+ 00b525d4 ["CALLIND", null, ["register:0:8"]]
- 00af2850 bytes 00013fd6
+ 00b525d4 bytes 00013fd6
- 00af28ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00af28ac ["INT_ADD", "register:40f0:8", ["const:af28ac:8", "const:4:8"]]
- 00af28ac ["CALLIND", null, ["register:0:8"]]
+ 00b52630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52630 ["INT_ADD", "register:40f0:8", ["const:b52630:8", "const:4:8"]]
+ 00b52630 ["CALLIND", null, ["register:0:8"]]
- 00af28ac bytes 00013fd6
+ 00b52630 bytes 00013fd6
- 00af2938 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af2938 ["INT_ADD", "register:40f0:8", ["const:af2938:8", "const:4:8"]]
- 00af2938 ["CALLIND", null, ["register:0:8"]]
+ 00b526bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b526bc ["INT_ADD", "register:40f0:8", ["const:b526bc:8", "const:4:8"]]
+ 00b526bc ["CALLIND", null, ["register:0:8"]]
- 00af2938 bytes 00013fd6
+ 00b526bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214b67dcaf6150aa8e1d31e2b1ae438f"></a>

### [`00af2f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md) → [`00b52ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52ca4.md) _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde650.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0d0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.38% / 新版 74.38%

CFGの説明率　旧版 29.73% / 新版 20.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af30b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b52e3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2f84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52ce4",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af2f84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b52d2c"
      ]
    ],
    [
      "00b52d30",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52ce4",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b52d2c"
      ]
    ],
    [
      "00b52d30",
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

- 旧版 [`00af2f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md#insn-00af2f68) · [`00af2f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md#insn-00af2f7c) · [`00af2f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md#insn-00af2f84)
- 新版 `00b52cec`（命令位置の公開資料なし）

~~~diff
- 00af2f68 ["INT_ADD", "register:40f0:8", ["const:af2f68:8", "const:4:8"]]
- 00af2f68 ["CALL", null, ["callee:004977f4:8"]]
+ 00b52cec ["INT_ADD", "register:40f0:8", ["const:b52cec:8", "const:4:8"]]
+ 00b52cec ["CALL", null, ["callee:004977f4:8"]]
- 00af2f68 bytes 7d06e697
+ 00b52cec bytes c212e597
- 00af2f7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af2f7c ["INT_ADD", "register:40f0:8", ["const:af2f7c:8", "const:4:8"]]
- 00af2f7c ["CALLIND", null, ["register:0:8"]]
- 00af2f7c bytes 00013fd6
- 00af2f84 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00af2f84 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d7ffdb5d078914333f42d371c0a05d5"></a>

### [`00af31d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31d4.md) → [`00b52f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f58.md) _ZN8firebase4util23VariantVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde640.md) · 呼出先 3件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5c0.md)
- 新版 呼出元 1件 [`00c5b0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0c0.md) · 呼出先 3件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.93% / 新版 37.93%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af31d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af31d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af31d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af31d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af31d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af31dc",
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
      "00b52f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b52f5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b52f60",
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

- 旧版 [`00af31d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31d4.md#insn-00af31d4) · [`00af31d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31d4.md#insn-00af31d8) · [`00af31dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31d4.md#insn-00af31dc)

~~~diff
- 00af31d4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af31d4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af31d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af31d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af31d4 bytes f85fbca9
- 00af31d8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af31d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af31d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af31d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af31d8 bytes f65701a9
- 00af31dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af31dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af31dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af31dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af31dc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-706a8f361ae1bf141e4ef82f4008ccef"></a>

### [`00af32bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md) → [`00b53040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md) _ZN8firebase4util25JavaListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_IS

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.64% / 新版 68.64%

CFGの説明率　旧版 7.14% / 新版 3.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 5件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af32c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af32c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af32c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af32c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af32c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af32c8",
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
      "00b53044",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b53048",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5304c",
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

- 旧版 [`00af32c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md#insn-00af32c0) · [`00af32c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md#insn-00af32c4) · [`00af32c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md#insn-00af32c8)

~~~diff
- 00af32c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af32c0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af32c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af32c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af32c0 bytes fa6702a9
- 00af32c4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af32c4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af32c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00af32c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af32c4 bytes f85f03a9
- 00af32c8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af32c8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af32c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af32c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af32c8 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52de16660f1c93f7866ed4b35bc416fc"></a>

### [`00af35a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md) → [`00b53328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md) _ZN8firebase4util31JavaObjectListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.56% / 新版 84.56%

CFGの説明率　旧版 91.43% / 新版 78.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af35a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af35a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af35ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af35a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af35ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af35b0",
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
      "00b5332c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b53330",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b53334",
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

- 旧版 [`00af35a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md#insn-00af35a8) · [`00af35ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md#insn-00af35ac) · [`00af35b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md#insn-00af35b0)

~~~diff
- 00af35a8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00af35a8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00af35a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af35a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af35a8 bytes fc6f02a9
- 00af35ac ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af35ac ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af35ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00af35ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af35ac bytes fa6703a9
- 00af35b0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af35b0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af35b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af35b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af35b0 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21eeeefcec0bff35cf52ae96365e97b7"></a>

### [`00af37f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af37f8.md) → [`00b5357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5357c.md) _ZN8firebase4util17JniObjectToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53598",
      "incomplete_value": true,
      "site": "00b535a0",
      "value": [
        "LOAD",
        "8",
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3814",
      "incomplete_value": true,
      "site": "00af381c",
      "value": [
        "LOAD",
        "8",
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
                "const:a98:8"
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
      "00b53598",
      "READ",
      [
        "storage",
        "010a0a98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af389c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00af38a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b1c0"
      ]
    ]
  ],
  "added": [
    [
      "00b53598",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53620",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53628",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b1c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af381c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af37f8.md#insn-00af381c) · [`00af3810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af37f8.md#insn-00af3810) · [`00af3814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af37f8.md#insn-00af3814)
- 新版 `00b535a0`（命令位置の公開資料なし） · `00b53594`（命令位置の公開資料なし） · `00b53598`（命令位置の公開資料なし）

~~~diff
- 00af381c ["INT_ADD", "register:40f0:8", ["const:af381c:8", "const:4:8"]]
- 00af381c ["CALL", null, ["callee:004977f4:8"]]
+ 00b535a0 ["INT_ADD", "register:40f0:8", ["const:b535a0:8", "const:4:8"]]
+ 00b535a0 ["CALL", null, ["callee:004977f4:8"]]
- 00af381c bytes 5004e697
+ 00b535a0 bytes 9510e597
- 00af3810 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b53594 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00af3810 bytes 682d00b0
+ 00b53594 bytes 882e00d0
- 00af3814 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 00af3814 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53598 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:958:8"]]
+ 00b53598 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af3814 bytes 024d45f9
+ 00b53598 bytes 02ad44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46a8f7d7104527e9eaf4bf5d69c17f2f"></a>

### [`00af38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md) → [`00b5362c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md) _ZN8firebase4util21JavaListToVariantListEP7_JNIEnvPNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEEP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde620.md) · 呼出先 8件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00c5b0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0a0.md) · 呼出先 8件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.86% / 新版 64.86%

CFGの説明率　旧版 9.52% / 新版 5.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af38ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af38b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af38b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af38ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af38b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af38b4",
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
      "00b53630",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b53634",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b53638",
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

- 旧版 [`00af38ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md#insn-00af38ac) · [`00af38b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md#insn-00af38b0) · [`00af38b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md#insn-00af38b4)

~~~diff
- 00af38ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00af38ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00af38ac bytes fb1300f9
- 00af38b0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af38b0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af38b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00af38b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af38b0 bytes fa6703a9
- 00af38b4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af38b4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af38b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af38b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af38b4 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-797e6d9d770208e75e67bfd0a87a06b0"></a>

### [`00af3c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3c14.md) → [`00b53998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53998.md) _ZN8firebase4util8IsJArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3c14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3c18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3c18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af3c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af3c18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af3c1c",
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
      "00b53998",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5399c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b539a0",
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

- 旧版 [`00af3c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3c14.md#insn-00af3c14) · [`00af3c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3c14.md#insn-00af3c18) · [`00af3c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3c14.md#insn-00af3c1c)

~~~diff
- 00af3c14 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af3c14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af3c14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af3c14 bytes f50f1df8
- 00af3c18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af3c18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af3c18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af3c18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af3c18 bytes f44f01a9
- 00af3c1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af3c1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af3c1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af3c1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af3c1c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e930cc08410ac948a95684b8fee36dcd"></a>

### [`00af3cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3cb8.md) → [`00b53a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53a3c.md) _ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af3ce4",
      "incomplete_value": true,
      "site": "00af3cec",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af3ce0",
      "incomplete_value": true,
      "site": "00af3cec",
      "value": [
        "LOAD",
        "8",
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
                "const:6b0:8"
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
      "00b53a64",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af3cd8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53a64",
      "READ",
      [
        "storage",
        "01125570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53a5c",
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

- 旧版 [`00af3cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3cb8.md#insn-00af3cd8) · [`00af3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3cb8.md#insn-00af3cec)
- 新版 `00b53a70`（命令位置の公開資料なし） · `00b53a5c`（命令位置の公開資料なし）

~~~diff
- 00af3cd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af3cd8 ["INT_ADD", "register:40f0:8", ["const:af3cd8:8", "const:4:8"]]
- 00af3cd8 ["CALLIND", null, ["register:0:8"]]
- 00af3cd8 bytes 20013fd6
- 00af3cec ["INT_ADD", "register:40f0:8", ["const:af3cec:8", "const:4:8"]]
- 00af3cec ["CALL", null, ["callee:004977f4:8"]]
+ 00b53a70 ["INT_ADD", "register:40f0:8", ["const:b53a70:8", "const:4:8"]]
+ 00b53a70 ["CALL", null, ["callee:004977f4:8"]]
- 00af3cec bytes 1c03e697
+ 00b53a70 bytes 610fe597
+ 00b53a5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b53a5c ["INT_ADD", "register:40f0:8", ["const:b53a5c:8", "const:4:8"]]
+ 00b53a5c ["CALLIND", null, ["register:0:8"]]
+ 00b53a5c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b6d00054fd424d98d957d51df805964"></a>

### [`00af3d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3d5c.md) → [`00b53ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ae0.md) _ZN8firebase4util14JBooleanToBoolEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde460.md) · 呼出先 1件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md)
- 新版 呼出元 1件 [`00c5aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aee0.md) · 呼出先 1件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53af0",
      "incomplete_value": true,
      "site": "00b53af8",
      "value": [
        "LOAD",
        "8",
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3d6c",
      "incomplete_value": true,
      "site": "00af3d74",
      "value": [
        "LOAD",
        "8",
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
                "const:5d8:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b53b0c"
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
      "00b53af0",
      "READ",
      [
        "storage",
        "010a05d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af3d88",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53af0",
      "READ",
      [
        "storage",
        "01125498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b0c",
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

- 旧版 [`00af3d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3d5c.md#insn-00af3d74) · [`00af3d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3d5c.md#insn-00af3d88) · [`00af3dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3d5c.md#insn-00af3dc4)
- 新版 `00b53af8`（命令位置の公開資料なし）

~~~diff
- 00af3d74 ["INT_ADD", "register:40f0:8", ["const:af3d74:8", "const:4:8"]]
- 00af3d74 ["CALL", null, ["callee:00497a08:8"]]
+ 00b53af8 ["INT_ADD", "register:40f0:8", ["const:b53af8:8", "const:4:8"]]
+ 00b53af8 ["CALL", null, ["callee:00497a08:8"]]
- 00af3d74 bytes 7f03e697
+ 00b53af8 bytes c40fe597
- 00af3d88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3d88 ["INT_ADD", "register:40f0:8", ["const:af3d88:8", "const:4:8"]]
- 00af3d88 ["CALLIND", null, ["register:0:8"]]
- 00af3d88 bytes 00013fd6
- 00af3dc4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af3dc4 ["RETURN", null, ["register:0:8"]]
- 00af3dc4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51cafcd9e61a63a6ebeb3a274e0f7baa"></a>

### [`00af3dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3dc8.md) → [`00b53b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53b4c.md) _ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b64",
      "value": [
        "LOAD",
        "8",
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3dd8",
      "incomplete_value": true,
      "site": "00af3de0",
      "value": [
        "LOAD",
        "8",
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
                "const:660:8"
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
      "unmatched:00af3dd8",
      "READ",
      [
        "storage",
        "010a0660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b5c",
      "READ",
      [
        "storage",
        "01125520",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af3de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3dc8.md#insn-00af3de0) · [`00af3dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3dc8.md#insn-00af3dd4) · [`00af3dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3dc8.md#insn-00af3dd8)
- 新版 `00b53b64`（命令位置の公開資料なし） · `00b53b58`（命令位置の公開資料なし）

~~~diff
- 00af3de0 ["INT_ADD", "register:40f0:8", ["const:af3de0:8", "const:4:8"]]
- 00af3de0 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00b53b64 ["INT_ADD", "register:40f0:8", ["const:b53b64:8", "const:4:8"]]
+ 00b53b64 ["CALL", null, ["callee:00c5ae00:8"]]
- 00af3de0 bytes 68a90394
+ 00b53b64 bytes a71c0494
- 00af3dd4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b53b58 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00af3dd4 bytes 682d00b0
+ 00b53b58 bytes 882e00d0
- 00af3dd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:660:8"]]
- 00af3dd8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af3dd8 bytes 023143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-037b2629214493d11be9be3c39ed9bfe"></a>

### [`00af3f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3f34.md) → [`00b53cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53cb8.md) _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde390.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae10.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53d28"
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
      "unmatched:00af3f98",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af3fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53d1c",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b53d28",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3f34.md#insn-00af3fa4) · [`00af3fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3f34.md#insn-00af3fa8)
- 新版 `00b53d2c`（命令位置の公開資料なし） · `00b53d28`（命令位置の公開資料なし）

~~~diff
- 00af3fa4 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00af3fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00af3fa4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00af3fa4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00af3fa4 bytes a1033dad
- 00af3fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3fa8 ["INT_ADD", "register:40f0:8", ["const:af3fa8:8", "const:4:8"]]
- 00af3fa8 ["CALLIND", null, ["register:0:8"]]
+ 00b53d2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53d2c ["INT_ADD", "register:40f0:8", ["const:b53d2c:8", "const:4:8"]]
+ 00b53d2c ["CALLIND", null, ["register:0:8"]]
- 00af3fa8 bytes 00013fd6
+ 00b53d2c bytes 00013fd6
+ 00b53d28 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
+ 00b53d28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
+ 00b53d28 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00b53d28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
+ 00b53d28 bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-374ac9adf9e8c8aa8f9101079d361ac2"></a>

### [`00af3fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3fd0.md) → [`00b53d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53d54.md) _ZN8firebase4util13JShortToInt16EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 33.33% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4004"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b53d88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53d64",
      "incomplete_value": true,
      "site": "00b53d6c",
      "value": [
        "LOAD",
        "8",
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
                "const:8c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3fe0",
      "incomplete_value": true,
      "site": "00af3fe8",
      "value": [
        "LOAD",
        "8",
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
                "const:a00:8"
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
      "unmatched:00af3fe0",
      "READ",
      [
        "storage",
        "010a0a00",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af4004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53dac"
      ]
    ]
  ],
  "added": [
    [
      "00b53d64",
      "READ",
      [
        "storage",
        "011258c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53dac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af3fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3fd0.md#insn-00af3fe8) · [`00af4004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3fd0.md#insn-00af4004)
- 新版 `00b53d6c`（命令位置の公開資料なし） · `00b53d88`（命令位置の公開資料なし）

~~~diff
- 00af3fe8 ["INT_ADD", "register:40f0:8", ["const:af3fe8:8", "const:4:8"]]
- 00af3fe8 ["CALL", null, ["callee:00c5ae20:8"]]
+ 00b53d6c ["INT_ADD", "register:40f0:8", ["const:b53d6c:8", "const:4:8"]]
+ 00b53d6c ["CALL", null, ["callee:00c5ae20:8"]]
- 00af3fe8 bytes eea80394
+ 00b53d6c bytes 2d1c0494
- 00af4004 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00af4004 bytes 20010054
+ 00b53d88 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00b53d88 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52341c96a4f8adf1acbe4879713bb88"></a>

### [`00af413c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af413c.md) → [`00b53ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md) _ZN8firebase4util12JLongToInt64EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde050.md) · 呼出先 1件 [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md)
- 新版 呼出元 1件 [`00c5aad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aad0.md) · 呼出先 1件 [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 33.33% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af413c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af413c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4140"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af413c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af4140",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53ed0",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53ed0",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af413c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af413c.md#insn-00af413c) · [`00af4140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af413c.md#insn-00af4140) · [`00af4154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af413c.md#insn-00af4154)
- 新版 `00b53ed8`（命令位置の公開資料なし）

~~~diff
- 00af413c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af413c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af413c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af413c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af413c bytes f44fbea9
- 00af4140 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af4140 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af4140 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af4140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af4140 bytes fd7b01a9
- 00af4154 ["INT_ADD", "register:40f0:8", ["const:af4154:8", "const:4:8"]]
- 00af4154 ["CALL", null, ["callee:0058f55c:8"]]
+ 00b53ed8 ["INT_ADD", "register:40f0:8", ["const:b53ed8:8", "const:4:8"]]
+ 00b53ed8 ["CALL", null, ["callee:0058f55c:8"]]
- 00af4154 bytes 5ce1e997
+ 00b53ed8 bytes a1ede897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cabe89ec478c52eb642ba910fd729462"></a>

### [`00af41a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af41a4.md) → [`00b53f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f28.md) _ZN8firebase4util13JFloatToFloatEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53f3c",
      "incomplete_value": true,
      "site": "00b53f44",
      "value": [
        "LOAD",
        "8",
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af41b8",
      "incomplete_value": true,
      "site": "00af41c0",
      "value": [
        "LOAD",
        "8",
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
                "const:840:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af41d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b53f58"
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
      "00b53f3c",
      "READ",
      [
        "storage",
        "010a0840",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af41d4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53f3c",
      "READ",
      [
        "storage",
        "01125700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f58",
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

- 旧版 [`00af41c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af41a4.md#insn-00af41c0) · [`00af41d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af41a4.md#insn-00af41d4)
- 新版 `00b53f44`（命令位置の公開資料なし） · `00b53f58`（命令位置の公開資料なし）

~~~diff
- 00af41c0 ["INT_ADD", "register:40f0:8", ["const:af41c0:8", "const:4:8"]]
- 00af41c0 ["CALL", null, ["callee:0057bdcc:8"]]
+ 00b53f44 ["INT_ADD", "register:40f0:8", ["const:b53f44:8", "const:4:8"]]
+ 00b53f44 ["CALL", null, ["callee:0057bdcc:8"]]
- 00af41c0 bytes 5d93e997
+ 00b53f44 bytes a29fe897
- 00af41d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af41d4 ["INT_ADD", "register:40f0:8", ["const:af41d4:8", "const:4:8"]]
- 00af41d4 ["CALLIND", null, ["register:0:8"]]
- 00af41d4 bytes 00013fd6
+ 00b53f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53f58 ["INT_ADD", "register:40f0:8", ["const:b53f58:8", "const:4:8"]]
+ 00b53f58 ["CALLIND", null, ["register:0:8"]]
+ 00b53f58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd9110d85c74b3bcd7771e33b6da1172"></a>

### [`00af4214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4214.md) → [`00b53f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53f98.md) _ZN8firebase4util15JDoubleToDoubleEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53fac",
      "incomplete_value": true,
      "site": "00b53fb4",
      "value": [
        "LOAD",
        "8",
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
                "const:658:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4244"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af425c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53fac",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af4244",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00af425c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53fac",
      "READ",
      [
        "storage",
        "01125658",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fc8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b53fe0",
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

- 旧版 [`00af4230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4214.md#insn-00af4230) · [`00af4244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4214.md#insn-00af4244) · [`00af425c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4214.md#insn-00af425c)
- 新版 `00b53fb4`（命令位置の公開資料なし）

~~~diff
- 00af4230 ["INT_ADD", "register:40f0:8", ["const:af4230:8", "const:4:8"]]
- 00af4230 ["CALL", null, ["callee:00c5ae30:8"]]
+ 00b53fb4 ["INT_ADD", "register:40f0:8", ["const:b53fb4:8", "const:4:8"]]
+ 00b53fb4 ["CALL", null, ["callee:00c5ae30:8"]]
- 00af4230 bytes 60a80394
+ 00b53fb4 bytes 9f1b0494
- 00af4244 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4244 ["INT_ADD", "register:40f0:8", ["const:af4244:8", "const:4:8"]]
- 00af4244 ["CALLIND", null, ["register:0:8"]]
- 00af4244 bytes 00013fd6
- 00af425c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af425c ["INT_ADD", "register:40f0:8", ["const:af425c:8", "const:4:8"]]
- 00af425c ["CALLIND", null, ["register:0:8"]]
- 00af425c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc486c82dc4cda02595e4f3c55fc40f"></a>

### [`00af4320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4320.md) → [`00b540a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b540a4.md) _ZN8firebase4util15IsJBooleanArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b540c0",
      "incomplete_value": false,
      "site": "00b540cc",
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
            "const:f4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af433c",
      "incomplete_value": false,
      "site": "00af4348",
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
            "const:d71:8"
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
      "00b540c0",
      "PARAM",
      [
        "storage",
        "0029bd71",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b540c0",
      "PARAM",
      [
        "storage",
        "002abf4e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4320.md#insn-00af4348) · [`00af4338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4320.md#insn-00af4338) · [`00af433c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4320.md#insn-00af433c)
- 新版 `00b540cc`（命令位置の公開資料なし） · `00b540bc`（命令位置の公開資料なし） · `00b540c0`（命令位置の公開資料なし）

~~~diff
- 00af4348 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4348 ["INT_ADD", "register:40f0:8", ["const:af4348:8", "const:4:8"]]
- 00af4348 ["CALLIND", null, ["register:0:8"]]
+ 00b540cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b540cc ["INT_ADD", "register:40f0:8", ["const:b540cc:8", "const:4:8"]]
+ 00b540cc ["CALLIND", null, ["register:0:8"]]
- 00af4348 bytes 00013fd6
+ 00b540cc bytes 00013fd6
- 00af4338 ["COPY", "register:4008:8", ["const:29b000:8"]]
+ 00b540bc ["COPY", "register:4008:8", ["const:2ab000:8"]]
- 00af4338 bytes 21bdfff0
+ 00b540bc bytes a1bafff0
- 00af433c ["COPY", "tmp:0:8", ["const:d71:8"]]
- 00af433c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af433c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af433c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b540c0 ["COPY", "tmp:0:8", ["const:f4e:8"]]
+ 00b540c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b540c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b540c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af433c bytes 21c43591
+ 00b540c0 bytes 21383d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3e1784a53f3fbe58ae687deea1b67d"></a>

### [`00af4398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4398.md) → [`00b5411c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5411c.md) _ZN8firebase4util12IsJByteArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54138",
      "incomplete_value": false,
      "site": "00b54144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af43b4",
      "incomplete_value": false,
      "site": "00af43c0",
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
            "const:fab:8"
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
      "00b54138",
      "PARAM",
      [
        "storage",
        "002aafab",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54138",
      "PARAM",
      [
        "storage",
        "002bbd74",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af43c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4398.md#insn-00af43c0) · [`00af43b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4398.md#insn-00af43b0) · [`00af43b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4398.md#insn-00af43b4)
- 新版 `00b54144`（命令位置の公開資料なし） · `00b54134`（命令位置の公開資料なし） · `00b54138`（命令位置の公開資料なし）

~~~diff
- 00af43c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af43c0 ["INT_ADD", "register:40f0:8", ["const:af43c0:8", "const:4:8"]]
- 00af43c0 ["CALLIND", null, ["register:0:8"]]
+ 00b54144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54144 ["INT_ADD", "register:40f0:8", ["const:b54144:8", "const:4:8"]]
+ 00b54144 ["CALLIND", null, ["register:0:8"]]
- 00af43c0 bytes 00013fd6
+ 00b54144 bytes 00013fd6
- 00af43b0 ["COPY", "register:4008:8", ["const:2aa000:8"]]
+ 00b54134 ["COPY", "register:4008:8", ["const:2bb000:8"]]
- 00af43b0 bytes a1bdffd0
+ 00b54134 bytes 21bbfff0
- 00af43b4 ["COPY", "tmp:0:8", ["const:fab:8"]]
- 00af43b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af43b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af43b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b54138 ["COPY", "tmp:0:8", ["const:d74:8"]]
+ 00b54138 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54138 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54138 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af43b4 bytes 21ac3e91
+ 00b54138 bytes 21d03591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bedb6e74c77be08113e0e5ea020ac7eb"></a>

### [`00af4410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4410.md) → [`00b54194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54194.md) _ZN8firebase4util12IsJCharArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b541b0",
      "incomplete_value": false,
      "site": "00b541bc",
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
            "const:bd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af442c",
      "incomplete_value": false,
      "site": "00af4438",
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
      "00b541b0",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b541b0",
      "PARAM",
      [
        "storage",
        "002b6bd1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4410.md#insn-00af4438) · [`00af4428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4410.md#insn-00af4428) · [`00af442c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4410.md#insn-00af442c)
- 新版 `00b541bc`（命令位置の公開資料なし） · `00b541ac`（命令位置の公開資料なし） · `00b541b0`（命令位置の公開資料なし）

~~~diff
- 00af4438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4438 ["INT_ADD", "register:40f0:8", ["const:af4438:8", "const:4:8"]]
- 00af4438 ["CALLIND", null, ["register:0:8"]]
+ 00b541bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b541bc ["INT_ADD", "register:40f0:8", ["const:b541bc:8", "const:4:8"]]
+ 00b541bc ["CALLIND", null, ["register:0:8"]]
- 00af4438 bytes 00013fd6
+ 00b541bc bytes 00013fd6
- 00af4428 ["COPY", "register:4008:8", ["const:2a6000:8"]]
+ 00b541ac ["COPY", "register:4008:8", ["const:2b6000:8"]]
- 00af4428 bytes 81bdffd0
+ 00b541ac bytes 01bbffd0
- 00af442c ["COPY", "tmp:0:8", ["const:10d:8"]]
- 00af442c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af442c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af442c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b541b0 ["COPY", "tmp:0:8", ["const:bd1:8"]]
+ 00b541b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b541b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b541b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af442c bytes 21340491
+ 00b541b0 bytes 21442f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1fda5c03ed6d1058dbb50b508f4a9bd"></a>

### [`00af4488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4488.md) → [`00b5420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b5420c.md) _ZN8firebase4util13IsJShortArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54228",
      "incomplete_value": false,
      "site": "00b54234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:58b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af44a4",
      "incomplete_value": false,
      "site": "00af44b0",
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
            "const:d74:8"
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
      "00b54228",
      "PARAM",
      [
        "storage",
        "002a3d74",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54228",
      "PARAM",
      [
        "storage",
        "002b458b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af44b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4488.md#insn-00af44b0) · [`00af44a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4488.md#insn-00af44a0) · [`00af44a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4488.md#insn-00af44a4)
- 新版 `00b54234`（命令位置の公開資料なし） · `00b54224`（命令位置の公開資料なし） · `00b54228`（命令位置の公開資料なし）

~~~diff
- 00af44b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af44b0 ["INT_ADD", "register:40f0:8", ["const:af44b0:8", "const:4:8"]]
- 00af44b0 ["CALLIND", null, ["register:0:8"]]
+ 00b54234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54234 ["INT_ADD", "register:40f0:8", ["const:b54234:8", "const:4:8"]]
+ 00b54234 ["CALLIND", null, ["register:0:8"]]
- 00af44b0 bytes 00013fd6
+ 00b54234 bytes 00013fd6
- 00af44a0 ["COPY", "register:4008:8", ["const:2a3000:8"]]
+ 00b54224 ["COPY", "register:4008:8", ["const:2b4000:8"]]
- 00af44a0 bytes 61bdfff0
+ 00b54224 bytes 01bbff90
- 00af44a4 ["COPY", "tmp:0:8", ["const:d74:8"]]
- 00af44a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af44a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af44a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b54228 ["COPY", "tmp:0:8", ["const:58b:8"]]
+ 00b54228 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54228 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b54228 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af44a4 bytes 21d03591
+ 00b54228 bytes 212c1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ec43d7bf8170f14aff10b0e8919c01"></a>

### [`00af4500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4500.md) → [`00b54284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54284.md) _ZN8firebase4util11IsJIntArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b542a0",
      "incomplete_value": false,
      "site": "00b542ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af451c",
      "incomplete_value": false,
      "site": "00af4528",
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
            "const:fbd:8"
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
      "00b542a0",
      "PARAM",
      [
        "storage",
        "002a9fbd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b542a0",
      "PARAM",
      [
        "storage",
        "002bad56",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4500.md#insn-00af4528) · [`00af4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4500.md#insn-00af4518) · [`00af451c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4500.md#insn-00af451c)
- 新版 `00b542ac`（命令位置の公開資料なし） · `00b5429c`（命令位置の公開資料なし） · `00b542a0`（命令位置の公開資料なし）

~~~diff
- 00af4528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4528 ["INT_ADD", "register:40f0:8", ["const:af4528:8", "const:4:8"]]
- 00af4528 ["CALLIND", null, ["register:0:8"]]
+ 00b542ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b542ac ["INT_ADD", "register:40f0:8", ["const:b542ac:8", "const:4:8"]]
+ 00b542ac ["CALLIND", null, ["register:0:8"]]
- 00af4528 bytes 00013fd6
+ 00b542ac bytes 00013fd6
- 00af4518 ["COPY", "register:4008:8", ["const:2a9000:8"]]
+ 00b5429c ["COPY", "register:4008:8", ["const:2ba000:8"]]
- 00af4518 bytes a1bdffb0
+ 00b5429c bytes 21bbffd0
- 00af451c ["COPY", "tmp:0:8", ["const:fbd:8"]]
- 00af451c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af451c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af451c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b542a0 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 00b542a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b542a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b542a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af451c bytes 21f43e91
+ 00b542a0 bytes 21583591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cd99187372e1021ce428c3b93821674"></a>

### [`00af45f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af45f0.md) → [`00b54374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54374.md) _ZN8firebase4util13IsJFloatArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54390",
      "incomplete_value": false,
      "site": "00b5439c",
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
            "const:6b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af460c",
      "incomplete_value": false,
      "site": "00af4618",
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
            "const:74a:8"
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
      "site": "00af4634"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4650"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af460c",
      "PARAM",
      [
        "storage",
        "0029a74a",
        null,
        null
      ]
    ],
    [
      "unmatched:00af4634",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00af4650",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54390",
      "PARAM",
      [
        "storage",
        "002aa6b7",
        null,
        null
      ]
    ],
    [
      "00b543b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b543d4",
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

- 旧版 [`00af4618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af45f0.md#insn-00af4618) · [`00af4634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af45f0.md#insn-00af4634) · [`00af4650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af45f0.md#insn-00af4650)
- 新版 `00b5439c`（命令位置の公開資料なし）

~~~diff
- 00af4618 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4618 ["INT_ADD", "register:40f0:8", ["const:af4618:8", "const:4:8"]]
- 00af4618 ["CALLIND", null, ["register:0:8"]]
+ 00b5439c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5439c ["INT_ADD", "register:40f0:8", ["const:b5439c:8", "const:4:8"]]
+ 00b5439c ["CALLIND", null, ["register:0:8"]]
- 00af4618 bytes 00013fd6
+ 00b5439c bytes 00013fd6
- 00af4634 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4634 ["INT_ADD", "register:40f0:8", ["const:af4634:8", "const:4:8"]]
- 00af4634 ["CALLIND", null, ["register:0:8"]]
- 00af4634 bytes 00013fd6
- 00af4650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4650 ["INT_ADD", "register:40f0:8", ["const:af4650:8", "const:4:8"]]
- 00af4650 ["CALLIND", null, ["register:0:8"]]
- 00af4650 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3a3b7fccad8d8536fbaed17359c1ac"></a>

### [`00af46e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af46e0.md) → [`00b54464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54464.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde630.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0b0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 42.86% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4838"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b545bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af47cc",
      "incomplete_value": true,
      "site": "00af47d0",
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
              [
                "live",
                "register:40b8:8"
              ]
            ]
          ],
          [
            "live",
            "register:40c0:8"
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
      "unmatched:00af4838",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b545e0"
      ]
    ]
  ],
  "added": [
    [
      "00b545bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b545e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af47d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af46e0.md#insn-00af47d0) · [`00af4838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af46e0.md#insn-00af4838) · [`00af4858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af46e0.md#insn-00af4858)
- 新版 `00b54554`（命令位置の公開資料なし）

~~~diff
- 00af47d0 ["INT_ADD", "register:40f0:8", ["const:af47d0:8", "const:4:8"]]
- 00af47d0 ["CALL", null, ["callee:00c5a440:8"]]
+ 00b54554 ["INT_ADD", "register:40f0:8", ["const:b54554:8", "const:4:8"]]
+ 00b54554 ["CALL", null, ["callee:00c5a440:8"]]
- 00af47d0 bytes 88a40394
+ 00b54554 bytes bb170494
- 00af4838 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af4838 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00af4838 bytes 21010054
- 00af4858 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af4858 ["RETURN", null, ["register:0:8"]]
- 00af4858 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

