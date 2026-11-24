# v15.7.4 → v16.0.0 · 最優先の変更候補 (62)

[一覧の目次](README.md)

<a id="compare-7a03ab50dfb5ab66aa1d18ab516746f7"></a>

### [`00b0596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md) → [`00b655c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b655c4.md) _ZN8firebase15options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b6561c",
      "incomplete_value": true,
      "site": "00b6561c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b059c4",
      "incomplete_value": true,
      "site": "00b059c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "definition_site": "00b655f8",
      "incomplete_value": true,
      "site": "00b65604",
      "value": [
        "LOAD",
        "8",
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b059a0",
      "incomplete_value": true,
      "site": "00b059ac",
      "value": [
        "LOAD",
        "8",
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
                "const:df0:8"
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
      "00b655d8",
      "READ",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b655f8",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6561c",
      "WRITE",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b655d8",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b655f8",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6561c",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b059ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b059ac) · [`00b059c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b059c4) · [`00b0597c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b0597c)
- 新版 [`00b65604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b655c4.md#insn-00b65604) · [`00b6561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b655c4.md#insn-00b6561c) · [`00b655d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b655c4.md#insn-00b655d4)

~~~diff
- 00b059ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b059ac ["INT_ADD", "register:40f0:8", ["const:b059ac:8", "const:4:8"]]
- 00b059ac ["CALLIND", null, ["register:0:8"]]
+ 00b65604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65604 ["INT_ADD", "register:40f0:8", ["const:b65604:8", "const:4:8"]]
+ 00b65604 ["CALLIND", null, ["register:0:8"]]
- 00b059ac bytes 00013fd6
+ 00b65604 bytes 00013fd6
- 00b059c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b059c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:df8:8"]]
- 00b059c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6561c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6561c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cb8:8"]]
+ 00b6561c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b059c4 bytes a0e23739
+ 00b6561c bytes a0e23239
- 00b0597c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b655d4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00b0597c bytes d52c00f0
+ 00b655d4 bytes 152e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8ed53a4844287d0782ea31e7e0da32"></a>

### [`00b059d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md) → [`00b65630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65630.md) _ZN8firebase15options_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b6566c",
      "incomplete_value": true,
      "site": "00b6566c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05a14",
      "incomplete_value": true,
      "site": "00b05a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "definition_site": "00b6568c",
      "incomplete_value": true,
      "site": "00b6568c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05a34",
      "incomplete_value": true,
      "site": "00b05a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "definition_site": "00b65648",
      "incomplete_value": true,
      "site": "00b65648",
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
      "definition_site": "00b059f0",
      "incomplete_value": true,
      "site": "00b059f0",
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
      "00b65644",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65650",
      "READ",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6566c",
      "WRITE",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65644",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65650",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6566c",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b05a14) · [`00b05a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b05a30) · [`00b05a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b05a34)
- 新版 [`00b6566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65630.md#insn-00b6566c) · [`00b65688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65630.md#insn-00b65688) · [`00b6568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65630.md#insn-00b6568c)

~~~diff
- 00b05a14 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05a14 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05a14 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:df8:8"]]
- 00b05a14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6566c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6566c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6566c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cb8:8"]]
+ 00b6566c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05a14 bytes bfe23739
+ 00b6566c bytes bfe23239
- 00b05a30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05a30 ["INT_ADD", "register:40f0:8", ["const:b05a30:8", "const:4:8"]]
- 00b05a30 ["CALLIND", null, ["register:0:8"]]
+ 00b65688 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65688 ["INT_ADD", "register:40f0:8", ["const:b65688:8", "const:4:8"]]
+ 00b65688 ["CALLIND", null, ["register:0:8"]]
- 00b05a30 bytes 00013fd6
+ 00b65688 bytes 00013fd6
- 00b05a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00b05a34 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b05a34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6568c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
+ 00b6568c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6568c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b05a34 bytes 9ffa06f9
+ 00b6568c bytes 9f5a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c5cff084b1e08d13f14f7cb79370e4"></a>

### [`00b05a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md) → [`00b656a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b656a0.md) _ZN8firebase15options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b05a88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b656e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05a64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05a5c",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05a64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b656e4"
      ]
    ],
    [
      "unmatched:00b05a6c",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b656b4",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b656e4"
      ]
    ],
    [
      "00b656c4",
      "PARAM",
      [
        "storage",
        "002a2989",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a64) · [`00b05a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a80) · [`00b05a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a88)
- 新版 [`00b656d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b656a0.md#insn-00b656d8)

~~~diff
- 00b05a64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05a64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b05a64 bytes 410100b5
- 00b05a80 ["INT_ADD", "register:40f0:8", ["const:b05a80:8", "const:4:8"]]
- 00b05a80 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b656d8 ["INT_ADD", "register:40f0:8", ["const:b656d8:8", "const:4:8"]]
+ 00b656d8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05a80 bytes 84610394
+ 00b656d8 bytes 0ed50394
- 00b05a88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00b05a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05a88 bytes 80fa06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba46f1b6f655de5a7faa4bf26113c5bf"></a>

### [`00b05ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md) → [`00b65710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65710.md) _ZN8firebase15options_builder11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b6572c",
      "incomplete_value": false,
      "site": "00b65730",
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
      "definition_site": "00b05ad4",
      "incomplete_value": false,
      "site": "00b05ad8",
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
      "definition_site": "00b6573c",
      "incomplete_value": true,
      "site": "00b65748",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b05ae4",
      "incomplete_value": true,
      "site": "00b05af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b6572c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6573c",
      "DATA",
      [
        "storage",
        "010a0e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6572c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b6573c",
      "DATA",
      [
        "storage",
        "01125cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ad8) · [`00b05ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ad0) · [`00b05ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ad4)
- 新版 [`00b65730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65710.md#insn-00b65730) · [`00b65728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65710.md#insn-00b65728) · [`00b6572c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65710.md#insn-00b6572c)

~~~diff
- 00b05ad8 ["INT_ADD", "register:40f0:8", ["const:b05ad8:8", "const:4:8"]]
- 00b05ad8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65730 ["INT_ADD", "register:40f0:8", ["const:b65730:8", "const:4:8"]]
+ 00b65730 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b05ad8 bytes aa610394
+ 00b65730 bytes 34d50394
- 00b05ad0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b65728 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b05ad0 bytes 80bcfff0
+ 00b65728 bytes 00bafff0
- 00b05ad4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b05ad4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05ad4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05ad4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6572c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b6572c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6572c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6572c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05ad4 bytes 001c1591
+ 00b6572c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77401a768a8376f54bb54565521d351f"></a>

### [`00b05af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md) → [`00b6574c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6574c.md) _ZN8firebase15options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b05b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6578c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05b08",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05b10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65790"
      ]
    ],
    [
      "unmatched:00b05b18",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65760",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65768",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65790"
      ]
    ],
    [
      "00b65770",
      "PARAM",
      [
        "storage",
        "002a2989",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b10) · [`00b05b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b2c) · [`00b05b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b34)
- 新版 [`00b65784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6574c.md#insn-00b65784)

~~~diff
- 00b05b10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05b10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b05b10 bytes 410100b5
- 00b05b2c ["INT_ADD", "register:40f0:8", ["const:b05b2c:8", "const:4:8"]]
- 00b05b2c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65784 ["INT_ADD", "register:40f0:8", ["const:b65784:8", "const:4:8"]]
+ 00b65784 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05b2c bytes 59610394
+ 00b65784 bytes e3d40394
- 00b05b34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00b05b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05b34 bytes 80fa06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86057f0ad465452b91b71b49d8b0b1a"></a>

### [`00b05ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md) → [`00b657f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657f8.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65824",
      "incomplete_value": true,
      "site": "00b65824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bcc",
      "incomplete_value": true,
      "site": "00b05bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6580c",
      "incomplete_value": true,
      "site": "00b6580c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bb4",
      "incomplete_value": true,
      "site": "00b05bb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65818",
      "incomplete_value": false,
      "site": "00b6581c",
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
            "const:92b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bc0",
      "incomplete_value": false,
      "site": "00b05bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f8a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65808",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65818",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b65824",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65808",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65818",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ],
    [
      "00b65824",
      "WRITE",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bc4) · [`00b05bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bcc) · [`00b05bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bac)
- 新版 [`00b6581c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657f8.md#insn-00b6581c) · [`00b65824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657f8.md#insn-00b65824) · [`00b65804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657f8.md#insn-00b65804)

~~~diff
- 00b05bc4 ["INT_ADD", "register:40f0:8", ["const:b05bc4:8", "const:4:8"]]
- 00b05bc4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b6581c ["INT_ADD", "register:40f0:8", ["const:b6581c:8", "const:4:8"]]
+ 00b6581c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05bc4 bytes 33610394
+ 00b6581c bytes bdd40394
- 00b05bcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
- 00b05bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d08:8"]]
+ 00b65824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05bcc bytes 602607f9
+ 00b65824 bytes 608606f9
- 00b05bac ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65804 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05bac bytes d32c00f0
+ 00b65804 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e3f5592689b96f46787dc2e0fcd513"></a>

### [`00b05be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md) → [`00b65838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65838.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65864",
      "incomplete_value": true,
      "site": "00b65864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c0c",
      "incomplete_value": true,
      "site": "00b05c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6584c",
      "incomplete_value": true,
      "site": "00b6584c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bf4",
      "incomplete_value": true,
      "site": "00b05bf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65854",
      "incomplete_value": false,
      "site": "00b6585c",
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
            "const:92b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bfc",
      "incomplete_value": false,
      "site": "00b05c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f8a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65848",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65854",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b65864",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65848",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65854",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ],
    [
      "00b65864",
      "WRITE",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05c04) · [`00b05c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05c0c) · [`00b05bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05bec)
- 新版 [`00b6585c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65838.md#insn-00b6585c) · [`00b65864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65838.md#insn-00b65864) · [`00b65844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65838.md#insn-00b65844)

~~~diff
- 00b05c04 ["INT_ADD", "register:40f0:8", ["const:b05c04:8", "const:4:8"]]
- 00b05c04 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b6585c ["INT_ADD", "register:40f0:8", ["const:b6585c:8", "const:4:8"]]
+ 00b6585c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05c04 bytes 23610394
+ 00b6585c bytes add40394
- 00b05c0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
- 00b05c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d08:8"]]
+ 00b65864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05c0c bytes 602607f9
+ 00b65864 bytes 608606f9
- 00b05bec ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65844 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05bec bytes d32c00f0
+ 00b65844 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283ce3b6ea7369a100c62cd1142cbce9"></a>

### [`00b05c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md) → [`00b65878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65878.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b658a8",
      "incomplete_value": true,
      "site": "00b658a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c50",
      "incomplete_value": true,
      "site": "00b05c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6588c",
      "incomplete_value": true,
      "site": "00b6588c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c34",
      "incomplete_value": true,
      "site": "00b05c34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65898",
      "incomplete_value": false,
      "site": "00b658a0",
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
            "const:92b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c40",
      "incomplete_value": false,
      "site": "00b05c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f8a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65888",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65898",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b658a8",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65888",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65898",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ],
    [
      "00b658a8",
      "WRITE",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c48) · [`00b05c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c50) · [`00b05c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c2c)
- 新版 [`00b658a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65878.md#insn-00b658a0) · [`00b658a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65878.md#insn-00b658a8) · [`00b65884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65878.md#insn-00b65884)

~~~diff
- 00b05c48 ["INT_ADD", "register:40f0:8", ["const:b05c48:8", "const:4:8"]]
- 00b05c48 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b658a0 ["INT_ADD", "register:40f0:8", ["const:b658a0:8", "const:4:8"]]
+ 00b658a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05c48 bytes 12610394
+ 00b658a0 bytes 9cd40394
- 00b05c50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
- 00b05c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b658a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d08:8"]]
+ 00b658a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05c50 bytes 602607f9
+ 00b658a8 bytes 608606f9
- 00b05c2c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65884 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05c2c bytes d32c00f0
+ 00b65884 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb4cabf074c71bcec246e0455ab825f"></a>

### [`00b05c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md) → [`00b658bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b658bc.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b05c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05c68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05c68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05c64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05c68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b658cc",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b658bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b658c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b658cc",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c64) · [`00b05c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c68) · [`00b05c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c78)
- 新版 [`00b658d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b658bc.md#insn-00b658d0)

~~~diff
- 00b05c64 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b05c64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05c64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05c64 bytes f30f1ef8
- 00b05c68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05c68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05c68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05c68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05c68 bytes fd7b01a9
- 00b05c78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05c78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b658d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b658d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05c78 bytes 080100b5
+ 00b658d0 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a22aa23d1fcea36ebdc618347a2a255"></a>

### [`00b05cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md) → [`00b6590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6590c.md) _ZN8firebase7options15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b65964",
      "incomplete_value": true,
      "site": "00b65964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d0c",
      "incomplete_value": true,
      "site": "00b05d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "definition_site": "00b65940",
      "incomplete_value": true,
      "site": "00b6594c",
      "value": [
        "LOAD",
        "8",
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ce8",
      "incomplete_value": true,
      "site": "00b05cf4",
      "value": [
        "LOAD",
        "8",
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
                "const:e48:8"
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
      "00b65920",
      "READ",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65940",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65964",
      "WRITE",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65920",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65940",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65964",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05cf4) · [`00b05d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05d0c) · [`00b05cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05cc4)
- 新版 [`00b6594c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6590c.md#insn-00b6594c) · [`00b65964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6590c.md#insn-00b65964) · [`00b6591c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6590c.md#insn-00b6591c)

~~~diff
- 00b05cf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05cf4 ["INT_ADD", "register:40f0:8", ["const:b05cf4:8", "const:4:8"]]
- 00b05cf4 ["CALLIND", null, ["register:0:8"]]
+ 00b6594c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6594c ["INT_ADD", "register:40f0:8", ["const:b6594c:8", "const:4:8"]]
+ 00b6594c ["CALLIND", null, ["register:0:8"]]
- 00b05cf4 bytes 00013fd6
+ 00b6594c bytes 00013fd6
- 00b05d0c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05d0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e50:8"]]
- 00b05d0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65964 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65964 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d10:8"]]
+ 00b65964 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05d0c bytes a0423939
+ 00b65964 bytes a0423439
- 00b05cc4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b6591c ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00b05cc4 bytes d52c00f0
+ 00b6591c bytes 152e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd81eb28a9d4d5a1fa866d0c8d68e04"></a>

### [`00b05d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md) → [`00b65978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65978.md) _ZN8firebase7options12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 14.29% / 新版 14.29%

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
      "site": "00b05d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b659b4"
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
      "00b6598c",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65990",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b05d80"
      ]
    ],
    [
      "00b65998",
      "READ",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6598c",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65990",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b659d8"
      ]
    ],
    [
      "00b65998",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d38) · [`00b05d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d5c) · [`00b05d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d64)
- 新版 [`00b65990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65978.md#insn-00b65990)

~~~diff
- 00b05d38 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05d38 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b65990 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b65990 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b05d38 bytes 410200b4
+ 00b65990 bytes 410200b4
- 00b05d5c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05d5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05d5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e50:8"]]
- 00b05d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05d5c bytes bf423939
- 00b05d64 ["INT_ADD", "register:40f0:8", ["const:b05d64:8", "const:4:8"]]
- 00b05d64 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b05d64 bytes df600394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ccdd8dd2b87934681c0de26c51ee74"></a>

### [`00b05d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md) → [`00b659e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b05dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65a28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05dac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05da4",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05dac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65a2c"
      ]
    ],
    [
      "unmatched:00b05db4",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b659fc",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65a2c"
      ]
    ],
    [
      "00b65a0c",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05dac) · [`00b05dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05dc8) · [`00b05dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05dd0)
- 新版 [`00b65a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md#insn-00b65a20)

~~~diff
- 00b05dac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05dac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05dac bytes 410100b5
- 00b05dc8 ["INT_ADD", "register:40f0:8", ["const:b05dc8:8", "const:4:8"]]
- 00b05dc8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65a20 ["INT_ADD", "register:40f0:8", ["const:b65a20:8", "const:4:8"]]
+ 00b65a20 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05dc8 bytes b2600394
+ 00b65a20 bytes 3cd40394
- 00b05dd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
- 00b05dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05dd0 bytes 802607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3563ed3a8fa0fd8f8d2e8a090136efd5"></a>

### [`00b05e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md) → [`00b65a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65a74",
      "incomplete_value": false,
      "site": "00b65a78",
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
      "definition_site": "00b05e1c",
      "incomplete_value": false,
      "site": "00b05e20",
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
      "definition_site": "00b65a84",
      "incomplete_value": true,
      "site": "00b65a90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b05e2c",
      "incomplete_value": true,
      "site": "00b05e38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b65a74",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65a84",
      "DATA",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65a74",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b65a84",
      "DATA",
      [
        "storage",
        "01125d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e20) · [`00b05e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e18) · [`00b05e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e1c)
- 新版 [`00b65a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a78) · [`00b65a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a70) · [`00b65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a74)

~~~diff
- 00b05e20 ["INT_ADD", "register:40f0:8", ["const:b05e20:8", "const:4:8"]]
- 00b05e20 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65a78 ["INT_ADD", "register:40f0:8", ["const:b65a78:8", "const:4:8"]]
+ 00b65a78 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b05e20 bytes d8600394
+ 00b65a78 bytes 62d40394
- 00b05e18 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b65a70 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b05e18 bytes 80bcfff0
+ 00b65a70 bytes 00bafff0
- 00b05e1c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b05e1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05e1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05e1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65a74 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b65a74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65a74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65a74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05e1c bytes 001c1591
+ 00b65a74 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f88349b93ec4ae71465ff2937adcfb59"></a>

### [`00b05e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md) → [`00b65a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65ad4",
      "incomplete_value": true,
      "site": "00b65ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e7c",
      "incomplete_value": true,
      "site": "00b05e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "00b65ab0",
      "incomplete_value": true,
      "site": "00b65ab0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e58",
      "incomplete_value": true,
      "site": "00b05e58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65ab8",
      "incomplete_value": false,
      "site": "00b65acc",
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
            "const:92b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e60",
      "incomplete_value": false,
      "site": "00b05e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f8a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65aa8",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ab8",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b65ad4",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65aa8",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ab8",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ],
    [
      "00b65ad4",
      "WRITE",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e74) · [`00b05e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e7c) · [`00b05e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e48)
- 新版 [`00b65acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65acc) · [`00b65ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65ad4) · [`00b65aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65aa0)

~~~diff
- 00b05e74 ["INT_ADD", "register:40f0:8", ["const:b05e74:8", "const:4:8"]]
- 00b05e74 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65acc ["INT_ADD", "register:40f0:8", ["const:b65acc:8", "const:4:8"]]
+ 00b65acc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05e74 bytes 87600394
+ 00b65acc bytes 11d40394
- 00b05e7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
- 00b05e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65ad4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
+ 00b65ad4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05e7c bytes 802607f9
+ 00b65ad4 bytes 808606f9
- 00b05e48 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b65aa0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00b05e48 bytes d42c00f0
+ 00b65aa0 bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-448efc49b450ab74d9fdd68ddb88f054"></a>

### [`00b05eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md) → [`00b65b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65b20",
      "incomplete_value": false,
      "site": "00b65b24",
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
      "definition_site": "00b05ec8",
      "incomplete_value": false,
      "site": "00b05ecc",
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
      "definition_site": "00b65b30",
      "incomplete_value": true,
      "site": "00b65b3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b05ed8",
      "incomplete_value": true,
      "site": "00b05ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b65b20",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65b30",
      "DATA",
      [
        "storage",
        "010a0e90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65b20",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b65b30",
      "DATA",
      [
        "storage",
        "01125d50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ecc) · [`00b05ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ec4) · [`00b05ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ec8)
- 新版 [`00b65b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b24) · [`00b65b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b1c) · [`00b65b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b20)

~~~diff
- 00b05ecc ["INT_ADD", "register:40f0:8", ["const:b05ecc:8", "const:4:8"]]
- 00b05ecc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65b24 ["INT_ADD", "register:40f0:8", ["const:b65b24:8", "const:4:8"]]
+ 00b65b24 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b05ecc bytes ad600394
+ 00b65b24 bytes 37d40394
- 00b05ec4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b65b1c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b05ec4 bytes a0bcff90
+ 00b65b1c bytes 20baff90
- 00b05ec8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b05ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65b20 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b65b20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05ec8 bytes 00c81791
+ 00b65b20 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653a18928dd9a6f92e27b5a69d18adeb"></a>

### [`00b05ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md) → [`00b65b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65b6c",
      "incomplete_value": true,
      "site": "00b65b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f14",
      "incomplete_value": true,
      "site": "00b05f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65b54",
      "incomplete_value": true,
      "site": "00b65b54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05efc",
      "incomplete_value": true,
      "site": "00b05efc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65b60",
      "incomplete_value": false,
      "site": "00b65b64",
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
            "const:93a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f08",
      "incomplete_value": false,
      "site": "00b05f0c",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65b50",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b60",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b65b6c",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65b50",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b60",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65b6c",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05f0c) · [`00b05f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05f14) · [`00b05ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05ef4)
- 新版 [`00b65b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b64) · [`00b65b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b6c) · [`00b65b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b4c)

~~~diff
- 00b05f0c ["INT_ADD", "register:40f0:8", ["const:b05f0c:8", "const:4:8"]]
- 00b05f0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65b64 ["INT_ADD", "register:40f0:8", ["const:b65b64:8", "const:4:8"]]
+ 00b65b64 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05f0c bytes 61600394
+ 00b65b64 bytes ebd30394
- 00b05f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
- 00b05f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
+ 00b65b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f14 bytes 604e07f9
+ 00b65b6c bytes 60ae06f9
- 00b05ef4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65b4c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05ef4 bytes d32c00f0
+ 00b65b4c bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1392cca20377ff03fa3d03abb2fa3e14"></a>

### [`00b05f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md) → [`00b65b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65bac",
      "incomplete_value": true,
      "site": "00b65bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f54",
      "incomplete_value": true,
      "site": "00b05f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65b94",
      "incomplete_value": true,
      "site": "00b65b94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f3c",
      "incomplete_value": true,
      "site": "00b05f3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65b9c",
      "incomplete_value": false,
      "site": "00b65ba4",
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
            "const:93a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f44",
      "incomplete_value": false,
      "site": "00b05f4c",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65b90",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b9c",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b65bac",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65b90",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b9c",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65bac",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f4c) · [`00b05f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f54) · [`00b05f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f34)
- 新版 [`00b65ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65ba4) · [`00b65bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65bac) · [`00b65b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65b8c)

~~~diff
- 00b05f4c ["INT_ADD", "register:40f0:8", ["const:b05f4c:8", "const:4:8"]]
- 00b05f4c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65ba4 ["INT_ADD", "register:40f0:8", ["const:b65ba4:8", "const:4:8"]]
+ 00b65ba4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05f4c bytes 51600394
+ 00b65ba4 bytes dbd30394
- 00b05f54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
- 00b05f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
+ 00b65bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f54 bytes 604e07f9
+ 00b65bac bytes 60ae06f9
- 00b05f34 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65b8c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05f34 bytes d32c00f0
+ 00b65b8c bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75d4d8cd4c298f959c13d85684d0cd1b"></a>

### [`00b05f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md) → [`00b65bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65bf0",
      "incomplete_value": true,
      "site": "00b65bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f98",
      "incomplete_value": true,
      "site": "00b05f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65bd4",
      "incomplete_value": true,
      "site": "00b65bd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f7c",
      "incomplete_value": true,
      "site": "00b05f7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65be0",
      "incomplete_value": false,
      "site": "00b65be8",
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
            "const:93a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f88",
      "incomplete_value": false,
      "site": "00b05f90",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65bd0",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65be0",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b65bf0",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65bd0",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65be0",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65bf0",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f90) · [`00b05f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f98) · [`00b05f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f74)
- 新版 [`00b65be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65be8) · [`00b65bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65bf0) · [`00b65bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65bcc)

~~~diff
- 00b05f90 ["INT_ADD", "register:40f0:8", ["const:b05f90:8", "const:4:8"]]
- 00b05f90 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65be8 ["INT_ADD", "register:40f0:8", ["const:b65be8:8", "const:4:8"]]
+ 00b65be8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05f90 bytes 40600394
+ 00b65be8 bytes cad30394
- 00b05f98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
- 00b05f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65bf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
+ 00b65bf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f98 bytes 604e07f9
+ 00b65bf0 bytes 60ae06f9
- 00b05f74 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65bcc ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05f74 bytes d32c00f0
+ 00b65bcc bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ee97b38e95f96f62d28854cda4ae198"></a>

### [`00b05fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md) → [`00b65c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65c34",
      "incomplete_value": true,
      "site": "00b65c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05fdc",
      "incomplete_value": true,
      "site": "00b05fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65c18",
      "incomplete_value": true,
      "site": "00b65c18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05fc0",
      "incomplete_value": true,
      "site": "00b05fc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65c20",
      "incomplete_value": false,
      "site": "00b65c2c",
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
            "const:93a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05fc8",
      "incomplete_value": false,
      "site": "00b05fd4",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65c14",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c20",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b65c34",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65c14",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c20",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65c34",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fd4) · [`00b05fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fdc) · [`00b05fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fb8)
- 新版 [`00b65c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c2c) · [`00b65c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c34) · [`00b65c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c10)

~~~diff
- 00b05fd4 ["INT_ADD", "register:40f0:8", ["const:b05fd4:8", "const:4:8"]]
- 00b05fd4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65c2c ["INT_ADD", "register:40f0:8", ["const:b65c2c:8", "const:4:8"]]
+ 00b65c2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05fd4 bytes 2f600394
+ 00b65c2c bytes b9d30394
- 00b05fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
- 00b05fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
+ 00b65c34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05fdc bytes 604e07f9
+ 00b65c34 bytes 60ae06f9
- 00b05fb8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65c10 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b05fb8 bytes d32c00f0
+ 00b65c10 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd208c53bfb1e06c8348e0721a2104ba"></a>

### [`00b05ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md) → [`00b65c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b65cac",
      "incomplete_value": true,
      "site": "00b65cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06054",
      "incomplete_value": true,
      "site": "00b06054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "definition_site": "00b65c88",
      "incomplete_value": true,
      "site": "00b65c94",
      "value": [
        "LOAD",
        "8",
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06030",
      "incomplete_value": true,
      "site": "00b0603c",
      "value": [
        "LOAD",
        "8",
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
                "const:e98:8"
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
      "00b65c68",
      "READ",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65c88",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65cac",
      "WRITE",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65c68",
      "READ",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65c88",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65cac",
      "WRITE",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0603c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b0603c) · [`00b06054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b06054) · [`00b0600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b0600c)
- 新版 [`00b65c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65c94) · [`00b65cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65cac) · [`00b65c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65c64)

~~~diff
- 00b0603c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0603c ["INT_ADD", "register:40f0:8", ["const:b0603c:8", "const:4:8"]]
- 00b0603c ["CALLIND", null, ["register:0:8"]]
+ 00b65c94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65c94 ["INT_ADD", "register:40f0:8", ["const:b65c94:8", "const:4:8"]]
+ 00b65c94 ["CALLIND", null, ["register:0:8"]]
- 00b0603c bytes 00013fd6
+ 00b65c94 bytes 00013fd6
- 00b06054 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b06054 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ea0:8"]]
- 00b06054 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65cac ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65cac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d60:8"]]
+ 00b65cac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b06054 bytes a0823a39
+ 00b65cac bytes a0823539
- 00b0600c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b65c64 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00b0600c bytes d52c00d0
+ 00b65c64 bytes 152e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0ab558f704076ddc26833347de12f7b"></a>

### [`00b06068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md) → [`00b65cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b65cfc",
      "incomplete_value": true,
      "site": "00b65cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060a4",
      "incomplete_value": true,
      "site": "00b060a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "definition_site": "00b65d1c",
      "incomplete_value": true,
      "site": "00b65d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060c4",
      "incomplete_value": true,
      "site": "00b060c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "00b65cd8",
      "incomplete_value": true,
      "site": "00b65cd8",
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
      "definition_site": "00b06080",
      "incomplete_value": true,
      "site": "00b06080",
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
      "00b65cd4",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ce0",
      "READ",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65cfc",
      "WRITE",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65cd4",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ce0",
      "READ",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65cfc",
      "WRITE",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b060a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b060a4) · [`00b060c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b060c0) · [`00b060c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b060c4)
- 新版 [`00b65cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65cfc) · [`00b65d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65d18) · [`00b65d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65d1c)

~~~diff
- 00b060a4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b060a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b060a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ea0:8"]]
- 00b060a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65cfc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65cfc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65cfc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d60:8"]]
+ 00b65cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b060a4 bytes bf823a39
+ 00b65cfc bytes bf823539
- 00b060c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b060c0 ["INT_ADD", "register:40f0:8", ["const:b060c0:8", "const:4:8"]]
- 00b060c0 ["CALLIND", null, ["register:0:8"]]
+ 00b65d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65d18 ["INT_ADD", "register:40f0:8", ["const:b65d18:8", "const:4:8"]]
+ 00b65d18 ["CALLIND", null, ["register:0:8"]]
- 00b060c0 bytes 00013fd6
+ 00b65d18 bytes 00013fd6
- 00b060c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
- 00b060c4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b060c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b65d1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00b65d1c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b65d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b060c4 bytes 9f4e07f9
+ 00b65d1c bytes 9fae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2274f0abbb315e66130fd168fa96085f"></a>

### [`00b060d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md) → [`00b65d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65d70",
      "incomplete_value": true,
      "site": "00b65d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06118",
      "incomplete_value": true,
      "site": "00b06118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "00b65d4c",
      "incomplete_value": true,
      "site": "00b65d4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060f4",
      "incomplete_value": true,
      "site": "00b060f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65d54",
      "incomplete_value": false,
      "site": "00b65d68",
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
            "const:93a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060fc",
      "incomplete_value": false,
      "site": "00b06110",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65d44",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d54",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b65d70",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65d44",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d54",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65d70",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b06110) · [`00b06118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b06118) · [`00b060e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b060e4)
- 新版 [`00b65d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d68) · [`00b65d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d70) · [`00b65d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d3c)

~~~diff
- 00b06110 ["INT_ADD", "register:40f0:8", ["const:b06110:8", "const:4:8"]]
- 00b06110 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65d68 ["INT_ADD", "register:40f0:8", ["const:b65d68:8", "const:4:8"]]
+ 00b65d68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b06110 bytes e05f0394
+ 00b65d68 bytes 6ad30394
- 00b06118 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
- 00b06118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65d70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00b65d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b06118 bytes 804e07f9
+ 00b65d70 bytes 80ae06f9
- 00b060e4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b65d3c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00b060e4 bytes d42c00d0
+ 00b65d3c bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94e725008c25bbac8bdcced871d35b0"></a>

### [`00b06148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md) → [`00b65da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65dbc",
      "incomplete_value": false,
      "site": "00b65dc0",
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
      "definition_site": "00b06164",
      "incomplete_value": false,
      "site": "00b06168",
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
      "definition_site": "00b65dcc",
      "incomplete_value": true,
      "site": "00b65dd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b06174",
      "incomplete_value": true,
      "site": "00b06180",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b65dbc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65dcc",
      "DATA",
      [
        "storage",
        "010a0ea8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65dbc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b65dcc",
      "DATA",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06168) · [`00b06160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06160) · [`00b06164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06164)
- 新版 [`00b65dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65dc0) · [`00b65db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65db8) · [`00b65dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65dbc)

~~~diff
- 00b06168 ["INT_ADD", "register:40f0:8", ["const:b06168:8", "const:4:8"]]
- 00b06168 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65dc0 ["INT_ADD", "register:40f0:8", ["const:b65dc0:8", "const:4:8"]]
+ 00b65dc0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b06168 bytes 06600394
+ 00b65dc0 bytes 90d30394
- 00b06160 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b65db8 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b06160 bytes 80bcffd0
+ 00b65db8 bytes 00bafff0
- 00b06164 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b06164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b06164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b06164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65dbc ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b65dbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65dbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65dbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b06164 bytes 001c1591
+ 00b65dbc bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-744cf81a3166a9bcb9604a30012fc81a"></a>

### [`00b06184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md) → [`00b65ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md) _ZN8firebase17version_registrar13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b061c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65e1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b061a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b06198",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b061a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65e20"
      ]
    ],
    [
      "unmatched:00b061a8",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65df0",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65df8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65e20"
      ]
    ],
    [
      "00b65e00",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b061a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b061a0) · [`00b061bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b061bc) · [`00b061c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b061c4)
- 新版 [`00b65e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md#insn-00b65e14)

~~~diff
- 00b061a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b061a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b061a0 bytes 410100b5
- 00b061bc ["INT_ADD", "register:40f0:8", ["const:b061bc:8", "const:4:8"]]
- 00b061bc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65e14 ["INT_ADD", "register:40f0:8", ["const:b65e14:8", "const:4:8"]]
+ 00b65e14 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b061bc bytes b55f0394
+ 00b65e14 bytes 3fd30394
- 00b061c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
- 00b061c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b061c4 bytes 804e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4e21d9fa1c670fe7f3a2a06bbe4ec03"></a>

### [`00b061f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md) → [`00b65e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b65e68",
      "incomplete_value": false,
      "site": "00b65e6c",
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
      "definition_site": "00b06210",
      "incomplete_value": false,
      "site": "00b06214",
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
      "definition_site": "00b65e78",
      "incomplete_value": true,
      "site": "00b65e84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b06220",
      "incomplete_value": true,
      "site": "00b0622c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b65e68",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65e78",
      "DATA",
      [
        "storage",
        "010a0ec0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65e68",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b65e78",
      "DATA",
      [
        "storage",
        "01125d80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b06214) · [`00b0620c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b0620c) · [`00b06210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b06210)
- 新版 [`00b65e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e6c) · [`00b65e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e64) · [`00b65e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e68)

~~~diff
- 00b06214 ["INT_ADD", "register:40f0:8", ["const:b06214:8", "const:4:8"]]
- 00b06214 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65e6c ["INT_ADD", "register:40f0:8", ["const:b65e6c:8", "const:4:8"]]
+ 00b65e6c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b06214 bytes db5f0394
+ 00b65e6c bytes 65d30394
- 00b0620c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b65e64 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b0620c bytes 80bcfff0
+ 00b65e64 bytes 20baff90
- 00b06210 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b06210 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b06210 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b06210 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65e68 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b65e68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b06210 bytes 00c81791
+ 00b65e68 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81f2e75bada8afaa96333469e38dd750"></a>

### [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) → [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b065bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bac0.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65ed0",
      "incomplete_value": true,
      "site": "00b65ee0",
      "value": [
        "LOAD",
        "8",
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06278",
      "incomplete_value": true,
      "site": "00b06288",
      "value": [
        "LOAD",
        "8",
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65ed4",
      "incomplete_value": true,
      "site": "00b65ee0",
      "value": [
        "LOAD",
        "8",
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0627c",
      "incomplete_value": true,
      "site": "00b06288",
      "value": [
        "LOAD",
        "8",
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
                "const:e58:8"
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
      "00b65ed0",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ed4",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65ed0",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ed4",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b06288) · [`00b06268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b06268) · [`00b06270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b06270)
- 新版 [`00b65ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ee0) · [`00b65ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ec0) · [`00b65ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ec8)

~~~diff
- 00b06288 ["INT_ADD", "register:40f0:8", ["const:b06288:8", "const:4:8"]]
- 00b06288 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00b65ee0 ["INT_ADD", "register:40f0:8", ["const:b65ee0:8", "const:4:8"]]
+ 00b65ee0 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b06288 bytes ae5e0394
+ 00b65ee0 bytes 30d20394
- 00b06268 ["INT_ADD", "register:40f0:8", ["const:b06268:8", "const:4:8"]]
- 00b06268 ["CALL", null, ["callee:00b6602c:8"]]
+ 00b65ec0 ["INT_ADD", "register:40f0:8", ["const:b65ec0:8", "const:4:8"]]
+ 00b65ec0 ["CALL", null, ["callee:00b6602c:8"]]
- 00b06268 bytes 5b000094
+ 00b65ec0 bytes 5b000094
- 00b06270 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b65ec8 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00b06270 bytes c82c00d0
+ 00b65ec8 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfb74a9d20f7a2f3bd3338f39c72a7b"></a>

### [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) → [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) FUN_00b6602c

採用 · 移動量 `+0x5fc58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) · 呼出先 5件 [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md)
- 新版 呼出元 4件 [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) · 呼出先 5件 [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66048",
      "incomplete_value": false,
      "site": "00b66048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b063f0",
      "incomplete_value": false,
      "site": "00b063f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "definition_site": "00b66094",
      "incomplete_value": true,
      "site": "00b66094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0643c",
      "incomplete_value": true,
      "site": "00b0643c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "definition_site": "00b660ec",
      "incomplete_value": true,
      "site": "00b660ec",
      "value": [
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
      "definition_site": "00b06494",
      "incomplete_value": true,
      "site": "00b06494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66040",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66048",
      "WRITE",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6606c",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66040",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66048",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6606c",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b063f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b063f0) · [`00b06434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b06434) · [`00b0643c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b0643c)
- 新版 [`00b66048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b66048) · [`00b6608c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b6608c) · [`00b66094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b66094)

~~~diff
- 00b063f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ec8:8"]]
- 00b063f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b66048 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d88:8"]]
+ 00b66048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b063f0 bytes a9ca0eb9
+ 00b66048 bytes a98a0db9
- 00b06434 ["INT_ADD", "register:40f0:8", ["const:b06434:8", "const:4:8"]]
- 00b06434 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b6608c ["INT_ADD", "register:40f0:8", ["const:b6608c:8", "const:4:8"]]
+ 00b6608c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b06434 bytes 175f0394
+ 00b6608c bytes a1d20394
- 00b0643c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d90:8"]]
- 00b0643c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66094 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c50:8"]]
+ 00b66094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b0643c bytes a0ca06f9
+ 00b66094 bytes a02a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08169c6652c78ad854a3f7ef781e9973"></a>

### [`00b065bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md) → [`00b66214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md) FUN_00b66214

採用 · 移動量 `+0x5fc58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 2件 [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.10% / 新版 86.10%

CFGの説明率　旧版 80.52% / 新版 83.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06798"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b067b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b068d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66274",
      "READ",
      [
        "storage",
        "010a0e60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66310",
      "READ",
      [
        "storage",
        "010a0e68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663ac",
      "READ",
      [
        "storage",
        "010a0e70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66274",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66310",
      "READ",
      [
        "storage",
        "01125d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663ac",
      "READ",
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

- 旧版 [`00b06628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md#insn-00b06628) · [`00b066c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md#insn-00b066c4) · [`00b06760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md#insn-00b06760)
- 新版 [`00b66280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md#insn-00b66280) · [`00b6631c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md#insn-00b6631c) · [`00b663b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md#insn-00b663b8)

~~~diff
- 00b06628 ["INT_ADD", "register:40f0:8", ["const:b06628:8", "const:4:8"]]
- 00b06628 ["CALL", null, ["callee:004977f4:8"]]
+ 00b66280 ["INT_ADD", "register:40f0:8", ["const:b66280:8", "const:4:8"]]
+ 00b66280 ["CALL", null, ["callee:004977f4:8"]]
- 00b06628 bytes cdb8e597
+ 00b66280 bytes 5dc5e497
- 00b066c4 ["INT_ADD", "register:40f0:8", ["const:b066c4:8", "const:4:8"]]
- 00b066c4 ["CALL", null, ["callee:004977f4:8"]]
+ 00b6631c ["INT_ADD", "register:40f0:8", ["const:b6631c:8", "const:4:8"]]
+ 00b6631c ["CALL", null, ["callee:004977f4:8"]]
- 00b066c4 bytes a6b8e597
+ 00b6631c bytes 36c5e497
- 00b06760 ["INT_ADD", "register:40f0:8", ["const:b06760:8", "const:4:8"]]
- 00b06760 ["CALL", null, ["callee:004977f4:8"]]
+ 00b663b8 ["INT_ADD", "register:40f0:8", ["const:b663b8:8", "const:4:8"]]
+ 00b663b8 ["CALL", null, ["callee:004977f4:8"]]
- 00b06760 bytes 7fb8e597
+ 00b663b8 bytes 0fc5e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b044618eeac4dc3e8c5216aed877b1b"></a>

### [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) → [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) FUN_00b66620

採用 · 移動量 `+0x5fc58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b06b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md) [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 4件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee70.md)
- 新版 呼出元 6件 [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 4件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b920.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.04% / 新版 28.04%

CFGの説明率　旧版 24.24% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66654",
      "incomplete_value": true,
      "site": "00b66654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b069fc",
      "incomplete_value": true,
      "site": "00b069fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "site": "00b06a3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66634",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66644",
      "PARAM",
      [
        "storage",
        "002ab049",
        null,
        "string"
      ]
    ],
    [
      "00b6664c",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b66634",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66644",
      "PARAM",
      [
        "storage",
        "002bbe12",
        null,
        "string"
      ]
    ],
    [
      "00b6664c",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b069fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b069fc) · [`00b06a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b06a1c) · [`00b06a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b06a28)
- 新版 [`00b66654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md#insn-00b66654) · [`00b66674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md#insn-00b66674)

~~~diff
- 00b069fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec8:8"]]
- 00b069fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b66654 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b66654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b069fc bytes 88ca0eb9
+ 00b66654 bytes 888a0db9
- 00b06a1c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b06a1c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b66674 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b66674 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b06a1c bytes 210200b4
+ 00b66674 bytes 210200b4
- 00b06a28 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b06a28 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b06a28 bytes c8000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b17f26a5ddc1727407c18d01f8945d9"></a>

### [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) → [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb00.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)
- 新版 呼出元 1件 [`00c5a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a550.md) · 呼出先 7件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "definition_site": "00b66900",
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
      "definition_site": "00b06ca8",
      "incomplete_value": true,
      "site": "00b06cac",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6691c",
      "incomplete_value": false,
      "site": "00b66920",
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
            "const:c6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06cc4",
      "incomplete_value": false,
      "site": "00b06cc8",
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
            "const:107:8"
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
      "00b668f0",
      "READ",
      [
        "storage",
        "00c1b978",
        null,
        "pointer"
      ]
    ],
    [
      "00b66900",
      "READ",
      [
        "storage",
        "00c106e0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66900",
      "PARAM",
      [
        "storage",
        "002a4f51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b668f0",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ],
    [
      "00b66900",
      "READ",
      [
        "storage",
        "00c8fe00",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66900",
      "PARAM",
      [
        "storage",
        "002b58f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06cac) · [`00b06cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06cc8) · [`00b06c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06c54)
- 新版 [`00b66904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b66904) · [`00b66920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b66920) · [`00b668ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b668ac)

~~~diff
- 00b06cac ["INT_ADD", "register:40f0:8", ["const:b06cac:8", "const:4:8"]]
- 00b06cac ["CALL", null, ["callee:00c5bad0:8"]]
+ 00b66904 ["INT_ADD", "register:40f0:8", ["const:b66904:8", "const:4:8"]]
+ 00b66904 ["CALL", null, ["callee:00c5bad0:8"]]
- 00b06cac bytes dd600394
+ 00b66904 bytes 73d40394
- 00b06cc8 ["INT_ADD", "register:40f0:8", ["const:b06cc8:8", "const:4:8"]]
- 00b06cc8 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b66920 ["INT_ADD", "register:40f0:8", ["const:b66920:8", "const:4:8"]]
+ 00b66920 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b06cc8 bytes 5e5c0394
+ 00b66920 bytes e0cf0394
- 00b06c54 ["INT_ADD", "register:40f0:8", ["const:b06c54:8", "const:4:8"]]
- 00b06c54 ["CALL", null, ["callee:00b6602c:8"]]
+ 00b668ac ["INT_ADD", "register:40f0:8", ["const:b668ac:8", "const:4:8"]]
+ 00b668ac ["CALL", null, ["callee:00b6602c:8"]]
- 00b06c54 bytes e0fdff97
+ 00b668ac bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e813497102eecc85e00ad665db36da7c"></a>

### [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) → [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf020.md) · 呼出先 28件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md)
- 新版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bad0.md) · 呼出先 28件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.60% / 新版 86.60%

CFGの説明率　旧版 60.23% / 新版 67.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件, `store_condition` 4件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07350"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b669cc",
      "PARAM",
      [
        "storage",
        "00290482",
        null,
        "string"
      ]
    ],
    [
      "00b669e0",
      "READ",
      [
        "storage",
        "00c1b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b669e8",
      "PARAM",
      [
        "storage",
        "002ac1f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b669cc",
      "PARAM",
      [
        "storage",
        "0029f9b9",
        null,
        "string"
      ]
    ],
    [
      "00b669e0",
      "READ",
      [
        "storage",
        "00c9b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b669e8",
      "PARAM",
      [
        "storage",
        "002bd17e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b07024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b07024) · [`00b07030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b07030) · [`00b07034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b07034)

~~~diff
- 00b07024 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b07024 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b07024 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b07024 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b07024 bytes ca000037
- 00b07030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00b07030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b07030 bytes 0a0900f9
- 00b07034 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b07034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b07034 bytes 0001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4473859aa0e0860933573247dc642f31"></a>

### [`00b07fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b07/00b07fc8.md) → [`00b67c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde930.md) · 呼出先 2件 [`00bdae9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdae9c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3b0.md) · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b320.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 62.50% / 新版 14.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_count` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b67c74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b67c4c"
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
      "00b67c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b07ff8"
      ]
    ],
    [
      "unmatched:00b07ff0",
      "PARAM",
      [
        "storage",
        "002a7e73",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b07ff4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00b67c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67c50"
      ]
    ],
    [
      "00b67c48",
      "PARAM",
      [
        "storage",
        "002b8aef",
        null,
        "string"
      ]
    ],
    [
      "00b67c4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b07ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b07/00b07fc8.md#insn-00b07ff4)
- 新版 [`00b67c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md#insn-00b67c4c) · [`00b67c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md#insn-00b67c64)

~~~diff
- 00b07ff4 ["INT_ADD", "register:40f0:8", ["const:b07ff4:8", "const:4:8"]]
- 00b07ff4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b07ff4 bytes 63580394
+ 00b67c4c ["INT_ADD", "register:40f0:8", ["const:b67c4c:8", "const:4:8"]]
+ 00b67c4c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b67c4c bytes edcb0394
+ 00b67c64 ["INT_ADD", "register:40f0:8", ["const:b67c64:8", "const:4:8"]]
+ 00b67c64 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00b67c64 bytes cfca0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8758b2b83a9f94cd764f78201ae57de"></a>

### [`00b080dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md) → [`00b67d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67d4c",
      "incomplete_value": true,
      "site": "00b67d4c",
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
      "definition_site": "00b080f4",
      "incomplete_value": true,
      "site": "00b080f4",
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
      "definition_site": "00b67d68",
      "incomplete_value": true,
      "site": "00b67d78",
      "value": [
        "LOAD",
        "8",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:ca0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08110",
      "incomplete_value": true,
      "site": "00b08120",
      "value": [
        "LOAD",
        "8",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:de0:8"
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
      "00b67d48",
      "READ",
      [
        "storage",
        "010a0de0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d68",
      "READ",
      [
        "storage",
        "010a0de0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d9c",
      "PARAM",
      [
        "storage",
        "002ac213",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b67d48",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d68",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d9c",
      "PARAM",
      [
        "storage",
        "002bd19e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b08120) · [`00b080ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b080ec) · [`00b080f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b080f0)
- 新版 [`00b67d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d78) · [`00b67d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d44) · [`00b67d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d48)

~~~diff
- 00b08120 ["INT_ADD", "register:40f0:8", ["const:b08120:8", "const:4:8"]]
- 00b08120 ["CALL", null, ["callee:00574cac:8"]]
+ 00b67d78 ["INT_ADD", "register:40f0:8", ["const:b67d78:8", "const:4:8"]]
+ 00b67d78 ["CALL", null, ["callee:00574cac:8"]]
- 00b08120 bytes 3d27e997
+ 00b67d78 bytes cd33e897
- 00b080ec ["COPY", "register:40b0:8", ["const:10a0000:8"]]
+ 00b67d44 ["COPY", "register:40b0:8", ["const:1125000:8"]]
- 00b080ec bytes d62c0090
+ 00b67d44 bytes f62d00d0
- 00b080f0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:de0:8"]]
- 00b080f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d48 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ca0:8"]]
+ 00b67d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b080f0 bytes c8f246f9
+ 00b67d48 bytes c85246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ae81ebb57bbc46f78a9cb6c8dac4ff"></a>

### [`00b08150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md) → [`00b67da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67dbc",
      "incomplete_value": true,
      "site": "00b67dbc",
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
      "definition_site": "00b08164",
      "incomplete_value": true,
      "site": "00b08164",
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
      "definition_site": "00b67dd4",
      "incomplete_value": true,
      "site": "00b67de0",
      "value": [
        "LOAD",
        "8",
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0817c",
      "incomplete_value": true,
      "site": "00b08188",
      "value": [
        "LOAD",
        "8",
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
                "const:dd8:8"
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
      "00b67db8",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0817c",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67db8",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67dd4",
      "READ",
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

- 旧版 [`00b08164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b08164) · [`00b08188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b08188) · [`00b0815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b0815c)
- 新版 [`00b67dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67dbc) · [`00b67de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67de0) · [`00b67db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67db4)

~~~diff
- 00b08164 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b08164 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b67dbc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b67dbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b08164 bytes 080200b4
+ 00b67dbc bytes 080200b4
- 00b08188 ["INT_ADD", "register:40f0:8", ["const:b08188:8", "const:4:8"]]
- 00b08188 ["CALL", null, ["callee:00497a08:8"]]
+ 00b67de0 ["INT_ADD", "register:40f0:8", ["const:b67de0:8", "const:4:8"]]
+ 00b67de0 ["CALL", null, ["callee:00497a08:8"]]
- 00b08188 bytes 7ab2e597
+ 00b67de0 bytes 0abfe497
- 00b0815c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b67db4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00b0815c bytes d42c0090
+ 00b67db4 bytes f42d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a9ddca0cd414a0b309f5f3762d61af7"></a>

### [`00b08760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md) → [`00b683b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b683b8.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 67.60% / 新版 76.59%

CFGの説明率　旧版 81.61% / 新版 77.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 18件, `call_count` 1件, `call_target` 1件, `store_count` 47件, `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b08794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b087a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b087a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b08794",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b087a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b087a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b683ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b683f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5b490"
      ]
    ],
    [
      "00b68400",
      "WRITE",
      [
        "storage",
        "Stack[-0x2dc]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b08794) · [`00b087a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b087a0) · [`00b087a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b087a4)

~~~diff
- 00b08794 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b08794 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b08794 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b08794 bytes a9031af8
- 00b087a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:508:8"]]
- 00b087a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b087a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b087a0 bytes ff8702f9
- 00b087a4 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00b087a4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:508:8"]]
- 00b087a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b087a4 bytes eb231439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422b3bcd2fba4d6b99dfbfe0446871fe"></a>

### [`00b0904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md) → [`00b68d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68d08.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0x5fcbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea70.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613984.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c5b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b500.md) · 呼出先 8件 [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 16.82% / 新版 14.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 9件, `call_argument_candidate` 15件, `call_count` 12件, `store_count` 69件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b09050"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b09080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0908c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b09050",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b09080",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b09088",
      "READ",
      [
        "storage",
        "002b1080",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68d0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b68d3c",
      "READ",
      [
        "storage",
        "002c30f0",
        null,
        null
      ]
    ],
    [
      "00b68d44",
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

- 旧版 [`00b09050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b09050) · [`00b09080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b09080) · [`00b0908c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b0908c)

~~~diff
- 00b09050 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b09050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b09050 bytes f91b00f9
- 00b09080 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b09080 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b09080 bytes e91700f9
- 00b0908c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b0908c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0908c bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea80d6511f18201afa597e5b4ff0205"></a>

### [`00b0a4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a4bc.md) → [`00b6a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0x5ff58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea80.md) · 呼出先 14件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`007101c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/007101c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea10.md)
- 新版 呼出元 1件 [`00c5b510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b510.md) · 呼出先 13件 [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4a0.md) [`00c5b4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4b0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 26.07% / 新版 28.95%

CFGの説明率　旧版 13.79% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 5件, `call_count` 3件, `store_count` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a4bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a4c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0a4bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0a4c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0a4c4",
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
      "00b6a414",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6a418",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6a41c",
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

- 旧版 [`00b0a4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a4bc.md#insn-00b0a4bc) · [`00b0a4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a4bc.md#insn-00b0a4c0) · [`00b0a4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a4bc.md#insn-00b0a4c4)

~~~diff
- 00b0a4bc ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b0a4bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b0a4bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0a4bc bytes f70f1cf8
- 00b0a4c0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0a4c0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0a4c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0a4c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0a4c0 bytes f65701a9
- 00b0a4c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0a4c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0a4c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b0a4c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0a4c4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dffd4fd3767c52edc13ac724b4ce5e4"></a>

### [`00b0a808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a808.md) → [`00b6a70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a70c.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0x5ff04` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea10.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5b4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4a0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count

命令の説明率　旧版 44.76% / 新版 29.01%

CFGの説明率　旧版 3.23% / 新版 1.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 17件, `call_argument_candidate` 4件, `call_count` 8件, `store_count` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a918"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6a76c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6a8e0"
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
      "unmatched:00b0a820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0a894"
      ]
    ],
    [
      "unmatched:00b0a828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0a8a4"
      ]
    ],
    [
      "unmatched:00b0a830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0a8b4"
      ]
    ]
  ],
  "added": [
    [
      "00b6a724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a774"
      ]
    ],
    [
      "00b6a730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a768"
      ]
    ],
    [
      "00b6a73c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a754"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0a820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a808.md#insn-00b0a820) · [`00b0a828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a808.md#insn-00b0a828) · [`00b0a830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a808.md#insn-00b0a830)

~~~diff
- 00b0a820 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0a820 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a820 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a820 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0a820 bytes a8030037
- 00b0a828 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0a828 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a828 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a828 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0a828 bytes e8030037
- 00b0a830 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0a830 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a830 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a830 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0a830 bytes 28040037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5275947a99feb2c2aab1df2e980a06fd"></a>

### [`00b0a9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md) → [`00b6a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5ffe8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea90.md) · 呼出先 5件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bdf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md)
- 新版 呼出元 1件 [`00c5b530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b530.md) · 呼出先 5件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bac0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.22% / 新版 83.22%

CFGの説明率　旧版 29.76% / 新版 28.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a9b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0a9b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0a9b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0a9b8",
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
      "00b6a998",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6a99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6a9a0",
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

- 旧版 [`00b0a9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0a9b0) · [`00b0a9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0a9b4) · [`00b0a9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0a9b8)

~~~diff
- 00b0a9b0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b0a9b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0a9b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b0a9b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0a9b0 bytes fc570ea9
- 00b0a9b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0a9b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0a9b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b0a9b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0a9b4 bytes f44f0fa9
- 00b0a9b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0a9b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0a9b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b0a9b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0a9b8 bytes fd7b10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-063698eabef7ed74cc0f3da3610e24da"></a>

### [`00b0abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md) → [`00b6abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0x5ffe8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea00.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b480.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 7.77% / 新版 4.65%

CFGの説明率　旧版 11.11% / 新版 4.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `call_count` 8件, `store_count` 17件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0abe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0abec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0abec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0abe8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0abec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0abf0",
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
      "00b6abd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6abd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6abd8",
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

- 旧版 [`00b0abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md#insn-00b0abe8) · [`00b0abec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md#insn-00b0abec) · [`00b0abf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md#insn-00b0abf0)

~~~diff
- 00b0abe8 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b0abe8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b0abe8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0abe8 bytes f70f1cf8
- 00b0abec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0abec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0abec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0abec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0abec bytes f65701a9
- 00b0abf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0abf0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0abf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b0abf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0abf0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-babd501b0d8dc4861060dd1a853877af"></a>

### [`00b0ad84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ad84.md) → [`00b6ae80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x600fc` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec20.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6e0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0addc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ad84.md#insn-00b0addc) · [`00b0ade8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ad84.md#insn-00b0ade8) · [`00b0adf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0ad84.md#insn-00b0adf4)
- 新版 [`00b6aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md#insn-00b6aed8) · [`00b6aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md#insn-00b6aee4) · [`00b6aef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md#insn-00b6aef0)

~~~diff
- 00b0addc ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00b0addc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b6aed8 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
+ 00b6aed8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b0addc bytes 590400b4
+ 00b6aed8 bytes 590400b4
- 00b0ade8 ["INT_ADD", "register:40f0:8", ["const:b0ade8:8", "const:4:8"]]
- 00b0ade8 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b6aee4 ["INT_ADD", "register:40f0:8", ["const:b6aee4:8", "const:4:8"]]
+ 00b6aee4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b0ade8 bytes 364d0394
+ 00b6aee4 bytes 97bf0394
- 00b0adf4 ["INT_ADD", "register:40f0:8", ["const:b0adf4:8", "const:4:8"]]
- 00b0adf4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b6aef0 ["INT_ADD", "register:40f0:8", ["const:b6aef0:8", "const:4:8"]]
+ 00b6aef0 ["CALL", null, ["callee:00c57a90:8"]]
- 00b0adf4 bytes 93400394
+ 00b6aef0 bytes e8b20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d28e4fa1e73cd51cea692a6a657c303"></a>

### [`00b0cfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cfcc.md) → [`00b6d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0x60174` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea20.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdeb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb80.md) [`00bdebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebd0.md)
- 新版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4b0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md) [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 30.00% / 新版 32.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d09c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d210"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0cfec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0cfec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d1bc"
      ]
    ],
    [
      "unmatched:00b0d058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d1e4"
      ]
    ],
    [
      "00b6d1d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0d098"
      ]
    ]
  ],
  "added": [
    [
      "00b6d160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d1bc"
      ]
    ],
    [
      "00b6d1cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d1e4"
      ]
    ],
    [
      "00b6d1d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d20c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cfcc.md#insn-00b0cfec) · [`00b0d024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cfcc.md#insn-00b0d024) · [`00b0d058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cfcc.md#insn-00b0d058)
- 新版 [`00b6d198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md#insn-00b6d198)

~~~diff
- 00b0cfec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b0cfec ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b0cfec bytes e1020054
- 00b0d024 ["INT_ADD", "register:40f0:8", ["const:b0d024:8", "const:4:8"]]
- 00b0d024 ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6d198 ["INT_ADD", "register:40f0:8", ["const:b6d198:8", "const:4:8"]]
+ 00b6d198 ["CALL", null, ["callee:00c5b680:8"]]
- 00b0d024 bytes eb460394
+ 00b6d198 bytes 3ab90394
- 00b0d058 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b0d058 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b0d058 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5918814ff828cc297e9f49b81930652c"></a>

### [`00b0d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d0b4.md) → [`00b6d310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEED2Ev

採用 · 移動量 `+0x6025c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea50.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea40.md) [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md)
- 新版 呼出元 1件 [`00c5b4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4e0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4d0.md) [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count

命令の説明率　旧版 90.70% / 新版 82.98%

CFGの説明率　旧版 57.89% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_argument_candidate` 1件, `call_count` 1件, `store_count` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d398"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d3a4"
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
      "unmatched:00b0d13c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0d104"
      ]
    ]
  ],
  "added": [
    [
      "00b6d394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d3a0"
      ]
    ],
    [
      "00b6d39c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ],
    [
      "00b6d3a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d360"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d0b4.md#insn-00b0d108) · [`00b0d138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d0b4.md#insn-00b0d138) · [`00b0d13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d0b4.md#insn-00b0d13c)
- 新版 [`00b6d364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md#insn-00b6d364)

~~~diff
- 00b0d108 ["INT_ADD", "register:40f0:8", ["const:b0d108:8", "const:4:8"]]
- 00b0d108 ["CALL", null, ["callee:00c5b4d0:8"]]
+ 00b6d364 ["INT_ADD", "register:40f0:8", ["const:b6d364:8", "const:4:8"]]
+ 00b6d364 ["CALL", null, ["callee:00c5b4d0:8"]]
- 00b0d108 bytes 4e460394
+ 00b6d364 bytes 5bb80394
- 00b0d138 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e0:8"]]
- 00b0d138 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0d138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b0d138 bytes bf7200f9
- 00b0d13c ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b0d13c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0d13c bytes 56feffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d715e2f4a6b38cea0ae00de3b4f2c48"></a>

### [`00b0d3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d3e0.md) → [`00b6d6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md)
- 新版 呼出元 1件 [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d3e0.md#insn-00b0d3e0) · [`00b0d3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d3e0.md#insn-00b0d3fc) · [`00b0d408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d3e0.md#insn-00b0d408)
- 新版 [`00b6d6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d6fc) · [`00b6d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d718) · [`00b6d724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d6fc.md#insn-00b6d724)

~~~diff
- 00b0d3e0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0d3e0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6d6fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6d6fc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b0d3e0 bytes 610200b4
+ 00b6d6fc bytes 610200b4
- 00b0d3fc ["INT_ADD", "register:40f0:8", ["const:b0d3fc:8", "const:4:8"]]
- 00b0d3fc ["CALL", null, ["callee:00c5b650:8"]]
+ 00b6d718 ["INT_ADD", "register:40f0:8", ["const:b6d718:8", "const:4:8"]]
+ 00b6d718 ["CALL", null, ["callee:00c5b650:8"]]
- 00b0d3fc bytes e9450394
+ 00b6d718 bytes ceb70394
- 00b0d408 ["INT_ADD", "register:40f0:8", ["const:b0d408:8", "const:4:8"]]
- 00b0d408 ["CALL", null, ["callee:00c5b650:8"]]
+ 00b6d724 ["INT_ADD", "register:40f0:8", ["const:b6d724:8", "const:4:8"]]
+ 00b6d724 ["CALL", null, ["callee:00c5b650:8"]]
- 00b0d408 bytes e6450394
+ 00b6d724 bytes cbb70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7266698ba415008f9debf42cc85ff721"></a>

### [`00b0d604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d604.md) → [`00b6d938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d938.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea40.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md)
- 新版 呼出元 1件 [`00c5b4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4d0.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 47.06% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d668"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d678"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d99c"
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
      "unmatched:00b0d668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d9bc"
      ]
    ],
    [
      "unmatched:00b0d678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d980"
      ]
    ]
  ],
  "added": [
    [
      "00b6d99c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d9bc"
      ]
    ],
    [
      "00b6d9ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d980"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d604.md#insn-00b0d658) · [`00b0d668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d604.md#insn-00b0d668) · [`00b0d678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d604.md#insn-00b0d678)
- 新版 [`00b6d98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d938.md#insn-00b6d98c)

~~~diff
- 00b0d658 ["INT_ADD", "register:40f0:8", ["const:b0d658:8", "const:4:8"]]
- 00b0d658 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b6d98c ["INT_ADD", "register:40f0:8", ["const:b6d98c:8", "const:4:8"]]
+ 00b6d98c ["CALL", null, ["callee:00c57ab0:8"]]
- 00b0d658 bytes 82360394
+ 00b6d98c bytes 49a80394
- 00b0d668 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b0d668 bytes 00010054
- 00b0d678 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0d678 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0d678 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0d678 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b0d678 bytes a8fe0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5779df126a51c7b10ff326d383f139cd"></a>

### [`00b0d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d694.md) → [`00b6d9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebe0.md)
- 新版 呼出元 1件 [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0d6a8",
      "incomplete_value": true,
      "site": "00b0d6b0",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d694.md#insn-00b0d6b0) · [`00b0d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d694.md#insn-00b0d694) · [`00b0d6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d694.md#insn-00b0d6bc)
- 新版 [`00b6d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9e4) · [`00b6d9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9c8) · [`00b6d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9f0)

~~~diff
- 00b0d6b0 ["INT_ADD", "register:40f0:8", ["const:b0d6b0:8", "const:4:8"]]
- 00b0d6b0 ["CALL", null, ["callee:00c5b690:8"]]
+ 00b6d9e4 ["INT_ADD", "register:40f0:8", ["const:b6d9e4:8", "const:4:8"]]
+ 00b6d9e4 ["CALL", null, ["callee:00c5b690:8"]]
- 00b0d6b0 bytes 4c450394
+ 00b6d9e4 bytes 2bb70394
- 00b0d694 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0d694 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6d9c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6d9c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0d694 bytes 610200b4
+ 00b6d9c8 bytes 610200b4
- 00b0d6bc ["INT_ADD", "register:40f0:8", ["const:b0d6bc:8", "const:4:8"]]
- 00b0d6bc ["CALL", null, ["callee:00c5b690:8"]]
+ 00b6d9f0 ["INT_ADD", "register:40f0:8", ["const:b6d9f0:8", "const:4:8"]]
+ 00b6d9f0 ["CALL", null, ["callee:00c5b690:8"]]
- 00b0d6bc bytes 49450394
+ 00b6d9f0 bytes 28b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f978e652046188968945a2502f0ce9"></a>

### [`00b0d6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d6e4.md) → [`00b6da18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdebf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdebf0.md)
- 新版 呼出元 1件 [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0d6f8",
      "incomplete_value": true,
      "site": "00b0d700",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d6e4.md#insn-00b0d700) · [`00b0d6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d6e4.md#insn-00b0d6e4) · [`00b0d70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d6e4.md#insn-00b0d70c)
- 新版 [`00b6da34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da34) · [`00b6da18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da18) · [`00b6da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da40)

~~~diff
- 00b0d700 ["INT_ADD", "register:40f0:8", ["const:b0d700:8", "const:4:8"]]
- 00b0d700 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00b6da34 ["INT_ADD", "register:40f0:8", ["const:b6da34:8", "const:4:8"]]
+ 00b6da34 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00b0d700 bytes 3c450394
+ 00b6da34 bytes 1bb70394
- 00b0d6e4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0d6e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6da18 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6da18 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0d6e4 bytes 610200b4
+ 00b6da18 bytes 610200b4
- 00b0d70c ["INT_ADD", "register:40f0:8", ["const:b0d70c:8", "const:4:8"]]
- 00b0d70c ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00b6da40 ["INT_ADD", "register:40f0:8", ["const:b6da40:8", "const:4:8"]]
+ 00b6da40 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00b0d70c bytes 39450394
+ 00b6da40 bytes 18b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0f7244d33ada5ce6b6d95ee3b947e5d"></a>

### [`00b0d784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md) → [`00b6dab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dab8.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md) · 呼出先 17件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)
- 新版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md) · 呼出先 17件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.04% / 新版 71.04%

CFGの説明率　旧版 30.88% / 新版 32.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d7b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0d7b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0d7b8",
      "READ",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b0d7bc",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b6daec",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6daf0",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d7b4) · [`00b0d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d7c4) · [`00b0d7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d7c8)

~~~diff
- 00b0d7b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b0d7b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0d7b4 bytes e81f00f9
- 00b0d7c4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ed0:8"]]
- 00b0d7c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b0d7c4 bytes 08d30eb9
- 00b0d7c8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b0d7c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b0d7c8 bytes 690000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1227c2ea7399112453eec4b35ec070"></a>

### [`00b0db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md) → [`00b6dec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee70.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5b920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b920.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.34% / 新版 75.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `call_target` 2件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6dee4",
      "incomplete_value": true,
      "site": "00b6dee4",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dbb0",
      "incomplete_value": true,
      "site": "00b0dbb0",
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
            "const:ed0:8"
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
      "definition_site": "00b6df48",
      "incomplete_value": true,
      "site": "00b6df48",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dc14",
      "incomplete_value": true,
      "site": "00b0dc14",
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
            "const:ef0:8"
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
      "definition_site": "00b6df70",
      "incomplete_value": true,
      "site": "00b6df70",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dc3c",
      "incomplete_value": true,
      "site": "00b0dc3c",
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
            "const:f10:8"
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
      "00b6ded8",
      "READ",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6dee4",
      "WRITE",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6def0",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6ded8",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6dee4",
      "WRITE",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6def0",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dbb0) · [`00b0dbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dbe0) · [`00b0dc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dc10)
- 新版 [`00b6dee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6dee4) · [`00b6df14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6df14) · [`00b6df44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6df44)

~~~diff
- 00b0dbb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
- 00b0dbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6dee4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
+ 00b6dee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b0dbb0 bytes 09d10eb9
+ 00b6dee4 bytes 09910db9
- 00b0dbe0 ["INT_ADD", "register:40f0:8", ["const:b0dbe0:8", "const:4:8"]]
- 00b0dbe0 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00b6df14 ["INT_ADD", "register:40f0:8", ["const:b6df14:8", "const:4:8"]]
+ 00b6df14 ["CALL", null, ["callee:00c5ae40:8"]]
- 00b0dbe0 bytes f8410394
+ 00b6df14 bytes cbb30394
- 00b0dc10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0dc10 ["INT_ADD", "register:40f0:8", ["const:b0dc10:8", "const:4:8"]]
- 00b0dc10 ["CALLIND", null, ["register:0:8"]]
+ 00b6df44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6df44 ["INT_ADD", "register:40f0:8", ["const:b6df44:8", "const:4:8"]]
+ 00b6df44 ["CALLIND", null, ["register:0:8"]]
- 00b0dc10 bytes 00013fd6
+ 00b6df44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8917a9171a22123a0b869d5d54dd9d1c"></a>

### [`00b0dcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md) → [`00b6dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf070.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md)
- 新版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb20.md) · 呼出先 4件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 54.55% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0dde8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ddec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e11c"
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
      "00b6dffc",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e010",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0dd04"
      ]
    ],
    [
      "unmatched:00b0dcf8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dffc",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e010",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e038"
      ]
    ],
    [
      "00b6e02c",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dcd4) · [`00b0dd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dd00) · [`00b0dd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dd18)
- 新版 [`00b6e008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md#insn-00b6e008) · [`00b6e04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md#insn-00b6e04c)

~~~diff
- 00b0dcd4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b0dcd4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6e008 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6e008 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b0dcd4 bytes a80000b4
+ 00b6e008 bytes a80000b4
- 00b0dd00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b0dd00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b0dd00 bytes 09ffff35
- 00b0dd18 ["INT_ADD", "register:40f0:8", ["const:b0dd18:8", "const:4:8"]]
- 00b0dd18 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00b6e04c ["INT_ADD", "register:40f0:8", ["const:b6e04c:8", "const:4:8"]]
+ 00b6e04c ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b0dd18 bytes 0a400394
+ 00b6e04c bytes d5b10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f52913bb445e47e95470d38ab4216552"></a>

### [`00b0de00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md) → [`00b6e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b0df74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00b6e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e16c",
      "incomplete_value": true,
      "site": "00b6e17c",
      "value": [
        "LOAD",
        "8",
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0de38",
      "incomplete_value": true,
      "site": "00b0de48",
      "value": [
        "LOAD",
        "8",
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e170",
      "incomplete_value": true,
      "site": "00b6e17c",
      "value": [
        "LOAD",
        "8",
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0de3c",
      "incomplete_value": true,
      "site": "00b0de48",
      "value": [
        "LOAD",
        "8",
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
                "const:f08:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e1b0",
      "incomplete_value": true,
      "site": "00b6e1b4",
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
      "definition_site": "00b0de7c",
      "incomplete_value": true,
      "site": "00b0de80",
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0de38",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0de3c",
      "READ",
      [
        "storage",
        "010a0f08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1a8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e16c",
      "READ",
      [
        "storage",
        "01125db8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e170",
      "READ",
      [
        "storage",
        "01125dc8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1a8",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de48) · [`00b0de80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de80) · [`00b0de9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de9c)
- 新版 [`00b6e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e17c) · [`00b6e1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e1b4) · [`00b6e1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e1d0)

~~~diff
- 00b0de48 ["INT_ADD", "register:40f0:8", ["const:b0de48:8", "const:4:8"]]
- 00b0de48 ["CALL", null, ["callee:00c5bb40:8"]]
+ 00b6e17c ["INT_ADD", "register:40f0:8", ["const:b6e17c:8", "const:4:8"]]
+ 00b6e17c ["CALL", null, ["callee:00c5bb40:8"]]
- 00b0de48 bytes 92440394
+ 00b6e17c bytes 71b60394
- 00b0de80 ["INT_ADD", "register:40f0:8", ["const:b0de80:8", "const:4:8"]]
- 00b0de80 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b6e1b4 ["INT_ADD", "register:40f0:8", ["const:b6e1b4:8", "const:4:8"]]
+ 00b6e1b4 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b0de80 bytes 40400394
+ 00b6e1b4 bytes 13b20394
- 00b0de9c ["INT_ADD", "register:40f0:8", ["const:b0de9c:8", "const:4:8"]]
- 00b0de9c ["CALL", null, ["callee:00c5a9a0:8"]]
+ 00b6e1d0 ["INT_ADD", "register:40f0:8", ["const:b6e1d0:8", "const:4:8"]]
+ 00b6e1d0 ["CALL", null, ["callee:00c5a9a0:8"]]
- 00b0de9c bytes d9430394
+ 00b6e1d0 bytes f4b10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613f4461743823f7bae3402289694be1"></a>

### [`00b0df74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md) → [`00b6e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee60.md) · 呼出先 14件 [`00b0de00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b910.md) · 呼出先 14件 [`00b6e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 84.67% / 新版 84.67%

CFGの説明率　旧版 28.21% / 新版 40.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0dfb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0dfcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e394",
      "incomplete_value": true,
      "site": "00b6e394",
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
      "definition_site": "00b0e060",
      "incomplete_value": true,
      "site": "00b0e060",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0dfa8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0dfb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e2f0"
      ]
    ],
    [
      "unmatched:00b0dfc8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e2dc",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e2f0"
      ]
    ],
    [
      "00b6e2fc",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0dfb0) · [`00b0dfc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0dfc4) · [`00b0dfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0dfcc)
- 新版 [`00b6e2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md#insn-00b6e2f8)

~~~diff
- 00b0dfb0 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b0dfb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b0dfb0 bytes 770000b4
- 00b0dfc4 ["INT_ADD", "register:40f0:8", ["const:b0dfc4:8", "const:4:8"]]
- 00b0dfc4 ["CALL", null, ["callee:00c5b900:8"]]
+ 00b6e2f8 ["INT_ADD", "register:40f0:8", ["const:b6e2f8:8", "const:4:8"]]
+ 00b6e2f8 ["CALL", null, ["callee:00c5b900:8"]]
- 00b0dfc4 bytes a3430394
+ 00b6e2f8 bytes 82b50394
- 00b0dfcc ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b0dfcc ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00b0dfcc bytes b70c00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a0d0f87ab12a0df327ee3ca2dfcb461"></a>

### [`00b0e198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e198.md) → [`00b6e4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e4cc.md) _ZN20google_play_services23MakeAvailableLastResultEv

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf080.md) · 呼出先 6件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)
- 新版 呼出元 1件 [`00c5bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb30.md) · 呼出先 6件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e1e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e514"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e1b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e4e0",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0e1b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e534"
      ]
    ],
    [
      "unmatched:00b0e1d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00b6e4e0",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e534"
      ]
    ],
    [
      "00b6e50c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e198.md#insn-00b0e1b4) · [`00b0e1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e198.md#insn-00b0e1d8) · [`00b0e1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e198.md#insn-00b0e1e0)

~~~diff
- 00b0e1b4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b0e1b4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b0e1b4 bytes 750200b4
- 00b0e1d8 ["INT_ADD", "register:40f0:8", ["const:b0e1d8:8", "const:4:8"]]
- 00b0e1d8 ["CALL", null, ["ram:bdde10:8"]]
- 00b0e1d8 bytes 0e3f0394
- 00b0e1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b0e1e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0e1e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b0e1e0 bytes 7f1600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7c165062c2836fcab09af0096954e6"></a>

### [`00b0e22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e22c.md) → [`00b6e560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e560.md) FUN_00b6e560

採用 · 移動量 `+0x60334` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 58.33% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e58c",
      "incomplete_value": true,
      "site": "00b6e58c",
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
      "definition_site": "00b0e258",
      "incomplete_value": true,
      "site": "00b0e258",
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
      "definition_site": "00b6e5e8",
      "incomplete_value": true,
      "site": "00b6e5f0",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00b6e5e4",
      "incomplete_value": true,
      "site": "00b6e5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e588",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e608",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00b6e588",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e608",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e22c.md#insn-00b0e258) · [`00b0e2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e22c.md#insn-00b0e2bc) · [`00b0e2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e22c.md#insn-00b0e2d4)
- 新版 [`00b6e58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e560.md#insn-00b6e58c) · [`00b6e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e560.md#insn-00b6e5f0) · [`00b6e608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e560.md#insn-00b6e608)

~~~diff
- 00b0e258 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b0e258 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b6e58c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b6e58c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b0e258 bytes 140400b4
+ 00b6e58c bytes 140400b4
- 00b0e2bc ["INT_ADD", "register:40f0:8", ["const:b0e2bc:8", "const:4:8"]]
- 00b0e2bc ["CALL", null, ["callee:00c5a9a0:8"]]
+ 00b6e5f0 ["INT_ADD", "register:40f0:8", ["const:b6e5f0:8", "const:4:8"]]
+ 00b6e5f0 ["CALL", null, ["callee:00c5a9a0:8"]]
- 00b0e2bc bytes d1420394
+ 00b6e5f0 bytes ecb00394
- 00b0e2d4 ["INT_ADD", "register:40f0:8", ["const:b0e2d4:8", "const:4:8"]]
- 00b0e2d4 ["CALL", null, ["ram:bddc40:8"]]
+ 00b6e608 ["INT_ADD", "register:40f0:8", ["const:b6e608:8", "const:4:8"]]
+ 00b6e608 ["CALL", null, ["ram:c5a690:8"]]
- 00b0e2d4 bytes 5b3e0394
+ 00b6e608 bytes 22b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1519037af5a695e91edb60dcdc904d"></a>

### [`00b0e888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md) → [`00b6e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e644.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fdbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md)
- 新版 呼出元 1件 [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.23% / 新版 74.23%

CFGの説明率　旧版 48.98% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ea10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ea14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0e8b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0e8bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0e8cc"
      ]
    ],
    [
      "unmatched:00b0e8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0e8d4"
      ]
    ]
  ],
  "added": [
    [
      "00b6e670",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b6e678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e688"
      ]
    ],
    [
      "00b6e680",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e8b4) · [`00b0e8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e8bc) · [`00b0e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e8c4)

~~~diff
- 00b0e8b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b0e8b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b0e8b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0e8b4 bytes a8831cf8
- 00b0e8bc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0e8bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0e8bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0e8bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0e8bc bytes 88000037
- 00b0e8c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b0e8c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b0e8c4 bytes 880000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb1551cfc268a53878b0ce99e60265f7"></a>

### [`00b0eb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md) → [`00b6e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x5fdbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6e92c",
      "incomplete_value": true,
      "site": "00b6e940",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0eb70",
      "incomplete_value": true,
      "site": "00b0eb84",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6e924",
      "incomplete_value": true,
      "site": "00b6e944",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0eb68",
      "incomplete_value": true,
      "site": "00b0eb88",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6e9b4",
      "incomplete_value": true,
      "site": "00b6e9c0",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0ebf8",
      "incomplete_value": true,
      "site": "00b0ec04",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e904",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e908",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e940",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6e904",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e908",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e940",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0ebd0) · [`00b0ec40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0ec40) · [`00b0eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0eb38)
- 新版 [`00b6e98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e98c) · [`00b6e9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e9fc) · [`00b6e8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e8f4)

~~~diff
- 00b0ebd0 ["INT_ADD", "register:40f0:8", ["const:b0ebd0:8", "const:4:8"]]
- 00b0ebd0 ["CALL", null, ["ram:bdd950:8"]]
+ 00b6e98c ["INT_ADD", "register:40f0:8", ["const:b6e98c:8", "const:4:8"]]
+ 00b6e98c ["CALL", null, ["ram:c5a3a0:8"]]
- 00b0ebd0 bytes 603b0394
+ 00b6e98c bytes 85ae0394
- 00b0ec40 ["INT_ADD", "register:40f0:8", ["const:b0ec40:8", "const:4:8"]]
- 00b0ec40 ["CALL", null, ["ram:bdb440:8"]]
+ 00b6e9fc ["INT_ADD", "register:40f0:8", ["const:b6e9fc:8", "const:4:8"]]
+ 00b6e9fc ["CALL", null, ["ram:c57e90:8"]]
- 00b0ec40 bytes 00320394
+ 00b6e9fc bytes 25a50394
- 00b0eb38 ["COPY", "register:40d0:8", ["const:c1a000:8"]]
+ 00b6e8f4 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
- 00b0eb38 bytes 7a080090
+ 00b6e8f4 bytes 7a090090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1279f4756bb41faa4439aba1d2d2cc2c"></a>

### [`00b0ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ec80.md) → [`00b6ea3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ea3c.md) _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x5fdbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1c0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00c5bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc00.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ece8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ecec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ecf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0ecb0",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0ecb4",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0ece8",
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
      "00b6ea6c",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ea70",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b6eaa4",
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

- 旧版 [`00b0ece8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ec80.md#insn-00b0ece8) · [`00b0ecec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ec80.md#insn-00b0ecec) · [`00b0ecf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ec80.md#insn-00b0ecf0)

~~~diff
- 00b0ece8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b0ece8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b0ece8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0ece8 bytes a9031af8
- 00b0ecec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b0ecec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0ecec bytes e84b00f9
- 00b0ecf0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0ecf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b0ecf0 bytes fb1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45f9661fceb64c4778ed4e4d07c15be"></a>

### [`00b0ede8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ede8.md) → [`00b6eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_

採用 · 移動量 `+0x5fdbc` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 63.64% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ede8.md#insn-00b0ee14) · [`00b0ee34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ede8.md#insn-00b0ee34) · [`00b0ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ede8.md#insn-00b0ee54)
- 新版 [`00b6ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ebd0) · [`00b6ebf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ebf0) · [`00b6ec10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md#insn-00b6ec10)

~~~diff
- 00b0ee14 ["INT_ADD", "register:40f0:8", ["const:b0ee14:8", "const:4:8"]]
- 00b0ee14 ["CALL", null, ["callee:00c57be0:8"]]
+ 00b6ebd0 ["INT_ADD", "register:40f0:8", ["const:b6ebd0:8", "const:4:8"]]
+ 00b6ebd0 ["CALL", null, ["callee:00c57be0:8"]]
- 00b0ee14 bytes df300394
+ 00b6ebd0 bytes 04a40394
- 00b0ee34 ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
+ 00b6ebf0 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b0ee34 bytes 82040054
+ 00b6ebf0 bytes 82040054
- 00b0ee54 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b0ee54 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b6ec10 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b6ec10 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0ee54 bytes 960100b5
+ 00b6ec10 bytes 960100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e99b3fc7b47adf9db629f1c41c28db6"></a>

### [`00b0eec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eec8.md) → [`00b6ec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fdbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)

変更の種類 branch_condition_or_target, branch_count, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count

命令の説明率　旧版 82.14% / 新版 71.88%

CFGの説明率　旧版 40.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_argument_candidate` 1件, `store_count` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0eeec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6ec9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6ecdc"
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
      "unmatched:00b0eee8",
      "PARAM",
      [
        "storage",
        "0029153b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0eeec",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b6eccc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ece0"
      ]
    ]
  ],
  "added": [
    [
      "00b6ec9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b6eca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ece0"
      ]
    ],
    [
      "00b6ecb0",
      "PARAM",
      [
        "storage",
        "002a0adf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0eeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eec8.md#insn-00b0eeec) · [`00b0eef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eec8.md#insn-00b0eef4)
- 新版 [`00b6ecb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md#insn-00b6ecb8) · [`00b6ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md#insn-00b6ec9c)

~~~diff
- 00b0eeec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b0eeec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0eeec bytes e80f00f9
- 00b0eef4 ["INT_ADD", "register:40f0:8", ["const:b0eef4:8", "const:4:8"]]
- 00b0eef4 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00b6ecb8 ["INT_ADD", "register:40f0:8", ["const:b6ecb8:8", "const:4:8"]]
+ 00b6ecb8 ["CALL", null, ["callee:00c57cb0:8"]]
- 00b0eef4 bytes db300394
+ 00b6ecb8 bytes fea30394
+ 00b6ec9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 00b6ec9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b6ec9c bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cf8e3f5a79f9b85f2d8bd9f742890ff"></a>

### [`00b0ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ef38.md) → [`00b6ed04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed04.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fdcc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ef3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ef40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ef40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0ef3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0ef40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0ef44",
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
      "00b6ed08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6ed0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6ed10",
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

- 旧版 [`00b0ef3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ef38.md#insn-00b0ef3c) · [`00b0ef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ef38.md#insn-00b0ef40) · [`00b0ef44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0ef38.md#insn-00b0ef44)

~~~diff
- 00b0ef3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0ef3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0ef3c bytes f51300f9
- 00b0ef40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0ef40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0ef40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b0ef40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0ef40 bytes f44f03a9
- 00b0ef44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0ef44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0ef44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b0ef44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0ef44 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014fd8fcee2756a2dfdc005a5278506b"></a>

### [`00b0efbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md) → [`00b6ed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0x5fdcc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7f0.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 1件 [`00c5c120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c120.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.12% / 新版 83.12%

CFGの説明率　旧版 55.00% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0efe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6edb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0efec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0efe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0efec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5bbe0"
      ]
    ],
    [
      "unmatched:00b0eff4",
      "PARAM",
      [
        "storage",
        "002a3e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6edb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b6edb8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5bbe0"
      ]
    ],
    [
      "00b6edc0",
      "PARAM",
      [
        "storage",
        "002c1bb8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0efe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0efe4) · [`00b0efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0efec) · [`00b0f004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0f004)
- 新版 [`00b6edd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md#insn-00b6edd0)

~~~diff
- 00b0efe4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b0efe4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b0efe4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0efe4 bytes a8831df8
- 00b0efec ["INT_ADD", "register:40f0:8", ["const:b0efec:8", "const:4:8"]]
- 00b0efec ["CALL", null, ["callee:00c5bbe0:8"]]
- 00b0efec bytes 6d400394
- 00b0f004 ["INT_ADD", "register:40f0:8", ["const:b0f004:8", "const:4:8"]]
- 00b0f004 ["CALL", null, ["callee:00c58bd0:8"]]
+ 00b6edd0 ["INT_ADD", "register:40f0:8", ["const:b6edd0:8", "const:4:8"]]
+ 00b6edd0 ["CALL", null, ["callee:00c58bd0:8"]]
- 00b0f004 bytes 5f340394
+ 00b6edd0 bytes 80a70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-979e2abbc6b9ee99f44164ea44ca260b"></a>

### [`00b0f0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f0f0.md) → [`00b6ef90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ef90.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x5fea0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5c640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c640.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 7.00% / 新版 8.05%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `call_count` 4件, `store_count` 10件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f0f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f0f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f0f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f0f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f0f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f0fc",
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
      "00b6ef94",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b6ef98",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6ef9c",
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

- 旧版 [`00b0f0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f0f0.md#insn-00b0f0f4) · [`00b0f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f0f0.md#insn-00b0f0f8) · [`00b0f0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f0f0.md#insn-00b0f0fc)

~~~diff
- 00b0f0f4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b0f0f4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b0f0f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b0f0f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f0f4 bytes fc6f06a9
- 00b0f0f8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b0f0f8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b0f0f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b0f0f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f0f8 bytes fa6707a9
- 00b0f0fc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b0f0fc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b0f0fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b0f0fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f0fc bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd1d040f69cd6c4e6739e3904fdf2ff6"></a>

### [`00b0f45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md) → [`00b6f294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0x5fe38` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf790.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c5c0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0c0.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.16% / 新版 88.71%

CFGの説明率　旧版 59.38% / 新版 65.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 1件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6f4cc",
      "incomplete_value": true,
      "site": "00b6f4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f688",
      "incomplete_value": true,
      "site": "00b0f688",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f4e8",
      "PARAM",
      [
        "storage",
        "002ad407",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0f508",
      "PARAM",
      [
        "storage",
        "002932cb",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0f548",
      "PARAM",
      [
        "storage",
        "00291545",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f320",
      "PARAM",
      [
        "storage",
        "002be64c",
        null,
        "string"
      ]
    ],
    [
      "00b6f340",
      "PARAM",
      [
        "storage",
        "002a2a33",
        null,
        "string"
      ]
    ],
    [
      "00b6f380",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f4f8) · [`00b0f524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f524) · [`00b0f550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f550)
- 新版 [`00b6f330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f330) · [`00b6f35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f35c) · [`00b6f388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f388)

~~~diff
- 00b0f4f8 ["INT_ADD", "register:40f0:8", ["const:b0f4f8:8", "const:4:8"]]
- 00b0f4f8 ["CALL", null, ["callee:00c58bd0:8"]]
+ 00b6f330 ["INT_ADD", "register:40f0:8", ["const:b6f330:8", "const:4:8"]]
+ 00b6f330 ["CALL", null, ["callee:00c58bd0:8"]]
- 00b0f4f8 bytes 22330394
+ 00b6f330 bytes 28a60394
- 00b0f524 ["INT_ADD", "register:40f0:8", ["const:b0f524:8", "const:4:8"]]
- 00b0f524 ["CALL", null, ["callee:00c57b80:8"]]
+ 00b6f35c ["INT_ADD", "register:40f0:8", ["const:b6f35c:8", "const:4:8"]]
+ 00b6f35c ["CALL", null, ["callee:00c57b80:8"]]
- 00b0f524 bytes 032f0394
+ 00b6f35c bytes 09a20394
- 00b0f550 ["INT_ADD", "register:40f0:8", ["const:b0f550:8", "const:4:8"]]
- 00b0f550 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00b6f388 ["INT_ADD", "register:40f0:8", ["const:b6f388:8", "const:4:8"]]
+ 00b6f388 ["CALL", null, ["callee:00c57cb0:8"]]
- 00b0f550 bytes 442f0394
+ 00b6f388 bytes 4aa20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944d2acce99ea9dd74a6a25e006e1b60"></a>

### [`00b0f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md) → [`00b6f57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f57c.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0x5fe44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf910.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)
- 新版 呼出元 1件 [`00c5c250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c250.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 52.94% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f740",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f744",
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
      "00b6f580",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6f584",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6f588",
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

- 旧版 [`00b0f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f73c) · [`00b0f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f740) · [`00b0f744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f744)

~~~diff
- 00b0f73c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b0f73c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0f73c bytes f52300f9
- 00b0f740 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0f740 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0f740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b0f740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f740 bytes f44f05a9
- 00b0f744 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0f744 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0f744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b0f744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f744 bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5679108ca72bf75cc8a80c7f5c05d254"></a>

### [`00b0f84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md) → [`00b6f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0x5fe44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md) · 呼出先 13件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 1件 [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) · 呼出先 14件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_destination, store_value, unresolved_return_alignment

命令の説明率　旧版 25.71% / 新版 25.06%

CFGの説明率　旧版 16.18% / 新版 14.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 7件, `call_argument_candidate` 10件, `call_count` 2件, `store_count` 4件, `store_destination` 9件, `store_value` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f854"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f850",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f854",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f858",
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
      "00b6f694",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b6f698",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6f69c",
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

- 旧版 [`00b0f850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b0f850) · [`00b0f854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b0f854) · [`00b0f858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b0f858)

~~~diff
- 00b0f850 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b0f850 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b0f850 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b0f850 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f850 bytes fc6f07a9
- 00b0f854 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b0f854 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b0f854 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b0f854 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f854 bytes fa6708a9
- 00b0f858 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b0f858 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b0f858 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b0f858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f858 bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4628cb3d87803d69159fc72184655d0a"></a>

### [`00b10eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md) → [`00b70d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70d74.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0x5fec8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md) · 呼出先 12件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 87.32% / 新版 83.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10ec0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b10ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b10ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b10ed8",
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
      "00b70d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b70d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b70da0",
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

- 旧版 [`00b10ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10ebc) · [`00b10ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10ec0) · [`00b10ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10ed8)

~~~diff
- 00b10ebc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b10ebc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b10ebc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b10ebc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b10ebc bytes f44f0ea9
- 00b10ec0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b10ec0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b10ec0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b10ec0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b10ec0 bytes fd7b0fa9
- 00b10ed8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b10ed8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b10ed8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b10ed8 bytes a9831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5da2da73561b84d661afc71969e63fc9"></a>

### [`00b11264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11264.md) → [`00b7112c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7112c.md) _ZN11flatbuffers6Parser16ParseNamespacingEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0x5fec8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8c0.md) · 呼出先 4件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md) [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md)
- 新版 呼出元 1件 [`00c5c200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c200.md) · 呼出先 4件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 54.55% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b11264",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11268",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1126c",
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
      "00b7112c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b71130",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b71134",
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

- 旧版 [`00b11264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11264.md#insn-00b11264) · [`00b11268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11264.md#insn-00b11268) · [`00b1126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11264.md#insn-00b1126c)

~~~diff
- 00b11264 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b11264 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b11264 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b11264 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b11264 bytes fa67bba9
- 00b11268 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b11268 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b11268 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b11268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b11268 bytes f85f01a9
- 00b1126c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b1126c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b1126c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b1126c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1126c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb306f00717eed6850cc64ca2602c49"></a>

### [`00b1136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1136c.md) → [`00b71234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71234.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fec8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md) [`00bdfca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfca0.md)
- 新版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c050.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 3.33% / 新版 1.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 17件, `call_count` 4件, `store_count` 14件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11374"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b11370",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11374",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11378",
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
      "00b71238",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7123c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b71240",
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

- 旧版 [`00b11370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1136c.md#insn-00b11370) · [`00b11374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1136c.md#insn-00b11374) · [`00b11378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1136c.md#insn-00b11378)

~~~diff
- 00b11370 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b11370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b11370 bytes f91300f9
- 00b11374 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b11374 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b11374 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b11374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b11374 bytes f85f03a9
- 00b11378 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b11378 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b11378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b11378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b11378 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40e0779dba7c203dd719fa4f7baf08e"></a>

### [`00b114a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b114a8.md) → [`00b717e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b717e4.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0x6033c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf870.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1a0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 45.59% / 新版 58.49%

CFGの説明率　旧版 31.11% / 新版 37.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 5件, `call_count` 2件, `store_condition` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b114ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b114ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b114b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b114ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b114b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b114b4",
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
      "00b717e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b717ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b717f0",
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

- 旧版 [`00b114ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b114a8.md#insn-00b114ac) · [`00b114b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b114a8.md#insn-00b114b0) · [`00b114b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b114a8.md#insn-00b114b4)

~~~diff
- 00b114ac ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b114ac ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b114ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b114ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b114ac bytes fa6704a9
- 00b114b0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b114b0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b114b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b114b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b114b0 bytes f85f05a9
- 00b114b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b114b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b114b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b114b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b114b4 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4a811b59c8f72f3c7c2a35be889980"></a>

### [`00b116c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md) → [`00b7198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0x602c4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf920.md) · 呼出先 16件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c5c260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c260.md) · 呼出先 17件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_destination

命令の説明率　旧版 35.80% / 新版 39.46%

CFGの説明率　旧版 21.01% / 新版 24.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 7件, `call_argument_candidate` 3件, `call_count` 2件, `store_count` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b116fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11760"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b116fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11710",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdfc70"
      ]
    ],
    [
      "unmatched:00b11720",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6b0"
      ]
    ]
  ],
  "added": [
    [
      "00b719c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b719d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5c640"
      ]
    ],
    [
      "00b719e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b116fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b116fc) · [`00b11744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b11744) · [`00b11760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b11760)

~~~diff
- 00b116fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b116fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b116fc bytes e82700f9
- 00b11744 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:90:8"]]
- 00b11744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b11744 bytes 689200b9
- 00b11760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:80:8"]]
- 00b11760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b11760 bytes 684200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12ef5217895f770203dda79cac7ffc26"></a>

### [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) → [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0x6024c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) [`00bdfa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa30.md) · 呼出先 12件 [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) [`00c5c3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3d0.md) · 呼出先 12件 [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, unresolved_return_alignment

命令の説明率　旧版 41.68% / 新版 40.00%

CFGの説明率　旧版 20.75% / 新版 16.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 2件, `call_argument_candidate` 9件, `call_count` 1件, `store_condition` 1件, `store_count` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11ca0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b11c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b71e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b11c84"
      ]
    ],
    [
      "00b71e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b11ccc"
      ]
    ]
  ],
  "added": [
    [
      "00b71e54",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b71e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71ed0"
      ]
    ],
    [
      "00b71e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71f04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11c08) · [`00b11c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11c98) · [`00b11ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11ca0)

~~~diff
- 00b11c08 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b11c08 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b11c08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b11c08 bytes a9831bf8
- 00b11c98 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b11c98 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b11c98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b11c98 bytes 69060039
- 00b11ca0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b11ca0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b11ca0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b11ca0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b11ca0 bytes ff7f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83afa15eabb8ddcd3ec2cd77b31ec363"></a>

### [`00b12344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md) → [`00b725e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b725e0.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0x6029c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9e0.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 1件 [`00c5c380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c380.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, branch_count, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_call_alignment

命令の説明率　旧版 39.38% / 新版 35.39%

CFGの説明率　旧版 7.50% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_argument_candidate` 4件, `store_count` 1件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1234c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b12348",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1234c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b12350",
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
      "00b725e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b725e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b725ec",
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

- 旧版 [`00b12348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b12348) · [`00b1234c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b1234c) · [`00b12350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b12350)

~~~diff
- 00b12348 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b12348 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b12348 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b12348 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12348 bytes fc6f04a9
- 00b1234c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1234c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1234c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b1234c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1234c bytes fa6705a9
- 00b12350 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b12350 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b12350 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b12350 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12350 bytes f85f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e7d66f3ef04b337636fc759e72663d"></a>

### [`00b125c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b125c4.md) → [`00b728a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b728a8.md) _ZN11flatbuffers10InlineSizeERKNS_4TypeE

採用 · 移動量 `+0x602e4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf170.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf170.md)
- 新版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbb0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 65.85% / 新版 50.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b125f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12608"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12650"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b728d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b12604"
      ]
    ],
    [
      "unmatched:00b125f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b12638"
      ]
    ],
    [
      "unmatched:00b12600",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b12644"
      ]
    ]
  ],
  "added": [
    [
      "00b728d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b728e8"
      ]
    ],
    [
      "00b728dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72910"
      ]
    ],
    [
      "00b728e4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72958"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b125f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b125c4.md#insn-00b125f8) · [`00b12608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b125c4.md#insn-00b12608) · [`00b12650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b125c4.md#insn-00b12650)

~~~diff
- 00b125f8 ["INT_EQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
- 00b125f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b125f8 bytes 0a020034
- 00b12608 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b12608 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b12608 bytes 81010054
- 00b12650 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b12650 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b12650 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0792c43f683b174bf841deebc2dd18f1"></a>

### [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) → [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) _ZN11flatbuffers6Parser10ParseFieldERNS_9StructDefE

採用 · 移動量 `+0x60314` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf750.md) · 呼出先 26件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c5c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c070.md) · 呼出先 27件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, unresolved_return_alignment

命令の説明率　旧版 23.77% / 新版 14.17%

CFGの説明率　旧版 4.58% / 新版 2.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 149件, `call_argument_candidate` 15件, `call_count` 60件, `store_condition` 8件, `store_count` 170件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12828"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b12824",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b12828",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1282c",
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
      "00b72b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b72b3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b72b40",
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

- 旧版 [`00b12824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b12824) · [`00b12828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b12828) · [`00b1282c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b1282c)

~~~diff
- 00b12824 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b12824 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b12824 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b12824 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12824 bytes fc6f13a9
- 00b12828 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b12828 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b12828 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b12828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12828 bytes fa6714a9
- 00b1282c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1282c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1282c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b1282c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1282c bytes f85f15a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f40735800a5d27b0f8792db747d5e126"></a>

### [`00b13e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e04.md) → [`00b74fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b74/00b74fec.md) _ZNK11flatbuffers6Parser29SupportsAdvancedArrayFeaturesEv

採用 · 移動量 `+0x611e8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 20.00% / 新版 20.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b74ff8",
      "incomplete_value": true,
      "site": "00b74ffc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_AND",
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
      "definition_site": "00b13e10",
      "incomplete_value": true,
      "site": "00b13e14",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_AND",
              [
                "leaf",
                "const:0:8"
              ]
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


#### 変更候補の命令位置

- 旧版 [`00b13e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e04.md#insn-00b13e04) · [`00b13e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e04.md#insn-00b13e08)
- 新版 [`00b74fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b74/00b74fec.md#insn-00b74fec) · [`00b74ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b74/00b74fec.md#insn-00b74ff0)

~~~diff
- 00b13e04 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:460:8"]]
- 00b13e04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b74fec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:518:8"]]
+ 00b74fec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b13e04 bytes 083042f9
+ 00b74fec bytes 088c42f9
- 00b13e08 ["COPY", "register:4048:8", ["const:fffffffffffffa54:8"]]
+ 00b74ff0 ["COPY", "register:4048:8", ["const:ffffffffffffb854:8"]]
- 00b13e08 bytes 69b58092
+ 00b74ff0 bytes 69f58892
~~~


<a id="compare-eaaaa2ce9f6aee7203e5314252d103af"></a>

### [`00b13e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md) → [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) _ZN11flatbuffers6Parser16ParseSingleValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueEb

採用 · 移動量 `+0x611dc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8f0.md) · 呼出先 34件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c230.md) · 呼出先 35件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_destination, unresolved_return_alignment

命令の説明率　旧版 18.74% / 新版 17.38%

CFGの説明率　旧版 2.79% / 新版 2.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 24件, `call_argument_candidate` 12件, `call_count` 6件, `call_target` 1件, `store_count` 10件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13e44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b13e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b13e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b13e48",
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
      "00b7501c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b75020",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b75024",
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

- 旧版 [`00b13e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b13e40) · [`00b13e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b13e44) · [`00b13e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b13e48)

~~~diff
- 00b13e40 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b13e40 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b13e40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b13e40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13e40 bytes fc6f13a9
- 00b13e44 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b13e44 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b13e44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b13e44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13e44 bytes fa6714a9
- 00b13e48 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b13e48 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b13e48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b13e48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13e48 bytes f85f15a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b3649693e9dfedc438be9181aa1c69"></a>

### [`00b14ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md) → [`00b76614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x61740` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc20.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5e0.md) [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md)
- 新版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5f0.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5bdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdb0.md) [`00c5bdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 22.22% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14f4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14fd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b14f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b766cc"
      ]
    ],
    [
      "00b766c4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b14fbc"
      ]
    ],
    [
      "unmatched:00b14fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76720"
      ]
    ]
  ],
  "added": [
    [
      "00b7668c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b766cc"
      ]
    ],
    [
      "00b766c4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b766fc"
      ]
    ],
    [
      "00b76704",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76720"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b14f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md#insn-00b14f24) · [`00b14f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md#insn-00b14f4c) · [`00b14fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md#insn-00b14fc4)
- 新版 [`00b76664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md#insn-00b76664)

~~~diff
- 00b14f24 ["INT_ADD", "register:40f0:8", ["const:b14f24:8", "const:4:8"]]
- 00b14f24 ["CALL", null, ["callee:00c5bdc0:8"]]
+ 00b76664 ["INT_ADD", "register:40f0:8", ["const:b76664:8", "const:4:8"]]
+ 00b76664 ["CALL", null, ["callee:00c5bdc0:8"]]
- 00b14f24 bytes b3290394
+ 00b76664 bytes d7950394
- 00b14f4c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b14f4c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b14f4c bytes 03020054
- 00b14fc4 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00b14fc4 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a55fb00f2d69d1a1a0ea9c7e42e480b7"></a>

### [`00b1500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md) → [`00b76214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76214.md) _ZN11flatbuffers6Parser13ParseMetaDataEPNS_11SymbolTableINS_5ValueEEE

採用 · 移動量 `+0x61208` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf820.md) · 呼出先 13件 [`00613fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613fbc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c150.md) · 呼出先 13件 [`00639ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_count, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, unresolved_return_alignment

命令の説明率　旧版 65.26% / 新版 58.40%

CFGの説明率　旧版 27.38% / 新版 28.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `branch_value` 1件, `call_argument_candidate` 5件, `call_count` 5件, `store_condition` 2件, `store_count` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b15010",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15014",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15018",
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
      "00b76218",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7621c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b76220",
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

- 旧版 [`00b15010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b15010) · [`00b15014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b15014) · [`00b15018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b15018)

~~~diff
- 00b15010 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b15010 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b15010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b15010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15010 bytes fc6f07a9
- 00b15014 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b15014 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b15014 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b15014 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15014 bytes fa6708a9
- 00b15018 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b15018 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b15018 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b15018 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15018 bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4eff7f501452cad95eb33cd9ae7a8b"></a>

### [`00b15360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15360.md) → [`00b7674c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b7674c.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x613ec` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf220.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc60.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 10.91% / 新版 17.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15394"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b15378",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15394",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b153a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b153b0"
      ]
    ]
  ],
  "added": [
    [
      "00b76764",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b76780",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b7678c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7679c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15360.md#insn-00b15378) · [`00b15394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15360.md#insn-00b15394) · [`00b153a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15360.md#insn-00b153a0)

~~~diff
- 00b15378 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b15378 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b15378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b15378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15378 bytes fd7b06a9
- 00b15394 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b15394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b15394 bytes e80700f9
- 00b153a0 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b153a0 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b430bc3aed5a2cb7932461195509c6"></a>

### [`00b156c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md) → [`00b76f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76f54.md) _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x61894` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`00c5bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbf0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.12% / 新版 79.12%

CFGの説明率　旧版 22.22% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15730"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b157a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b156f4",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b156f8",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b15730",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b76f88",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b76f8c",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b76fc4",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b15730) · [`00b15734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b15734) · [`00b1577c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b1577c)

~~~diff
- 00b15730 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b15730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b15730 bytes e84b00f9
- 00b15734 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b15734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b15734 bytes fb1300f9
- 00b1577c ["INT_ADD", "register:40f0:8", ["const:b1577c:8", "const:4:8"]]
- 00b1577c ["CALL", null, ["ram:bdd950:8"]]
- 00b1577c bytes 75200394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc781d44289146ad1c6cb0c213793078"></a>

### [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) → [`00b780f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b780f8.md) _ZN11flatbuffers6Parser16SkipAnyJsonValueEv

採用 · 移動量 `+0x61870` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) [`00bdf900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf900.md) · 呼出先 9件 [`00b16888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 2件 [`00b780f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b780f8.md) [`00c5c240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c240.md) · 呼出先 9件 [`00b780f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b780f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, branch_count, call, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 6.96% / 新版 6.99%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 2件, `store_count` 5件, `unresolved_call_alignment` 16件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1688c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16890",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16894",
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
      "00b780fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b78100",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b78104",
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

- 旧版 [`00b1688c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md#insn-00b1688c) · [`00b16890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md#insn-00b16890) · [`00b16894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16888.md#insn-00b16894)

~~~diff
- 00b1688c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1688c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1688c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b1688c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1688c bytes fc6f03a9
- 00b16890 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b16890 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b16890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b16890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16890 bytes fa6704a9
- 00b16894 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b16894 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b16894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b16894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16894 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d1a740a70774bc0338546faaebcb50d"></a>

### [`00b17120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17120.md) → [`00b7899c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b7899c.md) _ZNK11flatbuffers7EnumDef13ReverseLookupElb

採用 · 移動量 `+0x6187c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b789b4",
      "incomplete_value": true,
      "site": "00b789b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "00b17138",
      "incomplete_value": true,
      "site": "00b1713c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "00b789c4",
      "incomplete_value": true,
      "site": "00b789c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:4008:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b17148",
      "incomplete_value": true,
      "site": "00b1714c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:4008:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b17120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17120.md#insn-00b17120) · [`00b17128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17120.md#insn-00b17128) · [`00b17144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17120.md#insn-00b17144)
- 新版 [`00b7899c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b7899c.md#insn-00b7899c) · [`00b789a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b7899c.md#insn-00b789a4) · [`00b789c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b7899c.md#insn-00b789c0)

~~~diff
- 00b17120 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:94:8"]]
- 00b17120 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b17120 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b7899c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:a0:8"]]
+ 00b7899c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b7899c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b17120 bytes 08504239
+ 00b7899c bytes 08804239
- 00b17128 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d0:8"]]
- 00b17128 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b17128 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b17128 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
+ 00b789a4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e0:8"]]
+ 00b789a4 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b789a4 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
+ 00b789a4 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b17128 bytes 09204da9
+ 00b789a4 bytes 09204ea9
- 00b17144 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:50:8"]]
- 00b17144 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b789c0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:80:8"]]
+ 00b789c0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b17144 bytes 0a2840f9
+ 00b789c0 bytes 0a4040f9
~~~


<a id="compare-7ad2d2d04562f5a7d6072690f2c8be60"></a>

### [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) → [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) _ZN11flatbuffers6Parser10ParseTableERKNS_9StructDefEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEPj

採用 · 移動量 `+0x6187c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf760.md) · 呼出先 37件 [`00b3fccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fccc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c080.md) · 呼出先 41件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, unresolved_return_alignment

命令の説明率　旧版 8.02% / 新版 6.10%

CFGの説明率　旧版 1.43% / 新版 1.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 95件, `call_argument_candidate` 6件, `call_count` 23件, `store_condition` 5件, `store_count` 29件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b17164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b17164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b17168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b17164",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b17168",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1716c",
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
      "00b789e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b789e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b789e8",
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

- 旧版 [`00b17164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b17164) · [`00b17168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b17168) · [`00b1716c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b1716c)

~~~diff
- 00b17164 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b17164 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b17164 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b17164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b17164 bytes fc6f0ea9
- 00b17168 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b17168 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b17168 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b17168 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b17168 bytes fa670fa9
- 00b1716c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1716c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1716c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b1716c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1716c bytes f85f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87bfb616828a3216a323131cd2ae7436"></a>

### [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) → [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) _ZN11flatbuffers6Parser11ParseVectorERKNS_4TypeEPjPNS_8FieldDefEm

採用 · 移動量 `+0x62134` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7b0.md) · 呼出先 32件 [`00b1cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md) [`00b1ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md) [`00b40b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c5c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0e0.md) · 呼出先 31件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 1.83% / 新版 1.16%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 38件, `call_count` 8件, `store_count` 35件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b18d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b18d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b18d24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b18d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b18d24",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b18d28",
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
      "00b7ae54",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7ae58",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b7ae5c",
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

- 旧版 [`00b18d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b18d20) · [`00b18d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b18d24) · [`00b18d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b18d28)

~~~diff
- 00b18d20 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b18d20 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b18d20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b18d20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b18d20 bytes fc6f07a9
- 00b18d24 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b18d24 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b18d24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b18d24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b18d24 bytes fa6708a9
- 00b18d28 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b18d28 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b18d28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b18d28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b18d28 bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2cd5b1f3f59e582636336c3bf3d4ac0"></a>

### [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) → [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) _ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE

採用 · 移動量 `+0x6262c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf740.md) · 呼出先 32件 [`00b410bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b410bc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c060.md) · 呼出先 31件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 8.86% / 新版 5.77%

CFGの説明率　旧版 2.73% / 新版 1.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 29件, `call_argument_candidate` 1件, `call_count` 8件, `store_count` 37件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b195ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b195ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b195b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b195ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b195b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b195b4",
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
      "00b7bbd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7bbdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b7bbe0",
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

- 旧版 [`00b195ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md#insn-00b195ac) · [`00b195b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md#insn-00b195b0) · [`00b195b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md#insn-00b195b4)

~~~diff
- 00b195ac ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b195ac ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b195ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b195ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b195ac bytes fc6f10a9
- 00b195b0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b195b0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b195b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b195b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b195b0 bytes fa6711a9
- 00b195b4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b195b4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b195b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b195b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b195b4 bytes f85f12a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1520514be334f391fd98ff32d6c086c6"></a>

### [`00b19c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md) → [`00b7c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7c620.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0x629c4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa10.md) · 呼出先 11件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md) [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md)
- 新版 呼出元 1件 [`00c5c3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3b0.md) · 呼出先 11件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md) [`00c5bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 38.14% / 新版 38.14%

CFGの説明率　旧版 17.78% / 新版 17.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19c94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b19c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b19c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b19c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7c650",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b7c658",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7c65c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b19c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19c8c) · [`00b19c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19c94) · [`00b19c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19c98)

~~~diff
- 00b19c8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b19c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b19c8c bytes e80f00f9
- 00b19c94 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b19c94 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b19c94 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b19c94 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b19c94 bytes ff7f00a9
- 00b19c98 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b19c98 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00b19c98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b19c98 bytes e8030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54e4701b30716f69beb7f14a62281725"></a>

### [`00b1cfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md) → [`00b7ff48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7ff48.md) _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE

採用 · 移動量 `+0x62f60` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf950.md) · 呼出先 21件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c5c2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2b0.md) · 呼出先 20件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, store_destination, unresolved_return_alignment

命令の説明率　旧版 17.99% / 新版 21.30%

CFGの説明率　旧版 11.27% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 3件, `call_argument_candidate` 5件, `call_count` 3件, `store_condition` 1件, `store_count` 43件, `store_destination` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d08c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1d02c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1d060"
      ]
    ],
    [
      "unmatched:00b1d048",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdf800"
      ]
    ],
    [
      "00b7ffc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1d4d0"
      ]
    ]
  ],
  "added": [
    [
      "00b7ff8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7ffc8"
      ]
    ],
    [
      "00b7ff94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b80030"
      ]
    ],
    [
      "00b7ffb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5c130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d088) · [`00b1d08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d08c) · [`00b1d0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d0a4)

~~~diff
- 00b1d088 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b1d088 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b1d088 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b1d088 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b1d088 bytes ff7f01a9
- 00b1d08c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b1d08c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b1d08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b1d08c bytes ff0700f9
- 00b1d0a4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b1d0a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b1d0a4 bytes f70300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-452241d2d25a251b2e8c2a86abdaa3ec"></a>

### [`00b1d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d508.md) → [`00b8039c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b8039c.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0x62e94` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf160.md) · 呼出先 2件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md)
- 新版 呼出元 1件 [`00c5bba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bba0.md) · 呼出先 2件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc30.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_destination

命令の説明率　旧版 32.52% / 新版 20.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 12件, `call_count` 7件, `store_count` 19件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d5dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b803c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1d734"
      ]
    ],
    [
      "unmatched:00b1d554",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5acb0"
      ]
    ],
    [
      "unmatched:00b1d578",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5acb0"
      ]
    ]
  ],
  "added": [
    [
      "00b803c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b80710"
      ]
    ],
    [
      "00b803e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5acb0"
      ]
    ],
    [
      "00b8040c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5acb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d508.md#insn-00b1d528) · [`00b1d588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d508.md#insn-00b1d588) · [`00b1d5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d508.md#insn-00b1d5dc)

~~~diff
- 00b1d528 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:9:8"]]
- 00b1d528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1d528 bytes 0090803c
- 00b1d588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b1d588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b1d588 bytes 685200b9
- 00b1d5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:88:8"]]
- 00b1d5dc ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b1d5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b1d5dc bytes 68120179
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d168f6690f288cf462ae9b29c8ea350"></a>

### [`00b1d794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d794.md) → [`00b807c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0x6302c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf060.md) · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf880.md) [`00bdf940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf940.md) [`00bdfa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa20.md) [`00bdfb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb30.md)
- 新版 呼出元 1件 [`00c5bb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb10.md) · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1b0.md) [`00c5c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2a0.md) [`00c5c3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3c0.md) [`00c5c4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80818",
      "incomplete_value": true,
      "site": "00b8081c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1d7ec",
      "incomplete_value": true,
      "site": "00b1d7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d794.md#insn-00b1d7f0) · [`00b1d7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d794.md#insn-00b1d7b8) · [`00b1d7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d794.md#insn-00b1d7cc)
- 新版 [`00b8081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b8081c) · [`00b807e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b807e4) · [`00b807f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b807c0.md#insn-00b807f8)

~~~diff
- 00b1d7f0 ["INT_ADD", "register:40f0:8", ["const:b1d7f0:8", "const:4:8"]]
- 00b1d7f0 ["CALL", null, ["callee:00c5c2a0:8"]]
+ 00b8081c ["INT_ADD", "register:40f0:8", ["const:b8081c:8", "const:4:8"]]
+ 00b8081c ["CALL", null, ["callee:00c5c2a0:8"]]
- 00b1d7f0 bytes 54080394
+ 00b8081c bytes a16e0394
- 00b1d7b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2d8:8"]]
- 00b1d7b8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b1d7b8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b807e4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:301:8"]]
+ 00b807e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b807e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b1d7b8 bytes 08604b39
+ 00b807e4 bytes 08044c39
- 00b1d7cc ["INT_ADD", "register:40f0:8", ["const:b1d7cc:8", "const:4:8"]]
- 00b1d7cc ["CALL", null, ["callee:00c5c1b0:8"]]
+ 00b807f8 ["INT_ADD", "register:40f0:8", ["const:b807f8:8", "const:4:8"]]
+ 00b807f8 ["CALL", null, ["callee:00c5c1b0:8"]]
- 00b1d7cc bytes 2d080394
+ 00b807f8 bytes 6e6e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673fa0a20d3a5de8c9ba40357075a9c7"></a>

### [`00b1d854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md) → [`00b809a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b809a4.md) _ZN11flatbuffers6Parser19ParseEnumFromStringERKNS_4TypeEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x63150` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf930.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c5c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c290.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_value, unresolved_return_alignment

命令の説明率　旧版 28.75% / 新版 31.76%

CFGの説明率　旧版 15.25% / 新版 18.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 5件, `call_argument_candidate` 4件, `call_count` 2件, `store_count` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d85c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1d858",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1d85c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1d860",
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
      "00b809a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b809ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b809b0",
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

- 旧版 [`00b1d858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1d858) · [`00b1d85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1d85c) · [`00b1d860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1d860)

~~~diff
- 00b1d858 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1d858 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1d858 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00b1d858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1d858 bytes fc6f0ca9
- 00b1d85c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1d85c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1d85c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b1d85c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1d85c bytes fa670da9
- 00b1d860 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1d860 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1d860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b1d860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1d860 bytes f85f0ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4192663c8c2145632194d0194b5f34a5"></a>

### [`00b1dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md) → [`00b7f76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f76c.md) _ZN11flatbuffers11NumToStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x619fc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1d0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00c5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc10.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dde0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1de54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1dda0",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1dda4",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1dddc",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7f79c",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f7a0",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f7d8",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1dddc) · [`00b1dde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1dde0) · [`00b1de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1de28)

~~~diff
- 00b1dddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b1dddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1dddc bytes e84b00f9
- 00b1dde0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b1dde0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b1dde0 bytes fb1300f9
- 00b1de28 ["INT_ADD", "register:40f0:8", ["const:b1de28:8", "const:4:8"]]
- 00b1de28 ["CALL", null, ["ram:bdd950:8"]]
- 00b1de28 bytes cafe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edb400fdf703585a2fe8b9e66a9f1a74"></a>

### [`00b1ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md) → [`00b80e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80e44.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x62f6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1e0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`00c5bc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc20.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1df0c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1df10",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1df48",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b80e78",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b80e7c",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b80eb4",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1df48) · [`00b1df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1df4c) · [`00b1df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1df50)

~~~diff
- 00b1df48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b1df48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1df48 bytes e84b00f9
- 00b1df4c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b1df4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b1df4c bytes fb1300f9
- 00b1df50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b1df50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1df50 bytes e007803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31254066408787ff35e02282bbd1f18e"></a>

### [`00b1e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e044.md) → [`00b80fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80fb0.md) _ZN11flatbuffers11NumToStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x62f6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1f0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`00c5bc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc30.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 83.52% / 新版 83.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e0b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e0b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e0b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80fe4",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b80fe8",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1e0b0",
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
      "00b80fe4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b80fe8",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b8101c",
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

- 旧版 [`00b1e0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e044.md#insn-00b1e0b0) · [`00b1e0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e044.md#insn-00b1e0b4) · [`00b1e0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e044.md#insn-00b1e0b8)

~~~diff
- 00b1e0b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b1e0b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b1e0b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1e0b0 bytes a9031af8
- 00b1e0b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b1e0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1e0b4 bytes e84b00f9
- 00b1e0b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b1e0b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b1e0b8 bytes fb1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c399929bdee6aac5e84f7966d3440bf8"></a>

### [`00b1e1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md) → [`00b8111c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b8111c.md) _ZN11flatbuffers6Parser10TokenErrorEv

採用 · 移動量 `+0x62f6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf770.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5c090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c090.md) · 呼出先 10件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 64.29% / 新版 65.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b81174"
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
      "00b81168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1e234"
      ]
    ],
    [
      "unmatched:00b1e208",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e20c",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b81168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b811a0"
      ]
    ],
    [
      "00b81174",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b81178",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e208) · [`00b1e20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e20c) · [`00b1e23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e23c)

~~~diff
- 00b1e208 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b1e208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b1e208 bytes e90b00f9
- 00b1e20c ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b1e20c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1e20c bytes e003803d
- 00b1e23c ["CBRANCH", null, ["local:b31:8", "register:102:1"]]
- 00b1e23c bytes c20c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9783a70b098798eaf5883e9788b8ac8a"></a>

### [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) → [`00b81344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md) _ZN11flatbuffers6Parser13ParseFunctionEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueE

採用 · 移動量 `+0x62f6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf810.md) · 呼出先 23件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c5c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c140.md) · 呼出先 23件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00b7ed20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.39% / 新版 58.83%

CFGの説明率　旧版 33.00% / 新版 34.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 2件, `call_argument_candidate` 13件, `store_condition` 10件, `store_destination` 1件, `store_value` 2件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 53件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1e410",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e414",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1e43c"
      ]
    ]
  ],
  "added": [
    [
      "00b81390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b813b4"
      ]
    ],
    [
      "00b8139c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c120"
      ]
    ],
    [
      "00b813ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81824"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e410) · [`00b1e414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e414) · [`00b1e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e430)

~~~diff
- 00b1e410 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b1e410 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b1e410 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b1e410 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b1e410 bytes bfff37a9
- 00b1e414 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b1e414 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b1e414 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff70:8"]]
- 00b1e414 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:8"]]
- 00b1e414 bytes bf0317f8
- 00b1e430 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b1e430 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff80:8"]]
- 00b1e430 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1e430 bytes a80318f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811fe22d271a1844d3d3f4841048294e"></a>

### [`00b1eda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md) → [`00b81d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81d2c.md) _ZN11flatbuffers6Parser13TryTypedValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEibRNS_5ValueENS_8BaseTypeEPb

採用 · 移動量 `+0x62f84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf840.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c170.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_count, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.90% / 新版 72.59%

CFGの説明率　旧版 52.08% / 新版 48.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_argument_candidate` 7件, `store_condition` 16件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1edd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ee08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ee48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1edd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1ede0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82280"
      ]
    ],
    [
      "unmatched:00b1ee0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81dac"
      ]
    ]
  ],
  "added": [
    [
      "00b81d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b81d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81dac"
      ]
    ],
    [
      "00b81dcc",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1edd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1edd4) · [`00b1ee08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1ee08) · [`00b1ee48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1ee48)

~~~diff
- 00b1edd4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b1edd4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b1edd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1edd4 bytes a9031af8
- 00b1ee08 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b1ee08 ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00b1ee08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b1ee08 bytes c8000039
- 00b1ee48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b1ee48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b1ee48 bytes e01b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b3c26b0d64f0e2006ae926c8144a8c"></a>

### [`00b1f56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f56c.md) → [`00b8261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b8261c.md) _ZNK11flatbuffers7EnumDef8MinValueEv

採用 · 移動量 `+0x630b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b82620",
      "incomplete_value": true,
      "site": "00b82624",
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
      "definition_site": "00b1f570",
      "incomplete_value": true,
      "site": "00b1f574",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f56c.md#insn-00b1f56c)
- 新版 [`00b8261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b8261c.md#insn-00b8261c)

~~~diff
- 00b1f56c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d0:8"]]
- 00b1f56c ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1f56c ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b1f56c ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
+ 00b8261c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e0:8"]]
+ 00b8261c ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8261c ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
+ 00b8261c ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b1f56c bytes 08244da9
+ 00b8261c bytes 08244ea9
~~~


<a id="compare-37bf99acf0429a9095dd7d379a96792e"></a>

### [`00b1f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f588.md) → [`00b82638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82638.md) _ZNK11flatbuffers7EnumDef8MaxValueEv

採用 · 移動量 `+0x630b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b8263c",
      "incomplete_value": true,
      "site": "00b82640",
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
      "definition_site": "00b1f58c",
      "incomplete_value": true,
      "site": "00b1f590",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f588.md#insn-00b1f588)
- 新版 [`00b82638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82638.md#insn-00b82638)

~~~diff
- 00b1f588 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d0:8"]]
- 00b1f588 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1f588 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b1f588 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
+ 00b82638 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e0:8"]]
+ 00b82638 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82638 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
+ 00b82638 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b1f588 bytes 09204da9
+ 00b82638 bytes 09204ea9
~~~


<a id="compare-a7276b5d09808e9c719a9c2b405c7c21"></a>

### [`00b1f5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f5d8.md) → [`00b82688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82688.md) _ZNK11flatbuffers7EnumDef8AllFlagsEv

採用 · 移動量 `+0x630b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdf1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1c0.md) [`00bdf1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc00.md) [`00c5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc10.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b8268c",
      "incomplete_value": true,
      "site": "00b82690",
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
      "definition_site": "00b1f5dc",
      "incomplete_value": true,
      "site": "00b1f5e0",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f5d8.md#insn-00b1f5d8) · [`00b1f634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f5d8.md#insn-00b1f634) · [`00b1f638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f5d8.md#insn-00b1f638)
- 新版 [`00b82688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82688.md#insn-00b82688) · [`00b826e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82688.md#insn-00b826e4) · [`00b826e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82688.md#insn-00b826e8)

~~~diff
- 00b1f5d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d0:8"]]
- 00b1f5d8 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1f5d8 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b1f5d8 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
+ 00b82688 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e0:8"]]
+ 00b82688 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82688 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
+ 00b82688 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b1f5d8 bytes 0f284da9
+ 00b82688 bytes 0f284ea9
- 00b1f634 ["INT_ADD", "tmp:0:8", ["register:4088:8", "const:50:8"]]
- 00b1f634 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b826e4 ["INT_ADD", "tmp:0:8", ["register:4088:8", "const:80:8"]]
+ 00b826e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1f634 bytes 312a40f9
+ 00b826e4 bytes 314240f9
- 00b1f638 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
- 00b1f638 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b826e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:80:8"]]
+ 00b826e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1f638 bytes 212840f9
+ 00b826e8 bytes 214040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff1fd012cc11f4d412d659942a45cea"></a>

### [`00b1f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f6a0.md) → [`00b82750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82750.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0x630b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa70.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c410.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b520.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, store_destination, unresolved_return_alignment

命令の説明率　旧版 49.52% / 新版 65.00%

CFGの説明率　旧版 43.86% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 6件, `call_count` 2件, `store_condition` 1件, `store_count` 3件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f6a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1f6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1f6a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1f6a8",
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
      "00b82750",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b82754",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b82758",
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

- 旧版 [`00b1f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f6a0.md#insn-00b1f6a0) · [`00b1f6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f6a0.md#insn-00b1f6a4) · [`00b1f6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f6a0.md#insn-00b1f6a8)

~~~diff
- 00b1f6a0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1f6a0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1f6a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b1f6a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b1f6a0 bytes fa67bba9
- 00b1f6a4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1f6a4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1f6a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b1f6a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1f6a4 bytes f85f01a9
- 00b1f6a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b1f6a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b1f6a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b1f6a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1f6a8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

