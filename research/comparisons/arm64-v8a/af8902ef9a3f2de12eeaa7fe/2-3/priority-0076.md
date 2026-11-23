# v16.0.0 → v16.0.1 · 最優先の変更候補 (76)

[一覧の目次](README.md)

<a id="compare-f6743f1aa9bcf0854491f093a6704a2e"></a>

### [`00b659e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md) → [`00b65e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e10.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b65a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65e50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b659fc",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65a04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65e54"
      ]
    ],
    [
      "unmatched:00b65a0c",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65e24",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65e54"
      ]
    ],
    [
      "00b65e34",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md#insn-00b65a04) · [`00b65a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md#insn-00b65a20) · [`00b65a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b659e8.md#insn-00b65a28)
- 新版 `00b65e48`（命令位置の公開資料なし）

~~~diff
- 00b65a04 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65a04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65a04 bytes 410100b5
- 00b65a20 ["INT_ADD", "register:40f0:8", ["const:b65a20:8", "const:4:8"]]
- 00b65a20 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b65e48 ["INT_ADD", "register:40f0:8", ["const:b65e48:8", "const:4:8"]]
+ 00b65e48 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65a20 bytes 3cd40394
+ 00b65e48 bytes 32d40394
- 00b65a28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00b65a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65a28 bytes 808606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2d84f783497390b3bdb926092e042ae"></a>

### [`00b65a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md) → [`00b65e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e80.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b65e9c",
      "incomplete_value": false,
      "site": "00b65ea0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65eac",
      "incomplete_value": true,
      "site": "00b65eb8",
      "value": [
        "LOAD",
        "8",
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
      "00b65e9c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b65eac",
      "DATA",
      [
        "storage",
        "01125d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65e9c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b65eac",
      "DATA",
      [
        "storage",
        "01126118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a78) · [`00b65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a74) · [`00b65a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a58.md#insn-00b65a7c)
- 新版 `00b65ea0`（命令位置の公開資料なし） · `00b65e9c`（命令位置の公開資料なし） · `00b65ea4`（命令位置の公開資料なし）

~~~diff
- 00b65a78 ["INT_ADD", "register:40f0:8", ["const:b65a78:8", "const:4:8"]]
- 00b65a78 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b65ea0 ["INT_ADD", "register:40f0:8", ["const:b65ea0:8", "const:4:8"]]
+ 00b65ea0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b65a78 bytes 62d40394
+ 00b65ea0 bytes 58d40394
- 00b65a74 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b65a74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65a74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65a74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65e9c ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b65e9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65a74 bytes 00680a91
+ 00b65e9c bytes 009c0d91
- 00b65a7c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b65ea4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65a7c bytes 082e0090
+ 00b65ea4 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2869886f7dd0cb9a75027e970e1c3a7"></a>

### [`00b65a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md) → [`00b65ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ebc.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65efc",
      "incomplete_value": true,
      "site": "00b65efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65ed8",
      "incomplete_value": true,
      "site": "00b65ed8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65ee0",
      "incomplete_value": false,
      "site": "00b65ef4",
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
            "const:96b:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
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
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ee0",
      "PARAM",
      [
        "storage",
        "002b592b",
        null,
        "string"
      ]
    ],
    [
      "00b65efc",
      "WRITE",
      [
        "storage",
        "01125d08",
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
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ee0",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65efc",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65acc) · [`00b65ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65ad4) · [`00b65aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65a94.md#insn-00b65aa0)
- 新版 `00b65ef4`（命令位置の公開資料なし） · `00b65efc`（命令位置の公開資料なし） · `00b65ec8`（命令位置の公開資料なし）

~~~diff
- 00b65acc ["INT_ADD", "register:40f0:8", ["const:b65acc:8", "const:4:8"]]
- 00b65acc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b65ef4 ["INT_ADD", "register:40f0:8", ["const:b65ef4:8", "const:4:8"]]
+ 00b65ef4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65acc bytes 11d40394
+ 00b65ef4 bytes 07d40394
- 00b65ad4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00b65ad4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65efc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
+ 00b65efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ad4 bytes 808606f9
+ 00b65efc bytes 808600f9
- 00b65aa0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b65ec8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65aa0 bytes 142e0090
+ 00b65ec8 bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0845ede866f29c5d098f536358be3dc7"></a>

### [`00b65b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md) → [`00b65f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f2c.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b65f48",
      "incomplete_value": false,
      "site": "00b65f4c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65f58",
      "incomplete_value": true,
      "site": "00b65f64",
      "value": [
        "LOAD",
        "8",
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
      "00b65f48",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b65f58",
      "DATA",
      [
        "storage",
        "01125d50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65f48",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b65f58",
      "DATA",
      [
        "storage",
        "01126150",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b24) · [`00b65b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b20) · [`00b65b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b04.md#insn-00b65b28)
- 新版 `00b65f4c`（命令位置の公開資料なし） · `00b65f48`（命令位置の公開資料なし） · `00b65f50`（命令位置の公開資料なし）

~~~diff
- 00b65b24 ["INT_ADD", "register:40f0:8", ["const:b65b24:8", "const:4:8"]]
- 00b65b24 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b65f4c ["INT_ADD", "register:40f0:8", ["const:b65f4c:8", "const:4:8"]]
+ 00b65f4c ["CALL", null, ["callee:00c5b000:8"]]
- 00b65b24 bytes 37d40394
+ 00b65f4c bytes 2dd40394
- 00b65b20 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b65b20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65f48 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b65f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65b20 bytes 00441191
+ 00b65f48 bytes 00781491
- 00b65b28 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b65f50 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65b28 bytes 082e0090
+ 00b65f50 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa65b868421d70278d25659fe7839788"></a>

### [`00b65b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md) → [`00b65f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f68.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b65f94",
      "incomplete_value": true,
      "site": "00b65f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65f7c",
      "incomplete_value": true,
      "site": "00b65f7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65f88",
      "incomplete_value": false,
      "site": "00b65f8c",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65f78",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f88",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65f94",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65f78",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f88",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b65f94",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b64) · [`00b65b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b6c) · [`00b65b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b40.md#insn-00b65b4c)
- 新版 `00b65f8c`（命令位置の公開資料なし） · `00b65f94`（命令位置の公開資料なし） · `00b65f74`（命令位置の公開資料なし）

~~~diff
- 00b65b64 ["INT_ADD", "register:40f0:8", ["const:b65b64:8", "const:4:8"]]
- 00b65b64 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b65f8c ["INT_ADD", "register:40f0:8", ["const:b65f8c:8", "const:4:8"]]
+ 00b65f8c ["CALL", null, ["callee:00c5af10:8"]]
- 00b65b64 bytes ebd30394
+ 00b65f8c bytes e1d30394
- 00b65b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
- 00b65b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
+ 00b65f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b6c bytes 60ae06f9
+ 00b65f94 bytes 60ae00f9
- 00b65b4c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b65f74 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65b4c bytes 132e0090
+ 00b65f74 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6141ecd36f2bce7cf1da74c4ca988e2"></a>

### [`00b65b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md) → [`00b65fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fa8.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b65fd4",
      "incomplete_value": true,
      "site": "00b65fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65fbc",
      "incomplete_value": true,
      "site": "00b65fbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65fc4",
      "incomplete_value": false,
      "site": "00b65fcc",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65fb8",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fc4",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b65fd4",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65fb8",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fc4",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b65fd4",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65ba4) · [`00b65bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65bac) · [`00b65b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65b80.md#insn-00b65b8c)
- 新版 `00b65fcc`（命令位置の公開資料なし） · `00b65fd4`（命令位置の公開資料なし） · `00b65fb4`（命令位置の公開資料なし）

~~~diff
- 00b65ba4 ["INT_ADD", "register:40f0:8", ["const:b65ba4:8", "const:4:8"]]
- 00b65ba4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b65fcc ["INT_ADD", "register:40f0:8", ["const:b65fcc:8", "const:4:8"]]
+ 00b65fcc ["CALL", null, ["callee:00c5af10:8"]]
- 00b65ba4 bytes dbd30394
+ 00b65fcc bytes d1d30394
- 00b65bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
- 00b65bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
+ 00b65fd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65bac bytes 60ae06f9
+ 00b65fd4 bytes 60ae00f9
- 00b65b8c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b65fb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65b8c bytes 132e0090
+ 00b65fb4 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7c0193e32645281113fa08cf1b9687"></a>

### [`00b65bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md) → [`00b65fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fe8.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b66018",
      "incomplete_value": true,
      "site": "00b66018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65ffc",
      "incomplete_value": true,
      "site": "00b65ffc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66008",
      "incomplete_value": false,
      "site": "00b66010",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65ff8",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66008",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b66018",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65ff8",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66008",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66018",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65be8) · [`00b65bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65bf0) · [`00b65bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65bc0.md#insn-00b65bcc)
- 新版 `00b66010`（命令位置の公開資料なし） · `00b66018`（命令位置の公開資料なし） · `00b65ff4`（命令位置の公開資料なし）

~~~diff
- 00b65be8 ["INT_ADD", "register:40f0:8", ["const:b65be8:8", "const:4:8"]]
- 00b65be8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b66010 ["INT_ADD", "register:40f0:8", ["const:b66010:8", "const:4:8"]]
+ 00b66010 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65be8 bytes cad30394
+ 00b66010 bytes c0d30394
- 00b65bf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
- 00b65bf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
+ 00b66018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65bf0 bytes 60ae06f9
+ 00b66018 bytes 60ae00f9
- 00b65bcc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b65ff4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65bcc bytes 132e0090
+ 00b65ff4 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841d7b89f8d5445a5be8f437026615b6"></a>

### [`00b65c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md) → [`00b6602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6602c.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6605c",
      "incomplete_value": true,
      "site": "00b6605c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66040",
      "incomplete_value": true,
      "site": "00b66040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66048",
      "incomplete_value": false,
      "site": "00b66054",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6603c",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66048",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b6605c",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6603c",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66048",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b6605c",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c2c) · [`00b65c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c34) · [`00b65c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c04.md#insn-00b65c10)
- 新版 `00b66054`（命令位置の公開資料なし） · `00b6605c`（命令位置の公開資料なし） · `00b66038`（命令位置の公開資料なし）

~~~diff
- 00b65c2c ["INT_ADD", "register:40f0:8", ["const:b65c2c:8", "const:4:8"]]
- 00b65c2c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b66054 ["INT_ADD", "register:40f0:8", ["const:b66054:8", "const:4:8"]]
+ 00b66054 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65c2c bytes b9d30394
+ 00b66054 bytes afd30394
- 00b65c34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d58:8"]]
- 00b65c34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6605c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
+ 00b6605c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c34 bytes 60ae06f9
+ 00b6605c bytes 60ae00f9
- 00b65c10 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b66038 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65c10 bytes 132e0090
+ 00b66038 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f7898d128c046a65c2293468bf22890"></a>

### [`00b65c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md) → [`00b6607c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6607c.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b660d4",
      "incomplete_value": true,
      "site": "00b660d4",
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
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b660b0",
      "incomplete_value": true,
      "site": "00b660bc",
      "value": [
        "LOAD",
        "8",
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b66090",
      "READ",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b660b0",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660d4",
      "WRITE",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66090",
      "READ",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b660b0",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660d4",
      "WRITE",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65c94) · [`00b65cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65cac) · [`00b65c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65c54.md#insn-00b65c64)
- 新版 `00b660bc`（命令位置の公開資料なし） · `00b660d4`（命令位置の公開資料なし） · `00b6608c`（命令位置の公開資料なし）

~~~diff
- 00b65c94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65c94 ["INT_ADD", "register:40f0:8", ["const:b65c94:8", "const:4:8"]]
- 00b65c94 ["CALLIND", null, ["register:0:8"]]
+ 00b660bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b660bc ["INT_ADD", "register:40f0:8", ["const:b660bc:8", "const:4:8"]]
+ 00b660bc ["CALLIND", null, ["register:0:8"]]
- 00b65c94 bytes 00013fd6
+ 00b660bc bytes 00013fd6
- 00b65cac ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65cac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d60:8"]]
- 00b65cac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b660d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b660d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:160:8"]]
+ 00b660d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65cac bytes a0823539
+ 00b660d4 bytes a0820539
- 00b65c64 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b6608c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b65c64 bytes 152e0090
+ 00b6608c bytes 152e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00062879bf59e29d05cc4fa138faa12a"></a>

### [`00b65cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md) → [`00b660e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b660e8.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b66124",
      "incomplete_value": true,
      "site": "00b66124",
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
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66144",
      "incomplete_value": true,
      "site": "00b66144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66100",
      "incomplete_value": true,
      "site": "00b66100",
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
      "00b660fc",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66108",
      "READ",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66124",
      "WRITE",
      [
        "storage",
        "01125d60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b660fc",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66108",
      "READ",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66124",
      "WRITE",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65cfc) · [`00b65d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65d18) · [`00b65d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65cc0.md#insn-00b65d1c)
- 新版 `00b66124`（命令位置の公開資料なし） · `00b66140`（命令位置の公開資料なし） · `00b66144`（命令位置の公開資料なし）

~~~diff
- 00b65cfc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65cfc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65cfc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d60:8"]]
- 00b65cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66124 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66124 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66124 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:160:8"]]
+ 00b66124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65cfc bytes bf823539
+ 00b66124 bytes bf820539
- 00b65d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65d18 ["INT_ADD", "register:40f0:8", ["const:b65d18:8", "const:4:8"]]
- 00b65d18 ["CALLIND", null, ["register:0:8"]]
+ 00b66140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66140 ["INT_ADD", "register:40f0:8", ["const:b66140:8", "const:4:8"]]
+ 00b66140 ["CALLIND", null, ["register:0:8"]]
- 00b65d18 bytes 00013fd6
+ 00b66140 bytes 00013fd6
- 00b65d1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
- 00b65d1c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b66144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
+ 00b66144 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b66144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65d1c bytes 9fae06f9
+ 00b66144 bytes 9fae00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef94a24b6609d009940f718e6682e75"></a>

### [`00b65d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md) → [`00b66158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66158.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b66198",
      "incomplete_value": true,
      "site": "00b66198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66174",
      "incomplete_value": true,
      "site": "00b66174",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6617c",
      "incomplete_value": false,
      "site": "00b66190",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6616c",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6617c",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b66198",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6616c",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6617c",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66198",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d68) · [`00b65d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d70) · [`00b65d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65d30.md#insn-00b65d3c)
- 新版 `00b66190`（命令位置の公開資料なし） · `00b66198`（命令位置の公開資料なし） · `00b66164`（命令位置の公開資料なし）

~~~diff
- 00b65d68 ["INT_ADD", "register:40f0:8", ["const:b65d68:8", "const:4:8"]]
- 00b65d68 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b66190 ["INT_ADD", "register:40f0:8", ["const:b66190:8", "const:4:8"]]
+ 00b66190 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65d68 bytes 6ad30394
+ 00b66190 bytes 60d30394
- 00b65d70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
- 00b65d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
+ 00b66198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65d70 bytes 80ae06f9
+ 00b66198 bytes 80ae00f9
- 00b65d3c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b66164 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65d3c bytes 142e0090
+ 00b66164 bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abb8697a1a93a92fab09039e2db4328a"></a>

### [`00b65da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md) → [`00b661c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b661c8.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b661e4",
      "incomplete_value": false,
      "site": "00b661e8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b661f4",
      "incomplete_value": true,
      "site": "00b66200",
      "value": [
        "LOAD",
        "8",
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
      "00b661e4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b661f4",
      "DATA",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b661e4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b661f4",
      "DATA",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65dc0) · [`00b65dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65dbc) · [`00b65dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65da0.md#insn-00b65dc4)
- 新版 `00b661e8`（命令位置の公開資料なし） · `00b661e4`（命令位置の公開資料なし） · `00b661ec`（命令位置の公開資料なし）

~~~diff
- 00b65dc0 ["INT_ADD", "register:40f0:8", ["const:b65dc0:8", "const:4:8"]]
- 00b65dc0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b661e8 ["INT_ADD", "register:40f0:8", ["const:b661e8:8", "const:4:8"]]
+ 00b661e8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b65dc0 bytes 90d30394
+ 00b661e8 bytes 86d30394
- 00b65dbc ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b65dbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65dbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65dbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b661e4 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b661e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b661e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b661e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65dbc bytes 00680a91
+ 00b661e4 bytes 009c0d91
- 00b65dc4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b661ec ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65dc4 bytes 082e0090
+ 00b661ec bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-215f0df346258dfda0a0850b76de81a5"></a>

### [`00b65ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md) → [`00b66204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66204.md) _ZN8firebase17version_registrar13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b66244",
      "incomplete_value": true,
      "site": "00b66244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e1c",
      "incomplete_value": true,
      "site": "00b65e1c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66220",
      "incomplete_value": true,
      "site": "00b66220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65df8",
      "incomplete_value": true,
      "site": "00b65df8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66228",
      "incomplete_value": false,
      "site": "00b6623c",
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
            "const:97a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e00",
      "incomplete_value": false,
      "site": "00b65e14",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66218",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66228",
      "PARAM",
      [
        "storage",
        "002c093a",
        null,
        "string"
      ]
    ],
    [
      "00b66244",
      "WRITE",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66218",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66228",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66244",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md#insn-00b65e14) · [`00b65e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md#insn-00b65e1c) · [`00b65de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65ddc.md#insn-00b65de8)
- 新版 `00b6623c`（命令位置の公開資料なし） · `00b66244`（命令位置の公開資料なし） · `00b66210`（命令位置の公開資料なし）

~~~diff
- 00b65e14 ["INT_ADD", "register:40f0:8", ["const:b65e14:8", "const:4:8"]]
- 00b65e14 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b6623c ["INT_ADD", "register:40f0:8", ["const:b6623c:8", "const:4:8"]]
+ 00b6623c ["CALL", null, ["callee:00c5af10:8"]]
- 00b65e14 bytes 3fd30394
+ 00b6623c bytes 35d30394
- 00b65e1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
- 00b65e1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
+ 00b66244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e1c bytes 80ae06f9
+ 00b66244 bytes 80ae00f9
- 00b65de8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b66210 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65de8 bytes 142e0090
+ 00b66210 bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bf1d94e79806931af039b2e44fdaf6"></a>

### [`00b65e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md) → [`00b66274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66274.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b66290",
      "incomplete_value": false,
      "site": "00b66294",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b662a0",
      "incomplete_value": true,
      "site": "00b662ac",
      "value": [
        "LOAD",
        "8",
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
      "00b66290",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b662a0",
      "DATA",
      [
        "storage",
        "01125d80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66290",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b662a0",
      "DATA",
      [
        "storage",
        "01126180",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e6c) · [`00b65e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e68) · [`00b65e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e4c.md#insn-00b65e70)
- 新版 `00b66294`（命令位置の公開資料なし） · `00b66290`（命令位置の公開資料なし） · `00b66298`（命令位置の公開資料なし）

~~~diff
- 00b65e6c ["INT_ADD", "register:40f0:8", ["const:b65e6c:8", "const:4:8"]]
- 00b65e6c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b66294 ["INT_ADD", "register:40f0:8", ["const:b66294:8", "const:4:8"]]
+ 00b66294 ["CALL", null, ["callee:00c5b000:8"]]
- 00b65e6c bytes 65d30394
+ 00b66294 bytes 5bd30394
- 00b65e68 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b65e68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66290 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b66290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65e68 bytes 00441191
+ 00b66290 bytes 00781491
- 00b65e70 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b66298 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65e70 bytes 082e0090
+ 00b66298 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9601222f60d334f80a4f66b9b92f77e0"></a>

### [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) → [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bac0.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66214.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c5bec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bec0.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b6663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6663c.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00b662f8",
      "incomplete_value": true,
      "site": "00b66308",
      "value": [
        "LOAD",
        "8",
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b662fc",
      "incomplete_value": true,
      "site": "00b66308",
      "value": [
        "LOAD",
        "8",
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
                "const:118:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b662f8",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662fc",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b662f8",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662fc",
      "READ",
      [
        "storage",
        "01126118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ee0) · [`00b65ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ec0) · [`00b65ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md#insn-00b65ec8)
- 新版 `00b66308`（命令位置の公開資料なし） · `00b662e8`（命令位置の公開資料なし） · `00b662f0`（命令位置の公開資料なし）

~~~diff
- 00b65ee0 ["INT_ADD", "register:40f0:8", ["const:b65ee0:8", "const:4:8"]]
- 00b65ee0 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b66308 ["INT_ADD", "register:40f0:8", ["const:b66308:8", "const:4:8"]]
+ 00b66308 ["CALL", null, ["callee:00c5aba0:8"]]
- 00b65ee0 bytes 30d20394
+ 00b66308 bytes 26d20394
- 00b65ec0 ["INT_ADD", "register:40f0:8", ["const:b65ec0:8", "const:4:8"]]
- 00b65ec0 ["CALL", null, ["callee:00b66454:8"]]
+ 00b662e8 ["INT_ADD", "register:40f0:8", ["const:b662e8:8", "const:4:8"]]
+ 00b662e8 ["CALL", null, ["callee:00b66454:8"]]
- 00b65ec0 bytes 5b000094
+ 00b662e8 bytes 5b000094
- 00b65ec8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b662f0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65ec8 bytes 082e0090
+ 00b662f0 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f691d137ca89e0d12e86a63bbec48f"></a>

### [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) → [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) FUN_00b66454

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) [`00b67e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e18.md) · 呼出先 5件 [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md)
- 新版 呼出元 4件 [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) · 呼出先 5件 [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md)

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
      "definition_site": "00b66470",
      "incomplete_value": false,
      "site": "00b66470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b664bc",
      "incomplete_value": true,
      "site": "00b664bc",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66514",
      "incomplete_value": true,
      "site": "00b66514",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b66468",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66470",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66494",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66468",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66470",
      "WRITE",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66494",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b66048) · [`00b6608c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b6608c) · [`00b66094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md#insn-00b66094)
- 新版 `00b66470`（命令位置の公開資料なし） · `00b664b4`（命令位置の公開資料なし） · `00b664bc`（命令位置の公開資料なし）

~~~diff
- 00b66048 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d88:8"]]
- 00b66048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b66470 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:188:8"]]
+ 00b66470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b66048 bytes a98a0db9
+ 00b66470 bytes a98a01b9
- 00b6608c ["INT_ADD", "register:40f0:8", ["const:b6608c:8", "const:4:8"]]
- 00b6608c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b664b4 ["INT_ADD", "register:40f0:8", ["const:b664b4:8", "const:4:8"]]
+ 00b664b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b6608c bytes a1d20394
+ 00b664b4 bytes 97d20394
- 00b66094 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c50:8"]]
- 00b66094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b664bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:50:8"]]
+ 00b664bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66094 bytes a02a06f9
+ 00b664bc bytes a02a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c95f7032650340a69aa3f182f160f81d"></a>

### [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) → [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) FUN_00b66a48

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00b65e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65e88.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 4件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b920.md)
- 新版 呼出元 6件 [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) · 呼出先 4件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66a7c",
      "incomplete_value": true,
      "site": "00b66a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66abc",
      "incomplete_value": true,
      "site": "00b66abc",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66694",
      "incomplete_value": true,
      "site": "00b66694",
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
            "const:c58:8"
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
      "definition_site": "00b66adc",
      "incomplete_value": true,
      "site": "00b66adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b666b4",
      "incomplete_value": true,
      "site": "00b666b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00b66a5c",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66a6c",
      "PARAM",
      [
        "storage",
        "002bbe12",
        null,
        "string"
      ]
    ],
    [
      "00b66a74",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b66a5c",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66a6c",
      "PARAM",
      [
        "storage",
        "002bbe52",
        null,
        "string"
      ]
    ],
    [
      "00b66a74",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md#insn-00b66648) · [`00b66654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md#insn-00b66654) · [`00b66694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md#insn-00b66694)
- 新版 `00b66a70`（命令位置の公開資料なし） · `00b66a7c`（命令位置の公開資料なし） · `00b66abc`（命令位置の公開資料なし）

~~~diff
- 00b66648 ["INT_ADD", "register:40f0:8", ["const:b66648:8", "const:4:8"]]
- 00b66648 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b66a70 ["INT_ADD", "register:40f0:8", ["const:b66a70:8", "const:4:8"]]
+ 00b66a70 ["CALL", null, ["callee:00c5b000:8"]]
- 00b66648 bytes 6ed10394
+ 00b66a70 bytes 64d10394
- 00b66654 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
- 00b66654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b66a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:188:8"]]
+ 00b66a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b66654 bytes 888a0db9
+ 00b66a7c bytes 888a01b9
- 00b66694 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66694 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66694 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c58:8"]]
- 00b66694 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66abc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66abc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66abc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:58:8"]]
+ 00b66abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66694 bytes bf623139
+ 00b66abc bytes bf620139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eda17cadaabf39d96c936244ac913e28"></a>

### [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) → [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a550.md) · 呼出先 7件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md) [`00b66620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66620.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`00c5a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a950.md) · 呼出先 7件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)

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
      "definition_site": "00b66d28",
      "incomplete_value": true,
      "site": "00b66d2c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66d44",
      "incomplete_value": false,
      "site": "00b66d48",
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
            "const:caf:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b66d18",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ],
    [
      "00b66d28",
      "READ",
      [
        "storage",
        "00c8fe00",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66d28",
      "PARAM",
      [
        "storage",
        "002b58f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66d18",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b66d28",
      "READ",
      [
        "storage",
        "00c90200",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66d28",
      "PARAM",
      [
        "storage",
        "002b5932",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b66904) · [`00b66920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b66920) · [`00b668ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md#insn-00b668ac)
- 新版 `00b66d2c`（命令位置の公開資料なし） · `00b66d48`（命令位置の公開資料なし） · `00b66cd4`（命令位置の公開資料なし）

~~~diff
- 00b66904 ["INT_ADD", "register:40f0:8", ["const:b66904:8", "const:4:8"]]
- 00b66904 ["CALL", null, ["callee:00c5bed0:8"]]
+ 00b66d2c ["INT_ADD", "register:40f0:8", ["const:b66d2c:8", "const:4:8"]]
+ 00b66d2c ["CALL", null, ["callee:00c5bed0:8"]]
- 00b66904 bytes 73d40394
+ 00b66d2c bytes 69d40394
- 00b66920 ["INT_ADD", "register:40f0:8", ["const:b66920:8", "const:4:8"]]
- 00b66920 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b66d48 ["INT_ADD", "register:40f0:8", ["const:b66d48:8", "const:4:8"]]
+ 00b66d48 ["CALL", null, ["callee:00c5aca0:8"]]
- 00b66920 bytes e0cf0394
+ 00b66d48 bytes d6cf0394
- 00b668ac ["INT_ADD", "register:40f0:8", ["const:b668ac:8", "const:4:8"]]
- 00b668ac ["CALL", null, ["callee:00b66454:8"]]
+ 00b66cd4 ["INT_ADD", "register:40f0:8", ["const:b66cd4:8", "const:4:8"]]
+ 00b66cd4 ["CALL", null, ["callee:00b66454:8"]]
- 00b668ac bytes e0fdff97
+ 00b66cd4 bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa71c1a2b8d126f77d018a3a1b0b5f18"></a>

### [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) → [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bad0.md) · 呼出先 28件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00b6602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6602c.md)
- 新版 呼出元 1件 [`00c5bed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bed0.md) · 呼出先 28件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.96% / 新版 95.96%

CFGの説明率　旧版 94.21% / 新版 94.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67980"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b67da8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66df4",
      "incomplete_value": false,
      "site": "00b66dfc",
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
            "const:a86:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669cc",
      "incomplete_value": false,
      "site": "00b669d4",
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
            "const:9b9:8"
          ]
        ]
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
      "00b66df4",
      "PARAM",
      [
        "storage",
        "0029f9b9",
        null,
        "string"
      ]
    ],
    [
      "00b66e08",
      "READ",
      [
        "storage",
        "00c9b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b66e10",
      "PARAM",
      [
        "storage",
        "002bd17e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66df4",
      "PARAM",
      [
        "storage",
        "0029fa86",
        null,
        "string"
      ]
    ],
    [
      "00b66e08",
      "READ",
      [
        "storage",
        "00c9b7f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b66e10",
      "PARAM",
      [
        "storage",
        "002bd1be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md#insn-00b669d4) · [`00b669f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md#insn-00b669f4) · [`00b66a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md#insn-00b66a30)
- 新版 `00b66dfc`（命令位置の公開資料なし） · `00b66e1c`（命令位置の公開資料なし） · `00b66e58`（命令位置の公開資料なし）

~~~diff
- 00b669d4 ["INT_ADD", "register:40f0:8", ["const:b669d4:8", "const:4:8"]]
- 00b669d4 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b66dfc ["INT_ADD", "register:40f0:8", ["const:b66dfc:8", "const:4:8"]]
+ 00b66dfc ["CALL", null, ["callee:00c5aca0:8"]]
- 00b669d4 bytes b3cf0394
+ 00b66dfc bytes a9cf0394
- 00b669f4 ["INT_ADD", "register:40f0:8", ["const:b669f4:8", "const:4:8"]]
- 00b669f4 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b66e1c ["INT_ADD", "register:40f0:8", ["const:b66e1c:8", "const:4:8"]]
+ 00b66e1c ["CALL", null, ["callee:00c5b130:8"]]
- 00b669f4 bytes cfd00394
+ 00b66e1c bytes c5d00394
- 00b66a30 ["INT_ADD", "register:40f0:8", ["const:b66a30:8", "const:4:8"]]
- 00b66a30 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b66e58 ["INT_ADD", "register:40f0:8", ["const:b66e58:8", "const:4:8"]]
+ 00b66e58 ["CALL", null, ["callee:00c5aba0:8"]]
- 00b66a30 bytes 5ccf0394
+ 00b66e58 bytes 52cf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977bf54bfc3ccbd85559d467d73b2bff"></a>

### [`00b67c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md) → [`00b68048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68048.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3b0.md) · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b320.md)
- 新版 呼出元 1件 [`00c5b7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7b0.md) · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68070",
      "incomplete_value": false,
      "site": "00b68074",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c48",
      "incomplete_value": false,
      "site": "00b67c4c",
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
            "const:aef:8"
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
      "definition_site": "00b68080",
      "incomplete_value": true,
      "site": "00b6808c",
      "value": [
        "LOAD",
        "8",
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c58",
      "incomplete_value": true,
      "site": "00b67c64",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68084",
      "incomplete_value": true,
      "site": "00b6808c",
      "value": [
        "LOAD",
        "8",
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
                "const:168:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c5c",
      "incomplete_value": true,
      "site": "00b67c64",
      "value": [
        "LOAD",
        "8",
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
                "const:d68:8"
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
      "00b68068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b67c50"
      ]
    ],
    [
      "00b68070",
      "PARAM",
      [
        "storage",
        "002b8aef",
        null,
        "string"
      ]
    ],
    [
      "00b68080",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68078"
      ]
    ],
    [
      "00b68070",
      "PARAM",
      [
        "storage",
        "002b8b2f",
        null,
        "string"
      ]
    ],
    [
      "00b68080",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md#insn-00b67c4c) · [`00b67c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md#insn-00b67c64) · [`00b67c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67c20.md#insn-00b67c80)
- 新版 `00b68074`（命令位置の公開資料なし） · `00b6808c`（命令位置の公開資料なし） · `00b680a8`（命令位置の公開資料なし）

~~~diff
- 00b67c4c ["INT_ADD", "register:40f0:8", ["const:b67c4c:8", "const:4:8"]]
- 00b67c4c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b68074 ["INT_ADD", "register:40f0:8", ["const:b68074:8", "const:4:8"]]
+ 00b68074 ["CALL", null, ["callee:00c5b000:8"]]
- 00b67c4c bytes edcb0394
+ 00b68074 bytes e3cb0394
- 00b67c64 ["INT_ADD", "register:40f0:8", ["const:b67c64:8", "const:4:8"]]
- 00b67c64 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b6808c ["INT_ADD", "register:40f0:8", ["const:b6808c:8", "const:4:8"]]
+ 00b6808c ["CALL", null, ["callee:00c5aba0:8"]]
- 00b67c64 bytes cfca0394
+ 00b6808c bytes c5ca0394
- 00b67c80 ["INT_ADD", "register:40f0:8", ["const:b67c80:8", "const:4:8"]]
- 00b67c80 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
+ 00b680a8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b67c80 bytes e0cb0394
+ 00b680a8 bytes d6cb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52c9a2f7f566427e21286dcb48cd014b"></a>

### [`00b67d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md) → [`00b6815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b6815c.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

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
      "definition_site": "00b68174",
      "incomplete_value": true,
      "site": "00b68174",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68190",
      "incomplete_value": true,
      "site": "00b681a0",
      "value": [
        "LOAD",
        "8",
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b68170",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68190",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681c4",
      "PARAM",
      [
        "storage",
        "002bd19e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b68170",
      "READ",
      [
        "storage",
        "011260a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68190",
      "READ",
      [
        "storage",
        "011260a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681c4",
      "PARAM",
      [
        "storage",
        "002bd1de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d78) · [`00b67d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d44) · [`00b67d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67d34.md#insn-00b67d48)
- 新版 `00b681a0`（命令位置の公開資料なし） · `00b6816c`（命令位置の公開資料なし） · `00b68170`（命令位置の公開資料なし）

~~~diff
- 00b67d78 ["INT_ADD", "register:40f0:8", ["const:b67d78:8", "const:4:8"]]
- 00b67d78 ["CALL", null, ["callee:00574cec:8"]]
+ 00b681a0 ["INT_ADD", "register:40f0:8", ["const:b681a0:8", "const:4:8"]]
+ 00b681a0 ["CALL", null, ["callee:00574cec:8"]]
- 00b67d78 bytes cd33e897
+ 00b681a0 bytes d332e897
- 00b67d44 ["COPY", "register:40b0:8", ["const:1125000:8"]]
+ 00b6816c ["COPY", "register:40b0:8", ["const:1126000:8"]]
- 00b67d44 bytes f62d00d0
+ 00b6816c bytes f62d00d0
- 00b67d48 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ca0:8"]]
- 00b67d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68170 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a0:8"]]
+ 00b68170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67d48 bytes c85246f9
+ 00b68170 bytes c85240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1aea37c81758f3f837447dd55135036"></a>

### [`00b67da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md) → [`00b681d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b681d0.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b681e4",
      "incomplete_value": true,
      "site": "00b681e4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b681fc",
      "incomplete_value": true,
      "site": "00b68208",
      "value": [
        "LOAD",
        "8",
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
                "const:98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b681e0",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b67dd4",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b681e0",
      "READ",
      [
        "storage",
        "01126098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681fc",
      "READ",
      [
        "storage",
        "01126098",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67dbc) · [`00b67de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67de0) · [`00b67db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67da8.md#insn-00b67db4)
- 新版 `00b681e4`（命令位置の公開資料なし） · `00b68208`（命令位置の公開資料なし） · `00b681dc`（命令位置の公開資料なし）

~~~diff
- 00b67dbc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b67dbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b681e4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b681e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67dbc bytes 080200b4
+ 00b681e4 bytes 080200b4
- 00b67de0 ["INT_ADD", "register:40f0:8", ["const:b67de0:8", "const:4:8"]]
- 00b67de0 ["CALL", null, ["callee:00497a48:8"]]
+ 00b68208 ["INT_ADD", "register:40f0:8", ["const:b68208:8", "const:4:8"]]
+ 00b68208 ["CALL", null, ["callee:00497a48:8"]]
- 00b67de0 bytes 0abfe497
+ 00b68208 bytes 10bee497
- 00b67db4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b681dc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67db4 bytes f42d00d0
+ 00b681dc bytes f42d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f620e204ea5db05d29cb1c1f6cb6ab1"></a>

### [`00b683b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b683b8.md) → [`00b687e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b687e0.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.87% / 新版 90.87%

CFGの説明率　旧版 73.37% / 新版 74.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b683ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b68814"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6847c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b683ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b68838",
      "READ",
      [
        "storage",
        "00c9b340",
        null,
        "pointer"
      ]
    ],
    [
      "00b68838",
      "PARAM",
      [
        "storage",
        "0030bc98",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b68814",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b68838",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00b68838",
      "PARAM",
      [
        "storage",
        "0030bcd8",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b683b8.md#insn-00b683ec) · [`00b68420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b683b8.md#insn-00b68420) · [`00b6847c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b683b8.md#insn-00b6847c)
- 新版 `00b68848`（命令位置の公開資料なし）

~~~diff
- 00b683ec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b683ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b683ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b683ec bytes a8031af8
- 00b68420 ["INT_ADD", "register:40f0:8", ["const:b68420:8", "const:4:8"]]
- 00b68420 ["CALL", null, ["callee:00c5bf10:8"]]
+ 00b68848 ["INT_ADD", "register:40f0:8", ["const:b68848:8", "const:4:8"]]
+ 00b68848 ["CALL", null, ["callee:00c5bf10:8"]]
- 00b68420 bytes bccd0394
+ 00b68848 bytes b2cd0394
- 00b6847c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6847c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b6847c bytes 63040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1a4f4d4ff532b2824227c7df42aa577"></a>

### [`00b68b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68b98.md) → [`00b68fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68fc0.md) _ZN11flatbuffers10IDLOptionsC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b490.md) · 呼出先 1件 [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 1件 [`00c5b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b890.md) · 呼出先 1件 [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.83% / 新版 72.83%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 22件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b68fd0",
      "incomplete_value": true,
      "site": "00b69000",
      "value": [
        "LOAD",
        "8",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ba8",
      "incomplete_value": true,
      "site": "00b68bd8",
      "value": [
        "LOAD",
        "8",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68c34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b68fd0",
      "READ",
      [
        "storage",
        "002c4040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b68bc4",
      "PARAM",
      [
        "storage",
        "002a8478",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b68bec",
      "PARAM",
      [
        "storage",
        "002a0009",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68fd0",
      "READ",
      [
        "storage",
        "002c4080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68fec",
      "PARAM",
      [
        "storage",
        "002a8545",
        null,
        "string"
      ]
    ],
    [
      "00b69014",
      "PARAM",
      [
        "storage",
        "002a00d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68b98.md#insn-00b68c30) · [`00b68c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68b98.md#insn-00b68c34) · [`00b68c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68b98.md#insn-00b68c38)

~~~diff
- 00b68c30 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00b68c30 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:ffffffffffffffd8:8"]]
- 00b68c30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b68c30 bytes 74821d78
- 00b68c34 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68c34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68c34 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:ffffffffffffffda:8"]]
- 00b68c34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68c34 bytes 7fa21d38
- 00b68c38 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b68c38 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b68c38 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b68c38 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b68c38 bytes 7f7e0ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac696cc500faf0dc758315c14a852a1b"></a>

### [`00b68d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68d08.md) → [`00b69130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b69/00b69130.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b500.md) · 呼出先 8件 [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b900.md) · 呼出先 8件 [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.37% / 新版 26.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 59件, `unresolved_call_alignment` 83件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 457件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68dc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68dc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68d3c",
      "READ",
      [
        "storage",
        "002c30f0",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b69248",
      "READ",
      [
        "storage",
        "002c42a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69164",
      "READ",
      [
        "storage",
        "002c3130",
        null,
        null
      ]
    ],
    [
      "00b6916c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b69248",
      "READ",
      [
        "storage",
        "002c42e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68d08.md#insn-00b68d44) · [`00b68dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68d08.md#insn-00b68dc0) · [`00b68dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b68/00b68d08.md#insn-00b68dc4)

~~~diff
- 00b68d44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b68d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b68d44 bytes e91700f9
- 00b68dc0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:30:8"]]
- 00b68dc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b68dc0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b68dc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b68dc0 bytes 018701ad
- 00b68dc4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:50:8"]]
- 00b68dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b68dc4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b68dc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b68dc4 bytes 018702ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a773ef5653350f24fdb5ca5ae93022b1"></a>

### [`00b6a70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a70c.md) → [`00b6ab34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6ab34.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4a0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8a0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 54.37% / 新版 50.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a70c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6a70c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a710",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a714",
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
      "00b6ab34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6ab38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6ab3c",
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

- 旧版 [`00b6a70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a70c.md#insn-00b6a70c) · [`00b6a710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a70c.md#insn-00b6a710) · [`00b6a714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a70c.md#insn-00b6a714)

~~~diff
- 00b6a70c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6a70c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6a70c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6a70c bytes f50f1df8
- 00b6a710 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6a710 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6a710 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6a710 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a710 bytes f44f01a9
- 00b6a714 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6a714 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6a714 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6a714 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a714 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-790a8b8edb98e2b86b81ae4abb168585"></a>

### [`00b6a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md) → [`00b6adbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6adbc.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b530.md) · 呼出先 5件 [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bac0.md)
- 新版 呼出元 1件 [`00c5b930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b930.md) · 呼出先 5件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5bec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bec0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.41% / 新版 87.41%

CFGの説明率　旧版 31.03% / 新版 32.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a99c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6a998",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a9a0",
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
      "00b6adc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6adc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6adc8",
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

- 旧版 [`00b6a998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md#insn-00b6a998) · [`00b6a99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md#insn-00b6a99c) · [`00b6a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md#insn-00b6a9a0)

~~~diff
- 00b6a998 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b6a998 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6a998 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b6a998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a998 bytes fc570ea9
- 00b6a99c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6a99c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6a99c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b6a99c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a99c bytes f44f0fa9
- 00b6a9a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6a9a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6a9a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b6a9a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a9a0 bytes fd7b10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e91b1793a322c3ec4ef9bb9d5431a665"></a>

### [`00b6abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md) → [`00b6aff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6aff8.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b480.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)
- 新版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b880.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 45.83% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6abd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6abd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6abd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6abd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6abd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6abd8",
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
      "00b6aff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6affc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6b000",
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

- 旧版 [`00b6abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md#insn-00b6abd0) · [`00b6abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md#insn-00b6abd4) · [`00b6abd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md#insn-00b6abd8)

~~~diff
- 00b6abd0 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b6abd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b6abd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6abd0 bytes f90f1bf8
- 00b6abd4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6abd4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6abd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6abd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6abd4 bytes f85f01a9
- 00b6abd8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6abd8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6abd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6abd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6abd8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937bc245b501230a347a3f2e6441a2f0"></a>

### [`00b6b768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b768.md) → [`00b6bb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6bb90.md) _ZNK8firebase3fbs6Client6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5e0.md) · 呼出先 4件 [`00c5b550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b550.md) [`00c5b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b570.md) [`00c5b5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5d0.md) [`00c5b5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5f0.md)
- 新版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9e0.md) · 呼出先 4件 [`00c5b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b950.md) [`00c5b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b970.md) [`00c5b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9d0.md) [`00c5b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 46.47% / 新版 46.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 30件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b8ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6b7d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c000"
      ]
    ],
    [
      "unmatched:00b6b8e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6b8f0"
      ]
    ],
    [
      "unmatched:00b6b8ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c000"
      ]
    ]
  ],
  "added": [
    [
      "00b6bbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c000"
      ]
    ],
    [
      "00b6bd0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bd18"
      ]
    ],
    [
      "00b6bd14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b768.md#insn-00b6b7d4) · [`00b6b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b768.md#insn-00b6b8e4) · [`00b6b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b768.md#insn-00b6b8ec)

~~~diff
- 00b6b7d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6b7d4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b6b7d4 ["CBRANCH", null, ["local:b91:8", "tmp:1:1"]]
- 00b6b7d4 bytes 28200054
- 00b6b8e4 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00b6b8e4 bytes 60000054
- 00b6b8ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:4", "const:0:4"]]
- 00b6b8ec ["CBRANCH", null, ["local:b91:8", "tmp:0:1"]]
- 00b6b8ec bytes 6c170035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55cdd6f85a1ecca98b46a95b36d5cf0"></a>

### [`00b6bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bbf0.md) → [`00b6c018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c018.md) _ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b550.md) · 呼出先 1件 [`00c5b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5c0.md)
- 新版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b950.md) · 呼出先 1件 [`00c5b9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 86.90% / 新版 86.90%

CFGの説明率　旧版 63.64% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bc20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bc2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bc20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c24c"
      ]
    ],
    [
      "unmatched:00b6bc2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c24c"
      ]
    ],
    [
      "unmatched:00b6bd38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c170"
      ]
    ]
  ],
  "added": [
    [
      "00b6c048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c24c"
      ]
    ],
    [
      "00b6c054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c24c"
      ]
    ],
    [
      "00b6c160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c170"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bbf0.md#insn-00b6bc20) · [`00b6bc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bbf0.md#insn-00b6bc2c) · [`00b6bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bbf0.md#insn-00b6bd38)

~~~diff
- 00b6bc20 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6bc20 ["CBRANCH", null, ["local:b55:8", "tmp:0:1"]]
- 00b6bc20 bytes 23100054
- 00b6bc2c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6bc2c ["CBRANCH", null, ["local:b55:8", "tmp:0:1"]]
- 00b6bc2c bytes c30f0054
- 00b6bd38 ["CBRANCH", null, ["local:b31:8", "register:102:1"]]
- 00b6bd38 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694cece6987939bb08dba03a366db24e"></a>

### [`00b6be34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6be34.md) → [`00b6c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c25c.md) _ZNK8firebase3fbs17AndroidClientInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9c0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment

命令の説明率　旧版 81.13% / 新版 81.13%

CFGの説明率　旧版 28.40% / 新版 32.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_condition` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6becc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6be40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c274"
      ]
    ],
    [
      "unmatched:00b6be58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c3fc"
      ]
    ],
    [
      "00b6c344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c3fc"
      ]
    ]
  ],
  "added": [
    [
      "00b6c268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c274"
      ]
    ],
    [
      "00b6c280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c3fc"
      ]
    ],
    [
      "00b6c28c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c3fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6be34.md#insn-00b6be40) · [`00b6be58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6be34.md#insn-00b6be58) · [`00b6becc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6be34.md#insn-00b6becc)

~~~diff
- 00b6be40 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b6be40 bytes 60000054
- 00b6be58 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6be58 ["CBRANCH", null, ["local:b49:8", "tmp:0:1"]]
- 00b6be58 bytes e30b0054
- 00b6becc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6becc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b6becc ["CBRANCH", null, ["local:b49:8", "tmp:1:1"]]
- 00b6becc bytes 49080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782c536b589d000f523f1f7a82158db2"></a>

### [`00b6d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md) → [`00b6d568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d568.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4b0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md) [`00c5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8b0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md) [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 64.29% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d220"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d648"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d590",
      "incomplete_value": true,
      "site": "00b6d598",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00b6d220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d590"
      ]
    ],
    [
      "unmatched:00b6d224",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d59c"
      ]
    ]
  ],
  "added": [
    [
      "00b6d648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d590"
      ]
    ],
    [
      "00b6d64c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d59c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md#insn-00b6d170) · [`00b6d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d140.md#insn-00b6d220)
- 新版 `00b6d598`（命令位置の公開資料なし） · `00b6d648`（命令位置の公開資料なし）

~~~diff
- 00b6d170 ["INT_ADD", "register:40f0:8", ["const:b6d170:8", "const:4:8"]]
- 00b6d170 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
+ 00b6d598 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d170 bytes 50aa0394
+ 00b6d598 bytes 46aa0394
- 00b6d220 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b6d220 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6d220 bytes 54faffb5
+ 00b6d648 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b6d648 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6d648 bytes 54faffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ed785e4369a6f591c798f1069a034d"></a>

### [`00b6d310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md) → [`00b6d738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d738.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4e0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4d0.md) [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8e0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8d0.md) [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md#insn-00b6d32c) · [`00b6d33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md#insn-00b6d33c) · [`00b6d35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d310.md#insn-00b6d35c)
- 新版 `00b6d754`（命令位置の公開資料なし） · `00b6d764`（命令位置の公開資料なし） · `00b6d784`（命令位置の公開資料なし）

~~~diff
- 00b6d32c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6d32c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b6d754 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6d754 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b6d32c bytes e1020054
+ 00b6d754 bytes e1020054
- 00b6d33c ["INT_ADD", "register:40f0:8", ["const:b6d33c:8", "const:4:8"]]
- 00b6d33c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6d764 ["INT_ADD", "register:40f0:8", ["const:b6d764:8", "const:4:8"]]
+ 00b6d764 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d33c bytes dda90394
+ 00b6d764 bytes d3a90394
- 00b6d35c ["INT_ADD", "register:40f0:8", ["const:b6d35c:8", "const:4:8"]]
- 00b6d35c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6d784 ["INT_ADD", "register:40f0:8", ["const:b6d784:8", "const:4:8"]]
+ 00b6d784 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d35c bytes d5a90394
+ 00b6d784 bytes cba90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b37b6ad9a8efcb738512d5ed4bb3b37"></a>

### [`00b6d3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d3cc.md) → [`00b6d7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d7f4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4les

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b620.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b600.md) [`00c5b620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b620.md)
- 新版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba20.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md) [`00c5ba20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d3cc.md#insn-00b6d3cc) · [`00b6d3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d3cc.md#insn-00b6d3e8) · [`00b6d3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d3cc.md#insn-00b6d3f4)
- 新版 `00b6d7f4`（命令位置の公開資料なし） · `00b6d810`（命令位置の公開資料なし） · `00b6d81c`（命令位置の公開資料なし）

~~~diff
- 00b6d3cc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d3cc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b6d7f4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6d7f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d3cc bytes c10200b4
+ 00b6d7f4 bytes c10200b4
- 00b6d3e8 ["INT_ADD", "register:40f0:8", ["const:b6d3e8:8", "const:4:8"]]
- 00b6d3e8 ["CALL", null, ["callee:00c5ba20:8"]]
+ 00b6d810 ["INT_ADD", "register:40f0:8", ["const:b6d810:8", "const:4:8"]]
+ 00b6d810 ["CALL", null, ["callee:00c5ba20:8"]]
- 00b6d3e8 bytes 8eb80394
+ 00b6d810 bytes 84b80394
- 00b6d3f4 ["INT_ADD", "register:40f0:8", ["const:b6d3f4:8", "const:4:8"]]
- 00b6d3f4 ["CALL", null, ["callee:00c5ba20:8"]]
+ 00b6d81c ["INT_ADD", "register:40f0:8", ["const:b6d81c:8", "const:4:8"]]
+ 00b6d81c ["CALL", null, ["callee:00c5ba20:8"]]
- 00b6d3f4 bytes 8bb80394
+ 00b6d81c bytes 81b80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf81259dcfe333004c449598ee241159"></a>

### [`00b6d428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d428.md) → [`00b6d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d850.md) _ZNSt6__ndk16__treeIN11flatbuffers12IncludedFileENS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b600.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b600.md)
- 新版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d874",
      "incomplete_value": true,
      "site": "00b6d878",
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
      "definition_site": "00b6d870",
      "incomplete_value": true,
      "site": "00b6d878",
      "value": [
        "LOAD",
        "8",
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d894",
      "incomplete_value": true,
      "site": "00b6d898",
      "value": [
        "LOAD",
        "8",
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d428.md#insn-00b6d450) · [`00b6d470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d428.md#insn-00b6d470) · [`00b6d428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d428.md#insn-00b6d428)
- 新版 `00b6d878`（命令位置の公開資料なし） · `00b6d898`（命令位置の公開資料なし） · `00b6d850`（命令位置の公開資料なし）

~~~diff
- 00b6d450 ["INT_ADD", "register:40f0:8", ["const:b6d450:8", "const:4:8"]]
- 00b6d450 ["CALL", null, ["callee:00c5ba00:8"]]
+ 00b6d878 ["INT_ADD", "register:40f0:8", ["const:b6d878:8", "const:4:8"]]
+ 00b6d878 ["CALL", null, ["callee:00c5ba00:8"]]
- 00b6d450 bytes 6cb80394
+ 00b6d878 bytes 62b80394
- 00b6d470 ["INT_ADD", "register:40f0:8", ["const:b6d470:8", "const:4:8"]]
- 00b6d470 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6d898 ["INT_ADD", "register:40f0:8", ["const:b6d898:8", "const:4:8"]]
+ 00b6d898 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d470 bytes 90a90394
+ 00b6d898 bytes 86a90394
- 00b6d428 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d428 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b6d850 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6d850 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b6d428 bytes e10200b4
+ 00b6d850 bytes e10200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b23d17c8f357300ef0e5ad41cf01c0"></a>

### [`00b6d74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md) → [`00b6db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db74.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b630.md)
- 新版 呼出元 1件 [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6d760",
      "incomplete_value": true,
      "site": "00b6d768",
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

- 旧版 [`00b6d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d768) · [`00b6d74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d74c) · [`00b6d774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d74c.md#insn-00b6d774)
- 新版 `00b6db90`（命令位置の公開資料なし） · `00b6db74`（命令位置の公開資料なし） · `00b6db9c`（命令位置の公開資料なし）

~~~diff
- 00b6d768 ["INT_ADD", "register:40f0:8", ["const:b6d768:8", "const:4:8"]]
- 00b6d768 ["CALL", null, ["callee:00c5ba30:8"]]
+ 00b6db90 ["INT_ADD", "register:40f0:8", ["const:b6db90:8", "const:4:8"]]
+ 00b6db90 ["CALL", null, ["callee:00c5ba30:8"]]
- 00b6d768 bytes b2b70394
+ 00b6db90 bytes a8b70394
- 00b6d74c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d74c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6db74 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6db74 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b6d74c bytes 610200b4
+ 00b6db74 bytes 610200b4
- 00b6d774 ["INT_ADD", "register:40f0:8", ["const:b6d774:8", "const:4:8"]]
- 00b6d774 ["CALL", null, ["callee:00c5ba30:8"]]
+ 00b6db9c ["INT_ADD", "register:40f0:8", ["const:b6db9c:8", "const:4:8"]]
+ 00b6db9c ["CALL", null, ["callee:00c5ba30:8"]]
- 00b6d774 bytes afb70394
+ 00b6db9c bytes a5b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed9ff4839ec1542c901aa03e5f180c1"></a>

### [`00b6d79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d79c.md) → [`00b6dbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dbc4.md) _ZN11flatbuffers7EnumValD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b520.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md)
- 新版 呼出元 1件 [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 65.62% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6dbe0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6d7d0",
      "incomplete_value": true,
      "site": "00b6d7d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
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
      "unmatched:00b6d7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dc58"
      ]
    ]
  ],
  "added": [
    [
      "00b6dbe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dc58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d79c.md#insn-00b6d7b8) · [`00b6d7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d79c.md#insn-00b6d7d4)
- 新版 `00b6dbfc`（命令位置の公開資料なし） · `00b6dbe0`（命令位置の公開資料なし）

~~~diff
- 00b6d7b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6d7b8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b6d7b8 bytes c1030054
- 00b6d7d4 ["INT_ADD", "register:40f0:8", ["const:b6d7d4:8", "const:4:8"]]
- 00b6d7d4 ["CALL", null, ["callee:00c5ba50:8"]]
+ 00b6dbfc ["INT_ADD", "register:40f0:8", ["const:b6dbfc:8", "const:4:8"]]
+ 00b6dbfc ["CALL", null, ["callee:00c5ba50:8"]]
- 00b6d7d4 bytes 9fb70394
+ 00b6dbfc bytes 95b70394
+ 00b6dbe0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6dbe0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b6dbe0 bytes c1030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116a8b373d21f4c8bcd0b53be3eef99d"></a>

### [`00b6d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md) → [`00b6dcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dcc0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b670.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b670.md)
- 新版 呼出元 1件 [`00c5ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba70.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d898) · [`00b6d8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d8b4) · [`00b6d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d898.md#insn-00b6d8c0)
- 新版 `00b6dcc0`（命令位置の公開資料なし） · `00b6dcdc`（命令位置の公開資料なし） · `00b6dce8`（命令位置の公開資料なし）

~~~diff
- 00b6d898 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d898 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6dcc0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6dcc0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6d898 bytes 610200b4
+ 00b6dcc0 bytes 610200b4
- 00b6d8b4 ["INT_ADD", "register:40f0:8", ["const:b6d8b4:8", "const:4:8"]]
- 00b6d8b4 ["CALL", null, ["callee:00c5ba70:8"]]
+ 00b6dcdc ["INT_ADD", "register:40f0:8", ["const:b6dcdc:8", "const:4:8"]]
+ 00b6dcdc ["CALL", null, ["callee:00c5ba70:8"]]
- 00b6d8b4 bytes 6fb70394
+ 00b6dcdc bytes 65b70394
- 00b6d8c0 ["INT_ADD", "register:40f0:8", ["const:b6d8c0:8", "const:4:8"]]
- 00b6d8c0 ["CALL", null, ["callee:00c5ba70:8"]]
+ 00b6dce8 ["INT_ADD", "register:40f0:8", ["const:b6dce8:8", "const:4:8"]]
+ 00b6dce8 ["CALL", null, ["callee:00c5ba70:8"]]
- 00b6d8c0 bytes 6cb70394
+ 00b6dce8 bytes 62b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d37ae37601a2fe1deeb0ab81e9c553cb"></a>

### [`00b6d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md) → [`00b6dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md)
- 新版 呼出元 1件 [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6d8fc",
      "incomplete_value": true,
      "site": "00b6d904",
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

- 旧版 [`00b6d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d904) · [`00b6d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d8e8) · [`00b6d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d8e8.md#insn-00b6d910)
- 新版 `00b6dd2c`（命令位置の公開資料なし） · `00b6dd10`（命令位置の公開資料なし） · `00b6dd38`（命令位置の公開資料なし）

~~~diff
- 00b6d904 ["INT_ADD", "register:40f0:8", ["const:b6d904:8", "const:4:8"]]
- 00b6d904 ["CALL", null, ["callee:00c5ba60:8"]]
+ 00b6dd2c ["INT_ADD", "register:40f0:8", ["const:b6dd2c:8", "const:4:8"]]
+ 00b6dd2c ["CALL", null, ["callee:00c5ba60:8"]]
- 00b6d904 bytes 57b70394
+ 00b6dd2c bytes 4db70394
- 00b6d8e8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d8e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6dd10 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6dd10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b6d8e8 bytes 610200b4
+ 00b6dd10 bytes 610200b4
- 00b6d910 ["INT_ADD", "register:40f0:8", ["const:b6d910:8", "const:4:8"]]
- 00b6d910 ["CALL", null, ["callee:00c5ba60:8"]]
+ 00b6dd38 ["INT_ADD", "register:40f0:8", ["const:b6dd38:8", "const:4:8"]]
+ 00b6dd38 ["CALL", null, ["callee:00c5ba60:8"]]
- 00b6d910 bytes 54b70394
+ 00b6dd38 bytes 4ab70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827d6798c5f2a9cbec9a43ec2140ee4a"></a>

### [`00b6d938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d938.md) → [`00b6dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4d0.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8d0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 52.63% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6ddc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ddb0",
      "incomplete_value": true,
      "site": "00b6ddb4",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d99c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dde4"
      ]
    ]
  ],
  "added": [
    [
      "00b6ddc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dde4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d938.md#insn-00b6d98c) · [`00b6d99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d938.md#insn-00b6d99c)
- 新版 `00b6ddb4`（命令位置の公開資料なし） · `00b6ddc4`（命令位置の公開資料なし）

~~~diff
- 00b6d98c ["INT_ADD", "register:40f0:8", ["const:b6d98c:8", "const:4:8"]]
- 00b6d98c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b6ddb4 ["INT_ADD", "register:40f0:8", ["const:b6ddb4:8", "const:4:8"]]
+ 00b6ddb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b6d98c bytes 49a80394
+ 00b6ddb4 bytes 3fa80394
- 00b6d99c ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b6d99c bytes 00010054
+ 00b6ddc4 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 00b6ddc4 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d39d3b746d7afbadd169665b1f9165a"></a>

### [`00b6d9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md) → [`00b6ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6ddf0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6de04",
      "incomplete_value": true,
      "site": "00b6de0c",
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
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9e4) · [`00b6d9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9c8) · [`00b6d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d9c8.md#insn-00b6d9f0)
- 新版 `00b6de0c`（命令位置の公開資料なし） · `00b6ddf0`（命令位置の公開資料なし） · `00b6de18`（命令位置の公開資料なし）

~~~diff
- 00b6d9e4 ["INT_ADD", "register:40f0:8", ["const:b6d9e4:8", "const:4:8"]]
- 00b6d9e4 ["CALL", null, ["callee:00c5ba90:8"]]
+ 00b6de0c ["INT_ADD", "register:40f0:8", ["const:b6de0c:8", "const:4:8"]]
+ 00b6de0c ["CALL", null, ["callee:00c5ba90:8"]]
- 00b6d9e4 bytes 2bb70394
+ 00b6de0c bytes 21b70394
- 00b6d9c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d9c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6ddf0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6ddf0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d9c8 bytes 610200b4
+ 00b6ddf0 bytes 610200b4
- 00b6d9f0 ["INT_ADD", "register:40f0:8", ["const:b6d9f0:8", "const:4:8"]]
- 00b6d9f0 ["CALL", null, ["callee:00c5ba90:8"]]
+ 00b6de18 ["INT_ADD", "register:40f0:8", ["const:b6de18:8", "const:4:8"]]
+ 00b6de18 ["CALL", null, ["callee:00c5ba90:8"]]
- 00b6d9f0 bytes 28b70394
+ 00b6de18 bytes 1eb70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb8258cd5581cdc6286333a91171f4a6"></a>

### [`00b6da18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md) → [`00b6de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de40.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6de54",
      "incomplete_value": true,
      "site": "00b6de5c",
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
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6da34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da34) · [`00b6da18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da18) · [`00b6da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da18.md#insn-00b6da40)
- 新版 `00b6de5c`（命令位置の公開資料なし） · `00b6de40`（命令位置の公開資料なし） · `00b6de68`（命令位置の公開資料なし）

~~~diff
- 00b6da34 ["INT_ADD", "register:40f0:8", ["const:b6da34:8", "const:4:8"]]
- 00b6da34 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b6de5c ["INT_ADD", "register:40f0:8", ["const:b6de5c:8", "const:4:8"]]
+ 00b6de5c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b6da34 bytes 1bb70394
+ 00b6de5c bytes 11b70394
- 00b6da18 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6da18 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6de40 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6de40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6da18 bytes 610200b4
+ 00b6de40 bytes 610200b4
- 00b6da40 ["INT_ADD", "register:40f0:8", ["const:b6da40:8", "const:4:8"]]
- 00b6da40 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b6de68 ["INT_ADD", "register:40f0:8", ["const:b6de68:8", "const:4:8"]]
+ 00b6de68 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b6da40 bytes 18b70394
+ 00b6de68 bytes 0eb70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d989f2fe16423b34925a3a1ef36acb57"></a>

### [`00b6dab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dab8.md) → [`00b6dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dee0.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md) · 呼出先 17件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)
- 新版 呼出元 1件 [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md) · 呼出先 17件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.13% / 新版 74.13%

CFGの説明率　旧版 36.92% / 新版 38.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_condition` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6daf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6db48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6dae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6daec",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b6daf0",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df10",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b6df14",
      "READ",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6df18",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dab8.md#insn-00b6dae8) · [`00b6daf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dab8.md#insn-00b6daf8) · [`00b6dafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dab8.md#insn-00b6dafc)

~~~diff
- 00b6dae8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b6dae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6dae8 bytes e81f00f9
- 00b6daf8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d90:8"]]
- 00b6daf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b6daf8 bytes 08930db9
- 00b6dafc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6dafc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6dafc bytes 690000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e39658099e213304ed7bd49e5b54fb"></a>

### [`00b6dec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md) → [`00b6e2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e2ec.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b920.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd20.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 80.82% / 新版 80.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e30c",
      "incomplete_value": true,
      "site": "00b6e30c",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e370",
      "incomplete_value": true,
      "site": "00b6e370",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e398",
      "incomplete_value": true,
      "site": "00b6e398",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b6e300",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e30c",
      "WRITE",
      [
        "storage",
        "01125d90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e318",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e300",
      "READ",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e30c",
      "WRITE",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e318",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6dee4) · [`00b6df14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6df14) · [`00b6df44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dec4.md#insn-00b6df44)
- 新版 `00b6e30c`（命令位置の公開資料なし） · `00b6e33c`（命令位置の公開資料なし） · `00b6e36c`（命令位置の公開資料なし）

~~~diff
- 00b6dee4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
- 00b6dee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6e30c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
+ 00b6e30c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b6dee4 bytes 09910db9
+ 00b6e30c bytes 099101b9
- 00b6df14 ["INT_ADD", "register:40f0:8", ["const:b6df14:8", "const:4:8"]]
- 00b6df14 ["CALL", null, ["callee:00c5b240:8"]]
+ 00b6e33c ["INT_ADD", "register:40f0:8", ["const:b6e33c:8", "const:4:8"]]
+ 00b6e33c ["CALL", null, ["callee:00c5b240:8"]]
- 00b6df14 bytes cbb30394
+ 00b6e33c bytes c1b30394
- 00b6df44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6df44 ["INT_ADD", "register:40f0:8", ["const:b6df44:8", "const:4:8"]]
- 00b6df44 ["CALLIND", null, ["register:0:8"]]
+ 00b6e36c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e36c ["INT_ADD", "register:40f0:8", ["const:b6e36c:8", "const:4:8"]]
+ 00b6e36c ["CALLIND", null, ["register:0:8"]]
- 00b6df44 bytes 00013fd6
+ 00b6e36c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e446d932fdc005dd41d5597d32236171"></a>

### [`00b6dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md) → [`00b6e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e410.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb20.md) · 呼出先 4件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b900.md)
- 新版 呼出元 1件 [`00c5bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf20.md) · 呼出先 4件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.72% / 新版 80.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e544",
      "incomplete_value": true,
      "site": "00b6e544",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e11c",
      "incomplete_value": true,
      "site": "00b6e11c",
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
            "const:141:8"
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
      "definition_site": "00b6e548",
      "incomplete_value": true,
      "site": "00b6e548",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e120",
      "incomplete_value": true,
      "site": "00b6e120",
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
            "const:144:8"
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
      "definition_site": "00b6e430",
      "incomplete_value": true,
      "site": "00b6e430",
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
      "definition_site": "00b6e008",
      "incomplete_value": true,
      "site": "00b6e008",
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
      "00b6e424",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e038"
      ]
    ],
    [
      "00b6e454",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e424",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e460"
      ]
    ],
    [
      "00b6e454",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md#insn-00b6e04c) · [`00b6e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md#insn-00b6e080) · [`00b6dff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6dfe8.md#insn-00b6dff8)
- 新版 `00b6e474`（命令位置の公開資料なし） · `00b6e4a8`（命令位置の公開資料なし） · `00b6e420`（命令位置の公開資料なし）

~~~diff
- 00b6e04c ["INT_ADD", "register:40f0:8", ["const:b6e04c:8", "const:4:8"]]
- 00b6e04c ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b6e474 ["INT_ADD", "register:40f0:8", ["const:b6e474:8", "const:4:8"]]
+ 00b6e474 ["CALL", null, ["callee:00c5aba0:8"]]
- 00b6e04c bytes d5b10394
+ 00b6e474 bytes cbb10394
- 00b6e080 ["INT_ADD", "register:40f0:8", ["const:b6e080:8", "const:4:8"]]
- 00b6e080 ["CALL", null, ["callee:005762b8:8"]]
+ 00b6e4a8 ["INT_ADD", "register:40f0:8", ["const:b6e4a8:8", "const:4:8"]]
+ 00b6e4a8 ["CALL", null, ["callee:005762b8:8"]]
- 00b6e080 bytes 7e20e897
+ 00b6e4a8 bytes 841fe897
- 00b6dff8 ["COPY", "register:40b0:8", ["const:1125000:8"]]
+ 00b6e420 ["COPY", "register:40b0:8", ["const:1126000:8"]]
- 00b6dff8 bytes d62d0090
+ 00b6e420 bytes d62d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40331a0a249cf5a139de2d7c51882eb"></a>

### [`00b6e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md) → [`00b6e55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b6e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00b6e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e594",
      "incomplete_value": true,
      "site": "00b6e5a4",
      "value": [
        "LOAD",
        "8",
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
                "const:1b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e598",
      "incomplete_value": true,
      "site": "00b6e5a4",
      "value": [
        "LOAD",
        "8",
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
                "const:1c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e5d8",
      "incomplete_value": true,
      "site": "00b6e5dc",
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
      "00b6e594",
      "READ",
      [
        "storage",
        "01125db8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e598",
      "READ",
      [
        "storage",
        "01125dc8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e5d0",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e594",
      "READ",
      [
        "storage",
        "011261b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e598",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e5d0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e17c) · [`00b6e1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e1b4) · [`00b6e1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md#insn-00b6e1d0)
- 新版 `00b6e5a4`（命令位置の公開資料なし） · `00b6e5dc`（命令位置の公開資料なし） · `00b6e5f8`（命令位置の公開資料なし）

~~~diff
- 00b6e17c ["INT_ADD", "register:40f0:8", ["const:b6e17c:8", "const:4:8"]]
- 00b6e17c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00b6e5a4 ["INT_ADD", "register:40f0:8", ["const:b6e5a4:8", "const:4:8"]]
+ 00b6e5a4 ["CALL", null, ["callee:00c5bf40:8"]]
- 00b6e17c bytes 71b60394
+ 00b6e5a4 bytes 67b60394
- 00b6e1b4 ["INT_ADD", "register:40f0:8", ["const:b6e1b4:8", "const:4:8"]]
- 00b6e1b4 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00b6e5dc ["INT_ADD", "register:40f0:8", ["const:b6e5dc:8", "const:4:8"]]
+ 00b6e5dc ["CALL", null, ["callee:00c5ae00:8"]]
- 00b6e1b4 bytes 13b20394
+ 00b6e5dc bytes 09b20394
- 00b6e1d0 ["INT_ADD", "register:40f0:8", ["const:b6e1d0:8", "const:4:8"]]
- 00b6e1d0 ["CALL", null, ["callee:00c5ada0:8"]]
+ 00b6e5f8 ["INT_ADD", "register:40f0:8", ["const:b6e5f8:8", "const:4:8"]]
+ 00b6e5f8 ["CALL", null, ["callee:00c5ada0:8"]]
- 00b6e1d0 bytes f4b10394
+ 00b6e5f8 bytes eab10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96a12e0901cbc082852c85fa0d1ccea"></a>

### [`00b6e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md) → [`00b6e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b910.md) · 呼出先 14件 [`00b6e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e134.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md)
- 新版 呼出元 1件 [`00c5bd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd10.md) · 呼出先 14件 [`00b6e55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e70c",
      "incomplete_value": true,
      "site": "00b6e70c",
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
      "definition_site": "00b6e2e4",
      "incomplete_value": true,
      "site": "00b6e2e4",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e728",
      "incomplete_value": true,
      "site": "00b6e728",
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
      "definition_site": "00b6e300",
      "incomplete_value": true,
      "site": "00b6e300",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e7bc",
      "incomplete_value": true,
      "site": "00b6e7bc",
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
      "00b6e704",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e724",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e758",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e704",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e724",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e758",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md#insn-00b6e344) · [`00b6e368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md#insn-00b6e368) · [`00b6e3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e2a8.md#insn-00b6e3a4)
- 新版 `00b6e76c`（命令位置の公開資料なし） · `00b6e790`（命令位置の公開資料なし） · `00b6e7cc`（命令位置の公開資料なし）

~~~diff
- 00b6e344 ["INT_ADD", "register:40f0:8", ["const:b6e344:8", "const:4:8"]]
- 00b6e344 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00b6e76c ["INT_ADD", "register:40f0:8", ["const:b6e76c:8", "const:4:8"]]
+ 00b6e76c ["CALL", null, ["callee:00c5ae40:8"]]
- 00b6e344 bytes bfb10394
+ 00b6e76c bytes b5b10394
- 00b6e368 ["INT_ADD", "register:40f0:8", ["const:b6e368:8", "const:4:8"]]
- 00b6e368 ["CALL", null, ["callee:00c5bc70:8"]]
+ 00b6e790 ["INT_ADD", "register:40f0:8", ["const:b6e790:8", "const:4:8"]]
+ 00b6e790 ["CALL", null, ["callee:00c5bc70:8"]]
- 00b6e368 bytes 42b50394
+ 00b6e790 bytes 38b50394
- 00b6e3a4 ["INT_ADD", "register:40f0:8", ["const:b6e3a4:8", "const:4:8"]]
- 00b6e3a4 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00b6e7cc ["INT_ADD", "register:40f0:8", ["const:b6e7cc:8", "const:4:8"]]
+ 00b6e7cc ["CALL", null, ["callee:00c5aba0:8"]]
- 00b6e3a4 bytes ffb00394
+ 00b6e7cc bytes f5b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba76905b7bfbbefe16aadaf09f6f649"></a>

### [`00b6e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e638.md) → [`00b6ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea60.md) _ZN11flatbuffers19FLATBUFFERS_VERSIONEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b6ea64",
      "incomplete_value": false,
      "site": "00b6ea68",
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
            "const:e74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e63c",
      "incomplete_value": false,
      "site": "00b6e640",
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
            "const:e34:8"
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
      "00b6ea64",
      "DATA",
      [
        "storage",
        "002bbe34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ea64",
      "DATA",
      [
        "storage",
        "002bbe74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e638.md#insn-00b6e63c)
- 新版 `00b6ea64`（命令位置の公開資料なし）

~~~diff
- 00b6e63c ["COPY", "tmp:0:8", ["const:e34:8"]]
- 00b6e63c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e63c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e63c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6ea64 ["COPY", "tmp:0:8", ["const:e74:8"]]
+ 00b6ea64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ea64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ea64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e63c bytes 00d03891
+ 00b6ea64 bytes 00d03991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8f9ae09a067b4dcaa951d1cd50cd83c"></a>

### [`00b6e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e644.md) → [`00b6ea6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea6c.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 1件 [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6eabc",
      "incomplete_value": false,
      "site": "00b6eac8",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e694",
      "incomplete_value": false,
      "site": "00b6e6a0",
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
            "const:ba0:8"
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
      "definition_site": "00b6eb64",
      "incomplete_value": false,
      "site": "00b6eb70",
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
            "const:9c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e73c",
      "incomplete_value": false,
      "site": "00b6e748",
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
            "const:987:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6eb84",
      "incomplete_value": false,
      "site": "00b6eb90",
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
            "const:76e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e75c",
      "incomplete_value": false,
      "site": "00b6e768",
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
            "const:72e:8"
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
      "00b6eabc",
      "PARAM",
      [
        "storage",
        "002b4ba0",
        null,
        null
      ]
    ],
    [
      "00b6eb64",
      "PARAM",
      [
        "storage",
        "002b0987",
        null,
        null
      ]
    ],
    [
      "00b6eb84",
      "PARAM",
      [
        "storage",
        "002bd72e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6eabc",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ],
    [
      "00b6eb64",
      "PARAM",
      [
        "storage",
        "002b09c7",
        null,
        null
      ]
    ],
    [
      "00b6eb84",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e644.md#insn-00b6e6a0) · [`00b6e748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e644.md#insn-00b6e748) · [`00b6e768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e644.md#insn-00b6e768)
- 新版 `00b6eac8`（命令位置の公開資料なし） · `00b6eb70`（命令位置の公開資料なし） · `00b6eb90`（命令位置の公開資料なし）

~~~diff
- 00b6e6a0 ["INT_ADD", "register:40f0:8", ["const:b6e6a0:8", "const:4:8"]]
- 00b6e6a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6eac8 ["INT_ADD", "register:40f0:8", ["const:b6eac8:8", "const:4:8"]]
+ 00b6eac8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6e6a0 bytes 38a50394
+ 00b6eac8 bytes 2ea50394
- 00b6e748 ["INT_ADD", "register:40f0:8", ["const:b6e748:8", "const:4:8"]]
- 00b6e748 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6eb70 ["INT_ADD", "register:40f0:8", ["const:b6eb70:8", "const:4:8"]]
+ 00b6eb70 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6e748 bytes 0ea50394
+ 00b6eb70 bytes 04a50394
- 00b6e768 ["INT_ADD", "register:40f0:8", ["const:b6e768:8", "const:4:8"]]
- 00b6e768 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6eb90 ["INT_ADD", "register:40f0:8", ["const:b6eb90:8", "const:4:8"]]
+ 00b6eb90 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6e768 bytes 06a50394
+ 00b6eb90 bytes fca40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d898e3be86897ed6d87d25d7f994ded"></a>

### [`00b6e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md) → [`00b6ecf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ecf8.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ed54",
      "incomplete_value": true,
      "site": "00b6ed68",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ed4c",
      "incomplete_value": true,
      "site": "00b6ed6c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6eddc",
      "incomplete_value": true,
      "site": "00b6ede8",
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
      "00b6ed2c",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ed30",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ed68",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6ed2c",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ed30",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ed68",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e904) · [`00b6e908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e908) · [`00b6e94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e8d0.md#insn-00b6e94c)
- 新版 `00b6ed2c`（命令位置の公開資料なし） · `00b6ed30`（命令位置の公開資料なし） · `00b6ed74`（命令位置の公開資料なし）

~~~diff
- 00b6e904 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:818:8"]]
- 00b6e904 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ed2c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c18:8"]]
+ 00b6ed2c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e904 bytes 5a0f44f9
+ 00b6ed2c bytes 5a0f46f9
- 00b6e908 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:440:8"]]
- 00b6e908 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ed30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
+ 00b6ed30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e908 bytes 082142f9
+ 00b6ed30 bytes 082144f9
- 00b6e94c ["INT_ADD", "register:40f0:8", ["const:b6e94c:8", "const:4:8"]]
- 00b6e94c ["CALL", null, ["callee:00c581e0:8"]]
+ 00b6ed74 ["INT_ADD", "register:40f0:8", ["const:b6ed74:8", "const:4:8"]]
+ 00b6ed74 ["CALL", null, ["callee:00c581e0:8"]]
- 00b6e94c bytes 25a50394
+ 00b6ed74 bytes 1ba50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45ab0014544f4d19fc6ba18b074990dd"></a>

### [`00b6ea3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ea3c.md) → [`00b6ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ee64.md) _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc00.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e20.md)
- 新版 呼出元 1件 [`00c5c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c000.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6eebc",
      "incomplete_value": true,
      "site": "00b6eed0",
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
      "definition_site": "00b6ea94",
      "incomplete_value": true,
      "site": "00b6eaa8",
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
      "definition_site": "00b6eeb4",
      "incomplete_value": true,
      "site": "00b6eed4",
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
      "definition_site": "00b6ea8c",
      "incomplete_value": true,
      "site": "00b6eaac",
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
      "definition_site": "00b6ef44",
      "incomplete_value": true,
      "site": "00b6ef50",
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
      "definition_site": "00b6eb1c",
      "incomplete_value": true,
      "site": "00b6eb28",
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
      "00b6ee94",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ee98",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b6eed0",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6ee94",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ee98",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b6eed0",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ea3c.md#insn-00b6ea6c) · [`00b6ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ea3c.md#insn-00b6ea70) · [`00b6eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ea3c.md#insn-00b6eab4)
- 新版 `00b6ee94`（命令位置の公開資料なし） · `00b6ee98`（命令位置の公開資料なし） · `00b6eedc`（命令位置の公開資料なし）

~~~diff
- 00b6ea6c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:818:8"]]
- 00b6ea6c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ee94 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c18:8"]]
+ 00b6ee94 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ea6c bytes 5a0f44f9
+ 00b6ee94 bytes 5a0f46f9
- 00b6ea70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:440:8"]]
- 00b6ea70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ee98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
+ 00b6ee98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ea70 bytes 082142f9
+ 00b6ee98 bytes 082144f9
- 00b6eab4 ["INT_ADD", "register:40f0:8", ["const:b6eab4:8", "const:4:8"]]
- 00b6eab4 ["CALL", null, ["callee:00c581e0:8"]]
+ 00b6eedc ["INT_ADD", "register:40f0:8", ["const:b6eedc:8", "const:4:8"]]
+ 00b6eedc ["CALL", null, ["callee:00c581e0:8"]]
- 00b6eab4 bytes cba40394
+ 00b6eedc bytes c1a40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c56e006991dc891b0d5aa9d8250f3ab"></a>

### [`00b6ec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md) → [`00b6f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f0ac.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f0d8",
      "incomplete_value": false,
      "site": "00b6f0e0",
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
            "const:bac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ecb0",
      "incomplete_value": false,
      "site": "00b6ecb8",
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
            "const:adf:8"
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
      "00b6f0d8",
      "PARAM",
      [
        "storage",
        "002a0adf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f0d8",
      "PARAM",
      [
        "storage",
        "002a0bac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ecb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md#insn-00b6ecb8) · [`00b6ecb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md#insn-00b6ecb0) · [`00b6ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ec84.md#insn-00b6ecc4)
- 新版 `00b6f0e0`（命令位置の公開資料なし） · `00b6f0d8`（命令位置の公開資料なし） · `00b6f0ec`（命令位置の公開資料なし）

~~~diff
- 00b6ecb8 ["INT_ADD", "register:40f0:8", ["const:b6ecb8:8", "const:4:8"]]
- 00b6ecb8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b6f0e0 ["INT_ADD", "register:40f0:8", ["const:b6f0e0:8", "const:4:8"]]
+ 00b6f0e0 ["CALL", null, ["callee:00c580b0:8"]]
- 00b6ecb8 bytes fea30394
+ 00b6f0e0 bytes f4a30394
- 00b6ecb0 ["COPY", "tmp:0:8", ["const:adf:8"]]
- 00b6ecb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ecb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ecb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6f0d8 ["COPY", "tmp:0:8", ["const:bac:8"]]
+ 00b6f0d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f0d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f0d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ecb0 bytes 007c2b91
+ 00b6f0d8 bytes 00b02e91
- 00b6ecc4 ["INT_ADD", "register:40f0:8", ["const:b6ecc4:8", "const:4:8"]]
- 00b6ecc4 ["CALL", null, ["callee:00c5c770:8"]]
+ 00b6f0ec ["INT_ADD", "register:40f0:8", ["const:b6f0ec:8", "const:4:8"]]
+ 00b6f0ec ["CALL", null, ["callee:00c5c770:8"]]
- 00b6ecc4 bytes abb50394
+ 00b6f0ec bytes a1b50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660c03a229d6270ef7fd6c0d516d2281"></a>

### [`00b6ed04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed04.md) → [`00b6f12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f12c.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f154",
      "incomplete_value": false,
      "site": "00b6f160",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ed2c",
      "incomplete_value": false,
      "site": "00b6ed38",
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
            "const:ae9:8"
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
      "00b6f154",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f154",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed04.md#insn-00b6ed38) · [`00b6ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed04.md#insn-00b6ed2c) · [`00b6ed44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed04.md#insn-00b6ed44)
- 新版 `00b6f160`（命令位置の公開資料なし） · `00b6f154`（命令位置の公開資料なし） · `00b6f16c`（命令位置の公開資料なし）

~~~diff
- 00b6ed38 ["INT_ADD", "register:40f0:8", ["const:b6ed38:8", "const:4:8"]]
- 00b6ed38 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b6f160 ["INT_ADD", "register:40f0:8", ["const:b6f160:8", "const:4:8"]]
+ 00b6f160 ["CALL", null, ["callee:00c580b0:8"]]
- 00b6ed38 bytes dea30394
+ 00b6f160 bytes d4a30394
- 00b6ed2c ["COPY", "tmp:0:8", ["const:ae9:8"]]
- 00b6ed2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ed2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ed2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6f154 ["COPY", "tmp:0:8", ["const:bb6:8"]]
+ 00b6f154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ed2c bytes 00a42b91
+ 00b6f154 bytes 00d82e91
- 00b6ed44 ["INT_ADD", "register:40f0:8", ["const:b6ed44:8", "const:4:8"]]
- 00b6ed44 ["CALL", null, ["callee:00c5c770:8"]]
+ 00b6f16c ["INT_ADD", "register:40f0:8", ["const:b6f16c:8", "const:4:8"]]
+ 00b6f16c ["CALL", null, ["callee:00c5c770:8"]]
- 00b6ed44 bytes 8bb50394
+ 00b6f16c bytes 81b50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff780987cb61ce46e87bf61c9374595"></a>

### [`00b6ed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md) → [`00b6f1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f1b0.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c120.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)
- 新版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c520.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f1e8",
      "incomplete_value": false,
      "site": "00b6f1f8",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6edc0",
      "incomplete_value": false,
      "site": "00b6edd0",
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
            "const:bb8:8"
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
      "definition_site": "00b6f208",
      "incomplete_value": false,
      "site": "00b6f224",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ede0",
      "incomplete_value": false,
      "site": "00b6edfc",
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
            "const:49d:8"
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
      "definition_site": "00b6f248",
      "incomplete_value": false,
      "site": "00b6f250",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ee20",
      "incomplete_value": false,
      "site": "00b6ee28",
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
            "const:ae9:8"
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
      "00b6f1e8",
      "PARAM",
      [
        "storage",
        "002c1bb8",
        null,
        "string"
      ]
    ],
    [
      "00b6f208",
      "PARAM",
      [
        "storage",
        "002a849d",
        null,
        "string"
      ]
    ],
    [
      "00b6f248",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f1e8",
      "PARAM",
      [
        "storage",
        "002c1bf8",
        null,
        "string"
      ]
    ],
    [
      "00b6f208",
      "PARAM",
      [
        "storage",
        "002a856a",
        null,
        "string"
      ]
    ],
    [
      "00b6f248",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6edd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md#insn-00b6edd0) · [`00b6edfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md#insn-00b6edfc) · [`00b6ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md#insn-00b6ee28)
- 新版 `00b6f1f8`（命令位置の公開資料なし） · `00b6f224`（命令位置の公開資料なし） · `00b6f250`（命令位置の公開資料なし）

~~~diff
- 00b6edd0 ["INT_ADD", "register:40f0:8", ["const:b6edd0:8", "const:4:8"]]
- 00b6edd0 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b6f1f8 ["INT_ADD", "register:40f0:8", ["const:b6f1f8:8", "const:4:8"]]
+ 00b6f1f8 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b6edd0 bytes 80a70394
+ 00b6f1f8 bytes 76a70394
- 00b6edfc ["INT_ADD", "register:40f0:8", ["const:b6edfc:8", "const:4:8"]]
- 00b6edfc ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6f224 ["INT_ADD", "register:40f0:8", ["const:b6f224:8", "const:4:8"]]
+ 00b6f224 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6edfc bytes 61a30394
+ 00b6f224 bytes 57a30394
- 00b6ee28 ["INT_ADD", "register:40f0:8", ["const:b6ee28:8", "const:4:8"]]
- 00b6ee28 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b6f250 ["INT_ADD", "register:40f0:8", ["const:b6f250:8", "const:4:8"]]
+ 00b6f250 ["CALL", null, ["callee:00c580b0:8"]]
- 00b6ee28 bytes a2a30394
+ 00b6f250 bytes 98a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6b04802a6ee0f3daadf0d405a7c8497"></a>

### [`00b6f294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md) → [`00b6f6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f6bc.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0c0.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4c0.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.31% / 新版 97.31%

CFGの説明率　旧版 81.03% / 新版 77.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f4a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6f8d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f748",
      "incomplete_value": false,
      "site": "00b6f758",
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
            "const:68c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f320",
      "incomplete_value": false,
      "site": "00b6f330",
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
            "const:64c:8"
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
      "unmatched:00b6f320",
      "PARAM",
      [
        "storage",
        "002be64c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6f340",
      "PARAM",
      [
        "storage",
        "002a2a33",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6f380",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f748",
      "PARAM",
      [
        "storage",
        "002be68c",
        null,
        "string"
      ]
    ],
    [
      "00b6f768",
      "PARAM",
      [
        "storage",
        "002a2b00",
        null,
        "string"
      ]
    ],
    [
      "00b6f7a8",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f330) · [`00b6f35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f35c) · [`00b6f388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f294.md#insn-00b6f388)
- 新版 `00b6f758`（命令位置の公開資料なし） · `00b6f784`（命令位置の公開資料なし） · `00b6f7b0`（命令位置の公開資料なし）

~~~diff
- 00b6f330 ["INT_ADD", "register:40f0:8", ["const:b6f330:8", "const:4:8"]]
- 00b6f330 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b6f758 ["INT_ADD", "register:40f0:8", ["const:b6f758:8", "const:4:8"]]
+ 00b6f758 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b6f330 bytes 28a60394
+ 00b6f758 bytes 1ea60394
- 00b6f35c ["INT_ADD", "register:40f0:8", ["const:b6f35c:8", "const:4:8"]]
- 00b6f35c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6f784 ["INT_ADD", "register:40f0:8", ["const:b6f784:8", "const:4:8"]]
+ 00b6f784 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6f35c bytes 09a20394
+ 00b6f784 bytes ffa10394
- 00b6f388 ["INT_ADD", "register:40f0:8", ["const:b6f388:8", "const:4:8"]]
- 00b6f388 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b6f7b0 ["INT_ADD", "register:40f0:8", ["const:b6f7b0:8", "const:4:8"]]
+ 00b6f7b0 ["CALL", null, ["callee:00c580b0:8"]]
- 00b6f388 bytes 4aa20394
+ 00b6f7b0 bytes 40a20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02f6d3cc05e4cc532aa251e201e80815"></a>

### [`00b6f57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f57c.md) → [`00b6f9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f9a4.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c250.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c370.md)
- 新版 呼出元 1件 [`00c5c650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c650.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 58.82% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f584"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6f580",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6f584",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6f588",
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
      "00b6f9a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6f9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6f9b0",
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

- 旧版 [`00b6f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f57c.md#insn-00b6f580) · [`00b6f584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f57c.md#insn-00b6f584) · [`00b6f588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f57c.md#insn-00b6f588)

~~~diff
- 00b6f580 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b6f580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b6f580 bytes f52300f9
- 00b6f584 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6f584 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6f584 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b6f584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6f584 bytes f44f05a9
- 00b6f588 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6f588 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6f588 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b6f588 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6f588 bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7fc58b69640d24a1370caef75933013"></a>

### [`00b6f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md) → [`00b6fab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6fab8.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) · 呼出先 14件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)
- 新版 呼出元 1件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) · 呼出先 14件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.79% / 新版 76.79%

CFGの説明率　旧版 47.96% / 新版 47.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 15件, `store_value` 6件, `unresolved_branch_alignment` 44件, `unresolved_call_alignment` 13件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 30件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b703f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6f6d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fb30"
      ]
    ],
    [
      "00b6fba8",
      "DATA",
      [
        "storage",
        "0030de6e",
        "switchD_00b6f788::switchdataD_0030de6e",
        "ushort"
      ]
    ],
    [
      "unmatched:00b6f850",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70ef4"
      ]
    ]
  ],
  "added": [
    [
      "00b6fb00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fb30"
      ]
    ],
    [
      "00b6fba8",
      "DATA",
      [
        "storage",
        "0030deae",
        "switchD_00b6fbb0::switchdataD_0030deae",
        "ushort"
      ]
    ],
    [
      "00b6fc78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70ef4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md#insn-00b7012c) · [`00b70334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md#insn-00b70334) · [`00b703f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md#insn-00b703f0)
- 新版 `00b70554`（命令位置の公開資料なし） · `00b7075c`（命令位置の公開資料なし）

~~~diff
- 00b7012c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b7012c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b7012c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b7012c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b70554 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b70554 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b70554 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b70554 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b7012c bytes 28130036
+ 00b70554 bytes 28130036
- 00b70334 ["BRANCH", null, ["local:b240:8"]]
+ 00b7075c ["BRANCH", null, ["local:b241:8"]]
- 00b70334 bytes 2c000014
+ 00b7075c bytes 2c000014
- 00b703f0 ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00b703f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b703f0 bytes 680300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34fb092657d88939b86f13e17ac6b554"></a>

### [`00b70d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70d74.md) → [`00b7119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7119c.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md) · 呼出先 12件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md) · 呼出先 12件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 52.70% / 新版 48.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b70d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70da0",
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
      "00b711ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b711b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b711c8",
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

- 旧版 [`00b70d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70d74.md#insn-00b70d84) · [`00b70d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70d74.md#insn-00b70d88) · [`00b70da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70d74.md#insn-00b70da0)

~~~diff
- 00b70d84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b70d84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b70d84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b70d84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70d84 bytes f44f0ea9
- 00b70d88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b70d88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b70d88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b70d88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70d88 bytes fd7b0fa9
- 00b70da0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b70da0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b70da0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b70da0 bytes a9831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d120ced717288933f246684950f4eaa"></a>

### [`00b7112c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7112c.md) → [`00b71554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71554.md) _ZN11flatbuffers6Parser16ParseNamespacingEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c200.md) · 呼出先 4件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md) [`00c5c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c350.md)
- 新版 呼出元 1件 [`00c5c600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c600.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 23.53% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71130"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7112c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71130",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71134",
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
      "00b71554",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b71558",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b7155c",
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

- 旧版 [`00b7112c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7112c.md#insn-00b7112c) · [`00b71130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7112c.md#insn-00b71130) · [`00b71134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7112c.md#insn-00b71134)

~~~diff
- 00b7112c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b7112c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b7112c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b7112c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7112c bytes fa67bba9
- 00b71130 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b71130 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b71130 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b71130 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71130 bytes f85f01a9
- 00b71134 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b71134 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b71134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b71134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71134 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a98ec14a522416fde9a89c2bcf490080"></a>

### [`00b71234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71234.md) → [`00b7165c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7165c.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c050.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md)
- 新版 呼出元 1件 [`00c5c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c450.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 41.38% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7125c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71438"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b71684"
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
      "unmatched:00b7125c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71750"
      ]
    ]
  ],
  "added": [
    [
      "00b71684",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b7172c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71750"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7125c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71234.md#insn-00b7125c) · [`00b71304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71234.md#insn-00b71304) · [`00b713ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71234.md#insn-00b713ec)

~~~diff
- 00b7125c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b7125c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b7125c bytes e81700f9
- 00b71304 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b71304 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b71304 bytes 21010054
- 00b713ec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b713ec ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b713ec ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b713ec ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b713ec bytes 29018c9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d9299b558dea356bf22811ace15ddf"></a>

### [`00b71524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71524.md) → [`00b7194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7194c.md) _ZNK11flatbuffers6Parser32LookupStructThruParentNamespacesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5e0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md)
- 新版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9e0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 50.79% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7152c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71528",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7152c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71530",
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
      "00b71950",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b71954",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b71958",
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

- 旧版 [`00b71528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71524.md#insn-00b71528) · [`00b7152c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71524.md#insn-00b7152c) · [`00b71530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71524.md#insn-00b71530)

~~~diff
- 00b71528 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b71528 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b71528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b71528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71528 bytes fc6f03a9
- 00b7152c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b7152c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b7152c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b7152c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7152c bytes fa6704a9
- 00b71530 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b71530 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b71530 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b71530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71530 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8446f172ee205ad9fe96a6090f0c1901"></a>

### [`00b717e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b717e4.md) → [`00b71c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71c0c.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1a0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5a0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 45.95% / 新版 48.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71838"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71814",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71834",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71838",
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
      "00b71c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b71c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b71c60",
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

- 旧版 [`00b71814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b717e4.md#insn-00b71814) · [`00b71834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b717e4.md#insn-00b71834) · [`00b71838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b717e4.md#insn-00b71838)

~~~diff
- 00b71814 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b71814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b71814 bytes e90f00f9
- 00b71834 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b71834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b71834 bytes e80b00f9
- 00b71838 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b71838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b71838 bytes e003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49775cbc04fde9c979df865b5b8d2db9"></a>

### [`00b7198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md) → [`00b71db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71db4.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c260.md) · 呼出先 17件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00c5c660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c660.md) · 呼出先 17件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.14% / 新版 90.14%

CFGの説明率　旧版 58.82% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b719a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b719a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b719c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b719a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b719c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71a40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7209c"
      ]
    ]
  ],
  "added": [
    [
      "00b71dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b71de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b71e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7209c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b719a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md#insn-00b719a4) · [`00b719c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md#insn-00b719c0) · [`00b71a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md#insn-00b71a40)

~~~diff
- 00b719a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b719a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b719a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b719a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b719a4 bytes fd7b0aa9
- 00b719c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b719c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b719c0 bytes e82700f9
- 00b71a40 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b71a40 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00b71a40 bytes a91100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f2f20c3a385ae8fe7d36cf54fff756"></a>

### [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) → [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) [`00c5c3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3d0.md) · 呼出先 12件 [`00b71e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) [`00c5c7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7d0.md) · 呼出先 12件 [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.22% / 新版 62.22%

CFGの説明率　旧版 19.70% / 新版 20.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 2件, `unresolved_branch_alignment` 34件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 36件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71e28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71e2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71e30",
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
      "00b72250",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b72254",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b72258",
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

- 旧版 [`00b71e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md#insn-00b71e28) · [`00b71e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md#insn-00b71e2c) · [`00b71e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b71e24.md#insn-00b71e30)

~~~diff
- 00b71e28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b71e28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b71e28 bytes f93300f9
- 00b71e2c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b71e2c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b71e2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b71e2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71e2c bytes f85f07a9
- 00b71e30 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b71e30 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b71e30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b71e30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71e30 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a43ab811402b84b8566723a23bb65e"></a>

### [`00b725e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b725e0.md) → [`00b72a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72a08.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c380.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5c780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c780.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.72% / 新版 74.72%

CFGの説明率　旧版 25.93% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b725e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b725e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b725e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b725e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b725e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b725ec",
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
      "00b72a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b72a10",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b72a14",
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

- 旧版 [`00b725e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b725e0.md#insn-00b725e4) · [`00b725e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b725e0.md#insn-00b725e8) · [`00b725ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b725e0.md#insn-00b725ec)

~~~diff
- 00b725e4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b725e4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b725e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b725e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b725e4 bytes fc6f04a9
- 00b725e8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b725e8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b725e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b725e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b725e8 bytes fa6705a9
- 00b725ec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b725ec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b725ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b725ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b725ec bytes f85f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c97f2a80201ce3eac2351c02a7fd5e"></a>

### [`00b728a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b728a8.md) → [`00b72cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72cd0.md) _ZN11flatbuffers10InlineSizeERKNS_4TypeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbb0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbb0.md)
- 新版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfb0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.02% / 新版 83.02%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72d6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b728ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b728ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72d50"
      ]
    ],
    [
      "unmatched:00b72900",
      "DATA",
      [
        "storage",
        "0030e043",
        "switchD_00b7290c::switchdataD_0030e043",
        "byte"
      ]
    ],
    [
      "unmatched:00b72944",
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
      "00b72d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72d50"
      ]
    ],
    [
      "00b72d28",
      "DATA",
      [
        "storage",
        "0030e083",
        "switchD_00b72d34::switchdataD_0030e083",
        "byte"
      ]
    ],
    [
      "00b72d6c",
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

- 旧版 [`00b728ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b728a8.md#insn-00b728ec) · [`00b72944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b728a8.md#insn-00b72944) · [`00b7294c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b728a8.md#insn-00b7294c)
- 新版 `00b72d74`（命令位置の公開資料なし）

~~~diff
- 00b728ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b728ec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b728ec ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00b728ec bytes e8010054
- 00b72944 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b72944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b72944 bytes e003813c
- 00b7294c ["INT_ADD", "register:40f0:8", ["const:b7294c:8", "const:4:8"]]
- 00b7294c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b72d74 ["INT_ADD", "register:40f0:8", ["const:b72d74:8", "const:4:8"]]
+ 00b72d74 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b7294c bytes 99a40394
+ 00b72d74 bytes 8fa40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f6dd45f216dccfb056f1e4fd3d96075"></a>

### [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) → [`00b72f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72f5c.md) _ZN11flatbuffers6Parser10ParseFieldERNS_9StructDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c070.md) · 呼出先 27件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5c470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c470.md) · 呼出先 27件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.74% / 新版 65.74%

CFGの説明率　旧版 26.86% / 新版 27.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 31件, `store_condition` 5件, `store_destination` 1件, `store_value` 28件, `unresolved_branch_alignment` 75件, `unresolved_call_alignment` 45件, `unresolved_store_alignment` 211件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72b88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72c2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72b70",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b72b7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72fbc"
      ]
    ],
    [
      "unmatched:00b72b88",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b72f98",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "00b72fa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72fbc"
      ]
    ],
    [
      "00b72fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md#insn-00b72b70) · [`00b72b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md#insn-00b72b88) · [`00b72c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md#insn-00b72c2c)

~~~diff
- 00b72b70 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b72b70 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b72b70 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff30:8"]]
- 00b72b70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:8"]]
- 00b72b70 bytes bf0313f8
- 00b72b88 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b72b88 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff40:8"]]
- 00b72b88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b72b88 bytes a80314f8
- 00b72c2c ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffff50:8"]]
- 00b72c2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b72c2c bytes a003953c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767117f3ba743aa1a7570ca471f42a25"></a>

### [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) → [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) _ZN11flatbuffers6Parser16ParseSingleValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c230.md) · 呼出先 35件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)
- 新版 呼出元 1件 [`00c5c630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c630.md) · 呼出先 35件 [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.07% / 新版 85.07%

CFGの説明率　旧版 43.70% / 新版 44.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 44件, `store_condition` 5件, `store_value` 2件, `unresolved_branch_alignment` 28件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7501c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7501c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75020"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7501c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b75020",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b75024",
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
      "00b75444",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b75448",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b7544c",
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

- 旧版 [`00b7501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md#insn-00b7501c) · [`00b75020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md#insn-00b75020) · [`00b75024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md#insn-00b75024)

~~~diff
- 00b7501c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b7501c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b7501c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b7501c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7501c bytes fc6f12a9
- 00b75020 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b75020 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b75020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b75020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b75020 bytes fa6713a9
- 00b75024 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b75024 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b75024 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b75024 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b75024 bytes f85f14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9f9eca230622993c98fda59db9d7fd"></a>

### [`00b76214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76214.md) → [`00b7663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b7663c.md) _ZN11flatbuffers6Parser13ParseMetaDataEPNS_11SymbolTableINS_5ValueEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c150.md) · 呼出先 13件 [`00639ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c550.md) · 呼出先 13件 [`00639af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639af4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 70.00% / 新版 69.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b764d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b768fc"
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
      "00b767a4",
      "PARAM",
      [
        "storage",
        "002b803b",
        null,
        null
      ]
    ],
    [
      "unmatched:00b763b8",
      "PARAM",
      [
        "storage",
        "002be7d3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b763d4",
      "PARAM",
      [
        "storage",
        "002a0adf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b767a4",
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ],
    [
      "00b767e0",
      "PARAM",
      [
        "storage",
        "002be813",
        null,
        "string"
      ]
    ],
    [
      "00b767fc",
      "PARAM",
      [
        "storage",
        "002a0bac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7638c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76214.md#insn-00b7638c) · [`00b763bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76214.md#insn-00b763bc) · [`00b763d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76214.md#insn-00b763d8)
- 新版 `00b767b4`（命令位置の公開資料なし） · `00b767e4`（命令位置の公開資料なし）

~~~diff
- 00b7638c ["INT_ADD", "register:40f0:8", ["const:b7638c:8", "const:4:8"]]
- 00b7638c ["CALL", null, ["callee:00c5b5c0:8"]]
+ 00b767b4 ["INT_ADD", "register:40f0:8", ["const:b767b4:8", "const:4:8"]]
+ 00b767b4 ["CALL", null, ["callee:00c5b5c0:8"]]
- 00b7638c bytes 8d930394
+ 00b767b4 bytes 83930394
- 00b763bc ["INT_ADD", "register:40f0:8", ["const:b763bc:8", "const:4:8"]]
- 00b763bc ["CALL", null, ["callee:00c580b0:8"]]
+ 00b767e4 ["INT_ADD", "register:40f0:8", ["const:b767e4:8", "const:4:8"]]
+ 00b767e4 ["CALL", null, ["callee:00c580b0:8"]]
- 00b763bc bytes 3d860394
+ 00b767e4 bytes 33860394
- 00b763d8 ["INT_ADD", "register:40f0:8", ["const:b763d8:8", "const:4:8"]]
- 00b763d8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b763d8 bytes 36860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b190d08109cfdfab6176bfd5dbdb0f8"></a>

### [`00b76614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md) → [`00b76a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76a3c.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5f0.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5bdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdb0.md) [`00c5bdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdc0.md)
- 新版 呼出元 1件 [`00c5c9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9f0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5c1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1b0.md) [`00c5c1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.88% / 新版 90.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md#insn-00b76664) · [`00b7666c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md#insn-00b7666c) · [`00b76670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md#insn-00b76670)
- 新版 `00b76a8c`（命令位置の公開資料なし） · `00b76a94`（命令位置の公開資料なし） · `00b76a98`（命令位置の公開資料なし）

~~~diff
- 00b76664 ["INT_ADD", "register:40f0:8", ["const:b76664:8", "const:4:8"]]
- 00b76664 ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b76a8c ["INT_ADD", "register:40f0:8", ["const:b76a8c:8", "const:4:8"]]
+ 00b76a8c ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b76664 bytes d7950394
+ 00b76a8c bytes cd950394
- 00b7666c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b7666c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b7666c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b7666c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b76a94 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b76a94 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b76a94 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b76a94 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b7666c bytes 00040036
+ 00b76a94 bytes 00040036
- 00b76670 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b76670 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b76a98 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b76a98 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b76670 bytes 480400b4
+ 00b76a98 bytes 480400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c540189161c3fca337192b66a4becc34"></a>

### [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) → [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) FUN_00b76d2c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b97fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97fb8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 6件 [`00b72f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72f5c.md) [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b983e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b983e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b76ebc",
      "incomplete_value": false,
      "site": "00b76ed0",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76a94",
      "incomplete_value": false,
      "site": "00b76aa8",
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
            "const:d7c:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b76ee0",
      "incomplete_value": false,
      "site": "00b76f00",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76ab8",
      "incomplete_value": false,
      "site": "00b76ad8",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b76f24",
      "incomplete_value": false,
      "site": "00b76f2c",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76afc",
      "incomplete_value": false,
      "site": "00b76b04",
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
            "const:ae9:8"
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
      "00b76d6c",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b76db0",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b76dc4",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b76d6c",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b76db0",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b76dc4",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md#insn-00b76aa8) · [`00b76ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md#insn-00b76ad8) · [`00b76b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md#insn-00b76b04)
- 新版 `00b76ed0`（命令位置の公開資料なし） · `00b76f00`（命令位置の公開資料なし） · `00b76f2c`（命令位置の公開資料なし）

~~~diff
- 00b76aa8 ["INT_ADD", "register:40f0:8", ["const:b76aa8:8", "const:4:8"]]
- 00b76aa8 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b76ed0 ["INT_ADD", "register:40f0:8", ["const:b76ed0:8", "const:4:8"]]
+ 00b76ed0 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b76aa8 bytes 4a880394
+ 00b76ed0 bytes 40880394
- 00b76ad8 ["INT_ADD", "register:40f0:8", ["const:b76ad8:8", "const:4:8"]]
- 00b76ad8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b76f00 ["INT_ADD", "register:40f0:8", ["const:b76f00:8", "const:4:8"]]
+ 00b76f00 ["CALL", null, ["callee:00c57f80:8"]]
- 00b76ad8 bytes 2a840394
+ 00b76f00 bytes 20840394
- 00b76b04 ["INT_ADD", "register:40f0:8", ["const:b76b04:8", "const:4:8"]]
- 00b76b04 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b76f2c ["INT_ADD", "register:40f0:8", ["const:b76f2c:8", "const:4:8"]]
+ 00b76f2c ["CALL", null, ["callee:00c580b0:8"]]
- 00b76b04 bytes 6b840394
+ 00b76f2c bytes 61840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d6d9c88f323e87d8fbcd5e4910efff5"></a>

### [`00b76f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76f54.md) → [`00b7737c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7737c.md) _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbf0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bff0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.42% / 新版 82.42%

CFGの説明率　旧版 60.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ffc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76f88",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b76f8c",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b76fc4",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b773b0",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b773b4",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b773ec",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76f54.md#insn-00b76fc4) · [`00b76fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76f54.md#insn-00b76fc8) · [`00b76ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76f54.md#insn-00b76ffc)

~~~diff
- 00b76fc4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b76fc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b76fc4 bytes e84b00f9
- 00b76fc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b76fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b76fc8 bytes fb1300f9
- 00b76ffc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:120:8"]]
- 00b76ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b76ffc bytes e82301b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9e6f459abd0e9c746e8c03b3ddf16c0"></a>

### [`00b77104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md) → [`00b7752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7752c.md) _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b77104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md) [`00c5c130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c130.md) · 呼出先 29件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00b77104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00b7752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7752c.md) [`00c5c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c530.md) · 呼出先 29件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00b7752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7752c.md) [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 82.56% / 新版 81.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7749c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b774a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b77584",
      "DATA",
      [
        "storage",
        "0030e067",
        "switchD_00b7716c::switchdataD_0030e067",
        "byte"
      ]
    ],
    [
      "unmatched:00b77420",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77ab4"
      ]
    ],
    [
      "unmatched:00b7742c",
      "PARAM",
      [
        "storage",
        "002aa800",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77584",
      "DATA",
      [
        "storage",
        "0030e0a7",
        "switchD_00b77594::switchdataD_0030e0a7",
        "byte"
      ]
    ],
    [
      "00b77848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77ab4"
      ]
    ],
    [
      "00b77854",
      "PARAM",
      [
        "storage",
        "002aa8cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md#insn-00b77230) · [`00b77248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md#insn-00b77248) · [`00b77280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md#insn-00b77280)
- 新版 `00b77658`（命令位置の公開資料なし） · `00b77670`（命令位置の公開資料なし） · `00b776a8`（命令位置の公開資料なし）

~~~diff
- 00b77230 ["INT_ADD", "register:40f0:8", ["const:b77230:8", "const:4:8"]]
- 00b77230 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b77658 ["INT_ADD", "register:40f0:8", ["const:b77658:8", "const:4:8"]]
+ 00b77658 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b77230 bytes 20820394
+ 00b77658 bytes 16820394
- 00b77248 ["INT_ADD", "register:40f0:8", ["const:b77248:8", "const:4:8"]]
- 00b77248 ["CALL", null, ["callee:00c5c7b0:8"]]
+ 00b77670 ["INT_ADD", "register:40f0:8", ["const:b77670:8", "const:4:8"]]
+ 00b77670 ["CALL", null, ["callee:00c5c7b0:8"]]
- 00b77248 bytes 5a940394
+ 00b77670 bytes 50940394
- 00b77280 ["INT_ADD", "register:40f0:8", ["const:b77280:8", "const:4:8"]]
- 00b77280 ["CALL", null, ["callee:00c5c480:8"]]
+ 00b776a8 ["INT_ADD", "register:40f0:8", ["const:b776a8:8", "const:4:8"]]
+ 00b776a8 ["CALL", null, ["callee:00c5c480:8"]]
- 00b77280 bytes 80930394
+ 00b776a8 bytes 76930394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f9b580e9b1b9caa017aa1b312d18ac"></a>

### [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) → [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) FUN_00b780bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b77104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b982f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b982f8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 5件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b7752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7752c.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b98720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98720.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.48% / 新版 86.48%

CFGの説明率　旧版 54.35% / 新版 59.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77e78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77e80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b780fc",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b78140",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b78154",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b780fc",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b78140",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b78154",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md#insn-00b77db4) · [`00b77dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md#insn-00b77dbc) · [`00b77e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md#insn-00b77e1c)
- 新版 `00b781dc`（命令位置の公開資料なし）

~~~diff
- 00b77db4 ["INT_ADD", "register:40f0:8", ["const:b77db4:8", "const:4:8"]]
- 00b77db4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b781dc ["INT_ADD", "register:40f0:8", ["const:b781dc:8", "const:4:8"]]
+ 00b781dc ["CALL", null, ["callee:00c57fe0:8"]]
- 00b77db4 bytes 8b7f0394
+ 00b781dc bytes 817f0394
- 00b77dbc ["CBRANCH", null, ["local:b61:8", "register:102:1"]]
- 00b77dbc bytes c2190054
- 00b77e1c ["INT_ADD", "register:40f0:8", ["const:b77e1c:8", "const:4:8"]]
- 00b77e1c ["CALL", null, ["callee:00c58000:8"]]
- 00b77e1c bytes 797f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4006f91f99bc4f6cc4c8ca9ef74380c0"></a>

### [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) → [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) FUN_00b78960

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b77104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77104.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b97ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97ad8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 5件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b7752c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b77/00b7752c.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b97f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b97/00b97f00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b78af0",
      "incomplete_value": false,
      "site": "00b78b04",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b786c8",
      "incomplete_value": false,
      "site": "00b786dc",
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
            "const:d7c:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b78b14",
      "incomplete_value": false,
      "site": "00b78b34",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b786ec",
      "incomplete_value": false,
      "site": "00b7870c",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b78b58",
      "incomplete_value": false,
      "site": "00b78b60",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78730",
      "incomplete_value": false,
      "site": "00b78738",
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
            "const:ae9:8"
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
      "00b789a0",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b789e4",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b789f8",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b789a0",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b789e4",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b789f8",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b786dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md#insn-00b786dc) · [`00b7870c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md#insn-00b7870c) · [`00b78738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md#insn-00b78738)
- 新版 `00b78b04`（命令位置の公開資料なし） · `00b78b34`（命令位置の公開資料なし） · `00b78b60`（命令位置の公開資料なし）

~~~diff
- 00b786dc ["INT_ADD", "register:40f0:8", ["const:b786dc:8", "const:4:8"]]
- 00b786dc ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b78b04 ["INT_ADD", "register:40f0:8", ["const:b78b04:8", "const:4:8"]]
+ 00b78b04 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b786dc bytes 3d810394
+ 00b78b04 bytes 33810394
- 00b7870c ["INT_ADD", "register:40f0:8", ["const:b7870c:8", "const:4:8"]]
- 00b7870c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b78b34 ["INT_ADD", "register:40f0:8", ["const:b78b34:8", "const:4:8"]]
+ 00b78b34 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7870c bytes 1d7d0394
+ 00b78b34 bytes 137d0394
- 00b78738 ["INT_ADD", "register:40f0:8", ["const:b78738:8", "const:4:8"]]
- 00b78738 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b78b60 ["INT_ADD", "register:40f0:8", ["const:b78b60:8", "const:4:8"]]
+ 00b78b60 ["CALL", null, ["callee:00c580b0:8"]]
- 00b78738 bytes 5e7d0394
+ 00b78b60 bytes 547d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1620fec069a09331c336518462ebebd3"></a>

### [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) → [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) _ZN11flatbuffers6Parser10ParseTableERKNS_9StructDefEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEPj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c080.md) · 呼出先 41件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)
- 新版 呼出元 1件 [`00c5c480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c480.md) · 呼出先 41件 [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.31% / 新版 56.31%

CFGの説明率　旧版 35.65% / 新版 35.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 2件, `store_value` 3件, `unresolved_branch_alignment` 182件, `unresolved_call_alignment` 25件, `unresolved_store_alignment` 83件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b791b4",
      "incomplete_value": true,
      "site": "00b791c8",
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
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:749:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78d8c",
      "incomplete_value": true,
      "site": "00b78da0",
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
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:709:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b791b4",
      "incomplete_value": true,
      "site": "00b791c8",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78d8c",
      "incomplete_value": true,
      "site": "00b78da0",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b78a6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b78ec0"
      ]
    ],
    [
      "00b78eec",
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b78e94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b78ec0"
      ]
    ],
    [
      "00b78eec",
      "READ",
      [
        "storage",
        "002c27d0",
        null,
        null
      ]
    ],
    [
      "00b78f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md#insn-00b78ae4) · [`00b78c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md#insn-00b78c64) · [`00b78c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md#insn-00b78c74)
- 新版 `00b7908c`（命令位置の公開資料なし） · `00b7909c`（命令位置の公開資料なし）

~~~diff
- 00b78ae4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b78ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b78ae4 bytes e017803d
- 00b78c64 ["INT_ADD", "register:40f0:8", ["const:b78c64:8", "const:4:8"]]
- 00b78c64 ["CALL", null, ["callee:00c5c750:8"]]
+ 00b7908c ["INT_ADD", "register:40f0:8", ["const:b7908c:8", "const:4:8"]]
+ 00b7908c ["CALL", null, ["callee:00c5c750:8"]]
- 00b78c64 bytes bb8d0394
+ 00b7908c bytes b18d0394
- 00b78c74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b78c74 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
+ 00b7909c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b7909c ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00b78c74 bytes 68010035
+ 00b7909c bytes 68010035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e89c31f0ee7e85cd5012a9fbd2cfb2d"></a>

### [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) → [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) _ZN11flatbuffers6Parser11ParseVectorERKNS_4TypeEPjPNS_8FieldDefEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c0e0.md) · 呼出先 31件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)
- 新版 呼出元 1件 [`00c5c4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4e0.md) · 呼出先 31件 [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.52% / 新版 70.52%

CFGの説明率　旧版 52.79% / 新版 53.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 35件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7b62c",
      "incomplete_value": true,
      "site": "00b7b62c",
      "value": [
        "LOAD",
        "8",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:9b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b204",
      "incomplete_value": true,
      "site": "00b7b204",
      "value": [
        "LOAD",
        "8",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:979:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b56c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7b338",
      "DATA",
      [
        "storage",
        "0030e09a",
        "switchD_00b7af1c::switchdataD_0030e09a",
        "byte"
      ]
    ],
    [
      "00b7b424",
      "DATA",
      [
        "storage",
        "0030e0ad",
        "switchD_00b7b008::switchdataD_0030e0ad",
        "byte"
      ]
    ],
    [
      "00b7b484",
      "DATA",
      [
        "storage",
        "0030e0c0",
        "switchD_00b7b074::switchdataD_0030e0c0",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b7b338",
      "DATA",
      [
        "storage",
        "0030e0da",
        "switchD_00b7b344::switchdataD_0030e0da",
        "byte"
      ]
    ],
    [
      "00b7b424",
      "DATA",
      [
        "storage",
        "0030e0ed",
        "switchD_00b7b430::switchdataD_0030e0ed",
        "byte"
      ]
    ],
    [
      "00b7b484",
      "DATA",
      [
        "storage",
        "0030e100",
        "switchD_00b7b49c::switchdataD_0030e100",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md#insn-00b7b228) · [`00b7b554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md#insn-00b7b554) · [`00b7b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md#insn-00b7b56c)
- 新版 `00b7b650`（命令位置の公開資料なし）

~~~diff
- 00b7b228 ["INT_ADD", "register:40f0:8", ["const:b7b228:8", "const:4:8"]]
- 00b7b228 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b7b650 ["INT_ADD", "register:40f0:8", ["const:b7b650:8", "const:4:8"]]
+ 00b7b650 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b7b228 bytes 22720394
+ 00b7b650 bytes 18720394
- 00b7b554 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b7b554 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b7b554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b7b554 bytes 68020079
- 00b7b56c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b7b56c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b7b56c bytes 880300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57ffce7ab5302cdcef67f45828126fc"></a>

### [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) → [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) _ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c060.md) · 呼出先 31件 [`00b76904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76904.md) [`00b77c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b77/00b77c94.md) [`00b78538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b78538.md) [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md)
- 新版 呼出元 1件 [`00c5c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c460.md) · 呼出先 31件 [`00b76d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76d2c.md) [`00b780bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b780bc.md) [`00b78960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78960.md) [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.12% / 新版 58.12%

CFGの説明率　旧版 34.16% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 35件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 70件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7bbd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7bbd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7bbdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7bbd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7bbdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7bbe0",
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
      "00b7c000",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7c004",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b7c008",
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

- 旧版 [`00b7bbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md#insn-00b7bbd8) · [`00b7bbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md#insn-00b7bbdc) · [`00b7bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md#insn-00b7bbe0)

~~~diff
- 00b7bbd8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b7bbd8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b7bbd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b7bbd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7bbd8 bytes fc6f13a9
- 00b7bbdc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b7bbdc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b7bbdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b7bbdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7bbdc bytes fa6714a9
- 00b7bbe0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b7bbe0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b7bbe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b7bbe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7bbe0 bytes f85f15a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1296bfb6ec88bc2968633d88552bd967"></a>

### [`00b7c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7c620.md) → [`00b7ca48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ca48.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3b0.md) · 呼出先 11件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md) [`00c5bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbf0.md)
- 新版 呼出元 1件 [`00c5c7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7b0.md) · 呼出先 11件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md) [`00c5bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bff0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 42.61% / 新版 42.61%

CFGの説明率　旧版 10.22% / 新版 9.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c658"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7c650",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7c658",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7c65c",
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
      "00b7ca78",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b7ca80",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b7ca84",
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

- 旧版 [`00b7c650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7c620.md#insn-00b7c650) · [`00b7c658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7c620.md#insn-00b7c658) · [`00b7c65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7c620.md#insn-00b7c65c)

~~~diff
- 00b7c650 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b7c650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b7c650 bytes e80f00f9
- 00b7c658 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b7c658 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b7c658 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b7c658 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b7c658 bytes ff7f00a9
- 00b7c65c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b7c65c ["COPY", "tmp:1:8", ["register:8:8"]]
- 00b7c65c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b7c65c bytes e8030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802e7aa88875164d9818d45b7aff7899"></a>

### [`00b7caac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7caac.md) → [`00b7ced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md) _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1c0.md) · 呼出先 2件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5c0.md) · 呼出先 2件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 55.88% / 新版 63.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cb2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7cf54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cb30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7cb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7cf74"
      ]
    ]
  ],
  "added": [
    [
      "00b7cf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7cf74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7caac.md#insn-00b7cb2c) · [`00b7cb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7caac.md#insn-00b7cb30) · [`00b7cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7caac.md#insn-00b7cb90)
- 新版 `00b7cfb8`（命令位置の公開資料なし）

~~~diff
- 00b7cb2c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7cb2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7cb2c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b7cb2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b7cb2c bytes 3f010039
- 00b7cb30 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b7cb30 bytes e0000054
- 00b7cb90 ["INT_ADD", "register:40f0:8", ["const:b7cb90:8", "const:4:8"]]
- 00b7cb90 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7cfb8 ["INT_ADD", "register:40f0:8", ["const:b7cfb8:8", "const:4:8"]]
+ 00b7cfb8 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7cb90 bytes 847c0394
+ 00b7cfb8 bytes 7a7c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b76f71e532a607572a3aaaa5bb26e78"></a>

### [`00b7cc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cc24.md) → [`00b7d04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d04c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIhEEvtT_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bde0.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1e0.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 36.84% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7d110"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cc58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7cc58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7d08c"
      ]
    ],
    [
      "unmatched:00b7ccb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7d0ec"
      ]
    ]
  ],
  "added": [
    [
      "00b7d080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7d08c"
      ]
    ],
    [
      "00b7d0d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7d0ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cc24.md#insn-00b7cc58) · [`00b7ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cc24.md#insn-00b7ccb0) · [`00b7ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cc24.md#insn-00b7ccbc)
- 新版 `00b7d0e4`（命令位置の公開資料なし）

~~~diff
- 00b7cc58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b7cc58 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b7cc58 bytes 680000b5
- 00b7ccb0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7ccb0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b7ccb0 bytes a1000054
- 00b7ccbc ["INT_ADD", "register:40f0:8", ["const:b7ccbc:8", "const:4:8"]]
- 00b7ccbc ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7d0e4 ["INT_ADD", "register:40f0:8", ["const:b7d0e4:8", "const:4:8"]]
+ 00b7d0e4 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7ccbc bytes 397c0394
+ 00b7d0e4 bytes 2f7c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb91bc9d042865b30ced3e064ccd5a8e"></a>

### [`00b7cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md) → [`00b7d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d130.md) FUN_00b7d130

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b97c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97c78.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b980a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b980a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.51% / 新版 83.51%

CFGの説明率　旧版 56.25% / 新版 56.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d170",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d1b4",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7d1c8",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7d170",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d1b4",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7d1c8",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md#insn-00b7ce94) · [`00b7ceb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md#insn-00b7ceb0) · [`00b7cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7c/00b7cd08.md#insn-00b7cec4)

~~~diff
- 00b7ce94 ["INT_ADD", "register:40f0:8", ["const:b7ce94:8", "const:4:8"]]
- 00b7ce94 ["CALL", null, ["callee:00c58000:8"]]
- 00b7ce94 bytes 5b6b0394
- 00b7ceb0 ["INT_ADD", "register:40f0:8", ["const:b7ceb0:8", "const:4:8"]]
- 00b7ceb0 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7ceb0 bytes 486f0394
- 00b7cec4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00b7cec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b7cec4 bytes e01f803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51a7f5f621c9941a75c1dbe6f5974870"></a>

### [`00b7d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d17c.md) → [`00b7d5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d5a4.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIaEEvtT_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdd0.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1d0.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.50% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d17c.md#insn-00b7d1a8) · [`00b7d1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d17c.md#insn-00b7d1c8) · [`00b7d1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d17c.md#insn-00b7d1d4)
- 新版 `00b7d5d0`（命令位置の公開資料なし） · `00b7d5f0`（命令位置の公開資料なし） · `00b7d5fc`（命令位置の公開資料なし）

~~~diff
- 00b7d1a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b7d1a8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b7d5d0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b7d5d0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b7d1a8 bytes 48050034
+ 00b7d5d0 bytes 48050034
- 00b7d1c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7d1c8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b7d5f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7d5f0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b7d1c8 bytes a1000054
+ 00b7d5f0 bytes a1000054
- 00b7d1d4 ["INT_ADD", "register:40f0:8", ["const:b7d1d4:8", "const:4:8"]]
- 00b7d1d4 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7d5fc ["INT_ADD", "register:40f0:8", ["const:b7d5fc:8", "const:4:8"]]
+ 00b7d5fc ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7d1d4 bytes f37a0394
+ 00b7d5fc bytes e97a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb7474642f4fbb2b2e8c64828e0eec86"></a>

### [`00b7d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md) → [`00b7d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d688.md) FUN_00b7d688

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b97e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b97e18.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b98240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98240.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 44.57% / 新版 36.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d44c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7d294",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d2a0",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d70c",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7d6bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b7d6c8",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d70c",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md#insn-00b7d294) · [`00b7d448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md#insn-00b7d448) · [`00b7d44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d260.md#insn-00b7d44c)

~~~diff
- 00b7d294 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7d294 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b7d294 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b7d294 bytes a8831bf8
- 00b7d448 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffff80:8"]]
- 00b7d448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b7d448 bytes a003983c
- 00b7d44c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7d44c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff90:8"]]
- 00b7d44c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b7d44c bytes a80319f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88098c8efd9f6f48dfddaccb92dc785c"></a>

### [`00b7d7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d7e8.md) → [`00b7dc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dc10.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be00.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c200.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 17.86% / 新版 27.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d8c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7dce8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d80c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7d80c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7d818"
      ]
    ],
    [
      "unmatched:00b7d834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7dc74"
      ]
    ]
  ],
  "added": [
    [
      "00b7dc34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7dc40"
      ]
    ],
    [
      "00b7dc5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7dc74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d7e8.md#insn-00b7d80c) · [`00b7d834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d7e8.md#insn-00b7d834) · [`00b7d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d7e8.md#insn-00b7d840)
- 新版 `00b7dc68`（命令位置の公開資料なし）

~~~diff
- 00b7d80c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7d80c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b7d80c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b7d80c bytes 68000054
- 00b7d834 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b7d834 bytes c2000054
- 00b7d840 ["INT_ADD", "register:40f0:8", ["const:b7d840:8", "const:4:8"]]
- 00b7d840 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b7dc68 ["INT_ADD", "register:40f0:8", ["const:b7dc68:8", "const:4:8"]]
+ 00b7dc68 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b7d840 bytes 58790394
+ 00b7dc68 bytes 4e790394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8abd0647f339fdff4b0bc40a2b7e9e89"></a>

### [`00b7da24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7da24.md) → [`00b7de4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7de4c.md) FUN_00b7de4c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b98158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98158.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b98580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98580.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 54.44% / 新版 53.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dc0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dc10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dc14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7de8c",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ded0",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7dee4",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7de8c",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ded0",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7dee4",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7da24.md#insn-00b7dbb0) · [`00b7dbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7da24.md#insn-00b7dbcc) · [`00b7dbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7da24.md#insn-00b7dbfc)
- 新版 `00b7e024`（命令位置の公開資料なし）

~~~diff
- 00b7dbb0 ["INT_ADD", "register:40f0:8", ["const:b7dbb0:8", "const:4:8"]]
- 00b7dbb0 ["CALL", null, ["callee:00c58000:8"]]
- 00b7dbb0 bytes 14680394
- 00b7dbcc ["INT_ADD", "register:40f0:8", ["const:b7dbcc:8", "const:4:8"]]
- 00b7dbcc ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7dbcc bytes 016c0394
- 00b7dbfc ["INT_ADD", "register:40f0:8", ["const:b7dbfc:8", "const:4:8"]]
- 00b7dbfc ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7e024 ["INT_ADD", "register:40f0:8", ["const:b7e024:8", "const:4:8"]]
+ 00b7e024 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7dbfc bytes e1670394
+ 00b7e024 bytes d7670394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-042cd85f19d1abe66d628ac5c49b2afc"></a>

### [`00b7e068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e068.md) → [`00b7e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e490.md) FUN_00b7e490

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b98498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98498.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b988c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b988c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.81% / 新版 75.81%

CFGの説明率　旧版 46.58% / 新版 47.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e23c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7e528",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e170"
      ]
    ],
    [
      "00b7e564",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e338"
      ]
    ],
    [
      "unmatched:00b7e16c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58000"
      ]
    ]
  ],
  "added": [
    [
      "00b7e528",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e598"
      ]
    ],
    [
      "00b7e564",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e760"
      ]
    ],
    [
      "00b7e594",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e068.md#insn-00b7e16c) · [`00b7e188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e068.md#insn-00b7e188) · [`00b7e1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e068.md#insn-00b7e1b8)
- 新版 `00b7e5e0`（命令位置の公開資料なし）

~~~diff
- 00b7e16c ["INT_ADD", "register:40f0:8", ["const:b7e16c:8", "const:4:8"]]
- 00b7e16c ["CALL", null, ["callee:00c58000:8"]]
- 00b7e16c bytes a5660394
- 00b7e188 ["INT_ADD", "register:40f0:8", ["const:b7e188:8", "const:4:8"]]
- 00b7e188 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7e188 bytes 926a0394
- 00b7e1b8 ["INT_ADD", "register:40f0:8", ["const:b7e1b8:8", "const:4:8"]]
- 00b7e1b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7e5e0 ["INT_ADD", "register:40f0:8", ["const:b7e5e0:8", "const:4:8"]]
+ 00b7e5e0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7e1b8 bytes 72660394
+ 00b7e5e0 bytes 68660394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b94649c27a4e28b0abd8e3b2f60acfb"></a>

### [`00b7e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md) → [`00b7e954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e954.md) FUN_00b7e954

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 12件 [`00b98638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98638.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 12件 [`00b98a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b98/00b98a60.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 68.29% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ea74",
      "incomplete_value": false,
      "site": "00b7ea88",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e64c",
      "incomplete_value": false,
      "site": "00b7e660",
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
            "const:d7c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ea98",
      "incomplete_value": false,
      "site": "00b7eab8",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e670",
      "incomplete_value": false,
      "site": "00b7e690",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7eac8",
      "incomplete_value": false,
      "site": "00b7eae4",
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
            "const:bbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e6a0",
      "incomplete_value": false,
      "site": "00b7e6bc",
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
            "const:aee:8"
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
      "00b7ea74",
      "PARAM",
      [
        "storage",
        "002b6d7c",
        null,
        "string"
      ]
    ],
    [
      "00b7ea98",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "00b7eac8",
      "PARAM",
      [
        "storage",
        "002a1aee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7ea74",
      "PARAM",
      [
        "storage",
        "002b6dbc",
        null,
        "string"
      ]
    ],
    [
      "00b7ea98",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00b7eac8",
      "PARAM",
      [
        "storage",
        "002a1bbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md#insn-00b7e660) · [`00b7e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md#insn-00b7e690) · [`00b7e6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md#insn-00b7e6bc)
- 新版 `00b7ea88`（命令位置の公開資料なし） · `00b7eab8`（命令位置の公開資料なし） · `00b7eae4`（命令位置の公開資料なし）

~~~diff
- 00b7e660 ["INT_ADD", "register:40f0:8", ["const:b7e660:8", "const:4:8"]]
- 00b7e660 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b7ea88 ["INT_ADD", "register:40f0:8", ["const:b7ea88:8", "const:4:8"]]
+ 00b7ea88 ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7e660 bytes 5c690394
+ 00b7ea88 bytes 52690394
- 00b7e690 ["INT_ADD", "register:40f0:8", ["const:b7e690:8", "const:4:8"]]
- 00b7e690 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7eab8 ["INT_ADD", "register:40f0:8", ["const:b7eab8:8", "const:4:8"]]
+ 00b7eab8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7e690 bytes 3c650394
+ 00b7eab8 bytes 32650394
- 00b7e6bc ["INT_ADD", "register:40f0:8", ["const:b7e6bc:8", "const:4:8"]]
- 00b7e6bc ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7eae4 ["INT_ADD", "register:40f0:8", ["const:b7eae4:8", "const:4:8"]]
+ 00b7eae4 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7e6bc bytes 31650394
+ 00b7eae4 bytes 27650394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-454e358077af74dbb828446b5ca7ead0"></a>

### [`00b7ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ea40.md) → [`00b7ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7ee68.md) FUN_00b7ee68

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 4件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.64% / 新版 97.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ef38",
      "incomplete_value": false,
      "site": "00b7ef4c",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb10",
      "incomplete_value": false,
      "site": "00b7eb24",
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
            "const:d7c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ef5c",
      "incomplete_value": false,
      "site": "00b7ef7c",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb34",
      "incomplete_value": false,
      "site": "00b7eb54",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7efa0",
      "incomplete_value": false,
      "site": "00b7efa8",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb78",
      "incomplete_value": false,
      "site": "00b7eb80",
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
            "const:ae9:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7ef38",
      "PARAM",
      [
        "storage",
        "002b6d7c",
        null,
        "string"
      ]
    ],
    [
      "00b7ef5c",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "00b7efa0",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7ef38",
      "PARAM",
      [
        "storage",
        "002b6dbc",
        null,
        "string"
      ]
    ],
    [
      "00b7ef5c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00b7efa0",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7eb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ea40.md#insn-00b7eb24) · [`00b7eb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ea40.md#insn-00b7eb54) · [`00b7eb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ea40.md#insn-00b7eb80)
- 新版 `00b7ef4c`（命令位置の公開資料なし） · `00b7ef7c`（命令位置の公開資料なし） · `00b7efa8`（命令位置の公開資料なし）

~~~diff
- 00b7eb24 ["INT_ADD", "register:40f0:8", ["const:b7eb24:8", "const:4:8"]]
- 00b7eb24 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b7ef4c ["INT_ADD", "register:40f0:8", ["const:b7ef4c:8", "const:4:8"]]
+ 00b7ef4c ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7eb24 bytes 2b680394
+ 00b7ef4c bytes 21680394
- 00b7eb54 ["INT_ADD", "register:40f0:8", ["const:b7eb54:8", "const:4:8"]]
- 00b7eb54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7ef7c ["INT_ADD", "register:40f0:8", ["const:b7ef7c:8", "const:4:8"]]
+ 00b7ef7c ["CALL", null, ["callee:00c57f80:8"]]
- 00b7eb54 bytes 0b640394
+ 00b7ef7c bytes 01640394
- 00b7eb80 ["INT_ADD", "register:40f0:8", ["const:b7eb80:8", "const:4:8"]]
- 00b7eb80 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b7efa8 ["INT_ADD", "register:40f0:8", ["const:b7efa8:8", "const:4:8"]]
+ 00b7efa8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b7eb80 bytes 4c640394
+ 00b7efa8 bytes 42640394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ecc1d958fe2e65e624d9125996331d"></a>

### [`00b7ed20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md) → [`00b7f148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f148.md) FUN_00b7f148

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00b75018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75018.md) [`00b789dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b78/00b789dc.md) [`00b7ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7a/00b7ae50.md) [`00b7bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7b/00b7bbd4.md) [`00b81344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 5件 [`00b75440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b75/00b75440.md) [`00b78e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b78/00b78e04.md) [`00b7b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7b278.md) [`00b7bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7b/00b7bffc.md) [`00b8176c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8176c.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f218",
      "incomplete_value": false,
      "site": "00b7f22c",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7edf0",
      "incomplete_value": false,
      "site": "00b7ee04",
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
            "const:d7c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f23c",
      "incomplete_value": false,
      "site": "00b7f25c",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ee14",
      "incomplete_value": false,
      "site": "00b7ee34",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f280",
      "incomplete_value": false,
      "site": "00b7f288",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ee58",
      "incomplete_value": false,
      "site": "00b7ee60",
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
            "const:ae9:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7f218",
      "PARAM",
      [
        "storage",
        "002b6d7c",
        null,
        "string"
      ]
    ],
    [
      "00b7f23c",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "00b7f280",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7f218",
      "PARAM",
      [
        "storage",
        "002b6dbc",
        null,
        "string"
      ]
    ],
    [
      "00b7f23c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00b7f280",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ee04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md#insn-00b7ee04) · [`00b7ee34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md#insn-00b7ee34) · [`00b7ee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md#insn-00b7ee60)
- 新版 `00b7f22c`（命令位置の公開資料なし） · `00b7f25c`（命令位置の公開資料なし） · `00b7f288`（命令位置の公開資料なし）

~~~diff
- 00b7ee04 ["INT_ADD", "register:40f0:8", ["const:b7ee04:8", "const:4:8"]]
- 00b7ee04 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00b7f22c ["INT_ADD", "register:40f0:8", ["const:b7f22c:8", "const:4:8"]]
+ 00b7f22c ["CALL", null, ["callee:00c58fd0:8"]]
- 00b7ee04 bytes 73670394
+ 00b7f22c bytes 69670394
- 00b7ee34 ["INT_ADD", "register:40f0:8", ["const:b7ee34:8", "const:4:8"]]
- 00b7ee34 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7f25c ["INT_ADD", "register:40f0:8", ["const:b7f25c:8", "const:4:8"]]
+ 00b7f25c ["CALL", null, ["callee:00c57f80:8"]]
- 00b7ee34 bytes 53630394
+ 00b7f25c bytes 49630394
- 00b7ee60 ["INT_ADD", "register:40f0:8", ["const:b7ee60:8", "const:4:8"]]
- 00b7ee60 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b7f288 ["INT_ADD", "register:40f0:8", ["const:b7f288:8", "const:4:8"]]
+ 00b7f288 ["CALL", null, ["callee:00c580b0:8"]]
- 00b7ee60 bytes 94630394
+ 00b7f288 bytes 8a630394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0493f362c7ccbcc15f7e50f82eca5a92"></a>

### [`00b7f43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f43c.md) → [`00b7f864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f864.md) _ZN11flatbuffers6Parser19ParseAlignAttributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEmPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c280.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 1件 [`00c5c680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c680.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f984",
      "incomplete_value": false,
      "site": "00b7f994",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f55c",
      "incomplete_value": false,
      "site": "00b7f56c",
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
            "const:a62:8"
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
      "definition_site": "00b7f99c",
      "incomplete_value": false,
      "site": "00b7f9a8",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f574",
      "incomplete_value": false,
      "site": "00b7f580",
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
            "const:f80:8"
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
      "definition_site": "00b7fa04",
      "incomplete_value": false,
      "site": "00b7fa20",
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
            "const:b79:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f5dc",
      "incomplete_value": false,
      "site": "00b7f5f8",
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
            "const:b39:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7f8f8",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f910",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f920",
      "READ",
      [
        "storage",
        "01125de0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f8f8",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f910",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f920",
      "READ",
      [
        "storage",
        "011261e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f43c.md#insn-00b7f56c) · [`00b7f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f43c.md#insn-00b7f580) · [`00b7f5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f43c.md#insn-00b7f5f8)
- 新版 `00b7f994`（命令位置の公開資料なし） · `00b7f9a8`（命令位置の公開資料なし） · `00b7fa20`（命令位置の公開資料なし）

~~~diff
- 00b7f56c ["INT_ADD", "register:40f0:8", ["const:b7f56c:8", "const:4:8"]]
- 00b7f56c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b7f994 ["INT_ADD", "register:40f0:8", ["const:b7f994:8", "const:4:8"]]
+ 00b7f994 ["CALL", null, ["callee:00c580b0:8"]]
- 00b7f56c bytes d1610394
+ 00b7f994 bytes c7610394
- 00b7f580 ["INT_ADD", "register:40f0:8", ["const:b7f580:8", "const:4:8"]]
- 00b7f580 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7f9a8 ["INT_ADD", "register:40f0:8", ["const:b7f9a8:8", "const:4:8"]]
+ 00b7f9a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7f580 bytes 80610394
+ 00b7f9a8 bytes 76610394
- 00b7f5f8 ["INT_ADD", "register:40f0:8", ["const:b7f5f8:8", "const:4:8"]]
- 00b7f5f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b7fa20 ["INT_ADD", "register:40f0:8", ["const:b7fa20:8", "const:4:8"]]
+ 00b7fa20 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7f5f8 bytes 62610394
+ 00b7fa20 bytes 58610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2766b6df322ba1e7652180166ef9530f"></a>

### [`00b7f76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f76c.md) → [`00b7fb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7fb94.md) _ZN11flatbuffers11NumToStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc10.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)
- 新版 呼出元 1件 [`00c5c010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c010.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7fbec",
      "incomplete_value": true,
      "site": "00b7fc00",
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
      "definition_site": "00b7f7c4",
      "incomplete_value": true,
      "site": "00b7f7d8",
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
      "definition_site": "00b7fbe4",
      "incomplete_value": true,
      "site": "00b7fc04",
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
      "definition_site": "00b7f7bc",
      "incomplete_value": true,
      "site": "00b7f7dc",
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
      "definition_site": "00b7fc74",
      "incomplete_value": true,
      "site": "00b7fc80",
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
      "definition_site": "00b7f84c",
      "incomplete_value": true,
      "site": "00b7f858",
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
      "00b7fbc4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fbc8",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fc00",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7fbc4",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fbc8",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fc00",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f76c.md#insn-00b7f79c) · [`00b7f7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f76c.md#insn-00b7f7a0) · [`00b7f7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7f76c.md#insn-00b7f7e4)
- 新版 `00b7fbc4`（命令位置の公開資料なし） · `00b7fbc8`（命令位置の公開資料なし） · `00b7fc0c`（命令位置の公開資料なし）

~~~diff
- 00b7f79c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:818:8"]]
- 00b7f79c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7fbc4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c18:8"]]
+ 00b7fbc4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f79c bytes 5a0f44f9
+ 00b7fbc4 bytes 5a0f46f9
- 00b7f7a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:440:8"]]
- 00b7f7a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7fbc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
+ 00b7fbc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f7a0 bytes 082142f9
+ 00b7fbc8 bytes 082144f9
- 00b7f7e4 ["INT_ADD", "register:40f0:8", ["const:b7f7e4:8", "const:4:8"]]
- 00b7f7e4 ["CALL", null, ["callee:00c581e0:8"]]
+ 00b7fc0c ["INT_ADD", "register:40f0:8", ["const:b7fc0c:8", "const:4:8"]]
+ 00b7fc0c ["CALL", null, ["callee:00c581e0:8"]]
- 00b7f7e4 bytes 7f610394
+ 00b7fc0c bytes 75610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b75d0953dc9fa1825a5d3ebf867afec"></a>

### [`00b7ff48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7ff48.md) → [`00b80370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80370.md) _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2b0.md) · 呼出先 20件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6b0.md) · 呼出先 20件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80464",
      "incomplete_value": true,
      "site": "00b80474",
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
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8003c",
      "incomplete_value": true,
      "site": "00b8004c",
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
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80470",
      "incomplete_value": true,
      "site": "00b80480",
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
                "leaf",
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:b5b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80048",
      "incomplete_value": true,
      "site": "00b80058",
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
                "leaf",
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:a8e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80470",
      "incomplete_value": true,
      "site": "00b80480",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80048",
      "incomplete_value": true,
      "site": "00b80058",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80464",
      "READ",
      [
        "storage",
        "002c3190",
        null,
        null
      ]
    ],
    [
      "00b80470",
      "READ",
      [
        "storage",
        "002a1a8e",
        null,
        "string"
      ]
    ],
    [
      "00b80470",
      "READ",
      [
        "storage",
        "002a1a9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b80464",
      "READ",
      [
        "storage",
        "002c31d0",
        null,
        null
      ]
    ],
    [
      "00b80470",
      "READ",
      [
        "storage",
        "002a1b5b",
        null,
        "string"
      ]
    ],
    [
      "00b80470",
      "READ",
      [
        "storage",
        "002a1b6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7ff48.md#insn-00b8007c) · [`00b802e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7ff48.md#insn-00b802e0) · [`00b7ffb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7f/00b7ff48.md#insn-00b7ffb0)
- 新版 `00b804a4`（命令位置の公開資料なし） · `00b80708`（命令位置の公開資料なし） · `00b803d8`（命令位置の公開資料なし）

~~~diff
- 00b8007c ["INT_ADD", "register:40f0:8", ["const:b8007c:8", "const:4:8"]]
- 00b8007c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b804a4 ["INT_ADD", "register:40f0:8", ["const:b804a4:8", "const:4:8"]]
+ 00b804a4 ["CALL", null, ["callee:00c580b0:8"]]
- 00b8007c bytes 0d5f0394
+ 00b804a4 bytes 035f0394
- 00b802e0 ["INT_ADD", "register:40f0:8", ["const:b802e0:8", "const:4:8"]]
- 00b802e0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b80708 ["INT_ADD", "register:40f0:8", ["const:b80708:8", "const:4:8"]]
+ 00b80708 ["CALL", null, ["callee:00c580b0:8"]]
- 00b802e0 bytes 745e0394
+ 00b80708 bytes 6a5e0394
- 00b7ffb0 ["INT_ADD", "register:40f0:8", ["const:b7ffb0:8", "const:4:8"]]
- 00b7ffb0 ["CALL", null, ["callee:00c5c530:8"]]
+ 00b803d8 ["INT_ADD", "register:40f0:8", ["const:b803d8:8", "const:4:8"]]
+ 00b803d8 ["CALL", null, ["callee:00c5c530:8"]]
- 00b7ffb0 bytes 60700394
+ 00b803d8 bytes 56700394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-492a49ed79176c133647502fc59420bc"></a>

### [`00b809a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b809a4.md) → [`00b80dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b80/00b80dcc.md) _ZN11flatbuffers6Parser19ParseEnumFromStringERKNS_4TypeEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c290.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c690.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 95.88% / 新版 94.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 5件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80e28",
      "incomplete_value": true,
      "site": "00b80e54",
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
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80a00",
      "incomplete_value": true,
      "site": "00b80a2c",
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
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81030",
      "incomplete_value": true,
      "site": "00b81040",
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
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:61b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80c08",
      "incomplete_value": true,
      "site": "00b80c18",
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
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:5db:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81030",
      "incomplete_value": true,
      "site": "00b81040",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80c08",
      "incomplete_value": true,
      "site": "00b80c18",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80e28",
      "READ",
      [
        "storage",
        "002c31c0",
        null,
        null
      ]
    ],
    [
      "00b80f3c",
      "PARAM",
      [
        "storage",
        "002ae26a",
        null,
        "string"
      ]
    ],
    [
      "00b80f50",
      "PARAM",
      [
        "storage",
        "002a0ae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b80e28",
      "READ",
      [
        "storage",
        "002c3200",
        null,
        null
      ]
    ],
    [
      "00b80f3c",
      "PARAM",
      [
        "storage",
        "002ae2aa",
        null,
        "string"
      ]
    ],
    [
      "00b80f50",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b809a4.md#insn-00b80b18) · [`00b80c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b809a4.md#insn-00b80c90) · [`00b80ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b809a4.md#insn-00b80ca4)
- 新版 `00b80f40`（命令位置の公開資料なし） · `00b810b8`（命令位置の公開資料なし） · `00b810cc`（命令位置の公開資料なし）

~~~diff
- 00b80b18 ["INT_ADD", "register:40f0:8", ["const:b80b18:8", "const:4:8"]]
- 00b80b18 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b80f40 ["INT_ADD", "register:40f0:8", ["const:b80f40:8", "const:4:8"]]
+ 00b80f40 ["CALL", null, ["callee:00c580b0:8"]]
- 00b80b18 bytes 665c0394
+ 00b80f40 bytes 5c5c0394
- 00b80c90 ["INT_ADD", "register:40f0:8", ["const:b80c90:8", "const:4:8"]]
- 00b80c90 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b810b8 ["INT_ADD", "register:40f0:8", ["const:b810b8:8", "const:4:8"]]
+ 00b810b8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b80c90 bytes 085c0394
+ 00b810b8 bytes fe5b0394
- 00b80ca4 ["INT_ADD", "register:40f0:8", ["const:b80ca4:8", "const:4:8"]]
- 00b80ca4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b810cc ["INT_ADD", "register:40f0:8", ["const:b810cc:8", "const:4:8"]]
+ 00b810cc ["CALL", null, ["callee:00c580b0:8"]]
- 00b80ca4 bytes 035c0394
+ 00b810cc bytes f95b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a7d524cef75feb76d8755dc725fce89"></a>

### [`00b80e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80e44.md) → [`00b8126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8126c.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc20.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c020.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 90.11% / 新版 90.11%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81350",
      "incomplete_value": true,
      "site": "00b8135c",
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
      "definition_site": "00b80f28",
      "incomplete_value": true,
      "site": "00b80f34",
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
      "unmatched:00b80e78",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b80e7c",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b80eb4",
      "DATA",
      [
        "storage",
        "00c907d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b812a0",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b812a4",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b812dc",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80e44.md#insn-00b80eb4) · [`00b80eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80e44.md#insn-00b80eb8)
- 新版 `00b812dc`（命令位置の公開資料なし）

~~~diff
- 00b80eb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b80eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b80eb4 bytes e84b00f9
- 00b80eb8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b80eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b80eb8 bytes fb1300f9
+ 00b812dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
+ 00b812dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b812dc bytes e84b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1a8c2ed0bed467c209ec4504fce5e3f"></a>

### [`00b80fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80fb0.md) → [`00b813d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b813d8.md) _ZN11flatbuffers11NumToStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc30.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c030.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 74.73% / 新版 74.73%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8101c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b80fd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b80fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x19c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b80fe4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b813f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ],
    [
      "00b81404",
      "WRITE",
      [
        "storage",
        "Stack[-0x19c]",
        null,
        null
      ]
    ],
    [
      "00b8140c",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80fb0.md#insn-00b80fd0) · [`00b80fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80fb0.md#insn-00b80fdc) · [`00b8101c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b80/00b80fb0.md#insn-00b8101c)

~~~diff
- 00b80fd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b80fd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b80fd0 bytes e80700f9
- 00b80fdc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:4:8"]]
- 00b80fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00b80fdc bytes e00700b9
- 00b8101c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b8101c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b8101c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b8101c bytes a9031af8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b117162e776b258a28d2914b0db4de1b"></a>

### [`00b8111c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b8111c.md) → [`00b81544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b81544.md) _ZN11flatbuffers6Parser10TokenErrorEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c090.md) · 呼出先 10件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5c490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c490.md) · 呼出先 10件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.93% / 新版 94.93%

CFGの説明率　旧版 70.73% / 新版 72.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8159c"
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
      "unmatched:00b81174",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b81178",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b81604",
      "DATA",
      [
        "storage",
        "00c90558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b8159c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b815a0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b81604",
      "DATA",
      [
        "storage",
        "00c90958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b8111c.md#insn-00b81174) · [`00b81178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b8111c.md#insn-00b81178) · [`00b811ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b8111c.md#insn-00b811ec)
- 新版 `00b81614`（命令位置の公開資料なし）

~~~diff
- 00b81174 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b81174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b81174 bytes e90b00f9
- 00b81178 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b81178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b81178 bytes e003803d
- 00b811ec ["INT_ADD", "register:40f0:8", ["const:b811ec:8", "const:4:8"]]
- 00b811ec ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b81614 ["INT_ADD", "register:40f0:8", ["const:b81614:8", "const:4:8"]]
+ 00b81614 ["CALL", null, ["callee:00c57fe0:8"]]
- 00b811ec bytes 7d5a0394
+ 00b81614 bytes 735a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd70f6a4914560ef2f4adab262fd271b"></a>

### [`00b81344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md) → [`00b8176c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8176c.md) _ZN11flatbuffers6Parser13ParseFunctionEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c140.md) · 呼出先 23件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00b7ed20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7ed20.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5c540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c540.md) · 呼出先 23件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00b7f148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7f/00b7f148.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.86% / 新版 81.86%

CFGの説明率　旧版 54.21% / 新版 53.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_value` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8135c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8135c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8137c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8135c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8137c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b814ec",
      "PARAM",
      [
        "storage",
        "002b1608",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b81784",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b817a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b81914",
      "PARAM",
      [
        "storage",
        "002b1648",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8135c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md#insn-00b8135c) · [`00b8137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md#insn-00b8137c) · [`00b81598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md#insn-00b81598)

~~~diff
- 00b8135c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8135c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8135c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00b8135c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8135c bytes fd7b1aa9
- 00b8137c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b8137c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b8137c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b8137c bytes a8031af8
- 00b81598 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00b81598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b81598 bytes e01f803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d9fcfa33e27e20a003b0389c58e92c"></a>

### [`00b81d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81d2c.md) → [`00b82154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82154.md) _ZN11flatbuffers6Parser13TryTypedValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEibRNS_5ValueENS_8BaseTypeEPb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c170.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5c570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c570.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.98% / 新版 81.98%

CFGの説明率　旧版 50.32% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 3件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b821f4",
      "incomplete_value": true,
      "site": "00b8220c",
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
                "leaf",
                "const:2c2000:8"
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
      "definition_site": "00b81dcc",
      "incomplete_value": true,
      "site": "00b81de4",
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
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
            ]
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
      "definition_site": "00b821f8",
      "incomplete_value": true,
      "site": "00b82210",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81dd0",
      "incomplete_value": true,
      "site": "00b81de8",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b821f4",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "00b821f8",
      "READ",
      [
        "storage",
        "002b46d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b821a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b821f4",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "00b821f8",
      "READ",
      [
        "storage",
        "002b4713",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81d2c.md#insn-00b81d80) · [`00b81ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81d2c.md#insn-00b81ec8) · [`00b81edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81d2c.md#insn-00b81edc)
- 新版 `00b822f0`（命令位置の公開資料なし）

~~~diff
- 00b81d80 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b81d80 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b81d80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b81d80 bytes a9031af8
- 00b81ec8 ["INT_ADD", "register:40f0:8", ["const:b81ec8:8", "const:4:8"]]
- 00b81ec8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b822f0 ["INT_ADD", "register:40f0:8", ["const:b822f0:8", "const:4:8"]]
+ 00b822f0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b81ec8 bytes 2e570394
+ 00b822f0 bytes 24570394
- 00b81edc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00b81edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b81edc bytes e023803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef293b3261e42e3f81f6fd2b642c702d"></a>

### [`00b82890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md) → [`00b82cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82cb8.md) _ZN11flatbuffers6Parser9ParseEnumEbPPNS_7EnumDefEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3a0.md) · 呼出先 36件 [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00babb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00babb74.md) [`00bacfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bacfd0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5c7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7a0.md) · 呼出先 36件 [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00babf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bab/00babf9c.md) [`00bad3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.24% / 新版 92.24%

CFGの説明率　旧版 86.50% / 新版 87.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 3件, `store_value` 17件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 29件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82d04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84310"
      ]
    ],
    [
      "unmatched:00b82954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82d64"
      ]
    ],
    [
      "unmatched:00b82cd8",
      "READ",
      [
        "storage",
        "002a8488",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b82d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84310"
      ]
    ],
    [
      "00b82d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82d64"
      ]
    ],
    [
      "00b83100",
      "READ",
      [
        "storage",
        "002a8555",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b829fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md#insn-00b829fc) · [`00b82a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md#insn-00b82a0c) · [`00b82a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md#insn-00b82a58)
- 新版 `00b82e24`（命令位置の公開資料なし） · `00b82e34`（命令位置の公開資料なし） · `00b82e80`（命令位置の公開資料なし）

~~~diff
- 00b829fc ["BRANCH", null, ["local:b16:8"]]
+ 00b82e24 ["BRANCH", null, ["local:b17:8"]]
- 00b829fc bytes 0e000014
+ 00b82e24 bytes 0e000014
- 00b82a0c ["INT_ADD", "register:40f0:8", ["const:b82a0c:8", "const:4:8"]]
- 00b82a0c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b82e34 ["INT_ADD", "register:40f0:8", ["const:b82e34:8", "const:4:8"]]
+ 00b82e34 ["CALL", null, ["callee:00c57e90:8"]]
- 00b82a0c bytes 21540394
+ 00b82e34 bytes 17540394
- 00b82a58 ["INT_ADD", "register:40f0:8", ["const:b82a58:8", "const:4:8"]]
- 00b82a58 ["CALL", null, ["callee:00c5c750:8"]]
+ 00b82e80 ["INT_ADD", "register:40f0:8", ["const:b82e80:8", "const:4:8"]]
+ 00b82e80 ["CALL", null, ["callee:00c5c750:8"]]
- 00b82a58 bytes 3e660394
+ 00b82e80 bytes 34660394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

