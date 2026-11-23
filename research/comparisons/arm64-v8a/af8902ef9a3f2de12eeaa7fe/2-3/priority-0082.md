# v16.0.0 → v16.0.1 · 最優先の変更候補 (82)

[一覧の目次](README.md)

<a id="compare-c25ac6c252c5dbc066d337388ae643c7"></a>

### [`00bcf088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md) → [`00bcf4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf254"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcf67c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf4fc",
      "incomplete_value": true,
      "site": "00bcf500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf0d4",
      "incomplete_value": true,
      "site": "00bcf0d8",
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
                "register:4000:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00bcf550",
      "READ",
      [
        "storage",
        "011263c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcf1c4",
      "PARAM",
      [
        "storage",
        "002b36d9",
        null,
        "string"
      ]
    ],
    [
      "00bcf628",
      "READ",
      [
        "storage",
        "00c9b618",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bcf550",
      "READ",
      [
        "storage",
        "011267c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf5ec",
      "PARAM",
      [
        "storage",
        "002b3719",
        null,
        "string"
      ]
    ],
    [
      "00bcf628",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md#insn-00bcf0d8) · [`00bcf13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md#insn-00bcf13c) · [`00bcf180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md#insn-00bcf180)
- 新版 `00bcf500`（命令位置の公開資料なし） · `00bcf564`（命令位置の公開資料なし） · `00bcf5a8`（命令位置の公開資料なし）

~~~diff
- 00bcf0d8 ["INT_ADD", "register:40f0:8", ["const:bcf0d8:8", "const:4:8"]]
- 00bcf0d8 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bcf500 ["INT_ADD", "register:40f0:8", ["const:bcf500:8", "const:4:8"]]
+ 00bcf500 ["CALL", null, ["callee:00c5ae40:8"]]
- 00bcf0d8 bytes 5a2e0294
+ 00bcf500 bytes 502e0294
- 00bcf13c ["INT_ADD", "register:40f0:8", ["const:bcf13c:8", "const:4:8"]]
- 00bcf13c ["CALL", null, ["callee:00497834:8"]]
+ 00bcf564 ["INT_ADD", "register:40f0:8", ["const:bcf564:8", "const:4:8"]]
+ 00bcf564 ["CALL", null, ["callee:00497834:8"]]
- 00bcf13c bytes ae21e397
+ 00bcf564 bytes b420e397
- 00bcf180 ["INT_ADD", "register:40f0:8", ["const:bcf180:8", "const:4:8"]]
- 00bcf180 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bcf5a8 ["INT_ADD", "register:40f0:8", ["const:bcf5a8:8", "const:4:8"]]
+ 00bcf5a8 ["CALL", null, ["callee:00c5b080:8"]]
- 00bcf180 bytes c02e0294
+ 00bcf5a8 bytes b62e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656f8980a51e1eb79104060c6cd666d4"></a>

### [`00bcf2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md) → [`00bcf6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d900.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd00.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 21.43% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf2fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcf2f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf2fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf300",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcf720",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00bcf724",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcf728",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md#insn-00bcf2f8) · [`00bcf2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md#insn-00bcf2fc) · [`00bcf300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md#insn-00bcf300)

~~~diff
- 00bcf2f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcf2f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00bcf2f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bcf2f8 bytes a8831df8
- 00bcf2fc ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bcf2fc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcf2fc ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bcf2fc ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bcf2fc bytes ff7f02a9
- 00bcf300 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bcf300 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcf300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bcf300 bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f608bf22cdc087704e76e7739794aaef"></a>

### [`00bcf3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf3d8.md) → [`00bcf800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf850",
      "incomplete_value": true,
      "site": "00bcf864",
      "value": [
        "LOAD",
        "8",
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf428",
      "incomplete_value": true,
      "site": "00bcf43c",
      "value": [
        "LOAD",
        "8",
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf450"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcf878"
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
      "unmatched:00bcf428",
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcf450",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcf850",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf878",
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

- 旧版 [`00bcf43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf3d8.md#insn-00bcf43c) · [`00bcf450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf3d8.md#insn-00bcf450)
- 新版 `00bcf864`（命令位置の公開資料なし） · `00bcf878`（命令位置の公開資料なし）

~~~diff
- 00bcf43c ["INT_ADD", "register:40f0:8", ["const:bcf43c:8", "const:4:8"]]
- 00bcf43c ["CALL", null, ["callee:00574cec:8"]]
+ 00bcf864 ["INT_ADD", "register:40f0:8", ["const:bcf864:8", "const:4:8"]]
+ 00bcf864 ["CALL", null, ["callee:00574cec:8"]]
- 00bcf43c bytes 1c96e697
+ 00bcf864 bytes 2295e697
- 00bcf450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf450 ["INT_ADD", "register:40f0:8", ["const:bcf450:8", "const:4:8"]]
- 00bcf450 ["CALLIND", null, ["register:0:8"]]
- 00bcf450 bytes 00013fd6
+ 00bcf878 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf878 ["INT_ADD", "register:40f0:8", ["const:bcf878:8", "const:4:8"]]
+ 00bcf878 ["CALLIND", null, ["register:0:8"]]
+ 00bcf878 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdb0998f150a3f0d0193e87122685a39"></a>

### [`00bcf4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md) → [`00bcf924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf924.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHand

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbd0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 14.29% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf988",
      "incomplete_value": false,
      "site": "00bcf98c",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf560",
      "incomplete_value": false,
      "site": "00bcf564",
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
            "const:8:8"
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
      "definition_site": "00bcf990",
      "incomplete_value": true,
      "site": "00bcf9a0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf994",
      "incomplete_value": true,
      "site": "00bcf9a0",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
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
      "unmatched:00bcf560",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf988",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md#insn-00bcf564) · [`00bcf578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md#insn-00bcf578) · [`00bcf584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md#insn-00bcf584)
- 新版 `00bcf98c`（命令位置の公開資料なし） · `00bcf9a0`（命令位置の公開資料なし） · `00bcf9ac`（命令位置の公開資料なし）

~~~diff
- 00bcf564 ["INT_ADD", "register:40f0:8", ["const:bcf564:8", "const:4:8"]]
- 00bcf564 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcf98c ["INT_ADD", "register:40f0:8", ["const:bcf98c:8", "const:4:8"]]
+ 00bcf98c ["CALL", null, ["callee:00c5b000:8"]]
- 00bcf564 bytes a72d0294
+ 00bcf98c bytes 9d2d0294
- 00bcf578 ["INT_ADD", "register:40f0:8", ["const:bcf578:8", "const:4:8"]]
- 00bcf578 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bcf9a0 ["INT_ADD", "register:40f0:8", ["const:bcf9a0:8", "const:4:8"]]
+ 00bcf9a0 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bcf578 bytes 3e2d0294
+ 00bcf9a0 bytes 342d0294
- 00bcf584 ["INT_ADD", "register:40f0:8", ["const:bcf584:8", "const:4:8"]]
- 00bcf584 ["CALL", null, ["callee:00c5ae30:8"]]
+ 00bcf9ac ["INT_ADD", "register:40f0:8", ["const:bcf9ac:8", "const:4:8"]]
+ 00bcf9ac ["CALL", null, ["callee:00c5ae30:8"]]
- 00bcf584 bytes 2b2d0294
+ 00bcf9ac bytes 212d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca8e35bd4b78d0ff0283c28e72f86d5f"></a>

### [`00bcf6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md) → [`00bcfb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfb00.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobje

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7a0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dba0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfb6c",
      "incomplete_value": false,
      "site": "00bcfb70",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf744",
      "incomplete_value": false,
      "site": "00bcf748",
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
            "const:8:8"
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
      "00bcfb6c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcfb6c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md#insn-00bcf748) · [`00bcf70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md#insn-00bcf70c) · [`00bcf718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md#insn-00bcf718)
- 新版 `00bcfb70`（命令位置の公開資料なし） · `00bcfb34`（命令位置の公開資料なし） · `00bcfb40`（命令位置の公開資料なし）

~~~diff
- 00bcf748 ["INT_ADD", "register:40f0:8", ["const:bcf748:8", "const:4:8"]]
- 00bcf748 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcfb70 ["INT_ADD", "register:40f0:8", ["const:bcfb70:8", "const:4:8"]]
+ 00bcfb70 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcf748 bytes 2e2d0294
+ 00bcfb70 bytes 242d0294
- 00bcf70c ["INT_ADD", "register:40f0:8", ["const:bcf70c:8", "const:4:8"]]
- 00bcf70c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcfb34 ["INT_ADD", "register:40f0:8", ["const:bcfb34:8", "const:4:8"]]
+ 00bcfb34 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcf70c bytes bd2b0294
+ 00bcfb34 bytes b32b0294
- 00bcf718 ["INT_ADD", "register:40f0:8", ["const:bcf718:8", "const:4:8"]]
- 00bcf718 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bcfb40 ["INT_ADD", "register:40f0:8", ["const:bcfb40:8", "const:4:8"]]
+ 00bcfb40 ["CALL", null, ["callee:00c5ae80:8"]]
- 00bcf718 bytes da2c0294
+ 00bcfb40 bytes d02c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d68bd0869cd8011c1909789fd65334e"></a>

### [`00bcf9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf9f0.md) → [`00bcfe18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfe18.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12Fut

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d790.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db90.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 9.09% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfe84",
      "incomplete_value": false,
      "site": "00bcfe88",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcfa5c",
      "incomplete_value": false,
      "site": "00bcfa60",
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
            "const:8:8"
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
      "00bcfe5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcfaf4"
      ]
    ],
    [
      "unmatched:00bcfa5c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcfaf4",
      "DATA",
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
      "00bcfe5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcff1c"
      ]
    ],
    [
      "00bcfe84",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bcff1c",
      "DATA",
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

- 旧版 [`00bcfa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf9f0.md#insn-00bcfa60) · [`00bcfa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf9f0.md#insn-00bcfa24) · [`00bcfa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf9f0.md#insn-00bcfa30)
- 新版 `00bcfe88`（命令位置の公開資料なし） · `00bcfe4c`（命令位置の公開資料なし） · `00bcfe58`（命令位置の公開資料なし）

~~~diff
- 00bcfa60 ["INT_ADD", "register:40f0:8", ["const:bcfa60:8", "const:4:8"]]
- 00bcfa60 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcfe88 ["INT_ADD", "register:40f0:8", ["const:bcfe88:8", "const:4:8"]]
+ 00bcfe88 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcfa60 bytes 682c0294
+ 00bcfe88 bytes 5e2c0294
- 00bcfa24 ["INT_ADD", "register:40f0:8", ["const:bcfa24:8", "const:4:8"]]
- 00bcfa24 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcfe4c ["INT_ADD", "register:40f0:8", ["const:bcfe4c:8", "const:4:8"]]
+ 00bcfe4c ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcfa24 bytes f72a0294
+ 00bcfe4c bytes ed2a0294
- 00bcfa30 ["INT_ADD", "register:40f0:8", ["const:bcfa30:8", "const:4:8"]]
- 00bcfa30 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bcfe58 ["INT_ADD", "register:40f0:8", ["const:bcfe58:8", "const:4:8"]]
+ 00bcfe58 ["CALL", null, ["callee:00c5ae80:8"]]
- 00bcfa30 bytes 142c0294
+ 00bcfe58 bytes 0a2c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f10d647be604854bbaef145683bfe42c"></a>

### [`00bcfb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfb28.md) → [`00bcff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcff50.md) _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d930.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd30.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcff7c",
      "incomplete_value": true,
      "site": "00bcff84",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00bcfb54",
      "incomplete_value": true,
      "site": "00bcfb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfb28.md#insn-00bcfb5c) · [`00bcfb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfb28.md#insn-00bcfb48) · [`00bcfb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfb28.md#insn-00bcfb54)
- 新版 `00bcff84`（命令位置の公開資料なし） · `00bcff70`（命令位置の公開資料なし）

~~~diff
- 00bcfb5c ["INT_ADD", "register:40f0:8", ["const:bcfb5c:8", "const:4:8"]]
- 00bcfb5c ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcff84 ["INT_ADD", "register:40f0:8", ["const:bcff84:8", "const:4:8"]]
+ 00bcff84 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bcfb5c bytes a92b0294
+ 00bcff84 bytes 9f2b0294
- 00bcfb48 ["INT_ADD", "register:40f0:8", ["const:bcfb48:8", "const:4:8"]]
- 00bcfb48 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcff70 ["INT_ADD", "register:40f0:8", ["const:bcff70:8", "const:4:8"]]
+ 00bcff70 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcfb48 bytes 4a2b0294
+ 00bcff70 bytes 402b0294
- 00bcfb54 ["COPY", "register:4000:8", ["register:40a0:8"]]
- 00bcfb54 bytes e00314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19ca6e125d78a996116fbd7e56675cf0"></a>

### [`00bcfbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbdc.md) → [`00bd0004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0004.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7e0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbe0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 66.67% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0068",
      "incomplete_value": false,
      "site": "00bd006c",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcfc40",
      "incomplete_value": false,
      "site": "00bcfc44",
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
            "const:8:8"
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
      "00bd0068",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcfcac",
      "READ",
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
      "00bd0068",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bd00d4",
      "READ",
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

- 旧版 [`00bcfc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbdc.md#insn-00bcfc44) · [`00bcfc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbdc.md#insn-00bcfc08) · [`00bcfc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbdc.md#insn-00bcfc14)
- 新版 `00bd006c`（命令位置の公開資料なし） · `00bd0030`（命令位置の公開資料なし） · `00bd003c`（命令位置の公開資料なし）

~~~diff
- 00bcfc44 ["INT_ADD", "register:40f0:8", ["const:bcfc44:8", "const:4:8"]]
- 00bcfc44 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd006c ["INT_ADD", "register:40f0:8", ["const:bd006c:8", "const:4:8"]]
+ 00bd006c ["CALL", null, ["callee:00c5b000:8"]]
- 00bcfc44 bytes ef2b0294
+ 00bd006c bytes e52b0294
- 00bcfc08 ["INT_ADD", "register:40f0:8", ["const:bcfc08:8", "const:4:8"]]
- 00bcfc08 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bd0030 ["INT_ADD", "register:40f0:8", ["const:bd0030:8", "const:4:8"]]
+ 00bd0030 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcfc08 bytes 7e2a0294
+ 00bd0030 bytes 742a0294
- 00bcfc14 ["INT_ADD", "register:40f0:8", ["const:bcfc14:8", "const:4:8"]]
- 00bcfc14 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bd003c ["INT_ADD", "register:40f0:8", ["const:bd003c:8", "const:4:8"]]
+ 00bd003c ["CALL", null, ["callee:00c5ae80:8"]]
- 00bcfc14 bytes 9b2b0294
+ 00bd003c bytes 912b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e8669a456efd20685da35da3d90773"></a>

### [`00bcfce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md) → [`00bd010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd010c.md) _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bce0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) [`00bdfddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7b0.md)
- 新版 呼出元 2件 [`00bce4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce4dc.md) [`00be0204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbb0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfd14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfd18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd013c"
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
      "unmatched:00bcfd14",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcfd18",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcfd84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd01c8"
      ]
    ]
  ],
  "added": [
    [
      "00bd013c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bd0140",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "00bd01ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd01c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md#insn-00bcfd14) · [`00bcfd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md#insn-00bcfd18) · [`00bcfd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md#insn-00bcfd1c)
- 新版 `00bd0144`（命令位置の公開資料なし）

~~~diff
- 00bcfd14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bcfd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcfd14 bytes e81f00f9
- 00bcfd18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcfd18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcfd18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:34:8"]]
- 00bcfd18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcfd18 bytes ffd30039
- 00bcfd1c ["INT_ADD", "register:40f0:8", ["const:bcfd1c:8", "const:4:8"]]
- 00bcfd1c ["CALL", null, ["callee:00c5dd20:8"]]
+ 00bd0144 ["INT_ADD", "register:40f0:8", ["const:bd0144:8", "const:4:8"]]
+ 00bd0144 ["CALL", null, ["callee:00c5dd20:8"]]
- 00bcfd1c bytes 01370294
+ 00bd0144 bytes f7360294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e62828a13812c178083aa68c21bd3791"></a>

### [`00bcfdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfdb8.md) → [`00bd01e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd01e0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResu

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7b0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbb0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfe54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd027c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd024c",
      "incomplete_value": false,
      "site": "00bd0250",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcfe24",
      "incomplete_value": false,
      "site": "00bcfe28",
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
            "const:8:8"
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
      "unmatched:00bcfe24",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcfe54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0290"
      ]
    ]
  ],
  "added": [
    [
      "00bd024c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bd027c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0290"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfe28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfdb8.md#insn-00bcfe28) · [`00bcfe54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfdb8.md#insn-00bcfe54) · [`00bcfe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfdb8.md#insn-00bcfe64)
- 新版 `00bd0250`（命令位置の公開資料なし） · `00bd028c`（命令位置の公開資料なし）

~~~diff
- 00bcfe28 ["INT_ADD", "register:40f0:8", ["const:bcfe28:8", "const:4:8"]]
- 00bcfe28 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd0250 ["INT_ADD", "register:40f0:8", ["const:bd0250:8", "const:4:8"]]
+ 00bd0250 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcfe28 bytes 762b0294
+ 00bd0250 bytes 6c2b0294
- 00bcfe54 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcfe54 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcfe54 bytes a80000b4
- 00bcfe64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfe64 ["INT_ADD", "register:40f0:8", ["const:bcfe64:8", "const:4:8"]]
- 00bcfe64 ["CALLIND", null, ["register:0:8"]]
+ 00bd028c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd028c ["INT_ADD", "register:40f0:8", ["const:bd028c:8", "const:4:8"]]
+ 00bd028c ["CALLIND", null, ["register:0:8"]]
- 00bcfe64 bytes 00013fd6
+ 00bd028c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884799160ba2090897eb00b28b2c0a3e"></a>

### [`00bcfef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfef0.md) → [`00bd0318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0318.md) _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d950.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd50.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcff48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd0370"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcff3c",
      "incomplete_value": true,
      "site": "00bcff40",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00bcff48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0384"
      ]
    ],
    [
      "unmatched:00bcff58",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0384"
      ]
    ],
    [
      "00bd0380",
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

- 旧版 [`00bcff40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfef0.md#insn-00bcff40) · [`00bcff48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfef0.md#insn-00bcff48) · [`00bcff58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfef0.md#insn-00bcff58)
- 新版 `00bd0368`（命令位置の公開資料なし）

~~~diff
- 00bcff40 ["INT_ADD", "register:40f0:8", ["const:bcff40:8", "const:4:8"]]
- 00bcff40 ["CALL", null, ["callee:00c5adf0:8"]]
+ 00bd0368 ["INT_ADD", "register:40f0:8", ["const:bd0368:8", "const:4:8"]]
+ 00bd0368 ["CALL", null, ["callee:00c5adf0:8"]]
- 00bcff40 bytes ac2a0294
+ 00bd0368 bytes a22a0294
- 00bcff48 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcff48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcff48 bytes a00000b4
- 00bcff58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcff58 ["INT_ADD", "register:40f0:8", ["const:bcff58:8", "const:4:8"]]
- 00bcff58 ["CALLIND", null, ["register:0:8"]]
- 00bcff58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d3bde3763dae33f759e6ad20b476d1"></a>

### [`00bcff90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcff90.md) → [`00bd03b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd03b8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7c0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbc0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 9.09% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcffec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd0414"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd03d4",
      "incomplete_value": true,
      "site": "00bd03e4",
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
    "old": null,
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
      "unmatched:00bcffec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0424"
      ]
    ],
    [
      "unmatched:00bcfff4",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcffe4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0424"
      ]
    ],
    [
      "00bd041c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bd040c",
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

- 旧版 [`00bcffbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcff90.md#insn-00bcffbc) · [`00bcffc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcff90.md#insn-00bcffc8) · [`00bcffe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcff90.md#insn-00bcffe4)
- 新版 `00bd03e4`（命令位置の公開資料なし） · `00bd03f0`（命令位置の公開資料なし）

~~~diff
- 00bcffbc ["INT_ADD", "register:40f0:8", ["const:bcffbc:8", "const:4:8"]]
- 00bcffbc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bd03e4 ["INT_ADD", "register:40f0:8", ["const:bd03e4:8", "const:4:8"]]
+ 00bd03e4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcffbc bytes 91290294
+ 00bd03e4 bytes 87290294
- 00bcffc8 ["INT_ADD", "register:40f0:8", ["const:bcffc8:8", "const:4:8"]]
- 00bcffc8 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bd03f0 ["INT_ADD", "register:40f0:8", ["const:bd03f0:8", "const:4:8"]]
+ 00bd03f0 ["CALL", null, ["callee:00c5ae80:8"]]
- 00bcffc8 bytes ae2a0294
+ 00bd03f0 bytes a42a0294
- 00bcffe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcffe4 ["INT_ADD", "register:40f0:8", ["const:bcffe4:8", "const:4:8"]]
- 00bcffe4 ["CALLIND", null, ["register:0:8"]]
- 00bcffe4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed330a3af49d1cef4306205594a73a4d"></a>

### [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) → [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) _ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00bcf088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md) [`00bdf328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md) [`00bdf550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md) [`00be0028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md) [`00be0218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7f0.md)
- 新版 呼出元 8件 [`00bcf4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md) [`00bdf750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md) [`00bdf978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md) [`00be0450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md) [`00be0640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd009c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd009c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd00a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd009c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd00a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd00a4",
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
      "00bd04c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd04c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd04cc",
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

- 旧版 [`00bd009c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md#insn-00bd009c) · [`00bd00a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md#insn-00bd00a0) · [`00bd00a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md#insn-00bd00a4)

~~~diff
- 00bd009c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bd009c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bd009c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bd009c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd009c bytes f85f04a9
- 00bd00a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd00a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd00a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bd00a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd00a0 bytes f65705a9
- 00bd00a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd00a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd00a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bd00a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd00a4 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8c811d7cf2fb8e74ad73fd43983e35"></a>

### [`00bd016c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd016c.md) → [`00bd0594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0594.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS_4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7f0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbf0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.03% / 新版 91.03%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd016c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0170"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd016c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0170",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0174",
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
      "00bd0594",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd0598",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd059c",
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

- 旧版 [`00bd016c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd016c.md#insn-00bd016c) · [`00bd0170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd016c.md#insn-00bd0170) · [`00bd0174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd016c.md#insn-00bd0174)

~~~diff
- 00bd016c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00bd016c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bd016c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd016c bytes f90f1bf8
- 00bd0170 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bd0170 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bd0170 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0170 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0170 bytes f85f01a9
- 00bd0174 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd0174 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd0174 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd0174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0174 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a861b08e2ac52cef9a2a743d4c09f6a4"></a>

### [`00bd02a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02a4.md) → [`00bd06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd06cc.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bd02d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd06f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd06e0",
      "incomplete_value": true,
      "site": "00bd06e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd02b8",
      "incomplete_value": true,
      "site": "00bd02b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd06dc",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd02c4",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd02c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd06dc",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd06ec",
      "PARAM",
      [
        "storage",
        "002b2756",
        null,
        "string"
      ]
    ],
    [
      "00bd06f0",
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

- 旧版 [`00bd02c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02a4.md#insn-00bd02c8) · [`00bd02d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02a4.md#insn-00bd02d0)
- 新版 `00bd06f0`（命令位置の公開資料なし）

~~~diff
- 00bd02c8 ["INT_ADD", "register:40f0:8", ["const:bd02c8:8", "const:4:8"]]
- 00bd02c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd02c8 bytes 122a0294
- 00bd02d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:448:8"]]
- 00bd02d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd02d0 bytes 602602f9
+ 00bd06f0 ["INT_ADD", "register:40f0:8", ["const:bd06f0:8", "const:4:8"]]
+ 00bd06f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd06f0 bytes 082a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97049767a81c01bab321cc30da589f7"></a>

### [`00bd02e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02e4.md) → [`00bd070c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd070c.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd0738",
      "incomplete_value": true,
      "site": "00bd0738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0310",
      "incomplete_value": true,
      "site": "00bd0310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "definition_site": "00bd0720",
      "incomplete_value": true,
      "site": "00bd0720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd02f8",
      "incomplete_value": true,
      "site": "00bd02f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0728",
      "incomplete_value": false,
      "site": "00bd0730",
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
            "const:756:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0300",
      "incomplete_value": false,
      "site": "00bd0308",
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
            "const:716:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd071c",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0728",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ],
    [
      "00bd0738",
      "WRITE",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd071c",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0728",
      "PARAM",
      [
        "storage",
        "002b2756",
        null,
        "string"
      ]
    ],
    [
      "00bd0738",
      "WRITE",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02e4.md#insn-00bd0308) · [`00bd0310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02e4.md#insn-00bd0310) · [`00bd02f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02e4.md#insn-00bd02f4)
- 新版 `00bd0730`（命令位置の公開資料なし） · `00bd0738`（命令位置の公開資料なし） · `00bd071c`（命令位置の公開資料なし）

~~~diff
- 00bd0308 ["INT_ADD", "register:40f0:8", ["const:bd0308:8", "const:4:8"]]
- 00bd0308 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0730 ["INT_ADD", "register:40f0:8", ["const:bd0730:8", "const:4:8"]]
+ 00bd0730 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0308 bytes 022a0294
+ 00bd0730 bytes f8290294
- 00bd0310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:448:8"]]
- 00bd0310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0738 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:848:8"]]
+ 00bd0738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0310 bytes 602602f9
+ 00bd0738 bytes 602604f9
- 00bd02f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:448:8"]]
- 00bd02f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd071c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:848:8"]]
+ 00bd071c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd02f4 bytes 682642f9
+ 00bd071c bytes 682644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec407a94cca213dd33054c8becacc4d"></a>

### [`00bd0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0324.md) → [`00bd074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd074c.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bd0324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0328"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0328"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0324",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0328",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd075c",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd074c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0750",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd075c",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0324.md#insn-00bd0324) · [`00bd0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0324.md#insn-00bd0328) · [`00bd034c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0324.md#insn-00bd034c)

~~~diff
- 00bd0324 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd0324 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd0324 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0324 bytes f30f1ef8
- 00bd0328 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0328 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0328 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0328 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0328 bytes fd7b01a9
- 00bd034c ["INT_ADD", "register:40f0:8", ["const:bd034c:8", "const:4:8"]]
- 00bd034c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd034c bytes f1290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f8d5cf1ca35df8f8f4ccb314622e514"></a>

### [`00bd0368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0368.md) → [`00bd0790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0790.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bd0368"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd036c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd036c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0368",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd036c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd07a0",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0790",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0794",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd07a0",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0368.md#insn-00bd0368) · [`00bd036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0368.md#insn-00bd036c) · [`00bd037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0368.md#insn-00bd037c)
- 新版 `00bd07a4`（命令位置の公開資料なし）

~~~diff
- 00bd0368 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd0368 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd0368 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0368 bytes f30f1ef8
- 00bd036c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd036c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd036c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd036c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd036c bytes fd7b01a9
- 00bd037c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd037c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd07a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd07a4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd037c bytes 080100b5
+ 00bd07a4 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84dfbfdd487168a478908f6fd26b7828"></a>

### [`00bd03b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd03b8.md) → [`00bd07e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd07e0.md) _ZN8firebase4auth10authresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0838"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0814",
      "incomplete_value": true,
      "site": "00bd0820",
      "value": [
        "LOAD",
        "8",
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
                "const:848:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd03ec",
      "incomplete_value": true,
      "site": "00bd03f8",
      "value": [
        "LOAD",
        "8",
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
                "const:448:8"
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
      "unmatched:00bd03cc",
      "READ",
      [
        "storage",
        "01126450",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0800",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0414"
      ]
    ],
    [
      "unmatched:00bd03ec",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd07f4",
      "READ",
      [
        "storage",
        "01126850",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0800",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd083c"
      ]
    ],
    [
      "00bd0814",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd03f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd03b8.md#insn-00bd03f8) · [`00bd0410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd03b8.md#insn-00bd0410) · [`00bd0420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd03b8.md#insn-00bd0420)
- 新版 `00bd0820`（命令位置の公開資料なし）

~~~diff
- 00bd03f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd03f8 ["INT_ADD", "register:40f0:8", ["const:bd03f8:8", "const:4:8"]]
- 00bd03f8 ["CALLIND", null, ["register:0:8"]]
+ 00bd0820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0820 ["INT_ADD", "register:40f0:8", ["const:bd0820:8", "const:4:8"]]
+ 00bd0820 ["CALLIND", null, ["register:0:8"]]
- 00bd03f8 bytes 00013fd6
+ 00bd0820 bytes 00013fd6
- 00bd0410 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd0410 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:450:8"]]
- 00bd0410 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd0410 bytes a0421139
- 00bd0420 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0420 ["RETURN", null, ["register:0:8"]]
- 00bd0420 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6048c6df8278a0fb67b6a2a18300ab99"></a>

### [`00bd0424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0424.md) → [`00bd084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd084c.md) _ZN8firebase4auth10authresult12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.43% / 新版 46.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00bd0424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0424",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd042c",
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
      "00bd084c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0850",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0854",
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

- 旧版 [`00bd0424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0424.md#insn-00bd0424) · [`00bd0428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0424.md#insn-00bd0428) · [`00bd042c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0424.md#insn-00bd042c)

~~~diff
- 00bd0424 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd0424 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd0424 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0424 bytes f50f1df8
- 00bd0428 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0428 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0428 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0428 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0428 bytes f44f01a9
- 00bd042c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd042c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd042c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd042c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd042c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f708f4b6f89617e7c846882abc42006e"></a>

### [`00bd0494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0494.md) → [`00bd08bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd08bc.md) _ZN8firebase4auth10authresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd04d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd08fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd04b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd04a8",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd04b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0900"
      ]
    ],
    [
      "unmatched:00bd04b8",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd08d0",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd08d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0900"
      ]
    ],
    [
      "00bd08e0",
      "PARAM",
      [
        "storage",
        "002b2756",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0494.md#insn-00bd04b0) · [`00bd04cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0494.md#insn-00bd04cc) · [`00bd04d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0494.md#insn-00bd04d4)
- 新版 `00bd08f4`（命令位置の公開資料なし）

~~~diff
- 00bd04b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd04b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd04b0 bytes 410100b5
- 00bd04cc ["INT_ADD", "register:40f0:8", ["const:bd04cc:8", "const:4:8"]]
- 00bd04cc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd08f4 ["INT_ADD", "register:40f0:8", ["const:bd08f4:8", "const:4:8"]]
+ 00bd08f4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd04cc bytes 91290294
+ 00bd08f4 bytes 87290294
- 00bd04d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:448:8"]]
- 00bd04d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd04d4 bytes 802602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-860d334454499d065152e2dcbf109719"></a>

### [`00bd0540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0540.md) → [`00bd0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0968.md) _ZN8firebase4auth10authresult13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd0540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0544"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0540",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0544",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0554",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0968",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd096c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd097c",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0540.md#insn-00bd0540) · [`00bd0544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0540.md#insn-00bd0544) · [`00bd055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0540.md#insn-00bd055c)

~~~diff
- 00bd0540 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0540 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0540 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd0540 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0540 bytes f44fbea9
- 00bd0544 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0544 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0544 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0544 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0544 bytes fd7b01a9
- 00bd055c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd055c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd055c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5090dafc3df01ca0230c26036bfa0b48"></a>

### [`00bd05ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05ec.md) → [`00bd0a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0a14.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

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
      "site": "00bd0618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0a40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0a28",
      "incomplete_value": true,
      "site": "00bd0a28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0600",
      "incomplete_value": true,
      "site": "00bd0600",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd0a24",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0a28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd061c"
      ]
    ],
    [
      "unmatched:00bd060c",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0a24",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0a28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0a44"
      ]
    ],
    [
      "00bd0a34",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05ec.md#insn-00bd0610) · [`00bd0618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05ec.md#insn-00bd0618) · [`00bd0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05ec.md#insn-00bd0628)

~~~diff
- 00bd0610 ["INT_ADD", "register:40f0:8", ["const:bd0610:8", "const:4:8"]]
- 00bd0610 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0610 bytes 40290294
- 00bd0618 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bd0618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0618 bytes 603e02f9
- 00bd0628 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0628 ["RETURN", null, ["register:0:8"]]
- 00bd0628 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e5aef5c0f207708b06b9f5bd05867a4"></a>

### [`00bd062c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd062c.md) → [`00bd0a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0a54.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bd0658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0a80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0a68",
      "incomplete_value": true,
      "site": "00bd0a68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0640",
      "incomplete_value": true,
      "site": "00bd0640",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd0a64",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0648",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0650",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd0a64",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0a70",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ],
    [
      "00bd0a78",
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

- 旧版 [`00bd0640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd062c.md#insn-00bd0640) · [`00bd0650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd062c.md#insn-00bd0650) · [`00bd0658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd062c.md#insn-00bd0658)
- 新版 `00bd0a68`（命令位置の公開資料なし）

~~~diff
- 00bd0640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd0640 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd0a68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0a68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0640 bytes e80000b5
+ 00bd0a68 bytes e80000b5
- 00bd0650 ["INT_ADD", "register:40f0:8", ["const:bd0650:8", "const:4:8"]]
- 00bd0650 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0650 bytes 30290294
- 00bd0658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bd0658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0658 bytes 603e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab5da5d48e9eed8e70f7d3e61f396c7c"></a>

### [`00bd066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd066c.md) → [`00bd0a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0a94.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd0ac4",
      "incomplete_value": true,
      "site": "00bd0ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd069c",
      "incomplete_value": true,
      "site": "00bd069c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "00bd0aa8",
      "incomplete_value": true,
      "site": "00bd0aa8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0680",
      "incomplete_value": true,
      "site": "00bd0680",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0ab4",
      "incomplete_value": false,
      "site": "00bd0abc",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd068c",
      "incomplete_value": false,
      "site": "00bd0694",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0aa4",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0ab4",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd0ac4",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0aa4",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0ab4",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ],
    [
      "00bd0ac4",
      "WRITE",
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

- 旧版 [`00bd0694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd066c.md#insn-00bd0694) · [`00bd069c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd066c.md#insn-00bd069c) · [`00bd067c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd066c.md#insn-00bd067c)
- 新版 `00bd0abc`（命令位置の公開資料なし） · `00bd0ac4`（命令位置の公開資料なし） · `00bd0aa4`（命令位置の公開資料なし）

~~~diff
- 00bd0694 ["INT_ADD", "register:40f0:8", ["const:bd0694:8", "const:4:8"]]
- 00bd0694 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0abc ["INT_ADD", "register:40f0:8", ["const:bd0abc:8", "const:4:8"]]
+ 00bd0abc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0694 bytes 1f290294
+ 00bd0abc bytes 15290294
- 00bd069c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bd069c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0ac4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00bd0ac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd069c bytes 603e02f9
+ 00bd0ac4 bytes 603e04f9
- 00bd067c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bd067c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0aa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00bd0aa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd067c bytes 683e42f9
+ 00bd0aa4 bytes 683e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d86a689531a4b60901b573b509eca635"></a>

### [`00bd06b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd06b0.md) → [`00bd0ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0ad8.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd06e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0b08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0aec",
      "incomplete_value": true,
      "site": "00bd0aec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd06c4",
      "incomplete_value": true,
      "site": "00bd06c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd0ae8",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd06cc",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd06e0",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0ae8",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0af4",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ],
    [
      "00bd0b08",
      "WRITE",
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

- 旧版 [`00bd06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd06b0.md#insn-00bd06c4) · [`00bd06d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd06b0.md#insn-00bd06d8) · [`00bd06e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd06b0.md#insn-00bd06e0)
- 新版 `00bd0aec`（命令位置の公開資料なし） · `00bd0b00`（命令位置の公開資料なし）

~~~diff
- 00bd06c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd06c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd0aec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0aec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd06c4 bytes 080100b5
+ 00bd0aec bytes 080100b5
- 00bd06d8 ["INT_ADD", "register:40f0:8", ["const:bd06d8:8", "const:4:8"]]
- 00bd06d8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0b00 ["INT_ADD", "register:40f0:8", ["const:bd0b00:8", "const:4:8"]]
+ 00bd0b00 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd06d8 bytes 0e290294
+ 00bd0b00 bytes 04290294
- 00bd06e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bd06e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd06e0 bytes 603e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e1ced13459e1cbbd741a8568a6418a9"></a>

### [`00bd0700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0700.md) → [`00bd0b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0b28.md) _ZN8firebase4auth20additional_user_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd0b80",
      "incomplete_value": true,
      "site": "00bd0b80",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0758",
      "incomplete_value": true,
      "site": "00bd0758",
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
            "const:480:8"
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
      "definition_site": "00bd0b5c",
      "incomplete_value": true,
      "site": "00bd0b68",
      "value": [
        "LOAD",
        "8",
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
                "const:878:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0734",
      "incomplete_value": true,
      "site": "00bd0740",
      "value": [
        "LOAD",
        "8",
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
                "const:478:8"
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
      "00bd0b3c",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0b5c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0b80",
      "WRITE",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd0b3c",
      "READ",
      [
        "storage",
        "01126880",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0b5c",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0b80",
      "WRITE",
      [
        "storage",
        "01126880",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0700.md#insn-00bd0740) · [`00bd0758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0700.md#insn-00bd0758) · [`00bd0714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0700.md#insn-00bd0714)
- 新版 `00bd0b68`（命令位置の公開資料なし） · `00bd0b80`（命令位置の公開資料なし） · `00bd0b3c`（命令位置の公開資料なし）

~~~diff
- 00bd0740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0740 ["INT_ADD", "register:40f0:8", ["const:bd0740:8", "const:4:8"]]
- 00bd0740 ["CALLIND", null, ["register:0:8"]]
+ 00bd0b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b68 ["INT_ADD", "register:40f0:8", ["const:bd0b68:8", "const:4:8"]]
+ 00bd0b68 ["CALLIND", null, ["register:0:8"]]
- 00bd0740 bytes 00013fd6
+ 00bd0b68 bytes 00013fd6
- 00bd0758 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd0758 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:480:8"]]
- 00bd0758 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd0b80 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd0b80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:880:8"]]
+ 00bd0b80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd0758 bytes a0021239
+ 00bd0b80 bytes a0022239
- 00bd0714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:480:8"]]
- 00bd0714 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd0714 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd0b3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:880:8"]]
+ 00bd0b3c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0b3c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd0714 bytes a8025239
+ 00bd0b3c bytes a8026239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bbd68635a06065605c227c0ee9ab75f"></a>

### [`00bd076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd076c.md) → [`00bd0b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0b94.md) _ZN8firebase4auth20additional_user_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 33.33% / 新版 28.57%

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
      "site": "00bd07a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd0bf0",
      "incomplete_value": true,
      "site": "00bd0bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd07c8",
      "incomplete_value": true,
      "site": "00bd07c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "site": "00bd0bd0"
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
      "00bd0ba8",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0bb4",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd07a8",
      "WRITE",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd0ba8",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0bb4",
      "READ",
      [
        "storage",
        "01126880",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0bd0",
      "WRITE",
      [
        "storage",
        "01126880",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd076c.md#insn-00bd0784) · [`00bd07a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd076c.md#insn-00bd07a8) · [`00bd07c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd076c.md#insn-00bd07c4)
- 新版 `00bd0bac`（命令位置の公開資料なし） · `00bd0bec`（命令位置の公開資料なし）

~~~diff
- 00bd0784 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd0784 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd0bac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd0bac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd0784 bytes 410200b4
+ 00bd0bac bytes 410200b4
- 00bd07a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd07a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd07a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:480:8"]]
- 00bd07a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd07a8 bytes bf021239
- 00bd07c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd07c4 ["INT_ADD", "register:40f0:8", ["const:bd07c4:8", "const:4:8"]]
- 00bd07c4 ["CALLIND", null, ["register:0:8"]]
+ 00bd0bec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0bec ["INT_ADD", "register:40f0:8", ["const:bd0bec:8", "const:4:8"]]
+ 00bd0bec ["CALLIND", null, ["register:0:8"]]
- 00bd07c4 bytes 00013fd6
+ 00bd0bec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46ba4b52d8f9ff23f0681827214b0ab5"></a>

### [`00bd07dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd07dc.md) → [`00bd0c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0c04.md) _ZN8firebase4auth20additional_user_info14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd0c44",
      "incomplete_value": true,
      "site": "00bd0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd081c",
      "incomplete_value": true,
      "site": "00bd081c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "00bd0c20",
      "incomplete_value": true,
      "site": "00bd0c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd07f8",
      "incomplete_value": true,
      "site": "00bd07f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0c28",
      "incomplete_value": false,
      "site": "00bd0c3c",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0800",
      "incomplete_value": false,
      "site": "00bd0814",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0c18",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0c28",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd0c44",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0c18",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0c28",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ],
    [
      "00bd0c44",
      "WRITE",
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

- 旧版 [`00bd0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd07dc.md#insn-00bd0814) · [`00bd081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd07dc.md#insn-00bd081c) · [`00bd07f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd07dc.md#insn-00bd07f0)
- 新版 `00bd0c3c`（命令位置の公開資料なし） · `00bd0c44`（命令位置の公開資料なし） · `00bd0c18`（命令位置の公開資料なし）

~~~diff
- 00bd0814 ["INT_ADD", "register:40f0:8", ["const:bd0814:8", "const:4:8"]]
- 00bd0814 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0c3c ["INT_ADD", "register:40f0:8", ["const:bd0c3c:8", "const:4:8"]]
+ 00bd0c3c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0814 bytes bf280294
+ 00bd0c3c bytes b5280294
- 00bd081c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bd081c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0c44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
+ 00bd0c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd081c bytes 803e02f9
+ 00bd0c44 bytes 803e04f9
- 00bd07f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bd07f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0c18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
+ 00bd0c18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd07f0 bytes 813e42f9
+ 00bd0c18 bytes 813e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8866fbde5c62678621045377df7cc3"></a>

### [`00bd084c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd084c.md) → [`00bd0c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0c74.md) _ZN8firebase4auth20additional_user_info11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd0c90",
      "incomplete_value": false,
      "site": "00bd0c94",
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
      "definition_site": "00bd0868",
      "incomplete_value": false,
      "site": "00bd086c",
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
      "definition_site": "00bd0ca0",
      "incomplete_value": true,
      "site": "00bd0cac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd0878",
      "incomplete_value": true,
      "site": "00bd0884",
      "value": [
        "LOAD",
        "8",
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
      "00bd0c90",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd0ca0",
      "DATA",
      [
        "storage",
        "01126488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0c90",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd0ca0",
      "DATA",
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

- 旧版 [`00bd086c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd084c.md#insn-00bd086c) · [`00bd0868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd084c.md#insn-00bd0868) · [`00bd0874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd084c.md#insn-00bd0874)
- 新版 `00bd0c94`（命令位置の公開資料なし） · `00bd0c90`（命令位置の公開資料なし） · `00bd0c9c`（命令位置の公開資料なし）

~~~diff
- 00bd086c ["INT_ADD", "register:40f0:8", ["const:bd086c:8", "const:4:8"]]
- 00bd086c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd0c94 ["INT_ADD", "register:40f0:8", ["const:bd0c94:8", "const:4:8"]]
+ 00bd0c94 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd086c bytes e5280294
+ 00bd0c94 bytes db280294
- 00bd0868 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd0868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0c90 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd0c90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0c90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0c90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd0868 bytes 00680a91
+ 00bd0c90 bytes 009c0d91
- 00bd0874 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00bd0874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd0c9c ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00bd0c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd0874 bytes 08211291
+ 00bd0c9c bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87e2d31905b7cc0fb7e57cac68e54636"></a>

### [`00bd0888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0888.md) → [`00bd0cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0cb0.md) _ZN8firebase4auth20additional_user_info13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd08c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0cf0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd08a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd089c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd08a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0cf4"
      ]
    ],
    [
      "unmatched:00bd08ac",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0cc4",
      "READ",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0ccc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0cf4"
      ]
    ],
    [
      "00bd0cd4",
      "PARAM",
      [
        "storage",
        "002ac2da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd08a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0888.md#insn-00bd08a4) · [`00bd08c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0888.md#insn-00bd08c0) · [`00bd08c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0888.md#insn-00bd08c8)
- 新版 `00bd0ce8`（命令位置の公開資料なし）

~~~diff
- 00bd08a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd08a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd08a4 bytes 410100b5
- 00bd08c0 ["INT_ADD", "register:40f0:8", ["const:bd08c0:8", "const:4:8"]]
- 00bd08c0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0ce8 ["INT_ADD", "register:40f0:8", ["const:bd0ce8:8", "const:4:8"]]
+ 00bd0ce8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd08c0 bytes 94280294
+ 00bd0ce8 bytes 8a280294
- 00bd08c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bd08c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd08c8 bytes 803e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b96002520eb67df72c8ee9afbe3addbe"></a>

### [`00bd08f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd08f8.md) → [`00bd0d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0d20.md) _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd0d3c",
      "incomplete_value": false,
      "site": "00bd0d40",
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
      "definition_site": "00bd0914",
      "incomplete_value": false,
      "site": "00bd0918",
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
      "definition_site": "00bd0d4c",
      "incomplete_value": true,
      "site": "00bd0d58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd0924",
      "incomplete_value": true,
      "site": "00bd0930",
      "value": [
        "LOAD",
        "8",
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
      "00bd0d3c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd0d4c",
      "DATA",
      [
        "storage",
        "011264a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0d3c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd0d4c",
      "DATA",
      [
        "storage",
        "011268a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd08f8.md#insn-00bd0918) · [`00bd0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd08f8.md#insn-00bd0914) · [`00bd0920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd08f8.md#insn-00bd0920)
- 新版 `00bd0d40`（命令位置の公開資料なし） · `00bd0d3c`（命令位置の公開資料なし） · `00bd0d48`（命令位置の公開資料なし）

~~~diff
- 00bd0918 ["INT_ADD", "register:40f0:8", ["const:bd0918:8", "const:4:8"]]
- 00bd0918 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd0d40 ["INT_ADD", "register:40f0:8", ["const:bd0d40:8", "const:4:8"]]
+ 00bd0d40 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd0918 bytes ba280294
+ 00bd0d40 bytes b0280294
- 00bd0914 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd0914 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0914 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0914 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0d3c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd0d3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0d3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0d3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd0914 bytes 00441191
+ 00bd0d3c bytes 00781491
- 00bd0920 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00bd0920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd0d48 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00bd0d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd0920 bytes 08811291
+ 00bd0d48 bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4954f23e1c1912ab8e49437b0b2336"></a>

### [`00bd0934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0934.md) → [`00bd0d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0d5c.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd0960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0d88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0d70",
      "incomplete_value": true,
      "site": "00bd0d70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0948",
      "incomplete_value": true,
      "site": "00bd0948",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd0d6c",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0954",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0958",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd0d6c",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0d7c",
      "PARAM",
      [
        "storage",
        "002a7450",
        null,
        "string"
      ]
    ],
    [
      "00bd0d80",
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

- 旧版 [`00bd0948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0934.md#insn-00bd0948) · [`00bd0958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0934.md#insn-00bd0958) · [`00bd0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0934.md#insn-00bd0960)
- 新版 `00bd0d70`（命令位置の公開資料なし）

~~~diff
- 00bd0948 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd0948 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd0d70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0d70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd0948 bytes e80000b5
+ 00bd0d70 bytes e80000b5
- 00bd0958 ["INT_ADD", "register:40f0:8", ["const:bd0958:8", "const:4:8"]]
- 00bd0958 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0958 bytes 6e280294
- 00bd0960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00bd0960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0960 bytes 605602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63af403a3ddd21497868d98e313edaa6"></a>

### [`00bd0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0974.md) → [`00bd0d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0d9c.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00bd0dc8",
      "incomplete_value": true,
      "site": "00bd0dc8",
      "value": [
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
      "definition_site": "00bd09a0",
      "incomplete_value": true,
      "site": "00bd09a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "definition_site": "00bd0db0",
      "incomplete_value": true,
      "site": "00bd0db0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0988",
      "incomplete_value": true,
      "site": "00bd0988",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0db8",
      "incomplete_value": false,
      "site": "00bd0dc0",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0990",
      "incomplete_value": false,
      "site": "00bd0998",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0dac",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0db8",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0dc8",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0dac",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0db8",
      "PARAM",
      [
        "storage",
        "002a7450",
        null,
        "string"
      ]
    ],
    [
      "00bd0dc8",
      "WRITE",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0974.md#insn-00bd0998) · [`00bd09a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0974.md#insn-00bd09a0) · [`00bd0984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0974.md#insn-00bd0984)
- 新版 `00bd0dc0`（命令位置の公開資料なし） · `00bd0dc8`（命令位置の公開資料なし） · `00bd0dac`（命令位置の公開資料なし）

~~~diff
- 00bd0998 ["INT_ADD", "register:40f0:8", ["const:bd0998:8", "const:4:8"]]
- 00bd0998 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0dc0 ["INT_ADD", "register:40f0:8", ["const:bd0dc0:8", "const:4:8"]]
+ 00bd0dc0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0998 bytes 5e280294
+ 00bd0dc0 bytes 54280294
- 00bd09a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00bd09a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00bd0dc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd09a0 bytes 605602f9
+ 00bd0dc8 bytes 605604f9
- 00bd0984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00bd0984 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0dac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00bd0dac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd0984 bytes 685642f9
+ 00bd0dac bytes 685644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f7a5f58aa49f08df353fd7231cd774"></a>

### [`00bd09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09f8.md) → [`00bd0e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0e20.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd0e50",
      "incomplete_value": true,
      "site": "00bd0e50",
      "value": [
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
      "definition_site": "00bd0a28",
      "incomplete_value": true,
      "site": "00bd0a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "definition_site": "00bd0e34",
      "incomplete_value": true,
      "site": "00bd0e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0a0c",
      "incomplete_value": true,
      "site": "00bd0a0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0e3c",
      "incomplete_value": false,
      "site": "00bd0e48",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0a14",
      "incomplete_value": false,
      "site": "00bd0a20",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0e30",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0e3c",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0e50",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0e30",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0e3c",
      "PARAM",
      [
        "storage",
        "002a7450",
        null,
        "string"
      ]
    ],
    [
      "00bd0e50",
      "WRITE",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09f8.md#insn-00bd0a20) · [`00bd0a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09f8.md#insn-00bd0a28) · [`00bd0a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09f8.md#insn-00bd0a08)
- 新版 `00bd0e48`（命令位置の公開資料なし） · `00bd0e50`（命令位置の公開資料なし） · `00bd0e30`（命令位置の公開資料なし）

~~~diff
- 00bd0a20 ["INT_ADD", "register:40f0:8", ["const:bd0a20:8", "const:4:8"]]
- 00bd0a20 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0e48 ["INT_ADD", "register:40f0:8", ["const:bd0e48:8", "const:4:8"]]
+ 00bd0e48 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0a20 bytes 3c280294
+ 00bd0e48 bytes 32280294
- 00bd0a28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00bd0a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0e50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00bd0e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0a28 bytes 605602f9
+ 00bd0e50 bytes 605604f9
- 00bd0a08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00bd0a08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0e30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00bd0e30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd0a08 bytes 685642f9
+ 00bd0e30 bytes 685644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-096f28787689f6e3d2d4c3950512c0dd"></a>

### [`00bd0ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md) → [`00bd0edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0edc.md) _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bd0ab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0ab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0abc",
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
      "00bd0edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0ee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0ee4",
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

- 旧版 [`00bd0ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md#insn-00bd0ab4) · [`00bd0ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md#insn-00bd0ab8) · [`00bd0abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md#insn-00bd0abc)

~~~diff
- 00bd0ab4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd0ab4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd0ab4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0ab4 bytes f50f1df8
- 00bd0ab8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0ab8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0ab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0ab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0ab8 bytes f44f01a9
- 00bd0abc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0abc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0abc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd0abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0abc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97338f648df15d2e97d8f25771432ac"></a>

### [`00bd0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b24.md) → [`00bd0f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0f4c.md) _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd0f8c",
      "incomplete_value": true,
      "site": "00bd0f8c",
      "value": [
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
      "definition_site": "00bd0b64",
      "incomplete_value": true,
      "site": "00bd0b64",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0f68",
      "incomplete_value": true,
      "site": "00bd0f68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0b40",
      "incomplete_value": true,
      "site": "00bd0b40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd0b4c",
      "incomplete_value": true,
      "site": "00bd0b5c",
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
      "00bd0f60",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0b48",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0f8c",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0f60",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0f70",
      "PARAM",
      [
        "storage",
        "002a7450",
        null,
        "string"
      ]
    ],
    [
      "00bd0f8c",
      "WRITE",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b24.md#insn-00bd0b5c) · [`00bd0b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b24.md#insn-00bd0b64) · [`00bd0b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b24.md#insn-00bd0b38)
- 新版 `00bd0f84`（命令位置の公開資料なし） · `00bd0f8c`（命令位置の公開資料なし） · `00bd0f60`（命令位置の公開資料なし）

~~~diff
- 00bd0b5c ["INT_ADD", "register:40f0:8", ["const:bd0b5c:8", "const:4:8"]]
- 00bd0b5c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd0f84 ["INT_ADD", "register:40f0:8", ["const:bd0f84:8", "const:4:8"]]
+ 00bd0f84 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0b5c bytes ed270294
+ 00bd0f84 bytes e3270294
- 00bd0b64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00bd0b64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0f8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00bd0f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0b64 bytes 805602f9
+ 00bd0f8c bytes 805604f9
- 00bd0b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00bd0b38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd0f60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00bd0f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd0b38 bytes 815642f9
+ 00bd0f60 bytes 815644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa0b76391513826173912e6c6e0a797c"></a>

### [`00bd0b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md) → [`00bd0fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0fbc.md) _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd0fd8",
      "incomplete_value": false,
      "site": "00bd0fdc",
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
      "definition_site": "00bd0bb0",
      "incomplete_value": false,
      "site": "00bd0bb4",
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
      "definition_site": "00bd0fe8",
      "incomplete_value": true,
      "site": "00bd0ff4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd0bc0",
      "incomplete_value": true,
      "site": "00bd0bcc",
      "value": [
        "LOAD",
        "8",
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
      "00bd0fd8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd0fe8",
      "DATA",
      [
        "storage",
        "011264b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0fd8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd0fe8",
      "DATA",
      [
        "storage",
        "011268b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md#insn-00bd0bb4) · [`00bd0bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md#insn-00bd0bb0) · [`00bd0bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md#insn-00bd0bbc)
- 新版 `00bd0fdc`（命令位置の公開資料なし） · `00bd0fd8`（命令位置の公開資料なし） · `00bd0fe4`（命令位置の公開資料なし）

~~~diff
- 00bd0bb4 ["INT_ADD", "register:40f0:8", ["const:bd0bb4:8", "const:4:8"]]
- 00bd0bb4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd0fdc ["INT_ADD", "register:40f0:8", ["const:bd0fdc:8", "const:4:8"]]
+ 00bd0fdc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd0bb4 bytes 13280294
+ 00bd0fdc bytes 09280294
- 00bd0bb0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd0bb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0bb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd0bb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0fd8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd0fd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0fd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0fd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd0bb0 bytes 00680a91
+ 00bd0fd8 bytes 009c0d91
- 00bd0bbc ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00bd0bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd0fe4 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00bd0fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd0bbc bytes 08e11291
+ 00bd0fe4 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a1b787578b4b41e6dbaa8c02ffc8854"></a>

### [`00bd0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0bd0.md) → [`00bd0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0ff8.md) _ZN8firebase4auth27api_not_available_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd0bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0bd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0bd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0be4",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd100c",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0bd0.md#insn-00bd0bd0) · [`00bd0bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0bd0.md#insn-00bd0bd4) · [`00bd0bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0bd0.md#insn-00bd0bec)

~~~diff
- 00bd0bd0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0bd0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0bd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd0bd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0bd0 bytes f44fbea9
- 00bd0bd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0bd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0bd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0bd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0bd4 bytes fd7b01a9
- 00bd0bec ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd0bec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0bec bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8f2e2b32e8f761d57e2a56ae00c95b"></a>

### [`00bd0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c7c.md) → [`00bd10a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd10a4.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd0ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd10d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd10b8",
      "incomplete_value": true,
      "site": "00bd10b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0c90",
      "incomplete_value": true,
      "site": "00bd0c90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd10b4",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0c9c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0ca0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd10b4",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd10c4",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ],
    [
      "00bd10c8",
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

- 旧版 [`00bd0c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c7c.md#insn-00bd0c90) · [`00bd0ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c7c.md#insn-00bd0ca0) · [`00bd0ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c7c.md#insn-00bd0ca8)
- 新版 `00bd10b8`（命令位置の公開資料なし）

~~~diff
- 00bd0c90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd0c90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd10b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd10b8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0c90 bytes e80000b5
+ 00bd10b8 bytes e80000b5
- 00bd0ca0 ["INT_ADD", "register:40f0:8", ["const:bd0ca0:8", "const:4:8"]]
- 00bd0ca0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0ca0 bytes 9c270294
- 00bd0ca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00bd0ca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0ca8 bytes 606602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-025a1d3db2a5736302e81bcd4cba3a1b"></a>

### [`00bd0d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d40.md) → [`00bd1168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1168.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bd0d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1198"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd117c",
      "incomplete_value": true,
      "site": "00bd117c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0d54",
      "incomplete_value": true,
      "site": "00bd0d54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd1178",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd117c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0d74"
      ]
    ],
    [
      "unmatched:00bd0d5c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1178",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd117c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd119c"
      ]
    ],
    [
      "00bd1184",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d40.md#insn-00bd0d68) · [`00bd0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d40.md#insn-00bd0d70) · [`00bd0d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d40.md#insn-00bd0d80)
- 新版 `00bd1190`（命令位置の公開資料なし）

~~~diff
- 00bd0d68 ["INT_ADD", "register:40f0:8", ["const:bd0d68:8", "const:4:8"]]
- 00bd0d68 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1190 ["INT_ADD", "register:40f0:8", ["const:bd1190:8", "const:4:8"]]
+ 00bd1190 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0d68 bytes 6a270294
+ 00bd1190 bytes 60270294
- 00bd0d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00bd0d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0d70 bytes 606602f9
- 00bd0d80 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0d80 ["RETURN", null, ["register:0:8"]]
- 00bd0d80 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6950b34652306e62ed2655a6cce44e9"></a>

### [`00bd0dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0dfc.md) → [`00bd1224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1224.md) _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bd0dfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0e00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0e04",
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
      "00bd1224",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd1228",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd122c",
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

- 旧版 [`00bd0dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0dfc.md#insn-00bd0dfc) · [`00bd0e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0dfc.md#insn-00bd0e00) · [`00bd0e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0dfc.md#insn-00bd0e04)

~~~diff
- 00bd0dfc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd0dfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd0dfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0dfc bytes f50f1df8
- 00bd0e00 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0e00 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0e00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0e00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0e00 bytes f44f01a9
- 00bd0e04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0e04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0e04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd0e04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0e04 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-836b3d583acba9e9338efd71e6df5133"></a>

### [`00bd0e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0e6c.md) → [`00bd1294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1294.md) _ZN8firebase4auth21action_code_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd0eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd12d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0e88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0e80",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd12d8"
      ]
    ],
    [
      "unmatched:00bd0e90",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd12a8",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd12b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd12d8"
      ]
    ],
    [
      "00bd12b8",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0e6c.md#insn-00bd0e88) · [`00bd0ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0e6c.md#insn-00bd0ea4) · [`00bd0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0e6c.md#insn-00bd0eac)
- 新版 `00bd12cc`（命令位置の公開資料なし）

~~~diff
- 00bd0e88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd0e88 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0e88 bytes 410100b5
- 00bd0ea4 ["INT_ADD", "register:40f0:8", ["const:bd0ea4:8", "const:4:8"]]
- 00bd0ea4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd12cc ["INT_ADD", "register:40f0:8", ["const:bd12cc:8", "const:4:8"]]
+ 00bd12cc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0ea4 bytes 1b270294
+ 00bd12cc bytes 11270294
- 00bd0eac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00bd0eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0eac bytes 806602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-099a65dc5560e9132b04a2843a7290f1"></a>

### [`00bd0f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f18.md) → [`00bd1340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1340.md) _ZN8firebase4auth21action_code_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd0f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1380"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0f34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0f2c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0f34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1384"
      ]
    ],
    [
      "unmatched:00bd0f3c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1354",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd135c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1384"
      ]
    ],
    [
      "00bd1364",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f18.md#insn-00bd0f34) · [`00bd0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f18.md#insn-00bd0f50) · [`00bd0f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f18.md#insn-00bd0f58)
- 新版 `00bd1378`（命令位置の公開資料なし）

~~~diff
- 00bd0f34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd0f34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd0f34 bytes 410100b5
- 00bd0f50 ["INT_ADD", "register:40f0:8", ["const:bd0f50:8", "const:4:8"]]
- 00bd0f50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1378 ["INT_ADD", "register:40f0:8", ["const:bd1378:8", "const:4:8"]]
+ 00bd1378 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0f50 bytes f0260294
+ 00bd1378 bytes e6260294
- 00bd0f58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00bd0f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0f58 bytes 806602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f60d611c65b85d82b21aec598574dccd"></a>

### [`00bd0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0fc4.md) → [`00bd13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13ec.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00bd1418",
      "incomplete_value": true,
      "site": "00bd1418",
      "value": [
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
      "definition_site": "00bd0ff0",
      "incomplete_value": true,
      "site": "00bd0ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "definition_site": "00bd1400",
      "incomplete_value": true,
      "site": "00bd1400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0fd8",
      "incomplete_value": true,
      "site": "00bd0fd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd140c",
      "incomplete_value": false,
      "site": "00bd1410",
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
            "const:c84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0fe4",
      "incomplete_value": false,
      "site": "00bd0fe8",
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
            "const:bb7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd13fc",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd140c",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ],
    [
      "00bd1418",
      "WRITE",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd13fc",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd140c",
      "PARAM",
      [
        "storage",
        "002a1c84",
        null,
        "string"
      ]
    ],
    [
      "00bd1418",
      "WRITE",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0fc4.md#insn-00bd0fe8) · [`00bd0ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0fc4.md#insn-00bd0ff0) · [`00bd0fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0fc4.md#insn-00bd0fd4)
- 新版 `00bd1410`（命令位置の公開資料なし） · `00bd1418`（命令位置の公開資料なし） · `00bd13fc`（命令位置の公開資料なし）

~~~diff
- 00bd0fe8 ["INT_ADD", "register:40f0:8", ["const:bd0fe8:8", "const:4:8"]]
- 00bd0fe8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1410 ["INT_ADD", "register:40f0:8", ["const:bd1410:8", "const:4:8"]]
+ 00bd1410 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0fe8 bytes ca260294
+ 00bd1410 bytes c0260294
- 00bd0ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd0ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00bd1418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0ff0 bytes 607602f9
+ 00bd1418 bytes 607604f9
- 00bd0fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd0fd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd13fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00bd13fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd0fd4 bytes 687642f9
+ 00bd13fc bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccdb07bf774ff191414cd8cdaae4ccb"></a>

### [`00bd1044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1044.md) → [`00bd146c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd146c.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd149c",
      "incomplete_value": true,
      "site": "00bd149c",
      "value": [
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
      "definition_site": "00bd1074",
      "incomplete_value": true,
      "site": "00bd1074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "definition_site": "00bd1480",
      "incomplete_value": true,
      "site": "00bd1480",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1058",
      "incomplete_value": true,
      "site": "00bd1058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd148c",
      "incomplete_value": false,
      "site": "00bd1494",
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
            "const:c84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1064",
      "incomplete_value": false,
      "site": "00bd106c",
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
            "const:bb7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd147c",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd148c",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ],
    [
      "00bd149c",
      "WRITE",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd147c",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd148c",
      "PARAM",
      [
        "storage",
        "002a1c84",
        null,
        "string"
      ]
    ],
    [
      "00bd149c",
      "WRITE",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd106c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1044.md#insn-00bd106c) · [`00bd1074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1044.md#insn-00bd1074) · [`00bd1054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1044.md#insn-00bd1054)
- 新版 `00bd1494`（命令位置の公開資料なし） · `00bd149c`（命令位置の公開資料なし） · `00bd147c`（命令位置の公開資料なし）

~~~diff
- 00bd106c ["INT_ADD", "register:40f0:8", ["const:bd106c:8", "const:4:8"]]
- 00bd106c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1494 ["INT_ADD", "register:40f0:8", ["const:bd1494:8", "const:4:8"]]
+ 00bd1494 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd106c bytes a9260294
+ 00bd1494 bytes 9f260294
- 00bd1074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd1074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd149c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00bd149c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1074 bytes 607602f9
+ 00bd149c bytes 607604f9
- 00bd1054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd1054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd147c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00bd147c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1054 bytes 687642f9
+ 00bd147c bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7115ad524a558657a7e86bb242d0b3d"></a>

### [`00bd1088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1088.md) → [`00bd14b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd14b0.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00bd10b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd14e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd109c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd14c0",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd109c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd14e4"
      ]
    ],
    [
      "unmatched:00bd10a4",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd14c0",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd14c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd14e4"
      ]
    ],
    [
      "00bd14cc",
      "PARAM",
      [
        "storage",
        "002a1c84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd109c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1088.md#insn-00bd109c) · [`00bd10b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1088.md#insn-00bd10b0) · [`00bd10b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1088.md#insn-00bd10b8)
- 新版 `00bd14d8`（命令位置の公開資料なし）

~~~diff
- 00bd109c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd109c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd109c bytes 080100b5
- 00bd10b0 ["INT_ADD", "register:40f0:8", ["const:bd10b0:8", "const:4:8"]]
- 00bd10b0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd14d8 ["INT_ADD", "register:40f0:8", ["const:bd14d8:8", "const:4:8"]]
+ 00bd14d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd10b0 bytes 98260294
+ 00bd14d8 bytes 8e260294
- 00bd10b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd10b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd10b8 bytes 607602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b27605a6648a6317e4aeb448b73aaf37"></a>

### [`00bd10d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd10d8.md) → [`00bd1500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1500.md) _ZN8firebase4auth15email_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd1558",
      "incomplete_value": true,
      "site": "00bd1558",
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
      "definition_site": "00bd1130",
      "incomplete_value": true,
      "site": "00bd1130",
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
            "const:4f0:8"
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
      "definition_site": "00bd1534",
      "incomplete_value": true,
      "site": "00bd1540",
      "value": [
        "LOAD",
        "8",
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
                "const:8e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd110c",
      "incomplete_value": true,
      "site": "00bd1118",
      "value": [
        "LOAD",
        "8",
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
                "const:4e8:8"
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
      "00bd1514",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1534",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1558",
      "WRITE",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1514",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1534",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1558",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd10d8.md#insn-00bd1118) · [`00bd1130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd10d8.md#insn-00bd1130) · [`00bd10ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd10d8.md#insn-00bd10ec)
- 新版 `00bd1540`（命令位置の公開資料なし） · `00bd1558`（命令位置の公開資料なし） · `00bd1514`（命令位置の公開資料なし）

~~~diff
- 00bd1118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1118 ["INT_ADD", "register:40f0:8", ["const:bd1118:8", "const:4:8"]]
- 00bd1118 ["CALLIND", null, ["register:0:8"]]
+ 00bd1540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1540 ["INT_ADD", "register:40f0:8", ["const:bd1540:8", "const:4:8"]]
+ 00bd1540 ["CALLIND", null, ["register:0:8"]]
- 00bd1118 bytes 00013fd6
+ 00bd1540 bytes 00013fd6
- 00bd1130 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1130 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
- 00bd1130 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1558 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1558 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f0:8"]]
+ 00bd1558 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1130 bytes a0c21339
+ 00bd1558 bytes a0c22339
- 00bd10ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
- 00bd10ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd10ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd1514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
+ 00bd1514 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1514 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd10ec bytes a8c25339
+ 00bd1514 bytes a8c26339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200702daafbbd487bd8ddfa266b564c4"></a>

### [`00bd1144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1144.md) → [`00bd156c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd156c.md) _ZN8firebase4auth15email_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bd1180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd15a8"
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
      "00bd1580",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd158c",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd1184"
      ]
    ]
  ],
  "added": [
    [
      "00bd1580",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd158c",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd15ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd115c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1144.md#insn-00bd115c) · [`00bd1180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1144.md#insn-00bd1180) · [`00bd1188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1144.md#insn-00bd1188)
- 新版 `00bd1584`（命令位置の公開資料なし）

~~~diff
- 00bd115c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd115c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd1584 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd1584 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd115c bytes 410200b4
+ 00bd1584 bytes 410200b4
- 00bd1180 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd1180 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd1180 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4f0:8"]]
- 00bd1180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd1180 bytes bfc21339
- 00bd1188 ["INT_ADD", "register:40f0:8", ["const:bd1188:8", "const:4:8"]]
- 00bd1188 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd1188 bytes 76260294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3277a4ac44cd2a04f91680c8d35bea76"></a>

### [`00bd11b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd11b4.md) → [`00bd15dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd15dc.md) _ZN8firebase4auth15email_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bd11b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd11b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd11b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd11c8",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd15dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd15e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd15f0",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd11b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd11b4.md#insn-00bd11b4) · [`00bd11b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd11b4.md#insn-00bd11b8) · [`00bd11d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd11b4.md#insn-00bd11d0)

~~~diff
- 00bd11b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd11b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd11b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd11b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd11b4 bytes f44fbea9
- 00bd11b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd11b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd11b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd11b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd11b8 bytes fd7b01a9
- 00bd11d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd11d0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd11d0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d8560f1c4071015ea0de2839c87203"></a>

### [`00bd1224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1224.md) → [`00bd164c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd164c.md) _ZN8firebase4auth15email_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd1668",
      "incomplete_value": false,
      "site": "00bd166c",
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
      "definition_site": "00bd1240",
      "incomplete_value": false,
      "site": "00bd1244",
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
      "definition_site": "00bd1678",
      "incomplete_value": true,
      "site": "00bd1684",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd1250",
      "incomplete_value": true,
      "site": "00bd125c",
      "value": [
        "LOAD",
        "8",
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
      "00bd1668",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd1678",
      "DATA",
      [
        "storage",
        "011264f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1668",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd1678",
      "DATA",
      [
        "storage",
        "011268f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1224.md#insn-00bd1244) · [`00bd1240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1224.md#insn-00bd1240) · [`00bd124c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1224.md#insn-00bd124c)
- 新版 `00bd166c`（命令位置の公開資料なし） · `00bd1668`（命令位置の公開資料なし） · `00bd1674`（命令位置の公開資料なし）

~~~diff
- 00bd1244 ["INT_ADD", "register:40f0:8", ["const:bd1244:8", "const:4:8"]]
- 00bd1244 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd166c ["INT_ADD", "register:40f0:8", ["const:bd166c:8", "const:4:8"]]
+ 00bd166c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1244 bytes 6f260294
+ 00bd166c bytes 65260294
- 00bd1240 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd1240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1668 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd1668 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1668 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1668 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd1240 bytes 00680a91
+ 00bd1668 bytes 009c0d91
- 00bd124c ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00bd124c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd124c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd124c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1674 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00bd1674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd124c bytes 08e11391
+ 00bd1674 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98d90e1d802c6edae6ee5fc7b501b2ef"></a>

### [`00bd1260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1260.md) → [`00bd1688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1688.md) _ZN8firebase4auth15email_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd12a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd16c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd127c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1274",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd127c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd16cc"
      ]
    ],
    [
      "unmatched:00bd1284",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd169c",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd16a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd16cc"
      ]
    ],
    [
      "00bd16ac",
      "PARAM",
      [
        "storage",
        "002a1c84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd127c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1260.md#insn-00bd127c) · [`00bd1298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1260.md#insn-00bd1298) · [`00bd12a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1260.md#insn-00bd12a0)
- 新版 `00bd16c0`（命令位置の公開資料なし）

~~~diff
- 00bd127c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd127c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd127c bytes 410100b5
- 00bd1298 ["INT_ADD", "register:40f0:8", ["const:bd1298:8", "const:4:8"]]
- 00bd1298 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd16c0 ["INT_ADD", "register:40f0:8", ["const:bd16c0:8", "const:4:8"]]
+ 00bd16c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1298 bytes 1e260294
+ 00bd16c0 bytes 14260294
- 00bd12a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00bd12a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd12a0 bytes 807602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5460a1015b1d90fd262b2b59599b43e0"></a>

### [`00bd130c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd130c.md) → [`00bd1734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1734.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bd1760",
      "incomplete_value": true,
      "site": "00bd1760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1338",
      "incomplete_value": true,
      "site": "00bd1338",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1748",
      "incomplete_value": true,
      "site": "00bd1748",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1320",
      "incomplete_value": true,
      "site": "00bd1320",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1754",
      "incomplete_value": false,
      "site": "00bd1758",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd132c",
      "incomplete_value": false,
      "site": "00bd1330",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1744",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1754",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1760",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1744",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1754",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ],
    [
      "00bd1760",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd130c.md#insn-00bd1330) · [`00bd1338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd130c.md#insn-00bd1338) · [`00bd131c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd130c.md#insn-00bd131c)
- 新版 `00bd1758`（命令位置の公開資料なし） · `00bd1760`（命令位置の公開資料なし） · `00bd1744`（命令位置の公開資料なし）

~~~diff
- 00bd1330 ["INT_ADD", "register:40f0:8", ["const:bd1330:8", "const:4:8"]]
- 00bd1330 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1758 ["INT_ADD", "register:40f0:8", ["const:bd1758:8", "const:4:8"]]
+ 00bd1758 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1330 bytes f8250294
+ 00bd1758 bytes ee250294
- 00bd1338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd1338 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd1760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1338 bytes 608602f9
+ 00bd1760 bytes 608604f9
- 00bd131c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd131c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1744 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd1744 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd131c bytes 688642f9
+ 00bd1744 bytes 688644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b7e341b78652b02df4b261837a6bcb"></a>

### [`00bd134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd134c.md) → [`00bd1774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1774.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bd17a0",
      "incomplete_value": true,
      "site": "00bd17a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1378",
      "incomplete_value": true,
      "site": "00bd1378",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1788",
      "incomplete_value": true,
      "site": "00bd1788",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1360",
      "incomplete_value": true,
      "site": "00bd1360",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1790",
      "incomplete_value": false,
      "site": "00bd1798",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1368",
      "incomplete_value": false,
      "site": "00bd1370",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1784",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1790",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd17a0",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1784",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1790",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ],
    [
      "00bd17a0",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd134c.md#insn-00bd1370) · [`00bd1378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd134c.md#insn-00bd1378) · [`00bd135c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd134c.md#insn-00bd135c)
- 新版 `00bd1798`（命令位置の公開資料なし） · `00bd17a0`（命令位置の公開資料なし） · `00bd1784`（命令位置の公開資料なし）

~~~diff
- 00bd1370 ["INT_ADD", "register:40f0:8", ["const:bd1370:8", "const:4:8"]]
- 00bd1370 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1798 ["INT_ADD", "register:40f0:8", ["const:bd1798:8", "const:4:8"]]
+ 00bd1798 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1370 bytes e8250294
+ 00bd1798 bytes de250294
- 00bd1378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd1378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd17a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd17a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1378 bytes 608602f9
+ 00bd17a0 bytes 608604f9
- 00bd135c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd135c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1784 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd1784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd135c bytes 688642f9
+ 00bd1784 bytes 688644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e5d2ed5cfa3a09224a26686adac376e"></a>

### [`00bd13d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd13d0.md) → [`00bd17f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd17f8.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1828",
      "incomplete_value": true,
      "site": "00bd1828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1400",
      "incomplete_value": true,
      "site": "00bd1400",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd180c",
      "incomplete_value": true,
      "site": "00bd180c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd13e4",
      "incomplete_value": true,
      "site": "00bd13e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1814",
      "incomplete_value": false,
      "site": "00bd1820",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd13ec",
      "incomplete_value": false,
      "site": "00bd13f8",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1808",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1814",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1828",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1808",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1814",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ],
    [
      "00bd1828",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd13f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd13d0.md#insn-00bd13f8) · [`00bd1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd13d0.md#insn-00bd1400) · [`00bd13e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd13d0.md#insn-00bd13e0)
- 新版 `00bd1820`（命令位置の公開資料なし） · `00bd1828`（命令位置の公開資料なし） · `00bd1808`（命令位置の公開資料なし）

~~~diff
- 00bd13f8 ["INT_ADD", "register:40f0:8", ["const:bd13f8:8", "const:4:8"]]
- 00bd13f8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1820 ["INT_ADD", "register:40f0:8", ["const:bd1820:8", "const:4:8"]]
+ 00bd1820 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd13f8 bytes c6250294
+ 00bd1820 bytes bc250294
- 00bd1400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd1400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1828 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd1828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1400 bytes 608602f9
+ 00bd1828 bytes 608604f9
- 00bd13e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd13e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00bd1808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd13e0 bytes 688642f9
+ 00bd1808 bytes 688644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b9eb0475373e2caa2ca713c47d01e5"></a>

### [`00bd1420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1420.md) → [`00bd1848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1848.md) _ZN8firebase4auth23weak_password_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd18a0",
      "incomplete_value": true,
      "site": "00bd18a0",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1478",
      "incomplete_value": true,
      "site": "00bd1478",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd187c",
      "incomplete_value": true,
      "site": "00bd1888",
      "value": [
        "LOAD",
        "8",
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1454",
      "incomplete_value": true,
      "site": "00bd1460",
      "value": [
        "LOAD",
        "8",
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
                "const:508:8"
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
      "00bd185c",
      "READ",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd187c",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd18a0",
      "WRITE",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd185c",
      "READ",
      [
        "storage",
        "01126910",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd187c",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd18a0",
      "WRITE",
      [
        "storage",
        "01126910",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1420.md#insn-00bd1460) · [`00bd1478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1420.md#insn-00bd1478) · [`00bd1434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1420.md#insn-00bd1434)
- 新版 `00bd1888`（命令位置の公開資料なし） · `00bd18a0`（命令位置の公開資料なし） · `00bd185c`（命令位置の公開資料なし）

~~~diff
- 00bd1460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1460 ["INT_ADD", "register:40f0:8", ["const:bd1460:8", "const:4:8"]]
- 00bd1460 ["CALLIND", null, ["register:0:8"]]
+ 00bd1888 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1888 ["INT_ADD", "register:40f0:8", ["const:bd1888:8", "const:4:8"]]
+ 00bd1888 ["CALLIND", null, ["register:0:8"]]
- 00bd1460 bytes 00013fd6
+ 00bd1888 bytes 00013fd6
- 00bd1478 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1478 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:510:8"]]
- 00bd1478 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd18a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd18a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:910:8"]]
+ 00bd18a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1478 bytes a0421439
+ 00bd18a0 bytes a0422439
- 00bd1434 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00bd1434 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd1434 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd185c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:910:8"]]
+ 00bd185c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd185c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd1434 bytes a8425439
+ 00bd185c bytes a8426439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9a9615fd9422105467587bb4d13e99"></a>

### [`00bd148c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd148c.md) → [`00bd18b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd18b4.md) _ZN8firebase4auth23weak_password_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bd14c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd14e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd18f0"
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
      "00bd18c8",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd18d4",
      "READ",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd18dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd14cc"
      ]
    ]
  ],
  "added": [
    [
      "00bd18c8",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd18d4",
      "READ",
      [
        "storage",
        "01126910",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd18dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd18f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd14a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd148c.md#insn-00bd14a4) · [`00bd14c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd148c.md#insn-00bd14c8) · [`00bd14d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd148c.md#insn-00bd14d0)
- 新版 `00bd18cc`（命令位置の公開資料なし）

~~~diff
- 00bd14a4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd14a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd18cc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd18cc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd14a4 bytes 410200b4
+ 00bd18cc bytes 410200b4
- 00bd14c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd14c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd14c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
- 00bd14c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd14c8 bytes bf421439
- 00bd14d0 ["INT_ADD", "register:40f0:8", ["const:bd14d0:8", "const:4:8"]]
- 00bd14d0 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd14d0 bytes a4250294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719eca5e36fa6ed7f5c27a7a88311d11"></a>

### [`00bd14fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd14fc.md) → [`00bd1924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1924.md) _ZN8firebase4auth23weak_password_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1964",
      "incomplete_value": true,
      "site": "00bd1964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd153c",
      "incomplete_value": true,
      "site": "00bd153c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1940",
      "incomplete_value": true,
      "site": "00bd1940",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1518",
      "incomplete_value": true,
      "site": "00bd1518",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1948",
      "incomplete_value": false,
      "site": "00bd195c",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1520",
      "incomplete_value": false,
      "site": "00bd1534",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1938",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1948",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1964",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1938",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1948",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ],
    [
      "00bd1964",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd14fc.md#insn-00bd1534) · [`00bd153c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd14fc.md#insn-00bd153c) · [`00bd1510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd14fc.md#insn-00bd1510)
- 新版 `00bd195c`（命令位置の公開資料なし） · `00bd1964`（命令位置の公開資料なし） · `00bd1938`（命令位置の公開資料なし）

~~~diff
- 00bd1534 ["INT_ADD", "register:40f0:8", ["const:bd1534:8", "const:4:8"]]
- 00bd1534 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd195c ["INT_ADD", "register:40f0:8", ["const:bd195c:8", "const:4:8"]]
+ 00bd195c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1534 bytes 77250294
+ 00bd195c bytes 6d250294
- 00bd153c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00bd153c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1964 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00bd1964 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd153c bytes 808602f9
+ 00bd1964 bytes 808604f9
- 00bd1510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00bd1510 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1938 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00bd1938 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1510 bytes 818642f9
+ 00bd1938 bytes 818644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b2745cfb20695bf6418e60844eccbd"></a>

### [`00bd156c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd156c.md) → [`00bd1994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1994.md) _ZN8firebase4auth23weak_password_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd19b0",
      "incomplete_value": false,
      "site": "00bd19b4",
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
      "definition_site": "00bd1588",
      "incomplete_value": false,
      "site": "00bd158c",
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
      "definition_site": "00bd19c0",
      "incomplete_value": true,
      "site": "00bd19cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd1598",
      "incomplete_value": true,
      "site": "00bd15a4",
      "value": [
        "LOAD",
        "8",
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
      "00bd19b0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd19c0",
      "DATA",
      [
        "storage",
        "01126518",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd19b0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd19c0",
      "DATA",
      [
        "storage",
        "01126918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd158c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd156c.md#insn-00bd158c) · [`00bd1588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd156c.md#insn-00bd1588) · [`00bd1594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd156c.md#insn-00bd1594)
- 新版 `00bd19b4`（命令位置の公開資料なし） · `00bd19b0`（命令位置の公開資料なし） · `00bd19bc`（命令位置の公開資料なし）

~~~diff
- 00bd158c ["INT_ADD", "register:40f0:8", ["const:bd158c:8", "const:4:8"]]
- 00bd158c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd19b4 ["INT_ADD", "register:40f0:8", ["const:bd19b4:8", "const:4:8"]]
+ 00bd19b4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd158c bytes 9d250294
+ 00bd19b4 bytes 93250294
- 00bd1588 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd1588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd19b0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd19b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd19b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd19b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd1588 bytes 00680a91
+ 00bd19b0 bytes 009c0d91
- 00bd1594 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00bd1594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd19bc ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00bd19bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd19bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd19bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1594 bytes 08611491
+ 00bd19bc bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4c8ca9bfe63921fb7273f4c42f6a0f3"></a>

### [`00bd15a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd15a8.md) → [`00bd19d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd19d0.md) _ZN8firebase4auth23weak_password_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1a10",
      "incomplete_value": true,
      "site": "00bd1a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd15e8",
      "incomplete_value": true,
      "site": "00bd15e8",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd19ec",
      "incomplete_value": true,
      "site": "00bd19ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd15c4",
      "incomplete_value": true,
      "site": "00bd15c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd19f4",
      "incomplete_value": false,
      "site": "00bd1a08",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd15cc",
      "incomplete_value": false,
      "site": "00bd15e0",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd19e4",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19f4",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1a10",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd19e4",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19f4",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ],
    [
      "00bd1a10",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd15a8.md#insn-00bd15e0) · [`00bd15e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd15a8.md#insn-00bd15e8) · [`00bd15bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd15a8.md#insn-00bd15bc)
- 新版 `00bd1a08`（命令位置の公開資料なし） · `00bd1a10`（命令位置の公開資料なし） · `00bd19e4`（命令位置の公開資料なし）

~~~diff
- 00bd15e0 ["INT_ADD", "register:40f0:8", ["const:bd15e0:8", "const:4:8"]]
- 00bd15e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1a08 ["INT_ADD", "register:40f0:8", ["const:bd1a08:8", "const:4:8"]]
+ 00bd1a08 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd15e0 bytes 4c250294
+ 00bd1a08 bytes 42250294
- 00bd15e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00bd15e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1a10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00bd1a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd15e8 bytes 808602f9
+ 00bd1a10 bytes 808604f9
- 00bd15bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00bd15bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd19e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00bd19e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd15bc bytes 818642f9
+ 00bd19e4 bytes 818644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c729e10dfdd149a9b71a857115cdb401"></a>

### [`00bd1618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1618.md) → [`00bd1a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1a40.md) _ZN8firebase4auth23weak_password_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd1a5c",
      "incomplete_value": false,
      "site": "00bd1a60",
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
      "definition_site": "00bd1634",
      "incomplete_value": false,
      "site": "00bd1638",
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
      "definition_site": "00bd1a6c",
      "incomplete_value": true,
      "site": "00bd1a78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd1644",
      "incomplete_value": true,
      "site": "00bd1650",
      "value": [
        "LOAD",
        "8",
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
      "00bd1a5c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd1a6c",
      "DATA",
      [
        "storage",
        "01126520",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1a5c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd1a6c",
      "DATA",
      [
        "storage",
        "01126920",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1618.md#insn-00bd1638) · [`00bd1634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1618.md#insn-00bd1634) · [`00bd1640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1618.md#insn-00bd1640)
- 新版 `00bd1a60`（命令位置の公開資料なし） · `00bd1a5c`（命令位置の公開資料なし） · `00bd1a68`（命令位置の公開資料なし）

~~~diff
- 00bd1638 ["INT_ADD", "register:40f0:8", ["const:bd1638:8", "const:4:8"]]
- 00bd1638 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd1a60 ["INT_ADD", "register:40f0:8", ["const:bd1a60:8", "const:4:8"]]
+ 00bd1a60 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1638 bytes 72250294
+ 00bd1a60 bytes 68250294
- 00bd1634 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd1634 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1634 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1634 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1a5c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd1a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd1634 bytes 00441191
+ 00bd1a5c bytes 00781491
- 00bd1640 ["COPY", "tmp:0:8", ["const:520:8"]]
- 00bd1640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1a68 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00bd1a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1640 bytes 08811491
+ 00bd1a68 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5823d02d67d4e1dd3f793a8e592e0fae"></a>

### [`00bd1654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1654.md) → [`00bd1a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1a7c.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

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
      "definition_site": "00bd1aa8",
      "incomplete_value": true,
      "site": "00bd1aa8",
      "value": [
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
    "old": {
      "definition_site": "00bd1680",
      "incomplete_value": true,
      "site": "00bd1680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00bd1a90",
      "incomplete_value": true,
      "site": "00bd1a90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1668",
      "incomplete_value": true,
      "site": "00bd1668",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1a9c",
      "incomplete_value": false,
      "site": "00bd1aa0",
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
            "const:c8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1674",
      "incomplete_value": false,
      "site": "00bd1678",
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
            "const:c4e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1a8c",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1a9c",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1aa8",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1a8c",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1a9c",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1aa8",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1654.md#insn-00bd1678) · [`00bd1680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1654.md#insn-00bd1680) · [`00bd1664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1654.md#insn-00bd1664)
- 新版 `00bd1aa0`（命令位置の公開資料なし） · `00bd1aa8`（命令位置の公開資料なし） · `00bd1a8c`（命令位置の公開資料なし）

~~~diff
- 00bd1678 ["INT_ADD", "register:40f0:8", ["const:bd1678:8", "const:4:8"]]
- 00bd1678 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1aa0 ["INT_ADD", "register:40f0:8", ["const:bd1aa0:8", "const:4:8"]]
+ 00bd1aa0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1678 bytes 26250294
+ 00bd1aa0 bytes 1c250294
- 00bd1680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd1680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1aa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00bd1aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1680 bytes 609602f9
+ 00bd1aa8 bytes 609604f9
- 00bd1664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd1664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1a8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00bd1a8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1664 bytes 689642f9
+ 00bd1a8c bytes 689644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9edf18d35343f6bd5574e4bfb9cffde3"></a>

### [`00bd1694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md) → [`00bd1abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1abc.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

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
      "definition_site": "00bd1ae8",
      "incomplete_value": true,
      "site": "00bd1ae8",
      "value": [
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
    "old": {
      "definition_site": "00bd16c0",
      "incomplete_value": true,
      "site": "00bd16c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00bd1ad0",
      "incomplete_value": true,
      "site": "00bd1ad0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd16a8",
      "incomplete_value": true,
      "site": "00bd16a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1ad8",
      "incomplete_value": false,
      "site": "00bd1ae0",
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
            "const:c8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd16b0",
      "incomplete_value": false,
      "site": "00bd16b8",
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
            "const:c4e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1acc",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ad8",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1ae8",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1acc",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ad8",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1ae8",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd16b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md#insn-00bd16b8) · [`00bd16c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md#insn-00bd16c0) · [`00bd16a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md#insn-00bd16a4)
- 新版 `00bd1ae0`（命令位置の公開資料なし） · `00bd1ae8`（命令位置の公開資料なし） · `00bd1acc`（命令位置の公開資料なし）

~~~diff
- 00bd16b8 ["INT_ADD", "register:40f0:8", ["const:bd16b8:8", "const:4:8"]]
- 00bd16b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1ae0 ["INT_ADD", "register:40f0:8", ["const:bd1ae0:8", "const:4:8"]]
+ 00bd1ae0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd16b8 bytes 16250294
+ 00bd1ae0 bytes 0c250294
- 00bd16c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd16c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1ae8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00bd1ae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd16c0 bytes 609602f9
+ 00bd1ae8 bytes 609604f9
- 00bd16a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd16a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1acc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00bd1acc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd16a4 bytes 689642f9
+ 00bd1acc bytes 689644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f722111a05f995db9da174f1661bac3"></a>

### [`00bd16d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md) → [`00bd1afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1afc.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd1704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1b2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1b10",
      "incomplete_value": true,
      "site": "00bd1b10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd16e8",
      "incomplete_value": true,
      "site": "00bd16e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd1b0c",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd16f4",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd16fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd1b0c",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b1c",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1b24",
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

- 旧版 [`00bd16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md#insn-00bd16e8) · [`00bd16fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md#insn-00bd16fc) · [`00bd1704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md#insn-00bd1704)
- 新版 `00bd1b10`（命令位置の公開資料なし）

~~~diff
- 00bd16e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd16e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd1b10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd1b10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd16e8 bytes 080100b5
+ 00bd1b10 bytes 080100b5
- 00bd16fc ["INT_ADD", "register:40f0:8", ["const:bd16fc:8", "const:4:8"]]
- 00bd16fc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd16fc bytes 05250294
- 00bd1704 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd1704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1704 bytes 609602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5ed5a2d89286ccb5dab7d96d967cf0"></a>

### [`00bd1718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1718.md) → [`00bd1b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1b40.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd1748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1b70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1b54",
      "incomplete_value": true,
      "site": "00bd1b54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd172c",
      "incomplete_value": true,
      "site": "00bd172c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd1b50",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1734",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd1748",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1b50",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b5c",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1b70",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd172c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1718.md#insn-00bd172c) · [`00bd1740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1718.md#insn-00bd1740) · [`00bd1748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1718.md#insn-00bd1748)
- 新版 `00bd1b54`（命令位置の公開資料なし） · `00bd1b68`（命令位置の公開資料なし）

~~~diff
- 00bd172c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd172c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd1b54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd1b54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd172c bytes 080100b5
+ 00bd1b54 bytes 080100b5
- 00bd1740 ["INT_ADD", "register:40f0:8", ["const:bd1740:8", "const:4:8"]]
- 00bd1740 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1b68 ["INT_ADD", "register:40f0:8", ["const:bd1b68:8", "const:4:8"]]
+ 00bd1b68 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1740 bytes f4240294
+ 00bd1b68 bytes ea240294
- 00bd1748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
- 00bd1748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1748 bytes 609602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7215bff0208c8b4f06c9a7c4e9c1764"></a>

### [`00bd1768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1768.md) → [`00bd1b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1b90.md) _ZN8firebase4auth29invalid_credentials_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd1be8",
      "incomplete_value": true,
      "site": "00bd1be8",
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
    "old": {
      "definition_site": "00bd17c0",
      "incomplete_value": true,
      "site": "00bd17c0",
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
            "const:530:8"
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
      "definition_site": "00bd1bc4",
      "incomplete_value": true,
      "site": "00bd1bd0",
      "value": [
        "LOAD",
        "8",
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd179c",
      "incomplete_value": true,
      "site": "00bd17a8",
      "value": [
        "LOAD",
        "8",
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
                "const:528:8"
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
      "00bd1ba4",
      "READ",
      [
        "storage",
        "01126530",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1bc4",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1be8",
      "WRITE",
      [
        "storage",
        "01126530",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1ba4",
      "READ",
      [
        "storage",
        "01126930",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1bc4",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1be8",
      "WRITE",
      [
        "storage",
        "01126930",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd17a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1768.md#insn-00bd17a8) · [`00bd17c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1768.md#insn-00bd17c0) · [`00bd177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1768.md#insn-00bd177c)
- 新版 `00bd1bd0`（命令位置の公開資料なし） · `00bd1be8`（命令位置の公開資料なし） · `00bd1ba4`（命令位置の公開資料なし）

~~~diff
- 00bd17a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd17a8 ["INT_ADD", "register:40f0:8", ["const:bd17a8:8", "const:4:8"]]
- 00bd17a8 ["CALLIND", null, ["register:0:8"]]
+ 00bd1bd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1bd0 ["INT_ADD", "register:40f0:8", ["const:bd1bd0:8", "const:4:8"]]
+ 00bd1bd0 ["CALLIND", null, ["register:0:8"]]
- 00bd17a8 bytes 00013fd6
+ 00bd1bd0 bytes 00013fd6
- 00bd17c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd17c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:530:8"]]
- 00bd17c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1be8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1be8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:930:8"]]
+ 00bd1be8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd17c0 bytes a0c21439
+ 00bd1be8 bytes a0c22439
- 00bd177c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:530:8"]]
- 00bd177c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd177c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd1ba4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:930:8"]]
+ 00bd1ba4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1ba4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd177c bytes a8c25439
+ 00bd1ba4 bytes a8c26439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4745c4f0f2ed7b3bc0267adffa12444"></a>

### [`00bd17d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd17d4.md) → [`00bd1bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1bfc.md) _ZN8firebase4auth29invalid_credentials_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd1c38",
      "incomplete_value": true,
      "site": "00bd1c38",
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
    "old": {
      "definition_site": "00bd1810",
      "incomplete_value": true,
      "site": "00bd1810",
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
            "const:530:8"
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
      "definition_site": "00bd1c58",
      "incomplete_value": true,
      "site": "00bd1c58",
      "value": [
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
    "old": {
      "definition_site": "00bd1830",
      "incomplete_value": true,
      "site": "00bd1830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00bd1c14",
      "incomplete_value": true,
      "site": "00bd1c14",
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
      "definition_site": "00bd17ec",
      "incomplete_value": true,
      "site": "00bd17ec",
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
      "00bd1c10",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1c1c",
      "READ",
      [
        "storage",
        "01126530",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1c38",
      "WRITE",
      [
        "storage",
        "01126530",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1c10",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1c1c",
      "READ",
      [
        "storage",
        "01126930",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1c38",
      "WRITE",
      [
        "storage",
        "01126930",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd17d4.md#insn-00bd1810) · [`00bd182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd17d4.md#insn-00bd182c) · [`00bd1830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd17d4.md#insn-00bd1830)
- 新版 `00bd1c38`（命令位置の公開資料なし） · `00bd1c54`（命令位置の公開資料なし） · `00bd1c58`（命令位置の公開資料なし）

~~~diff
- 00bd1810 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd1810 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd1810 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:530:8"]]
- 00bd1810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd1c38 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd1c38 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd1c38 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:930:8"]]
+ 00bd1c38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd1810 bytes bfc21439
+ 00bd1c38 bytes bfc22439
- 00bd182c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd182c ["INT_ADD", "register:40f0:8", ["const:bd182c:8", "const:4:8"]]
- 00bd182c ["CALLIND", null, ["register:0:8"]]
+ 00bd1c54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1c54 ["INT_ADD", "register:40f0:8", ["const:bd1c54:8", "const:4:8"]]
+ 00bd1c54 ["CALLIND", null, ["register:0:8"]]
- 00bd182c bytes 00013fd6
+ 00bd1c54 bytes 00013fd6
- 00bd1830 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:528:8"]]
- 00bd1830 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd1830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd1c58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00bd1c58 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd1c58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd1830 bytes 9f9602f9
+ 00bd1c58 bytes 9f9604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b3e969e338618ca269b3f2a7ef0c9b"></a>

### [`00bd1844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1844.md) → [`00bd1c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1c6c.md) _ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1cac",
      "incomplete_value": true,
      "site": "00bd1cac",
      "value": [
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
    "old": {
      "definition_site": "00bd1884",
      "incomplete_value": true,
      "site": "00bd1884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00bd1c88",
      "incomplete_value": true,
      "site": "00bd1c88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1860",
      "incomplete_value": true,
      "site": "00bd1860",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1c90",
      "incomplete_value": false,
      "site": "00bd1ca4",
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
            "const:c8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1868",
      "incomplete_value": false,
      "site": "00bd187c",
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
            "const:c4e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1c80",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1c90",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1cac",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1c80",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1c90",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1cac",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1844.md#insn-00bd187c) · [`00bd1884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1844.md#insn-00bd1884) · [`00bd1858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1844.md#insn-00bd1858)
- 新版 `00bd1ca4`（命令位置の公開資料なし） · `00bd1cac`（命令位置の公開資料なし） · `00bd1c80`（命令位置の公開資料なし）

~~~diff
- 00bd187c ["INT_ADD", "register:40f0:8", ["const:bd187c:8", "const:4:8"]]
- 00bd187c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1ca4 ["INT_ADD", "register:40f0:8", ["const:bd1ca4:8", "const:4:8"]]
+ 00bd1ca4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd187c bytes a5240294
+ 00bd1ca4 bytes 9b240294
- 00bd1884 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:528:8"]]
- 00bd1884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1cac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00bd1cac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1884 bytes 809602f9
+ 00bd1cac bytes 809604f9
- 00bd1858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:528:8"]]
- 00bd1858 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1c80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00bd1c80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1858 bytes 819642f9
+ 00bd1c80 bytes 819644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b697c0565d6a83fb429a2858f5207e0b"></a>

### [`00bd18b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md) → [`00bd1cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1cdc.md) _ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd1cf8",
      "incomplete_value": false,
      "site": "00bd1cfc",
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
      "definition_site": "00bd18d0",
      "incomplete_value": false,
      "site": "00bd18d4",
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
      "definition_site": "00bd1d08",
      "incomplete_value": true,
      "site": "00bd1d14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd18e0",
      "incomplete_value": true,
      "site": "00bd18ec",
      "value": [
        "LOAD",
        "8",
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
      "00bd1cf8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd1d08",
      "DATA",
      [
        "storage",
        "01126538",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1cf8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd1d08",
      "DATA",
      [
        "storage",
        "01126938",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd18d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md#insn-00bd18d4) · [`00bd18d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md#insn-00bd18d0) · [`00bd18dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md#insn-00bd18dc)
- 新版 `00bd1cfc`（命令位置の公開資料なし） · `00bd1cf8`（命令位置の公開資料なし） · `00bd1d04`（命令位置の公開資料なし）

~~~diff
- 00bd18d4 ["INT_ADD", "register:40f0:8", ["const:bd18d4:8", "const:4:8"]]
- 00bd18d4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd1cfc ["INT_ADD", "register:40f0:8", ["const:bd1cfc:8", "const:4:8"]]
+ 00bd1cfc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd18d4 bytes cb240294
+ 00bd1cfc bytes c1240294
- 00bd18d0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd18d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd18d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd18d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1cf8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd1cf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1cf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1cf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd18d0 bytes 00680a91
+ 00bd1cf8 bytes 009c0d91
- 00bd18dc ["COPY", "tmp:0:8", ["const:538:8"]]
- 00bd18dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd18dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd18dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d04 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00bd1d04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd18dc bytes 08e11491
+ 00bd1d04 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1e901fbb67c23b03050fb40c8ed7e7c"></a>

### [`00bd18f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18f0.md) → [`00bd1d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1d18.md) _ZN8firebase4auth29invalid_credentials_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1d58",
      "incomplete_value": true,
      "site": "00bd1d58",
      "value": [
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
    "old": {
      "definition_site": "00bd1930",
      "incomplete_value": true,
      "site": "00bd1930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00bd1d34",
      "incomplete_value": true,
      "site": "00bd1d34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd190c",
      "incomplete_value": true,
      "site": "00bd190c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1d3c",
      "incomplete_value": false,
      "site": "00bd1d50",
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
            "const:c8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1914",
      "incomplete_value": false,
      "site": "00bd1928",
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
            "const:c4e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1d2c",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1d3c",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1d58",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d2c",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1d3c",
      "PARAM",
      [
        "storage",
        "002b9c8e",
        null,
        "string"
      ]
    ],
    [
      "00bd1d58",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18f0.md#insn-00bd1928) · [`00bd1930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18f0.md#insn-00bd1930) · [`00bd1904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18f0.md#insn-00bd1904)
- 新版 `00bd1d50`（命令位置の公開資料なし） · `00bd1d58`（命令位置の公開資料なし） · `00bd1d2c`（命令位置の公開資料なし）

~~~diff
- 00bd1928 ["INT_ADD", "register:40f0:8", ["const:bd1928:8", "const:4:8"]]
- 00bd1928 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1d50 ["INT_ADD", "register:40f0:8", ["const:bd1d50:8", "const:4:8"]]
+ 00bd1d50 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1928 bytes 7a240294
+ 00bd1d50 bytes 70240294
- 00bd1930 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:528:8"]]
- 00bd1930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1d58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00bd1d58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1930 bytes 809602f9
+ 00bd1d58 bytes 809604f9
- 00bd1904 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:528:8"]]
- 00bd1904 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00bd1d2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1904 bytes 819642f9
+ 00bd1d2c bytes 819644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236a8d3d1729727e6140c7f5c901d2a2"></a>

### [`00bd199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd199c.md) → [`00bd1dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1dc4.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00bd1df0",
      "incomplete_value": true,
      "site": "00bd1df0",
      "value": [
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
      "definition_site": "00bd19c8",
      "incomplete_value": true,
      "site": "00bd19c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1dd8",
      "incomplete_value": true,
      "site": "00bd1dd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19b0",
      "incomplete_value": true,
      "site": "00bd19b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1de4",
      "incomplete_value": false,
      "site": "00bd1de8",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19bc",
      "incomplete_value": false,
      "site": "00bd19c0",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1dd4",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1de4",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1df0",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1dd4",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1de4",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd1df0",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd19c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd199c.md#insn-00bd19c0) · [`00bd19c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd199c.md#insn-00bd19c8) · [`00bd19ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd199c.md#insn-00bd19ac)
- 新版 `00bd1de8`（命令位置の公開資料なし） · `00bd1df0`（命令位置の公開資料なし） · `00bd1dd4`（命令位置の公開資料なし）

~~~diff
- 00bd19c0 ["INT_ADD", "register:40f0:8", ["const:bd19c0:8", "const:4:8"]]
- 00bd19c0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1de8 ["INT_ADD", "register:40f0:8", ["const:bd1de8:8", "const:4:8"]]
+ 00bd1de8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd19c0 bytes 54240294
+ 00bd1de8 bytes 4a240294
- 00bd19c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd19c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1df0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd19c8 bytes 60a602f9
+ 00bd1df0 bytes 60a604f9
- 00bd19ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd19ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1dd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd19ac bytes 68a642f9
+ 00bd1dd4 bytes 68a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65312402ff6f952671fb2f5f6e3dd4af"></a>

### [`00bd19dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd19dc.md) → [`00bd1e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1e04.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00bd1e30",
      "incomplete_value": true,
      "site": "00bd1e30",
      "value": [
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
      "definition_site": "00bd1a08",
      "incomplete_value": true,
      "site": "00bd1a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1e18",
      "incomplete_value": true,
      "site": "00bd1e18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19f0",
      "incomplete_value": true,
      "site": "00bd19f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1e20",
      "incomplete_value": false,
      "site": "00bd1e28",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19f8",
      "incomplete_value": false,
      "site": "00bd1a00",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1e14",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e20",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1e30",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e14",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e20",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd1e30",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd19dc.md#insn-00bd1a00) · [`00bd1a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd19dc.md#insn-00bd1a08) · [`00bd19ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd19dc.md#insn-00bd19ec)
- 新版 `00bd1e28`（命令位置の公開資料なし） · `00bd1e30`（命令位置の公開資料なし） · `00bd1e14`（命令位置の公開資料なし）

~~~diff
- 00bd1a00 ["INT_ADD", "register:40f0:8", ["const:bd1a00:8", "const:4:8"]]
- 00bd1a00 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1e28 ["INT_ADD", "register:40f0:8", ["const:bd1e28:8", "const:4:8"]]
+ 00bd1e28 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1a00 bytes 44240294
+ 00bd1e28 bytes 3a240294
- 00bd1a08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd1a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1e30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1e30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1a08 bytes 60a602f9
+ 00bd1e30 bytes 60a604f9
- 00bd19ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd19ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd19ec bytes 68a642f9
+ 00bd1e14 bytes 68a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1671aecdedbacaa79aa0515b9dd33ef"></a>

### [`00bd1a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a1c.md) → [`00bd1e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1e44.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd1e74",
      "incomplete_value": true,
      "site": "00bd1e74",
      "value": [
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
      "definition_site": "00bd1a4c",
      "incomplete_value": true,
      "site": "00bd1a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1e58",
      "incomplete_value": true,
      "site": "00bd1e58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1a30",
      "incomplete_value": true,
      "site": "00bd1a30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1e64",
      "incomplete_value": false,
      "site": "00bd1e6c",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1a3c",
      "incomplete_value": false,
      "site": "00bd1a44",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1e54",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e64",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1e74",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e54",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e64",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd1e74",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a1c.md#insn-00bd1a44) · [`00bd1a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a1c.md#insn-00bd1a4c) · [`00bd1a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a1c.md#insn-00bd1a2c)
- 新版 `00bd1e6c`（命令位置の公開資料なし） · `00bd1e74`（命令位置の公開資料なし） · `00bd1e54`（命令位置の公開資料なし）

~~~diff
- 00bd1a44 ["INT_ADD", "register:40f0:8", ["const:bd1a44:8", "const:4:8"]]
- 00bd1a44 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1e6c ["INT_ADD", "register:40f0:8", ["const:bd1e6c:8", "const:4:8"]]
+ 00bd1e6c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1a44 bytes 33240294
+ 00bd1e6c bytes 29240294
- 00bd1a4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd1a4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1e74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1a4c bytes 60a602f9
+ 00bd1e74 bytes 60a604f9
- 00bd1a2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd1a2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1e54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1e54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1a2c bytes 68a642f9
+ 00bd1e54 bytes 68a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13e777a54680afffe0d5a7b55c2cb379"></a>

### [`00bd1a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a60.md) → [`00bd1e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1e88.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1eb8",
      "incomplete_value": true,
      "site": "00bd1eb8",
      "value": [
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
      "definition_site": "00bd1a90",
      "incomplete_value": true,
      "site": "00bd1a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1e9c",
      "incomplete_value": true,
      "site": "00bd1e9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1a74",
      "incomplete_value": true,
      "site": "00bd1a74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1ea4",
      "incomplete_value": false,
      "site": "00bd1eb0",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1a7c",
      "incomplete_value": false,
      "site": "00bd1a88",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1e98",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ea4",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1eb8",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e98",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ea4",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd1eb8",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a60.md#insn-00bd1a88) · [`00bd1a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a60.md#insn-00bd1a90) · [`00bd1a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a60.md#insn-00bd1a70)
- 新版 `00bd1eb0`（命令位置の公開資料なし） · `00bd1eb8`（命令位置の公開資料なし） · `00bd1e98`（命令位置の公開資料なし）

~~~diff
- 00bd1a88 ["INT_ADD", "register:40f0:8", ["const:bd1a88:8", "const:4:8"]]
- 00bd1a88 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1eb0 ["INT_ADD", "register:40f0:8", ["const:bd1eb0:8", "const:4:8"]]
+ 00bd1eb0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1a88 bytes 22240294
+ 00bd1eb0 bytes 18240294
- 00bd1a90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd1a90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1a90 bytes 60a602f9
+ 00bd1eb8 bytes 60a604f9
- 00bd1a70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00bd1a70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
+ 00bd1e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1a70 bytes 68a642f9
+ 00bd1e98 bytes 68a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52175166ec4e65290ba1cf29a6bbf2c6"></a>

### [`00bd1ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ab0.md) → [`00bd1ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ed8.md) _ZN8firebase4auth22invalid_user_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bd1b08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1f30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1f0c",
      "incomplete_value": true,
      "site": "00bd1f18",
      "value": [
        "LOAD",
        "8",
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1ae4",
      "incomplete_value": true,
      "site": "00bd1af0",
      "value": [
        "LOAD",
        "8",
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
                "const:548:8"
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
      "00bd1eec",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd1ae4",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1b08",
      "WRITE",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1eec",
      "READ",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1f0c",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1f30",
      "WRITE",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ab0.md#insn-00bd1af0) · [`00bd1b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ab0.md#insn-00bd1b08)
- 新版 `00bd1f18`（命令位置の公開資料なし） · `00bd1f30`（命令位置の公開資料なし）

~~~diff
- 00bd1af0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1af0 ["INT_ADD", "register:40f0:8", ["const:bd1af0:8", "const:4:8"]]
- 00bd1af0 ["CALLIND", null, ["register:0:8"]]
+ 00bd1f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1f18 ["INT_ADD", "register:40f0:8", ["const:bd1f18:8", "const:4:8"]]
+ 00bd1f18 ["CALLIND", null, ["register:0:8"]]
- 00bd1af0 bytes 00013fd6
+ 00bd1f18 bytes 00013fd6
- 00bd1b08 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1b08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:550:8"]]
- 00bd1b08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1b08 bytes a0421539
+ 00bd1f30 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1f30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:950:8"]]
+ 00bd1f30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1f30 bytes a0422539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d585efe2fac540980524e3396f57295"></a>

### [`00bd1b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b1c.md) → [`00bd1f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1f44.md) _ZN8firebase4auth22invalid_user_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "definition_site": "00bd1f80",
      "incomplete_value": true,
      "site": "00bd1f80",
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
      "definition_site": "00bd1b58",
      "incomplete_value": true,
      "site": "00bd1b58",
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
            "const:550:8"
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
      "definition_site": "00bd1fa0",
      "incomplete_value": true,
      "site": "00bd1fa0",
      "value": [
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
      "definition_site": "00bd1b78",
      "incomplete_value": true,
      "site": "00bd1b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1f5c",
      "incomplete_value": true,
      "site": "00bd1f5c",
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
      "definition_site": "00bd1b34",
      "incomplete_value": true,
      "site": "00bd1b34",
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
      "00bd1f58",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1f64",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1f80",
      "WRITE",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f58",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1f64",
      "READ",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1f80",
      "WRITE",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b1c.md#insn-00bd1b58) · [`00bd1b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b1c.md#insn-00bd1b74) · [`00bd1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b1c.md#insn-00bd1b78)
- 新版 `00bd1f80`（命令位置の公開資料なし） · `00bd1f9c`（命令位置の公開資料なし） · `00bd1fa0`（命令位置の公開資料なし）

~~~diff
- 00bd1b58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd1b58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd1b58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:550:8"]]
- 00bd1b58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd1f80 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd1f80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd1f80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:950:8"]]
+ 00bd1f80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd1b58 bytes bf421539
+ 00bd1f80 bytes bf422539
- 00bd1b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1b74 ["INT_ADD", "register:40f0:8", ["const:bd1b74:8", "const:4:8"]]
- 00bd1b74 ["CALLIND", null, ["register:0:8"]]
+ 00bd1f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1f9c ["INT_ADD", "register:40f0:8", ["const:bd1f9c:8", "const:4:8"]]
+ 00bd1f9c ["CALLIND", null, ["register:0:8"]]
- 00bd1b74 bytes 00013fd6
+ 00bd1f9c bytes 00013fd6
- 00bd1b78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00bd1b78 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd1b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd1fa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00bd1fa0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd1fa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd1b78 bytes 9fa602f9
+ 00bd1fa0 bytes 9fa604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a9bc25d15f0bf721e82ff4c7cb8ae3"></a>

### [`00bd1b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b8c.md) → [`00bd1fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1fb4.md) _ZN8firebase4auth22invalid_user_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd1ff4",
      "incomplete_value": true,
      "site": "00bd1ff4",
      "value": [
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
      "definition_site": "00bd1bcc",
      "incomplete_value": true,
      "site": "00bd1bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd1fd0",
      "incomplete_value": true,
      "site": "00bd1fd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1ba8",
      "incomplete_value": true,
      "site": "00bd1ba8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd1fd8",
      "incomplete_value": false,
      "site": "00bd1fec",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1bb0",
      "incomplete_value": false,
      "site": "00bd1bc4",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1fc8",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1fd8",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1ff4",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1fc8",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1fd8",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd1ff4",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b8c.md#insn-00bd1bc4) · [`00bd1bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b8c.md#insn-00bd1bcc) · [`00bd1ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b8c.md#insn-00bd1ba0)
- 新版 `00bd1fec`（命令位置の公開資料なし） · `00bd1ff4`（命令位置の公開資料なし） · `00bd1fc8`（命令位置の公開資料なし）

~~~diff
- 00bd1bc4 ["INT_ADD", "register:40f0:8", ["const:bd1bc4:8", "const:4:8"]]
- 00bd1bc4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd1fec ["INT_ADD", "register:40f0:8", ["const:bd1fec:8", "const:4:8"]]
+ 00bd1fec ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1bc4 bytes d3230294
+ 00bd1fec bytes c9230294
- 00bd1bcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00bd1bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1ff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00bd1ff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1bcc bytes 80a602f9
+ 00bd1ff4 bytes 80a604f9
- 00bd1ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00bd1ba0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd1fc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00bd1fc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1ba0 bytes 81a642f9
+ 00bd1fc8 bytes 81a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7656b9940d8e58aa591bedc9c7c8dc10"></a>

### [`00bd1bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1bfc.md) → [`00bd2024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2024.md) _ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd2040",
      "incomplete_value": false,
      "site": "00bd2044",
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
      "definition_site": "00bd1c18",
      "incomplete_value": false,
      "site": "00bd1c1c",
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
      "definition_site": "00bd2050",
      "incomplete_value": true,
      "site": "00bd205c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd1c28",
      "incomplete_value": true,
      "site": "00bd1c34",
      "value": [
        "LOAD",
        "8",
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
      "00bd2040",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd2050",
      "DATA",
      [
        "storage",
        "01126558",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2040",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd2050",
      "DATA",
      [
        "storage",
        "01126958",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1bfc.md#insn-00bd1c1c) · [`00bd1c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1bfc.md#insn-00bd1c18) · [`00bd1c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1bfc.md#insn-00bd1c24)
- 新版 `00bd2044`（命令位置の公開資料なし） · `00bd2040`（命令位置の公開資料なし） · `00bd204c`（命令位置の公開資料なし）

~~~diff
- 00bd1c1c ["INT_ADD", "register:40f0:8", ["const:bd1c1c:8", "const:4:8"]]
- 00bd1c1c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2044 ["INT_ADD", "register:40f0:8", ["const:bd2044:8", "const:4:8"]]
+ 00bd2044 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1c1c bytes f9230294
+ 00bd2044 bytes ef230294
- 00bd1c18 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd1c18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1c18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd1c18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2040 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd2040 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2040 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2040 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd1c18 bytes 00680a91
+ 00bd2040 bytes 009c0d91
- 00bd1c24 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00bd1c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd204c ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bd204c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd204c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd204c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1c24 bytes 08611591
+ 00bd204c bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570a3d246f09f8b56c5d893f74f8ec07"></a>

### [`00bd1c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1c38.md) → [`00bd2060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2060.md) _ZN8firebase4auth22invalid_user_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd20a0",
      "incomplete_value": true,
      "site": "00bd20a0",
      "value": [
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
      "definition_site": "00bd1c78",
      "incomplete_value": true,
      "site": "00bd1c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "definition_site": "00bd207c",
      "incomplete_value": true,
      "site": "00bd207c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1c54",
      "incomplete_value": true,
      "site": "00bd1c54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2084",
      "incomplete_value": false,
      "site": "00bd2098",
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
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1c5c",
      "incomplete_value": false,
      "site": "00bd1c70",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2074",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2084",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd20a0",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2074",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2084",
      "PARAM",
      [
        "storage",
        "002a1cbc",
        null,
        "string"
      ]
    ],
    [
      "00bd20a0",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1c38.md#insn-00bd1c70) · [`00bd1c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1c38.md#insn-00bd1c78) · [`00bd1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1c38.md#insn-00bd1c4c)
- 新版 `00bd2098`（命令位置の公開資料なし） · `00bd20a0`（命令位置の公開資料なし） · `00bd2074`（命令位置の公開資料なし）

~~~diff
- 00bd1c70 ["INT_ADD", "register:40f0:8", ["const:bd1c70:8", "const:4:8"]]
- 00bd1c70 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2098 ["INT_ADD", "register:40f0:8", ["const:bd2098:8", "const:4:8"]]
+ 00bd2098 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1c70 bytes a8230294
+ 00bd2098 bytes 9e230294
- 00bd1c78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00bd1c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd20a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00bd20a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1c78 bytes 80a602f9
+ 00bd20a0 bytes 80a604f9
- 00bd1c4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00bd1c4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
+ 00bd2074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1c4c bytes 81a642f9
+ 00bd2074 bytes 81a644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8e81b00ddadb9c028545c3eea2d83d5"></a>

### [`00bd1ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ce4.md) → [`00bd210c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd210c.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bd2138",
      "incomplete_value": true,
      "site": "00bd2138",
      "value": [
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
      "definition_site": "00bd1d10",
      "incomplete_value": true,
      "site": "00bd1d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "definition_site": "00bd2120",
      "incomplete_value": true,
      "site": "00bd2120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1cf8",
      "incomplete_value": true,
      "site": "00bd1cf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd212c",
      "incomplete_value": false,
      "site": "00bd2130",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1d04",
      "incomplete_value": false,
      "site": "00bd1d08",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd211c",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd212c",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd2138",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd211c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd212c",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ],
    [
      "00bd2138",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ce4.md#insn-00bd1d08) · [`00bd1d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ce4.md#insn-00bd1d10) · [`00bd1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ce4.md#insn-00bd1cf4)
- 新版 `00bd2130`（命令位置の公開資料なし） · `00bd2138`（命令位置の公開資料なし） · `00bd211c`（命令位置の公開資料なし）

~~~diff
- 00bd1d08 ["INT_ADD", "register:40f0:8", ["const:bd1d08:8", "const:4:8"]]
- 00bd1d08 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2130 ["INT_ADD", "register:40f0:8", ["const:bd2130:8", "const:4:8"]]
+ 00bd2130 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1d08 bytes 82230294
+ 00bd2130 bytes 78230294
- 00bd1d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd2138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1d10 bytes 60b602f9
+ 00bd2138 bytes 60b604f9
- 00bd1cf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd211c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd211c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1cf4 bytes 68b642f9
+ 00bd211c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-150afc762021298d4e517a29248b93ea"></a>

### [`00bd1d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d64.md) → [`00bd218c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd218c.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd21bc",
      "incomplete_value": true,
      "site": "00bd21bc",
      "value": [
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
      "definition_site": "00bd1d94",
      "incomplete_value": true,
      "site": "00bd1d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "definition_site": "00bd21a0",
      "incomplete_value": true,
      "site": "00bd21a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1d78",
      "incomplete_value": true,
      "site": "00bd1d78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd21ac",
      "incomplete_value": false,
      "site": "00bd21b4",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1d84",
      "incomplete_value": false,
      "site": "00bd1d8c",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd219c",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21ac",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd21bc",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd219c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21ac",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ],
    [
      "00bd21bc",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d64.md#insn-00bd1d8c) · [`00bd1d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d64.md#insn-00bd1d94) · [`00bd1d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d64.md#insn-00bd1d74)
- 新版 `00bd21b4`（命令位置の公開資料なし） · `00bd21bc`（命令位置の公開資料なし） · `00bd219c`（命令位置の公開資料なし）

~~~diff
- 00bd1d8c ["INT_ADD", "register:40f0:8", ["const:bd1d8c:8", "const:4:8"]]
- 00bd1d8c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd21b4 ["INT_ADD", "register:40f0:8", ["const:bd21b4:8", "const:4:8"]]
+ 00bd21b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1d8c bytes 61230294
+ 00bd21b4 bytes 57230294
- 00bd1d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd21bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd21bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1d94 bytes 60b602f9
+ 00bd21bc bytes 60b604f9
- 00bd1d74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd219c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd219c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1d74 bytes 68b642f9
+ 00bd219c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5684cf3757a87e91aeb8cbd016bd4926"></a>

### [`00bd1da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1da8.md) → [`00bd21d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd21d0.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd2200",
      "incomplete_value": true,
      "site": "00bd2200",
      "value": [
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
      "definition_site": "00bd1dd8",
      "incomplete_value": true,
      "site": "00bd1dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "definition_site": "00bd21e4",
      "incomplete_value": true,
      "site": "00bd21e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1dbc",
      "incomplete_value": true,
      "site": "00bd1dbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd21ec",
      "incomplete_value": false,
      "site": "00bd21f8",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1dc4",
      "incomplete_value": false,
      "site": "00bd1dd0",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd21e0",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21ec",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd2200",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd21e0",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21ec",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ],
    [
      "00bd2200",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1da8.md#insn-00bd1dd0) · [`00bd1dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1da8.md#insn-00bd1dd8) · [`00bd1db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1da8.md#insn-00bd1db8)
- 新版 `00bd21f8`（命令位置の公開資料なし） · `00bd2200`（命令位置の公開資料なし） · `00bd21e0`（命令位置の公開資料なし）

~~~diff
- 00bd1dd0 ["INT_ADD", "register:40f0:8", ["const:bd1dd0:8", "const:4:8"]]
- 00bd1dd0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd21f8 ["INT_ADD", "register:40f0:8", ["const:bd21f8:8", "const:4:8"]]
+ 00bd21f8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1dd0 bytes 50230294
+ 00bd21f8 bytes 46230294
- 00bd1dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd2200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1dd8 bytes 60b602f9
+ 00bd2200 bytes 60b604f9
- 00bd1db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd21e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00bd21e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1db8 bytes 68b642f9
+ 00bd21e0 bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3cd7432470b67459c2b75f49c19520"></a>

### [`00bd1df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1df8.md) → [`00bd2220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2220.md) _ZN8firebase4auth31recent_login_required_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "00bd1e50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2278"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2254",
      "incomplete_value": true,
      "site": "00bd2260",
      "value": [
        "LOAD",
        "8",
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
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1e2c",
      "incomplete_value": true,
      "site": "00bd1e38",
      "value": [
        "LOAD",
        "8",
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
                "const:568:8"
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
      "00bd2234",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd1e2c",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1e50",
      "WRITE",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2234",
      "READ",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2254",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2278",
      "WRITE",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1df8.md#insn-00bd1e38) · [`00bd1e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1df8.md#insn-00bd1e50)
- 新版 `00bd2260`（命令位置の公開資料なし） · `00bd2278`（命令位置の公開資料なし）

~~~diff
- 00bd1e38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1e38 ["INT_ADD", "register:40f0:8", ["const:bd1e38:8", "const:4:8"]]
- 00bd1e38 ["CALLIND", null, ["register:0:8"]]
+ 00bd2260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2260 ["INT_ADD", "register:40f0:8", ["const:bd2260:8", "const:4:8"]]
+ 00bd2260 ["CALLIND", null, ["register:0:8"]]
- 00bd1e38 bytes 00013fd6
+ 00bd2260 bytes 00013fd6
- 00bd1e50 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1e50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:570:8"]]
- 00bd1e50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1e50 bytes a0c21539
+ 00bd2278 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2278 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
+ 00bd2278 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2278 bytes a0c22539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b50aafcf46e7df535991abca6131b29c"></a>

### [`00bd1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1e64.md) → [`00bd228c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd228c.md) _ZN8firebase4auth31recent_login_required_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 39.29% / 新版 39.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1e6c",
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
      "00bd228c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd2290",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd2294",
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

- 旧版 [`00bd1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1e64.md#insn-00bd1e64) · [`00bd1e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1e64.md#insn-00bd1e68) · [`00bd1e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1e64.md#insn-00bd1e6c)

~~~diff
- 00bd1e64 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd1e64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd1e64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd1e64 bytes f50f1df8
- 00bd1e68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd1e68 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd1e68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd1e68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1e68 bytes f44f01a9
- 00bd1e6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd1e6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd1e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd1e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1e6c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f05c52a4d99e7e5bd6f73d896535a66"></a>

### [`00bd1ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ed4.md) → [`00bd22fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd22fc.md) _ZN8firebase4auth31recent_login_required_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd1f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd233c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1ee8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2340"
      ]
    ],
    [
      "unmatched:00bd1ef8",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2310",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2340"
      ]
    ],
    [
      "00bd2320",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ed4.md#insn-00bd1ef0) · [`00bd1f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ed4.md#insn-00bd1f0c) · [`00bd1f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ed4.md#insn-00bd1f14)
- 新版 `00bd2334`（命令位置の公開資料なし）

~~~diff
- 00bd1ef0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd1ef0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd1ef0 bytes 410100b5
- 00bd1f0c ["INT_ADD", "register:40f0:8", ["const:bd1f0c:8", "const:4:8"]]
- 00bd1f0c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2334 ["INT_ADD", "register:40f0:8", ["const:bd2334:8", "const:4:8"]]
+ 00bd2334 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1f0c bytes 01230294
+ 00bd2334 bytes f7220294
- 00bd1f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
- 00bd1f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1f14 bytes 80b602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18ca51fb13e9c493482917f8090f3414"></a>

### [`00bd1f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f80.md) → [`00bd23a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd23a8.md) _ZN8firebase4auth31recent_login_required_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd23e8",
      "incomplete_value": true,
      "site": "00bd23e8",
      "value": [
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
      "definition_site": "00bd1fc0",
      "incomplete_value": true,
      "site": "00bd1fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "definition_site": "00bd23c4",
      "incomplete_value": true,
      "site": "00bd23c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1f9c",
      "incomplete_value": true,
      "site": "00bd1f9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd23cc",
      "incomplete_value": false,
      "site": "00bd23e0",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1fa4",
      "incomplete_value": false,
      "site": "00bd1fb8",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd23bc",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd23cc",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd23e8",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd23bc",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd23cc",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ],
    [
      "00bd23e8",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f80.md#insn-00bd1fb8) · [`00bd1fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f80.md#insn-00bd1fc0) · [`00bd1f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f80.md#insn-00bd1f94)
- 新版 `00bd23e0`（命令位置の公開資料なし） · `00bd23e8`（命令位置の公開資料なし） · `00bd23bc`（命令位置の公開資料なし）

~~~diff
- 00bd1fb8 ["INT_ADD", "register:40f0:8", ["const:bd1fb8:8", "const:4:8"]]
- 00bd1fb8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd23e0 ["INT_ADD", "register:40f0:8", ["const:bd23e0:8", "const:4:8"]]
+ 00bd23e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1fb8 bytes d6220294
+ 00bd23e0 bytes cc220294
- 00bd1fc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
- 00bd1fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd23e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00bd23e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1fc0 bytes 80b602f9
+ 00bd23e8 bytes 80b604f9
- 00bd1f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
- 00bd1f94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd23bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00bd23bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd1f94 bytes 81b642f9
+ 00bd23bc bytes 81b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef13a816b7f3038296dcebb28f2bc026"></a>

### [`00bd1ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ff0.md) → [`00bd2418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2418.md) _ZN8firebase4auth31recent_login_required_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd2434",
      "incomplete_value": false,
      "site": "00bd2438",
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
      "definition_site": "00bd200c",
      "incomplete_value": false,
      "site": "00bd2010",
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
      "definition_site": "00bd2444",
      "incomplete_value": true,
      "site": "00bd2450",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd201c",
      "incomplete_value": true,
      "site": "00bd2028",
      "value": [
        "LOAD",
        "8",
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
      "00bd2434",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd2444",
      "DATA",
      [
        "storage",
        "01126580",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2434",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd2444",
      "DATA",
      [
        "storage",
        "01126980",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ff0.md#insn-00bd2010) · [`00bd200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ff0.md#insn-00bd200c) · [`00bd2018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ff0.md#insn-00bd2018)
- 新版 `00bd2438`（命令位置の公開資料なし） · `00bd2434`（命令位置の公開資料なし） · `00bd2440`（命令位置の公開資料なし）

~~~diff
- 00bd2010 ["INT_ADD", "register:40f0:8", ["const:bd2010:8", "const:4:8"]]
- 00bd2010 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2438 ["INT_ADD", "register:40f0:8", ["const:bd2438:8", "const:4:8"]]
+ 00bd2438 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd2010 bytes fc220294
+ 00bd2438 bytes f2220294
- 00bd200c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd200c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd200c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd200c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2434 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd2434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd200c bytes 00441191
+ 00bd2434 bytes 00781491
- 00bd2018 ["COPY", "tmp:0:8", ["const:580:8"]]
- 00bd2018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2440 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00bd2440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2018 bytes 08011691
+ 00bd2440 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a7fcf1d7b87b38491989d39c21aeb8"></a>

### [`00bd202c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd202c.md) → [`00bd2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2454.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

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
      "definition_site": "00bd2480",
      "incomplete_value": true,
      "site": "00bd2480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2058",
      "incomplete_value": true,
      "site": "00bd2058",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2468",
      "incomplete_value": true,
      "site": "00bd2468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2040",
      "incomplete_value": true,
      "site": "00bd2040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2474",
      "incomplete_value": false,
      "site": "00bd2478",
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
            "const:cf7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd204c",
      "incomplete_value": false,
      "site": "00bd2050",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2464",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2474",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2480",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2464",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2474",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ],
    [
      "00bd2480",
      "WRITE",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd202c.md#insn-00bd2050) · [`00bd2058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd202c.md#insn-00bd2058) · [`00bd203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd202c.md#insn-00bd203c)
- 新版 `00bd2478`（命令位置の公開資料なし） · `00bd2480`（命令位置の公開資料なし） · `00bd2464`（命令位置の公開資料なし）

~~~diff
- 00bd2050 ["INT_ADD", "register:40f0:8", ["const:bd2050:8", "const:4:8"]]
- 00bd2050 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2478 ["INT_ADD", "register:40f0:8", ["const:bd2478:8", "const:4:8"]]
+ 00bd2478 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2050 bytes b0220294
+ 00bd2478 bytes a6220294
- 00bd2058 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
- 00bd2058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00bd2480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2058 bytes 60c602f9
+ 00bd2480 bytes 60c604f9
- 00bd203c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
- 00bd203c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00bd2464 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd203c bytes 68c642f9
+ 00bd2464 bytes 68c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8240d7333a8723caf0b647a8cc7a2dc"></a>

### [`00bd206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd206c.md) → [`00bd2494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2494.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd2098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd24c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd24a8",
      "incomplete_value": true,
      "site": "00bd24a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd24a4",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd2088",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd2090",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd24a4",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd24b0",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ],
    [
      "00bd24b8",
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

- 旧版 [`00bd2080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd206c.md#insn-00bd2080) · [`00bd2090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd206c.md#insn-00bd2090) · [`00bd2098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd206c.md#insn-00bd2098)
- 新版 `00bd24a8`（命令位置の公開資料なし）

~~~diff
- 00bd2080 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd2080 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd24a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd24a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd2080 bytes e80000b5
+ 00bd24a8 bytes e80000b5
- 00bd2090 ["INT_ADD", "register:40f0:8", ["const:bd2090:8", "const:4:8"]]
- 00bd2090 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2090 bytes a0220294
- 00bd2098 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
- 00bd2098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2098 bytes 60c602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-677afbf825443077a0e9b7de46f465d5"></a>

### [`00bd20f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20f0.md) → [`00bd2518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2518.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd2120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2548"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd252c",
      "incomplete_value": true,
      "site": "00bd252c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd2528",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd210c",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd2120",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2528",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2534",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ],
    [
      "00bd2548",
      "WRITE",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20f0.md#insn-00bd2104) · [`00bd2118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20f0.md#insn-00bd2118) · [`00bd2120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20f0.md#insn-00bd2120)
- 新版 `00bd252c`（命令位置の公開資料なし） · `00bd2540`（命令位置の公開資料なし）

~~~diff
- 00bd2104 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd2104 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd252c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd252c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd2104 bytes 080100b5
+ 00bd252c bytes 080100b5
- 00bd2118 ["INT_ADD", "register:40f0:8", ["const:bd2118:8", "const:4:8"]]
- 00bd2118 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2540 ["INT_ADD", "register:40f0:8", ["const:bd2540:8", "const:4:8"]]
+ 00bd2540 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2118 bytes 7e220294
+ 00bd2540 bytes 74220294
- 00bd2120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
- 00bd2120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2120 bytes 60c602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8325189cb97fc2639c3b2cfa59ec8ea"></a>

### [`00bd2140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2140.md) → [`00bd2568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2568.md) _ZN8firebase4auth24user_collision_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd25c0",
      "incomplete_value": true,
      "site": "00bd25c0",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2198",
      "incomplete_value": true,
      "site": "00bd2198",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd259c",
      "incomplete_value": true,
      "site": "00bd25a8",
      "value": [
        "LOAD",
        "8",
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd2188",
      "incomplete_value": true,
      "site": "00bd218c",
      "value": [
        "live",
        "register:4098:8"
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
      "00bd257c",
      "READ",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd259c",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd25c0",
      "WRITE",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd257c",
      "READ",
      [
        "storage",
        "01126990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd259c",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd25c0",
      "WRITE",
      [
        "storage",
        "01126990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2140.md#insn-00bd2180) · [`00bd218c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2140.md#insn-00bd218c) · [`00bd2198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2140.md#insn-00bd2198)
- 新版 `00bd25a8`（命令位置の公開資料なし） · `00bd25b4`（命令位置の公開資料なし） · `00bd25c0`（命令位置の公開資料なし）

~~~diff
- 00bd2180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2180 ["INT_ADD", "register:40f0:8", ["const:bd2180:8", "const:4:8"]]
- 00bd2180 ["CALLIND", null, ["register:0:8"]]
+ 00bd25a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd25a8 ["INT_ADD", "register:40f0:8", ["const:bd25a8:8", "const:4:8"]]
+ 00bd25a8 ["CALLIND", null, ["register:0:8"]]
- 00bd2180 bytes 00013fd6
+ 00bd25a8 bytes 00013fd6
- 00bd218c ["INT_ADD", "register:40f0:8", ["const:bd218c:8", "const:4:8"]]
- 00bd218c ["CALL", null, ["callee:00c5af60:8"]]
+ 00bd25b4 ["INT_ADD", "register:40f0:8", ["const:bd25b4:8", "const:4:8"]]
+ 00bd25b4 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd218c bytes 75220294
+ 00bd25b4 bytes 6b220294
- 00bd2198 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd2198 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:590:8"]]
- 00bd2198 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd25c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd25c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:990:8"]]
+ 00bd25c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd2198 bytes a0421639
+ 00bd25c0 bytes a0422639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecbcd0e49fa0f3b85b265c7adfa0bd70"></a>

### [`00bd21ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd21ac.md) → [`00bd25d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd25d4.md) _ZN8firebase4auth24user_collision_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 66.67% / 新版 57.14%

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
      "site": "00bd21e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd2630",
      "incomplete_value": true,
      "site": "00bd2630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2610"
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
      "00bd25e8",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd25f4",
      "READ",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd21e8",
      "WRITE",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd25e8",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd25f4",
      "READ",
      [
        "storage",
        "01126990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2610",
      "WRITE",
      [
        "storage",
        "01126990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd21c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd21ac.md#insn-00bd21c4) · [`00bd21e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd21ac.md#insn-00bd21e4) · [`00bd21e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd21ac.md#insn-00bd21e8)
- 新版 `00bd25ec`（命令位置の公開資料なし）

~~~diff
- 00bd21c4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd21c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd25ec ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd25ec ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd21c4 bytes 410200b4
+ 00bd25ec bytes 410200b4
- 00bd21e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd21e4 ["INT_ADD", "register:40f0:8", ["const:bd21e4:8", "const:4:8"]]
- 00bd21e4 ["CALLIND", null, ["register:0:8"]]
- 00bd21e4 bytes 00013fd6
- 00bd21e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd21e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd21e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:590:8"]]
- 00bd21e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd21e8 bytes bf421639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c81bea16119ea4052469636d60889e18"></a>

### [`00bd221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd221c.md) → [`00bd2644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2644.md) _ZN8firebase4auth24user_collision_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bd225c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2684"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2230",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd2238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2688"
      ]
    ],
    [
      "unmatched:00bd2240",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2658",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2688"
      ]
    ],
    [
      "00bd2668",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd221c.md#insn-00bd2238) · [`00bd2254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd221c.md#insn-00bd2254) · [`00bd225c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd221c.md#insn-00bd225c)
- 新版 `00bd267c`（命令位置の公開資料なし）

~~~diff
- 00bd2238 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd2238 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd2238 bytes 410100b5
- 00bd2254 ["INT_ADD", "register:40f0:8", ["const:bd2254:8", "const:4:8"]]
- 00bd2254 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd267c ["INT_ADD", "register:40f0:8", ["const:bd267c:8", "const:4:8"]]
+ 00bd267c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2254 bytes 2f220294
+ 00bd267c bytes 25220294
- 00bd225c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
- 00bd225c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd225c bytes 80c602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cdcb283581ed9ad9ae69b035bda4123"></a>

### [`00bd228c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd228c.md) → [`00bd26b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd26b4.md) _ZN8firebase4auth24user_collision_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd26d0",
      "incomplete_value": false,
      "site": "00bd26d4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd26e0",
      "incomplete_value": true,
      "site": "00bd26ec",
      "value": [
        "LOAD",
        "8",
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
      "00bd26d0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd26e0",
      "DATA",
      [
        "storage",
        "01126598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd26d0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd26e0",
      "DATA",
      [
        "storage",
        "01126998",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd22ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd228c.md#insn-00bd22ac) · [`00bd22a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd228c.md#insn-00bd22a8) · [`00bd22b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd228c.md#insn-00bd22b4)
- 新版 `00bd26d4`（命令位置の公開資料なし） · `00bd26d0`（命令位置の公開資料なし） · `00bd26dc`（命令位置の公開資料なし）

~~~diff
- 00bd22ac ["INT_ADD", "register:40f0:8", ["const:bd22ac:8", "const:4:8"]]
- 00bd22ac ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd26d4 ["INT_ADD", "register:40f0:8", ["const:bd26d4:8", "const:4:8"]]
+ 00bd26d4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd22ac bytes 55220294
+ 00bd26d4 bytes 4b220294
- 00bd22a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd22a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd22a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd22a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd26d0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd26d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd26d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd26d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd22a8 bytes 00680a91
+ 00bd26d0 bytes 009c0d91
- 00bd22b4 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bd22b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd22b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd22b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd26dc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00bd26dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd26dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd26dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd22b4 bytes 08611691
+ 00bd26dc bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c9fc7b684c6b423634ce5a9659f12fb"></a>

### [`00bd22c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd22c8.md) → [`00bd26f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd26f0.md) _ZN8firebase4auth24user_collision_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd2730",
      "incomplete_value": true,
      "site": "00bd2730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd270c",
      "incomplete_value": true,
      "site": "00bd270c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2714",
      "incomplete_value": false,
      "site": "00bd2728",
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
            "const:cf7:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2704",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2714",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2730",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2704",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2714",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ],
    [
      "00bd2730",
      "WRITE",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd22c8.md#insn-00bd2300) · [`00bd2308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd22c8.md#insn-00bd2308) · [`00bd22dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd22c8.md#insn-00bd22dc)
- 新版 `00bd2728`（命令位置の公開資料なし） · `00bd2730`（命令位置の公開資料なし） · `00bd2704`（命令位置の公開資料なし）

~~~diff
- 00bd2300 ["INT_ADD", "register:40f0:8", ["const:bd2300:8", "const:4:8"]]
- 00bd2300 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2728 ["INT_ADD", "register:40f0:8", ["const:bd2728:8", "const:4:8"]]
+ 00bd2728 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2300 bytes 04220294
+ 00bd2728 bytes fa210294
- 00bd2308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
- 00bd2308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00bd2730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2308 bytes 80c602f9
+ 00bd2730 bytes 80c604f9
- 00bd22dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
- 00bd22dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2704 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00bd2704 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd22dc bytes 81c642f9
+ 00bd2704 bytes 81c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45ffdf09930bed264029525dc2fe5075"></a>

### [`00bd2338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2338.md) → [`00bd2760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2760.md) _ZN8firebase4auth24user_collision_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd277c",
      "incomplete_value": false,
      "site": "00bd2780",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd278c",
      "incomplete_value": true,
      "site": "00bd2798",
      "value": [
        "LOAD",
        "8",
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
      "00bd277c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd278c",
      "DATA",
      [
        "storage",
        "011265a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd277c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd278c",
      "DATA",
      [
        "storage",
        "011269a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2338.md#insn-00bd2358) · [`00bd2354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2338.md#insn-00bd2354) · [`00bd2360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2338.md#insn-00bd2360)
- 新版 `00bd2780`（命令位置の公開資料なし） · `00bd277c`（命令位置の公開資料なし） · `00bd2788`（命令位置の公開資料なし）

~~~diff
- 00bd2358 ["INT_ADD", "register:40f0:8", ["const:bd2358:8", "const:4:8"]]
- 00bd2358 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2780 ["INT_ADD", "register:40f0:8", ["const:bd2780:8", "const:4:8"]]
+ 00bd2780 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd2358 bytes 2a220294
+ 00bd2780 bytes 20220294
- 00bd2354 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd2354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd277c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd277c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd277c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd277c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd2354 bytes 00441191
+ 00bd277c bytes 00781491
- 00bd2360 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00bd2360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2788 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00bd2788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2360 bytes 08811691
+ 00bd2788 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9aee291d5c012926af7f03cc4886a31"></a>

### [`00bd2374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2374.md) → [`00bd279c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd279c.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd27c8",
      "incomplete_value": true,
      "site": "00bd27c8",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd27b0",
      "incomplete_value": true,
      "site": "00bd27b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd27bc",
      "incomplete_value": false,
      "site": "00bd27c0",
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
            "const:d55:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd27ac",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd27bc",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd27c8",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd27ac",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd27bc",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ],
    [
      "00bd27c8",
      "WRITE",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2374.md#insn-00bd2398) · [`00bd23a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2374.md#insn-00bd23a0) · [`00bd2384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2374.md#insn-00bd2384)
- 新版 `00bd27c0`（命令位置の公開資料なし） · `00bd27c8`（命令位置の公開資料なし） · `00bd27ac`（命令位置の公開資料なし）

~~~diff
- 00bd2398 ["INT_ADD", "register:40f0:8", ["const:bd2398:8", "const:4:8"]]
- 00bd2398 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd27c0 ["INT_ADD", "register:40f0:8", ["const:bd27c0:8", "const:4:8"]]
+ 00bd27c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2398 bytes de210294
+ 00bd27c0 bytes d4210294
- 00bd23a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd23a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd27c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd27c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd23a0 bytes 60d602f9
+ 00bd27c8 bytes 60d604f9
- 00bd2384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd2384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd27ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd27ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2384 bytes 68d642f9
+ 00bd27ac bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1e16d8532ef762a3cf48e91e83ba3b"></a>

### [`00bd23b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23b4.md) → [`00bd27dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd27dc.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "site": "00bd23b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd23b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd23b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd23b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd23b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd27ec",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd27dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd27e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd27ec",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd23b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23b4.md#insn-00bd23b4) · [`00bd23b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23b4.md#insn-00bd23b8) · [`00bd23c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23b4.md#insn-00bd23c8)
- 新版 `00bd27f0`（命令位置の公開資料なし）

~~~diff
- 00bd23b4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd23b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd23b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd23b4 bytes f30f1ef8
- 00bd23b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd23b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd23b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd23b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd23b8 bytes fd7b01a9
- 00bd23c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd23c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd27f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd27f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd23c8 bytes e80000b5
+ 00bd27f0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8bbb03196abc69acd0d5d30ec1dfef"></a>

### [`00bd23f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23f4.md) → [`00bd281c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd281c.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd284c",
      "incomplete_value": true,
      "site": "00bd284c",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2830",
      "incomplete_value": true,
      "site": "00bd2830",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd283c",
      "incomplete_value": false,
      "site": "00bd2844",
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
            "const:d55:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd282c",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd283c",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd284c",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd282c",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd283c",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ],
    [
      "00bd284c",
      "WRITE",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd241c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23f4.md#insn-00bd241c) · [`00bd2424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23f4.md#insn-00bd2424) · [`00bd2404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23f4.md#insn-00bd2404)
- 新版 `00bd2844`（命令位置の公開資料なし） · `00bd284c`（命令位置の公開資料なし） · `00bd282c`（命令位置の公開資料なし）

~~~diff
- 00bd241c ["INT_ADD", "register:40f0:8", ["const:bd241c:8", "const:4:8"]]
- 00bd241c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2844 ["INT_ADD", "register:40f0:8", ["const:bd2844:8", "const:4:8"]]
+ 00bd2844 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd241c bytes bd210294
+ 00bd2844 bytes b3210294
- 00bd2424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd2424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd284c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd284c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2424 bytes 60d602f9
+ 00bd284c bytes 60d604f9
- 00bd2404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd2404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd282c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd282c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2404 bytes 68d642f9
+ 00bd282c bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad6414ae2fe60064474383b95268605e"></a>

### [`00bd2438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2438.md) → [`00bd2860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2860.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd2890",
      "incomplete_value": true,
      "site": "00bd2890",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2874",
      "incomplete_value": true,
      "site": "00bd2874",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd287c",
      "incomplete_value": false,
      "site": "00bd2888",
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
            "const:d55:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2870",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd287c",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd2890",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2870",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd287c",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ],
    [
      "00bd2890",
      "WRITE",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2438.md#insn-00bd2460) · [`00bd2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2438.md#insn-00bd2468) · [`00bd2448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2438.md#insn-00bd2448)
- 新版 `00bd2888`（命令位置の公開資料なし） · `00bd2890`（命令位置の公開資料なし） · `00bd2870`（命令位置の公開資料なし）

~~~diff
- 00bd2460 ["INT_ADD", "register:40f0:8", ["const:bd2460:8", "const:4:8"]]
- 00bd2460 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2888 ["INT_ADD", "register:40f0:8", ["const:bd2888:8", "const:4:8"]]
+ 00bd2888 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2460 bytes ac210294
+ 00bd2888 bytes a2210294
- 00bd2468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd2468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd2890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2468 bytes 60d602f9
+ 00bd2890 bytes 60d604f9
- 00bd2448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00bd2448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00bd2870 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2448 bytes 68d642f9
+ 00bd2870 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

