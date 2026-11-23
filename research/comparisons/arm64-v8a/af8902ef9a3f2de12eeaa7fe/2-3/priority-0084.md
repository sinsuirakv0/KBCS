# v16.0.0 → v16.0.1 · 最優先の変更候補 (84)

[一覧の目次](README.md)

<a id="compare-5eeb7e9952aef339bf26dcb82c10884c"></a>

### [`00bd5f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md) → [`00bd6344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6344.md) _ZN8firebase4auth11twittercred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd639c",
      "incomplete_value": true,
      "site": "00bd639c",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6378",
      "incomplete_value": true,
      "site": "00bd6384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd6358",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6378",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd639c",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6358",
      "READ",
      [
        "storage",
        "01126b10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6378",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd639c",
      "WRITE",
      [
        "storage",
        "01126b10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md#insn-00bd5f5c) · [`00bd5f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md#insn-00bd5f74) · [`00bd5f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md#insn-00bd5f30)
- 新版 `00bd6384`（命令位置の公開資料なし） · `00bd639c`（命令位置の公開資料なし） · `00bd6358`（命令位置の公開資料なし）

~~~diff
- 00bd5f5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5f5c ["INT_ADD", "register:40f0:8", ["const:bd5f5c:8", "const:4:8"]]
- 00bd5f5c ["CALLIND", null, ["register:0:8"]]
+ 00bd6384 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6384 ["INT_ADD", "register:40f0:8", ["const:bd6384:8", "const:4:8"]]
+ 00bd6384 ["CALLIND", null, ["register:0:8"]]
- 00bd5f5c bytes 00013fd6
+ 00bd6384 bytes 00013fd6
- 00bd5f74 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd5f74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:710:8"]]
- 00bd5f74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd639c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd639c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b10:8"]]
+ 00bd639c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd5f74 bytes a0421c39
+ 00bd639c bytes a0422c39
- 00bd5f30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:710:8"]]
- 00bd5f30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd5f30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd6358 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b10:8"]]
+ 00bd6358 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6358 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd5f30 bytes a8425c39
+ 00bd6358 bytes a8426c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2b3accd79a0f73951a580b0dce4db9"></a>

### [`00bd5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md) → [`00bd63b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd63b0.md) _ZN8firebase4auth11twittercred12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd63ec",
      "incomplete_value": true,
      "site": "00bd63ec",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd640c",
      "incomplete_value": true,
      "site": "00bd640c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd63c8",
      "incomplete_value": true,
      "site": "00bd63c8",
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
      "00bd63c4",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd63d0",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd63ec",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd63c4",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd63d0",
      "READ",
      [
        "storage",
        "01126b10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd63ec",
      "WRITE",
      [
        "storage",
        "01126b10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md#insn-00bd5fc4) · [`00bd5fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md#insn-00bd5fe0) · [`00bd5fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md#insn-00bd5fe4)
- 新版 `00bd63ec`（命令位置の公開資料なし） · `00bd6408`（命令位置の公開資料なし） · `00bd640c`（命令位置の公開資料なし）

~~~diff
- 00bd5fc4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd5fc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd5fc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:710:8"]]
- 00bd5fc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd63ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd63ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd63ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b10:8"]]
+ 00bd63ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd5fc4 bytes bf421c39
+ 00bd63ec bytes bf422c39
- 00bd5fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5fe0 ["INT_ADD", "register:40f0:8", ["const:bd5fe0:8", "const:4:8"]]
- 00bd5fe0 ["CALLIND", null, ["register:0:8"]]
+ 00bd6408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6408 ["INT_ADD", "register:40f0:8", ["const:bd6408:8", "const:4:8"]]
+ 00bd6408 ["CALLIND", null, ["register:0:8"]]
- 00bd5fe0 bytes 00013fd6
+ 00bd6408 bytes 00013fd6
- 00bd5fe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
- 00bd5fe4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd5fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd640c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b08:8"]]
+ 00bd640c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd5fe4 bytes 9f8603f9
+ 00bd640c bytes 9f8605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bd20f4dd16a57657d773546710e428a"></a>

### [`00bd5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md) → [`00bd6420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6420.md) _ZN8firebase4auth11twittercred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd6038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6460"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd600c",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6464"
      ]
    ],
    [
      "unmatched:00bd601c",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6434",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd643c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6464"
      ]
    ],
    [
      "00bd6444",
      "PARAM",
      [
        "storage",
        "002a1d18",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md#insn-00bd6014) · [`00bd6030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md#insn-00bd6030) · [`00bd6038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md#insn-00bd6038)
- 新版 `00bd6458`（命令位置の公開資料なし）

~~~diff
- 00bd6014 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6014 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6014 bytes 410100b5
- 00bd6030 ["INT_ADD", "register:40f0:8", ["const:bd6030:8", "const:4:8"]]
- 00bd6030 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6458 ["INT_ADD", "register:40f0:8", ["const:bd6458:8", "const:4:8"]]
+ 00bd6458 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6030 bytes b8120294
+ 00bd6458 bytes ae120294
- 00bd6038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
- 00bd6038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6038 bytes 808603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fb8af604c147a55f006436df35b7f23"></a>

### [`00bd60a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md) → [`00bd64cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd64cc.md) _ZN8firebase4auth11twittercred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd60a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd60a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd60a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd60a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd60a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd60b8",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd64cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd64d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd64e0",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd60a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md#insn-00bd60a4) · [`00bd60a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md#insn-00bd60a8) · [`00bd60c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md#insn-00bd60c0)

~~~diff
- 00bd60a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd60a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd60a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd60a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd60a4 bytes f44fbea9
- 00bd60a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd60a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd60a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd60a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd60a8 bytes fd7b01a9
- 00bd60c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd60c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd60c0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cede97d1a6dcc1472ab5af8d64d24723"></a>

### [`00bd61d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md) → [`00bd65f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65f8.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

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
      "site": "00bd61d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd61d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd61d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd61d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd61d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6608",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd65f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd65fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6608",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd61d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md#insn-00bd61d0) · [`00bd61d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md#insn-00bd61d4) · [`00bd61e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md#insn-00bd61e4)
- 新版 `00bd660c`（命令位置の公開資料なし）

~~~diff
- 00bd61d0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd61d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd61d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd61d0 bytes f30f1ef8
- 00bd61d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd61d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd61d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd61d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd61d4 bytes fd7b01a9
- 00bd61e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd61e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd660c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd660c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd61e4 bytes 080100b5
+ 00bd660c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a790cbdfb19f3f50879281c17c5b30a2"></a>

### [`00bd6214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md) → [`00bd663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd663c.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00bd6244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd666c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6228"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6224",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6228",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6670"
      ]
    ],
    [
      "unmatched:00bd6230",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd664c",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6670"
      ]
    ],
    [
      "00bd6658",
      "PARAM",
      [
        "storage",
        "002b9d48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md#insn-00bd6228) · [`00bd623c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md#insn-00bd623c) · [`00bd6244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md#insn-00bd6244)
- 新版 `00bd6664`（命令位置の公開資料なし）

~~~diff
- 00bd6228 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd6228 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6228 bytes 080100b5
- 00bd623c ["INT_ADD", "register:40f0:8", ["const:bd623c:8", "const:4:8"]]
- 00bd623c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6664 ["INT_ADD", "register:40f0:8", ["const:bd6664:8", "const:4:8"]]
+ 00bd6664 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd623c bytes 35120294
+ 00bd6664 bytes 2b120294
- 00bd6244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bd6244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6244 bytes 609603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82dbc56dd17df4ea42a587ab3e07e06f"></a>

### [`00bd62d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md) → [`00bd66f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd66f8.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 21.05% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd630c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6754",
      "incomplete_value": true,
      "site": "00bd6754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd632c",
      "incomplete_value": true,
      "site": "00bd632c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "site": "00bd6734"
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
      "00bd670c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6718",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6310"
      ]
    ]
  ],
  "added": [
    [
      "00bd670c",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6718",
      "READ",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd62e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md#insn-00bd62e8) · [`00bd630c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md#insn-00bd630c) · [`00bd6314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md#insn-00bd6314)
- 新版 `00bd6710`（命令位置の公開資料なし）

~~~diff
- 00bd62e8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd62e8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00bd6710 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd6710 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bd62e8 bytes 410200b4
+ 00bd6710 bytes 410200b4
- 00bd630c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd630c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd630c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:730:8"]]
- 00bd630c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd630c bytes bfc21c39
- 00bd6314 ["INT_ADD", "register:40f0:8", ["const:bd6314:8", "const:4:8"]]
- 00bd6314 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd6314 bytes 13120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b70a6ce5f4683b5a018c880ef2341a"></a>

### [`00bd6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md) → [`00bd6768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6768.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bd6380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd67a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd635c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6354",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd635c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd67ac"
      ]
    ],
    [
      "unmatched:00bd6364",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd677c",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd67ac"
      ]
    ],
    [
      "00bd678c",
      "PARAM",
      [
        "storage",
        "002b9d48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd635c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md#insn-00bd635c) · [`00bd6378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md#insn-00bd6378) · [`00bd6380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md#insn-00bd6380)
- 新版 `00bd67a0`（命令位置の公開資料なし）

~~~diff
- 00bd635c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd635c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bd635c bytes 410100b5
- 00bd6378 ["INT_ADD", "register:40f0:8", ["const:bd6378:8", "const:4:8"]]
- 00bd6378 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd67a0 ["INT_ADD", "register:40f0:8", ["const:bd67a0:8", "const:4:8"]]
+ 00bd67a0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6378 bytes e6110294
+ 00bd67a0 bytes dc110294
- 00bd6380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bd6380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6380 bytes 809603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8a960f47531a78ac898219690273ee"></a>

### [`00bd63ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md) → [`00bd6814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6814.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd642c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6854"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6400",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6858"
      ]
    ],
    [
      "unmatched:00bd6410",
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6828",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6858"
      ]
    ],
    [
      "00bd6838",
      "PARAM",
      [
        "storage",
        "002b9d48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md#insn-00bd6408) · [`00bd6424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md#insn-00bd6424) · [`00bd642c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md#insn-00bd642c)
- 新版 `00bd684c`（命令位置の公開資料なし）

~~~diff
- 00bd6408 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6408 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd6408 bytes 410100b5
- 00bd6424 ["INT_ADD", "register:40f0:8", ["const:bd6424:8", "const:4:8"]]
- 00bd6424 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd684c ["INT_ADD", "register:40f0:8", ["const:bd684c:8", "const:4:8"]]
+ 00bd684c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6424 bytes bb110294
+ 00bd684c bytes b1110294
- 00bd642c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bd642c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd642c bytes 809603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bf75f4505a5558b2eb2fb07c8262fbb"></a>

### [`00bd655c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md) → [`00bd6984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6984.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd655c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6560"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd655c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6560",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd656c",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6984",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6988",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6994",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd655c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md#insn-00bd655c) · [`00bd6560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md#insn-00bd6560) · [`00bd6570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md#insn-00bd6570)

~~~diff
- 00bd655c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd655c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd655c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd655c bytes f30f1ef8
- 00bd6560 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6560 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6560 bytes fd7b01a9
- 00bd6570 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd6570 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6570 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06303ce78aea074a03d517935e04cf4"></a>

### [`00bd6618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6618.md) → [`00bd6a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6a40.md) _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00bd6654"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6a9c",
      "incomplete_value": true,
      "site": "00bd6a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6674",
      "incomplete_value": true,
      "site": "00bd6674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:758:8"
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
      "site": "00bd6a7c"
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
      "00bd6a54",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6638",
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd6654",
      "WRITE",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6a54",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6a60",
      "READ",
      [
        "storage",
        "01126b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6a7c",
      "WRITE",
      [
        "storage",
        "01126b60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6618.md#insn-00bd6630) · [`00bd6654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6618.md#insn-00bd6654) · [`00bd6670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6618.md#insn-00bd6670)
- 新版 `00bd6a58`（命令位置の公開資料なし） · `00bd6a98`（命令位置の公開資料なし）

~~~diff
- 00bd6630 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6630 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bd6a58 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd6a58 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6630 bytes 410200b4
+ 00bd6a58 bytes 410200b4
- 00bd6654 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd6654 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd6654 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:760:8"]]
- 00bd6654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd6654 bytes bf821d39
- 00bd6670 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6670 ["INT_ADD", "register:40f0:8", ["const:bd6670:8", "const:4:8"]]
- 00bd6670 ["CALLIND", null, ["register:0:8"]]
+ 00bd6a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6a98 ["INT_ADD", "register:40f0:8", ["const:bd6a98:8", "const:4:8"]]
+ 00bd6a98 ["CALLIND", null, ["register:0:8"]]
- 00bd6670 bytes 00013fd6
+ 00bd6a98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad54d212c2cc25ed96355f526a3eb53"></a>

### [`00bd6688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md) → [`00bd6ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6ab0.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bd66c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6af0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd66a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd669c",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd66a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6af4"
      ]
    ],
    [
      "unmatched:00bd66ac",
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6ac4",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6af4"
      ]
    ],
    [
      "00bd6ad4",
      "PARAM",
      [
        "storage",
        "002b37ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd66a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md#insn-00bd66a4) · [`00bd66c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md#insn-00bd66c0) · [`00bd66c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md#insn-00bd66c8)
- 新版 `00bd6ae8`（命令位置の公開資料なし）

~~~diff
- 00bd66a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd66a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd66a4 bytes 410100b5
- 00bd66c0 ["INT_ADD", "register:40f0:8", ["const:bd66c0:8", "const:4:8"]]
- 00bd66c0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6ae8 ["INT_ADD", "register:40f0:8", ["const:bd6ae8:8", "const:4:8"]]
+ 00bd6ae8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd66c0 bytes 14110294
+ 00bd6ae8 bytes 0a110294
- 00bd66c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00bd66c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd66c8 bytes 80ae03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d744eefc6b35f1157ef9ba7b970cd11f"></a>

### [`00bd6734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md) → [`00bd6b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6b5c.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd6734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6738"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6734",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6738",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6748",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6b5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6b70",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md#insn-00bd6734) · [`00bd6738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md#insn-00bd6738) · [`00bd6750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md#insn-00bd6750)

~~~diff
- 00bd6734 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd6734 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd6734 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6734 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6734 bytes f44fbea9
- 00bd6738 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6738 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6738 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6738 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6738 bytes fd7b01a9
- 00bd6750 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6750 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6750 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e0bba02196c788e201e1b96f4ae12e"></a>

### [`00bd67e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md) → [`00bd6c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6c08.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd67e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd67e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd67e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd67e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd67e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6c18",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6c0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6c18",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd67e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md#insn-00bd67e0) · [`00bd67e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md#insn-00bd67e4) · [`00bd67f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md#insn-00bd67f4)
- 新版 `00bd6c1c`（命令位置の公開資料なし）

~~~diff
- 00bd67e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd67e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd67e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd67e0 bytes f30f1ef8
- 00bd67e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd67e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd67e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd67e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd67e4 bytes fd7b01a9
- 00bd67f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd67f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd6c1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd6c1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd67f4 bytes e80000b5
+ 00bd6c1c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce0dac7c65d9086d56c68fbef537720"></a>

### [`00bd6820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md) → [`00bd6c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6c48.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00bd6c74",
      "incomplete_value": true,
      "site": "00bd6c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd684c",
      "incomplete_value": true,
      "site": "00bd684c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6c5c",
      "incomplete_value": true,
      "site": "00bd6c5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6834",
      "incomplete_value": true,
      "site": "00bd6834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6c64",
      "incomplete_value": false,
      "site": "00bd6c6c",
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
            "const:d31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd683c",
      "incomplete_value": false,
      "site": "00bd6844",
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6c58",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c64",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6c74",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6c58",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6c64",
      "PARAM",
      [
        "storage",
        "0029fd31",
        null,
        "string"
      ]
    ],
    [
      "00bd6c74",
      "WRITE",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md#insn-00bd6844) · [`00bd684c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md#insn-00bd684c) · [`00bd6830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md#insn-00bd6830)
- 新版 `00bd6c6c`（命令位置の公開資料なし） · `00bd6c74`（命令位置の公開資料なし） · `00bd6c58`（命令位置の公開資料なし）

~~~diff
- 00bd6844 ["INT_ADD", "register:40f0:8", ["const:bd6844:8", "const:4:8"]]
- 00bd6844 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6c6c ["INT_ADD", "register:40f0:8", ["const:bd6c6c:8", "const:4:8"]]
+ 00bd6c6c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6844 bytes b3100294
+ 00bd6c6c bytes a9100294
- 00bd684c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd684c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6c74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6c74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd684c bytes 60be03f9
+ 00bd6c74 bytes 60be05f9
- 00bd6830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd6830 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6c58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6c58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6830 bytes 68be43f9
+ 00bd6c58 bytes 68be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e9e37f3ffc68c0adc17193e58317d30"></a>

### [`00bd6860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md) → [`00bd6c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6c88.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6cb8",
      "incomplete_value": true,
      "site": "00bd6cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6c9c",
      "incomplete_value": true,
      "site": "00bd6c9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6ca8",
      "incomplete_value": false,
      "site": "00bd6cb0",
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
            "const:d31:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6c98",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ca8",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6cb8",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6c98",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ca8",
      "PARAM",
      [
        "storage",
        "0029fd31",
        null,
        "string"
      ]
    ],
    [
      "00bd6cb8",
      "WRITE",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md#insn-00bd6888) · [`00bd6890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md#insn-00bd6890) · [`00bd6870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md#insn-00bd6870)
- 新版 `00bd6cb0`（命令位置の公開資料なし） · `00bd6cb8`（命令位置の公開資料なし） · `00bd6c98`（命令位置の公開資料なし）

~~~diff
- 00bd6888 ["INT_ADD", "register:40f0:8", ["const:bd6888:8", "const:4:8"]]
- 00bd6888 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6cb0 ["INT_ADD", "register:40f0:8", ["const:bd6cb0:8", "const:4:8"]]
+ 00bd6cb0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6888 bytes a2100294
+ 00bd6cb0 bytes 98100294
- 00bd6890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd6890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6cb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6890 bytes 60be03f9
+ 00bd6cb8 bytes 60be05f9
- 00bd6870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd6870 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6870 bytes 68be43f9
+ 00bd6c98 bytes 68be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7fd1e5b4b700a1e480919943ac04df4"></a>

### [`00bd68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md) → [`00bd6ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6ccc.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6cfc",
      "incomplete_value": true,
      "site": "00bd6cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6ce0",
      "incomplete_value": true,
      "site": "00bd6ce0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6ce8",
      "incomplete_value": false,
      "site": "00bd6cf4",
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
            "const:d31:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6cdc",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ce8",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6cfc",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6cdc",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ce8",
      "PARAM",
      [
        "storage",
        "0029fd31",
        null,
        "string"
      ]
    ],
    [
      "00bd6cfc",
      "WRITE",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd68cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md#insn-00bd68cc) · [`00bd68d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md#insn-00bd68d4) · [`00bd68b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md#insn-00bd68b4)
- 新版 `00bd6cf4`（命令位置の公開資料なし） · `00bd6cfc`（命令位置の公開資料なし） · `00bd6cdc`（命令位置の公開資料なし）

~~~diff
- 00bd68cc ["INT_ADD", "register:40f0:8", ["const:bd68cc:8", "const:4:8"]]
- 00bd68cc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6cf4 ["INT_ADD", "register:40f0:8", ["const:bd6cf4:8", "const:4:8"]]
+ 00bd6cf4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd68cc bytes 91100294
+ 00bd6cf4 bytes 87100294
- 00bd68d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd68d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6cfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd68d4 bytes 60be03f9
+ 00bd6cfc bytes 60be05f9
- 00bd68b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00bd68b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00bd6cdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd68b4 bytes 68be43f9
+ 00bd6cdc bytes 68be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56cad558d019ed5d17508f6346473c65"></a>

### [`00bd68f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md) → [`00bd6d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6d1c.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd6d74",
      "incomplete_value": true,
      "site": "00bd6d74",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6d50",
      "incomplete_value": true,
      "site": "00bd6d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd6d30",
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6d50",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6d74",
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d30",
      "READ",
      [
        "storage",
        "01126b80",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6d50",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6d74",
      "WRITE",
      [
        "storage",
        "01126b80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md#insn-00bd6934) · [`00bd694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md#insn-00bd694c) · [`00bd6908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md#insn-00bd6908)
- 新版 `00bd6d5c`（命令位置の公開資料なし） · `00bd6d74`（命令位置の公開資料なし） · `00bd6d30`（命令位置の公開資料なし）

~~~diff
- 00bd6934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6934 ["INT_ADD", "register:40f0:8", ["const:bd6934:8", "const:4:8"]]
- 00bd6934 ["CALLIND", null, ["register:0:8"]]
+ 00bd6d5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6d5c ["INT_ADD", "register:40f0:8", ["const:bd6d5c:8", "const:4:8"]]
+ 00bd6d5c ["CALLIND", null, ["register:0:8"]]
- 00bd6934 bytes 00013fd6
+ 00bd6d5c bytes 00013fd6
- 00bd694c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd694c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:780:8"]]
- 00bd694c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd6d74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd6d74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b80:8"]]
+ 00bd6d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd694c bytes a0021e39
+ 00bd6d74 bytes a0022e39
- 00bd6908 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:780:8"]]
- 00bd6908 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6908 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd6d30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b80:8"]]
+ 00bd6d30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6d30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd6908 bytes a8025e39
+ 00bd6d30 bytes a8026e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4665c357981e880f60daeb9ff8072d7e"></a>

### [`00bd6960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md) → [`00bd6d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6d88.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd6dc4",
      "incomplete_value": true,
      "site": "00bd6dc4",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6de4",
      "incomplete_value": true,
      "site": "00bd6de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6da0",
      "incomplete_value": true,
      "site": "00bd6da0",
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
      "00bd6d9c",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6da8",
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6dc4",
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d9c",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6da8",
      "READ",
      [
        "storage",
        "01126b80",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6dc4",
      "WRITE",
      [
        "storage",
        "01126b80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd699c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md#insn-00bd699c) · [`00bd69b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md#insn-00bd69b8) · [`00bd69bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md#insn-00bd69bc)
- 新版 `00bd6dc4`（命令位置の公開資料なし） · `00bd6de0`（命令位置の公開資料なし） · `00bd6de4`（命令位置の公開資料なし）

~~~diff
- 00bd699c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd699c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd699c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:780:8"]]
- 00bd699c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd6dc4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd6dc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd6dc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b80:8"]]
+ 00bd6dc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd699c bytes bf021e39
+ 00bd6dc4 bytes bf022e39
- 00bd69b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd69b8 ["INT_ADD", "register:40f0:8", ["const:bd69b8:8", "const:4:8"]]
- 00bd69b8 ["CALLIND", null, ["register:0:8"]]
+ 00bd6de0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd6de0 ["INT_ADD", "register:40f0:8", ["const:bd6de0:8", "const:4:8"]]
+ 00bd6de0 ["CALLIND", null, ["register:0:8"]]
- 00bd69b8 bytes 00013fd6
+ 00bd6de0 bytes 00013fd6
- 00bd69bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00bd69bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd69bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd6de4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b78:8"]]
+ 00bd6de4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd6de4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd69bc bytes 9fbe03f9
+ 00bd6de4 bytes 9fbe05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b35babfe0ac08d46ec444e63250a1e"></a>

### [`00bd69d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md) → [`00bd6df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6df8.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6e38",
      "incomplete_value": true,
      "site": "00bd6e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6e14",
      "incomplete_value": true,
      "site": "00bd6e14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6e1c",
      "incomplete_value": false,
      "site": "00bd6e30",
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
            "const:d31:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6e0c",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6e1c",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6e38",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e0c",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6e1c",
      "PARAM",
      [
        "storage",
        "0029fd31",
        null,
        "string"
      ]
    ],
    [
      "00bd6e38",
      "WRITE",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md#insn-00bd6a08) · [`00bd6a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md#insn-00bd6a10) · [`00bd69e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md#insn-00bd69e4)
- 新版 `00bd6e30`（命令位置の公開資料なし） · `00bd6e38`（命令位置の公開資料なし） · `00bd6e0c`（命令位置の公開資料なし）

~~~diff
- 00bd6a08 ["INT_ADD", "register:40f0:8", ["const:bd6a08:8", "const:4:8"]]
- 00bd6a08 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6e30 ["INT_ADD", "register:40f0:8", ["const:bd6e30:8", "const:4:8"]]
+ 00bd6e30 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6a08 bytes 42100294
+ 00bd6e30 bytes 38100294
- 00bd6a10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00bd6a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6e38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b78:8"]]
+ 00bd6e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6a10 bytes 80be03f9
+ 00bd6e38 bytes 80be05f9
- 00bd69e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00bd69e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6e0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b78:8"]]
+ 00bd6e0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd69e4 bytes 81be43f9
+ 00bd6e0c bytes 81be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0b07dd500b5a72011e3445d3e5a313"></a>

### [`00bd6a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md) → [`00bd6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6e68.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6e84",
      "incomplete_value": false,
      "site": "00bd6e88",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd6e94",
      "incomplete_value": true,
      "site": "00bd6ea0",
      "value": [
        "LOAD",
        "8",
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
      "00bd6e84",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd6e94",
      "DATA",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e84",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd6e94",
      "DATA",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md#insn-00bd6a60) · [`00bd6a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md#insn-00bd6a5c) · [`00bd6a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md#insn-00bd6a68)
- 新版 `00bd6e88`（命令位置の公開資料なし） · `00bd6e84`（命令位置の公開資料なし） · `00bd6e90`（命令位置の公開資料なし）

~~~diff
- 00bd6a60 ["INT_ADD", "register:40f0:8", ["const:bd6a60:8", "const:4:8"]]
- 00bd6a60 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd6e88 ["INT_ADD", "register:40f0:8", ["const:bd6e88:8", "const:4:8"]]
+ 00bd6e88 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6a60 bytes 68100294
+ 00bd6e88 bytes 5e100294
- 00bd6a5c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd6a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e84 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd6e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd6a5c bytes 00680a91
+ 00bd6e84 bytes 009c0d91
- 00bd6a68 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00bd6a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd6e90 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00bd6e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd6e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd6e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd6a68 bytes 08211e91
+ 00bd6e90 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f27e6e1bc0b91a032ff8cb15a527cb"></a>

### [`00bd6a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md) → [`00bd6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6ea4.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6ee4",
      "incomplete_value": true,
      "site": "00bd6ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6ec0",
      "incomplete_value": true,
      "site": "00bd6ec0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6ec8",
      "incomplete_value": false,
      "site": "00bd6edc",
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
            "const:d31:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6eb8",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ec8",
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      "00bd6ee4",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6eb8",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ec8",
      "PARAM",
      [
        "storage",
        "0029fd31",
        null,
        "string"
      ]
    ],
    [
      "00bd6ee4",
      "WRITE",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md#insn-00bd6ab4) · [`00bd6abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md#insn-00bd6abc) · [`00bd6a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md#insn-00bd6a90)
- 新版 `00bd6edc`（命令位置の公開資料なし） · `00bd6ee4`（命令位置の公開資料なし） · `00bd6eb8`（命令位置の公開資料なし）

~~~diff
- 00bd6ab4 ["INT_ADD", "register:40f0:8", ["const:bd6ab4:8", "const:4:8"]]
- 00bd6ab4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6edc ["INT_ADD", "register:40f0:8", ["const:bd6edc:8", "const:4:8"]]
+ 00bd6edc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6ab4 bytes 17100294
+ 00bd6edc bytes 0d100294
- 00bd6abc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00bd6abc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6ee4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b78:8"]]
+ 00bd6ee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6abc bytes 80be03f9
+ 00bd6ee4 bytes 80be05f9
- 00bd6a90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00bd6a90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6eb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b78:8"]]
+ 00bd6eb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6a90 bytes 81be43f9
+ 00bd6eb8 bytes 81be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3cd71f368de0ca360ecb6027e8120ef"></a>

### [`00bd6b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md) → [`00bd6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f50.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6f7c",
      "incomplete_value": true,
      "site": "00bd6f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6f64",
      "incomplete_value": true,
      "site": "00bd6f64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6f70",
      "incomplete_value": false,
      "site": "00bd6f74",
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
            "const:d49:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6f60",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f70",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6f7c",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6f60",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6f70",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ],
    [
      "00bd6f7c",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md#insn-00bd6b4c) · [`00bd6b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md#insn-00bd6b54) · [`00bd6b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md#insn-00bd6b38)
- 新版 `00bd6f74`（命令位置の公開資料なし） · `00bd6f7c`（命令位置の公開資料なし） · `00bd6f60`（命令位置の公開資料なし）

~~~diff
- 00bd6b4c ["INT_ADD", "register:40f0:8", ["const:bd6b4c:8", "const:4:8"]]
- 00bd6b4c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6f74 ["INT_ADD", "register:40f0:8", ["const:bd6f74:8", "const:4:8"]]
+ 00bd6f74 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6b4c bytes f10f0294
+ 00bd6f74 bytes e70f0294
- 00bd6b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6f7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd6f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6b54 bytes 60ea03f9
+ 00bd6f7c bytes 60ea05f9
- 00bd6b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6b38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6f60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd6f60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6b38 bytes 68ea43f9
+ 00bd6f60 bytes 68ea45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b996ddf5030673d43501db6bcef706c"></a>

### [`00bd6b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md) → [`00bd6f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f90.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6fbc",
      "incomplete_value": true,
      "site": "00bd6fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6fa4",
      "incomplete_value": true,
      "site": "00bd6fa4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6fac",
      "incomplete_value": false,
      "site": "00bd6fb4",
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
            "const:d49:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6fa0",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6fac",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd6fbc",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6fa0",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6fac",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ],
    [
      "00bd6fbc",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md#insn-00bd6b8c) · [`00bd6b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md#insn-00bd6b94) · [`00bd6b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md#insn-00bd6b78)
- 新版 `00bd6fb4`（命令位置の公開資料なし） · `00bd6fbc`（命令位置の公開資料なし） · `00bd6fa0`（命令位置の公開資料なし）

~~~diff
- 00bd6b8c ["INT_ADD", "register:40f0:8", ["const:bd6b8c:8", "const:4:8"]]
- 00bd6b8c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6fb4 ["INT_ADD", "register:40f0:8", ["const:bd6fb4:8", "const:4:8"]]
+ 00bd6fb4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6b8c bytes e10f0294
+ 00bd6fb4 bytes d70f0294
- 00bd6b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6fbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd6fbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6b94 bytes 60ea03f9
+ 00bd6fbc bytes 60ea05f9
- 00bd6b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6b78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6fa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd6fa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6b78 bytes 68ea43f9
+ 00bd6fa0 bytes 68ea45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4a92746b26d3f2a2df9dee9a560ba8"></a>

### [`00bd6ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md) → [`00bd6fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6fd0.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7000",
      "incomplete_value": true,
      "site": "00bd7000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6fe4",
      "incomplete_value": true,
      "site": "00bd6fe4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6ff0",
      "incomplete_value": false,
      "site": "00bd6ff8",
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
            "const:d49:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6fe0",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ff0",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd7000",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6fe0",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6ff0",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ],
    [
      "00bd7000",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md#insn-00bd6bd0) · [`00bd6bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md#insn-00bd6bd8) · [`00bd6bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md#insn-00bd6bb8)
- 新版 `00bd6ff8`（命令位置の公開資料なし） · `00bd7000`（命令位置の公開資料なし） · `00bd6fe0`（命令位置の公開資料なし）

~~~diff
- 00bd6bd0 ["INT_ADD", "register:40f0:8", ["const:bd6bd0:8", "const:4:8"]]
- 00bd6bd0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6ff8 ["INT_ADD", "register:40f0:8", ["const:bd6ff8:8", "const:4:8"]]
+ 00bd6ff8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6bd0 bytes d00f0294
+ 00bd6ff8 bytes c60f0294
- 00bd6bd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7000 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd7000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6bd8 bytes 60ea03f9
+ 00bd7000 bytes 60ea05f9
- 00bd6bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6bb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd6fe0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6bb8 bytes 68ea43f9
+ 00bd6fe0 bytes 68ea45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b131a2c591c004c9c937d83f4a8a989"></a>

### [`00bd6bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md) → [`00bd7014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7014.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7044",
      "incomplete_value": true,
      "site": "00bd7044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7028",
      "incomplete_value": true,
      "site": "00bd7028",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7030",
      "incomplete_value": false,
      "site": "00bd703c",
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
            "const:d49:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7024",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7030",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd7044",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7024",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7030",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ],
    [
      "00bd7044",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md#insn-00bd6c14) · [`00bd6c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md#insn-00bd6c1c) · [`00bd6bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md#insn-00bd6bfc)
- 新版 `00bd703c`（命令位置の公開資料なし） · `00bd7044`（命令位置の公開資料なし） · `00bd7024`（命令位置の公開資料なし）

~~~diff
- 00bd6c14 ["INT_ADD", "register:40f0:8", ["const:bd6c14:8", "const:4:8"]]
- 00bd6c14 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd703c ["INT_ADD", "register:40f0:8", ["const:bd703c:8", "const:4:8"]]
+ 00bd703c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6c14 bytes bf0f0294
+ 00bd703c bytes b50f0294
- 00bd6c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6c1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7044 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd7044 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6c1c bytes 60ea03f9
+ 00bd7044 bytes 60ea05f9
- 00bd6bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bd6bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bd7024 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6bfc bytes 68ea43f9
+ 00bd7024 bytes 68ea45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58dd716f7a2695d86a5e29e071f9349"></a>

### [`00bd6c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md) → [`00bd7064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7064.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd70bc",
      "incomplete_value": true,
      "site": "00bd70bc",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7098",
      "incomplete_value": true,
      "site": "00bd70a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7078",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7098",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd70bc",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7078",
      "READ",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7098",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd70bc",
      "WRITE",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md#insn-00bd6c7c) · [`00bd6c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md#insn-00bd6c94) · [`00bd6c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md#insn-00bd6c50)
- 新版 `00bd70a4`（命令位置の公開資料なし） · `00bd70bc`（命令位置の公開資料なし） · `00bd7078`（命令位置の公開資料なし）

~~~diff
- 00bd6c7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6c7c ["INT_ADD", "register:40f0:8", ["const:bd6c7c:8", "const:4:8"]]
- 00bd6c7c ["CALLIND", null, ["register:0:8"]]
+ 00bd70a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd70a4 ["INT_ADD", "register:40f0:8", ["const:bd70a4:8", "const:4:8"]]
+ 00bd70a4 ["CALLIND", null, ["register:0:8"]]
- 00bd6c7c bytes 00013fd6
+ 00bd70a4 bytes 00013fd6
- 00bd6c94 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd6c94 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
- 00bd6c94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd70bc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd70bc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bd8:8"]]
+ 00bd70bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd6c94 bytes a0621f39
+ 00bd70bc bytes a0622f39
- 00bd6c50 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
- 00bd6c50 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6c50 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd7078 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bd8:8"]]
+ 00bd7078 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7078 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd6c50 bytes a8625f39
+ 00bd7078 bytes a8626f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddef83b93824ffe846e82d6a3e4ca3b5"></a>

### [`00bd6ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md) → [`00bd70d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd70d0.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd710c",
      "incomplete_value": true,
      "site": "00bd710c",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd712c",
      "incomplete_value": true,
      "site": "00bd712c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd70e8",
      "incomplete_value": true,
      "site": "00bd70e8",
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
      "00bd70e4",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd70f0",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd710c",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd70e4",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd70f0",
      "READ",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd710c",
      "WRITE",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md#insn-00bd6ce4) · [`00bd6d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md#insn-00bd6d00) · [`00bd6d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md#insn-00bd6d04)
- 新版 `00bd710c`（命令位置の公開資料なし） · `00bd7128`（命令位置の公開資料なし） · `00bd712c`（命令位置の公開資料なし）

~~~diff
- 00bd6ce4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd6ce4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd6ce4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d8:8"]]
- 00bd6ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd710c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd710c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd710c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bd8:8"]]
+ 00bd710c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd6ce4 bytes bf621f39
+ 00bd710c bytes bf622f39
- 00bd6d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6d00 ["INT_ADD", "register:40f0:8", ["const:bd6d00:8", "const:4:8"]]
- 00bd6d00 ["CALLIND", null, ["register:0:8"]]
+ 00bd7128 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7128 ["INT_ADD", "register:40f0:8", ["const:bd7128:8", "const:4:8"]]
+ 00bd7128 ["CALLIND", null, ["register:0:8"]]
- 00bd6d00 bytes 00013fd6
+ 00bd7128 bytes 00013fd6
- 00bd6d04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bd6d04 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd6d04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd712c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00bd712c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd712c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd6d04 bytes 9fea03f9
+ 00bd712c bytes 9fea05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf7b51601ab0f8e61a83320778bf2781"></a>

### [`00bd6d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md) → [`00bd7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7140.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bd6d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7180"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6d34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6d2c",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7184"
      ]
    ],
    [
      "unmatched:00bd6d3c",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7154",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd715c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7184"
      ]
    ],
    [
      "00bd7164",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md#insn-00bd6d34) · [`00bd6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md#insn-00bd6d50) · [`00bd6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md#insn-00bd6d58)
- 新版 `00bd7178`（命令位置の公開資料なし）

~~~diff
- 00bd6d34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6d34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6d34 bytes 410100b5
- 00bd6d50 ["INT_ADD", "register:40f0:8", ["const:bd6d50:8", "const:4:8"]]
- 00bd6d50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7178 ["INT_ADD", "register:40f0:8", ["const:bd7178:8", "const:4:8"]]
+ 00bd7178 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6d50 bytes 700f0294
+ 00bd7178 bytes 660f0294
- 00bd6d58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bd6d58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6d58 bytes 80ea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd63d0703ae44483ffc4358d625160a8"></a>

### [`00bd6d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md) → [`00bd71b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd71b0.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd71cc",
      "incomplete_value": false,
      "site": "00bd71d0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd71dc",
      "incomplete_value": true,
      "site": "00bd71e8",
      "value": [
        "LOAD",
        "8",
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
      "00bd71cc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd71dc",
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd71cc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd71dc",
      "DATA",
      [
        "storage",
        "01126be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md#insn-00bd6da8) · [`00bd6da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md#insn-00bd6da4) · [`00bd6db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md#insn-00bd6db0)
- 新版 `00bd71d0`（命令位置の公開資料なし） · `00bd71cc`（命令位置の公開資料なし） · `00bd71d8`（命令位置の公開資料なし）

~~~diff
- 00bd6da8 ["INT_ADD", "register:40f0:8", ["const:bd6da8:8", "const:4:8"]]
- 00bd6da8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd71d0 ["INT_ADD", "register:40f0:8", ["const:bd71d0:8", "const:4:8"]]
+ 00bd71d0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6da8 bytes 960f0294
+ 00bd71d0 bytes 8c0f0294
- 00bd6da4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd6da4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6da4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6da4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd71cc ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd71cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd71cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd71cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd6da4 bytes 00680a91
+ 00bd71cc bytes 009c0d91
- 00bd6db0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00bd6db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd71d8 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00bd71d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd71d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd71d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd6db0 bytes 08811f91
+ 00bd71d8 bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369930a7ce506a3b9b23c76c863d84e3"></a>

### [`00bd6dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md) → [`00bd71ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd71ec.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd722c",
      "incomplete_value": true,
      "site": "00bd722c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7208",
      "incomplete_value": true,
      "site": "00bd7208",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7210",
      "incomplete_value": false,
      "site": "00bd7224",
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
            "const:d49:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7200",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7210",
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      "00bd722c",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7200",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7210",
      "PARAM",
      [
        "storage",
        "002a1d49",
        null,
        "string"
      ]
    ],
    [
      "00bd722c",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md#insn-00bd6dfc) · [`00bd6e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md#insn-00bd6e04) · [`00bd6dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md#insn-00bd6dd8)
- 新版 `00bd7224`（命令位置の公開資料なし） · `00bd722c`（命令位置の公開資料なし） · `00bd7200`（命令位置の公開資料なし）

~~~diff
- 00bd6dfc ["INT_ADD", "register:40f0:8", ["const:bd6dfc:8", "const:4:8"]]
- 00bd6dfc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7224 ["INT_ADD", "register:40f0:8", ["const:bd7224:8", "const:4:8"]]
+ 00bd7224 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6dfc bytes 450f0294
+ 00bd7224 bytes 3b0f0294
- 00bd6e04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bd6e04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd722c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00bd722c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6e04 bytes 80ea03f9
+ 00bd722c bytes 80ea05f9
- 00bd6dd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bd6dd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7200 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00bd7200 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6dd8 bytes 81ea43f9
+ 00bd7200 bytes 81ea45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13b9d6706effb1109082130195a6cc88"></a>

### [`00bd6e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md) → [`00bd725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd725c.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd7278",
      "incomplete_value": false,
      "site": "00bd727c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd7288",
      "incomplete_value": true,
      "site": "00bd7294",
      "value": [
        "LOAD",
        "8",
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
      "00bd7278",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd7288",
      "DATA",
      [
        "storage",
        "011267f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7278",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd7288",
      "DATA",
      [
        "storage",
        "01126bf8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md#insn-00bd6e54) · [`00bd6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md#insn-00bd6e50) · [`00bd6e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md#insn-00bd6e5c)
- 新版 `00bd727c`（命令位置の公開資料なし） · `00bd7278`（命令位置の公開資料なし） · `00bd7284`（命令位置の公開資料なし）

~~~diff
- 00bd6e54 ["INT_ADD", "register:40f0:8", ["const:bd6e54:8", "const:4:8"]]
- 00bd6e54 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd727c ["INT_ADD", "register:40f0:8", ["const:bd727c:8", "const:4:8"]]
+ 00bd727c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6e54 bytes 6b0f0294
+ 00bd727c bytes 610f0294
- 00bd6e50 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd6e50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6e50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6e50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7278 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd7278 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7278 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7278 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd6e50 bytes 00441191
+ 00bd7278 bytes 00781491
- 00bd6e5c ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00bd6e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd6e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7284 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00bd7284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd6e5c bytes 08e11f91
+ 00bd7284 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620f8472b2e4e9d53e8bbfa283fc5edd"></a>

### [`00bd6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md) → [`00bd7298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7298.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd72c4",
      "incomplete_value": true,
      "site": "00bd72c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd72ac",
      "incomplete_value": true,
      "site": "00bd72ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd72b8",
      "incomplete_value": false,
      "site": "00bd72bc",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd72a8",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd72b8",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd72c4",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd72a8",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd72b8",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd72c4",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md#insn-00bd6e94) · [`00bd6e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md#insn-00bd6e9c) · [`00bd6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md#insn-00bd6e80)
- 新版 `00bd72bc`（命令位置の公開資料なし） · `00bd72c4`（命令位置の公開資料なし） · `00bd72a8`（命令位置の公開資料なし）

~~~diff
- 00bd6e94 ["INT_ADD", "register:40f0:8", ["const:bd6e94:8", "const:4:8"]]
- 00bd6e94 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd72bc ["INT_ADD", "register:40f0:8", ["const:bd72bc:8", "const:4:8"]]
+ 00bd72bc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6e94 bytes 1f0f0294
+ 00bd72bc bytes 150f0294
- 00bd6e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd72c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd72c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6e9c bytes 600204f9
+ 00bd72c4 bytes 600206f9
- 00bd6e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd72a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd72a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6e80 bytes 680244f9
+ 00bd72a8 bytes 680246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c60aa8aff0df985ff15d4526a97b0504"></a>

### [`00bd6eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md) → [`00bd72d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd72d8.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd7304",
      "incomplete_value": true,
      "site": "00bd7304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd72ec",
      "incomplete_value": true,
      "site": "00bd72ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd72f4",
      "incomplete_value": false,
      "site": "00bd72fc",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd72e8",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd72f4",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd7304",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd72e8",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd72f4",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd7304",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md#insn-00bd6ed4) · [`00bd6edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md#insn-00bd6edc) · [`00bd6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md#insn-00bd6ec0)
- 新版 `00bd72fc`（命令位置の公開資料なし） · `00bd7304`（命令位置の公開資料なし） · `00bd72e8`（命令位置の公開資料なし）

~~~diff
- 00bd6ed4 ["INT_ADD", "register:40f0:8", ["const:bd6ed4:8", "const:4:8"]]
- 00bd6ed4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd72fc ["INT_ADD", "register:40f0:8", ["const:bd72fc:8", "const:4:8"]]
+ 00bd72fc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6ed4 bytes 0f0f0294
+ 00bd72fc bytes 050f0294
- 00bd6edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd7304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6edc bytes 600204f9
+ 00bd7304 bytes 600206f9
- 00bd6ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd72e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd72e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6ec0 bytes 680244f9
+ 00bd72e8 bytes 680246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6156286994a9039af84fbee2cb8fdb"></a>

### [`00bd6ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md) → [`00bd7318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7318.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7348",
      "incomplete_value": true,
      "site": "00bd7348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd732c",
      "incomplete_value": true,
      "site": "00bd732c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7338",
      "incomplete_value": false,
      "site": "00bd7340",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7328",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7338",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd7348",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7328",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7338",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd7348",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md#insn-00bd6f18) · [`00bd6f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md#insn-00bd6f20) · [`00bd6f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md#insn-00bd6f00)
- 新版 `00bd7340`（命令位置の公開資料なし） · `00bd7348`（命令位置の公開資料なし） · `00bd7328`（命令位置の公開資料なし）

~~~diff
- 00bd6f18 ["INT_ADD", "register:40f0:8", ["const:bd6f18:8", "const:4:8"]]
- 00bd6f18 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7340 ["INT_ADD", "register:40f0:8", ["const:bd7340:8", "const:4:8"]]
+ 00bd7340 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6f18 bytes fe0e0294
+ 00bd7340 bytes f40e0294
- 00bd6f20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7348 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd7348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6f20 bytes 600204f9
+ 00bd7348 bytes 600206f9
- 00bd6f00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6f00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd7328 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6f00 bytes 680244f9
+ 00bd7328 bytes 680246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b9a294cd6195fd4e90e88daf9c892e"></a>

### [`00bd6f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f34.md) → [`00bd735c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd735c.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd738c",
      "incomplete_value": true,
      "site": "00bd738c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7370",
      "incomplete_value": true,
      "site": "00bd7370",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7378",
      "incomplete_value": false,
      "site": "00bd7384",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd736c",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7378",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd738c",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd736c",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7378",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd738c",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f34.md#insn-00bd6f5c) · [`00bd6f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f34.md#insn-00bd6f64) · [`00bd6f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f34.md#insn-00bd6f44)
- 新版 `00bd7384`（命令位置の公開資料なし） · `00bd738c`（命令位置の公開資料なし） · `00bd736c`（命令位置の公開資料なし）

~~~diff
- 00bd6f5c ["INT_ADD", "register:40f0:8", ["const:bd6f5c:8", "const:4:8"]]
- 00bd6f5c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7384 ["INT_ADD", "register:40f0:8", ["const:bd7384:8", "const:4:8"]]
+ 00bd7384 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6f5c bytes ed0e0294
+ 00bd7384 bytes e30e0294
- 00bd6f64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6f64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd738c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd738c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6f64 bytes 600204f9
+ 00bd738c bytes 600206f9
- 00bd6f44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00bd6f44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd736c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c00:8"]]
+ 00bd736c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6f44 bytes 680244f9
+ 00bd736c bytes 680246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f401a03c44391db6872f48f888289de4"></a>

### [`00bd6f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f84.md) → [`00bd73ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd73ac.md) _ZN8firebase4auth21oauthprovider_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd7404",
      "incomplete_value": true,
      "site": "00bd7404",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd73e0",
      "incomplete_value": true,
      "site": "00bd73ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd73c0",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd73e0",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7404",
      "WRITE",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd73c0",
      "READ",
      [
        "storage",
        "01126c08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd73e0",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7404",
      "WRITE",
      [
        "storage",
        "01126c08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f84.md#insn-00bd6fc4) · [`00bd6fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f84.md#insn-00bd6fdc) · [`00bd6f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6f84.md#insn-00bd6f98)
- 新版 `00bd73ec`（命令位置の公開資料なし） · `00bd7404`（命令位置の公開資料なし） · `00bd73c0`（命令位置の公開資料なし）

~~~diff
- 00bd6fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6fc4 ["INT_ADD", "register:40f0:8", ["const:bd6fc4:8", "const:4:8"]]
- 00bd6fc4 ["CALLIND", null, ["register:0:8"]]
+ 00bd73ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd73ec ["INT_ADD", "register:40f0:8", ["const:bd73ec:8", "const:4:8"]]
+ 00bd73ec ["CALLIND", null, ["register:0:8"]]
- 00bd6fc4 bytes 00013fd6
+ 00bd73ec bytes 00013fd6
- 00bd6fdc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd6fdc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:808:8"]]
- 00bd6fdc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd7404 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd7404 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c08:8"]]
+ 00bd7404 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd6fdc bytes a0222039
+ 00bd7404 bytes a0223039
- 00bd6f98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
- 00bd6f98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6f98 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd73c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c08:8"]]
+ 00bd73c0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd73c0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd6f98 bytes a8226039
+ 00bd73c0 bytes a8227039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a50b0558ccf45f9a4f42062a89842b"></a>

### [`00bd6ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ff0.md) → [`00bd7418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7418.md) _ZN8firebase4auth21oauthprovider_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd7454",
      "incomplete_value": true,
      "site": "00bd7454",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7474",
      "incomplete_value": true,
      "site": "00bd7474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7430",
      "incomplete_value": true,
      "site": "00bd7430",
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
      "00bd742c",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7438",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7454",
      "WRITE",
      [
        "storage",
        "01126808",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd742c",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7438",
      "READ",
      [
        "storage",
        "01126c08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7454",
      "WRITE",
      [
        "storage",
        "01126c08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd702c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ff0.md#insn-00bd702c) · [`00bd7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ff0.md#insn-00bd7048) · [`00bd704c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ff0.md#insn-00bd704c)
- 新版 `00bd7454`（命令位置の公開資料なし） · `00bd7470`（命令位置の公開資料なし） · `00bd7474`（命令位置の公開資料なし）

~~~diff
- 00bd702c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd702c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd702c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:808:8"]]
- 00bd702c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd7454 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd7454 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd7454 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c08:8"]]
+ 00bd7454 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd702c bytes bf222039
+ 00bd7454 bytes bf223039
- 00bd7048 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7048 ["INT_ADD", "register:40f0:8", ["const:bd7048:8", "const:4:8"]]
- 00bd7048 ["CALLIND", null, ["register:0:8"]]
+ 00bd7470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7470 ["INT_ADD", "register:40f0:8", ["const:bd7470:8", "const:4:8"]]
+ 00bd7470 ["CALLIND", null, ["register:0:8"]]
- 00bd7048 bytes 00013fd6
+ 00bd7470 bytes 00013fd6
- 00bd704c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00bd704c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd704c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd7474 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c00:8"]]
+ 00bd7474 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd7474 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd704c bytes 9f0204f9
+ 00bd7474 bytes 9f0206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5cc73b5d79e20a3f78e2ae55c5e87e"></a>

### [`00bd7060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7060.md) → [`00bd7488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7488.md) _ZN8firebase4auth21oauthprovider_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd74c8",
      "incomplete_value": true,
      "site": "00bd74c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd74a4",
      "incomplete_value": true,
      "site": "00bd74a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd74ac",
      "incomplete_value": false,
      "site": "00bd74c0",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd749c",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd74ac",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd74c8",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd749c",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd74ac",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd74c8",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7060.md#insn-00bd7098) · [`00bd70a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7060.md#insn-00bd70a0) · [`00bd7074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7060.md#insn-00bd7074)
- 新版 `00bd74c0`（命令位置の公開資料なし） · `00bd74c8`（命令位置の公開資料なし） · `00bd749c`（命令位置の公開資料なし）

~~~diff
- 00bd7098 ["INT_ADD", "register:40f0:8", ["const:bd7098:8", "const:4:8"]]
- 00bd7098 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd74c0 ["INT_ADD", "register:40f0:8", ["const:bd74c0:8", "const:4:8"]]
+ 00bd74c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7098 bytes 9e0e0294
+ 00bd74c0 bytes 940e0294
- 00bd70a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00bd70a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd74c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c00:8"]]
+ 00bd74c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd70a0 bytes 800204f9
+ 00bd74c8 bytes 800206f9
- 00bd7074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00bd7074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd749c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c00:8"]]
+ 00bd749c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7074 bytes 810244f9
+ 00bd749c bytes 810246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-616fedd01a0e60aee5f7d71acce34c84"></a>

### [`00bd70d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd70d0.md) → [`00bd74f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd74f8.md) _ZN8firebase4auth21oauthprovider_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd7514",
      "incomplete_value": false,
      "site": "00bd7518",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd7524",
      "incomplete_value": true,
      "site": "00bd7530",
      "value": [
        "LOAD",
        "8",
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
      "00bd7514",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd7524",
      "DATA",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7514",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd7524",
      "DATA",
      [
        "storage",
        "01126c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd70d0.md#insn-00bd70f0) · [`00bd70ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd70d0.md#insn-00bd70ec) · [`00bd70f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd70d0.md#insn-00bd70f8)
- 新版 `00bd7518`（命令位置の公開資料なし） · `00bd7514`（命令位置の公開資料なし） · `00bd7520`（命令位置の公開資料なし）

~~~diff
- 00bd70f0 ["INT_ADD", "register:40f0:8", ["const:bd70f0:8", "const:4:8"]]
- 00bd70f0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd7518 ["INT_ADD", "register:40f0:8", ["const:bd7518:8", "const:4:8"]]
+ 00bd7518 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd70f0 bytes c40e0294
+ 00bd7518 bytes ba0e0294
- 00bd70ec ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd70ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd70ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd70ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7514 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd7514 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7514 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7514 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd70ec bytes 00680a91
+ 00bd7514 bytes 009c0d91
- 00bd70f8 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00bd70f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd70f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd70f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7520 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00bd7520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd70f8 bytes 08412091
+ 00bd7520 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-898f99329bbdd01cedde2227db39d4b2"></a>

### [`00bd710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd710c.md) → [`00bd7534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7534.md) _ZN8firebase4auth21oauthprovider_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7574",
      "incomplete_value": true,
      "site": "00bd7574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7550",
      "incomplete_value": true,
      "site": "00bd7550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7558",
      "incomplete_value": false,
      "site": "00bd756c",
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
            "const:d1a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7548",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7558",
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      "00bd7574",
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7548",
      "READ",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7558",
      "PARAM",
      [
        "storage",
        "002c0d1a",
        null,
        "string"
      ]
    ],
    [
      "00bd7574",
      "WRITE",
      [
        "storage",
        "01126c00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd710c.md#insn-00bd7144) · [`00bd714c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd710c.md#insn-00bd714c) · [`00bd7120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd710c.md#insn-00bd7120)
- 新版 `00bd756c`（命令位置の公開資料なし） · `00bd7574`（命令位置の公開資料なし） · `00bd7548`（命令位置の公開資料なし）

~~~diff
- 00bd7144 ["INT_ADD", "register:40f0:8", ["const:bd7144:8", "const:4:8"]]
- 00bd7144 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd756c ["INT_ADD", "register:40f0:8", ["const:bd756c:8", "const:4:8"]]
+ 00bd756c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7144 bytes 730e0294
+ 00bd756c bytes 690e0294
- 00bd714c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00bd714c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c00:8"]]
+ 00bd7574 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd714c bytes 800204f9
+ 00bd7574 bytes 800206f9
- 00bd7120 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
- 00bd7120 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7548 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c00:8"]]
+ 00bd7548 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7120 bytes 810244f9
+ 00bd7548 bytes 810246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5433ee6b0b7dadb361a15683f90c8e92"></a>

### [`00bd717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd717c.md) → [`00bd75a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd75a4.md) _ZN8firebase4auth21oauthprovider_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd75c0",
      "incomplete_value": false,
      "site": "00bd75c4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd75d0",
      "incomplete_value": true,
      "site": "00bd75dc",
      "value": [
        "LOAD",
        "8",
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
      "00bd75c0",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd75d0",
      "DATA",
      [
        "storage",
        "01126828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd75c0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd75d0",
      "DATA",
      [
        "storage",
        "01126c28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd719c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd717c.md#insn-00bd719c) · [`00bd7198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd717c.md#insn-00bd7198) · [`00bd71a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd717c.md#insn-00bd71a4)
- 新版 `00bd75c4`（命令位置の公開資料なし） · `00bd75c0`（命令位置の公開資料なし） · `00bd75cc`（命令位置の公開資料なし）

~~~diff
- 00bd719c ["INT_ADD", "register:40f0:8", ["const:bd719c:8", "const:4:8"]]
- 00bd719c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd75c4 ["INT_ADD", "register:40f0:8", ["const:bd75c4:8", "const:4:8"]]
+ 00bd75c4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd719c bytes 990e0294
+ 00bd75c4 bytes 8f0e0294
- 00bd7198 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd7198 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7198 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7198 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd75c0 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd75c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd75c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd75c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd7198 bytes 00441191
+ 00bd75c0 bytes 00781491
- 00bd71a4 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00bd71a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd71a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd71a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd75cc ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00bd75cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd75cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd75cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd71a4 bytes 08a12091
+ 00bd75cc bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da2514a3a04091508ab9cf61a6eebfde"></a>

### [`00bd71b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71b8.md) → [`00bd75e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd75e0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bd760c",
      "incomplete_value": true,
      "site": "00bd760c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd75f4",
      "incomplete_value": true,
      "site": "00bd75f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7600",
      "incomplete_value": false,
      "site": "00bd7604",
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
            "const:213:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd75f0",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7600",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd760c",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd75f0",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7600",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ],
    [
      "00bd760c",
      "WRITE",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd71dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71b8.md#insn-00bd71dc) · [`00bd71e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71b8.md#insn-00bd71e4) · [`00bd71c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71b8.md#insn-00bd71c8)
- 新版 `00bd7604`（命令位置の公開資料なし） · `00bd760c`（命令位置の公開資料なし） · `00bd75f0`（命令位置の公開資料なし）

~~~diff
- 00bd71dc ["INT_ADD", "register:40f0:8", ["const:bd71dc:8", "const:4:8"]]
- 00bd71dc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7604 ["INT_ADD", "register:40f0:8", ["const:bd7604:8", "const:4:8"]]
+ 00bd7604 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd71dc bytes 4d0e0294
+ 00bd7604 bytes 430e0294
- 00bd71e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd71e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd760c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd760c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd71e4 bytes 601a04f9
+ 00bd760c bytes 601a06f9
- 00bd71c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd71c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd75f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd75f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd71c8 bytes 681a44f9
+ 00bd75f0 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ef7d81ee231acc5620ea80db5d6cc1"></a>

### [`00bd71f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71f8.md) → [`00bd7620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7620.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bd764c",
      "incomplete_value": true,
      "site": "00bd764c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7634",
      "incomplete_value": true,
      "site": "00bd7634",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd763c",
      "incomplete_value": false,
      "site": "00bd7644",
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
            "const:213:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7630",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd763c",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd764c",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7630",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd763c",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ],
    [
      "00bd764c",
      "WRITE",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71f8.md#insn-00bd721c) · [`00bd7224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71f8.md#insn-00bd7224) · [`00bd7208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd71f8.md#insn-00bd7208)
- 新版 `00bd7644`（命令位置の公開資料なし） · `00bd764c`（命令位置の公開資料なし） · `00bd7630`（命令位置の公開資料なし）

~~~diff
- 00bd721c ["INT_ADD", "register:40f0:8", ["const:bd721c:8", "const:4:8"]]
- 00bd721c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7644 ["INT_ADD", "register:40f0:8", ["const:bd7644:8", "const:4:8"]]
+ 00bd7644 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd721c bytes 3d0e0294
+ 00bd7644 bytes 330e0294
- 00bd7224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd7224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd764c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd764c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7224 bytes 601a04f9
+ 00bd764c bytes 601a06f9
- 00bd7208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd7208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7630 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd7630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7208 bytes 681a44f9
+ 00bd7630 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6b0e9ab00e93975c6d52a8bdfd85c73"></a>

### [`00bd7238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7238.md) → [`00bd7660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7660.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7690",
      "incomplete_value": true,
      "site": "00bd7690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7674",
      "incomplete_value": true,
      "site": "00bd7674",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7680",
      "incomplete_value": false,
      "site": "00bd7688",
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
            "const:213:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7670",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7680",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd7690",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7670",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7680",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ],
    [
      "00bd7690",
      "WRITE",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7238.md#insn-00bd7260) · [`00bd7268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7238.md#insn-00bd7268) · [`00bd7248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7238.md#insn-00bd7248)
- 新版 `00bd7688`（命令位置の公開資料なし） · `00bd7690`（命令位置の公開資料なし） · `00bd7670`（命令位置の公開資料なし）

~~~diff
- 00bd7260 ["INT_ADD", "register:40f0:8", ["const:bd7260:8", "const:4:8"]]
- 00bd7260 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7688 ["INT_ADD", "register:40f0:8", ["const:bd7688:8", "const:4:8"]]
+ 00bd7688 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7260 bytes 2c0e0294
+ 00bd7688 bytes 220e0294
- 00bd7268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd7268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7690 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd7690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7268 bytes 601a04f9
+ 00bd7690 bytes 601a06f9
- 00bd7248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd7248 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7670 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd7670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7248 bytes 681a44f9
+ 00bd7670 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34cdcff9958a5e4067b623c0d86b74e2"></a>

### [`00bd727c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd727c.md) → [`00bd76a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd76a4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd76d4",
      "incomplete_value": true,
      "site": "00bd76d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd76b8",
      "incomplete_value": true,
      "site": "00bd76b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd76c0",
      "incomplete_value": false,
      "site": "00bd76cc",
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
            "const:213:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd76b4",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd76c0",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd76d4",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd76b4",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd76c0",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ],
    [
      "00bd76d4",
      "WRITE",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd72a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd727c.md#insn-00bd72a4) · [`00bd72ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd727c.md#insn-00bd72ac) · [`00bd728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd727c.md#insn-00bd728c)
- 新版 `00bd76cc`（命令位置の公開資料なし） · `00bd76d4`（命令位置の公開資料なし） · `00bd76b4`（命令位置の公開資料なし）

~~~diff
- 00bd72a4 ["INT_ADD", "register:40f0:8", ["const:bd72a4:8", "const:4:8"]]
- 00bd72a4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd76cc ["INT_ADD", "register:40f0:8", ["const:bd76cc:8", "const:4:8"]]
+ 00bd76cc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd72a4 bytes 1b0e0294
+ 00bd76cc bytes 110e0294
- 00bd72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd76d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd76d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd72ac bytes 601a04f9
+ 00bd76d4 bytes 601a06f9
- 00bd728c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00bd728c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd76b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00bd76b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd728c bytes 681a44f9
+ 00bd76b4 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cada330270d42fbf1130933caec0b507"></a>

### [`00bd72cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd72cc.md) → [`00bd76f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd76f4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd774c",
      "incomplete_value": true,
      "site": "00bd774c",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7728",
      "incomplete_value": true,
      "site": "00bd7734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7708",
      "READ",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7728",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd774c",
      "WRITE",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7708",
      "READ",
      [
        "storage",
        "01126c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7728",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd774c",
      "WRITE",
      [
        "storage",
        "01126c38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd730c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd72cc.md#insn-00bd730c) · [`00bd7324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd72cc.md#insn-00bd7324) · [`00bd72e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd72cc.md#insn-00bd72e0)
- 新版 `00bd7734`（命令位置の公開資料なし） · `00bd774c`（命令位置の公開資料なし） · `00bd7708`（命令位置の公開資料なし）

~~~diff
- 00bd730c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd730c ["INT_ADD", "register:40f0:8", ["const:bd730c:8", "const:4:8"]]
- 00bd730c ["CALLIND", null, ["register:0:8"]]
+ 00bd7734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7734 ["INT_ADD", "register:40f0:8", ["const:bd7734:8", "const:4:8"]]
+ 00bd7734 ["CALLIND", null, ["register:0:8"]]
- 00bd730c bytes 00013fd6
+ 00bd7734 bytes 00013fd6
- 00bd7324 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd7324 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
- 00bd7324 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd774c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd774c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c38:8"]]
+ 00bd774c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd7324 bytes a0e22039
+ 00bd774c bytes a0e23039
- 00bd72e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
- 00bd72e0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd72e0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd7708 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c38:8"]]
+ 00bd7708 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7708 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd72e0 bytes a8e26039
+ 00bd7708 bytes a8e27039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77166eaa317d9566c0805343e63067be"></a>

### [`00bd7338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7338.md) → [`00bd7760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7760.md) _ZN8firebase4auth31oauthprovider_credentialbuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bd7374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd779c"
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
      "00bd7774",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7780",
      "READ",
      [
        "storage",
        "01126838",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7378"
      ]
    ]
  ],
  "added": [
    [
      "00bd7774",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7780",
      "READ",
      [
        "storage",
        "01126c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd77a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7338.md#insn-00bd7350) · [`00bd7374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7338.md#insn-00bd7374) · [`00bd737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7338.md#insn-00bd737c)
- 新版 `00bd7778`（命令位置の公開資料なし）

~~~diff
- 00bd7350 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd7350 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd7778 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd7778 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd7350 bytes 410200b4
+ 00bd7778 bytes 410200b4
- 00bd7374 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd7374 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd7374 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
- 00bd7374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd7374 bytes bfe22039
- 00bd737c ["INT_ADD", "register:40f0:8", ["const:bd737c:8", "const:4:8"]]
- 00bd737c ["CALL", null, ["callee:00c5af60:8"]]
- 00bd737c bytes f90d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c6f4309fe4fc1147f9ab854728fcc8"></a>

### [`00bd73a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd73a8.md) → [`00bd77d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd77d0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd73e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7810"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd73c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd73bc",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd73c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7814"
      ]
    ],
    [
      "unmatched:00bd73cc",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd77e4",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd77ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7814"
      ]
    ],
    [
      "00bd77f4",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd73c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd73a8.md#insn-00bd73c4) · [`00bd73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd73a8.md#insn-00bd73e0) · [`00bd73e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd73a8.md#insn-00bd73e8)
- 新版 `00bd7808`（命令位置の公開資料なし）

~~~diff
- 00bd73c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd73c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd73c4 bytes 410100b5
- 00bd73e0 ["INT_ADD", "register:40f0:8", ["const:bd73e0:8", "const:4:8"]]
- 00bd73e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7808 ["INT_ADD", "register:40f0:8", ["const:bd7808:8", "const:4:8"]]
+ 00bd7808 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd73e0 bytes cc0d0294
+ 00bd7808 bytes c20d0294
- 00bd73e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00bd73e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd73e8 bytes 801a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feea9d98f9d800e82979ccdd4d5cc106"></a>

### [`00bd7418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7418.md) → [`00bd7840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7840.md) _ZN8firebase4auth31oauthprovider_credentialbuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd785c",
      "incomplete_value": false,
      "site": "00bd7860",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd786c",
      "incomplete_value": true,
      "site": "00bd7878",
      "value": [
        "LOAD",
        "8",
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
      "00bd785c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd786c",
      "DATA",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd785c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd786c",
      "DATA",
      [
        "storage",
        "01126c40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7418.md#insn-00bd7438) · [`00bd7434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7418.md#insn-00bd7434) · [`00bd7440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7418.md#insn-00bd7440)
- 新版 `00bd7860`（命令位置の公開資料なし） · `00bd785c`（命令位置の公開資料なし） · `00bd7868`（命令位置の公開資料なし）

~~~diff
- 00bd7438 ["INT_ADD", "register:40f0:8", ["const:bd7438:8", "const:4:8"]]
- 00bd7438 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd7860 ["INT_ADD", "register:40f0:8", ["const:bd7860:8", "const:4:8"]]
+ 00bd7860 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd7438 bytes f20d0294
+ 00bd7860 bytes e80d0294
- 00bd7434 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd7434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd785c ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd785c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd785c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd785c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd7434 bytes 00680a91
+ 00bd785c bytes 009c0d91
- 00bd7440 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00bd7440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7868 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00bd7868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd7440 bytes 08012191
+ 00bd7868 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4981993a7a8df0a5d9e28f98ca58e38e"></a>

### [`00bd7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7454.md) → [`00bd787c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd787c.md) _ZN8firebase4auth31oauthprovider_credentialbuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd78bc",
      "incomplete_value": true,
      "site": "00bd78bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7898",
      "incomplete_value": true,
      "site": "00bd7898",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd78a0",
      "incomplete_value": false,
      "site": "00bd78b4",
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
            "const:213:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7890",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78a0",
      "PARAM",
      [
        "storage",
        "002bc1d3",
        null,
        "string"
      ]
    ],
    [
      "00bd78bc",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7890",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd78a0",
      "PARAM",
      [
        "storage",
        "002bc213",
        null,
        "string"
      ]
    ],
    [
      "00bd78bc",
      "WRITE",
      [
        "storage",
        "01126c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd748c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7454.md#insn-00bd748c) · [`00bd7494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7454.md#insn-00bd7494) · [`00bd7468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7454.md#insn-00bd7468)
- 新版 `00bd78b4`（命令位置の公開資料なし） · `00bd78bc`（命令位置の公開資料なし） · `00bd7890`（命令位置の公開資料なし）

~~~diff
- 00bd748c ["INT_ADD", "register:40f0:8", ["const:bd748c:8", "const:4:8"]]
- 00bd748c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd78b4 ["INT_ADD", "register:40f0:8", ["const:bd78b4:8", "const:4:8"]]
+ 00bd78b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd748c bytes a10d0294
+ 00bd78b4 bytes 970d0294
- 00bd7494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00bd7494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd78bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00bd78bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7494 bytes 801a04f9
+ 00bd78bc bytes 801a06f9
- 00bd7468 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00bd7468 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7890 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00bd7890 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7468 bytes 811a44f9
+ 00bd7890 bytes 811a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6344ea4001319eed8e108a2df4dac5"></a>

### [`00bd74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd74c4.md) → [`00bd78ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd78ec.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd7908",
      "incomplete_value": false,
      "site": "00bd790c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd7918",
      "incomplete_value": true,
      "site": "00bd7924",
      "value": [
        "LOAD",
        "8",
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
      "00bd7908",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd7918",
      "DATA",
      [
        "storage",
        "01126860",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7908",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd7918",
      "DATA",
      [
        "storage",
        "01126c60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd74e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd74c4.md#insn-00bd74e4) · [`00bd74e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd74c4.md#insn-00bd74e0) · [`00bd74ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd74c4.md#insn-00bd74ec)
- 新版 `00bd790c`（命令位置の公開資料なし） · `00bd7908`（命令位置の公開資料なし） · `00bd7914`（命令位置の公開資料なし）

~~~diff
- 00bd74e4 ["INT_ADD", "register:40f0:8", ["const:bd74e4:8", "const:4:8"]]
- 00bd74e4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd790c ["INT_ADD", "register:40f0:8", ["const:bd790c:8", "const:4:8"]]
+ 00bd790c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd74e4 bytes c70d0294
+ 00bd790c bytes bd0d0294
- 00bd74e0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd74e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd74e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd74e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7908 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd7908 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7908 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7908 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd74e0 bytes 00441191
+ 00bd7908 bytes 00781491
- 00bd74ec ["COPY", "tmp:0:8", ["const:860:8"]]
- 00bd74ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd74ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd74ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7914 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00bd7914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd74ec bytes 08812191
+ 00bd7914 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33d9a8f3bc0ed1e1c2b9917c6d13dd2"></a>

### [`00bd7500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7500.md) → [`00bd7928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7928.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bd7954",
      "incomplete_value": true,
      "site": "00bd7954",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd793c",
      "incomplete_value": true,
      "site": "00bd793c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7948",
      "incomplete_value": false,
      "site": "00bd794c",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7938",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7948",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd7954",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7938",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7948",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bd7954",
      "WRITE",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7500.md#insn-00bd7524) · [`00bd752c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7500.md#insn-00bd752c) · [`00bd7510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7500.md#insn-00bd7510)
- 新版 `00bd794c`（命令位置の公開資料なし） · `00bd7954`（命令位置の公開資料なし） · `00bd7938`（命令位置の公開資料なし）

~~~diff
- 00bd7524 ["INT_ADD", "register:40f0:8", ["const:bd7524:8", "const:4:8"]]
- 00bd7524 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd794c ["INT_ADD", "register:40f0:8", ["const:bd794c:8", "const:4:8"]]
+ 00bd794c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7524 bytes 7b0d0294
+ 00bd794c bytes 710d0294
- 00bd752c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd752c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7954 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00bd7954 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd752c bytes 603604f9
+ 00bd7954 bytes 603606f9
- 00bd7510 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd7510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00bd7938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7510 bytes 683644f9
+ 00bd7938 bytes 683646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9fd5a7522f1589a21251c6aa5b105f"></a>

### [`00bd7540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7540.md) → [`00bd7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7968.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00bd756c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7994"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd797c",
      "incomplete_value": true,
      "site": "00bd797c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7978",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd755c",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7564",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd7978",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7984",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bd798c",
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

- 旧版 [`00bd7554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7540.md#insn-00bd7554) · [`00bd7564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7540.md#insn-00bd7564) · [`00bd756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7540.md#insn-00bd756c)
- 新版 `00bd797c`（命令位置の公開資料なし）

~~~diff
- 00bd7554 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7554 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd797c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd797c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7554 bytes e80000b5
+ 00bd797c bytes e80000b5
- 00bd7564 ["INT_ADD", "register:40f0:8", ["const:bd7564:8", "const:4:8"]]
- 00bd7564 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7564 bytes 6b0d0294
- 00bd756c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd756c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd756c bytes 603604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3175617c70e5d6d78a4c7e0dcb8cd94b"></a>

### [`00bd7580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7580.md) → [`00bd79a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd79a8.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd75b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd79d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd79bc",
      "incomplete_value": true,
      "site": "00bd79bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd79b8",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd79bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd75b4"
      ]
    ],
    [
      "unmatched:00bd75a0",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd79b8",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd79bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd79dc"
      ]
    ],
    [
      "00bd79c8",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd75a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7580.md#insn-00bd75a8) · [`00bd75b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7580.md#insn-00bd75b0) · [`00bd75c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7580.md#insn-00bd75c0)

~~~diff
- 00bd75a8 ["INT_ADD", "register:40f0:8", ["const:bd75a8:8", "const:4:8"]]
- 00bd75a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd75a8 bytes 5a0d0294
- 00bd75b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd75b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd75b0 bytes 603604f9
- 00bd75c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd75c0 ["RETURN", null, ["register:0:8"]]
- 00bd75c0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7c03ce04afcbe99e2b1d10a38aa88e5"></a>

### [`00bd75c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd75c4.md) → [`00bd79ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd79ec.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7a1c",
      "incomplete_value": true,
      "site": "00bd7a1c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7a00",
      "incomplete_value": true,
      "site": "00bd7a00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7a08",
      "incomplete_value": false,
      "site": "00bd7a14",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd79fc",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7a08",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd7a1c",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd79fc",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7a08",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bd7a1c",
      "WRITE",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd75c4.md#insn-00bd75ec) · [`00bd75f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd75c4.md#insn-00bd75f4) · [`00bd75d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd75c4.md#insn-00bd75d4)
- 新版 `00bd7a14`（命令位置の公開資料なし） · `00bd7a1c`（命令位置の公開資料なし） · `00bd79fc`（命令位置の公開資料なし）

~~~diff
- 00bd75ec ["INT_ADD", "register:40f0:8", ["const:bd75ec:8", "const:4:8"]]
- 00bd75ec ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7a14 ["INT_ADD", "register:40f0:8", ["const:bd7a14:8", "const:4:8"]]
+ 00bd7a14 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd75ec bytes 490d0294
+ 00bd7a14 bytes 3f0d0294
- 00bd75f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd75f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7a1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00bd7a1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd75f4 bytes 603604f9
+ 00bd7a1c bytes 603606f9
- 00bd75d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00bd75d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00bd79fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd75d4 bytes 683644f9
+ 00bd79fc bytes 683646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16a56727ed8cb2f03f1cb878707edc05"></a>

### [`00bd7614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7614.md) → [`00bd7a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7a3c.md) _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7618"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7618",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd761c",
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
      "00bd7a3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd7a40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd7a44",
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

- 旧版 [`00bd7614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7614.md#insn-00bd7614) · [`00bd7618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7614.md#insn-00bd7618) · [`00bd761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7614.md#insn-00bd761c)

~~~diff
- 00bd7614 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd7614 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd7614 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7614 bytes f50f1df8
- 00bd7618 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd7618 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd7618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7618 bytes f44f01a9
- 00bd761c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd761c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd761c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd761c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd761c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369eb49d18078d3f698d180c098d5b78"></a>

### [`00bd7680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7680.md) → [`00bd7aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7aa8.md) _ZN8firebase4auth8auth_idp12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 28.57% / 新版 33.33%

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
      "site": "00bd76bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd76dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7ae4"
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
      "00bd7abc",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ac8",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd76c0"
      ]
    ]
  ],
  "added": [
    [
      "00bd7abc",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ac8",
      "READ",
      [
        "storage",
        "01126c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ae8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7680.md#insn-00bd7698) · [`00bd76bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7680.md#insn-00bd76bc) · [`00bd76c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7680.md#insn-00bd76c4)
- 新版 `00bd7ac0`（命令位置の公開資料なし）

~~~diff
- 00bd7698 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd7698 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd7ac0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd7ac0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd7698 bytes 410200b4
+ 00bd7ac0 bytes 410200b4
- 00bd76bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd76bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd76bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:870:8"]]
- 00bd76bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd76bc bytes bfc22139
- 00bd76c4 ["INT_ADD", "register:40f0:8", ["const:bd76c4:8", "const:4:8"]]
- 00bd76c4 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd76c4 bytes 270d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de490c3fb9e3b0ab04c919f95e7f3ef9"></a>

### [`00bd76f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd76f0.md) → [`00bd7b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b18.md) _ZN8firebase4auth8auth_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7b58",
      "incomplete_value": true,
      "site": "00bd7b58",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7b34",
      "incomplete_value": true,
      "site": "00bd7b34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7b3c",
      "incomplete_value": false,
      "site": "00bd7b50",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7b2c",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7b3c",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd7b58",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7b2c",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7b3c",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bd7b58",
      "WRITE",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd76f0.md#insn-00bd7728) · [`00bd7730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd76f0.md#insn-00bd7730) · [`00bd7704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd76f0.md#insn-00bd7704)
- 新版 `00bd7b50`（命令位置の公開資料なし） · `00bd7b58`（命令位置の公開資料なし） · `00bd7b2c`（命令位置の公開資料なし）

~~~diff
- 00bd7728 ["INT_ADD", "register:40f0:8", ["const:bd7728:8", "const:4:8"]]
- 00bd7728 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7b50 ["INT_ADD", "register:40f0:8", ["const:bd7b50:8", "const:4:8"]]
+ 00bd7b50 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7728 bytes fa0c0294
+ 00bd7b50 bytes f00c0294
- 00bd7730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00bd7730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00bd7b58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7730 bytes 803604f9
+ 00bd7b58 bytes 803606f9
- 00bd7704 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00bd7704 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7b2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00bd7b2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7704 bytes 813644f9
+ 00bd7b2c bytes 813646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d947214d299fd288a91af8ed89e7c6"></a>

### [`00bd779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd779c.md) → [`00bd7bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7bc4.md) _ZN8firebase4auth8auth_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7c04",
      "incomplete_value": true,
      "site": "00bd7c04",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7be0",
      "incomplete_value": true,
      "site": "00bd7be0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7be8",
      "incomplete_value": false,
      "site": "00bd7bfc",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7bd8",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7be8",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bd7c04",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7bd8",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7be8",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bd7c04",
      "WRITE",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd77d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd779c.md#insn-00bd77d4) · [`00bd77dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd779c.md#insn-00bd77dc) · [`00bd77b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd779c.md#insn-00bd77b0)
- 新版 `00bd7bfc`（命令位置の公開資料なし） · `00bd7c04`（命令位置の公開資料なし） · `00bd7bd8`（命令位置の公開資料なし）

~~~diff
- 00bd77d4 ["INT_ADD", "register:40f0:8", ["const:bd77d4:8", "const:4:8"]]
- 00bd77d4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7bfc ["INT_ADD", "register:40f0:8", ["const:bd7bfc:8", "const:4:8"]]
+ 00bd7bfc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd77d4 bytes cf0c0294
+ 00bd7bfc bytes c50c0294
- 00bd77dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00bd77dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7c04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00bd7c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd77dc bytes 803604f9
+ 00bd7c04 bytes 803606f9
- 00bd77b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00bd77b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7bd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00bd7bd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd77b0 bytes 813644f9
+ 00bd7bd8 bytes 813646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce6bcecb8ce1c5b0a9e0c444ed877aa"></a>

### [`00bd780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd780c.md) → [`00bd7c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c34.md) _ZN8firebase4auth8auth_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd7c50",
      "incomplete_value": false,
      "site": "00bd7c54",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd7c60",
      "incomplete_value": true,
      "site": "00bd7c6c",
      "value": [
        "LOAD",
        "8",
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
      "00bd7c50",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd7c60",
      "DATA",
      [
        "storage",
        "01126880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7c50",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd7c60",
      "DATA",
      [
        "storage",
        "01126c80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd782c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd780c.md#insn-00bd782c) · [`00bd7828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd780c.md#insn-00bd7828) · [`00bd7834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd780c.md#insn-00bd7834)
- 新版 `00bd7c54`（命令位置の公開資料なし） · `00bd7c50`（命令位置の公開資料なし） · `00bd7c5c`（命令位置の公開資料なし）

~~~diff
- 00bd782c ["INT_ADD", "register:40f0:8", ["const:bd782c:8", "const:4:8"]]
- 00bd782c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd7c54 ["INT_ADD", "register:40f0:8", ["const:bd7c54:8", "const:4:8"]]
+ 00bd7c54 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd782c bytes f50c0294
+ 00bd7c54 bytes eb0c0294
- 00bd7828 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd7828 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7828 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7828 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7c50 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd7c50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7c50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7c50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd7828 bytes 00441191
+ 00bd7c50 bytes 00781491
- 00bd7834 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00bd7834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7c5c ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 00bd7c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd7834 bytes 08012291
+ 00bd7c5c bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aaa911aaa98ad9b6385952b44f7f294"></a>

### [`00bd7888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7888.md) → [`00bd7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7cb0.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd7cdc",
      "incomplete_value": true,
      "site": "00bd7cdc",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7cc4",
      "incomplete_value": true,
      "site": "00bd7cc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7ccc",
      "incomplete_value": false,
      "site": "00bd7cd4",
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
            "const:887:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7cc0",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ccc",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd7cdc",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7cc0",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ccc",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bd7cdc",
      "WRITE",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd78ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7888.md#insn-00bd78ac) · [`00bd78b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7888.md#insn-00bd78b4) · [`00bd7898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7888.md#insn-00bd7898)
- 新版 `00bd7cd4`（命令位置の公開資料なし） · `00bd7cdc`（命令位置の公開資料なし） · `00bd7cc0`（命令位置の公開資料なし）

~~~diff
- 00bd78ac ["INT_ADD", "register:40f0:8", ["const:bd78ac:8", "const:4:8"]]
- 00bd78ac ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7cd4 ["INT_ADD", "register:40f0:8", ["const:bd7cd4:8", "const:4:8"]]
+ 00bd7cd4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd78ac bytes 990c0294
+ 00bd7cd4 bytes 8f0c0294
- 00bd78b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd78b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00bd7cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd78b4 bytes 604604f9
+ 00bd7cdc bytes 604606f9
- 00bd7898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd7898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7cc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00bd7cc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7898 bytes 684644f9
+ 00bd7cc0 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055d1744da323ac478cfb1a770fcef31"></a>

### [`00bd78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd78c8.md) → [`00bd7cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7cf0.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd7d20",
      "incomplete_value": true,
      "site": "00bd7d20",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7d04",
      "incomplete_value": true,
      "site": "00bd7d04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7d10",
      "incomplete_value": false,
      "site": "00bd7d18",
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
            "const:887:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7d00",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d10",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd7d20",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d00",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d10",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bd7d20",
      "WRITE",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd78f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd78c8.md#insn-00bd78f0) · [`00bd78f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd78c8.md#insn-00bd78f8) · [`00bd78d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd78c8.md#insn-00bd78d8)
- 新版 `00bd7d18`（命令位置の公開資料なし） · `00bd7d20`（命令位置の公開資料なし） · `00bd7d00`（命令位置の公開資料なし）

~~~diff
- 00bd78f0 ["INT_ADD", "register:40f0:8", ["const:bd78f0:8", "const:4:8"]]
- 00bd78f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7d18 ["INT_ADD", "register:40f0:8", ["const:bd7d18:8", "const:4:8"]]
+ 00bd7d18 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd78f0 bytes 880c0294
+ 00bd7d18 bytes 7e0c0294
- 00bd78f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd78f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7d20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00bd7d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd78f8 bytes 604604f9
+ 00bd7d20 bytes 604606f9
- 00bd78d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd78d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00bd7d00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd78d8 bytes 684644f9
+ 00bd7d00 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a62b2ca0199a2da2fbede52374ab191"></a>

### [`00bd790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd790c.md) → [`00bd7d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7d34.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bd793c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7d64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7d48",
      "incomplete_value": true,
      "site": "00bd7d48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd7d44",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7928",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd793c",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d44",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d50",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bd7d64",
      "WRITE",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd790c.md#insn-00bd7920) · [`00bd7934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd790c.md#insn-00bd7934) · [`00bd793c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd790c.md#insn-00bd793c)
- 新版 `00bd7d48`（命令位置の公開資料なし） · `00bd7d5c`（命令位置の公開資料なし）

~~~diff
- 00bd7920 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7920 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd7d48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd7d48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7920 bytes 080100b5
+ 00bd7d48 bytes 080100b5
- 00bd7934 ["INT_ADD", "register:40f0:8", ["const:bd7934:8", "const:4:8"]]
- 00bd7934 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7d5c ["INT_ADD", "register:40f0:8", ["const:bd7d5c:8", "const:4:8"]]
+ 00bd7d5c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7934 bytes 770c0294
+ 00bd7d5c bytes 6d0c0294
- 00bd793c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd793c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd793c bytes 604604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02c3e7052155b00090dbabaffbef0de"></a>

### [`00bd79c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd79c8.md) → [`00bd7df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7df0.md) _ZN8firebase4auth8user_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd7e2c",
      "incomplete_value": true,
      "site": "00bd7e2c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7e4c",
      "incomplete_value": true,
      "site": "00bd7e4c",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7e08",
      "incomplete_value": true,
      "site": "00bd7e08",
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
      "00bd7e04",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7e10",
      "READ",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7e2c",
      "WRITE",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e04",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7e10",
      "READ",
      [
        "storage",
        "01126c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7e2c",
      "WRITE",
      [
        "storage",
        "01126c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd79c8.md#insn-00bd7a04) · [`00bd7a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd79c8.md#insn-00bd7a20) · [`00bd7a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd79c8.md#insn-00bd7a24)
- 新版 `00bd7e2c`（命令位置の公開資料なし） · `00bd7e48`（命令位置の公開資料なし） · `00bd7e4c`（命令位置の公開資料なし）

~~~diff
- 00bd7a04 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd7a04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd7a04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
- 00bd7a04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd7e2c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd7e2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd7e2c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c90:8"]]
+ 00bd7e2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd7a04 bytes bf422239
+ 00bd7e2c bytes bf423239
- 00bd7a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7a20 ["INT_ADD", "register:40f0:8", ["const:bd7a20:8", "const:4:8"]]
- 00bd7a20 ["CALLIND", null, ["register:0:8"]]
+ 00bd7e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7e48 ["INT_ADD", "register:40f0:8", ["const:bd7e48:8", "const:4:8"]]
+ 00bd7e48 ["CALLIND", null, ["register:0:8"]]
- 00bd7a20 bytes 00013fd6
+ 00bd7e48 bytes 00013fd6
- 00bd7a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00bd7a24 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd7a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd7e4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00bd7e4c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd7e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd7a24 bytes 9f4604f9
+ 00bd7e4c bytes 9f4606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f96e9c7aef66084c544b34d8509cc9c"></a>

### [`00bd7a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7a38.md) → [`00bd7e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7e60.md) _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd7a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7ea0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7a54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7a4c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7a54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ea4"
      ]
    ],
    [
      "unmatched:00bd7a5c",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e74",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7e7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ea4"
      ]
    ],
    [
      "00bd7e84",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7a38.md#insn-00bd7a54) · [`00bd7a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7a38.md#insn-00bd7a70) · [`00bd7a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7a38.md#insn-00bd7a78)
- 新版 `00bd7e98`（命令位置の公開資料なし）

~~~diff
- 00bd7a54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd7a54 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd7a54 bytes 410100b5
- 00bd7a70 ["INT_ADD", "register:40f0:8", ["const:bd7a70:8", "const:4:8"]]
- 00bd7a70 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7e98 ["INT_ADD", "register:40f0:8", ["const:bd7e98:8", "const:4:8"]]
+ 00bd7e98 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7a70 bytes 280c0294
+ 00bd7e98 bytes 1e0c0294
- 00bd7a78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00bd7a78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7a78 bytes 804604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a070be50d57007b2b71e60b2caa22a5"></a>

### [`00bd7aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7aa8.md) → [`00bd7ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7ed0.md) _ZN8firebase4auth8user_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd7eec",
      "incomplete_value": false,
      "site": "00bd7ef0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd7efc",
      "incomplete_value": true,
      "site": "00bd7f08",
      "value": [
        "LOAD",
        "8",
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
      "00bd7eec",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd7efc",
      "DATA",
      [
        "storage",
        "01126898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7eec",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd7efc",
      "DATA",
      [
        "storage",
        "01126c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7aa8.md#insn-00bd7ac8) · [`00bd7ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7aa8.md#insn-00bd7ac4) · [`00bd7ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7aa8.md#insn-00bd7ad0)
- 新版 `00bd7ef0`（命令位置の公開資料なし） · `00bd7eec`（命令位置の公開資料なし） · `00bd7ef8`（命令位置の公開資料なし）

~~~diff
- 00bd7ac8 ["INT_ADD", "register:40f0:8", ["const:bd7ac8:8", "const:4:8"]]
- 00bd7ac8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd7ef0 ["INT_ADD", "register:40f0:8", ["const:bd7ef0:8", "const:4:8"]]
+ 00bd7ef0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd7ac8 bytes 4e0c0294
+ 00bd7ef0 bytes 440c0294
- 00bd7ac4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd7ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd7ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd7eec ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd7eec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7eec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd7eec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd7ac4 bytes 00680a91
+ 00bd7eec bytes 009c0d91
- 00bd7ad0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bd7ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7ef8 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00bd7ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd7ad0 bytes 08612291
+ 00bd7ef8 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71dad28b996b98d0da845f3ef99b4cb7"></a>

### [`00bd7ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ae4.md) → [`00bd7f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7f0c.md) _ZN8firebase4auth8user_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd7f4c",
      "incomplete_value": true,
      "site": "00bd7f4c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7f28",
      "incomplete_value": true,
      "site": "00bd7f28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7f30",
      "incomplete_value": false,
      "site": "00bd7f44",
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
            "const:887:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7f20",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7f30",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bd7f4c",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7f20",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7f30",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bd7f4c",
      "WRITE",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ae4.md#insn-00bd7b1c) · [`00bd7b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ae4.md#insn-00bd7b24) · [`00bd7af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ae4.md#insn-00bd7af8)
- 新版 `00bd7f44`（命令位置の公開資料なし） · `00bd7f4c`（命令位置の公開資料なし） · `00bd7f20`（命令位置の公開資料なし）

~~~diff
- 00bd7b1c ["INT_ADD", "register:40f0:8", ["const:bd7b1c:8", "const:4:8"]]
- 00bd7b1c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7f44 ["INT_ADD", "register:40f0:8", ["const:bd7f44:8", "const:4:8"]]
+ 00bd7f44 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7b1c bytes fd0b0294
+ 00bd7f44 bytes f30b0294
- 00bd7b24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00bd7b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7f4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00bd7f4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7b24 bytes 804604f9
+ 00bd7f4c bytes 804606f9
- 00bd7af8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00bd7af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7f20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00bd7f20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7af8 bytes 814644f9
+ 00bd7f20 bytes 814646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acaa14f65cda72b74323580822f43d2b"></a>

### [`00bd7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b90.md) → [`00bd7fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7fb8.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bd7fe4",
      "incomplete_value": true,
      "site": "00bd7fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd7fcc",
      "incomplete_value": true,
      "site": "00bd7fcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7fd8",
      "incomplete_value": false,
      "site": "00bd7fdc",
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
            "const:7b7:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7fc8",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7fd8",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd7fe4",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7fc8",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7fd8",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ],
    [
      "00bd7fe4",
      "WRITE",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b90.md#insn-00bd7bb4) · [`00bd7bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b90.md#insn-00bd7bbc) · [`00bd7ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b90.md#insn-00bd7ba0)
- 新版 `00bd7fdc`（命令位置の公開資料なし） · `00bd7fe4`（命令位置の公開資料なし） · `00bd7fc8`（命令位置の公開資料なし）

~~~diff
- 00bd7bb4 ["INT_ADD", "register:40f0:8", ["const:bd7bb4:8", "const:4:8"]]
- 00bd7bb4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd7fdc ["INT_ADD", "register:40f0:8", ["const:bd7fdc:8", "const:4:8"]]
+ 00bd7fdc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7bb4 bytes d70b0294
+ 00bd7fdc bytes cd0b0294
- 00bd7bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
- 00bd7bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd7fe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb0:8"]]
+ 00bd7fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7bbc bytes 605a04f9
+ 00bd7fe4 bytes 605a06f9
- 00bd7ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
- 00bd7ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd7fc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb0:8"]]
+ 00bd7fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7ba0 bytes 685a44f9
+ 00bd7fc8 bytes 685a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055d4c101c19612f55a1dbed29b7eef3"></a>

### [`00bd7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7bd0.md) → [`00bd7ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7ff8.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00bd7bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7bd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7bd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8008",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd7ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd7ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8008",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7bd0.md#insn-00bd7bd0) · [`00bd7bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7bd0.md#insn-00bd7bd4) · [`00bd7be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7bd0.md#insn-00bd7be4)
- 新版 `00bd800c`（命令位置の公開資料なし）

~~~diff
- 00bd7bd0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd7bd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd7bd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7bd0 bytes f30f1ef8
- 00bd7bd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7bd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7bd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7bd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7bd4 bytes fd7b01a9
- 00bd7be4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7be4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd800c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd800c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd7be4 bytes e80000b5
+ 00bd800c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bd69a6e7562d4daee6ce38853babaaa"></a>

### [`00bd7c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c10.md) → [`00bd8038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8038.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd7c40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8068"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd804c",
      "incomplete_value": true,
      "site": "00bd804c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd8048",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd804c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7c44"
      ]
    ],
    [
      "unmatched:00bd7c30",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd8048",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd804c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd806c"
      ]
    ],
    [
      "00bd8058",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c10.md#insn-00bd7c38) · [`00bd7c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c10.md#insn-00bd7c40) · [`00bd7c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c10.md#insn-00bd7c50)

~~~diff
- 00bd7c38 ["INT_ADD", "register:40f0:8", ["const:bd7c38:8", "const:4:8"]]
- 00bd7c38 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7c38 bytes b60b0294
- 00bd7c40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
- 00bd7c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7c40 bytes 605a04f9
- 00bd7c50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd7c50 ["RETURN", null, ["register:0:8"]]
- 00bd7c50 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-831d6eaf881843660d7505eb3bdc4830"></a>

### [`00bd7c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c54.md) → [`00bd807c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd807c.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bd7c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd80ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd8090",
      "incomplete_value": true,
      "site": "00bd8090",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd808c",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7c70",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7c84",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd808c",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8098",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ],
    [
      "00bd80ac",
      "WRITE",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c54.md#insn-00bd7c68) · [`00bd7c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c54.md#insn-00bd7c7c) · [`00bd7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7c54.md#insn-00bd7c84)
- 新版 `00bd8090`（命令位置の公開資料なし） · `00bd80a4`（命令位置の公開資料なし）

~~~diff
- 00bd7c68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7c68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd8090 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd8090 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7c68 bytes 080100b5
+ 00bd8090 bytes 080100b5
- 00bd7c7c ["INT_ADD", "register:40f0:8", ["const:bd7c7c:8", "const:4:8"]]
- 00bd7c7c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd80a4 ["INT_ADD", "register:40f0:8", ["const:bd80a4:8", "const:4:8"]]
+ 00bd80a4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7c7c bytes a50b0294
+ 00bd80a4 bytes 9b0b0294
- 00bd7c84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b0:8"]]
- 00bd7c84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7c84 bytes 605a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cdbe2ec255e020e6daafc5b34419ac4"></a>

### [`00bd7ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ca4.md) → [`00bd80cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd80cc.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 25.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8124"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8100",
      "incomplete_value": true,
      "site": "00bd810c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd80e0",
      "READ",
      [
        "storage",
        "011268b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd80ec",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7d00"
      ]
    ],
    [
      "unmatched:00bd7cd8",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd80e0",
      "READ",
      [
        "storage",
        "01126cb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd80ec",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8128"
      ]
    ],
    [
      "00bd8100",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ca4.md#insn-00bd7ce4) · [`00bd7cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ca4.md#insn-00bd7cfc) · [`00bd7d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ca4.md#insn-00bd7d0c)
- 新版 `00bd810c`（命令位置の公開資料なし）

~~~diff
- 00bd7ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7ce4 ["INT_ADD", "register:40f0:8", ["const:bd7ce4:8", "const:4:8"]]
- 00bd7ce4 ["CALLIND", null, ["register:0:8"]]
+ 00bd810c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd810c ["INT_ADD", "register:40f0:8", ["const:bd810c:8", "const:4:8"]]
+ 00bd810c ["CALLIND", null, ["register:0:8"]]
- 00bd7ce4 bytes 00013fd6
+ 00bd810c bytes 00013fd6
- 00bd7cfc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd7cfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b8:8"]]
- 00bd7cfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd7cfc bytes a0e22239
- 00bd7d0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd7d0c ["RETURN", null, ["register:0:8"]]
- 00bd7d0c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130c3f0a79d95f2e87ff451a0a5c5d65"></a>

### [`00bd7d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d10.md) → [`00bd8138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8138.md) _ZN8firebase4auth8jniphone12ReleaseClassEP7_JNIEnv

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
      "site": "00bd7d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7d14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7d18",
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
      "00bd8138",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd813c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd8140",
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

- 旧版 [`00bd7d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d10.md#insn-00bd7d10) · [`00bd7d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d10.md#insn-00bd7d14) · [`00bd7d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d10.md#insn-00bd7d18)

~~~diff
- 00bd7d10 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd7d10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd7d10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7d10 bytes f50f1df8
- 00bd7d14 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd7d14 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd7d14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7d14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7d14 bytes f44f01a9
- 00bd7d18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7d18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7d18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd7d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7d18 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f38a41d002248a064c4b580f35d545"></a>

### [`00bd7d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d80.md) → [`00bd81a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd81a8.md) _ZN8firebase4auth8jniphone14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd81e8",
      "incomplete_value": true,
      "site": "00bd81e8",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd81c4",
      "incomplete_value": true,
      "site": "00bd81c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd81cc",
      "incomplete_value": false,
      "site": "00bd81e0",
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
            "const:7b7:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd81bc",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd81cc",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ],
    [
      "00bd81e8",
      "WRITE",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd81bc",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd81cc",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ],
    [
      "00bd81e8",
      "WRITE",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d80.md#insn-00bd7db8) · [`00bd7dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d80.md#insn-00bd7dc0) · [`00bd7d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7d80.md#insn-00bd7d94)
- 新版 `00bd81e0`（命令位置の公開資料なし） · `00bd81e8`（命令位置の公開資料なし） · `00bd81bc`（命令位置の公開資料なし）

~~~diff
- 00bd7db8 ["INT_ADD", "register:40f0:8", ["const:bd7db8:8", "const:4:8"]]
- 00bd7db8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd81e0 ["INT_ADD", "register:40f0:8", ["const:bd81e0:8", "const:4:8"]]
+ 00bd81e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7db8 bytes 560b0294
+ 00bd81e0 bytes 4c0b0294
- 00bd7dc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b0:8"]]
- 00bd7dc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd81e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
+ 00bd81e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7dc0 bytes 805a04f9
+ 00bd81e8 bytes 805a06f9
- 00bd7d94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b0:8"]]
- 00bd7d94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd81bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
+ 00bd81bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7d94 bytes 815a44f9
+ 00bd81bc bytes 815a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce63ac3c274e67da4b7fb84b3ba78a22"></a>

### [`00bd7e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e2c.md) → [`00bd8254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8254.md) _ZN8firebase4auth8jniphone13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd7e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8294"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7e48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7e40",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8298"
      ]
    ],
    [
      "unmatched:00bd7e50",
      "PARAM",
      [
        "storage",
        "002b2777",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd8268",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8298"
      ]
    ],
    [
      "00bd8278",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e2c.md#insn-00bd7e48) · [`00bd7e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e2c.md#insn-00bd7e64) · [`00bd7e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e2c.md#insn-00bd7e6c)
- 新版 `00bd828c`（命令位置の公開資料なし）

~~~diff
- 00bd7e48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd7e48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7e48 bytes 410100b5
- 00bd7e64 ["INT_ADD", "register:40f0:8", ["const:bd7e64:8", "const:4:8"]]
- 00bd7e64 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd828c ["INT_ADD", "register:40f0:8", ["const:bd828c:8", "const:4:8"]]
+ 00bd828c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7e64 bytes 2b0b0294
+ 00bd828c bytes 210b0294
- 00bd7e6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b0:8"]]
- 00bd7e6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7e6c bytes 805a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834bcffcc77ab04983114cde137ab9c0"></a>

### [`00bd7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ed8.md) → [`00bd8300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8300.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00bd832c",
      "incomplete_value": true,
      "site": "00bd832c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd8314",
      "incomplete_value": true,
      "site": "00bd8314",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8320",
      "incomplete_value": false,
      "site": "00bd8324",
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
            "const:cec:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd8310",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8320",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd832c",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd8310",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8320",
      "PARAM",
      [
        "storage",
        "002b5cec",
        null,
        "string"
      ]
    ],
    [
      "00bd832c",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ed8.md#insn-00bd7efc) · [`00bd7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ed8.md#insn-00bd7f04) · [`00bd7ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7ed8.md#insn-00bd7ee8)
- 新版 `00bd8324`（命令位置の公開資料なし） · `00bd832c`（命令位置の公開資料なし） · `00bd8310`（命令位置の公開資料なし）

~~~diff
- 00bd7efc ["INT_ADD", "register:40f0:8", ["const:bd7efc:8", "const:4:8"]]
- 00bd7efc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd8324 ["INT_ADD", "register:40f0:8", ["const:bd8324:8", "const:4:8"]]
+ 00bd8324 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7efc bytes 050b0294
+ 00bd8324 bytes fb0a0294
- 00bd7f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd832c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd832c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7f04 bytes 606e04f9
+ 00bd832c bytes 606e06f9
- 00bd7ee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7ee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd8310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd8310 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7ee8 bytes 686e44f9
+ 00bd8310 bytes 686e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f9db4adf60ecc12aef9cc5c09dbe94"></a>

### [`00bd7f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f18.md) → [`00bd8340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8340.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd7f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd836c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd8354",
      "incomplete_value": true,
      "site": "00bd8354",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd8350",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7f34",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7f3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd8350",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd835c",
      "PARAM",
      [
        "storage",
        "002b5cec",
        null,
        "string"
      ]
    ],
    [
      "00bd8364",
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

- 旧版 [`00bd7f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f18.md#insn-00bd7f2c) · [`00bd7f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f18.md#insn-00bd7f3c) · [`00bd7f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f18.md#insn-00bd7f44)
- 新版 `00bd8354`（命令位置の公開資料なし）

~~~diff
- 00bd7f2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7f2c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd8354 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd8354 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd7f2c bytes e80000b5
+ 00bd8354 bytes e80000b5
- 00bd7f3c ["INT_ADD", "register:40f0:8", ["const:bd7f3c:8", "const:4:8"]]
- 00bd7f3c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7f3c bytes f50a0294
- 00bd7f44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7f44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7f44 bytes 606e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd62d6dbd0737337641f6958eaa309af"></a>

### [`00bd7f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f58.md) → [`00bd8380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8380.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd83b0",
      "incomplete_value": true,
      "site": "00bd83b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd8394",
      "incomplete_value": true,
      "site": "00bd8394",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd83a0",
      "incomplete_value": false,
      "site": "00bd83a8",
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
            "const:cec:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd8390",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd83a0",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd83b0",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd8390",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd83a0",
      "PARAM",
      [
        "storage",
        "002b5cec",
        null,
        "string"
      ]
    ],
    [
      "00bd83b0",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f58.md#insn-00bd7f80) · [`00bd7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f58.md#insn-00bd7f88) · [`00bd7f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f58.md#insn-00bd7f68)
- 新版 `00bd83a8`（命令位置の公開資料なし） · `00bd83b0`（命令位置の公開資料なし） · `00bd8390`（命令位置の公開資料なし）

~~~diff
- 00bd7f80 ["INT_ADD", "register:40f0:8", ["const:bd7f80:8", "const:4:8"]]
- 00bd7f80 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd83a8 ["INT_ADD", "register:40f0:8", ["const:bd83a8:8", "const:4:8"]]
+ 00bd83a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7f80 bytes e40a0294
+ 00bd83a8 bytes da0a0294
- 00bd7f88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7f88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd83b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd83b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7f88 bytes 606e04f9
+ 00bd83b0 bytes 606e06f9
- 00bd7f68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7f68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd8390 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd8390 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7f68 bytes 686e44f9
+ 00bd8390 bytes 686e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-798e7fdfaaf636b19e15396f97070fbd"></a>

### [`00bd7f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f9c.md) → [`00bd83c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd83c4.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd83f4",
      "incomplete_value": true,
      "site": "00bd83f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd83d8",
      "incomplete_value": true,
      "site": "00bd83d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd83e0",
      "incomplete_value": false,
      "site": "00bd83ec",
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
            "const:cec:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd83d4",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd83e0",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd83f4",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd83d4",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd83e0",
      "PARAM",
      [
        "storage",
        "002b5cec",
        null,
        "string"
      ]
    ],
    [
      "00bd83f4",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f9c.md#insn-00bd7fc4) · [`00bd7fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f9c.md#insn-00bd7fcc) · [`00bd7fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7f9c.md#insn-00bd7fac)
- 新版 `00bd83ec`（命令位置の公開資料なし） · `00bd83f4`（命令位置の公開資料なし） · `00bd83d4`（命令位置の公開資料なし）

~~~diff
- 00bd7fc4 ["INT_ADD", "register:40f0:8", ["const:bd7fc4:8", "const:4:8"]]
- 00bd7fc4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd83ec ["INT_ADD", "register:40f0:8", ["const:bd83ec:8", "const:4:8"]]
+ 00bd83ec ["CALL", null, ["callee:00c5af10:8"]]
- 00bd7fc4 bytes d30a0294
+ 00bd83ec bytes c90a0294
- 00bd7fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd83f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd83f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7fcc bytes 606e04f9
+ 00bd83f4 bytes 606e06f9
- 00bd7fac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00bd7fac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd83d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd8:8"]]
+ 00bd83d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7fac bytes 686e44f9
+ 00bd83d4 bytes 686e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1db9e1181621636fd7d799b8c677c6"></a>

### [`00bd80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd80c8.md) → [`00bd84f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd84f0.md) _ZN8firebase4auth15phonecredential14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd80c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd80c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd80cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd80c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd80cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd80dc",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd84f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd84f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8504",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd80c8.md#insn-00bd80c8) · [`00bd80cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd80c8.md#insn-00bd80cc) · [`00bd80e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd80c8.md#insn-00bd80e4)

~~~diff
- 00bd80c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd80c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd80c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd80c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd80c8 bytes f44fbea9
- 00bd80cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd80cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd80cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd80cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd80cc bytes fd7b01a9
- 00bd80e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd80e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd80e4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afda2077769986f9c6b4696ed8a0f265"></a>

### [`00bd8138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8138.md) → [`00bd8560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8560.md) _ZN8firebase4auth15phonecredential11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd857c",
      "incomplete_value": false,
      "site": "00bd8580",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd858c",
      "incomplete_value": true,
      "site": "00bd8598",
      "value": [
        "LOAD",
        "8",
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
      "00bd857c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd858c",
      "DATA",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd857c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd858c",
      "DATA",
      [
        "storage",
        "01126ce8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8138.md#insn-00bd8158) · [`00bd8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8138.md#insn-00bd8154) · [`00bd8160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8138.md#insn-00bd8160)
- 新版 `00bd8580`（命令位置の公開資料なし） · `00bd857c`（命令位置の公開資料なし） · `00bd8588`（命令位置の公開資料なし）

~~~diff
- 00bd8158 ["INT_ADD", "register:40f0:8", ["const:bd8158:8", "const:4:8"]]
- 00bd8158 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd8580 ["INT_ADD", "register:40f0:8", ["const:bd8580:8", "const:4:8"]]
+ 00bd8580 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd8158 bytes aa0a0294
+ 00bd8580 bytes a00a0294
- 00bd8154 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd8154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd8154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd8154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd857c ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd857c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd857c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd857c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd8154 bytes 00680a91
+ 00bd857c bytes 009c0d91
- 00bd8160 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00bd8160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd8160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd8160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd8588 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00bd8588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd8588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd8588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd8160 bytes 08a12391
+ 00bd8588 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c385e3dd0bc45cd9627894f182052d04"></a>

### [`00bd8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8174.md) → [`00bd859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd859c.md) _ZN8firebase4auth15phonecredential13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd85dc",
      "incomplete_value": true,
      "site": "00bd85dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd85b8",
      "incomplete_value": true,
      "site": "00bd85b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd85c0",
      "incomplete_value": false,
      "site": "00bd85d4",
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
            "const:cec:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd85b0",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd85c0",
      "PARAM",
      [
        "storage",
        "002b5cac",
        null,
        "string"
      ]
    ],
    [
      "00bd85dc",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd85b0",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd85c0",
      "PARAM",
      [
        "storage",
        "002b5cec",
        null,
        "string"
      ]
    ],
    [
      "00bd85dc",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd81ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8174.md#insn-00bd81ac) · [`00bd81b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8174.md#insn-00bd81b4) · [`00bd8188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8174.md#insn-00bd8188)
- 新版 `00bd85d4`（命令位置の公開資料なし） · `00bd85dc`（命令位置の公開資料なし） · `00bd85b0`（命令位置の公開資料なし）

~~~diff
- 00bd81ac ["INT_ADD", "register:40f0:8", ["const:bd81ac:8", "const:4:8"]]
- 00bd81ac ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd85d4 ["INT_ADD", "register:40f0:8", ["const:bd85d4:8", "const:4:8"]]
+ 00bd85d4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd81ac bytes 590a0294
+ 00bd85d4 bytes 4f0a0294
- 00bd81b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
- 00bd81b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd85dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
+ 00bd85dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd81b4 bytes 806e04f9
+ 00bd85dc bytes 806e06f9
- 00bd8188 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
- 00bd8188 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd85b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
+ 00bd85b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd8188 bytes 816e44f9
+ 00bd85b0 bytes 816e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa12a3c5a941ecc6126ec64cb3ae894"></a>

### [`00bd81e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd81e4.md) → [`00bd860c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd860c.md) _ZN8firebase4auth15phonecredential10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd8628",
      "incomplete_value": false,
      "site": "00bd862c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd8638",
      "incomplete_value": true,
      "site": "00bd8644",
      "value": [
        "LOAD",
        "8",
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
      "00bd8628",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd8638",
      "DATA",
      [
        "storage",
        "011268f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd8628",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd8638",
      "DATA",
      [
        "storage",
        "01126cf0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd81e4.md#insn-00bd8204) · [`00bd8200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd81e4.md#insn-00bd8200) · [`00bd820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd81e4.md#insn-00bd820c)
- 新版 `00bd862c`（命令位置の公開資料なし） · `00bd8628`（命令位置の公開資料なし） · `00bd8634`（命令位置の公開資料なし）

~~~diff
- 00bd8204 ["INT_ADD", "register:40f0:8", ["const:bd8204:8", "const:4:8"]]
- 00bd8204 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd862c ["INT_ADD", "register:40f0:8", ["const:bd862c:8", "const:4:8"]]
+ 00bd862c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd8204 bytes 7f0a0294
+ 00bd862c bytes 750a0294
- 00bd8200 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd8200 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd8200 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd8200 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd8628 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd8628 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8628 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd8628 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd8200 bytes 00441191
+ 00bd8628 bytes 00781491
- 00bd820c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00bd820c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd820c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd820c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd8634 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00bd8634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd8634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd8634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd820c bytes 08c12391
+ 00bd8634 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e574011afaf425d8bd9dabba6d7697a"></a>

### [`00bd8220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8220.md) → [`00bd8648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8648.md) _ZN8firebase4auth24CacheCredentialMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8b0.md) · 呼出先 4件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcb0.md) · 呼出先 4件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 16.55% / 新版 16.55%

CFGの説明率　旧版 2.86% / 新版 2.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 24件

アドレスに依存する影響 `branch_value` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8224"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8220",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8224",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8228",
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
      "00bd8648",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd864c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd8650",
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

- 旧版 [`00bd8220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8220.md#insn-00bd8220) · [`00bd8224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8220.md#insn-00bd8224) · [`00bd8228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8220.md#insn-00bd8228)

~~~diff
- 00bd8220 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd8220 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd8220 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd8220 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd8220 bytes f657bda9
- 00bd8224 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd8224 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd8224 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd8224 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8224 bytes f44f01a9
- 00bd8228 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd8228 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd8228 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd8228 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8228 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b00d332d89efa25c302caaebcd35754"></a>

### [`00bd888c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd888c.md) → [`00bd8cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8cb4.md) _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8c0.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcc0.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 6.29% / 新版 6.29%

CFGの説明率　旧版 0.88% / 新版 0.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 31件, `unresolved_call_alignment` 51件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 34件

アドレスに依存する影響 `branch_value` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd88c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd88e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8914"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd8cc8",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8cd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd88ec"
      ]
    ],
    [
      "00bd8cd8",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd8cc8",
      "READ",
      [
        "storage",
        "01126c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8cd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8d14"
      ]
    ],
    [
      "00bd8cd8",
      "READ",
      [
        "storage",
        "01126c70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd88c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd888c.md#insn-00bd88c8) · [`00bd88e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd888c.md#insn-00bd88e8) · [`00bd8914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd888c.md#insn-00bd8914)

~~~diff
- 00bd88c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd88c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd88c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:870:8"]]
- 00bd88c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd88c8 bytes bfc22139
- 00bd88e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00bd88e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd88e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd88e8 bytes 9f3604f9
- 00bd8914 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd8914 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd8914 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:650:8"]]
- 00bd8914 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd8914 bytes bf421939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9332e5a227af1a4202e3b94476129d7"></a>

### [`00bd8dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8dc4.md) → [`00bd91ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd91ec.md) _ZN8firebase4auth10CredentialD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5da00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da00.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 2件 [`00c5a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9f0.md) [`00c5de00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de00.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8dc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8dec",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd91ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd91f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd9214",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8dc4.md#insn-00bd8dc4) · [`00bd8dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8dc4.md#insn-00bd8dc8) · [`00bd8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8dc4.md#insn-00bd8df0)
- 新版 `00bd9218`（命令位置の公開資料なし）

~~~diff
- 00bd8dc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd8dc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd8dc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd8dc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd8dc4 bytes f44fbea9
- 00bd8dc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd8dc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd8dc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd8dc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8dc8 bytes fd7b01a9
- 00bd8df0 ["INT_ADD", "register:40f0:8", ["const:bd8df0:8", "const:4:8"]]
- 00bd8df0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9218 ["INT_ADD", "register:40f0:8", ["const:bd9218:8", "const:4:8"]]
+ 00bd9218 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd8df0 bytes 84070294
+ 00bd9218 bytes 7a070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c70c8bcf750fd1952f7a9fc661f0832f"></a>

### [`00bd8e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e98.md) → [`00bd92c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd92c0.md) _ZN8firebase4auth10CredentialaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) · 呼出先 4件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md) · 呼出先 4件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 61.11% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8f4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd9370"
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
      "00bd92f8",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd8f10",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd92f8",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd9338",
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

- 旧版 [`00bd8ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e98.md#insn-00bd8ed4) · [`00bd8f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e98.md#insn-00bd8f10) · [`00bd8f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8e98.md#insn-00bd8f48)
- 新版 `00bd92fc`（命令位置の公開資料なし）

~~~diff
- 00bd8ed4 ["INT_ADD", "register:40f0:8", ["const:bd8ed4:8", "const:4:8"]]
- 00bd8ed4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd92fc ["INT_ADD", "register:40f0:8", ["const:bd92fc:8", "const:4:8"]]
+ 00bd92fc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd8ed4 bytes 4b070294
+ 00bd92fc bytes 41070294
- 00bd8f10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd8f10 ["INT_ADD", "register:40f0:8", ["const:bd8f10:8", "const:4:8"]]
- 00bd8f10 ["CALLIND", null, ["register:0:8"]]
- 00bd8f10 bytes 00013fd6
- 00bd8f48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd8f48 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00bd8f48 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bd8f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00bd8f48 bytes 6115889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38116a8188f1187f8e4695ff6df9406a"></a>

### [`00bd8f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8f68.md) → [`00bd9390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9390.md) _ZNK8firebase4auth10Credential8providerEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

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
      "definition_site": "00bd93b8",
      "incomplete_value": false,
      "site": "00bd93bc",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd93d4",
      "incomplete_value": true,
      "site": "00bd93dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8fe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8f90",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd93d4",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd93b8",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd93d4",
      "READ",
      [
        "storage",
        "01126a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8f68.md#insn-00bd8f94) · [`00bd8fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8f68.md#insn-00bd8fb4) · [`00bd8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8f68.md#insn-00bd8fe8)
- 新版 `00bd93bc`（命令位置の公開資料なし） · `00bd93dc`（命令位置の公開資料なし）

~~~diff
- 00bd8f94 ["INT_ADD", "register:40f0:8", ["const:bd8f94:8", "const:4:8"]]
- 00bd8f94 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd93bc ["INT_ADD", "register:40f0:8", ["const:bd93bc:8", "const:4:8"]]
+ 00bd93bc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd8f94 bytes 1b070294
+ 00bd93bc bytes 11070294
- 00bd8fb4 ["INT_ADD", "register:40f0:8", ["const:bd8fb4:8", "const:4:8"]]
- 00bd8fb4 ["CALL", null, ["callee:00497834:8"]]
+ 00bd93dc ["INT_ADD", "register:40f0:8", ["const:bd93dc:8", "const:4:8"]]
+ 00bd93dc ["CALL", null, ["callee:00497834:8"]]
- 00bd8fb4 bytes 10fae297
+ 00bd93dc bytes 16f9e297
- 00bd8fe8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd8fe8 ["RETURN", null, ["register:0:8"]]
- 00bd8fe8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccdbfe7cd3f605c40525636092eb9b4c"></a>

### [`00bd8fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8fec.md) → [`00bd9414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9414.md) _ZNK8firebase4auth10Credential8is_validEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-41484018171545bf9b4b4d360fa0c535"></a>

### [`00bd8ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8ffc.md) → [`00bd9424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 71.43% / 新版 75.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd947c",
      "incomplete_value": false,
      "site": "00bd9480",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd94c0",
      "incomplete_value": true,
      "site": "00bd94d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd94c4",
      "incomplete_value": true,
      "site": "00bd94d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "unmatched:00bd9038",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9464",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd91c8"
      ]
    ],
    [
      "00bd947c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9460",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9464",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd95f0"
      ]
    ],
    [
      "00bd947c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8ffc.md#insn-00bd9058) · [`00bd90b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8ffc.md#insn-00bd90b0) · [`00bd9100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8ffc.md#insn-00bd9100)
- 新版 `00bd9480`（命令位置の公開資料なし） · `00bd94d8`（命令位置の公開資料なし） · `00bd9528`（命令位置の公開資料なし）

~~~diff
- 00bd9058 ["INT_ADD", "register:40f0:8", ["const:bd9058:8", "const:4:8"]]
- 00bd9058 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9480 ["INT_ADD", "register:40f0:8", ["const:bd9480:8", "const:4:8"]]
+ 00bd9480 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9058 bytes ea060294
+ 00bd9480 bytes e0060294
- 00bd90b0 ["INT_ADD", "register:40f0:8", ["const:bd90b0:8", "const:4:8"]]
- 00bd90b0 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bd94d8 ["INT_ADD", "register:40f0:8", ["const:bd94d8:8", "const:4:8"]]
+ 00bd94d8 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd90b0 bytes bc050294
+ 00bd94d8 bytes b2050294
- 00bd9100 ["INT_ADD", "register:40f0:8", ["const:bd9100:8", "const:4:8"]]
- 00bd9100 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9528 ["INT_ADD", "register:40f0:8", ["const:bd9528:8", "const:4:8"]]
+ 00bd9528 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9100 bytes c0060294
+ 00bd9528 bytes b6060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb91fba9a6460b69b1d12a1ae28b51e"></a>

### [`00bd9340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9340.md) → [`00bd9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9768.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

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
      "definition_site": "00bd9798",
      "incomplete_value": false,
      "site": "00bd979c",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd97b0",
      "incomplete_value": true,
      "site": "00bd97b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd9798",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bd97b0",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd9798",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd97b0",
      "READ",
      [
        "storage",
        "01126ce8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9340.md#insn-00bd9374) · [`00bd9390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9340.md#insn-00bd9390) · [`00bd9360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9340.md#insn-00bd9360)
- 新版 `00bd979c`（命令位置の公開資料なし） · `00bd97b8`（命令位置の公開資料なし） · `00bd9788`（命令位置の公開資料なし）

~~~diff
- 00bd9374 ["INT_ADD", "register:40f0:8", ["const:bd9374:8", "const:4:8"]]
- 00bd9374 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd979c ["INT_ADD", "register:40f0:8", ["const:bd979c:8", "const:4:8"]]
+ 00bd979c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9374 bytes 23060294
+ 00bd979c bytes 19060294
- 00bd9390 ["INT_ADD", "register:40f0:8", ["const:bd9390:8", "const:4:8"]]
- 00bd9390 ["CALL", null, ["callee:00497834:8"]]
+ 00bd97b8 ["INT_ADD", "register:40f0:8", ["const:bd97b8:8", "const:4:8"]]
+ 00bd97b8 ["CALL", null, ["callee:00497834:8"]]
- 00bd9390 bytes 19f9e297
+ 00bd97b8 bytes 1ff8e297
- 00bd9360 ["INT_ADD", "register:40f0:8", ["const:bd9360:8", "const:4:8"]]
- 00bd9360 ["CALL", null, ["callee:00c5b260:8"]]
+ 00bd9788 ["INT_ADD", "register:40f0:8", ["const:bd9788:8", "const:4:8"]]
+ 00bd9788 ["CALL", null, ["callee:00c5b260:8"]]
- 00bd9360 bytes c0060294
+ 00bd9788 bytes b6060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f408af7ee8d08bac82c635b8712a87"></a>

### [`00bd93c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd93c8.md) → [`00bd97f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd97f0.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9a0.md) · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5dda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dda0.md) · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
      "definition_site": "00bd981c",
      "incomplete_value": false,
      "site": "00bd9820",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd981c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd981c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd93f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd93c8.md#insn-00bd93f8) · [`00bd93e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd93c8.md#insn-00bd93e4) · [`00bd93f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd93c8.md#insn-00bd93f4)
- 新版 `00bd9820`（命令位置の公開資料なし） · `00bd980c`（命令位置の公開資料なし） · `00bd981c`（命令位置の公開資料なし）

~~~diff
- 00bd93f8 ["INT_ADD", "register:40f0:8", ["const:bd93f8:8", "const:4:8"]]
- 00bd93f8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9820 ["INT_ADD", "register:40f0:8", ["const:bd9820:8", "const:4:8"]]
+ 00bd9820 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd93f8 bytes 02060294
+ 00bd9820 bytes f8050294
- 00bd93e4 ["INT_ADD", "register:40f0:8", ["const:bd93e4:8", "const:4:8"]]
- 00bd93e4 ["CALL", null, ["callee:00c5b260:8"]]
+ 00bd980c ["INT_ADD", "register:40f0:8", ["const:bd980c:8", "const:4:8"]]
+ 00bd980c ["CALL", null, ["callee:00c5b260:8"]]
- 00bd93e4 bytes 9f060294
+ 00bd980c bytes 95060294
- 00bd93f4 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bd93f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd93f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd93f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd981c ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bd981c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd981c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd981c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd93f4 bytes 00601691
+ 00bd981c bytes 00601791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd9d38634c5a596043af0e1b083d1988"></a>

### [`00bd9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9458.md) → [`00bd9880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9880.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

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
      "definition_site": "00bd98bc",
      "incomplete_value": false,
      "site": "00bd98c0",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd98e8",
      "incomplete_value": true,
      "site": "00bd98fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd98ec",
      "incomplete_value": true,
      "site": "00bd98fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd98a0",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd98a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9564"
      ]
    ],
    [
      "00bd98bc",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd98a0",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd98a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd998c"
      ]
    ],
    [
      "00bd98bc",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9458.md#insn-00bd9498) · [`00bd94d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9458.md#insn-00bd94d4) · [`00bd951c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9458.md#insn-00bd951c)
- 新版 `00bd98c0`（命令位置の公開資料なし） · `00bd98fc`（命令位置の公開資料なし） · `00bd9944`（命令位置の公開資料なし）

~~~diff
- 00bd9498 ["INT_ADD", "register:40f0:8", ["const:bd9498:8", "const:4:8"]]
- 00bd9498 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd98c0 ["INT_ADD", "register:40f0:8", ["const:bd98c0:8", "const:4:8"]]
+ 00bd98c0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9498 bytes da050294
+ 00bd98c0 bytes d0050294
- 00bd94d4 ["INT_ADD", "register:40f0:8", ["const:bd94d4:8", "const:4:8"]]
- 00bd94d4 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bd98fc ["INT_ADD", "register:40f0:8", ["const:bd98fc:8", "const:4:8"]]
+ 00bd98fc ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd94d4 bytes b3040294
+ 00bd98fc bytes a9040294
- 00bd951c ["INT_ADD", "register:40f0:8", ["const:bd951c:8", "const:4:8"]]
- 00bd951c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9944 ["INT_ADD", "register:40f0:8", ["const:bd9944:8", "const:4:8"]]
+ 00bd9944 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd951c bytes b9050294
+ 00bd9944 bytes af050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc46da1ac6ab04f208902ade7bd8745"></a>

### [`00bd95a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd95a4.md) → [`00bd99cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd99cc.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

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
      "definition_site": "00bd9a08",
      "incomplete_value": false,
      "site": "00bd9a0c",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9a34",
      "incomplete_value": true,
      "site": "00bd9a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9a38",
      "incomplete_value": true,
      "site": "00bd9a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd99ec",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd99f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd96b0"
      ]
    ],
    [
      "00bd9a08",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd99ec",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd99f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9ad8"
      ]
    ],
    [
      "00bd9a08",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd95e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd95a4.md#insn-00bd95e4) · [`00bd9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd95a4.md#insn-00bd9620) · [`00bd9668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd95a4.md#insn-00bd9668)
- 新版 `00bd9a0c`（命令位置の公開資料なし） · `00bd9a48`（命令位置の公開資料なし） · `00bd9a90`（命令位置の公開資料なし）

~~~diff
- 00bd95e4 ["INT_ADD", "register:40f0:8", ["const:bd95e4:8", "const:4:8"]]
- 00bd95e4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9a0c ["INT_ADD", "register:40f0:8", ["const:bd9a0c:8", "const:4:8"]]
+ 00bd9a0c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd95e4 bytes 87050294
+ 00bd9a0c bytes 7d050294
- 00bd9620 ["INT_ADD", "register:40f0:8", ["const:bd9620:8", "const:4:8"]]
- 00bd9620 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bd9a48 ["INT_ADD", "register:40f0:8", ["const:bd9a48:8", "const:4:8"]]
+ 00bd9a48 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd9620 bytes 60040294
+ 00bd9a48 bytes 56040294
- 00bd9668 ["INT_ADD", "register:40f0:8", ["const:bd9668:8", "const:4:8"]]
- 00bd9668 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9a90 ["INT_ADD", "register:40f0:8", ["const:bd9a90:8", "const:4:8"]]
+ 00bd9a90 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9668 bytes 66050294
+ 00bd9a90 bytes 5c050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0043d3b6562e1a9dc63f82823ad5d4d"></a>

### [`00bd96f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd96f0.md) → [`00bd9b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9b18.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5d0.md) · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5a9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9d0.md) · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 59.38% / 新版 52.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9b54",
      "incomplete_value": false,
      "site": "00bd9b58",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9794"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
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
      "00bd9b30",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9b54",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd9790",
      "PARAM",
      [
        "storage",
        "002b7dd0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9b30",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9b54",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd9bb8",
      "PARAM",
      [
        "storage",
        "002b7e10",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd96f0.md#insn-00bd9730) · [`00bd9794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd96f0.md#insn-00bd9794) · [`00bd97a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd96f0.md#insn-00bd97a0)
- 新版 `00bd9b58`（命令位置の公開資料なし） · `00bd9bc8`（命令位置の公開資料なし）

~~~diff
- 00bd9730 ["INT_ADD", "register:40f0:8", ["const:bd9730:8", "const:4:8"]]
- 00bd9730 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9b58 ["INT_ADD", "register:40f0:8", ["const:bd9b58:8", "const:4:8"]]
+ 00bd9b58 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9730 bytes 34050294
+ 00bd9b58 bytes 2a050294
- 00bd9794 ["INT_ADD", "register:40f0:8", ["const:bd9794:8", "const:4:8"]]
- 00bd9794 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bd9794 bytes 43040294
- 00bd97a0 ["INT_ADD", "register:40f0:8", ["const:bd97a0:8", "const:4:8"]]
- 00bd97a0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9bc8 ["INT_ADD", "register:40f0:8", ["const:bd9bc8:8", "const:4:8"]]
+ 00bd9bc8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd97a0 bytes 18050294
+ 00bd9bc8 bytes 0e050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696e0b423749341e629760127dbdf8f0"></a>

### [`00bd9894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md) → [`00bd9cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9cbc.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 86.75% / 新版 86.75%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9cf8",
      "incomplete_value": false,
      "site": "00bd9cfc",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9d24",
      "incomplete_value": true,
      "site": "00bd9d38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9d28",
      "incomplete_value": true,
      "site": "00bd9d38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd9cdc",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd99a0"
      ]
    ],
    [
      "00bd9cf8",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9cdc",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9dc8"
      ]
    ],
    [
      "00bd9cf8",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd98d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md#insn-00bd98d4) · [`00bd9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md#insn-00bd9910) · [`00bd9958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md#insn-00bd9958)
- 新版 `00bd9cfc`（命令位置の公開資料なし） · `00bd9d38`（命令位置の公開資料なし） · `00bd9d80`（命令位置の公開資料なし）

~~~diff
- 00bd98d4 ["INT_ADD", "register:40f0:8", ["const:bd98d4:8", "const:4:8"]]
- 00bd98d4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9cfc ["INT_ADD", "register:40f0:8", ["const:bd9cfc:8", "const:4:8"]]
+ 00bd9cfc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd98d4 bytes cb040294
+ 00bd9cfc bytes c1040294
- 00bd9910 ["INT_ADD", "register:40f0:8", ["const:bd9910:8", "const:4:8"]]
- 00bd9910 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bd9d38 ["INT_ADD", "register:40f0:8", ["const:bd9d38:8", "const:4:8"]]
+ 00bd9d38 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd9910 bytes a4030294
+ 00bd9d38 bytes 9a030294
- 00bd9958 ["INT_ADD", "register:40f0:8", ["const:bd9958:8", "const:4:8"]]
- 00bd9958 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9d80 ["INT_ADD", "register:40f0:8", ["const:bd9d80:8", "const:4:8"]]
+ 00bd9d80 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9958 bytes aa040294
+ 00bd9d80 bytes a0040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce3317b8ec2d40afa2f88779b1843923"></a>

### [`00bd99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd99e0.md) → [`00bd9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9e08.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 85.71% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9e4c",
      "incomplete_value": false,
      "site": "00bd9e50",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9e90",
      "incomplete_value": true,
      "site": "00bd9ea8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9e94",
      "incomplete_value": true,
      "site": "00bd9ea8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bd9e30",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9b24"
      ]
    ],
    [
      "00bd9e4c",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9e30",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9f4c"
      ]
    ],
    [
      "00bd9e4c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd99e0.md#insn-00bd9a28) · [`00bd9a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd99e0.md#insn-00bd9a80) · [`00bd9adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd99e0.md#insn-00bd9adc)
- 新版 `00bd9e50`（命令位置の公開資料なし） · `00bd9ea8`（命令位置の公開資料なし） · `00bd9f04`（命令位置の公開資料なし）

~~~diff
- 00bd9a28 ["INT_ADD", "register:40f0:8", ["const:bd9a28:8", "const:4:8"]]
- 00bd9a28 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9e50 ["INT_ADD", "register:40f0:8", ["const:bd9e50:8", "const:4:8"]]
+ 00bd9e50 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9a28 bytes 76040294
+ 00bd9e50 bytes 6c040294
- 00bd9a80 ["INT_ADD", "register:40f0:8", ["const:bd9a80:8", "const:4:8"]]
- 00bd9a80 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bd9ea8 ["INT_ADD", "register:40f0:8", ["const:bd9ea8:8", "const:4:8"]]
+ 00bd9ea8 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd9a80 bytes 48030294
+ 00bd9ea8 bytes 3e030294
- 00bd9adc ["INT_ADD", "register:40f0:8", ["const:bd9adc:8", "const:4:8"]]
- 00bd9adc ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9f04 ["INT_ADD", "register:40f0:8", ["const:bd9f04:8", "const:4:8"]]
+ 00bd9f04 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9adc bytes 49040294
+ 00bd9f04 bytes 3f040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26227a0bcbf346bb5f6fbe0b1523407"></a>

### [`00bd9b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9b64.md) → [`00bd9f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9f8c.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9fdc",
      "incomplete_value": false,
      "site": "00bd9fe0",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda038",
      "incomplete_value": true,
      "site": "00bda054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda03c",
      "incomplete_value": true,
      "site": "00bda054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9c14",
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
                "const:738:8"
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
      "00bd9fc0",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9ce4"
      ]
    ],
    [
      "00bd9fdc",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9fc0",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda10c"
      ]
    ],
    [
      "00bd9fdc",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9b64.md#insn-00bd9bb8) · [`00bd9c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9b64.md#insn-00bd9c2c) · [`00bd9c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9b64.md#insn-00bd9c9c)
- 新版 `00bd9fe0`（命令位置の公開資料なし） · `00bda054`（命令位置の公開資料なし） · `00bda0c4`（命令位置の公開資料なし）

~~~diff
- 00bd9bb8 ["INT_ADD", "register:40f0:8", ["const:bd9bb8:8", "const:4:8"]]
- 00bd9bb8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd9fe0 ["INT_ADD", "register:40f0:8", ["const:bd9fe0:8", "const:4:8"]]
+ 00bd9fe0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9bb8 bytes 12040294
+ 00bd9fe0 bytes 08040294
- 00bd9c2c ["INT_ADD", "register:40f0:8", ["const:bd9c2c:8", "const:4:8"]]
- 00bd9c2c ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bda054 ["INT_ADD", "register:40f0:8", ["const:bda054:8", "const:4:8"]]
+ 00bda054 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd9c2c bytes dd020294
+ 00bda054 bytes d3020294
- 00bd9c9c ["INT_ADD", "register:40f0:8", ["const:bd9c9c:8", "const:4:8"]]
- 00bd9c9c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda0c4 ["INT_ADD", "register:40f0:8", ["const:bda0c4:8", "const:4:8"]]
+ 00bda0c4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9c9c bytes d9030294
+ 00bda0c4 bytes cf030294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bda8a11e8a34e85750bdc74b3fd69164"></a>

### [`00bd9d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9d28.md) → [`00bda150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda1a4",
      "incomplete_value": false,
      "site": "00bda1a8",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda200",
      "incomplete_value": true,
      "site": "00bda214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda204",
      "incomplete_value": true,
      "site": "00bda214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bda184",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9ebc"
      ]
    ],
    [
      "00bda1a4",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda184",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda2e4"
      ]
    ],
    [
      "00bda1a4",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9d28.md#insn-00bd9d80) · [`00bd9dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9d28.md#insn-00bd9dec) · [`00bd9e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9d28.md#insn-00bd9e18)
- 新版 `00bda1a8`（命令位置の公開資料なし） · `00bda214`（命令位置の公開資料なし） · `00bda240`（命令位置の公開資料なし）

~~~diff
- 00bd9d80 ["INT_ADD", "register:40f0:8", ["const:bd9d80:8", "const:4:8"]]
- 00bd9d80 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda1a8 ["INT_ADD", "register:40f0:8", ["const:bda1a8:8", "const:4:8"]]
+ 00bda1a8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd9d80 bytes a0030294
+ 00bda1a8 bytes 96030294
- 00bd9dec ["INT_ADD", "register:40f0:8", ["const:bd9dec:8", "const:4:8"]]
- 00bd9dec ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bda214 ["INT_ADD", "register:40f0:8", ["const:bda214:8", "const:4:8"]]
+ 00bda214 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bd9dec bytes 6d020294
+ 00bda214 bytes 63020294
- 00bd9e18 ["INT_ADD", "register:40f0:8", ["const:bd9e18:8", "const:4:8"]]
- 00bd9e18 ["CALL", null, ["callee:00497834:8"]]
+ 00bda240 ["INT_ADD", "register:40f0:8", ["const:bda240:8", "const:4:8"]]
+ 00bda240 ["CALL", null, ["callee:00497834:8"]]
- 00bd9e18 bytes 77f6e297
+ 00bda240 bytes 7df5e297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

