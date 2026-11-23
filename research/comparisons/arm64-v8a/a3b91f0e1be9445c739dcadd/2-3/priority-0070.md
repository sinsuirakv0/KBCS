# v15.7.4 → v16.0.0 · 最優先の変更候補 (70)

[一覧の目次](README.md)

<a id="compare-75f2e7c19aeb8ca2d3b6c8df5c52bb83"></a>

### [`00b68a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a58.md) → [`00bd7f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f58.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7f88",
      "incomplete_value": true,
      "site": "00bd7f88",
      "value": [
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
      "definition_site": "00b68a88",
      "incomplete_value": true,
      "site": "00b68a88",
      "value": [
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
      "definition_site": "00bd7f6c",
      "incomplete_value": true,
      "site": "00bd7f6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a6c",
      "incomplete_value": true,
      "site": "00b68a6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7f78",
      "incomplete_value": false,
      "site": "00bd7f80",
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
      "definition_site": "00b68a78",
      "incomplete_value": false,
      "site": "00b68a80",
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
      "00bd7f68",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7f78",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00bd7f88",
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
      "00bd7f68",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7f78",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd7f88",
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

- 旧版 [`00b68a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a58.md#insn-00b68a80) · [`00b68a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a58.md#insn-00b68a88) · [`00b68a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a58.md#insn-00b68a64)
- 新版 `00bd7f80`（命令位置の公開資料なし） · `00bd7f88`（命令位置の公開資料なし） · `00bd7f64`（命令位置の公開資料なし）

~~~diff
- 00b68a80 ["INT_ADD", "register:40f0:8", ["const:b68a80:8", "const:4:8"]]
- 00b68a80 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7f80 ["INT_ADD", "register:40f0:8", ["const:bd7f80:8", "const:4:8"]]
+ 00bd7f80 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68a80 bytes 84d50194
+ 00bd7f80 bytes e40a0294
- 00b68a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00b68a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7f88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00bd7f88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a88 bytes 60ea04f9
+ 00bd7f88 bytes 606e04f9
- 00b68a64 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7f64 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68a64 bytes d32900b0
+ 00bd7f64 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-160cf2dcc95137733a29fb99ef06d429"></a>

### [`00b68a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a9c.md) → [`00bd7f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f9c.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7fcc",
      "incomplete_value": true,
      "site": "00bd7fcc",
      "value": [
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
      "definition_site": "00b68acc",
      "incomplete_value": true,
      "site": "00b68acc",
      "value": [
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
      "definition_site": "00bd7fb0",
      "incomplete_value": true,
      "site": "00bd7fb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ab0",
      "incomplete_value": true,
      "site": "00b68ab0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7fb8",
      "incomplete_value": false,
      "site": "00bd7fc4",
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
      "definition_site": "00b68ab8",
      "incomplete_value": false,
      "site": "00b68ac4",
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
      "00bd7fac",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7fb8",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00bd7fcc",
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
      "00bd7fac",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7fb8",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd7fcc",
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

- 旧版 [`00b68ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a9c.md#insn-00b68ac4) · [`00b68acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a9c.md#insn-00b68acc) · [`00b68aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a9c.md#insn-00b68aa8)
- 新版 `00bd7fc4`（命令位置の公開資料なし） · `00bd7fcc`（命令位置の公開資料なし） · `00bd7fa8`（命令位置の公開資料なし）

~~~diff
- 00b68ac4 ["INT_ADD", "register:40f0:8", ["const:b68ac4:8", "const:4:8"]]
- 00b68ac4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd7fc4 ["INT_ADD", "register:40f0:8", ["const:bd7fc4:8", "const:4:8"]]
+ 00bd7fc4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68ac4 bytes 73d50194
+ 00bd7fc4 bytes d30a0294
- 00b68acc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00b68acc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00bd7fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68acc bytes 60ea04f9
+ 00bd7fcc bytes 606e04f9
- 00b68aa8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd7fa8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b68aa8 bytes d32900b0
+ 00bd7fa8 bytes 732a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c61dbdcefb2571d57af9bd59cdaa6767"></a>

### [`00b68aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md) → [`00bd7fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7fec.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8044",
      "incomplete_value": true,
      "site": "00bd8044",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68b44",
      "incomplete_value": true,
      "site": "00b68b44",
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
            "const:9d8:8"
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
      "definition_site": "00bd8020",
      "incomplete_value": true,
      "site": "00bd802c",
      "value": [
        "LOAD",
        "8",
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
                "const:8d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68b20",
      "incomplete_value": true,
      "site": "00b68b2c",
      "value": [
        "LOAD",
        "8",
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
                "const:9d0:8"
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
      "site": "00b68b54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd8000",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd800c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b68b48"
      ]
    ],
    [
      "00bd8020",
      "READ",
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
      "00bd8000",
      "READ",
      [
        "storage",
        "011268e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd800c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8048"
      ]
    ],
    [
      "00bd8020",
      "READ",
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

- 旧版 [`00b68b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md#insn-00b68b2c) · [`00b68b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md#insn-00b68b44) · [`00b68b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md#insn-00b68b54)
- 新版 `00bd802c`（命令位置の公開資料なし） · `00bd8044`（命令位置の公開資料なし）

~~~diff
- 00b68b2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68b2c ["INT_ADD", "register:40f0:8", ["const:b68b2c:8", "const:4:8"]]
- 00b68b2c ["CALLIND", null, ["register:0:8"]]
+ 00bd802c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd802c ["INT_ADD", "register:40f0:8", ["const:bd802c:8", "const:4:8"]]
+ 00bd802c ["CALLIND", null, ["register:0:8"]]
- 00b68b2c bytes 00013fd6
+ 00bd802c bytes 00013fd6
- 00b68b44 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68b44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d8:8"]]
- 00b68b44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd8044 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd8044 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8e0:8"]]
+ 00bd8044 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68b44 bytes a0622739
+ 00bd8044 bytes a0822339
- 00b68b54 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b68b54 ["RETURN", null, ["register:0:8"]]
- 00b68b54 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b9e63c6bfeb5d863adbd2f83f5b1d65"></a>

### [`00b68bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68bc8.md) → [`00bd80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd80c8.md) _ZN8firebase4auth15phonecredential14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b68bc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68bc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68bcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68bc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68bcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68bdc",
      "READ",
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
      "00bd80c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd80cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd80dc",
      "READ",
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

- 旧版 [`00b68bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68bc8.md#insn-00b68bc8) · [`00b68bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68bc8.md#insn-00b68bcc) · [`00b68be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68bc8.md#insn-00b68be4)

~~~diff
- 00b68bc8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b68bc8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b68bc8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b68bc8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b68bc8 bytes f44fbea9
- 00b68bcc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b68bcc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b68bcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b68bcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b68bcc bytes fd7b01a9
- 00b68be4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b68be4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b68be4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aeb4f6260f1032bdcf857b279bf89fc"></a>

### [`00b68c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c38.md) → [`00bd8138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8138.md) _ZN8firebase4auth15phonecredential11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd8154",
      "incomplete_value": false,
      "site": "00bd8158",
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
      "definition_site": "00b68c54",
      "incomplete_value": false,
      "site": "00b68c58",
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
      "definition_site": "00bd8164",
      "incomplete_value": true,
      "site": "00bd8170",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68c64",
      "incomplete_value": true,
      "site": "00b68c70",
      "value": [
        "LOAD",
        "8",
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
      "00bd8154",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd8164",
      "DATA",
      [
        "storage",
        "010a19e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd8154",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd8164",
      "DATA",
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

- 旧版 [`00b68c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c38.md#insn-00b68c58) · [`00b68c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c38.md#insn-00b68c50) · [`00b68c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c38.md#insn-00b68c54)
- 新版 `00bd8158`（命令位置の公開資料なし） · `00bd8150`（命令位置の公開資料なし） · `00bd8154`（命令位置の公開資料なし）

~~~diff
- 00b68c58 ["INT_ADD", "register:40f0:8", ["const:b68c58:8", "const:4:8"]]
- 00b68c58 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd8158 ["INT_ADD", "register:40f0:8", ["const:bd8158:8", "const:4:8"]]
+ 00bd8158 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b68c58 bytes 4ad50194
+ 00bd8158 bytes aa0a0294
- 00b68c50 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd8150 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b68c50 bytes 80b9ff90
+ 00bd8150 bytes 80b6ff90
- 00b68c54 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b68c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd8154 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd8154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68c54 bytes 001c1591
+ 00bd8154 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c271e690714efc6dea439800e89d4672"></a>

### [`00b68c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c74.md) → [`00bd8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8174.md) _ZN8firebase4auth15phonecredential13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd81b4",
      "incomplete_value": true,
      "site": "00bd81b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68cb4",
      "incomplete_value": true,
      "site": "00b68cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "definition_site": "00bd8190",
      "incomplete_value": true,
      "site": "00bd8190",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68c90",
      "incomplete_value": true,
      "site": "00b68c90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8198",
      "incomplete_value": false,
      "site": "00bd81ac",
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
      "definition_site": "00b68c98",
      "incomplete_value": false,
      "site": "00b68cac",
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
      "00bd8188",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8198",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00bd81b4",
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
      "00bd8188",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8198",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd81b4",
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

- 旧版 [`00b68cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c74.md#insn-00b68cac) · [`00b68cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c74.md#insn-00b68cb4) · [`00b68c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c74.md#insn-00b68c80)
- 新版 `00bd81ac`（命令位置の公開資料なし） · `00bd81b4`（命令位置の公開資料なし） · `00bd8180`（命令位置の公開資料なし）

~~~diff
- 00b68cac ["INT_ADD", "register:40f0:8", ["const:b68cac:8", "const:4:8"]]
- 00b68cac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd81ac ["INT_ADD", "register:40f0:8", ["const:bd81ac:8", "const:4:8"]]
+ 00bd81ac ["CALL", null, ["callee:00c5ab10:8"]]
- 00b68cac bytes f9d40194
+ 00bd81ac bytes 590a0294
- 00b68cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00b68cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd81b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00bd81b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68cb4 bytes 80ea04f9
+ 00bd81b4 bytes 806e04f9
- 00b68c80 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd8180 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b68c80 bytes d42900b0
+ 00bd8180 bytes 742a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df02e4d6f262b6d4d12950f1042f7c0f"></a>

### [`00b68ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68ce4.md) → [`00bd81e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd81e4.md) _ZN8firebase4auth15phonecredential10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd8200",
      "incomplete_value": false,
      "site": "00bd8204",
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
      "definition_site": "00b68d00",
      "incomplete_value": false,
      "site": "00b68d04",
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
      "definition_site": "00bd8210",
      "incomplete_value": true,
      "site": "00bd821c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68d10",
      "incomplete_value": true,
      "site": "00b68d1c",
      "value": [
        "LOAD",
        "8",
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
      "00bd8200",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd8210",
      "DATA",
      [
        "storage",
        "010a19e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd8200",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd8210",
      "DATA",
      [
        "storage",
        "011268f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68ce4.md#insn-00b68d04) · [`00b68cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68ce4.md#insn-00b68cfc) · [`00b68d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68ce4.md#insn-00b68d00)
- 新版 `00bd8204`（命令位置の公開資料なし） · `00bd81fc`（命令位置の公開資料なし） · `00bd8200`（命令位置の公開資料なし）

~~~diff
- 00b68d04 ["INT_ADD", "register:40f0:8", ["const:b68d04:8", "const:4:8"]]
- 00b68d04 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd8204 ["INT_ADD", "register:40f0:8", ["const:bd8204:8", "const:4:8"]]
+ 00bd8204 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b68d04 bytes 1fd50194
+ 00bd8204 bytes 7f0a0294
- 00b68cfc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd81fc ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b68cfc bytes 80b9ffb0
+ 00bd81fc bytes 80b6ffb0
- 00b68d00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b68d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd8200 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd8200 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8200 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8200 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68d00 bytes 00c81791
+ 00bd8200 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcbf669621581c61c80c13ec5c0630ba"></a>

### [`00b68d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68d20.md) → [`00bd8220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8220.md) _ZN8firebase4auth24CacheCredentialMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cb0.md) · 呼出先 4件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8b0.md) · 呼出先 4件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 18.00% / 新版 18.00%

CFGの説明率　旧版 5.43% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_destination` 1件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 26件, `unresolved_store_alignment` 22件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68d24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68d24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b68d28",
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
      "00bd8220",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd8224",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd8228",
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

- 旧版 [`00b68d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68d20.md#insn-00b68d20) · [`00b68d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68d20.md#insn-00b68d24) · [`00b68d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68d20.md#insn-00b68d28)

~~~diff
- 00b68d20 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b68d20 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b68d20 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b68d20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b68d20 bytes f657bda9
- 00b68d24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b68d24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b68d24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b68d24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b68d24 bytes f44f01a9
- 00b68d28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b68d28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b68d28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b68d28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b68d28 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45b73ea4ed2dad40cae1911f27bb4b8c"></a>

### [`00b6938c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b6938c.md) → [`00bd888c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd888c.md) _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cc0.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8c0.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.17% / 新版 13.17%

CFGの説明率　旧版 6.60% / 新版 6.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 28件, `unresolved_call_alignment` 48件, `unresolved_store_alignment` 32件

アドレスに依存する影響 `branch_value` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b693c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b693e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd88a0",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd88a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b693ec"
      ]
    ],
    [
      "00bd88b0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd88a0",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd88a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd88ec"
      ]
    ],
    [
      "00bd88b0",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b693c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b6938c.md#insn-00b693c8) · [`00b693e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b6938c.md#insn-00b693e8) · [`00b69414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b6938c.md#insn-00b69414)

~~~diff
- 00b693c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b693c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b693c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
- 00b693c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b693c8 bytes bfa22539
- 00b693e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b693e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b693e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b693e8 bytes 9fb204f9
- 00b69414 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b69414 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b69414 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
- 00b69414 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b69414 bytes bf221d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17c1bc8483b5288d8887aee5d5b6cc7f"></a>

### [`00b698c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b698c4.md) → [`00bd8dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8dc4.md) _ZN8firebase4auth10CredentialD2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00be0e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e00.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 2件 [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5da00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da00.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8dec",
      "incomplete_value": false,
      "site": "00bd8df0",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b698ec",
      "incomplete_value": false,
      "site": "00b698f0",
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
            "const:ed7:8"
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
      "00bd8dec",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd8dec",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b698f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b698c4.md#insn-00b698f0) · [`00b698dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b698c4.md#insn-00b698dc) · [`00b698e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b698c4.md#insn-00b698e8)
- 新版 `00bd8df0`（命令位置の公開資料なし） · `00bd8ddc`（命令位置の公開資料なし） · `00bd8de8`（命令位置の公開資料なし）

~~~diff
- 00b698f0 ["INT_ADD", "register:40f0:8", ["const:b698f0:8", "const:4:8"]]
- 00b698f0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd8df0 ["INT_ADD", "register:40f0:8", ["const:bd8df0:8", "const:4:8"]]
+ 00bd8df0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b698f0 bytes 24d20194
+ 00bd8df0 bytes 84070294
- 00b698dc ["INT_ADD", "register:40f0:8", ["const:b698dc:8", "const:4:8"]]
- 00b698dc ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bd8ddc ["INT_ADD", "register:40f0:8", ["const:bd8ddc:8", "const:4:8"]]
+ 00bd8ddc ["CALL", null, ["callee:00c5ae60:8"]]
- 00b698dc bytes c1d20194
+ 00bd8ddc bytes 21080294
- 00b698e8 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bd8de8 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b698e8 bytes c0b9ff90
+ 00bd8de8 bytes c0b6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b540cab00a6f9710979826eaea0e45"></a>

### [`00b69998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69998.md) → [`00bd8e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e98.md) _ZN8firebase4auth10CredentialaSERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) · 呼出先 4件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 1件 [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) · 呼出先 4件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 73.33% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd8f48"
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
      "00bd8ed0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b69a10",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd8ed0",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd8f10",
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

- 旧版 [`00b699d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69998.md#insn-00b699d4) · [`00b69a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69998.md#insn-00b69a10) · [`00b69a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69998.md#insn-00b69a48)
- 新版 `00bd8ed4`（命令位置の公開資料なし）

~~~diff
- 00b699d4 ["INT_ADD", "register:40f0:8", ["const:b699d4:8", "const:4:8"]]
- 00b699d4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd8ed4 ["INT_ADD", "register:40f0:8", ["const:bd8ed4:8", "const:4:8"]]
+ 00bd8ed4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b699d4 bytes ebd10194
+ 00bd8ed4 bytes 4b070294
- 00b69a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b69a10 ["INT_ADD", "register:40f0:8", ["const:b69a10:8", "const:4:8"]]
- 00b69a10 ["CALLIND", null, ["register:0:8"]]
- 00b69a10 bytes 00013fd6
- 00b69a48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b69a48 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00b69a48 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b69a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b69a48 bytes 6115889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361c0957f6306b40a4dad895abba612e"></a>

### [`00b69a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69a68.md) → [`00bd8f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8f68.md) _ZNK8firebase4auth10Credential8providerEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8f90",
      "incomplete_value": true,
      "site": "00bd8f94",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69a90",
      "incomplete_value": false,
      "site": "00b69a94",
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
            "const:ed7:8"
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
      "definition_site": "00bd8fac",
      "incomplete_value": true,
      "site": "00bd8fb4",
      "value": [
        "LOAD",
        "8",
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
                "const:658:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69aac",
      "incomplete_value": true,
      "site": "00b69ab4",
      "value": [
        "LOAD",
        "8",
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69ae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b69a90",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00bd8fac",
      "READ",
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
      "00bd8f90",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd8fac",
      "READ",
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

- 旧版 [`00b69a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69a68.md#insn-00b69a94) · [`00b69ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69a68.md#insn-00b69ab4) · [`00b69ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69a68.md#insn-00b69ae8)
- 新版 `00bd8f94`（命令位置の公開資料なし） · `00bd8fb4`（命令位置の公開資料なし）

~~~diff
- 00b69a94 ["INT_ADD", "register:40f0:8", ["const:b69a94:8", "const:4:8"]]
- 00b69a94 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd8f94 ["INT_ADD", "register:40f0:8", ["const:bd8f94:8", "const:4:8"]]
+ 00bd8f94 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69a94 bytes bbd10194
+ 00bd8f94 bytes 1b070294
- 00b69ab4 ["INT_ADD", "register:40f0:8", ["const:b69ab4:8", "const:4:8"]]
- 00b69ab4 ["CALL", null, ["callee:004977f4:8"]]
+ 00bd8fb4 ["INT_ADD", "register:40f0:8", ["const:bd8fb4:8", "const:4:8"]]
+ 00bd8fb4 ["CALL", null, ["callee:004977f4:8"]]
- 00b69ab4 bytes aa2be497
+ 00bd8fb4 bytes 10fae297
- 00b69ae8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b69ae8 ["RETURN", null, ["register:0:8"]]
- 00b69ae8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc4c2e1c4d2a88d97c82bfacc969e17e"></a>

### [`00b69aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69aec.md) → [`00bd8fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8fec.md) _ZNK8firebase4auth10Credential8is_validEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-842ffb01ddd84d61c42376e41a896cc6"></a>

### [`00b69afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md) → [`00bd8ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8ffc.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 75.76% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9054",
      "incomplete_value": false,
      "site": "00bd9058",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69b54",
      "incomplete_value": false,
      "site": "00b69b58",
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
            "const:ed7:8"
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
      "definition_site": "00bd9098",
      "incomplete_value": true,
      "site": "00bd90b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b69b98",
      "incomplete_value": true,
      "site": "00b69bb0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd909c",
      "incomplete_value": true,
      "site": "00bd90b0",
      "value": [
        "LOAD",
        "8",
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69b9c",
      "incomplete_value": true,
      "site": "00b69bb0",
      "value": [
        "LOAD",
        "8",
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
                "const:770:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b69b38",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd903c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b69cc8"
      ]
    ],
    [
      "00bd9054",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9038",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd903c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd91c8"
      ]
    ],
    [
      "00bd9054",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md#insn-00b69b58) · [`00b69bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md#insn-00b69bb0) · [`00b69c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md#insn-00b69c00)
- 新版 `00bd9058`（命令位置の公開資料なし） · `00bd90b0`（命令位置の公開資料なし） · `00bd9100`（命令位置の公開資料なし）

~~~diff
- 00b69b58 ["INT_ADD", "register:40f0:8", ["const:b69b58:8", "const:4:8"]]
- 00b69b58 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9058 ["INT_ADD", "register:40f0:8", ["const:bd9058:8", "const:4:8"]]
+ 00bd9058 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69b58 bytes 8ad10194
+ 00bd9058 bytes ea060294
- 00b69bb0 ["INT_ADD", "register:40f0:8", ["const:b69bb0:8", "const:4:8"]]
- 00b69bb0 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd90b0 ["INT_ADD", "register:40f0:8", ["const:bd90b0:8", "const:4:8"]]
+ 00bd90b0 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b69bb0 bytes 64d00194
+ 00bd90b0 bytes bc050294
- 00b69c00 ["INT_ADD", "register:40f0:8", ["const:b69c00:8", "const:4:8"]]
- 00b69c00 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9100 ["INT_ADD", "register:40f0:8", ["const:bd9100:8", "const:4:8"]]
+ 00bd9100 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69c00 bytes 60d10194
+ 00bd9100 bytes c0060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0941a01a62557abb5ef203dd35773295"></a>

### [`00b69e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69e40.md) → [`00bd9340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9340.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9370",
      "incomplete_value": false,
      "site": "00bd9374",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69e70",
      "incomplete_value": false,
      "site": "00b69e74",
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
            "const:ed7:8"
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
      "definition_site": "00bd9388",
      "incomplete_value": true,
      "site": "00bd9390",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b69e88",
      "incomplete_value": true,
      "site": "00b69e90",
      "value": [
        "LOAD",
        "8",
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
                "const:9e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9370",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00bd9388",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd9370",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd9388",
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

- 旧版 [`00b69e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69e40.md#insn-00b69e74) · [`00b69e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69e40.md#insn-00b69e90) · [`00b69e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69e40.md#insn-00b69e60)
- 新版 `00bd9374`（命令位置の公開資料なし） · `00bd9390`（命令位置の公開資料なし） · `00bd9360`（命令位置の公開資料なし）

~~~diff
- 00b69e74 ["INT_ADD", "register:40f0:8", ["const:b69e74:8", "const:4:8"]]
- 00b69e74 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9374 ["INT_ADD", "register:40f0:8", ["const:bd9374:8", "const:4:8"]]
+ 00bd9374 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69e74 bytes c3d00194
+ 00bd9374 bytes 23060294
- 00b69e90 ["INT_ADD", "register:40f0:8", ["const:b69e90:8", "const:4:8"]]
- 00b69e90 ["CALL", null, ["callee:004977f4:8"]]
+ 00bd9390 ["INT_ADD", "register:40f0:8", ["const:bd9390:8", "const:4:8"]]
+ 00bd9390 ["CALL", null, ["callee:004977f4:8"]]
- 00b69e90 bytes b32ae497
+ 00bd9390 bytes 19f9e297
- 00b69e60 ["INT_ADD", "register:40f0:8", ["const:b69e60:8", "const:4:8"]]
- 00b69e60 ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bd9360 ["INT_ADD", "register:40f0:8", ["const:bd9360:8", "const:4:8"]]
+ 00bd9360 ["CALL", null, ["callee:00c5ae60:8"]]
- 00b69e60 bytes 60d10194
+ 00bd9360 bytes c0060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ecbe3f174a32a1faaa65fbe5ecb09c"></a>

### [`00b69ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69ec8.md) → [`00bd93c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd93c8.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0da0.md) · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 1件 [`00c5d9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9a0.md) · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd93f4",
      "incomplete_value": false,
      "site": "00bd93f8",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69ef4",
      "incomplete_value": false,
      "site": "00b69ef8",
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
            "const:ed7:8"
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
      "00bd93f4",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd93f4",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69ec8.md#insn-00b69ef8) · [`00b69ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69ec8.md#insn-00b69ee4) · [`00b69ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69ec8.md#insn-00b69ef0)
- 新版 `00bd93f8`（命令位置の公開資料なし） · `00bd93e4`（命令位置の公開資料なし） · `00bd93f0`（命令位置の公開資料なし）

~~~diff
- 00b69ef8 ["INT_ADD", "register:40f0:8", ["const:b69ef8:8", "const:4:8"]]
- 00b69ef8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd93f8 ["INT_ADD", "register:40f0:8", ["const:bd93f8:8", "const:4:8"]]
+ 00bd93f8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69ef8 bytes a2d00194
+ 00bd93f8 bytes 02060294
- 00b69ee4 ["INT_ADD", "register:40f0:8", ["const:b69ee4:8", "const:4:8"]]
- 00b69ee4 ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bd93e4 ["INT_ADD", "register:40f0:8", ["const:bd93e4:8", "const:4:8"]]
+ 00bd93e4 ["CALL", null, ["callee:00c5ae60:8"]]
- 00b69ee4 bytes 3fd10194
+ 00bd93e4 bytes 9f060294
- 00b69ef0 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bd93f0 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b69ef0 bytes c0b9ff90
+ 00bd93f0 bytes c0b6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653723508d3bdf4cde99e9a123643f4f"></a>

### [`00b69f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69f58.md) → [`00bd9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9458.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9494",
      "incomplete_value": false,
      "site": "00bd9498",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69f94",
      "incomplete_value": false,
      "site": "00b69f98",
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
            "const:ed7:8"
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
      "definition_site": "00bd94c0",
      "incomplete_value": true,
      "site": "00bd94d4",
      "value": [
        "LOAD",
        "8",
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
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69fc0",
      "incomplete_value": true,
      "site": "00b69fd4",
      "value": [
        "LOAD",
        "8",
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
                "const:780:8"
              ]
            ]
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
      "definition_site": "00bd94c4",
      "incomplete_value": true,
      "site": "00bd94d4",
      "value": [
        "LOAD",
        "8",
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69fc4",
      "incomplete_value": true,
      "site": "00b69fd4",
      "value": [
        "LOAD",
        "8",
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9478",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd947c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a064"
      ]
    ],
    [
      "00bd9494",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9478",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd947c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9564"
      ]
    ],
    [
      "00bd9494",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69f58.md#insn-00b69f98) · [`00b69fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69f58.md#insn-00b69fd4) · [`00b6a01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69f58.md#insn-00b6a01c)
- 新版 `00bd9498`（命令位置の公開資料なし） · `00bd94d4`（命令位置の公開資料なし） · `00bd951c`（命令位置の公開資料なし）

~~~diff
- 00b69f98 ["INT_ADD", "register:40f0:8", ["const:b69f98:8", "const:4:8"]]
- 00b69f98 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9498 ["INT_ADD", "register:40f0:8", ["const:bd9498:8", "const:4:8"]]
+ 00bd9498 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b69f98 bytes 7ad00194
+ 00bd9498 bytes da050294
- 00b69fd4 ["INT_ADD", "register:40f0:8", ["const:b69fd4:8", "const:4:8"]]
- 00b69fd4 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd94d4 ["INT_ADD", "register:40f0:8", ["const:bd94d4:8", "const:4:8"]]
+ 00bd94d4 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b69fd4 bytes 5bcf0194
+ 00bd94d4 bytes b3040294
- 00b6a01c ["INT_ADD", "register:40f0:8", ["const:b6a01c:8", "const:4:8"]]
- 00b6a01c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd951c ["INT_ADD", "register:40f0:8", ["const:bd951c:8", "const:4:8"]]
+ 00bd951c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a01c bytes 59d00194
+ 00bd951c bytes b9050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dfe7efb3ab6e5f295c8cbcd91afca98"></a>

### [`00b6a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a0a4.md) → [`00bd95a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd95a4.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd95e0",
      "incomplete_value": false,
      "site": "00bd95e4",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a0e0",
      "incomplete_value": false,
      "site": "00b6a0e4",
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
            "const:ed7:8"
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
      "definition_site": "00bd960c",
      "incomplete_value": true,
      "site": "00bd9620",
      "value": [
        "LOAD",
        "8",
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
                "const:6a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a10c",
      "incomplete_value": true,
      "site": "00b6a120",
      "value": [
        "LOAD",
        "8",
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
                "const:7a0:8"
              ]
            ]
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
      "definition_site": "00bd9610",
      "incomplete_value": true,
      "site": "00bd9620",
      "value": [
        "LOAD",
        "8",
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
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a110",
      "incomplete_value": true,
      "site": "00b6a120",
      "value": [
        "LOAD",
        "8",
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
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd95c4",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd95c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a1b0"
      ]
    ],
    [
      "00bd95e0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd95c4",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd95c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd96b0"
      ]
    ],
    [
      "00bd95e0",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a0a4.md#insn-00b6a0e4) · [`00b6a120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a0a4.md#insn-00b6a120) · [`00b6a168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a0a4.md#insn-00b6a168)
- 新版 `00bd95e4`（命令位置の公開資料なし） · `00bd9620`（命令位置の公開資料なし） · `00bd9668`（命令位置の公開資料なし）

~~~diff
- 00b6a0e4 ["INT_ADD", "register:40f0:8", ["const:b6a0e4:8", "const:4:8"]]
- 00b6a0e4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd95e4 ["INT_ADD", "register:40f0:8", ["const:bd95e4:8", "const:4:8"]]
+ 00bd95e4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a0e4 bytes 27d00194
+ 00bd95e4 bytes 87050294
- 00b6a120 ["INT_ADD", "register:40f0:8", ["const:b6a120:8", "const:4:8"]]
- 00b6a120 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd9620 ["INT_ADD", "register:40f0:8", ["const:bd9620:8", "const:4:8"]]
+ 00bd9620 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6a120 bytes 08cf0194
+ 00bd9620 bytes 60040294
- 00b6a168 ["INT_ADD", "register:40f0:8", ["const:b6a168:8", "const:4:8"]]
- 00b6a168 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9668 ["INT_ADD", "register:40f0:8", ["const:bd9668:8", "const:4:8"]]
+ 00bd9668 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a168 bytes 06d00194
+ 00bd9668 bytes 66050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6fdb50ba7df8732931a2b383a0280a"></a>

### [`00b6a1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a1f0.md) → [`00bd96f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd96f0.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb80.md) · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5a5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5d0.md) · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd972c",
      "incomplete_value": false,
      "site": "00bd9730",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a22c",
      "incomplete_value": false,
      "site": "00b6a230",
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
            "const:ed7:8"
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
      "definition_site": "00bd9790",
      "incomplete_value": false,
      "site": "00bd9794",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a290",
      "incomplete_value": false,
      "site": "00b6a294",
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
            "const:261:8"
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
      "definition_site": "00bd979c",
      "incomplete_value": false,
      "site": "00bd97a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a29c",
      "incomplete_value": false,
      "site": "00b6a2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2fa000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00bd9708",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd972c",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00bd9790",
      "PARAM",
      [
        "storage",
        "002a7261",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9708",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd972c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd9790",
      "PARAM",
      [
        "storage",
        "002b7dd0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a1f0.md#insn-00b6a230) · [`00b6a294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a1f0.md#insn-00b6a294) · [`00b6a2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a1f0.md#insn-00b6a2a0)
- 新版 `00bd9730`（命令位置の公開資料なし） · `00bd9794`（命令位置の公開資料なし） · `00bd97a0`（命令位置の公開資料なし）

~~~diff
- 00b6a230 ["INT_ADD", "register:40f0:8", ["const:b6a230:8", "const:4:8"]]
- 00b6a230 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9730 ["INT_ADD", "register:40f0:8", ["const:bd9730:8", "const:4:8"]]
+ 00bd9730 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a230 bytes d4cf0194
+ 00bd9730 bytes 34050294
- 00b6a294 ["INT_ADD", "register:40f0:8", ["const:b6a294:8", "const:4:8"]]
- 00b6a294 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bd9794 ["INT_ADD", "register:40f0:8", ["const:bd9794:8", "const:4:8"]]
+ 00bd9794 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b6a294 bytes ebce0194
+ 00bd9794 bytes 43040294
- 00b6a2a0 ["INT_ADD", "register:40f0:8", ["const:b6a2a0:8", "const:4:8"]]
- 00b6a2a0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd97a0 ["INT_ADD", "register:40f0:8", ["const:bd97a0:8", "const:4:8"]]
+ 00bd97a0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a2a0 bytes b8cf0194
+ 00bd97a0 bytes 18050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7385b83ff2f813d198f3eab63c6e0d0"></a>

### [`00b6a394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a394.md) → [`00bd9894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 86.75% / 新版 86.75%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd98d0",
      "incomplete_value": false,
      "site": "00bd98d4",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a3d0",
      "incomplete_value": false,
      "site": "00b6a3d4",
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
            "const:ed7:8"
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
      "definition_site": "00bd98fc",
      "incomplete_value": true,
      "site": "00bd9910",
      "value": [
        "LOAD",
        "8",
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
                "const:6e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a3fc",
      "incomplete_value": true,
      "site": "00b6a410",
      "value": [
        "LOAD",
        "8",
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
                "const:7e0:8"
              ]
            ]
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
      "definition_site": "00bd9900",
      "incomplete_value": true,
      "site": "00bd9910",
      "value": [
        "LOAD",
        "8",
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
                "const:6f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a400",
      "incomplete_value": true,
      "site": "00b6a410",
      "value": [
        "LOAD",
        "8",
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
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd98b4",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd98b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a4a0"
      ]
    ],
    [
      "00bd98d0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd98b4",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd98b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd99a0"
      ]
    ],
    [
      "00bd98d0",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a394.md#insn-00b6a3d4) · [`00b6a410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a394.md#insn-00b6a410) · [`00b6a458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a394.md#insn-00b6a458)
- 新版 `00bd98d4`（命令位置の公開資料なし） · `00bd9910`（命令位置の公開資料なし） · `00bd9958`（命令位置の公開資料なし）

~~~diff
- 00b6a3d4 ["INT_ADD", "register:40f0:8", ["const:b6a3d4:8", "const:4:8"]]
- 00b6a3d4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd98d4 ["INT_ADD", "register:40f0:8", ["const:bd98d4:8", "const:4:8"]]
+ 00bd98d4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a3d4 bytes 6bcf0194
+ 00bd98d4 bytes cb040294
- 00b6a410 ["INT_ADD", "register:40f0:8", ["const:b6a410:8", "const:4:8"]]
- 00b6a410 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd9910 ["INT_ADD", "register:40f0:8", ["const:bd9910:8", "const:4:8"]]
+ 00bd9910 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6a410 bytes 4cce0194
+ 00bd9910 bytes a4030294
- 00b6a458 ["INT_ADD", "register:40f0:8", ["const:b6a458:8", "const:4:8"]]
- 00b6a458 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9958 ["INT_ADD", "register:40f0:8", ["const:bd9958:8", "const:4:8"]]
+ 00bd9958 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a458 bytes 4acf0194
+ 00bd9958 bytes aa040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9904df06177985fd170ed2789da6db41"></a>

### [`00b6a4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a4e0.md) → [`00bd99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd99e0.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 90.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9a24",
      "incomplete_value": false,
      "site": "00bd9a28",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a524",
      "incomplete_value": false,
      "site": "00b6a528",
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
            "const:ed7:8"
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
      "definition_site": "00bd9a68",
      "incomplete_value": true,
      "site": "00bd9a80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6a568",
      "incomplete_value": true,
      "site": "00b6a580",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9a6c",
      "incomplete_value": true,
      "site": "00bd9a80",
      "value": [
        "LOAD",
        "8",
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
                "const:718:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a56c",
      "incomplete_value": true,
      "site": "00b6a580",
      "value": [
        "LOAD",
        "8",
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9a08",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a624"
      ]
    ],
    [
      "00bd9a24",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9a08",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9b24"
      ]
    ],
    [
      "00bd9a24",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a4e0.md#insn-00b6a528) · [`00b6a580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a4e0.md#insn-00b6a580) · [`00b6a5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a4e0.md#insn-00b6a5dc)
- 新版 `00bd9a28`（命令位置の公開資料なし） · `00bd9a80`（命令位置の公開資料なし） · `00bd9adc`（命令位置の公開資料なし）

~~~diff
- 00b6a528 ["INT_ADD", "register:40f0:8", ["const:b6a528:8", "const:4:8"]]
- 00b6a528 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9a28 ["INT_ADD", "register:40f0:8", ["const:bd9a28:8", "const:4:8"]]
+ 00bd9a28 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a528 bytes 16cf0194
+ 00bd9a28 bytes 76040294
- 00b6a580 ["INT_ADD", "register:40f0:8", ["const:b6a580:8", "const:4:8"]]
- 00b6a580 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd9a80 ["INT_ADD", "register:40f0:8", ["const:bd9a80:8", "const:4:8"]]
+ 00bd9a80 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6a580 bytes f0cd0194
+ 00bd9a80 bytes 48030294
- 00b6a5dc ["INT_ADD", "register:40f0:8", ["const:b6a5dc:8", "const:4:8"]]
- 00b6a5dc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9adc ["INT_ADD", "register:40f0:8", ["const:bd9adc:8", "const:4:8"]]
+ 00bd9adc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a5dc bytes e9ce0194
+ 00bd9adc bytes 49040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-879c2f7ea121c7bd9c91519e535a600b"></a>

### [`00b6a664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md) → [`00bd9b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9b64.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 82.30% / 新版 82.30%

CFGの説明率　旧版 50.00% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9bb4",
      "incomplete_value": false,
      "site": "00bd9bb8",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a6b4",
      "incomplete_value": false,
      "site": "00b6a6b8",
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
            "const:ed7:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a6d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9c10",
      "incomplete_value": true,
      "site": "00bd9c2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6a710",
      "incomplete_value": true,
      "site": "00b6a72c",
      "value": [
        "LOAD",
        "8",
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
      "00bd9b98",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a7e4"
      ]
    ],
    [
      "unmatched:00b6a6b4",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9b98",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9ce4"
      ]
    ],
    [
      "00bd9bb4",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a6b8) · [`00b6a6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a6d4) · [`00b6a72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a72c)
- 新版 `00bd9bb8`（命令位置の公開資料なし） · `00bd9c2c`（命令位置の公開資料なし）

~~~diff
- 00b6a6b8 ["INT_ADD", "register:40f0:8", ["const:b6a6b8:8", "const:4:8"]]
- 00b6a6b8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9bb8 ["INT_ADD", "register:40f0:8", ["const:bd9bb8:8", "const:4:8"]]
+ 00bd9bb8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a6b8 bytes b2ce0194
+ 00bd9bb8 bytes 12040294
- 00b6a6d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6a6d4 ["INT_ADD", "register:40f0:8", ["const:b6a6d4:8", "const:4:8"]]
- 00b6a6d4 ["CALLIND", null, ["register:0:8"]]
- 00b6a6d4 bytes 00013fd6
- 00b6a72c ["INT_ADD", "register:40f0:8", ["const:b6a72c:8", "const:4:8"]]
- 00b6a72c ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd9c2c ["INT_ADD", "register:40f0:8", ["const:bd9c2c:8", "const:4:8"]]
+ 00bd9c2c ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6a72c bytes 85cd0194
+ 00bd9c2c bytes dd020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39ff1753449c12b75585bb5c552d2da"></a>

### [`00b6a828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md) → [`00bd9d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9d28.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.61% / 新版 92.61%

CFGの説明率　旧版 86.11% / 新版 88.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9d7c",
      "incomplete_value": false,
      "site": "00bd9d80",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a87c",
      "incomplete_value": false,
      "site": "00b6a880",
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
            "const:ed7:8"
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
      "definition_site": "00bd9dd8",
      "incomplete_value": true,
      "site": "00bd9dec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6a8d8",
      "incomplete_value": true,
      "site": "00b6a8ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9ddc",
      "incomplete_value": true,
      "site": "00bd9dec",
      "value": [
        "LOAD",
        "8",
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
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a8dc",
      "incomplete_value": true,
      "site": "00b6a8ec",
      "value": [
        "LOAD",
        "8",
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9d5c",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a9bc"
      ]
    ],
    [
      "00bd9d7c",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9d5c",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9ebc"
      ]
    ],
    [
      "00bd9d7c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a880) · [`00b6a8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a8ec) · [`00b6a918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a918)
- 新版 `00bd9d80`（命令位置の公開資料なし） · `00bd9dec`（命令位置の公開資料なし） · `00bd9e18`（命令位置の公開資料なし）

~~~diff
- 00b6a880 ["INT_ADD", "register:40f0:8", ["const:b6a880:8", "const:4:8"]]
- 00b6a880 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd9d80 ["INT_ADD", "register:40f0:8", ["const:bd9d80:8", "const:4:8"]]
+ 00bd9d80 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6a880 bytes 40ce0194
+ 00bd9d80 bytes a0030294
- 00b6a8ec ["INT_ADD", "register:40f0:8", ["const:b6a8ec:8", "const:4:8"]]
- 00b6a8ec ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bd9dec ["INT_ADD", "register:40f0:8", ["const:bd9dec:8", "const:4:8"]]
+ 00bd9dec ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6a8ec bytes 15cd0194
+ 00bd9dec bytes 6d020294
- 00b6a918 ["INT_ADD", "register:40f0:8", ["const:b6a918:8", "const:4:8"]]
- 00b6a918 ["CALL", null, ["callee:004977f4:8"]]
+ 00bd9e18 ["INT_ADD", "register:40f0:8", ["const:bd9e18:8", "const:4:8"]]
+ 00bd9e18 ["CALL", null, ["callee:004977f4:8"]]
- 00b6a918 bytes 1128e497
+ 00bd9e18 bytes 77f6e297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84934e1d07c52c1a40689b7cbfe5cf03"></a>

### [`00b6aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md) → [`00bd9fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b6cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdc000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc000.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6abbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bda0bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda03c",
      "incomplete_value": true,
      "site": "00bda044",
      "value": [
        "live",
        "register:40a0:8"
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
      "00bda030",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ],
    [
      "00bda030",
      "PARAM",
      [
        "storage",
        "00b6cb00",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00b6ab58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bda030",
      "READ",
      [
        "storage",
        "00c9b630",
        null,
        "pointer"
      ]
    ],
    [
      "00bda030",
      "PARAM",
      [
        "storage",
        "00bdc000",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00bda058",
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

- 旧版 [`00b6ab44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab44) · [`00b6ab58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab58) · [`00b6ab80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab80)
- 新版 `00bda044`（命令位置の公開資料なし） · `00bda080`（命令位置の公開資料なし）

~~~diff
- 00b6ab44 ["INT_ADD", "register:40f0:8", ["const:b6ab44:8", "const:4:8"]]
- 00b6ab44 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bda044 ["INT_ADD", "register:40f0:8", ["const:bda044:8", "const:4:8"]]
+ 00bda044 ["CALL", null, ["callee:00c5aa40:8"]]
- 00b6ab44 bytes 1fcd0194
+ 00bda044 bytes 7f020294
- 00b6ab58 ["INT_ADD", "register:40f0:8", ["const:b6ab58:8", "const:4:8"]]
- 00b6ab58 ["CALL", null, ["ram:bddc40:8"]]
- 00b6ab58 bytes 3acc0194
- 00b6ab80 ["INT_ADD", "register:40f0:8", ["const:b6ab80:8", "const:4:8"]]
- 00b6ab80 ["CALL", null, ["callee:00c5d9d0:8"]]
+ 00bda080 ["INT_ADD", "register:40f0:8", ["const:bda080:8", "const:4:8"]]
+ 00bda080 ["CALL", null, ["callee:00c5d9d0:8"]]
- 00b6ab80 bytes 94d80194
+ 00bda080 bytes 540e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a0ef6a2ecf1ba12b5edc252888d1216"></a>

### [`00b6ac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ac0c.md) → [`00bda10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda10c.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bda15c",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6ac5c",
      "value": [
        "leaf",
        "ram:bdde10:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bda16c",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6ac6c",
      "value": [
        "leaf",
        "ram:bddf90:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bda184",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6ac84",
      "value": [
        "leaf",
        "ram:bdde10:8"
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
      "00bda15c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bda16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ],
    [
      "00bda184",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00bda15c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bda16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ],
    [
      "00bda184",
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

- 旧版 [`00b6ac5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ac0c.md#insn-00b6ac5c) · [`00b6ac6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ac0c.md#insn-00b6ac6c) · [`00b6ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ac0c.md#insn-00b6ac84)
- 新版 `00bda15c`（命令位置の公開資料なし） · `00bda16c`（命令位置の公開資料なし） · `00bda184`（命令位置の公開資料なし）

~~~diff
- 00b6ac5c ["INT_ADD", "register:40f0:8", ["const:b6ac5c:8", "const:4:8"]]
- 00b6ac5c ["CALL", null, ["ram:bdde10:8"]]
+ 00bda15c ["INT_ADD", "register:40f0:8", ["const:bda15c:8", "const:4:8"]]
+ 00bda15c ["CALL", null, ["ram:c5a870:8"]]
- 00b6ac5c bytes 6dcc0194
+ 00bda15c bytes c5010294
- 00b6ac6c ["INT_ADD", "register:40f0:8", ["const:b6ac6c:8", "const:4:8"]]
- 00b6ac6c ["CALL", null, ["ram:bddf90:8"]]
+ 00bda16c ["INT_ADD", "register:40f0:8", ["const:bda16c:8", "const:4:8"]]
+ 00bda16c ["CALL", null, ["ram:c5aa10:8"]]
- 00b6ac6c bytes c9cc0194
+ 00bda16c bytes 29020294
- 00b6ac84 ["INT_ADD", "register:40f0:8", ["const:b6ac84:8", "const:4:8"]]
- 00b6ac84 ["CALL", null, ["ram:bdde10:8"]]
+ 00bda184 ["INT_ADD", "register:40f0:8", ["const:bda184:8", "const:4:8"]]
+ 00bda184 ["CALL", null, ["ram:c5a870:8"]]
- 00b6ac84 bytes 63cc0194
+ 00bda184 bytes bb010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e867a44580b52ef9568b0a541e80373"></a>

### [`00b6ad30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md) → [`00bda230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda230.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda23c",
      "incomplete_value": false,
      "site": "00bda240",
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
            "const:8e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ad3c",
      "incomplete_value": false,
      "site": "00b6ad40",
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
            "const:7a:8"
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
      "00bda23c",
      "PARAM",
      [
        "storage",
        "002a407a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda23c",
      "PARAM",
      [
        "storage",
        "002b48e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ad40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad40) · [`00b6ad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad38) · [`00b6ad3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad3c)
- 新版 `00bda240`（命令位置の公開資料なし） · `00bda238`（命令位置の公開資料なし） · `00bda23c`（命令位置の公開資料なし）

~~~diff
- 00b6ad40 ["INT_ADD", "register:40f0:8", ["const:b6ad40:8", "const:4:8"]]
- 00b6ad40 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda240 ["INT_ADD", "register:40f0:8", ["const:bda240:8", "const:4:8"]]
+ 00bda240 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6ad40 bytes 10cd0194
+ 00bda240 bytes 70020294
- 00b6ad38 ["COPY", "register:4000:8", ["const:2a4000:8"]]
+ 00bda238 ["COPY", "register:4000:8", ["const:2b4000:8"]]
- 00b6ad38 bytes c0b9ffd0
+ 00bda238 bytes c0b6ffd0
- 00b6ad3c ["COPY", "tmp:0:8", ["const:7a:8"]]
- 00b6ad3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ad3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ad3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda23c ["COPY", "tmp:0:8", ["const:8e7:8"]]
+ 00bda23c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda23c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda23c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ad3c bytes 00e80191
+ 00bda23c bytes 009c2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-183a0181a46a93b3f8a5bf63f5d6b761"></a>

### [`00b6ad7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md) → [`00bda27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda27c.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ad80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ad7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ad80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ada8",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda27c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bda280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bda2a8",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ad7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6ad7c) · [`00b6ad80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6ad80) · [`00b6adac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6adac)
- 新版 `00bda2ac`（命令位置の公開資料なし）

~~~diff
- 00b6ad7c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6ad7c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6ad7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6ad7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6ad7c bytes f44fbea9
- 00b6ad80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6ad80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6ad80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6ad80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ad80 bytes fd7b01a9
- 00b6adac ["INT_ADD", "register:40f0:8", ["const:b6adac:8", "const:4:8"]]
- 00b6adac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda2ac ["INT_ADD", "register:40f0:8", ["const:bda2ac:8", "const:4:8"]]
+ 00bda2ac ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6adac bytes f5cc0194
+ 00bda2ac bytes 55020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0008362271af8add144a11874d505d"></a>

### [`00b6ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md) → [`00bda320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda320.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md) · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md) · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda350",
      "incomplete_value": false,
      "site": "00bda354",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ae50",
      "incomplete_value": false,
      "site": "00b6ae54",
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
            "const:ed7:8"
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
      "definition_site": "00bda384",
      "incomplete_value": false,
      "site": "00bda388",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ae84",
      "incomplete_value": false,
      "site": "00b6ae88",
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
            "const:ed7:8"
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
      "00bda350",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00bda384",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda350",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bda384",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ae54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae54) · [`00b6ae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae88) · [`00b6ae40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae40)
- 新版 `00bda354`（命令位置の公開資料なし） · `00bda388`（命令位置の公開資料なし） · `00bda340`（命令位置の公開資料なし）

~~~diff
- 00b6ae54 ["INT_ADD", "register:40f0:8", ["const:b6ae54:8", "const:4:8"]]
- 00b6ae54 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda354 ["INT_ADD", "register:40f0:8", ["const:bda354:8", "const:4:8"]]
+ 00bda354 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6ae54 bytes cbcc0194
+ 00bda354 bytes 2b020294
- 00b6ae88 ["INT_ADD", "register:40f0:8", ["const:b6ae88:8", "const:4:8"]]
- 00b6ae88 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda388 ["INT_ADD", "register:40f0:8", ["const:bda388:8", "const:4:8"]]
+ 00bda388 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6ae88 bytes becc0194
+ 00bda388 bytes 1e020294
- 00b6ae40 ["INT_ADD", "register:40f0:8", ["const:b6ae40:8", "const:4:8"]]
- 00b6ae40 ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bda340 ["INT_ADD", "register:40f0:8", ["const:bda340:8", "const:4:8"]]
+ 00bda340 ["CALL", null, ["callee:00c5ae60:8"]]
- 00b6ae40 bytes 68cd0194
+ 00bda340 bytes c8020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce240832489b6e4529b3bd082bdb5bec"></a>

### [`00b6aef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md) → [`00bda3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3f4.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda41c",
      "incomplete_value": false,
      "site": "00bda420",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6af1c",
      "incomplete_value": false,
      "site": "00b6af20",
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
            "const:ed7:8"
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
      "00bda41c",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda41c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6af20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af20) · [`00b6af0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af0c) · [`00b6af18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af18)
- 新版 `00bda420`（命令位置の公開資料なし） · `00bda40c`（命令位置の公開資料なし） · `00bda418`（命令位置の公開資料なし）

~~~diff
- 00b6af20 ["INT_ADD", "register:40f0:8", ["const:b6af20:8", "const:4:8"]]
- 00b6af20 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda420 ["INT_ADD", "register:40f0:8", ["const:bda420:8", "const:4:8"]]
+ 00bda420 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6af20 bytes 98cc0194
+ 00bda420 bytes f8010294
- 00b6af0c ["INT_ADD", "register:40f0:8", ["const:b6af0c:8", "const:4:8"]]
- 00b6af0c ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bda40c ["INT_ADD", "register:40f0:8", ["const:bda40c:8", "const:4:8"]]
+ 00bda40c ["CALL", null, ["callee:00c5ae60:8"]]
- 00b6af0c bytes 35cd0194
+ 00bda40c bytes 95020294
- 00b6af18 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bda418 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b6af18 bytes a0b9fff0
+ 00bda418 bytes c0b6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418425f88fdb45413aeaedfcfd8810ab"></a>

### [`00b6af60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md) → [`00bda460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda460.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda488",
      "incomplete_value": false,
      "site": "00bda48c",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6af88",
      "incomplete_value": false,
      "site": "00b6af8c",
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
            "const:ed7:8"
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
      "00bda488",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda488",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af8c) · [`00b6af78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af78) · [`00b6af84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af84)
- 新版 `00bda48c`（命令位置の公開資料なし） · `00bda478`（命令位置の公開資料なし） · `00bda484`（命令位置の公開資料なし）

~~~diff
- 00b6af8c ["INT_ADD", "register:40f0:8", ["const:b6af8c:8", "const:4:8"]]
- 00b6af8c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda48c ["INT_ADD", "register:40f0:8", ["const:bda48c:8", "const:4:8"]]
+ 00bda48c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6af8c bytes 7dcc0194
+ 00bda48c bytes dd010294
- 00b6af78 ["INT_ADD", "register:40f0:8", ["const:b6af78:8", "const:4:8"]]
- 00b6af78 ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bda478 ["INT_ADD", "register:40f0:8", ["const:bda478:8", "const:4:8"]]
+ 00bda478 ["CALL", null, ["callee:00c5ae60:8"]]
- 00b6af78 bytes 1acd0194
+ 00bda478 bytes 7a020294
- 00b6af84 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bda484 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b6af84 bytes a0b9fff0
+ 00bda484 bytes c0b6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-301bdccadb5686ed6fa606599bed985b"></a>

### [`00b6afd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md) → [`00bda4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md) _ZN8firebase4auth17PhoneAuthProviderD1Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be09c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09c0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda4fc",
      "incomplete_value": false,
      "site": "00bda500",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6affc",
      "incomplete_value": false,
      "site": "00b6b000",
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
            "const:ed7:8"
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
      "00bda4fc",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda4fc",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6b000) · [`00b6afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6afec) · [`00b6aff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6aff8)
- 新版 `00bda500`（命令位置の公開資料なし） · `00bda4ec`（命令位置の公開資料なし） · `00bda4f8`（命令位置の公開資料なし）

~~~diff
- 00b6b000 ["INT_ADD", "register:40f0:8", ["const:b6b000:8", "const:4:8"]]
- 00b6b000 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda500 ["INT_ADD", "register:40f0:8", ["const:bda500:8", "const:4:8"]]
+ 00bda500 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b000 bytes 60cc0194
+ 00bda500 bytes c0010294
- 00b6afec ["INT_ADD", "register:40f0:8", ["const:b6afec:8", "const:4:8"]]
- 00b6afec ["CALL", null, ["callee:00c5ae60:8"]]
+ 00bda4ec ["INT_ADD", "register:40f0:8", ["const:bda4ec:8", "const:4:8"]]
+ 00bda4ec ["CALL", null, ["callee:00c5ae60:8"]]
- 00b6afec bytes fdcc0194
+ 00bda4ec bytes 5d020294
- 00b6aff8 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bda4f8 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b6aff8 bytes a0b9fff0
+ 00bda4f8 bytes c0b6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23aa8c0cd333d2f0d89cdb2079326b5a"></a>

### [`00b6b044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md) → [`00bda544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda544.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bda55c",
      "incomplete_value": true,
      "site": "00bda560",
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
      "definition_site": "00b6b05c",
      "incomplete_value": true,
      "site": "00b6b060",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda584",
      "incomplete_value": false,
      "site": "00bda588",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b084",
      "incomplete_value": false,
      "site": "00b6b088",
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
            "const:ed7:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda59c",
      "incomplete_value": true,
      "site": "00bda5ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6b09c",
      "incomplete_value": true,
      "site": "00b6b0ac",
      "value": [
        "LOAD",
        "8",
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
      "00bda554",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00bda560",
      "DATA",
      [
        "storage",
        "00c12798",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda584",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda554",
      "READ",
      [
        "storage",
        "00c9b640",
        null,
        "pointer"
      ]
    ],
    [
      "00bda560",
      "DATA",
      [
        "storage",
        "00c92140",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda584",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b088) · [`00b6b0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b0ac) · [`00b6b050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b050)
- 新版 `00bda588`（命令位置の公開資料なし） · `00bda5ac`（命令位置の公開資料なし） · `00bda550`（命令位置の公開資料なし）

~~~diff
- 00b6b088 ["INT_ADD", "register:40f0:8", ["const:b6b088:8", "const:4:8"]]
- 00b6b088 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda588 ["INT_ADD", "register:40f0:8", ["const:bda588:8", "const:4:8"]]
+ 00bda588 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b088 bytes 3ecc0194
+ 00bda588 bytes 9e010294
- 00b6b0ac ["INT_ADD", "register:40f0:8", ["const:b6b0ac:8", "const:4:8"]]
- 00b6b0ac ["CALL", null, ["callee:005896b4:8"]]
+ 00bda5ac ["INT_ADD", "register:40f0:8", ["const:bda5ac:8", "const:4:8"]]
+ 00bda5ac ["CALL", null, ["callee:005896b4:8"]]
- 00b6b0ac bytes dcede797
+ 00bda5ac bytes 42bce697
- 00b6b050 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bda550 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b6b050 bytes 88050090
+ 00bda550 bytes 080600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4b3379c24a273489316fccb2c3a652"></a>

### [`00b6b0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md) → [`00bda5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda5d8.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bda5f0",
      "incomplete_value": true,
      "site": "00bda5f4",
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
      "definition_site": "00b6b0f0",
      "incomplete_value": true,
      "site": "00b6b0f4",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda608",
      "incomplete_value": false,
      "site": "00bda60c",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b108",
      "incomplete_value": false,
      "site": "00b6b10c",
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
            "const:ed7:8"
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
      "definition_site": "00bda620",
      "incomplete_value": true,
      "site": "00bda62c",
      "value": [
        "LOAD",
        "8",
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b120",
      "incomplete_value": true,
      "site": "00b6b12c",
      "value": [
        "LOAD",
        "8",
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
                "const:9c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda5e8",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00bda5f4",
      "DATA",
      [
        "storage",
        "00c12798",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda608",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda5e8",
      "READ",
      [
        "storage",
        "00c9b640",
        null,
        "pointer"
      ]
    ],
    [
      "00bda5f4",
      "DATA",
      [
        "storage",
        "00c92140",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda608",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b10c) · [`00b6b12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b12c) · [`00b6b0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b0e4)
- 新版 `00bda60c`（命令位置の公開資料なし） · `00bda62c`（命令位置の公開資料なし） · `00bda5e4`（命令位置の公開資料なし）

~~~diff
- 00b6b10c ["INT_ADD", "register:40f0:8", ["const:b6b10c:8", "const:4:8"]]
- 00b6b10c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda60c ["INT_ADD", "register:40f0:8", ["const:bda60c:8", "const:4:8"]]
+ 00bda60c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b10c bytes 1dcc0194
+ 00bda60c bytes 7d010294
- 00b6b12c ["INT_ADD", "register:40f0:8", ["const:b6b12c:8", "const:4:8"]]
- 00b6b12c ["CALL", null, ["callee:00574cac:8"]]
+ 00bda62c ["INT_ADD", "register:40f0:8", ["const:bda62c:8", "const:4:8"]]
+ 00bda62c ["CALL", null, ["callee:00574cac:8"]]
- 00b6b12c bytes 3a9be797
+ 00bda62c bytes a069e697
- 00b6b0e4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bda5e4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b6b0e4 bytes 88050090
+ 00bda5e4 bytes 080600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a8c36eb5b41a0d9e0f41888e5253310"></a>

### [`00b6b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md) → [`00bda670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda670.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda6dc",
      "incomplete_value": true,
      "site": "00bda6f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6b1dc",
      "incomplete_value": true,
      "site": "00b6b1f4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda6e8",
      "incomplete_value": true,
      "site": "00bda6f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6b1e8",
      "incomplete_value": true,
      "site": "00b6b1f4",
      "value": [
        "LOAD",
        "8",
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
                "const:880:8"
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
      "definition_site": "00bda70c",
      "incomplete_value": false,
      "site": "00bda714",
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
            "const:8dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b20c",
      "incomplete_value": false,
      "site": "00b6b214",
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
            "const:5b7:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda6dc",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00bda6e8",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00bda70c",
      "PARAM",
      [
        "storage",
        "002ad5b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda6dc",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bda6e8",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ],
    [
      "00bda70c",
      "PARAM",
      [
        "storage",
        "002be8dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b1f4) · [`00b6b214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b214) · [`00b6b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b238)
- 新版 `00bda6f4`（命令位置の公開資料なし） · `00bda714`（命令位置の公開資料なし） · `00bda738`（命令位置の公開資料なし）

~~~diff
- 00b6b1f4 ["INT_ADD", "register:40f0:8", ["const:b6b1f4:8", "const:4:8"]]
- 00b6b1f4 ["CALL", null, ["callee:005896b4:8"]]
+ 00bda6f4 ["INT_ADD", "register:40f0:8", ["const:bda6f4:8", "const:4:8"]]
+ 00bda6f4 ["CALL", null, ["callee:005896b4:8"]]
- 00b6b1f4 bytes 8aede797
+ 00bda6f4 bytes f0bbe697
- 00b6b214 ["INT_ADD", "register:40f0:8", ["const:b6b214:8", "const:4:8"]]
- 00b6b214 ["CALL", null, ["callee:00c5b1c0:8"]]
+ 00bda714 ["INT_ADD", "register:40f0:8", ["const:bda714:8", "const:4:8"]]
+ 00bda714 ["CALL", null, ["callee:00c5b1c0:8"]]
- 00b6b214 bytes 4bcd0194
+ 00bda714 bytes ab020294
- 00b6b238 ["INT_ADD", "register:40f0:8", ["const:b6b238:8", "const:4:8"]]
- 00b6b238 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bda738 ["INT_ADD", "register:40f0:8", ["const:bda738:8", "const:4:8"]]
+ 00bda738 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b238 bytes d2cb0194
+ 00bda738 bytes 32010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75fb642cd9c4312d464283767de510d5"></a>

### [`00b6b690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md) → [`00bdab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdac08",
      "incomplete_value": true,
      "site": "00bdac20",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6b708",
      "incomplete_value": true,
      "site": "00b6b720",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdac0c",
      "incomplete_value": true,
      "site": "00bdac20",
      "value": [
        "LOAD",
        "8",
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b70c",
      "incomplete_value": true,
      "site": "00b6b720",
      "value": [
        "LOAD",
        "8",
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdac78",
      "incomplete_value": false,
      "site": "00bdac7c",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b778",
      "incomplete_value": false,
      "site": "00b6b77c",
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
            "const:ed7:8"
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
      "00bdabb8",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdabbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6b7dc"
      ]
    ],
    [
      "00bdac08",
      "READ",
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
      "00bdabb8",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdabbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdacdc"
      ]
    ],
    [
      "00bdac08",
      "READ",
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

- 旧版 [`00b6b720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b720) · [`00b6b77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b77c) · [`00b6b7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b7e4)
- 新版 `00bdac20`（命令位置の公開資料なし） · `00bdac7c`（命令位置の公開資料なし） · `00bdace4`（命令位置の公開資料なし）

~~~diff
- 00b6b720 ["INT_ADD", "register:40f0:8", ["const:b6b720:8", "const:4:8"]]
- 00b6b720 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bdac20 ["INT_ADD", "register:40f0:8", ["const:bdac20:8", "const:4:8"]]
+ 00bdac20 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6b720 bytes 88c90194
+ 00bdac20 bytes e0fe0194
- 00b6b77c ["INT_ADD", "register:40f0:8", ["const:b6b77c:8", "const:4:8"]]
- 00b6b77c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdac7c ["INT_ADD", "register:40f0:8", ["const:bdac7c:8", "const:4:8"]]
+ 00bdac7c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b77c bytes 81ca0194
+ 00bdac7c bytes e1ff0194
- 00b6b7e4 ["INT_ADD", "register:40f0:8", ["const:b6b7e4:8", "const:4:8"]]
- 00b6b7e4 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bdace4 ["INT_ADD", "register:40f0:8", ["const:bdace4:8", "const:4:8"]]
+ 00bdace4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b6b7e4 bytes 97c90194
+ 00bdace4 bytes effe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1528aeb6d6b48122fc5d71bcdb9527"></a>

### [`00b6b8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md) → [`00bdadac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdadac.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdadec",
      "incomplete_value": false,
      "site": "00bdadf0",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b8ec",
      "incomplete_value": false,
      "site": "00b6b8f0",
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
            "const:ed7:8"
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
      "definition_site": "00bdae58",
      "incomplete_value": true,
      "site": "00bdae5c",
      "value": [
        "LOAD",
        "8",
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
                "register:8:8"
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
    "old": null,
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdae64",
      "value": [
        "leaf",
        "ram:c5da00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6b964",
      "value": [
        "leaf",
        "ram:be0e00:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdadec",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00bdae64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0e00"
      ]
    ]
  ],
  "added": [
    [
      "00bdadec",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bdae64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5da00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b8f0) · [`00b6b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b95c) · [`00b6b964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b964)
- 新版 `00bdadf0`（命令位置の公開資料なし） · `00bdae5c`（命令位置の公開資料なし） · `00bdae64`（命令位置の公開資料なし）

~~~diff
- 00b6b8f0 ["INT_ADD", "register:40f0:8", ["const:b6b8f0:8", "const:4:8"]]
- 00b6b8f0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdadf0 ["INT_ADD", "register:40f0:8", ["const:bdadf0:8", "const:4:8"]]
+ 00bdadf0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6b8f0 bytes 24ca0194
+ 00bdadf0 bytes 84ff0194
- 00b6b95c ["INT_ADD", "register:40f0:8", ["const:b6b95c:8", "const:4:8"]]
- 00b6b95c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bdae5c ["INT_ADD", "register:40f0:8", ["const:bdae5c:8", "const:4:8"]]
+ 00bdae5c ["CALL", null, ["callee:00c57ab0:8"]]
- 00b6b95c bytes c1bd0194
+ 00bdae5c bytes 15f30194
- 00b6b964 ["INT_ADD", "register:40f0:8", ["const:b6b964:8", "const:4:8"]]
- 00b6b964 ["CALL", null, ["ram:be0e00:8"]]
+ 00bdae64 ["INT_ADD", "register:40f0:8", ["const:bdae64:8", "const:4:8"]]
+ 00bdae64 ["CALL", null, ["ram:c5da00:8"]]
- 00b6b964 bytes 27d50194
+ 00bdae64 bytes e70a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1fe0ef368512c8b8b1dc6e2dc35df67"></a>

### [`00b6ba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md) → [`00bdaf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaf48.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 57.89% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ba4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ba4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ba50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ba4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ba50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ba54",
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
      "00bdaf4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bdaf50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bdaf54",
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

- 旧版 [`00b6ba4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6ba4c) · [`00b6ba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6ba50) · [`00b6ba54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6ba54)

~~~diff
- 00b6ba4c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6ba4c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6ba4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b6ba4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ba4c bytes f85f03a9
- 00b6ba50 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6ba50 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6ba50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b6ba50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ba50 bytes f65704a9
- 00b6ba54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6ba54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6ba54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b6ba54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ba54 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c174a18c03a5867664e6a2e5ec5f0fe1"></a>

### [`00b6bdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bdb0.md) → [`00bdb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb2b0.md) _ZN8firebase4auth22FederatedOAuthProviderD1Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 72.22% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bdd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdb2d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb2c8",
      "incomplete_value": true,
      "site": "00bdb2d8",
      "value": [
        "LOAD",
        "8",
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
                "register:4000:8"
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
      "00bdb2c4",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6bdd4",
      "DATA",
      [
        "storage",
        "00c127d8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00bdb2c4",
      "READ",
      [
        "storage",
        "00c9b648",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb2d4",
      "DATA",
      [
        "storage",
        "00c92180",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bdb0.md#insn-00b6bdd4) · [`00b6bdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bdb0.md#insn-00b6bdd8)
- 新版 `00bdb2d8`（命令位置の公開資料なし） · `00bdb2d4`（命令位置の公開資料なし）

~~~diff
- 00b6bdd4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b6bdd4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b6bdd4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00b6bdd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6bdd4 bytes 088403f8
- 00b6bdd8 ["INT_ADD", "register:40f0:8", ["const:b6bdd8:8", "const:4:8"]]
- 00b6bdd8 ["CALL", null, ["callee:0046d450:8"]]
+ 00bdb2d8 ["INT_ADD", "register:40f0:8", ["const:bdb2d8:8", "const:4:8"]]
+ 00bdb2d8 ["CALL", null, ["callee:0046d450:8"]]
- 00b6bdd8 bytes f879e397
+ 00bdb2d8 bytes 5e48e297
+ 00bdb2d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bdb2d4 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bdb2d4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
+ 00bdb2d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bdb2d4 bytes 088403f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-690533f65f54a792a91c8a36ce6cc1d3"></a>

### [`00b6be5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6be5c.md) → [`00bdb35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb35c.md) _ZN8firebase4auth22FederatedOAuthProviderD0Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 60.00% / 新版 70.59%

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
      "site": "00b6be5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6be5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6be60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6be64",
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
      "00bdb35c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bdb360",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdb364",
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

- 旧版 [`00b6be5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6be5c.md#insn-00b6be5c) · [`00b6be60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6be5c.md#insn-00b6be60) · [`00b6be64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6be5c.md#insn-00b6be64)

~~~diff
- 00b6be5c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6be5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6be5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6be5c bytes f50f1df8
- 00b6be60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6be60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6be60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6be60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6be60 bytes f44f01a9
- 00b6be64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6be64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6be64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6be64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6be64 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdbb3100a7cef6c2664e2b441080c890"></a>

### [`00b6bf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md) → [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) _ZN8firebase4auth22FederatedOAuthProvider6SignInEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00b6c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md) [`00b6d254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 36.36% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bf80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bf80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bf84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bf80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6bf84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6bfa0",
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
      "00bdb480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdb484",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdb4a0",
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

- 旧版 [`00b6bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md#insn-00b6bf80) · [`00b6bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md#insn-00b6bf84) · [`00b6bfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md#insn-00b6bfa0)

~~~diff
- 00b6bf80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6bf80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6bf80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 00b6bf80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6bf80 bytes f44f1ba9
- 00b6bf84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6bf84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6bf84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 00b6bf84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6bf84 bytes fd7b1ca9
- 00b6bfa0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b6bfa0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b6bfa0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6bfa0 bytes a9031af8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27dcfe9314b47d7806cf41ededd6789d"></a>

### [`00b6c244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md) → [`00bdb744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0de0.md) · 呼出先 7件 [`00b603b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9e0.md) · 呼出先 7件 [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb790",
      "incomplete_value": true,
      "site": "00bdb7a4",
      "value": [
        "LOAD",
        "8",
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
                "const:c9b000:8"
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
      "definition_site": "00b6c290",
      "incomplete_value": true,
      "site": "00b6c2a4",
      "value": [
        "LOAD",
        "8",
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
                "const:c1b000:8"
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
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdb7b8",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6c2b8",
      "value": [
        "leaf",
        "ram:bddc40:8"
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
      "00bdb790",
      "READ",
      [
        "storage",
        "00c1bbb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb790",
      "PARAM",
      [
        "storage",
        "00b603b0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "00bdb7b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bdb790",
      "READ",
      [
        "storage",
        "00c9b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb790",
      "PARAM",
      [
        "storage",
        "00bcf8b0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "00bdb7b8",
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

- 旧版 [`00b6c2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md#insn-00b6c2a4) · [`00b6c2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md#insn-00b6c2b8) · [`00b6c27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md#insn-00b6c27c)
- 新版 `00bdb7a4`（命令位置の公開資料なし） · `00bdb7b8`（命令位置の公開資料なし） · `00bdb77c`（命令位置の公開資料なし）

~~~diff
- 00b6c2a4 ["INT_ADD", "register:40f0:8", ["const:b6c2a4:8", "const:4:8"]]
- 00b6c2a4 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bdb7a4 ["INT_ADD", "register:40f0:8", ["const:bdb7a4:8", "const:4:8"]]
+ 00bdb7a4 ["CALL", null, ["callee:00c5aa40:8"]]
- 00b6c2a4 bytes 47c70194
+ 00bdb7a4 bytes a7fc0194
- 00b6c2b8 ["INT_ADD", "register:40f0:8", ["const:b6c2b8:8", "const:4:8"]]
- 00b6c2b8 ["CALL", null, ["ram:bddc40:8"]]
+ 00bdb7b8 ["INT_ADD", "register:40f0:8", ["const:bdb7b8:8", "const:4:8"]]
+ 00bdb7b8 ["CALL", null, ["ram:c5a690:8"]]
- 00b6c2b8 bytes 62c60194
+ 00bdb7b8 bytes b6fb0194
- 00b6c27c ["INT_ADD", "register:40f0:8", ["const:b6c27c:8", "const:4:8"]]
- 00b6c27c ["CALL", null, ["callee:00c57a90:8"]]
+ 00bdb77c ["INT_ADD", "register:40f0:8", ["const:bdb77c:8", "const:4:8"]]
+ 00bdb77c ["CALL", null, ["callee:00c57a90:8"]]
- 00b6c27c bytes 71bb0194
+ 00bdb77c bytes c5f00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e434fb5c13f6c967594d7e4a3b5c83e0"></a>

### [`00b6c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md) → [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) FUN_00bdb810

採用 · 移動量 `+0x6f500` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b6bf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md) [`00b6c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md) [`00b6c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde130.md)
- 新版 呼出元 3件 [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) [`00bdba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdba50.md) [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5abb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 46.15% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb86c",
      "incomplete_value": true,
      "site": "00bdb884",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6c36c",
      "incomplete_value": true,
      "site": "00b6c384",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb870",
      "incomplete_value": true,
      "site": "00bdb884",
      "value": [
        "LOAD",
        "8",
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c370",
      "incomplete_value": true,
      "site": "00b6c384",
      "value": [
        "LOAD",
        "8",
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
                "const:838:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb8e4",
      "incomplete_value": true,
      "site": "00bdb8f4",
      "value": [
        "LOAD",
        "8",
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
                "const:818:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c3e4",
      "incomplete_value": true,
      "site": "00b6c3f4",
      "value": [
        "LOAD",
        "8",
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdb86c",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdb870",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdb8e4",
      "READ",
      [
        "storage",
        "010a1910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdb86c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdb870",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdb8e4",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c384) · [`00b6c3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c3f4) · [`00b6c40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c40c)
- 新版 `00bdb884`（命令位置の公開資料なし） · `00bdb8f4`（命令位置の公開資料なし）

~~~diff
- 00b6c384 ["INT_ADD", "register:40f0:8", ["const:b6c384:8", "const:4:8"]]
- 00b6c384 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bdb884 ["INT_ADD", "register:40f0:8", ["const:bdb884:8", "const:4:8"]]
+ 00bdb884 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00b6c384 bytes 6fc60194
+ 00bdb884 bytes c7fb0194
- 00b6c3f4 ["INT_ADD", "register:40f0:8", ["const:b6c3f4:8", "const:4:8"]]
- 00b6c3f4 ["CALL", null, ["callee:004977f4:8"]]
+ 00bdb8f4 ["INT_ADD", "register:40f0:8", ["const:bdb8f4:8", "const:4:8"]]
+ 00bdb8f4 ["CALL", null, ["callee:004977f4:8"]]
- 00b6c3f4 bytes 5a21e497
+ 00bdb8f4 bytes c0efe297
- 00b6c40c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6c40c ["INT_ADD", "register:40f0:8", ["const:b6c40c:8", "const:4:8"]]
- 00b6c40c ["CALLIND", null, ["register:0:8"]]
- 00b6c40c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3dca75991a7b585a38bc6c8bc953f80"></a>

### [`00b6c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md) → [`00bdba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdba50.md) _ZN8firebase4auth22FederatedOAuthProvider4LinkEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00b6c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md) [`00b6d254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdbbe8",
      "incomplete_value": true,
      "site": "00bdbbe8",
      "value": [
        "LOAD",
        "8",
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
                "const:c9b000:8"
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
      "definition_site": "00b6c6e8",
      "incomplete_value": true,
      "site": "00b6c6e8",
      "value": [
        "LOAD",
        "8",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdbaf8",
      "value": [
        "leaf",
        "ram:c5d760:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6c5f8",
      "value": [
        "leaf",
        "ram:be0b60:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdbb18",
      "value": [
        "leaf",
        "ram:c5a650:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6c618",
      "value": [
        "leaf",
        "ram:bddbe0:8"
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
      "00bdbaf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0b60"
      ]
    ],
    [
      "00bdbb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddbe0"
      ]
    ],
    [
      "00bdbb20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0e00"
      ]
    ]
  ],
  "added": [
    [
      "00bdbaf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5d760"
      ]
    ],
    [
      "00bdbb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a650"
      ]
    ],
    [
      "00bdbb20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5da00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md#insn-00b6c5f8) · [`00b6c618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md#insn-00b6c618) · [`00b6c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md#insn-00b6c620)
- 新版 `00bdbaf8`（命令位置の公開資料なし） · `00bdbb18`（命令位置の公開資料なし） · `00bdbb20`（命令位置の公開資料なし）

~~~diff
- 00b6c5f8 ["INT_ADD", "register:40f0:8", ["const:b6c5f8:8", "const:4:8"]]
- 00b6c5f8 ["CALL", null, ["ram:be0b60:8"]]
+ 00bdbaf8 ["INT_ADD", "register:40f0:8", ["const:bdbaf8:8", "const:4:8"]]
+ 00bdbaf8 ["CALL", null, ["ram:c5d760:8"]]
- 00b6c5f8 bytes 5ad10194
+ 00bdbaf8 bytes 1a070294
- 00b6c618 ["INT_ADD", "register:40f0:8", ["const:b6c618:8", "const:4:8"]]
- 00b6c618 ["CALL", null, ["ram:bddbe0:8"]]
+ 00bdbb18 ["INT_ADD", "register:40f0:8", ["const:bdbb18:8", "const:4:8"]]
+ 00bdbb18 ["CALL", null, ["ram:c5a650:8"]]
- 00b6c618 bytes 72c50194
+ 00bdbb18 bytes cefa0194
- 00b6c620 ["INT_ADD", "register:40f0:8", ["const:b6c620:8", "const:4:8"]]
- 00b6c620 ["CALL", null, ["ram:be0e00:8"]]
+ 00bdbb20 ["INT_ADD", "register:40f0:8", ["const:bdbb20:8", "const:4:8"]]
+ 00bdbb20 ["CALL", null, ["ram:c5da00:8"]]
- 00b6c620 bytes f8d10194
+ 00bdbb20 bytes b8070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15d02027f6bfd8e0494686061424522c"></a>

### [`00b6c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md) → [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) _ZN8firebase4auth22FederatedOAuthProvider14ReauthenticateEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00b6c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md) [`00b6d254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdbec0",
      "incomplete_value": true,
      "site": "00bdbec0",
      "value": [
        "LOAD",
        "8",
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
                "const:c9b000:8"
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
      "definition_site": "00b6c9c0",
      "incomplete_value": true,
      "site": "00b6c9c0",
      "value": [
        "LOAD",
        "8",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdbdd0",
      "value": [
        "leaf",
        "ram:c5d760:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6c8d0",
      "value": [
        "leaf",
        "ram:be0b60:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdbdf0",
      "value": [
        "leaf",
        "ram:c5a650:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6c8f0",
      "value": [
        "leaf",
        "ram:bddbe0:8"
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
      "00bdbdd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0b60"
      ]
    ],
    [
      "00bdbdf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddbe0"
      ]
    ],
    [
      "00bdbdf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0e00"
      ]
    ]
  ],
  "added": [
    [
      "00bdbdd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5d760"
      ]
    ],
    [
      "00bdbdf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a650"
      ]
    ],
    [
      "00bdbdf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5da00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md#insn-00b6c8d0) · [`00b6c8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md#insn-00b6c8f0) · [`00b6c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md#insn-00b6c8f8)
- 新版 `00bdbdd0`（命令位置の公開資料なし） · `00bdbdf0`（命令位置の公開資料なし） · `00bdbdf8`（命令位置の公開資料なし）

~~~diff
- 00b6c8d0 ["INT_ADD", "register:40f0:8", ["const:b6c8d0:8", "const:4:8"]]
- 00b6c8d0 ["CALL", null, ["ram:be0b60:8"]]
+ 00bdbdd0 ["INT_ADD", "register:40f0:8", ["const:bdbdd0:8", "const:4:8"]]
+ 00bdbdd0 ["CALL", null, ["ram:c5d760:8"]]
- 00b6c8d0 bytes a4d00194
+ 00bdbdd0 bytes 64060294
- 00b6c8f0 ["INT_ADD", "register:40f0:8", ["const:b6c8f0:8", "const:4:8"]]
- 00b6c8f0 ["CALL", null, ["ram:bddbe0:8"]]
+ 00bdbdf0 ["INT_ADD", "register:40f0:8", ["const:bdbdf0:8", "const:4:8"]]
+ 00bdbdf0 ["CALL", null, ["ram:c5a650:8"]]
- 00b6c8f0 bytes bcc40194
+ 00bdbdf0 bytes 18fa0194
- 00b6c8f8 ["INT_ADD", "register:40f0:8", ["const:b6c8f8:8", "const:4:8"]]
- 00b6c8f8 ["CALL", null, ["ram:be0e00:8"]]
+ 00bdbdf8 ["INT_ADD", "register:40f0:8", ["const:bdbdf8:8", "const:4:8"]]
+ 00bdbdf8 ["CALL", null, ["ram:c5da00:8"]]
- 00b6c8f8 bytes 42d10194
+ 00bdbdf8 bytes 02070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb043a99403adee088f0047c8930a7da"></a>

### [`00b6cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb00.md) → [`00bdc000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc000.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b6aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e00.md)
- 新版 呼出元 1件 [`00bd9fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5da00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bdc014",
      "value": [
        "leaf",
        "ram:c5da00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6cb14",
      "value": [
        "leaf",
        "ram:be0e00:8"
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
      "00bdc014",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0e00"
      ]
    ]
  ],
  "added": [
    [
      "00bdc014",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5da00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb00.md#insn-00b6cb14)
- 新版 `00bdc014`（命令位置の公開資料なし）

~~~diff
- 00b6cb14 ["INT_ADD", "register:40f0:8", ["const:b6cb14:8", "const:4:8"]]
- 00b6cb14 ["CALL", null, ["ram:be0e00:8"]]
+ 00bdc014 ["INT_ADD", "register:40f0:8", ["const:bdc014:8", "const:4:8"]]
+ 00bdc014 ["CALL", null, ["ram:c5da00:8"]]
- 00b6cb14 bytes bbd00194
+ 00bdc014 bytes 7b060294
~~~


<a id="compare-60a483bd8bb40164fe2cfdb2033c1482"></a>

### [`00b6cb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md) → [`00bdc02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc02c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0dd0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc090",
      "incomplete_value": false,
      "site": "00bdc094",
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
    "old": {
      "definition_site": "00b6cb90",
      "incomplete_value": false,
      "site": "00b6cb94",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cc30"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bdc130"
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
      "00bdc090",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdc090",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md#insn-00b6cb94) · [`00b6cc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md#insn-00b6cc30)
- 新版 `00bdc094`（命令位置の公開資料なし） · `00bdc130`（命令位置の公開資料なし）

~~~diff
- 00b6cb94 ["INT_ADD", "register:40f0:8", ["const:b6cb94:8", "const:4:8"]]
- 00b6cb94 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdc094 ["INT_ADD", "register:40f0:8", ["const:bdc094:8", "const:4:8"]]
+ 00bdc094 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6cb94 bytes 7bc50194
+ 00bdc094 bytes dbfa0194
- 00b6cc30 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6cc30 ["RETURN", null, ["register:0:8"]]
- 00b6cc30 bytes c0035fd6
+ 00bdc130 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bdc130 ["RETURN", null, ["register:0:8"]]
+ 00bdc130 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d02a1bf17afa2fb76e6abae5ed2c39e"></a>

### [`00b6cf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cf14.md) → [`00bdc414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc414.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e70.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00be0e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e60.md)
- 新版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da70.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5da60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 17.65% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 6件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdc46c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cf54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4cc"
      ]
    ],
    [
      "unmatched:00b6cfa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4b4"
      ]
    ],
    [
      "unmatched:00b6cfd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4f8"
      ]
    ]
  ],
  "added": [
    [
      "00bdc454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4cc"
      ]
    ],
    [
      "00bdc4a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4b4"
      ]
    ],
    [
      "00bdc4d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc4f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cf14.md#insn-00b6cf54) · [`00b6cf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cf14.md#insn-00b6cf6c) · [`00b6cf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cf14.md#insn-00b6cf78)
- 新版 `00bdc478`（命令位置の公開資料なし）

~~~diff
- 00b6cf54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b6cf54 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b6cf54 bytes d30300b5
- 00b6cf6c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6cf6c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6cf6c ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:20:8"]]
- 00b6cf6c ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:1:4"]]
- 00b6cf6c bytes ff0e02b8
- 00b6cf78 ["INT_ADD", "register:40f0:8", ["const:b6cf78:8", "const:4:8"]]
- 00b6cf78 ["CALL", null, ["callee:00c5a4f0:8"]]
+ 00bdc478 ["INT_ADD", "register:40f0:8", ["const:bdc478:8", "const:4:8"]]
+ 00bdc478 ["CALL", null, ["callee:00c5a4f0:8"]]
- 00b6cf78 bytes cac20194
+ 00bdc478 bytes 1ef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7addb212dffc541055124f732a484bf4"></a>

### [`00b6d028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d028.md) → [`00bdc528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc528.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e60.md) · 呼出先 1件 [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md)
- 新版 呼出元 1件 [`00c5da60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da60.md) · 呼出先 1件 [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.06% / 新版 69.06%

CFGの説明率　旧版 31.65% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d080"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d0b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc5f0"
      ]
    ],
    [
      "unmatched:00b6d0b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc674"
      ]
    ],
    [
      "unmatched:00b6d110",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6d118"
      ]
    ]
  ],
  "added": [
    [
      "00bdc580",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc5f0"
      ]
    ],
    [
      "00bdc5b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc674"
      ]
    ],
    [
      "00bdc610",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc618"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d028.md#insn-00b6d080) · [`00b6d0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d028.md#insn-00b6d0a4) · [`00b6d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d028.md#insn-00b6d0b4)
- 新版 `00bdc5a4`（命令位置の公開資料なし）

~~~diff
- 00b6d080 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b6d080 bytes 80030054
- 00b6d0a4 ["INT_ADD", "register:40f0:8", ["const:b6d0a4:8", "const:4:8"]]
- 00b6d0a4 ["CALL", null, ["callee:00c5b1a0:8"]]
+ 00bdc5a4 ["INT_ADD", "register:40f0:8", ["const:bdc5a4:8", "const:4:8"]]
+ 00bdc5a4 ["CALL", null, ["callee:00c5b1a0:8"]]
- 00b6d0a4 bytes 9fc50194
+ 00bdc5a4 bytes fffa0194
- 00b6d0b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d0b4 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00b6d0b4 bytes 080600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f469c565ac624690aac202010500e465"></a>

### [`00b6d254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md) → [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b6bf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md) [`00b6c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md) [`00b6c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d20.md)
- 新版 呼出元 3件 [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) [`00bdba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdba50.md) [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d920.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdc784"
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
      "unmatched:00b6d284",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d288",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d2dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bdc784",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bdc788",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "00bdc7dc",
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

- 旧版 [`00b6d284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md#insn-00b6d284) · [`00b6d288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md#insn-00b6d288) · [`00b6d28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d254.md#insn-00b6d28c)
- 新版 `00bdc78c`（命令位置の公開資料なし）

~~~diff
- 00b6d284 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b6d284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6d284 bytes e81f00f9
- 00b6d288 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d288 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d288 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:34:8"]]
- 00b6d288 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d288 bytes ffd30039
- 00b6d28c ["INT_ADD", "register:40f0:8", ["const:b6d28c:8", "const:4:8"]]
- 00b6d28c ["CALL", null, ["callee:00c5d920:8"]]
+ 00bdc78c ["INT_ADD", "register:40f0:8", ["const:bdc78c:8", "const:4:8"]]
+ 00bdc78c ["CALL", null, ["callee:00c5d920:8"]]
- 00b6d28c bytes a5ce0194
+ 00bdc78c bytes 65040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5746de8a277a7118920452d4e0de32ad"></a>

### [`00b6d330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md) → [`00bdc830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc830.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0dc0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9c0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 50.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc89c",
      "incomplete_value": false,
      "site": "00bdc8a0",
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
    "old": {
      "definition_site": "00b6d39c",
      "incomplete_value": false,
      "site": "00b6d3a0",
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
            "const:467:8"
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
    "new": null,
    "old": {
      "definition_site": "00b6d3d4",
      "incomplete_value": true,
      "site": "00b6d3dc",
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
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6d3d8",
      "incomplete_value": true,
      "site": "00b6d3dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdc89c",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdc89c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d3a0) · [`00b6d3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d3dc) · [`00b6d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d3e8)
- 新版 `00bdc8a0`（命令位置の公開資料なし） · `00bdc8dc`（命令位置の公開資料なし） · `00bdc8e8`（命令位置の公開資料なし）

~~~diff
- 00b6d3a0 ["INT_ADD", "register:40f0:8", ["const:b6d3a0:8", "const:4:8"]]
- 00b6d3a0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdc8a0 ["INT_ADD", "register:40f0:8", ["const:bdc8a0:8", "const:4:8"]]
+ 00bdc8a0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6d3a0 bytes 78c30194
+ 00bdc8a0 bytes d8f80194
- 00b6d3dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d3dc ["INT_ADD", "register:40f0:8", ["const:b6d3dc:8", "const:4:8"]]
- 00b6d3dc ["CALLIND", null, ["register:0:8"]]
+ 00bdc8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdc8dc ["INT_ADD", "register:40f0:8", ["const:bdc8dc:8", "const:4:8"]]
+ 00bdc8dc ["CALLIND", null, ["register:0:8"]]
- 00b6d3dc bytes 00013fd6
+ 00bdc8dc bytes 00013fd6
- 00b6d3e8 ["INT_ADD", "register:40f0:8", ["const:b6d3e8:8", "const:4:8"]]
- 00b6d3e8 ["CALL", null, ["callee:00c5aa60:8"]]
+ 00bdc8e8 ["INT_ADD", "register:40f0:8", ["const:bdc8e8:8", "const:4:8"]]
+ 00bdc8e8 ["CALL", null, ["callee:00c5aa60:8"]]
- 00b6d3e8 bytes fec20194
+ 00bdc8e8 bytes 5ef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6b9e9cc963ed44d690f6e9c6a10d8f"></a>

### [`00b6d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md) → [`00bdc9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc9f0.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdca1c",
      "incomplete_value": true,
      "site": "00bdca1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d51c",
      "incomplete_value": true,
      "site": "00b6d51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "definition_site": "00bdca04",
      "incomplete_value": true,
      "site": "00bdca04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d504",
      "incomplete_value": true,
      "site": "00b6d504",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdca10",
      "incomplete_value": false,
      "site": "00bdca14",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d510",
      "incomplete_value": false,
      "site": "00b6d514",
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
            "const:2ed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdca00",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdca10",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "00bdca1c",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdca00",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdca10",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdca1c",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d514) · [`00b6d51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d51c) · [`00b6d4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d4fc)
- 新版 `00bdca14`（命令位置の公開資料なし） · `00bdca1c`（命令位置の公開資料なし） · `00bdc9fc`（命令位置の公開資料なし）

~~~diff
- 00b6d514 ["INT_ADD", "register:40f0:8", ["const:b6d514:8", "const:4:8"]]
- 00b6d514 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdca14 ["INT_ADD", "register:40f0:8", ["const:bdca14:8", "const:4:8"]]
+ 00bdca14 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d514 bytes dfc20194
+ 00bdca14 bytes 3ff80194
- 00b6d51c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6d51c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdca1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
+ 00bdca1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d51c bytes 60fe04f9
+ 00bdca1c bytes 608204f9
- 00b6d4fc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdc9fc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6d4fc bytes b3290090
+ 00bdc9fc bytes 532a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96da3d04d899a9b0803e280b1c24300"></a>

### [`00b6d530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md) → [`00bdca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca30.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00b6d530"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d534"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d534"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d530",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d534",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdca40",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdca30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdca34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdca40",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d530) · [`00b6d534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d534) · [`00b6d544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d544)
- 新版 `00bdca44`（命令位置の公開資料なし）

~~~diff
- 00b6d530 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6d530 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d530 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d530 bytes f30f1ef8
- 00b6d534 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d534 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d534 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d534 bytes fd7b01a9
- 00b6d544 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d544 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bdca44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdca44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6d544 bytes e80000b5
+ 00bdca44 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c341b1c0af17337dd6a542ff706c824"></a>

### [`00b6d570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md) → [`00bdca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca70.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00b6d5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcaa0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdca84",
      "incomplete_value": true,
      "site": "00bdca84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bdca80",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d590",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6d598",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bdca80",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdca90",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdca98",
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

- 旧版 [`00b6d584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d584) · [`00b6d598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d598) · [`00b6d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d5a0)
- 新版 `00bdca84`（命令位置の公開資料なし）

~~~diff
- 00b6d584 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d584 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bdca84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdca84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6d584 bytes 080100b5
+ 00bdca84 bytes 080100b5
- 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
- 00b6d598 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d598 bytes bec20194
- 00b6d5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6d5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d5a0 bytes 60fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1435fa2877552ab445488efd2041120d"></a>

### [`00b6d5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md) → [`00bdcab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b6d5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcae4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdcac8",
      "incomplete_value": true,
      "site": "00bdcac8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d5c8",
      "incomplete_value": true,
      "site": "00b6d5c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bdcac4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d5d0",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6d5e4",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcac4",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcad0",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdcae4",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5c8) · [`00b6d5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5dc) · [`00b6d5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5e4)
- 新版 `00bdcac8`（命令位置の公開資料なし） · `00bdcadc`（命令位置の公開資料なし）

~~~diff
- 00b6d5c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d5c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bdcac8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdcac8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d5c8 bytes 080100b5
+ 00bdcac8 bytes 080100b5
- 00b6d5dc ["INT_ADD", "register:40f0:8", ["const:b6d5dc:8", "const:4:8"]]
- 00b6d5dc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcadc ["INT_ADD", "register:40f0:8", ["const:bdcadc:8", "const:4:8"]]
+ 00bdcadc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d5dc bytes adc20194
+ 00bdcadc bytes 0df80194
- 00b6d5e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6d5e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d5e4 bytes 60fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6069b614420d0a3bf66bf0c5759a4d2e"></a>

### [`00b6d604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md) → [`00bdcb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bdcb5c",
      "incomplete_value": true,
      "site": "00bdcb5c",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d65c",
      "incomplete_value": true,
      "site": "00b6d65c",
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
            "const:a00:8"
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
      "definition_site": "00bdcb38",
      "incomplete_value": true,
      "site": "00bdcb44",
      "value": [
        "LOAD",
        "8",
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d638",
      "incomplete_value": true,
      "site": "00b6d644",
      "value": [
        "LOAD",
        "8",
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
                "const:9f8:8"
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
      "00bdcb18",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcb38",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcb5c",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdcb18",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcb38",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcb5c",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d644) · [`00b6d65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d65c) · [`00b6d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d614)
- 新版 `00bdcb44`（命令位置の公開資料なし） · `00bdcb5c`（命令位置の公開資料なし） · `00bdcb14`（命令位置の公開資料なし）

~~~diff
- 00b6d644 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d644 ["INT_ADD", "register:40f0:8", ["const:b6d644:8", "const:4:8"]]
- 00b6d644 ["CALLIND", null, ["register:0:8"]]
+ 00bdcb44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdcb44 ["INT_ADD", "register:40f0:8", ["const:bdcb44:8", "const:4:8"]]
+ 00bdcb44 ["CALLIND", null, ["register:0:8"]]
- 00b6d644 bytes 00013fd6
+ 00bdcb44 bytes 00013fd6
- 00b6d65c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d65c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a00:8"]]
- 00b6d65c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdcb5c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdcb5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:908:8"]]
+ 00bdcb5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d65c bytes a0022839
+ 00bdcb5c bytes a0222439
- 00b6d614 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bdcb14 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b6d614 bytes b5290090
+ 00bdcb14 bytes 552a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3ae91439776a5d33fc07349221ea23"></a>

### [`00b6d670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md) → [`00bdcb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb70.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdcbac",
      "incomplete_value": true,
      "site": "00bdcbac",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6ac",
      "incomplete_value": true,
      "site": "00b6d6ac",
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
            "const:a00:8"
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
      "definition_site": "00bdcbcc",
      "incomplete_value": true,
      "site": "00bdcbcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6cc",
      "incomplete_value": true,
      "site": "00b6d6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "definition_site": "00bdcb88",
      "incomplete_value": true,
      "site": "00bdcb88",
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
      "definition_site": "00b6d688",
      "incomplete_value": true,
      "site": "00b6d688",
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
      "00bdcb84",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcb90",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcbac",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdcb84",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcb90",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcbac",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d6ac) · [`00b6d6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d6c8) · [`00b6d6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d6cc)
- 新版 `00bdcbac`（命令位置の公開資料なし） · `00bdcbc8`（命令位置の公開資料なし） · `00bdcbcc`（命令位置の公開資料なし）

~~~diff
- 00b6d6ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d6ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d6ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a00:8"]]
- 00b6d6ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdcbac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdcbac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdcbac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:908:8"]]
+ 00bdcbac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d6ac bytes bf022839
+ 00bdcbac bytes bf222439
- 00b6d6c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d6c8 ["INT_ADD", "register:40f0:8", ["const:b6d6c8:8", "const:4:8"]]
- 00b6d6c8 ["CALLIND", null, ["register:0:8"]]
+ 00bdcbc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdcbc8 ["INT_ADD", "register:40f0:8", ["const:bdcbc8:8", "const:4:8"]]
+ 00bdcbc8 ["CALLIND", null, ["register:0:8"]]
- 00b6d6c8 bytes 00013fd6
+ 00bdcbc8 bytes 00013fd6
- 00b6d6cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6d6cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6d6cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdcbcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
+ 00bdcbcc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdcbcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6d6cc bytes 9ffe04f9
+ 00bdcbcc bytes 9f8204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca373a9a8c98565f8f61f292dd02a5a"></a>

### [`00b6d6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md) → [`00bdcbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcbe0.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b6d720"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcc20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d6fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d6f4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d6fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcc24"
      ]
    ],
    [
      "unmatched:00b6d704",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdcbf4",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcc24"
      ]
    ],
    [
      "00bdcc04",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d6fc) · [`00b6d718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d718) · [`00b6d720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d720)
- 新版 `00bdcc18`（命令位置の公開資料なし）

~~~diff
- 00b6d6fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d6fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6d6fc bytes 410100b5
- 00b6d718 ["INT_ADD", "register:40f0:8", ["const:b6d718:8", "const:4:8"]]
- 00b6d718 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcc18 ["INT_ADD", "register:40f0:8", ["const:bdcc18:8", "const:4:8"]]
+ 00bdcc18 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d718 bytes 5ec20194
+ 00bdcc18 bytes bef70194
- 00b6d720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6d720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d720 bytes 80fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd58888bf7e13fad205a2f015f319fcf"></a>

### [`00b6d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md) → [`00bdcc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc50.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdcc6c",
      "incomplete_value": false,
      "site": "00bdcc70",
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
      "definition_site": "00b6d76c",
      "incomplete_value": false,
      "site": "00b6d770",
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
      "definition_site": "00bdcc7c",
      "incomplete_value": true,
      "site": "00bdcc88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6d77c",
      "incomplete_value": true,
      "site": "00b6d788",
      "value": [
        "LOAD",
        "8",
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
      "00bdcc6c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bdcc7c",
      "DATA",
      [
        "storage",
        "010a1a08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcc6c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdcc7c",
      "DATA",
      [
        "storage",
        "01126910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d770) · [`00b6d768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d768) · [`00b6d76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d76c)
- 新版 `00bdcc70`（命令位置の公開資料なし） · `00bdcc68`（命令位置の公開資料なし） · `00bdcc6c`（命令位置の公開資料なし）

~~~diff
- 00b6d770 ["INT_ADD", "register:40f0:8", ["const:b6d770:8", "const:4:8"]]
- 00b6d770 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdcc70 ["INT_ADD", "register:40f0:8", ["const:bdcc70:8", "const:4:8"]]
+ 00bdcc70 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6d770 bytes 84c20194
+ 00bdcc70 bytes e4f70194
- 00b6d768 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bdcc68 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b6d768 bytes 40b9fff0
+ 00bdcc68 bytes 60b6ff90
- 00b6d76c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6d76c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d76c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d76c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdcc6c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bdcc6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdcc6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdcc6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6d76c bytes 001c1591
+ 00bdcc6c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab1656d668ddde444fe042159506dd8"></a>

### [`00b6d78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md) → [`00bdcc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc8c.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b6d7cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcccc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d7a0",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d7a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdccd0"
      ]
    ],
    [
      "unmatched:00b6d7b0",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdcca0",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdccd0"
      ]
    ],
    [
      "00bdccb0",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7a8) · [`00b6d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7c4) · [`00b6d7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7cc)
- 新版 `00bdccc4`（命令位置の公開資料なし）

~~~diff
- 00b6d7a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d7a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6d7a8 bytes 410100b5
- 00b6d7c4 ["INT_ADD", "register:40f0:8", ["const:b6d7c4:8", "const:4:8"]]
- 00b6d7c4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdccc4 ["INT_ADD", "register:40f0:8", ["const:bdccc4:8", "const:4:8"]]
+ 00bdccc4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d7c4 bytes 33c20194
+ 00bdccc4 bytes 93f70194
- 00b6d7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6d7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d7cc bytes 80fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0813f76a8b7ed3c69311e672fa80fc"></a>

### [`00b6d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md) → [`00bdccfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdccfc.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdcd18",
      "incomplete_value": false,
      "site": "00bdcd1c",
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
      "definition_site": "00b6d818",
      "incomplete_value": false,
      "site": "00b6d81c",
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
      "definition_site": "00bdcd28",
      "incomplete_value": true,
      "site": "00bdcd34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6d828",
      "incomplete_value": true,
      "site": "00b6d834",
      "value": [
        "LOAD",
        "8",
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
      "00bdcd18",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bdcd28",
      "DATA",
      [
        "storage",
        "010a1a10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdcd18",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdcd28",
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

- 旧版 [`00b6d81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d81c) · [`00b6d814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d814) · [`00b6d818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d818)
- 新版 `00bdcd1c`（命令位置の公開資料なし） · `00bdcd14`（命令位置の公開資料なし） · `00bdcd18`（命令位置の公開資料なし）

~~~diff
- 00b6d81c ["INT_ADD", "register:40f0:8", ["const:b6d81c:8", "const:4:8"]]
- 00b6d81c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdcd1c ["INT_ADD", "register:40f0:8", ["const:bdcd1c:8", "const:4:8"]]
+ 00bdcd1c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6d81c bytes 59c20194
+ 00bdcd1c bytes b9f70194
- 00b6d814 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bdcd14 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6d814 bytes 60b9ff90
+ 00bdcd14 bytes 60b6ffb0
- 00b6d818 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6d818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdcd18 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bdcd18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdcd18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdcd18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6d818 bytes 00c81791
+ 00bdcd18 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e70668dd92ad61acce4df5cfbf8ddf"></a>

### [`00b6d838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md) → [`00bdcd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd38.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00bdcd64",
      "incomplete_value": true,
      "site": "00bdcd64",
      "value": [
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
      "definition_site": "00b6d864",
      "incomplete_value": true,
      "site": "00b6d864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "definition_site": "00bdcd4c",
      "incomplete_value": true,
      "site": "00bdcd4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d84c",
      "incomplete_value": true,
      "site": "00b6d84c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdcd58",
      "incomplete_value": false,
      "site": "00bdcd5c",
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
      "definition_site": "00b6d858",
      "incomplete_value": false,
      "site": "00b6d85c",
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
      "00bdcd48",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcd58",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bdcd64",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcd48",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcd58",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdcd64",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d85c) · [`00b6d864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d864) · [`00b6d844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d844)
- 新版 `00bdcd5c`（命令位置の公開資料なし） · `00bdcd64`（命令位置の公開資料なし） · `00bdcd44`（命令位置の公開資料なし）

~~~diff
- 00b6d85c ["INT_ADD", "register:40f0:8", ["const:b6d85c:8", "const:4:8"]]
- 00b6d85c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcd5c ["INT_ADD", "register:40f0:8", ["const:bdcd5c:8", "const:4:8"]]
+ 00bdcd5c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d85c bytes 0dc20194
+ 00bdcd5c bytes 6df70194
- 00b6d864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
- 00b6d864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcd64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00bdcd64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d864 bytes 600e05f9
+ 00bdcd64 bytes 609204f9
- 00b6d844 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdcd44 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6d844 bytes b3290090
+ 00bdcd44 bytes 532a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab5f8b308cdc237cddc352d555e2639"></a>

### [`00b6d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md) → [`00bdcd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd78.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdcda4",
      "incomplete_value": true,
      "site": "00bdcda4",
      "value": [
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
      "definition_site": "00b6d8a4",
      "incomplete_value": true,
      "site": "00b6d8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "definition_site": "00bdcd8c",
      "incomplete_value": true,
      "site": "00bdcd8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d88c",
      "incomplete_value": true,
      "site": "00b6d88c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdcd94",
      "incomplete_value": false,
      "site": "00bdcd9c",
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
      "definition_site": "00b6d894",
      "incomplete_value": false,
      "site": "00b6d89c",
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
      "00bdcd88",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcd94",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bdcda4",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcd88",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcd94",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdcda4",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d89c) · [`00b6d8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d8a4) · [`00b6d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d884)
- 新版 `00bdcd9c`（命令位置の公開資料なし） · `00bdcda4`（命令位置の公開資料なし） · `00bdcd84`（命令位置の公開資料なし）

~~~diff
- 00b6d89c ["INT_ADD", "register:40f0:8", ["const:b6d89c:8", "const:4:8"]]
- 00b6d89c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcd9c ["INT_ADD", "register:40f0:8", ["const:bdcd9c:8", "const:4:8"]]
+ 00bdcd9c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d89c bytes fdc10194
+ 00bdcd9c bytes 5df70194
- 00b6d8a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
- 00b6d8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcda4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00bdcda4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d8a4 bytes 600e05f9
+ 00bdcda4 bytes 609204f9
- 00b6d884 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdcd84 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6d884 bytes b3290090
+ 00bdcd84 bytes 532a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae9f0b186388ae59246162c81c91f48"></a>

### [`00b6d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md) → [`00bdcdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdb8.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdcde8",
      "incomplete_value": true,
      "site": "00bdcde8",
      "value": [
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
      "definition_site": "00b6d8e8",
      "incomplete_value": true,
      "site": "00b6d8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "definition_site": "00bdcdcc",
      "incomplete_value": true,
      "site": "00bdcdcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d8cc",
      "incomplete_value": true,
      "site": "00b6d8cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdcdd8",
      "incomplete_value": false,
      "site": "00bdcde0",
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
      "definition_site": "00b6d8d8",
      "incomplete_value": false,
      "site": "00b6d8e0",
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
      "00bdcdc8",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcdd8",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bdcde8",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcdc8",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcdd8",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdcde8",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8e0) · [`00b6d8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8e8) · [`00b6d8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8c4)
- 新版 `00bdcde0`（命令位置の公開資料なし） · `00bdcde8`（命令位置の公開資料なし） · `00bdcdc4`（命令位置の公開資料なし）

~~~diff
- 00b6d8e0 ["INT_ADD", "register:40f0:8", ["const:b6d8e0:8", "const:4:8"]]
- 00b6d8e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcde0 ["INT_ADD", "register:40f0:8", ["const:bdcde0:8", "const:4:8"]]
+ 00bdcde0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d8e0 bytes ecc10194
+ 00bdcde0 bytes 4cf70194
- 00b6d8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
- 00b6d8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcde8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00bdcde8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d8e8 bytes 600e05f9
+ 00bdcde8 bytes 609204f9
- 00b6d8c4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdcdc4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6d8c4 bytes b3290090
+ 00bdcdc4 bytes 532a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f11e22642efb663067e1a1c6ef042dc3"></a>

### [`00b6d8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md) → [`00bdcdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdfc.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdce2c",
      "incomplete_value": true,
      "site": "00bdce2c",
      "value": [
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
      "definition_site": "00b6d92c",
      "incomplete_value": true,
      "site": "00b6d92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "definition_site": "00bdce10",
      "incomplete_value": true,
      "site": "00bdce10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d910",
      "incomplete_value": true,
      "site": "00b6d910",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdce18",
      "incomplete_value": false,
      "site": "00bdce24",
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
      "definition_site": "00b6d918",
      "incomplete_value": false,
      "site": "00b6d924",
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
      "00bdce0c",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce18",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00bdce2c",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdce0c",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce18",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdce2c",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d924) · [`00b6d92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d92c) · [`00b6d908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d908)
- 新版 `00bdce24`（命令位置の公開資料なし） · `00bdce2c`（命令位置の公開資料なし） · `00bdce08`（命令位置の公開資料なし）

~~~diff
- 00b6d924 ["INT_ADD", "register:40f0:8", ["const:b6d924:8", "const:4:8"]]
- 00b6d924 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdce24 ["INT_ADD", "register:40f0:8", ["const:bdce24:8", "const:4:8"]]
+ 00bdce24 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6d924 bytes dbc10194
+ 00bdce24 bytes 3bf70194
- 00b6d92c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
- 00b6d92c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdce2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00bdce2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d92c bytes 600e05f9
+ 00bdce2c bytes 609204f9
- 00b6d908 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdce08 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6d908 bytes b3290090
+ 00bdce08 bytes 532a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-572e26b801df3bcefdad55f2200ac99a"></a>

### [`00b6d94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md) → [`00bdce4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdce4c.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bdcea4",
      "incomplete_value": true,
      "site": "00bdcea4",
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
      "definition_site": "00b6d9a4",
      "incomplete_value": true,
      "site": "00b6d9a4",
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
            "const:a20:8"
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
      "definition_site": "00bdce80",
      "incomplete_value": true,
      "site": "00bdce8c",
      "value": [
        "LOAD",
        "8",
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d980",
      "incomplete_value": true,
      "site": "00b6d98c",
      "value": [
        "LOAD",
        "8",
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
                "const:a18:8"
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
      "00bdce60",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdce80",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcea4",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdce60",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdce80",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcea4",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d98c) · [`00b6d9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d9a4) · [`00b6d95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d95c)
- 新版 `00bdce8c`（命令位置の公開資料なし） · `00bdcea4`（命令位置の公開資料なし） · `00bdce5c`（命令位置の公開資料なし）

~~~diff
- 00b6d98c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d98c ["INT_ADD", "register:40f0:8", ["const:b6d98c:8", "const:4:8"]]
- 00b6d98c ["CALLIND", null, ["register:0:8"]]
+ 00bdce8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdce8c ["INT_ADD", "register:40f0:8", ["const:bdce8c:8", "const:4:8"]]
+ 00bdce8c ["CALLIND", null, ["register:0:8"]]
- 00b6d98c bytes 00013fd6
+ 00bdce8c bytes 00013fd6
- 00b6d9a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d9a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a20:8"]]
- 00b6d9a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdcea4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdcea4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
+ 00bdcea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d9a4 bytes a0822839
+ 00bdcea4 bytes a0a22439
- 00b6d95c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bdce5c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b6d95c bytes b5290090
+ 00bdce5c bytes 552a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fb8c520149f9846979ac27507c7cb1"></a>

### [`00b6da28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md) → [`00bdcf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf28.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b6da68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcf68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6da3c",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6da44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcf6c"
      ]
    ],
    [
      "unmatched:00b6da4c",
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
      "00bdcf3c",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcf6c"
      ]
    ],
    [
      "00bdcf4c",
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

- 旧版 [`00b6da44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da44) · [`00b6da60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da60) · [`00b6da68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da68)
- 新版 `00bdcf60`（命令位置の公開資料なし）

~~~diff
- 00b6da44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6da44 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6da44 bytes 410100b5
- 00b6da60 ["INT_ADD", "register:40f0:8", ["const:b6da60:8", "const:4:8"]]
- 00b6da60 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdcf60 ["INT_ADD", "register:40f0:8", ["const:bdcf60:8", "const:4:8"]]
+ 00bdcf60 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6da60 bytes 8cc10194
+ 00bdcf60 bytes ecf60194
- 00b6da68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
- 00b6da68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6da68 bytes 800e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ae0b92152e109c1c992827375e473e"></a>

### [`00b6dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md) → [`00bdcfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b6db14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd014"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6daf0"
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
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6daf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd018"
      ]
    ],
    [
      "unmatched:00b6daf8",
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
      "00bdcfe8",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd018"
      ]
    ],
    [
      "00bdcff8",
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

- 旧版 [`00b6daf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6daf0) · [`00b6db0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6db0c) · [`00b6db14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6db14)
- 新版 `00bdd00c`（命令位置の公開資料なし）

~~~diff
- 00b6daf0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6daf0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6daf0 bytes 410100b5
- 00b6db0c ["INT_ADD", "register:40f0:8", ["const:b6db0c:8", "const:4:8"]]
- 00b6db0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd00c ["INT_ADD", "register:40f0:8", ["const:bdd00c:8", "const:4:8"]]
+ 00bdd00c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6db0c bytes 61c10194
+ 00bdd00c bytes c1f60194
- 00b6db14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
- 00b6db14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6db14 bytes 800e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722edec881fe5c6a69fde757840496fc"></a>

### [`00b6db44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md) → [`00bdd044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd044.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdd060",
      "incomplete_value": false,
      "site": "00bdd064",
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
      "definition_site": "00b6db60",
      "incomplete_value": false,
      "site": "00b6db64",
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
      "definition_site": "00bdd070",
      "incomplete_value": true,
      "site": "00bdd07c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6db70",
      "incomplete_value": true,
      "site": "00b6db7c",
      "value": [
        "LOAD",
        "8",
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
      "00bdd060",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bdd070",
      "DATA",
      [
        "storage",
        "010a1aa0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd060",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdd070",
      "DATA",
      [
        "storage",
        "011269a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6db64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db64) · [`00b6db5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db5c) · [`00b6db60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db60)
- 新版 `00bdd064`（命令位置の公開資料なし） · `00bdd05c`（命令位置の公開資料なし） · `00bdd060`（命令位置の公開資料なし）

~~~diff
- 00b6db64 ["INT_ADD", "register:40f0:8", ["const:b6db64:8", "const:4:8"]]
- 00b6db64 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdd064 ["INT_ADD", "register:40f0:8", ["const:bdd064:8", "const:4:8"]]
+ 00bdd064 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6db64 bytes 87c10194
+ 00bdd064 bytes e7f60194
- 00b6db5c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bdd05c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6db5c bytes 60b9ff90
+ 00bdd05c bytes 60b6ff90
- 00b6db60 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6db60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6db60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6db60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd060 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bdd060 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd060 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd060 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6db60 bytes 00c81791
+ 00bdd060 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb572fc4dabcc941674233ccd599b397"></a>

### [`00b6dbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md) → [`00bdd0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd0c0.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00b6dbec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd0ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdd0d4",
      "incomplete_value": true,
      "site": "00bdd0d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dbd4",
      "incomplete_value": true,
      "site": "00b6dbd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bdd0d0",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6dbf0"
      ]
    ],
    [
      "unmatched:00b6dbdc",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd0d0",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd0f0"
      ]
    ],
    [
      "00bdd0dc",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbe4) · [`00b6dbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbec) · [`00b6dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbfc)

~~~diff
- 00b6dbe4 ["INT_ADD", "register:40f0:8", ["const:b6dbe4:8", "const:4:8"]]
- 00b6dbe4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6dbe4 bytes 2bc10194
- 00b6dbec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b6dbec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dbec bytes 605605f9
- 00b6dbfc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6dbfc ["RETURN", null, ["register:0:8"]]
- 00b6dbfc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6064c6c5dd36507593be6e6a3d5cb114"></a>

### [`00b6dc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md) → [`00bdd100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd100.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd130",
      "incomplete_value": true,
      "site": "00bdd130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc30",
      "incomplete_value": true,
      "site": "00b6dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00bdd114",
      "incomplete_value": true,
      "site": "00bdd114",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc14",
      "incomplete_value": true,
      "site": "00b6dc14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd120",
      "incomplete_value": false,
      "site": "00bdd128",
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
            "const:73c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc20",
      "incomplete_value": false,
      "site": "00b6dc28",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd110",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd120",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00bdd130",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd110",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd120",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd130",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc28) · [`00b6dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc30) · [`00b6dc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc0c)
- 新版 `00bdd128`（命令位置の公開資料なし） · `00bdd130`（命令位置の公開資料なし） · `00bdd10c`（命令位置の公開資料なし）

~~~diff
- 00b6dc28 ["INT_ADD", "register:40f0:8", ["const:b6dc28:8", "const:4:8"]]
- 00b6dc28 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd128 ["INT_ADD", "register:40f0:8", ["const:bdd128:8", "const:4:8"]]
+ 00bdd128 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6dc28 bytes 1ac10194
+ 00bdd128 bytes 7af60194
- 00b6dc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b6dc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
+ 00bdd130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dc30 bytes 605605f9
+ 00bdd130 bytes 60da04f9
- 00b6dc0c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd10c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6dc0c bytes b3290090
+ 00bdd10c bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8796f9db8d4d52d5c4874fc8572c2c75"></a>

### [`00b6dc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md) → [`00bdd144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd144.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd174",
      "incomplete_value": true,
      "site": "00bdd174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc74",
      "incomplete_value": true,
      "site": "00b6dc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00bdd158",
      "incomplete_value": true,
      "site": "00bdd158",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc58",
      "incomplete_value": true,
      "site": "00b6dc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd160",
      "incomplete_value": false,
      "site": "00bdd16c",
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
            "const:73c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc60",
      "incomplete_value": false,
      "site": "00b6dc6c",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd154",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd160",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00bdd174",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd154",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd160",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd174",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc6c) · [`00b6dc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc74) · [`00b6dc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc50)
- 新版 `00bdd16c`（命令位置の公開資料なし） · `00bdd174`（命令位置の公開資料なし） · `00bdd150`（命令位置の公開資料なし）

~~~diff
- 00b6dc6c ["INT_ADD", "register:40f0:8", ["const:b6dc6c:8", "const:4:8"]]
- 00b6dc6c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd16c ["INT_ADD", "register:40f0:8", ["const:bdd16c:8", "const:4:8"]]
+ 00bdd16c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6dc6c bytes 09c10194
+ 00bdd16c bytes 69f60194
- 00b6dc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b6dc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd174 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
+ 00bdd174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dc74 bytes 605605f9
+ 00bdd174 bytes 60da04f9
- 00b6dc50 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd150 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6dc50 bytes b3290090
+ 00bdd150 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea059a7cca77283fd59c2b189634afaf"></a>

### [`00b6dc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md) → [`00bdd194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "00b6dcec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd1ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd1c8",
      "incomplete_value": true,
      "site": "00bdd1d4",
      "value": [
        "LOAD",
        "8",
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
                "const:9b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dcc8",
      "incomplete_value": true,
      "site": "00b6dcd4",
      "value": [
        "LOAD",
        "8",
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
                "const:aa8:8"
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
      "00bdd1a8",
      "READ",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b6dcc8",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6dcec",
      "WRITE",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd1a8",
      "READ",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd1c8",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd1ec",
      "WRITE",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md#insn-00b6dcd4) · [`00b6dcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md#insn-00b6dcec)
- 新版 `00bdd1d4`（命令位置の公開資料なし） · `00bdd1ec`（命令位置の公開資料なし）

~~~diff
- 00b6dcd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dcd4 ["INT_ADD", "register:40f0:8", ["const:b6dcd4:8", "const:4:8"]]
- 00b6dcd4 ["CALLIND", null, ["register:0:8"]]
+ 00bdd1d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd1d4 ["INT_ADD", "register:40f0:8", ["const:bdd1d4:8", "const:4:8"]]
+ 00bdd1d4 ["CALLIND", null, ["register:0:8"]]
- 00b6dcd4 bytes 00013fd6
+ 00bdd1d4 bytes 00013fd6
- 00b6dcec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6dcec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ab0:8"]]
- 00b6dcec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6dcec bytes a0c22a39
+ 00bdd1ec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd1ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b8:8"]]
+ 00bdd1ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd1ec bytes a0e22639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be759fef25d8e51acc7d1296719b4614"></a>

### [`00b6dd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md) → [`00bdd200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd200.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdd23c",
      "incomplete_value": true,
      "site": "00bdd23c",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dd3c",
      "incomplete_value": true,
      "site": "00b6dd3c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bdd25c",
      "incomplete_value": true,
      "site": "00bdd25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dd5c",
      "incomplete_value": true,
      "site": "00b6dd5c",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdd218",
      "incomplete_value": true,
      "site": "00bdd218",
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
      "definition_site": "00b6dd18",
      "incomplete_value": true,
      "site": "00b6dd18",
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
      "00bdd214",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd220",
      "READ",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd23c",
      "WRITE",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd214",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd220",
      "READ",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd23c",
      "WRITE",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd3c) · [`00b6dd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd58) · [`00b6dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd5c)
- 新版 `00bdd23c`（命令位置の公開資料なし） · `00bdd258`（命令位置の公開資料なし） · `00bdd25c`（命令位置の公開資料なし）

~~~diff
- 00b6dd3c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6dd3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6dd3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ab0:8"]]
- 00b6dd3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd23c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd23c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd23c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b8:8"]]
+ 00bdd23c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6dd3c bytes bfc22a39
+ 00bdd23c bytes bfe22639
- 00b6dd58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dd58 ["INT_ADD", "register:40f0:8", ["const:b6dd58:8", "const:4:8"]]
- 00b6dd58 ["CALLIND", null, ["register:0:8"]]
+ 00bdd258 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd258 ["INT_ADD", "register:40f0:8", ["const:bdd258:8", "const:4:8"]]
+ 00bdd258 ["CALLIND", null, ["register:0:8"]]
- 00b6dd58 bytes 00013fd6
+ 00bdd258 bytes 00013fd6
- 00b6dd5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b6dd5c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6dd5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
+ 00bdd25c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd25c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6dd5c bytes 9f5605f9
+ 00bdd25c bytes 9fda04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ac6305a8cd3ac776f7b86456ff3d4a"></a>

### [`00b6dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md) → [`00bdd270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd270.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b6ddb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd2b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dd8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6dd84",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6dd8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd2b4"
      ]
    ],
    [
      "unmatched:00b6dd94",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd284",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd28c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd2b4"
      ]
    ],
    [
      "00bdd294",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6dd8c) · [`00b6dda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6dda8) · [`00b6ddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6ddb0)
- 新版 `00bdd2a8`（命令位置の公開資料なし）

~~~diff
- 00b6dd8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6dd8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6dd8c bytes 410100b5
- 00b6dda8 ["INT_ADD", "register:40f0:8", ["const:b6dda8:8", "const:4:8"]]
- 00b6dda8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd2a8 ["INT_ADD", "register:40f0:8", ["const:bdd2a8:8", "const:4:8"]]
+ 00bdd2a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6dda8 bytes bac00194
+ 00bdd2a8 bytes 1af60194
- 00b6ddb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b6ddb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6ddb0 bytes 805605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68a3d113a06af8af7564a9446dd3d92c"></a>

### [`00b6de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md) → [`00bdd31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd31c.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd35c",
      "incomplete_value": true,
      "site": "00bdd35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de5c",
      "incomplete_value": true,
      "site": "00b6de5c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdd338",
      "incomplete_value": true,
      "site": "00bdd338",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de38",
      "incomplete_value": true,
      "site": "00b6de38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd340",
      "incomplete_value": false,
      "site": "00bdd354",
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
            "const:73c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de40",
      "incomplete_value": false,
      "site": "00b6de54",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd330",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd340",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00bdd35c",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd330",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd340",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd35c",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6de54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de54) · [`00b6de5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de5c) · [`00b6de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de28)
- 新版 `00bdd354`（命令位置の公開資料なし） · `00bdd35c`（命令位置の公開資料なし） · `00bdd328`（命令位置の公開資料なし）

~~~diff
- 00b6de54 ["INT_ADD", "register:40f0:8", ["const:b6de54:8", "const:4:8"]]
- 00b6de54 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd354 ["INT_ADD", "register:40f0:8", ["const:bdd354:8", "const:4:8"]]
+ 00bdd354 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6de54 bytes 8fc00194
+ 00bdd354 bytes eff50194
- 00b6de5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b6de5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd35c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
+ 00bdd35c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6de5c bytes 805605f9
+ 00bdd35c bytes 80da04f9
- 00b6de28 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bdd328 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6de28 bytes b4290090
+ 00bdd328 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab88c27bfaaf323c3d42f41982de5945"></a>

### [`00b6de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md) → [`00bdd38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd38c.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdd3a8",
      "incomplete_value": false,
      "site": "00bdd3ac",
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
      "definition_site": "00b6dea8",
      "incomplete_value": false,
      "site": "00b6deac",
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
      "definition_site": "00bdd3b8",
      "incomplete_value": true,
      "site": "00bdd3c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6deb8",
      "incomplete_value": true,
      "site": "00b6dec4",
      "value": [
        "LOAD",
        "8",
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
      "00bdd3a8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bdd3b8",
      "DATA",
      [
        "storage",
        "010a1af0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd3a8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdd3b8",
      "DATA",
      [
        "storage",
        "011269f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6deac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6deac) · [`00b6dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6dea4) · [`00b6dea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6dea8)
- 新版 `00bdd3ac`（命令位置の公開資料なし） · `00bdd3a4`（命令位置の公開資料なし） · `00bdd3a8`（命令位置の公開資料なし）

~~~diff
- 00b6deac ["INT_ADD", "register:40f0:8", ["const:b6deac:8", "const:4:8"]]
- 00b6deac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdd3ac ["INT_ADD", "register:40f0:8", ["const:bdd3ac:8", "const:4:8"]]
+ 00bdd3ac ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6deac bytes b5c00194
+ 00bdd3ac bytes 15f60194
- 00b6dea4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bdd3a4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6dea4 bytes 60b9ff90
+ 00bdd3a4 bytes 60b6ff90
- 00b6dea8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6dea8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6dea8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6dea8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3a8 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bdd3a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6dea8 bytes 00c81791
+ 00bdd3a8 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c05cf57584fd9aeed08fdda8bfc745"></a>

### [`00b6dec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md) → [`00bdd3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd3c8.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bdd3f4",
      "incomplete_value": true,
      "site": "00bdd3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6def4",
      "incomplete_value": true,
      "site": "00b6def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd3dc",
      "incomplete_value": true,
      "site": "00bdd3dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dedc",
      "incomplete_value": true,
      "site": "00b6dedc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd3e8",
      "incomplete_value": false,
      "site": "00bdd3ec",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dee8",
      "incomplete_value": false,
      "site": "00b6deec",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd3d8",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd3e8",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd3f4",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd3d8",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd3e8",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd3f4",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6deec) · [`00b6def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6def4) · [`00b6ded4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6ded4)
- 新版 `00bdd3ec`（命令位置の公開資料なし） · `00bdd3f4`（命令位置の公開資料なし） · `00bdd3d4`（命令位置の公開資料なし）

~~~diff
- 00b6deec ["INT_ADD", "register:40f0:8", ["const:b6deec:8", "const:4:8"]]
- 00b6deec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd3ec ["INT_ADD", "register:40f0:8", ["const:bdd3ec:8", "const:4:8"]]
+ 00bdd3ec ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6deec bytes 69c00194
+ 00bdd3ec bytes c9f50194
- 00b6def4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
- 00b6def4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd3f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
+ 00bdd3f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6def4 bytes 607e05f9
+ 00bdd3f4 bytes 600205f9
- 00b6ded4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd3d4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6ded4 bytes b3290090
+ 00bdd3d4 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b31814a0b2958827f60ec2b7ae8f40"></a>

### [`00b6df08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md) → [`00bdd408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd408.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdd434",
      "incomplete_value": true,
      "site": "00bdd434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df34",
      "incomplete_value": true,
      "site": "00b6df34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd41c",
      "incomplete_value": true,
      "site": "00bdd41c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df1c",
      "incomplete_value": true,
      "site": "00b6df1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd424",
      "incomplete_value": false,
      "site": "00bdd42c",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df24",
      "incomplete_value": false,
      "site": "00b6df2c",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd418",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd424",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd434",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd418",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd424",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd434",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df2c) · [`00b6df34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df34) · [`00b6df14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df14)
- 新版 `00bdd42c`（命令位置の公開資料なし） · `00bdd434`（命令位置の公開資料なし） · `00bdd414`（命令位置の公開資料なし）

~~~diff
- 00b6df2c ["INT_ADD", "register:40f0:8", ["const:b6df2c:8", "const:4:8"]]
- 00b6df2c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd42c ["INT_ADD", "register:40f0:8", ["const:bdd42c:8", "const:4:8"]]
+ 00bdd42c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6df2c bytes 59c00194
+ 00bdd42c bytes b9f50194
- 00b6df34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
- 00b6df34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd434 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
+ 00bdd434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6df34 bytes 607e05f9
+ 00bdd434 bytes 600205f9
- 00b6df14 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd414 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6df14 bytes b3290090
+ 00bdd414 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e15ffb15b9bdb5aa304518f820fb09"></a>

### [`00b6df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md) → [`00bdd448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd448.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd478",
      "incomplete_value": true,
      "site": "00bdd478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df78",
      "incomplete_value": true,
      "site": "00b6df78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd45c",
      "incomplete_value": true,
      "site": "00bdd45c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd468",
      "incomplete_value": false,
      "site": "00bdd470",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df68",
      "incomplete_value": false,
      "site": "00b6df70",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd458",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd468",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd478",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd458",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd468",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd478",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df70) · [`00b6df78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df78) · [`00b6df54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df54)
- 新版 `00bdd470`（命令位置の公開資料なし） · `00bdd478`（命令位置の公開資料なし） · `00bdd454`（命令位置の公開資料なし）

~~~diff
- 00b6df70 ["INT_ADD", "register:40f0:8", ["const:b6df70:8", "const:4:8"]]
- 00b6df70 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd470 ["INT_ADD", "register:40f0:8", ["const:bdd470:8", "const:4:8"]]
+ 00bdd470 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6df70 bytes 48c00194
+ 00bdd470 bytes a8f50194
- 00b6df78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
- 00b6df78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd478 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
+ 00bdd478 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6df78 bytes 607e05f9
+ 00bdd478 bytes 600205f9
- 00b6df54 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd454 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6df54 bytes b3290090
+ 00bdd454 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-160815c1f3edecf8da81df3c31e05cd6"></a>

### [`00b6df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md) → [`00bdd48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd48c.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd4bc",
      "incomplete_value": true,
      "site": "00bdd4bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfbc",
      "incomplete_value": true,
      "site": "00b6dfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd4a0",
      "incomplete_value": true,
      "site": "00bdd4a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfa0",
      "incomplete_value": true,
      "site": "00b6dfa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd4a8",
      "incomplete_value": false,
      "site": "00bdd4b4",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfa8",
      "incomplete_value": false,
      "site": "00b6dfb4",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd49c",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4a8",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd4bc",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd49c",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4a8",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd4bc",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6dfb4) · [`00b6dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6dfbc) · [`00b6df98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6df98)
- 新版 `00bdd4b4`（命令位置の公開資料なし） · `00bdd4bc`（命令位置の公開資料なし） · `00bdd498`（命令位置の公開資料なし）

~~~diff
- 00b6dfb4 ["INT_ADD", "register:40f0:8", ["const:b6dfb4:8", "const:4:8"]]
- 00b6dfb4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd4b4 ["INT_ADD", "register:40f0:8", ["const:bdd4b4:8", "const:4:8"]]
+ 00bdd4b4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6dfb4 bytes 37c00194
+ 00bdd4b4 bytes 97f50194
- 00b6dfbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
- 00b6dfbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd4bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
+ 00bdd4bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dfbc bytes 607e05f9
+ 00bdd4bc bytes 600205f9
- 00b6df98 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd498 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6df98 bytes b3290090
+ 00bdd498 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9308e530189fc9941d481666e92c0cc1"></a>

### [`00b6e048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md) → [`00bdd548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd548.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

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
      "site": "00b6e084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e0a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd584"
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
      "00bdd55c",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e0a8"
      ]
    ],
    [
      "00bdd568",
      "READ",
      [
        "storage",
        "010a1b00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd55c",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd5a8"
      ]
    ],
    [
      "00bdd568",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e084) · [`00b6e08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e08c) · [`00b6e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e0a0)

~~~diff
- 00b6e084 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b00:8"]]
- 00b6e084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e084 bytes bf022c39
- 00b6e08c ["INT_ADD", "register:40f0:8", ["const:b6e08c:8", "const:4:8"]]
- 00b6e08c ["CALL", null, ["callee:00c5ab60:8"]]
- 00b6e08c bytes 15c00194
- 00b6e0a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e0a0 ["INT_ADD", "register:40f0:8", ["const:b6e0a0:8", "const:4:8"]]
- 00b6e0a0 ["CALLIND", null, ["register:0:8"]]
- 00b6e0a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7062c35f33613cdf237d268c9789049"></a>

### [`00b6e0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md) → [`00bdd5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd5b8.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd5f8",
      "incomplete_value": true,
      "site": "00bdd5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e0f8",
      "incomplete_value": true,
      "site": "00b6e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd5d4",
      "incomplete_value": true,
      "site": "00bdd5d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e0d4",
      "incomplete_value": true,
      "site": "00b6e0d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd5dc",
      "incomplete_value": false,
      "site": "00bdd5f0",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e0dc",
      "incomplete_value": false,
      "site": "00b6e0f0",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd5cc",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5dc",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd5f8",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd5cc",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5dc",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd5f8",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0f0) · [`00b6e0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0f8) · [`00b6e0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0c4)
- 新版 `00bdd5f0`（命令位置の公開資料なし） · `00bdd5f8`（命令位置の公開資料なし） · `00bdd5c4`（命令位置の公開資料なし）

~~~diff
- 00b6e0f0 ["INT_ADD", "register:40f0:8", ["const:b6e0f0:8", "const:4:8"]]
- 00b6e0f0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd5f0 ["INT_ADD", "register:40f0:8", ["const:bdd5f0:8", "const:4:8"]]
+ 00bdd5f0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e0f0 bytes e8bf0194
+ 00bdd5f0 bytes 48f50194
- 00b6e0f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
- 00b6e0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd5f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
+ 00bdd5f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e0f8 bytes 807e05f9
+ 00bdd5f8 bytes 800205f9
- 00b6e0c4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bdd5c4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6e0c4 bytes 942900f0
+ 00bdd5c4 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4cbc0e2a137014badb2b758a2dcffef"></a>

### [`00b6e128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md) → [`00bdd628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd628.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdd644",
      "incomplete_value": false,
      "site": "00bdd648",
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
      "definition_site": "00b6e144",
      "incomplete_value": false,
      "site": "00b6e148",
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
      "definition_site": "00bdd654",
      "incomplete_value": true,
      "site": "00bdd660",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e154",
      "incomplete_value": true,
      "site": "00b6e160",
      "value": [
        "LOAD",
        "8",
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
      "00bdd644",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bdd654",
      "DATA",
      [
        "storage",
        "010a1b08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd644",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdd654",
      "DATA",
      [
        "storage",
        "01126a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e148) · [`00b6e140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e140) · [`00b6e144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e144)
- 新版 `00bdd648`（命令位置の公開資料なし） · `00bdd640`（命令位置の公開資料なし） · `00bdd644`（命令位置の公開資料なし）

~~~diff
- 00b6e148 ["INT_ADD", "register:40f0:8", ["const:b6e148:8", "const:4:8"]]
- 00b6e148 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdd648 ["INT_ADD", "register:40f0:8", ["const:bdd648:8", "const:4:8"]]
+ 00bdd648 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6e148 bytes 0ec00194
+ 00bdd648 bytes 6ef50194
- 00b6e140 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bdd640 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b6e140 bytes 40b9ffd0
+ 00bdd640 bytes 40b6fff0
- 00b6e144 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6e144 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e144 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e144 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd644 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bdd644 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd644 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd644 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e144 bytes 001c1591
+ 00bdd644 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b84385fa1b2a83e9af5174c4d815a443"></a>

### [`00b6e164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md) → [`00bdd664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd6a4",
      "incomplete_value": true,
      "site": "00bdd6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1a4",
      "incomplete_value": true,
      "site": "00b6e1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "definition_site": "00bdd680",
      "incomplete_value": true,
      "site": "00bdd680",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e180",
      "incomplete_value": true,
      "site": "00b6e180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd688",
      "incomplete_value": false,
      "site": "00bdd69c",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e188",
      "incomplete_value": false,
      "site": "00b6e19c",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd678",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd688",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00bdd6a4",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd678",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd688",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd6a4",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e19c) · [`00b6e1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e1a4) · [`00b6e170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e170)
- 新版 `00bdd69c`（命令位置の公開資料なし） · `00bdd6a4`（命令位置の公開資料なし） · `00bdd670`（命令位置の公開資料なし）

~~~diff
- 00b6e19c ["INT_ADD", "register:40f0:8", ["const:b6e19c:8", "const:4:8"]]
- 00b6e19c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd69c ["INT_ADD", "register:40f0:8", ["const:bdd69c:8", "const:4:8"]]
+ 00bdd69c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e19c bytes bdbf0194
+ 00bdd69c bytes 1df50194
- 00b6e1a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
- 00b6e1a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd6a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
+ 00bdd6a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e1a4 bytes 807e05f9
+ 00bdd6a4 bytes 800205f9
- 00b6e170 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bdd670 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6e170 bytes 942900f0
+ 00bdd670 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f32bd7d2388ff53954e4568d3dd7a1c6"></a>

### [`00b6e250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md) → [`00bdd750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd750.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b6e27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd77c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdd764",
      "incomplete_value": true,
      "site": "00bdd764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e264",
      "incomplete_value": true,
      "site": "00b6e264",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bdd760",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e280"
      ]
    ],
    [
      "unmatched:00b6e26c",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd760",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd780"
      ]
    ],
    [
      "00bdd76c",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e264) · [`00b6e274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e274) · [`00b6e27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e27c)
- 新版 `00bdd764`（命令位置の公開資料なし）

~~~diff
- 00b6e264 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6e264 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bdd764 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdd764 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6e264 bytes e80000b5
+ 00bdd764 bytes e80000b5
- 00b6e274 ["INT_ADD", "register:40f0:8", ["const:b6e274:8", "const:4:8"]]
- 00b6e274 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e274 bytes 87bf0194
- 00b6e27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
- 00b6e27c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e27c bytes 609205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0379679328cac1726c7b600e480fff5"></a>

### [`00b6e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md) → [`00bdd790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd7c0",
      "incomplete_value": true,
      "site": "00bdd7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2c0",
      "incomplete_value": true,
      "site": "00b6e2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00bdd7a4",
      "incomplete_value": true,
      "site": "00bdd7a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2a4",
      "incomplete_value": true,
      "site": "00b6e2a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd7b0",
      "incomplete_value": false,
      "site": "00bdd7b8",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2b0",
      "incomplete_value": false,
      "site": "00b6e2b8",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd7a0",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd7b0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00bdd7c0",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd7a0",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd7b0",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bdd7c0",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e2b8) · [`00b6e2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e2c0) · [`00b6e29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e29c)
- 新版 `00bdd7b8`（命令位置の公開資料なし） · `00bdd7c0`（命令位置の公開資料なし） · `00bdd79c`（命令位置の公開資料なし）

~~~diff
- 00b6e2b8 ["INT_ADD", "register:40f0:8", ["const:b6e2b8:8", "const:4:8"]]
- 00b6e2b8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd7b8 ["INT_ADD", "register:40f0:8", ["const:bdd7b8:8", "const:4:8"]]
+ 00bdd7b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e2b8 bytes 76bf0194
+ 00bdd7b8 bytes d6f40194
- 00b6e2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
- 00b6e2c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd7c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bdd7c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e2c0 bytes 609205f9
+ 00bdd7c0 bytes 601605f9
- 00b6e29c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd79c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6e29c bytes 932900f0
+ 00bdd79c bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f7fee0d7447ce43d99ca1480e4892e"></a>

### [`00b6e2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md) → [`00bdd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd804",
      "incomplete_value": true,
      "site": "00bdd804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e304",
      "incomplete_value": true,
      "site": "00b6e304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00bdd7e8",
      "incomplete_value": true,
      "site": "00bdd7e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2e8",
      "incomplete_value": true,
      "site": "00b6e2e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd7f0",
      "incomplete_value": false,
      "site": "00bdd7fc",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2f0",
      "incomplete_value": false,
      "site": "00b6e2fc",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd7e4",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd7f0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00bdd804",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd7e4",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd7f0",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bdd804",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e2fc) · [`00b6e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e304) · [`00b6e2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e2e0)
- 新版 `00bdd7fc`（命令位置の公開資料なし） · `00bdd804`（命令位置の公開資料なし） · `00bdd7e0`（命令位置の公開資料なし）

~~~diff
- 00b6e2fc ["INT_ADD", "register:40f0:8", ["const:b6e2fc:8", "const:4:8"]]
- 00b6e2fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd7fc ["INT_ADD", "register:40f0:8", ["const:bdd7fc:8", "const:4:8"]]
+ 00bdd7fc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e2fc bytes 65bf0194
+ 00bdd7fc bytes c5f40194
- 00b6e304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
- 00b6e304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bdd804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e304 bytes 609205f9
+ 00bdd804 bytes 601605f9
- 00b6e2e0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bdd7e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6e2e0 bytes 932900f0
+ 00bdd7e0 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd46a1faa1223a3cbe3d16977d4b9e6"></a>

### [`00b6e324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md) → [`00bdd824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd87c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd858",
      "incomplete_value": true,
      "site": "00bdd864",
      "value": [
        "LOAD",
        "8",
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e358",
      "incomplete_value": true,
      "site": "00b6e364",
      "value": [
        "LOAD",
        "8",
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
                "const:b20:8"
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
      "00bdd838",
      "READ",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b6e358",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e37c",
      "WRITE",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd838",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd858",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd87c",
      "WRITE",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e364) · [`00b6e370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e370) · [`00b6e37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e37c)
- 新版 `00bdd864`（命令位置の公開資料なし） · `00bdd870`（命令位置の公開資料なし）

~~~diff
- 00b6e364 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e364 ["INT_ADD", "register:40f0:8", ["const:b6e364:8", "const:4:8"]]
- 00b6e364 ["CALLIND", null, ["register:0:8"]]
+ 00bdd864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd864 ["INT_ADD", "register:40f0:8", ["const:bdd864:8", "const:4:8"]]
+ 00bdd864 ["CALLIND", null, ["register:0:8"]]
- 00b6e364 bytes 00013fd6
+ 00bdd864 bytes 00013fd6
- 00b6e370 ["INT_ADD", "register:40f0:8", ["const:b6e370:8", "const:4:8"]]
- 00b6e370 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00bdd870 ["INT_ADD", "register:40f0:8", ["const:bdd870:8", "const:4:8"]]
+ 00bdd870 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b6e370 bytes 5cbf0194
+ 00bdd870 bytes bcf40194
- 00b6e37c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6e37c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b28:8"]]
- 00b6e37c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6e37c bytes a0a22c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d24d50a2e2ce4f1e1d555b2a60703aa"></a>

### [`00b6e390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md) → [`00bdd890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdd8cc",
      "incomplete_value": true,
      "site": "00bdd8cc",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3cc",
      "incomplete_value": true,
      "site": "00b6e3cc",
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
            "const:b28:8"
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
      "definition_site": "00bdd8ec",
      "incomplete_value": true,
      "site": "00bdd8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3ec",
      "incomplete_value": true,
      "site": "00b6e3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00bdd8a8",
      "incomplete_value": true,
      "site": "00bdd8a8",
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
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
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
      "00bdd8a4",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8b0",
      "READ",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd8cc",
      "WRITE",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd8a4",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8b0",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd8cc",
      "WRITE",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3cc) · [`00b6e3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3e8) · [`00b6e3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3ec)
- 新版 `00bdd8cc`（命令位置の公開資料なし） · `00bdd8e8`（命令位置の公開資料なし） · `00bdd8ec`（命令位置の公開資料なし）

~~~diff
- 00b6e3cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e3cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e3cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b28:8"]]
- 00b6e3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd8cc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd8cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd8cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a30:8"]]
+ 00bdd8cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e3cc bytes bfa22c39
+ 00bdd8cc bytes bfc22839
- 00b6e3e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e3e8 ["INT_ADD", "register:40f0:8", ["const:b6e3e8:8", "const:4:8"]]
- 00b6e3e8 ["CALLIND", null, ["register:0:8"]]
+ 00bdd8e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd8e8 ["INT_ADD", "register:40f0:8", ["const:bdd8e8:8", "const:4:8"]]
+ 00bdd8e8 ["CALLIND", null, ["register:0:8"]]
- 00b6e3e8 bytes 00013fd6
+ 00bdd8e8 bytes 00013fd6
- 00b6e3ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
- 00b6e3ec ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6e3ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd8ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
+ 00bdd8ec ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd8ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6e3ec bytes 9f9205f9
+ 00bdd8ec bytes 9f1605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-babbc6148651ba872618f8da14ca92ec"></a>

### [`00b6e400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md) → [`00bdd900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd900.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b6e440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd940"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e41c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e414",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e41c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd944"
      ]
    ],
    [
      "unmatched:00b6e424",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd914",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd944"
      ]
    ],
    [
      "00bdd924",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e41c) · [`00b6e438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e438) · [`00b6e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e440)
- 新版 `00bdd938`（命令位置の公開資料なし）

~~~diff
- 00b6e41c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6e41c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6e41c bytes 410100b5
- 00b6e438 ["INT_ADD", "register:40f0:8", ["const:b6e438:8", "const:4:8"]]
- 00b6e438 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd938 ["INT_ADD", "register:40f0:8", ["const:bdd938:8", "const:4:8"]]
+ 00bdd938 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e438 bytes 16bf0194
+ 00bdd938 bytes 76f40194
- 00b6e440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
- 00b6e440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e440 bytes 809205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0eae9456597d0e4ce6e484ca80ed73"></a>

### [`00b6e470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md) → [`00bdd970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd970.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdd98c",
      "incomplete_value": false,
      "site": "00bdd990",
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
      "definition_site": "00b6e48c",
      "incomplete_value": false,
      "site": "00b6e490",
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
      "definition_site": "00bdd99c",
      "incomplete_value": true,
      "site": "00bdd9a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e49c",
      "incomplete_value": true,
      "site": "00b6e4a8",
      "value": [
        "LOAD",
        "8",
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
      "00bdd98c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bdd99c",
      "DATA",
      [
        "storage",
        "010a1b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd98c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdd99c",
      "DATA",
      [
        "storage",
        "01126a38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e490) · [`00b6e488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e488) · [`00b6e48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e48c)
- 新版 `00bdd990`（命令位置の公開資料なし） · `00bdd988`（命令位置の公開資料なし） · `00bdd98c`（命令位置の公開資料なし）

~~~diff
- 00b6e490 ["INT_ADD", "register:40f0:8", ["const:b6e490:8", "const:4:8"]]
- 00b6e490 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdd990 ["INT_ADD", "register:40f0:8", ["const:bdd990:8", "const:4:8"]]
+ 00bdd990 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6e490 bytes 3cbf0194
+ 00bdd990 bytes 9cf40194
- 00b6e488 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bdd988 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b6e488 bytes 40b9ffd0
+ 00bdd988 bytes 40b6fff0
- 00b6e48c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6e48c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e48c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e48c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd98c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bdd98c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd98c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd98c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e48c bytes 001c1591
+ 00bdd98c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2199ac44e353f4fbd0970184e01bcad7"></a>

### [`00b6e4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md) → [`00bdd9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd9ec",
      "incomplete_value": true,
      "site": "00bdd9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e4ec",
      "incomplete_value": true,
      "site": "00b6e4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00bdd9c8",
      "incomplete_value": true,
      "site": "00bdd9c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e4c8",
      "incomplete_value": true,
      "site": "00b6e4c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd9d0",
      "incomplete_value": false,
      "site": "00bdd9e4",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e4d0",
      "incomplete_value": false,
      "site": "00b6e4e4",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd9c0",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd9d0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00bdd9ec",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd9c0",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd9d0",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bdd9ec",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4e4) · [`00b6e4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4ec) · [`00b6e4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4b8)
- 新版 `00bdd9e4`（命令位置の公開資料なし） · `00bdd9ec`（命令位置の公開資料なし） · `00bdd9b8`（命令位置の公開資料なし）

~~~diff
- 00b6e4e4 ["INT_ADD", "register:40f0:8", ["const:b6e4e4:8", "const:4:8"]]
- 00b6e4e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bdd9e4 ["INT_ADD", "register:40f0:8", ["const:bdd9e4:8", "const:4:8"]]
+ 00bdd9e4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e4e4 bytes ebbe0194
+ 00bdd9e4 bytes 4bf40194
- 00b6e4ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
- 00b6e4ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd9ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
+ 00bdd9ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e4ec bytes 809205f9
+ 00bdd9ec bytes 801605f9
- 00b6e4b8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bdd9b8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6e4b8 bytes 942900f0
+ 00bdd9b8 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0303d6aaf611a4b650a9ff152f20bda"></a>

### [`00b6e51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md) → [`00bdda1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda1c.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdda38",
      "incomplete_value": false,
      "site": "00bdda3c",
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
      "definition_site": "00b6e538",
      "incomplete_value": false,
      "site": "00b6e53c",
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
      "definition_site": "00bdda48",
      "incomplete_value": true,
      "site": "00bdda54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e548",
      "incomplete_value": true,
      "site": "00b6e554",
      "value": [
        "LOAD",
        "8",
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
      "00bdda38",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bdda48",
      "DATA",
      [
        "storage",
        "010a1b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdda38",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdda48",
      "DATA",
      [
        "storage",
        "01126a58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e53c) · [`00b6e534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e534) · [`00b6e538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e538)
- 新版 `00bdda3c`（命令位置の公開資料なし） · `00bdda34`（命令位置の公開資料なし） · `00bdda38`（命令位置の公開資料なし）

~~~diff
- 00b6e53c ["INT_ADD", "register:40f0:8", ["const:b6e53c:8", "const:4:8"]]
- 00b6e53c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdda3c ["INT_ADD", "register:40f0:8", ["const:bdda3c:8", "const:4:8"]]
+ 00bdda3c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6e53c bytes 11bf0194
+ 00bdda3c bytes 71f40194
- 00b6e534 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bdda34 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b6e534 bytes 40b9fff0
+ 00bdda34 bytes 60b6ff90
- 00b6e538 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6e538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdda38 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bdda38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdda38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdda38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e538 bytes 00c81791
+ 00bdda38 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134b085175cabc5e1fe71746f3b321f1"></a>

### [`00b6e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md) → [`00bdda58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda58.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c50.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d850.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e59c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e64c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e570",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e5a0"
      ]
    ],
    [
      "unmatched:00b6e580",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdda70",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdda78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddaa0"
      ]
    ],
    [
      "00bdda80",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e578) · [`00b6e594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e594) · [`00b6e59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e59c)

~~~diff
- 00b6e578 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6e578 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6e578 bytes 410100b5
- 00b6e594 ["INT_ADD", "register:40f0:8", ["const:b6e594:8", "const:4:8"]]
- 00b6e594 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6e594 bytes bfbe0194
- 00b6e59c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
- 00b6e59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e59c bytes a0fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be2a65e6cb8b994cb4bfcaf1cd4d2fae"></a>

### [`00b6e744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md) → [`00bddc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddc44.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c70.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d870.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.46% / 新版 13.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e7cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bddc58",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e7a4"
      ]
    ],
    [
      "00bddc68",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddc58",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddca4"
      ]
    ],
    [
      "00bddc68",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e76c) · [`00b6e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e780) · [`00b6e7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e7a0)

~~~diff
- 00b6e76c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b6e76c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6e76c bytes c8000034
- 00b6e780 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e780 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e780 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a00:8"]]
- 00b6e780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e780 bytes bf022839
- 00b6e7a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6e7a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6e7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6e7a0 bytes 9ffe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42871fad07910403ae2070d8330c71ac"></a>

### [`00b6e9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e9a4.md) → [`00bddea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddea4.md) _ZNK8firebase4auth4User3uidEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdded4",
      "incomplete_value": true,
      "site": "00bddee0",
      "value": [
        "LOAD",
        "8",
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
                "const:9c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e9d4",
      "incomplete_value": true,
      "site": "00b6e9e0",
      "value": [
        "LOAD",
        "8",
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
                "const:ab8:8"
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ea44"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bddf44"
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
      "00bdded4",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6ea24",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdded4",
      "READ",
      [
        "storage",
        "011269c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddf24",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e9a4.md#insn-00b6e9e0) · [`00b6ea44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e9a4.md#insn-00b6ea44)
- 新版 `00bddee0`（命令位置の公開資料なし） · `00bddf44`（命令位置の公開資料なし）

~~~diff
- 00b6e9e0 ["INT_ADD", "register:40f0:8", ["const:b6e9e0:8", "const:4:8"]]
- 00b6e9e0 ["CALL", null, ["callee:004977f4:8"]]
+ 00bddee0 ["INT_ADD", "register:40f0:8", ["const:bddee0:8", "const:4:8"]]
+ 00bddee0 ["CALL", null, ["callee:004977f4:8"]]
- 00b6e9e0 bytes df17e497
+ 00bddee0 bytes 45e6e297
- 00b6ea44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6ea44 ["RETURN", null, ["register:0:8"]]
- 00b6ea44 bytes c0035fd6
+ 00bddf44 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bddf44 ["RETURN", null, ["register:0:8"]]
+ 00bddf44 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce6fe3cf44489fab674f2e89459dcfa9"></a>

### [`00b6ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ea48.md) → [`00bddf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddf48.md) _ZNK8firebase4auth4User5emailEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 70.00% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddf78",
      "incomplete_value": true,
      "site": "00bddf84",
      "value": [
        "LOAD",
        "8",
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
                "const:9e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ea78",
      "incomplete_value": true,
      "site": "00b6ea84",
      "value": [
        "LOAD",
        "8",
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
                "const:ae0:8"
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
      "00bddf78",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddfc8",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddf78",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddfc8",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ea84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ea48.md#insn-00b6ea84) · [`00b6ea60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ea48.md#insn-00b6ea60) · [`00b6ea68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ea48.md#insn-00b6ea68)
- 新版 `00bddf84`（命令位置の公開資料なし） · `00bddf60`（命令位置の公開資料なし） · `00bddf68`（命令位置の公開資料なし）

~~~diff
- 00b6ea84 ["INT_ADD", "register:40f0:8", ["const:b6ea84:8", "const:4:8"]]
- 00b6ea84 ["CALL", null, ["callee:004977f4:8"]]
+ 00bddf84 ["INT_ADD", "register:40f0:8", ["const:bddf84:8", "const:4:8"]]
+ 00bddf84 ["CALL", null, ["callee:004977f4:8"]]
- 00b6ea84 bytes b617e497
+ 00bddf84 bytes 1ce6e297
- 00b6ea60 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6ea60 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bddf60 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bddf60 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6ea60 bytes c90200b4
+ 00bddf60 bytes c90200b4
- 00b6ea68 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6ea68 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bddf68 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00bddf68 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6ea68 bytes 950200b4
+ 00bddf68 bytes 950200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7de7c36ed6f0b3b0347b1f9721a01d"></a>

### [`00b6eaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eaec.md) → [`00bddfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddfec.md) _ZNK8firebase4auth4User12display_nameEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde01c",
      "incomplete_value": true,
      "site": "00bde028",
      "value": [
        "LOAD",
        "8",
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eb1c",
      "incomplete_value": true,
      "site": "00b6eb28",
      "value": [
        "LOAD",
        "8",
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
                "const:ac8:8"
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6eb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bde08c"
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
      "00bde01c",
      "READ",
      [
        "storage",
        "010a1ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6eb6c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bde01c",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde06c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eaec.md#insn-00b6eb28) · [`00b6eb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eaec.md#insn-00b6eb8c)
- 新版 `00bde028`（命令位置の公開資料なし） · `00bde08c`（命令位置の公開資料なし）

~~~diff
- 00b6eb28 ["INT_ADD", "register:40f0:8", ["const:b6eb28:8", "const:4:8"]]
- 00b6eb28 ["CALL", null, ["callee:004977f4:8"]]
+ 00bde028 ["INT_ADD", "register:40f0:8", ["const:bde028:8", "const:4:8"]]
+ 00bde028 ["CALL", null, ["callee:004977f4:8"]]
- 00b6eb28 bytes 8d17e497
+ 00bde028 bytes f3e5e297
- 00b6eb8c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6eb8c ["RETURN", null, ["register:0:8"]]
- 00b6eb8c bytes c0035fd6
+ 00bde08c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bde08c ["RETURN", null, ["register:0:8"]]
+ 00bde08c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a43f2f9ea1896beae262989af120df"></a>

### [`00b6ec34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ec34.md) → [`00bde134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde134.md) _ZNK8firebase4auth4User9photo_urlEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde470.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5aef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aef0.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ec34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ec38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ec38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ec34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ec38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ec3c",
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
      "00bde134",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bde138",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bde13c",
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

- 旧版 [`00b6ec34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ec34.md#insn-00b6ec34) · [`00b6ec38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ec34.md#insn-00b6ec38) · [`00b6ec3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ec34.md#insn-00b6ec3c)

~~~diff
- 00b6ec34 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6ec34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6ec34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6ec34 bytes f50f1df8
- 00b6ec38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6ec38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6ec38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6ec38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ec38 bytes f44f01a9
- 00b6ec3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6ec3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6ec3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6ec3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ec3c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e6185845ac7e64c9d84445f8f1f0b7a"></a>

### [`00b6ecd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ecd8.md) → [`00bde1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde1d8.md) _ZNK8firebase4auth4User11provider_idEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 50.00% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde1fc",
      "incomplete_value": true,
      "site": "00bde200",
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
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde208",
      "incomplete_value": true,
      "site": "00bde214",
      "value": [
        "LOAD",
        "8",
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
                "const:9c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ed08",
      "incomplete_value": true,
      "site": "00b6ed14",
      "value": [
        "LOAD",
        "8",
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
                "const:ac0:8"
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
      "00bde208",
      "READ",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde258",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bde208",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde258",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ed00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ecd8.md#insn-00b6ed00) · [`00b6ed14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ecd8.md#insn-00b6ed14) · [`00b6ecf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ecd8.md#insn-00b6ecf0)
- 新版 `00bde200`（命令位置の公開資料なし） · `00bde214`（命令位置の公開資料なし） · `00bde1f0`（命令位置の公開資料なし）

~~~diff
- 00b6ed00 ["INT_ADD", "register:40f0:8", ["const:b6ed00:8", "const:4:8"]]
- 00b6ed00 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bde200 ["INT_ADD", "register:40f0:8", ["const:bde200:8", "const:4:8"]]
+ 00bde200 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b6ed00 bytes 40bd0194
+ 00bde200 bytes a0f20194
- 00b6ed14 ["INT_ADD", "register:40f0:8", ["const:b6ed14:8", "const:4:8"]]
- 00b6ed14 ["CALL", null, ["callee:004977f4:8"]]
+ 00bde214 ["INT_ADD", "register:40f0:8", ["const:bde214:8", "const:4:8"]]
+ 00bde214 ["CALL", null, ["callee:004977f4:8"]]
- 00b6ed14 bytes 1217e497
+ 00bde214 bytes 78e5e297
- 00b6ecf0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6ecf0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bde1f0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bde1f0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6ecf0 bytes c90200b4
+ 00bde1f0 bytes c90200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

