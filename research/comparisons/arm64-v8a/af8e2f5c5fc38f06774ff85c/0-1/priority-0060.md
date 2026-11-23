# v15.7.2 → v15.7.3 · 最優先の変更候補 (60)

[一覧の目次](README.md)

<a id="compare-b501e7d625ef14444f3604c3712740fe"></a>

### [`00ae996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae996c.md) → [`00ae9a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a34.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9a60",
      "incomplete_value": true,
      "site": "00ae9a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9998",
      "incomplete_value": true,
      "site": "00ae9998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "definition_site": "00ae9a48",
      "incomplete_value": true,
      "site": "00ae9a48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9980",
      "incomplete_value": true,
      "site": "00ae9980",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9a54",
      "incomplete_value": false,
      "site": "00ae9a58",
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
            "const:68b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae998c",
      "incomplete_value": false,
      "site": "00ae9990",
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
      "00ae9a44",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9a54",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9a60",
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9a44",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9a54",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9a60",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae996c.md#insn-00ae9990) · [`00ae9998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae996c.md#insn-00ae9998) · [`00ae997c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae996c.md#insn-00ae997c)
- 新版 `00ae9a58`（命令位置の公開資料なし） · `00ae9a60`（命令位置の公開資料なし） · `00ae9a44`（命令位置の公開資料なし）

~~~diff
- 00ae9990 ["INT_ADD", "register:40f0:8", ["const:ae9990:8", "const:4:8"]]
- 00ae9990 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9a58 ["INT_ADD", "register:40f0:8", ["const:ae9a58:8", "const:4:8"]]
+ 00ae9a58 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9990 bytes 80d10394
+ 00ae9a58 bytes 7ad10394
- 00ae9998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00ae9998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9a60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00ae9a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9998 bytes 602a03f9
+ 00ae9a60 bytes 608a03f9
- 00ae997c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00ae997c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00ae9a44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae997c bytes 682a43f9
+ 00ae9a44 bytes 688a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab5e360c0fb5ecfbb3f9f673b7df38a"></a>

### [`00ae99ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae99ec.md) → [`00ae9ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ab4.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae99ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae99f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae99f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae99ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae99f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae9ac4",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae9ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae9ac4",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae99ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae99ec.md#insn-00ae99ec) · [`00ae99f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae99ec.md#insn-00ae99f0) · [`00ae9a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae99ec.md#insn-00ae9a00)
- 新版 `00ae9ac8`（命令位置の公開資料なし）

~~~diff
- 00ae99ec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae99ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae99ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae99ec bytes f30f1ef8
- 00ae99f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae99f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae99f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae99f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae99f0 bytes fd7b01a9
- 00ae9a00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae9a00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae9ac8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae9ac8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9a00 bytes 080100b5
+ 00ae9ac8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1fd684dac39e3fd0e6ec25e3ad338a4"></a>

### [`00ae9a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a30.md) → [`00ae9af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9af8.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9b28",
      "incomplete_value": true,
      "site": "00ae9b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a60",
      "incomplete_value": true,
      "site": "00ae9a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "definition_site": "00ae9b0c",
      "incomplete_value": true,
      "site": "00ae9b0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a44",
      "incomplete_value": true,
      "site": "00ae9a44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9b14",
      "incomplete_value": false,
      "site": "00ae9b20",
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
            "const:68b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a4c",
      "incomplete_value": false,
      "site": "00ae9a58",
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
      "00ae9b08",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b14",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9b28",
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9b08",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b14",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9b28",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a30.md#insn-00ae9a58) · [`00ae9a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a30.md#insn-00ae9a60) · [`00ae9a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a30.md#insn-00ae9a40)
- 新版 `00ae9b20`（命令位置の公開資料なし） · `00ae9b28`（命令位置の公開資料なし） · `00ae9b08`（命令位置の公開資料なし）

~~~diff
- 00ae9a58 ["INT_ADD", "register:40f0:8", ["const:ae9a58:8", "const:4:8"]]
- 00ae9a58 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9b20 ["INT_ADD", "register:40f0:8", ["const:ae9b20:8", "const:4:8"]]
+ 00ae9b20 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9a58 bytes 4ed10394
+ 00ae9b20 bytes 48d10394
- 00ae9a60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00ae9a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00ae9b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9a60 bytes 602a03f9
+ 00ae9b28 bytes 608a03f9
- 00ae9a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00ae9a40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00ae9b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9a40 bytes 682a43f9
+ 00ae9b08 bytes 688a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d742f3acafb3ff71b1c8ea653debe76"></a>

### [`00ae9a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a80.md) → [`00ae9b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9b48.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9bd0",
      "incomplete_value": true,
      "site": "00ae9bd0",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b08",
      "incomplete_value": true,
      "site": "00ae9b08",
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
            "const:658:8"
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
      "definition_site": "00ae9b7c",
      "incomplete_value": true,
      "site": "00ae9b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ab4",
      "incomplete_value": true,
      "site": "00ae9ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:650:8"
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
      "site": "00ae9ad4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9b5c",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9ab4",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9bd0",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9b5c",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9b7c",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9bd0",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a80.md#insn-00ae9ac0) · [`00ae9ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a80.md#insn-00ae9ad4) · [`00ae9b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9a80.md#insn-00ae9b08)
- 新版 `00ae9b88`（命令位置の公開資料なし） · `00ae9bd0`（命令位置の公開資料なし）

~~~diff
- 00ae9ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9ac0 ["INT_ADD", "register:40f0:8", ["const:ae9ac0:8", "const:4:8"]]
- 00ae9ac0 ["CALLIND", null, ["register:0:8"]]
+ 00ae9b88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9b88 ["INT_ADD", "register:40f0:8", ["const:ae9b88:8", "const:4:8"]]
+ 00ae9b88 ["CALLIND", null, ["register:0:8"]]
- 00ae9ac0 bytes 00013fd6
+ 00ae9b88 bytes 00013fd6
- 00ae9ad4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9ad4 ["INT_ADD", "register:40f0:8", ["const:ae9ad4:8", "const:4:8"]]
- 00ae9ad4 ["CALLIND", null, ["register:0:8"]]
- 00ae9ad4 bytes 00013fd6
- 00ae9b08 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9b08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:658:8"]]
- 00ae9b08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9bd0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9bd0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:718:8"]]
+ 00ae9bd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9b08 bytes a0621939
+ 00ae9bd0 bytes a0621c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991509299da8f12774757188d7e6e8b6"></a>

### [`00ae9b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9b1c.md) → [`00ae9be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9be4.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 30.00% / 新版 27.27%

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
      "site": "00ae9b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9c20"
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
      "00ae9bf8",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c04",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9b58",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9bf8",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c04",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9c20",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9b1c.md#insn-00ae9b34) · [`00ae9b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9b1c.md#insn-00ae9b58) · [`00ae9b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9b1c.md#insn-00ae9b90)
- 新版 `00ae9bfc`（命令位置の公開資料なし）

~~~diff
- 00ae9b34 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9b34 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae9bfc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae9bfc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae9b34 bytes c10300b4
+ 00ae9bfc bytes c10300b4
- 00ae9b58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9b58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9b58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:658:8"]]
- 00ae9b58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9b58 bytes bf621939
- 00ae9b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9b90 ["INT_ADD", "register:40f0:8", ["const:ae9b90:8", "const:4:8"]]
- 00ae9b90 ["CALLIND", null, ["register:0:8"]]
- 00ae9b90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e050f11e57ecde5325a2b082dfff89a6"></a>

### [`00ae9bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9bbc.md) → [`00ae9c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae9bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9cc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9bd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9bd0",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9bd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9cc8"
      ]
    ],
    [
      "unmatched:00ae9be0",
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
      "00ae9c98",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9cc8"
      ]
    ],
    [
      "00ae9ca8",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9bbc.md#insn-00ae9bd8) · [`00ae9bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9bbc.md#insn-00ae9bf4) · [`00ae9bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9bbc.md#insn-00ae9bfc)
- 新版 `00ae9cbc`（命令位置の公開資料なし）

~~~diff
- 00ae9bd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9bd8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9bd8 bytes 410100b5
- 00ae9bf4 ["INT_ADD", "register:40f0:8", ["const:ae9bf4:8", "const:4:8"]]
- 00ae9bf4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9cbc ["INT_ADD", "register:40f0:8", ["const:ae9cbc:8", "const:4:8"]]
+ 00ae9cbc ["CALL", null, ["callee:00bde040:8"]]
- 00ae9bf4 bytes e7d00394
+ 00ae9cbc bytes e1d00394
- 00ae9bfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
- 00ae9bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9bfc bytes 802a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b105f9eeec184c178d1e6b9327b571"></a>

### [`00ae9c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9c68.md) → [`00ae9d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9d30.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae9ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9d70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9c84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9c7c",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9d74"
      ]
    ],
    [
      "unmatched:00ae9c8c",
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
      "00ae9d44",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9d74"
      ]
    ],
    [
      "00ae9d54",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9c68.md#insn-00ae9c84) · [`00ae9ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9c68.md#insn-00ae9ca0) · [`00ae9ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9c68.md#insn-00ae9ca8)
- 新版 `00ae9d68`（命令位置の公開資料なし）

~~~diff
- 00ae9c84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9c84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9c84 bytes 410100b5
- 00ae9ca0 ["INT_ADD", "register:40f0:8", ["const:ae9ca0:8", "const:4:8"]]
- 00ae9ca0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9d68 ["INT_ADD", "register:40f0:8", ["const:ae9d68:8", "const:4:8"]]
+ 00ae9d68 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9ca0 bytes bcd00394
+ 00ae9d68 bytes b6d00394
- 00ae9ca8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
- 00ae9ca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9ca8 bytes 802a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98eba6aae4c17c6a69cc158cef1fa4f"></a>

### [`00ae9cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9cd8.md) → [`00ae9da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9da0.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00ae9dbc",
      "incomplete_value": false,
      "site": "00ae9dc0",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9cf4",
      "incomplete_value": false,
      "site": "00ae9cf8",
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
      "definition_site": "00ae9dcc",
      "incomplete_value": true,
      "site": "00ae9dd8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9d04",
      "incomplete_value": true,
      "site": "00ae9d10",
      "value": [
        "LOAD",
        "8",
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
      "00ae9dbc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae9dcc",
      "DATA",
      [
        "storage",
        "010a0678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae9dbc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae9dcc",
      "DATA",
      [
        "storage",
        "010a0738",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9cd8.md#insn-00ae9cf8) · [`00ae9cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9cd8.md#insn-00ae9cf4) · [`00ae9d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9cd8.md#insn-00ae9d00)
- 新版 `00ae9dc0`（命令位置の公開資料なし） · `00ae9dbc`（命令位置の公開資料なし） · `00ae9dc8`（命令位置の公開資料なし）

~~~diff
- 00ae9cf8 ["INT_ADD", "register:40f0:8", ["const:ae9cf8:8", "const:4:8"]]
- 00ae9cf8 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae9dc0 ["INT_ADD", "register:40f0:8", ["const:ae9dc0:8", "const:4:8"]]
+ 00ae9dc0 ["CALL", null, ["callee:00bde130:8"]]
- 00ae9cf8 bytes e2d00394
+ 00ae9dc0 bytes dcd00394
- 00ae9cf4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae9cf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9cf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9cf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9dbc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae9dbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9dbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9dbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9cf4 bytes 00c81791
+ 00ae9dbc bytes 00fc1991
- 00ae9d00 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00ae9d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9dc8 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00ae9dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9d00 bytes 08e11991
+ 00ae9dc8 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da2e9d2a23cd7d4045d999017980fbc"></a>

### [`00ae9d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d14.md) → [`00ae9ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ddc.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9e08",
      "incomplete_value": true,
      "site": "00ae9e08",
      "value": [
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
    "old": {
      "definition_site": "00ae9d40",
      "incomplete_value": true,
      "site": "00ae9d40",
      "value": [
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
      "definition_site": "00ae9df0",
      "incomplete_value": true,
      "site": "00ae9df0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d28",
      "incomplete_value": true,
      "site": "00ae9d28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9dfc",
      "incomplete_value": false,
      "site": "00ae9e00",
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
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d34",
      "incomplete_value": false,
      "site": "00ae9d38",
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
            "const:32:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9dec",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9dfc",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ],
    [
      "00ae9e08",
      "WRITE",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9dec",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9dfc",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9e08",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d14.md#insn-00ae9d38) · [`00ae9d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d14.md#insn-00ae9d40) · [`00ae9d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d14.md#insn-00ae9d24)
- 新版 `00ae9e00`（命令位置の公開資料なし） · `00ae9e08`（命令位置の公開資料なし） · `00ae9dec`（命令位置の公開資料なし）

~~~diff
- 00ae9d38 ["INT_ADD", "register:40f0:8", ["const:ae9d38:8", "const:4:8"]]
- 00ae9d38 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9e00 ["INT_ADD", "register:40f0:8", ["const:ae9e00:8", "const:4:8"]]
+ 00ae9e00 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9d38 bytes 96d00394
+ 00ae9e00 bytes 90d00394
- 00ae9d40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9d40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9e08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9d40 bytes 604203f9
+ 00ae9e08 bytes 60a203f9
- 00ae9d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9dec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9dec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9d24 bytes 684243f9
+ 00ae9dec bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-370a5ed8e61834b0ff5afd2101747062"></a>

### [`00ae9d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d54.md) → [`00ae9e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e1c.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9e48",
      "incomplete_value": true,
      "site": "00ae9e48",
      "value": [
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
    "old": {
      "definition_site": "00ae9d80",
      "incomplete_value": true,
      "site": "00ae9d80",
      "value": [
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
      "definition_site": "00ae9e30",
      "incomplete_value": true,
      "site": "00ae9e30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d68",
      "incomplete_value": true,
      "site": "00ae9d68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9e38",
      "incomplete_value": false,
      "site": "00ae9e40",
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
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d70",
      "incomplete_value": false,
      "site": "00ae9d78",
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
            "const:32:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9e2c",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e38",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ],
    [
      "00ae9e48",
      "WRITE",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9e2c",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e38",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9e48",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d54.md#insn-00ae9d78) · [`00ae9d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d54.md#insn-00ae9d80) · [`00ae9d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d54.md#insn-00ae9d64)
- 新版 `00ae9e40`（命令位置の公開資料なし） · `00ae9e48`（命令位置の公開資料なし） · `00ae9e2c`（命令位置の公開資料なし）

~~~diff
- 00ae9d78 ["INT_ADD", "register:40f0:8", ["const:ae9d78:8", "const:4:8"]]
- 00ae9d78 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9e40 ["INT_ADD", "register:40f0:8", ["const:ae9e40:8", "const:4:8"]]
+ 00ae9e40 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9d78 bytes 86d00394
+ 00ae9e40 bytes 80d00394
- 00ae9d80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9e48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9d80 bytes 604203f9
+ 00ae9e48 bytes 60a203f9
- 00ae9d64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9e2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9d64 bytes 684243f9
+ 00ae9e2c bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffb903f2d90aeba650d4fe33663653a4"></a>

### [`00ae9d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d94.md) → [`00ae9e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e5c.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae9dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9e8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9e70",
      "incomplete_value": true,
      "site": "00ae9e70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9da8",
      "incomplete_value": true,
      "site": "00ae9da8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00ae9e6c",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9db4",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae9dbc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae9e6c",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e7c",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9e84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d94.md#insn-00ae9da8) · [`00ae9dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d94.md#insn-00ae9dbc) · [`00ae9dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d94.md#insn-00ae9dc4)
- 新版 `00ae9e70`（命令位置の公開資料なし）

~~~diff
- 00ae9da8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae9da8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae9e70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae9e70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9da8 bytes 080100b5
+ 00ae9e70 bytes 080100b5
- 00ae9dbc ["INT_ADD", "register:40f0:8", ["const:ae9dbc:8", "const:4:8"]]
- 00ae9dbc ["CALL", null, ["callee:00bde040:8"]]
- 00ae9dbc bytes 75d00394
- 00ae9dc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9dc4 bytes 604203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c7b84f024c7da79172d1d171d68ce7"></a>

### [`00ae9dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9dd8.md) → [`00ae9ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ea0.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e08",
      "incomplete_value": true,
      "site": "00ae9e08",
      "value": [
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
    "old": {
      "definition_site": "00ae9dec",
      "incomplete_value": true,
      "site": "00ae9dec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9ebc",
      "incomplete_value": false,
      "site": "00ae9ec8",
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
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9df4",
      "incomplete_value": false,
      "site": "00ae9e00",
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
            "const:32:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9eb0",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ebc",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ],
    [
      "00ae9ed0",
      "WRITE",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9eb0",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ebc",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9ed0",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9dd8.md#insn-00ae9e00) · [`00ae9e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9dd8.md#insn-00ae9e08) · [`00ae9de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9dd8.md#insn-00ae9de8)
- 新版 `00ae9ec8`（命令位置の公開資料なし） · `00ae9ed0`（命令位置の公開資料なし） · `00ae9eb0`（命令位置の公開資料なし）

~~~diff
- 00ae9e00 ["INT_ADD", "register:40f0:8", ["const:ae9e00:8", "const:4:8"]]
- 00ae9e00 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9ec8 ["INT_ADD", "register:40f0:8", ["const:ae9ec8:8", "const:4:8"]]
+ 00ae9ec8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9e00 bytes 64d00394
+ 00ae9ec8 bytes 5ed00394
- 00ae9e08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e08 bytes 604203f9
+ 00ae9ed0 bytes 60a203f9
- 00ae9de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9de8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00ae9eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9de8 bytes 684243f9
+ 00ae9eb0 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e5610c6115056c573d7636f38af6fd"></a>

### [`00ae9e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9e28.md) → [`00ae9ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ef0.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9eb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9f78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9f24",
      "incomplete_value": true,
      "site": "00ae9f30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e5c",
      "incomplete_value": true,
      "site": "00ae9e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ae9f04",
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9e5c",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9eb0",
      "WRITE",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9f04",
      "READ",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9f24",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9f78",
      "WRITE",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9e28.md#insn-00ae9e68) · [`00ae9eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9e28.md#insn-00ae9eb0)
- 新版 `00ae9f30`（命令位置の公開資料なし） · `00ae9f78`（命令位置の公開資料なし）

~~~diff
- 00ae9e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9e68 ["INT_ADD", "register:40f0:8", ["const:ae9e68:8", "const:4:8"]]
- 00ae9e68 ["CALLIND", null, ["register:0:8"]]
+ 00ae9f30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9f30 ["INT_ADD", "register:40f0:8", ["const:ae9f30:8", "const:4:8"]]
+ 00ae9f30 ["CALLIND", null, ["register:0:8"]]
- 00ae9e68 bytes 00013fd6
+ 00ae9f30 bytes 00013fd6
- 00ae9eb0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9eb0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
- 00ae9eb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9eb0 bytes a0221a39
+ 00ae9f78 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9f78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
+ 00ae9f78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9f78 bytes a0221d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4488b33196af07737448d166ab6069"></a>

### [`00ae9ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9ec4.md) → [`00ae9f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9f8c.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 30.00% / 新版 30.00%

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
      "site": "00ae9f00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea018",
      "incomplete_value": true,
      "site": "00aea018",
      "value": [
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
    "old": {
      "definition_site": "00ae9f50",
      "incomplete_value": true,
      "site": "00ae9f50",
      "value": [
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9fc8"
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
      "00ae9fa0",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9fac",
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9f00",
      "WRITE",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9fa0",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9fac",
      "READ",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9fc8",
      "WRITE",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9ec4.md#insn-00ae9f00) · [`00ae9f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9ec4.md#insn-00ae9f38) · [`00ae9f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9ec4.md#insn-00ae9f4c)
- 新版 `00aea014`（命令位置の公開資料なし）

~~~diff
- 00ae9f00 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9f00 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9f00 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
- 00ae9f00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9f00 bytes bf221a39
- 00ae9f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9f38 ["INT_ADD", "register:40f0:8", ["const:ae9f38:8", "const:4:8"]]
- 00ae9f38 ["CALLIND", null, ["register:0:8"]]
- 00ae9f38 bytes 00013fd6
- 00ae9f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9f4c ["INT_ADD", "register:40f0:8", ["const:ae9f4c:8", "const:4:8"]]
- 00ae9f4c ["CALLIND", null, ["register:0:8"]]
+ 00aea014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea014 ["INT_ADD", "register:40f0:8", ["const:aea014:8", "const:4:8"]]
+ 00aea014 ["CALLIND", null, ["register:0:8"]]
- 00ae9f4c bytes 00013fd6
+ 00aea014 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9908df9331a2f76366fdf03a8ca85591"></a>

### [`00ae9f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9f64.md) → [`00aea02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea02c.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae9fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aea06c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9f78",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aea070"
      ]
    ],
    [
      "unmatched:00ae9f88",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aea040",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aea070"
      ]
    ],
    [
      "00aea050",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9f64.md#insn-00ae9f80) · [`00ae9f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9f64.md#insn-00ae9f9c) · [`00ae9fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9f64.md#insn-00ae9fa4)
- 新版 `00aea064`（命令位置の公開資料なし）

~~~diff
- 00ae9f80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9f80 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9f80 bytes 410100b5
- 00ae9f9c ["INT_ADD", "register:40f0:8", ["const:ae9f9c:8", "const:4:8"]]
- 00ae9f9c ["CALL", null, ["callee:00bde040:8"]]
+ 00aea064 ["INT_ADD", "register:40f0:8", ["const:aea064:8", "const:4:8"]]
+ 00aea064 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9f9c bytes fdcf0394
+ 00aea064 bytes f7cf0394
- 00ae9fa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae9fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9fa4 bytes 804203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02deb8713c68e3374ab5114ec78deede"></a>

### [`00ae9fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9fd4.md) → [`00aea09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea09c.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde310.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3c0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea0b8",
      "incomplete_value": false,
      "site": "00aea0bc",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ff0",
      "incomplete_value": false,
      "site": "00ae9ff4",
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
      "definition_site": "00aea0c8",
      "incomplete_value": true,
      "site": "00aea0d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea000",
      "incomplete_value": true,
      "site": "00aea00c",
      "value": [
        "LOAD",
        "8",
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
      "00aea0b8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea0c8",
      "DATA",
      [
        "storage",
        "010a0690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea0b8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea0c8",
      "DATA",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9fd4.md#insn-00ae9ff4) · [`00ae9ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9fd4.md#insn-00ae9ff0) · [`00ae9ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9fd4.md#insn-00ae9ffc)
- 新版 `00aea0bc`（命令位置の公開資料なし） · `00aea0b8`（命令位置の公開資料なし） · `00aea0c4`（命令位置の公開資料なし）

~~~diff
- 00ae9ff4 ["INT_ADD", "register:40f0:8", ["const:ae9ff4:8", "const:4:8"]]
- 00ae9ff4 ["CALL", null, ["callee:00bde130:8"]]
+ 00aea0bc ["INT_ADD", "register:40f0:8", ["const:aea0bc:8", "const:4:8"]]
+ 00aea0bc ["CALL", null, ["callee:00bde130:8"]]
- 00ae9ff4 bytes 23d00394
+ 00aea0bc bytes 1dd00394
- 00ae9ff0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae9ff0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9ff0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9ff0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea0b8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aea0b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea0b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea0b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9ff0 bytes 001c1591
+ 00aea0b8 bytes 00501791
- 00ae9ffc ["COPY", "tmp:0:8", ["const:690:8"]]
- 00ae9ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea0c4 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00aea0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9ffc bytes 08411a91
+ 00aea0c4 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeb180f4ab07108f5ff3de28cc868cd6"></a>

### [`00aea010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea010.md) → [`00aea0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea0d8.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea118",
      "incomplete_value": true,
      "site": "00aea118",
      "value": [
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
    "old": {
      "definition_site": "00aea050",
      "incomplete_value": true,
      "site": "00aea050",
      "value": [
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
      "definition_site": "00aea0f4",
      "incomplete_value": true,
      "site": "00aea0f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea02c",
      "incomplete_value": true,
      "site": "00aea02c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea0fc",
      "incomplete_value": false,
      "site": "00aea110",
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
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea034",
      "incomplete_value": false,
      "site": "00aea048",
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
            "const:32:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea0ec",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea0fc",
      "PARAM",
      [
        "storage",
        "002a7032",
        null,
        "string"
      ]
    ],
    [
      "00aea118",
      "WRITE",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea0ec",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea0fc",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00aea118",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea010.md#insn-00aea048) · [`00aea050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea010.md#insn-00aea050) · [`00aea024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea010.md#insn-00aea024)
- 新版 `00aea110`（命令位置の公開資料なし） · `00aea118`（命令位置の公開資料なし） · `00aea0ec`（命令位置の公開資料なし）

~~~diff
- 00aea048 ["INT_ADD", "register:40f0:8", ["const:aea048:8", "const:4:8"]]
- 00aea048 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea110 ["INT_ADD", "register:40f0:8", ["const:aea110:8", "const:4:8"]]
+ 00aea110 ["CALL", null, ["callee:00bde040:8"]]
- 00aea048 bytes d2cf0394
+ 00aea110 bytes cccf0394
- 00aea050 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00aea050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea118 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00aea118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea050 bytes 804203f9
+ 00aea118 bytes 80a203f9
- 00aea024 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00aea024 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea0ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00aea0ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea024 bytes 814243f9
+ 00aea0ec bytes 81a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97ac52667ee39360fabaf8555135558"></a>

### [`00aea080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea080.md) → [`00aea148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea148.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea164",
      "incomplete_value": false,
      "site": "00aea168",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea09c",
      "incomplete_value": false,
      "site": "00aea0a0",
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
      "definition_site": "00aea174",
      "incomplete_value": true,
      "site": "00aea180",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea0ac",
      "incomplete_value": true,
      "site": "00aea0b8",
      "value": [
        "LOAD",
        "8",
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
      "00aea164",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea174",
      "DATA",
      [
        "storage",
        "010a06a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea164",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea174",
      "DATA",
      [
        "storage",
        "010a0760",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea080.md#insn-00aea0a0) · [`00aea09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea080.md#insn-00aea09c) · [`00aea0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea080.md#insn-00aea0a8)
- 新版 `00aea168`（命令位置の公開資料なし） · `00aea164`（命令位置の公開資料なし） · `00aea170`（命令位置の公開資料なし）

~~~diff
- 00aea0a0 ["INT_ADD", "register:40f0:8", ["const:aea0a0:8", "const:4:8"]]
- 00aea0a0 ["CALL", null, ["callee:00bde130:8"]]
+ 00aea168 ["INT_ADD", "register:40f0:8", ["const:aea168:8", "const:4:8"]]
+ 00aea168 ["CALL", null, ["callee:00bde130:8"]]
- 00aea0a0 bytes f8cf0394
+ 00aea168 bytes f2cf0394
- 00aea09c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea09c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea09c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea09c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea164 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aea164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea09c bytes 00c81791
+ 00aea164 bytes 00fc1991
- 00aea0a8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00aea0a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea0a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea0a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea170 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00aea170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea0a8 bytes 08811a91
+ 00aea170 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89faadfaec4308dee2a7b0126ede472d"></a>

### [`00aea0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0bc.md) → [`00aea184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea1b0",
      "incomplete_value": true,
      "site": "00aea1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea0e8",
      "incomplete_value": true,
      "site": "00aea0e8",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea198",
      "incomplete_value": true,
      "site": "00aea198",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea0d0",
      "incomplete_value": true,
      "site": "00aea0d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea0d0"
      ],
      [
        "FALL_THROUGH",
        "00aea198"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea198",
      "incomplete_value": true,
      "site": "00aea1b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea0d0",
      "incomplete_value": true,
      "site": "00aea0e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea194",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1b0",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea194",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1b0",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0bc.md#insn-00aea0e8) · [`00aea0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0bc.md#insn-00aea0cc) · [`00aea0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0bc.md#insn-00aea0e0)
- 新版 `00aea1b0`（命令位置の公開資料なし） · `00aea194`（命令位置の公開資料なし） · `00aea1a8`（命令位置の公開資料なし）

~~~diff
- 00aea0e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea0e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea0e8 bytes 605603f9
+ 00aea1b0 bytes 60b603f9
- 00aea0cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea0cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea194 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea194 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea0cc bytes 685643f9
+ 00aea194 bytes 68b643f9
- 00aea0e0 ["INT_ADD", "register:40f0:8", ["const:aea0e0:8", "const:4:8"]]
- 00aea0e0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea1a8 ["INT_ADD", "register:40f0:8", ["const:aea1a8:8", "const:4:8"]]
+ 00aea1a8 ["CALL", null, ["callee:00bde040:8"]]
- 00aea0e0 bytes accf0394
+ 00aea1a8 bytes a6cf0394
~~~


<a id="compare-a177cc47e8ac24e510b04c9f509bdca6"></a>

### [`00aea0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0fc.md) → [`00aea1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea1f0",
      "incomplete_value": true,
      "site": "00aea1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea128",
      "incomplete_value": true,
      "site": "00aea128",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea1d8",
      "incomplete_value": true,
      "site": "00aea1d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea110",
      "incomplete_value": true,
      "site": "00aea110",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea110"
      ],
      [
        "FALL_THROUGH",
        "00aea1d8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea1d8",
      "incomplete_value": true,
      "site": "00aea1f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea110",
      "incomplete_value": true,
      "site": "00aea128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea1d4",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1f0",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea1d4",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1f0",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0fc.md#insn-00aea128) · [`00aea10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0fc.md#insn-00aea10c) · [`00aea120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea0fc.md#insn-00aea120)
- 新版 `00aea1f0`（命令位置の公開資料なし） · `00aea1d4`（命令位置の公開資料なし） · `00aea1e8`（命令位置の公開資料なし）

~~~diff
- 00aea128 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea1f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea1f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea128 bytes 605603f9
+ 00aea1f0 bytes 60b603f9
- 00aea10c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea10c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea1d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea1d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea10c bytes 685643f9
+ 00aea1d4 bytes 68b643f9
- 00aea120 ["INT_ADD", "register:40f0:8", ["const:aea120:8", "const:4:8"]]
- 00aea120 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea1e8 ["INT_ADD", "register:40f0:8", ["const:aea1e8:8", "const:4:8"]]
+ 00aea1e8 ["CALL", null, ["callee:00bde040:8"]]
- 00aea120 bytes 9ccf0394
+ 00aea1e8 bytes 96cf0394
~~~


<a id="compare-5457a5307abda75dc29d1d8738a55582"></a>

### [`00aea13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea13c.md) → [`00aea204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea204.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea16c",
      "incomplete_value": true,
      "site": "00aea16c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea218",
      "incomplete_value": true,
      "site": "00aea218",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea150",
      "incomplete_value": true,
      "site": "00aea150",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea150"
      ],
      [
        "FALL_THROUGH",
        "00aea218"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea218",
      "incomplete_value": true,
      "site": "00aea234",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea150",
      "incomplete_value": true,
      "site": "00aea16c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea214",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea234",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea214",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea234",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea13c.md#insn-00aea16c) · [`00aea14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea13c.md#insn-00aea14c) · [`00aea164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea13c.md#insn-00aea164)
- 新版 `00aea234`（命令位置の公開資料なし） · `00aea214`（命令位置の公開資料なし） · `00aea22c`（命令位置の公開資料なし）

~~~diff
- 00aea16c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea16c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea16c bytes 605603f9
+ 00aea234 bytes 60b603f9
- 00aea14c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea14c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea214 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea214 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea14c bytes 685643f9
+ 00aea214 bytes 68b643f9
- 00aea164 ["INT_ADD", "register:40f0:8", ["const:aea164:8", "const:4:8"]]
- 00aea164 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea22c ["INT_ADD", "register:40f0:8", ["const:aea22c:8", "const:4:8"]]
+ 00aea22c ["CALL", null, ["callee:00bde040:8"]]
- 00aea164 bytes 8bcf0394
+ 00aea22c bytes 85cf0394
~~~


<a id="compare-d4a9100ccd7d7368359de347465efefc"></a>

### [`00aea180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea180.md) → [`00aea248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea248.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea1b0",
      "incomplete_value": true,
      "site": "00aea1b0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aea194",
      "incomplete_value": true,
      "site": "00aea194",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea194"
      ],
      [
        "FALL_THROUGH",
        "00aea25c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea25c",
      "incomplete_value": true,
      "site": "00aea278",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea194",
      "incomplete_value": true,
      "site": "00aea1b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea258",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea278",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea258",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea278",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea180.md#insn-00aea1b0) · [`00aea190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea180.md#insn-00aea190) · [`00aea1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea180.md#insn-00aea1a8)
- 新版 `00aea278`（命令位置の公開資料なし） · `00aea258`（命令位置の公開資料なし） · `00aea270`（命令位置の公開資料なし）

~~~diff
- 00aea1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea1b0 bytes 605603f9
+ 00aea278 bytes 60b603f9
- 00aea190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00aea190 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
+ 00aea258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea190 bytes 685643f9
+ 00aea258 bytes 68b643f9
- 00aea1a8 ["INT_ADD", "register:40f0:8", ["const:aea1a8:8", "const:4:8"]]
- 00aea1a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea270 ["INT_ADD", "register:40f0:8", ["const:aea270:8", "const:4:8"]]
+ 00aea270 ["CALL", null, ["callee:00bde040:8"]]
- 00aea1a8 bytes 7acf0394
+ 00aea270 bytes 74cf0394
~~~


<a id="compare-aae1dbe7297a4abd1fe61ffc176e05d4"></a>

### [`00aea1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea1d0.md) → [`00aea298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aea320",
      "incomplete_value": true,
      "site": "00aea320",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea258",
      "incomplete_value": true,
      "site": "00aea258",
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
            "const:6b0:8"
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
      "definition_site": "00aea2cc",
      "incomplete_value": true,
      "site": "00aea2d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea204",
      "incomplete_value": true,
      "site": "00aea210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a8:8"
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
      "00aea2ac",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea2cc",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea320",
      "WRITE",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea2ac",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea2cc",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea320",
      "WRITE",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea1d0.md#insn-00aea210) · [`00aea258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea1d0.md#insn-00aea258) · [`00aea1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea1d0.md#insn-00aea1e4)
- 新版 `00aea2d8`（命令位置の公開資料なし） · `00aea320`（命令位置の公開資料なし） · `00aea2ac`（命令位置の公開資料なし）

~~~diff
- 00aea210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea210 ["INT_ADD", "register:40f0:8", ["const:aea210:8", "const:4:8"]]
- 00aea210 ["CALLIND", null, ["register:0:8"]]
+ 00aea2d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea2d8 ["INT_ADD", "register:40f0:8", ["const:aea2d8:8", "const:4:8"]]
+ 00aea2d8 ["CALLIND", null, ["register:0:8"]]
- 00aea210 bytes 00013fd6
+ 00aea2d8 bytes 00013fd6
- 00aea258 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea258 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6b0:8"]]
- 00aea258 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aea320 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aea320 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:770:8"]]
+ 00aea320 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea258 bytes a0c21a39
+ 00aea320 bytes a0c21d39
- 00aea1e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
- 00aea1e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aea1e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aea2ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:770:8"]]
+ 00aea2ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aea2ac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aea1e4 bytes a8c25a39
+ 00aea2ac bytes a8c25d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed426f13d0aee52b68b121b29b1fca0"></a>

### [`00aea26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea26c.md) → [`00aea334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea334.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aea370",
      "incomplete_value": true,
      "site": "00aea370",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea2a8",
      "incomplete_value": true,
      "site": "00aea2a8",
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
            "const:6b0:8"
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
      "definition_site": "00aea3c0",
      "incomplete_value": true,
      "site": "00aea3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea2f8",
      "incomplete_value": true,
      "site": "00aea2f8",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea34c",
      "incomplete_value": true,
      "site": "00aea34c",
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
      "definition_site": "00aea284",
      "incomplete_value": true,
      "site": "00aea284",
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
      "00aea348",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea354",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea370",
      "WRITE",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea348",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea354",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea370",
      "WRITE",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea26c.md#insn-00aea2a8) · [`00aea2f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea26c.md#insn-00aea2f4) · [`00aea2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea26c.md#insn-00aea2f8)
- 新版 `00aea370`（命令位置の公開資料なし） · `00aea3bc`（命令位置の公開資料なし） · `00aea3c0`（命令位置の公開資料なし）

~~~diff
- 00aea2a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea2a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea2a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6b0:8"]]
- 00aea2a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aea370 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aea370 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aea370 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:770:8"]]
+ 00aea370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea2a8 bytes bfc21a39
+ 00aea370 bytes bfc21d39
- 00aea2f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea2f4 ["INT_ADD", "register:40f0:8", ["const:aea2f4:8", "const:4:8"]]
- 00aea2f4 ["CALLIND", null, ["register:0:8"]]
+ 00aea3bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea3bc ["INT_ADD", "register:40f0:8", ["const:aea3bc:8", "const:4:8"]]
+ 00aea3bc ["CALLIND", null, ["register:0:8"]]
- 00aea2f4 bytes 00013fd6
+ 00aea3bc bytes 00013fd6
- 00aea2f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00aea2f8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aea3c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
+ 00aea3c0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aea3c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea2f8 bytes 9f5603f9
+ 00aea3c0 bytes 9fb603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc66a424046eec160e96ffe466d98fe"></a>

### [`00aea30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea30c.md) → [`00aea3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea3d4.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea414",
      "incomplete_value": true,
      "site": "00aea414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea34c",
      "incomplete_value": true,
      "site": "00aea34c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea3f0",
      "incomplete_value": true,
      "site": "00aea3f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea328",
      "incomplete_value": true,
      "site": "00aea328",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea328"
      ],
      [
        "FALL_THROUGH",
        "00aea3f0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea3f0",
      "incomplete_value": true,
      "site": "00aea414",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea328",
      "incomplete_value": true,
      "site": "00aea34c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea3e8",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea414",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea428",
      "PARAM",
      [
        "storage",
        "00c10198",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aea3e8",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea414",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea428",
      "PARAM",
      [
        "storage",
        "00c10248",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea30c.md#insn-00aea34c) · [`00aea320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea30c.md#insn-00aea320) · [`00aea344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea30c.md#insn-00aea344)
- 新版 `00aea414`（命令位置の公開資料なし） · `00aea3e8`（命令位置の公開資料なし） · `00aea40c`（命令位置の公開資料なし）

~~~diff
- 00aea34c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00aea34c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea414 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
+ 00aea414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea34c bytes 805603f9
+ 00aea414 bytes 80b603f9
- 00aea320 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00aea320 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea3e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
+ 00aea3e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea320 bytes 815643f9
+ 00aea3e8 bytes 81b643f9
- 00aea344 ["INT_ADD", "register:40f0:8", ["const:aea344:8", "const:4:8"]]
- 00aea344 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea40c ["INT_ADD", "register:40f0:8", ["const:aea40c:8", "const:4:8"]]
+ 00aea40c ["CALL", null, ["callee:00bde040:8"]]
- 00aea344 bytes 13cf0394
+ 00aea40c bytes 0dcf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70897107eb8c1575797b3be82fbc2dc8"></a>

### [`00aea37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea37c.md) → [`00aea444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea444.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea460",
      "incomplete_value": false,
      "site": "00aea464",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea398",
      "incomplete_value": false,
      "site": "00aea39c",
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
      "definition_site": "00aea470",
      "incomplete_value": true,
      "site": "00aea47c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea3a8",
      "incomplete_value": true,
      "site": "00aea3b4",
      "value": [
        "LOAD",
        "8",
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
      "00aea460",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea470",
      "DATA",
      [
        "storage",
        "010a06b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea460",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea470",
      "DATA",
      [
        "storage",
        "010a0778",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea37c.md#insn-00aea39c) · [`00aea398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea37c.md#insn-00aea398) · [`00aea3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea37c.md#insn-00aea3a4)
- 新版 `00aea464`（命令位置の公開資料なし） · `00aea460`（命令位置の公開資料なし） · `00aea46c`（命令位置の公開資料なし）

~~~diff
- 00aea39c ["INT_ADD", "register:40f0:8", ["const:aea39c:8", "const:4:8"]]
- 00aea39c ["CALL", null, ["callee:00bde130:8"]]
+ 00aea464 ["INT_ADD", "register:40f0:8", ["const:aea464:8", "const:4:8"]]
+ 00aea464 ["CALL", null, ["callee:00bde130:8"]]
- 00aea39c bytes 39cf0394
+ 00aea464 bytes 33cf0394
- 00aea398 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aea398 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea398 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea398 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea460 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aea460 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea460 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea460 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea398 bytes 001c1591
+ 00aea460 bytes 00501791
- 00aea3a4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00aea3a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea3a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea3a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea46c ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00aea46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea3a4 bytes 08e11a91
+ 00aea46c bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-926ac907db20b68bf272af64b7e1771a"></a>

### [`00aea3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea3b8.md) → [`00aea480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea480.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea4c0",
      "incomplete_value": true,
      "site": "00aea4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea3f8",
      "incomplete_value": true,
      "site": "00aea3f8",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea49c",
      "incomplete_value": true,
      "site": "00aea49c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea3d4",
      "incomplete_value": true,
      "site": "00aea3d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea3d4"
      ],
      [
        "FALL_THROUGH",
        "00aea49c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea49c",
      "incomplete_value": true,
      "site": "00aea4c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea3d4",
      "incomplete_value": true,
      "site": "00aea3f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aea494",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea4c0",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea4d8",
      "PARAM",
      [
        "storage",
        "010a06c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea494",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea4c0",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea4d8",
      "PARAM",
      [
        "storage",
        "010a0788",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea3b8.md#insn-00aea3f8) · [`00aea3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea3b8.md#insn-00aea3cc) · [`00aea3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea3b8.md#insn-00aea3f0)
- 新版 `00aea4c0`（命令位置の公開資料なし） · `00aea494`（命令位置の公開資料なし） · `00aea4b8`（命令位置の公開資料なし）

~~~diff
- 00aea3f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00aea3f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea4c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
+ 00aea4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea3f8 bytes 805603f9
+ 00aea4c0 bytes 80b603f9
- 00aea3cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00aea3cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
+ 00aea494 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea3cc bytes 815643f9
+ 00aea494 bytes 81b643f9
- 00aea3f0 ["INT_ADD", "register:40f0:8", ["const:aea3f0:8", "const:4:8"]]
- 00aea3f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea4b8 ["INT_ADD", "register:40f0:8", ["const:aea4b8:8", "const:4:8"]]
+ 00aea4b8 ["CALL", null, ["callee:00bde040:8"]]
- 00aea3f0 bytes e8ce0394
+ 00aea4b8 bytes e2ce0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aaefa178bfcb09f3eb73ad62e6c78f4"></a>

### [`00aea428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea428.md) → [`00aea4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea4f0.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea50c",
      "incomplete_value": false,
      "site": "00aea510",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea444",
      "incomplete_value": false,
      "site": "00aea448",
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
      "definition_site": "00aea51c",
      "incomplete_value": true,
      "site": "00aea528",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea454",
      "incomplete_value": true,
      "site": "00aea460",
      "value": [
        "LOAD",
        "8",
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
      "00aea50c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea51c",
      "DATA",
      [
        "storage",
        "010a06c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea50c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea51c",
      "DATA",
      [
        "storage",
        "010a0788",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea428.md#insn-00aea448) · [`00aea444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea428.md#insn-00aea444) · [`00aea450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea428.md#insn-00aea450)
- 新版 `00aea510`（命令位置の公開資料なし） · `00aea50c`（命令位置の公開資料なし） · `00aea518`（命令位置の公開資料なし）

~~~diff
- 00aea448 ["INT_ADD", "register:40f0:8", ["const:aea448:8", "const:4:8"]]
- 00aea448 ["CALL", null, ["callee:00bde130:8"]]
+ 00aea510 ["INT_ADD", "register:40f0:8", ["const:aea510:8", "const:4:8"]]
+ 00aea510 ["CALL", null, ["callee:00bde130:8"]]
- 00aea448 bytes 0ecf0394
+ 00aea510 bytes 08cf0394
- 00aea444 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea444 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea444 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea444 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea50c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aea50c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea50c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea50c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea444 bytes 00c81791
+ 00aea50c bytes 00fc1991
- 00aea450 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00aea450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea518 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00aea518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea450 bytes 08211b91
+ 00aea518 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a7ec52de23bbdc8233caaef58c77499"></a>

### [`00aea464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea464.md) → [`00aea52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea52c.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea558",
      "incomplete_value": true,
      "site": "00aea558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea490",
      "incomplete_value": true,
      "site": "00aea490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea540",
      "incomplete_value": true,
      "site": "00aea540",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea478",
      "incomplete_value": true,
      "site": "00aea478",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea54c",
      "incomplete_value": false,
      "site": "00aea550",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea484",
      "incomplete_value": false,
      "site": "00aea488",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea53c",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea54c",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea558",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea53c",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea54c",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea558",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea464.md#insn-00aea488) · [`00aea490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea464.md#insn-00aea490) · [`00aea474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea464.md#insn-00aea474)
- 新版 `00aea550`（命令位置の公開資料なし） · `00aea558`（命令位置の公開資料なし） · `00aea53c`（命令位置の公開資料なし）

~~~diff
- 00aea488 ["INT_ADD", "register:40f0:8", ["const:aea488:8", "const:4:8"]]
- 00aea488 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea550 ["INT_ADD", "register:40f0:8", ["const:aea550:8", "const:4:8"]]
+ 00aea550 ["CALL", null, ["callee:00bde040:8"]]
- 00aea488 bytes c2ce0394
+ 00aea550 bytes bcce0394
- 00aea490 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea490 bytes 606a03f9
+ 00aea558 bytes 60ca03f9
- 00aea474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea474 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea53c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea53c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea474 bytes 686a43f9
+ 00aea53c bytes 68ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b78b0cb65b2b1aecd0ca54e8b0f11a69"></a>

### [`00aea4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4a4.md) → [`00aea56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea56c.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea598",
      "incomplete_value": true,
      "site": "00aea598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4d0",
      "incomplete_value": true,
      "site": "00aea4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea580",
      "incomplete_value": true,
      "site": "00aea580",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4b8",
      "incomplete_value": true,
      "site": "00aea4b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea588",
      "incomplete_value": false,
      "site": "00aea590",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4c0",
      "incomplete_value": false,
      "site": "00aea4c8",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea57c",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea588",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea598",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea57c",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea588",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea598",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4a4.md#insn-00aea4c8) · [`00aea4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4a4.md#insn-00aea4d0) · [`00aea4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4a4.md#insn-00aea4b4)
- 新版 `00aea590`（命令位置の公開資料なし） · `00aea598`（命令位置の公開資料なし） · `00aea57c`（命令位置の公開資料なし）

~~~diff
- 00aea4c8 ["INT_ADD", "register:40f0:8", ["const:aea4c8:8", "const:4:8"]]
- 00aea4c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea590 ["INT_ADD", "register:40f0:8", ["const:aea590:8", "const:4:8"]]
+ 00aea590 ["CALL", null, ["callee:00bde040:8"]]
- 00aea4c8 bytes b2ce0394
+ 00aea590 bytes acce0394
- 00aea4d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea4d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea598 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea4d0 bytes 606a03f9
+ 00aea598 bytes 60ca03f9
- 00aea4b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea4b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea57c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea4b4 bytes 686a43f9
+ 00aea57c bytes 68ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a360c8aa8b2cadafe44c76635f0c2a4"></a>

### [`00aea4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4e4.md) → [`00aea5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5ac.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea5dc",
      "incomplete_value": true,
      "site": "00aea5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea514",
      "incomplete_value": true,
      "site": "00aea514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea5c0",
      "incomplete_value": true,
      "site": "00aea5c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4f8",
      "incomplete_value": true,
      "site": "00aea4f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea5cc",
      "incomplete_value": false,
      "site": "00aea5d4",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea504",
      "incomplete_value": false,
      "site": "00aea50c",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea5bc",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea5cc",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea5dc",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea5bc",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea5cc",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea5dc",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea50c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4e4.md#insn-00aea50c) · [`00aea514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4e4.md#insn-00aea514) · [`00aea4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4e4.md#insn-00aea4f4)
- 新版 `00aea5d4`（命令位置の公開資料なし） · `00aea5dc`（命令位置の公開資料なし） · `00aea5bc`（命令位置の公開資料なし）

~~~diff
- 00aea50c ["INT_ADD", "register:40f0:8", ["const:aea50c:8", "const:4:8"]]
- 00aea50c ["CALL", null, ["callee:00bde040:8"]]
+ 00aea5d4 ["INT_ADD", "register:40f0:8", ["const:aea5d4:8", "const:4:8"]]
+ 00aea5d4 ["CALL", null, ["callee:00bde040:8"]]
- 00aea50c bytes a1ce0394
+ 00aea5d4 bytes 9bce0394
- 00aea514 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea514 bytes 606a03f9
+ 00aea5dc bytes 60ca03f9
- 00aea4f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea4f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea5bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea5bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea4f4 bytes 686a43f9
+ 00aea5bc bytes 68ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12fddc986e35bfd8134e2753c09f415e"></a>

### [`00aea528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea528.md) → [`00aea5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5f0.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea620",
      "incomplete_value": true,
      "site": "00aea620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea558",
      "incomplete_value": true,
      "site": "00aea558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea604",
      "incomplete_value": true,
      "site": "00aea604",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea53c",
      "incomplete_value": true,
      "site": "00aea53c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea60c",
      "incomplete_value": false,
      "site": "00aea618",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea544",
      "incomplete_value": false,
      "site": "00aea550",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea600",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea60c",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea620",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea600",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea60c",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea620",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea528.md#insn-00aea550) · [`00aea558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea528.md#insn-00aea558) · [`00aea538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea528.md#insn-00aea538)
- 新版 `00aea618`（命令位置の公開資料なし） · `00aea620`（命令位置の公開資料なし） · `00aea600`（命令位置の公開資料なし）

~~~diff
- 00aea550 ["INT_ADD", "register:40f0:8", ["const:aea550:8", "const:4:8"]]
- 00aea550 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea618 ["INT_ADD", "register:40f0:8", ["const:aea618:8", "const:4:8"]]
+ 00aea618 ["CALL", null, ["callee:00bde040:8"]]
- 00aea550 bytes 90ce0394
+ 00aea618 bytes 8ace0394
- 00aea558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea558 bytes 606a03f9
+ 00aea620 bytes 60ca03f9
- 00aea538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d0:8"]]
- 00aea538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea600 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
+ 00aea600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea538 bytes 686a43f9
+ 00aea600 bytes 68ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-726a73f64c9e016538f09849431d8c7a"></a>

### [`00aea578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea578.md) → [`00aea640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea640.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aea6c8",
      "incomplete_value": true,
      "site": "00aea6c8",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea600",
      "incomplete_value": true,
      "site": "00aea600",
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
            "const:6d8:8"
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
      "definition_site": "00aea674",
      "incomplete_value": true,
      "site": "00aea680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea5ac",
      "incomplete_value": true,
      "site": "00aea5b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d0:8"
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
      "00aea654",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea674",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea6c8",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea654",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea674",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea6c8",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea578.md#insn-00aea5b8) · [`00aea600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea578.md#insn-00aea600) · [`00aea58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea578.md#insn-00aea58c)
- 新版 `00aea680`（命令位置の公開資料なし） · `00aea6c8`（命令位置の公開資料なし） · `00aea654`（命令位置の公開資料なし）

~~~diff
- 00aea5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea5b8 ["INT_ADD", "register:40f0:8", ["const:aea5b8:8", "const:4:8"]]
- 00aea5b8 ["CALLIND", null, ["register:0:8"]]
+ 00aea680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea680 ["INT_ADD", "register:40f0:8", ["const:aea680:8", "const:4:8"]]
+ 00aea680 ["CALLIND", null, ["register:0:8"]]
- 00aea5b8 bytes 00013fd6
+ 00aea680 bytes 00013fd6
- 00aea600 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea600 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6d8:8"]]
- 00aea600 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aea6c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aea6c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:798:8"]]
+ 00aea6c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea600 bytes a0621b39
+ 00aea6c8 bytes a0621e39
- 00aea58c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6d8:8"]]
- 00aea58c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aea58c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aea654 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:798:8"]]
+ 00aea654 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aea654 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aea58c bytes a8625b39
+ 00aea654 bytes a8625e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eebd3c82e76a3d118ab4e51be87fe476"></a>

### [`00aea614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea614.md) → [`00aea6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea6dc.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aea718",
      "incomplete_value": true,
      "site": "00aea718",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea650",
      "incomplete_value": true,
      "site": "00aea650",
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
            "const:6d8:8"
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
      "definition_site": "00aea768",
      "incomplete_value": true,
      "site": "00aea768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea6a0",
      "incomplete_value": true,
      "site": "00aea6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea6f4",
      "incomplete_value": true,
      "site": "00aea6f4",
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
      "definition_site": "00aea62c",
      "incomplete_value": true,
      "site": "00aea62c",
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
      "00aea6f0",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea6fc",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea718",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea6f0",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea6fc",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea718",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea614.md#insn-00aea650) · [`00aea69c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea614.md#insn-00aea69c) · [`00aea6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea614.md#insn-00aea6a0)
- 新版 `00aea718`（命令位置の公開資料なし） · `00aea764`（命令位置の公開資料なし） · `00aea768`（命令位置の公開資料なし）

~~~diff
- 00aea650 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea650 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea650 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6d8:8"]]
- 00aea650 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aea718 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aea718 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aea718 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:798:8"]]
+ 00aea718 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea650 bytes bf621b39
+ 00aea718 bytes bf621e39
- 00aea69c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea69c ["INT_ADD", "register:40f0:8", ["const:aea69c:8", "const:4:8"]]
- 00aea69c ["CALLIND", null, ["register:0:8"]]
+ 00aea764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea764 ["INT_ADD", "register:40f0:8", ["const:aea764:8", "const:4:8"]]
+ 00aea764 ["CALLIND", null, ["register:0:8"]]
- 00aea69c bytes 00013fd6
+ 00aea764 bytes 00013fd6
- 00aea6a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d0:8"]]
- 00aea6a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aea768 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
+ 00aea768 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aea768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea6a0 bytes 9f6a03f9
+ 00aea768 bytes 9fca03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63fd498a1f6ed121861cb7a011ea26d3"></a>

### [`00aea6b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea6b4.md) → [`00aea77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea77c.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00aea7bc",
      "incomplete_value": true,
      "site": "00aea7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea6f4",
      "incomplete_value": true,
      "site": "00aea6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea798",
      "incomplete_value": true,
      "site": "00aea798",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea6d0",
      "incomplete_value": true,
      "site": "00aea6d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea7a0",
      "incomplete_value": false,
      "site": "00aea7b4",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea6d8",
      "incomplete_value": false,
      "site": "00aea6ec",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea790",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea7a0",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea7bc",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea790",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea7a0",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea7bc",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea6b4.md#insn-00aea6ec) · [`00aea6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea6b4.md#insn-00aea6f4) · [`00aea6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea6b4.md#insn-00aea6c8)
- 新版 `00aea7b4`（命令位置の公開資料なし） · `00aea7bc`（命令位置の公開資料なし） · `00aea790`（命令位置の公開資料なし）

~~~diff
- 00aea6ec ["INT_ADD", "register:40f0:8", ["const:aea6ec:8", "const:4:8"]]
- 00aea6ec ["CALL", null, ["callee:00bde040:8"]]
+ 00aea7b4 ["INT_ADD", "register:40f0:8", ["const:aea7b4:8", "const:4:8"]]
+ 00aea7b4 ["CALL", null, ["callee:00bde040:8"]]
- 00aea6ec bytes 29ce0394
+ 00aea7b4 bytes 23ce0394
- 00aea6f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d0:8"]]
- 00aea6f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea7bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
+ 00aea7bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea6f4 bytes 806a03f9
+ 00aea7bc bytes 80ca03f9
- 00aea6c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d0:8"]]
- 00aea6c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
+ 00aea790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea6c8 bytes 816a43f9
+ 00aea790 bytes 81ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45769e8821ba3bc9446c5f6e51e95744"></a>

### [`00aea724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea724.md) → [`00aea7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea7ec.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde590.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde640.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea808",
      "incomplete_value": false,
      "site": "00aea80c",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea740",
      "incomplete_value": false,
      "site": "00aea744",
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
      "definition_site": "00aea818",
      "incomplete_value": true,
      "site": "00aea824",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea750",
      "incomplete_value": true,
      "site": "00aea75c",
      "value": [
        "LOAD",
        "8",
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
      "00aea808",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea818",
      "DATA",
      [
        "storage",
        "010a06e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea808",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea818",
      "DATA",
      [
        "storage",
        "010a07a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea724.md#insn-00aea744) · [`00aea740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea724.md#insn-00aea740) · [`00aea74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea724.md#insn-00aea74c)
- 新版 `00aea80c`（命令位置の公開資料なし） · `00aea808`（命令位置の公開資料なし） · `00aea814`（命令位置の公開資料なし）

~~~diff
- 00aea744 ["INT_ADD", "register:40f0:8", ["const:aea744:8", "const:4:8"]]
- 00aea744 ["CALL", null, ["callee:00bde130:8"]]
+ 00aea80c ["INT_ADD", "register:40f0:8", ["const:aea80c:8", "const:4:8"]]
+ 00aea80c ["CALL", null, ["callee:00bde130:8"]]
- 00aea744 bytes 4fce0394
+ 00aea80c bytes 49ce0394
- 00aea740 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aea740 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea740 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea740 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea808 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aea808 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea808 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea808 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea740 bytes 001c1591
+ 00aea808 bytes 00501791
- 00aea74c ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00aea74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea814 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00aea814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea74c bytes 08811b91
+ 00aea814 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a049ace171b44ca747265db4a2d18b0b"></a>

### [`00aea760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea760.md) → [`00aea828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea828.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea868",
      "incomplete_value": true,
      "site": "00aea868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea7a0",
      "incomplete_value": true,
      "site": "00aea7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "00aea844",
      "incomplete_value": true,
      "site": "00aea844",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea77c",
      "incomplete_value": true,
      "site": "00aea77c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea84c",
      "incomplete_value": false,
      "site": "00aea860",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea784",
      "incomplete_value": false,
      "site": "00aea798",
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
            "const:df:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea83c",
      "READ",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea84c",
      "PARAM",
      [
        "storage",
        "002a60df",
        null,
        "string"
      ]
    ],
    [
      "00aea868",
      "WRITE",
      [
        "storage",
        "010a06d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea83c",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea84c",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea868",
      "WRITE",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea760.md#insn-00aea798) · [`00aea7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea760.md#insn-00aea7a0) · [`00aea774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea760.md#insn-00aea774)
- 新版 `00aea860`（命令位置の公開資料なし） · `00aea868`（命令位置の公開資料なし） · `00aea83c`（命令位置の公開資料なし）

~~~diff
- 00aea798 ["INT_ADD", "register:40f0:8", ["const:aea798:8", "const:4:8"]]
- 00aea798 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea860 ["INT_ADD", "register:40f0:8", ["const:aea860:8", "const:4:8"]]
+ 00aea860 ["CALL", null, ["callee:00bde040:8"]]
- 00aea798 bytes fecd0394
+ 00aea860 bytes f8cd0394
- 00aea7a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d0:8"]]
- 00aea7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea868 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
+ 00aea868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea7a0 bytes 806a03f9
+ 00aea868 bytes 80ca03f9
- 00aea774 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d0:8"]]
- 00aea774 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea83c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
+ 00aea83c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea774 bytes 816a43f9
+ 00aea83c bytes 81ca43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f0630aaf51b9eebb3fd65e7a92d636"></a>

### [`00aea7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea7d0.md) → [`00aea898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aea8b4",
      "incomplete_value": false,
      "site": "00aea8b8",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea7ec",
      "incomplete_value": false,
      "site": "00aea7f0",
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
      "definition_site": "00aea8c4",
      "incomplete_value": true,
      "site": "00aea8d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea7fc",
      "incomplete_value": true,
      "site": "00aea808",
      "value": [
        "LOAD",
        "8",
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
      "00aea8b4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea8c4",
      "DATA",
      [
        "storage",
        "010a0720",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea8b4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea8c4",
      "DATA",
      [
        "storage",
        "010a07e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea7d0.md#insn-00aea7f0) · [`00aea7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea7d0.md#insn-00aea7ec) · [`00aea7f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea7d0.md#insn-00aea7f8)
- 新版 `00aea8b8`（命令位置の公開資料なし） · `00aea8b4`（命令位置の公開資料なし） · `00aea8c0`（命令位置の公開資料なし）

~~~diff
- 00aea7f0 ["INT_ADD", "register:40f0:8", ["const:aea7f0:8", "const:4:8"]]
- 00aea7f0 ["CALL", null, ["callee:00bde130:8"]]
+ 00aea8b8 ["INT_ADD", "register:40f0:8", ["const:aea8b8:8", "const:4:8"]]
+ 00aea8b8 ["CALL", null, ["callee:00bde130:8"]]
- 00aea7f0 bytes 24ce0394
+ 00aea8b8 bytes 1ece0394
- 00aea7ec ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea7ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea7ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea7ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea8b4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aea8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea7ec bytes 00c81791
+ 00aea8b4 bytes 00fc1991
- 00aea7f8 ["COPY", "tmp:0:8", ["const:720:8"]]
- 00aea7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea8c0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00aea8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea7f8 bytes 08811c91
+ 00aea8c0 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c1b52b59365ccd2421443e48ff47ab"></a>

### [`00aea80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea80c.md) → [`00aea8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea8d4.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea900",
      "incomplete_value": true,
      "site": "00aea900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea838",
      "incomplete_value": true,
      "site": "00aea838",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea8e8",
      "incomplete_value": true,
      "site": "00aea8e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea820",
      "incomplete_value": true,
      "site": "00aea820",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea8f4",
      "incomplete_value": false,
      "site": "00aea8f8",
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
            "const:6e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea82c",
      "incomplete_value": false,
      "site": "00aea830",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea8e4",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea8f4",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aea900",
      "WRITE",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea8e4",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea8f4",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aea900",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea80c.md#insn-00aea830) · [`00aea838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea80c.md#insn-00aea838) · [`00aea81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea80c.md#insn-00aea81c)
- 新版 `00aea8f8`（命令位置の公開資料なし） · `00aea900`（命令位置の公開資料なし） · `00aea8e4`（命令位置の公開資料なし）

~~~diff
- 00aea830 ["INT_ADD", "register:40f0:8", ["const:aea830:8", "const:4:8"]]
- 00aea830 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea8f8 ["INT_ADD", "register:40f0:8", ["const:aea8f8:8", "const:4:8"]]
+ 00aea8f8 ["CALL", null, ["callee:00bde040:8"]]
- 00aea830 bytes d8cd0394
+ 00aea8f8 bytes d2cd0394
- 00aea838 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea900 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea838 bytes 609603f9
+ 00aea900 bytes 60f603f9
- 00aea81c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea81c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea8e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea8e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea81c bytes 689643f9
+ 00aea8e4 bytes 68f643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7df44c187fb285d98ace64e86afb563"></a>

### [`00aea84c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea84c.md) → [`00aea914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea914.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea940",
      "incomplete_value": true,
      "site": "00aea940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea878",
      "incomplete_value": true,
      "site": "00aea878",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea928",
      "incomplete_value": true,
      "site": "00aea928",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea860",
      "incomplete_value": true,
      "site": "00aea860",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea930",
      "incomplete_value": false,
      "site": "00aea938",
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
            "const:6e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea868",
      "incomplete_value": false,
      "site": "00aea870",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea924",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea930",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aea940",
      "WRITE",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea924",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea930",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aea940",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea84c.md#insn-00aea870) · [`00aea878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea84c.md#insn-00aea878) · [`00aea85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea84c.md#insn-00aea85c)
- 新版 `00aea938`（命令位置の公開資料なし） · `00aea940`（命令位置の公開資料なし） · `00aea924`（命令位置の公開資料なし）

~~~diff
- 00aea870 ["INT_ADD", "register:40f0:8", ["const:aea870:8", "const:4:8"]]
- 00aea870 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea938 ["INT_ADD", "register:40f0:8", ["const:aea938:8", "const:4:8"]]
+ 00aea938 ["CALL", null, ["callee:00bde040:8"]]
- 00aea870 bytes c8cd0394
+ 00aea938 bytes c2cd0394
- 00aea878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea940 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea878 bytes 609603f9
+ 00aea940 bytes 60f603f9
- 00aea85c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea85c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea924 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea85c bytes 689643f9
+ 00aea924 bytes 68f643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22014a29de98672a3cbbcbb8c01d07cd"></a>

### [`00aea88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea88c.md) → [`00aea954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea954.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea984",
      "incomplete_value": true,
      "site": "00aea984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8bc",
      "incomplete_value": true,
      "site": "00aea8bc",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea968",
      "incomplete_value": true,
      "site": "00aea968",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8a0",
      "incomplete_value": true,
      "site": "00aea8a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea974",
      "incomplete_value": false,
      "site": "00aea97c",
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
            "const:6e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8ac",
      "incomplete_value": false,
      "site": "00aea8b4",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea964",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea974",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aea984",
      "WRITE",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea964",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea974",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aea984",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea88c.md#insn-00aea8b4) · [`00aea8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea88c.md#insn-00aea8bc) · [`00aea89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea88c.md#insn-00aea89c)
- 新版 `00aea97c`（命令位置の公開資料なし） · `00aea984`（命令位置の公開資料なし） · `00aea964`（命令位置の公開資料なし）

~~~diff
- 00aea8b4 ["INT_ADD", "register:40f0:8", ["const:aea8b4:8", "const:4:8"]]
- 00aea8b4 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea97c ["INT_ADD", "register:40f0:8", ["const:aea97c:8", "const:4:8"]]
+ 00aea97c ["CALL", null, ["callee:00bde040:8"]]
- 00aea8b4 bytes b7cd0394
+ 00aea97c bytes b1cd0394
- 00aea8bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea8bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea8bc bytes 609603f9
+ 00aea984 bytes 60f603f9
- 00aea89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea89c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea964 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea89c bytes 689643f9
+ 00aea964 bytes 68f643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3793f2e105d89c0e76e69f83a46e7de1"></a>

### [`00aea8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea8d0.md) → [`00aea998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aea9c8",
      "incomplete_value": true,
      "site": "00aea9c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea900",
      "incomplete_value": true,
      "site": "00aea900",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea9ac",
      "incomplete_value": true,
      "site": "00aea9ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8e4",
      "incomplete_value": true,
      "site": "00aea8e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea9b4",
      "incomplete_value": false,
      "site": "00aea9c0",
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
            "const:6e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8ec",
      "incomplete_value": false,
      "site": "00aea8f8",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea9a8",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9b4",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aea9c8",
      "WRITE",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea9a8",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9b4",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aea9c8",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea8d0.md#insn-00aea8f8) · [`00aea900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea8d0.md#insn-00aea900) · [`00aea8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea8d0.md#insn-00aea8e0)
- 新版 `00aea9c0`（命令位置の公開資料なし） · `00aea9c8`（命令位置の公開資料なし） · `00aea9a8`（命令位置の公開資料なし）

~~~diff
- 00aea8f8 ["INT_ADD", "register:40f0:8", ["const:aea8f8:8", "const:4:8"]]
- 00aea8f8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aea9c0 ["INT_ADD", "register:40f0:8", ["const:aea9c0:8", "const:4:8"]]
+ 00aea9c0 ["CALL", null, ["callee:00bde040:8"]]
- 00aea8f8 bytes a6cd0394
+ 00aea9c0 bytes a0cd0394
- 00aea900 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea900 bytes 609603f9
+ 00aea9c8 bytes 60f603f9
- 00aea8e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00aea8e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea9a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00aea9a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea8e0 bytes 689643f9
+ 00aea9a8 bytes 68f643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8f771616ea302c31c3a2439ca243c2"></a>

### [`00aea920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea920.md) → [`00aea9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeaa70",
      "incomplete_value": true,
      "site": "00aeaa70",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9a8",
      "incomplete_value": true,
      "site": "00aea9a8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeaa1c",
      "incomplete_value": true,
      "site": "00aeaa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea954",
      "incomplete_value": true,
      "site": "00aea960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:728:8"
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
      "site": "00aea974"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aea9fc",
      "READ",
      [
        "storage",
        "010a0730",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aea954",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaa70",
      "WRITE",
      [
        "storage",
        "010a0730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea9fc",
      "READ",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaa1c",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaa70",
      "WRITE",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea920.md#insn-00aea960) · [`00aea974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea920.md#insn-00aea974) · [`00aea9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea920.md#insn-00aea9a8)
- 新版 `00aeaa28`（命令位置の公開資料なし） · `00aeaa70`（命令位置の公開資料なし）

~~~diff
- 00aea960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea960 ["INT_ADD", "register:40f0:8", ["const:aea960:8", "const:4:8"]]
- 00aea960 ["CALLIND", null, ["register:0:8"]]
+ 00aeaa28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeaa28 ["INT_ADD", "register:40f0:8", ["const:aeaa28:8", "const:4:8"]]
+ 00aeaa28 ["CALLIND", null, ["register:0:8"]]
- 00aea960 bytes 00013fd6
+ 00aeaa28 bytes 00013fd6
- 00aea974 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea974 ["INT_ADD", "register:40f0:8", ["const:aea974:8", "const:4:8"]]
- 00aea974 ["CALLIND", null, ["register:0:8"]]
- 00aea974 bytes 00013fd6
- 00aea9a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea9a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:730:8"]]
- 00aea9a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeaa70 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeaa70 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7f0:8"]]
+ 00aeaa70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea9a8 bytes a0c21c39
+ 00aeaa70 bytes a0c21f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b10f72874a3b9907a4518ec641e3792"></a>

### [`00aea9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea9bc.md) → [`00aeaa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeaac0",
      "incomplete_value": true,
      "site": "00aeaac0",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9f8",
      "incomplete_value": true,
      "site": "00aea9f8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaa48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeab10"
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
      "00aeaa98",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaaa4",
      "READ",
      [
        "storage",
        "010a0730",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaac0",
      "WRITE",
      [
        "storage",
        "010a0730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeaa98",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaaa4",
      "READ",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaac0",
      "WRITE",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea9bc.md#insn-00aea9d4) · [`00aea9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea9bc.md#insn-00aea9f8) · [`00aeaa44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea9bc.md#insn-00aeaa44)
- 新版 `00aeaa9c`（命令位置の公開資料なし） · `00aeaac0`（命令位置の公開資料なし）

~~~diff
- 00aea9d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aea9d4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00aeaa9c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aeaa9c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00aea9d4 bytes c10300b4
+ 00aeaa9c bytes c10300b4
- 00aea9f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea9f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea9f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:730:8"]]
- 00aea9f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeaac0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeaac0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeaac0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7f0:8"]]
+ 00aeaac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea9f8 bytes bfc21c39
+ 00aeaac0 bytes bfc21f39
- 00aeaa44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaa44 ["INT_ADD", "register:40f0:8", ["const:aeaa44:8", "const:4:8"]]
- 00aeaa44 ["CALLIND", null, ["register:0:8"]]
- 00aeaa44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8816ff271ab5b29cc31c66c6f1c659"></a>

### [`00aeaa5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaa5c.md) → [`00aeab24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00aeaa9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeab64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaa78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeaa70",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeaa78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeab68"
      ]
    ],
    [
      "unmatched:00aeaa80",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aeab38",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeab40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeab68"
      ]
    ],
    [
      "00aeab48",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaa78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaa5c.md#insn-00aeaa78) · [`00aeaa94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaa5c.md#insn-00aeaa94) · [`00aeaa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaa5c.md#insn-00aeaa9c)
- 新版 `00aeab5c`（命令位置の公開資料なし）

~~~diff
- 00aeaa78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeaa78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeaa78 bytes 410100b5
- 00aeaa94 ["INT_ADD", "register:40f0:8", ["const:aeaa94:8", "const:4:8"]]
- 00aeaa94 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeab5c ["INT_ADD", "register:40f0:8", ["const:aeab5c:8", "const:4:8"]]
+ 00aeab5c ["CALL", null, ["callee:00bde040:8"]]
- 00aeaa94 bytes 3fcd0394
+ 00aeab5c bytes 39cd0394
- 00aeaa9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00aeaa9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaa9c bytes 809603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55102232df1a3d2b04a03ca5c0279d7c"></a>

### [`00aeaacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaacc.md) → [`00aeab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aeabb0",
      "incomplete_value": false,
      "site": "00aeabb4",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaae8",
      "incomplete_value": false,
      "site": "00aeaaec",
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
      "definition_site": "00aeabc0",
      "incomplete_value": true,
      "site": "00aeabcc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeaaf8",
      "incomplete_value": true,
      "site": "00aeab04",
      "value": [
        "LOAD",
        "8",
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
      "00aeabb0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeabc0",
      "DATA",
      [
        "storage",
        "010a0738",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeabb0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeabc0",
      "DATA",
      [
        "storage",
        "010a07f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaaec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaacc.md#insn-00aeaaec) · [`00aeaae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaacc.md#insn-00aeaae8) · [`00aeaaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaacc.md#insn-00aeaaf4)
- 新版 `00aeabb4`（命令位置の公開資料なし） · `00aeabb0`（命令位置の公開資料なし） · `00aeabbc`（命令位置の公開資料なし）

~~~diff
- 00aeaaec ["INT_ADD", "register:40f0:8", ["const:aeaaec:8", "const:4:8"]]
- 00aeaaec ["CALL", null, ["callee:00bde130:8"]]
+ 00aeabb4 ["INT_ADD", "register:40f0:8", ["const:aeabb4:8", "const:4:8"]]
+ 00aeabb4 ["CALL", null, ["callee:00bde130:8"]]
- 00aeaaec bytes 65cd0394
+ 00aeabb4 bytes 5fcd0394
- 00aeaae8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeaae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeabb0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aeabb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeabb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeabb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeaae8 bytes 001c1591
+ 00aeabb0 bytes 00501791
- 00aeaaf4 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00aeaaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeabbc ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00aeabbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeabbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeabbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeaaf4 bytes 08e11c91
+ 00aeabbc bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd05c455a5eb974f6607e8979fef8871"></a>

### [`00aeab08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeab08.md) → [`00aeabd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeabd0.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeac10",
      "incomplete_value": true,
      "site": "00aeac10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab48",
      "incomplete_value": true,
      "site": "00aeab48",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeabec",
      "incomplete_value": true,
      "site": "00aeabec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab24",
      "incomplete_value": true,
      "site": "00aeab24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeabf4",
      "incomplete_value": false,
      "site": "00aeac08",
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
            "const:6e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab2c",
      "incomplete_value": false,
      "site": "00aeab40",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeabe4",
      "READ",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeabf4",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aeac10",
      "WRITE",
      [
        "storage",
        "010a0728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeabe4",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeabf4",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aeac10",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeab40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeab08.md#insn-00aeab40) · [`00aeab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeab08.md#insn-00aeab48) · [`00aeab1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeab08.md#insn-00aeab1c)
- 新版 `00aeac08`（命令位置の公開資料なし） · `00aeac10`（命令位置の公開資料なし） · `00aeabe4`（命令位置の公開資料なし）

~~~diff
- 00aeab40 ["INT_ADD", "register:40f0:8", ["const:aeab40:8", "const:4:8"]]
- 00aeab40 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeac08 ["INT_ADD", "register:40f0:8", ["const:aeac08:8", "const:4:8"]]
+ 00aeac08 ["CALL", null, ["callee:00bde040:8"]]
- 00aeab40 bytes 14cd0394
+ 00aeac08 bytes 0ecd0394
- 00aeab48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00aeab48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeac10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00aeac10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeab48 bytes 809603f9
+ 00aeac10 bytes 80f603f9
- 00aeab1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00aeab1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeabe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00aeabe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeab1c bytes 819643f9
+ 00aeabe4 bytes 81f643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-759182f4faa002f93126cf36a2004a39"></a>

### [`00aeabb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabb4.md) → [`00aeac7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeaca8",
      "incomplete_value": true,
      "site": "00aeaca8",
      "value": [
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
    "old": {
      "definition_site": "00aeabe0",
      "incomplete_value": true,
      "site": "00aeabe0",
      "value": [
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
      "definition_site": "00aeac90",
      "incomplete_value": true,
      "site": "00aeac90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeabc8",
      "incomplete_value": true,
      "site": "00aeabc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeac9c",
      "incomplete_value": false,
      "site": "00aeaca0",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeabd4",
      "incomplete_value": false,
      "site": "00aeabd8",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeac8c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeac9c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeaca8",
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
      "00aeac8c",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeac9c",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeaca8",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeabd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabb4.md#insn-00aeabd8) · [`00aeabe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabb4.md#insn-00aeabe0) · [`00aeabc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabb4.md#insn-00aeabc4)
- 新版 `00aeaca0`（命令位置の公開資料なし） · `00aeaca8`（命令位置の公開資料なし） · `00aeac8c`（命令位置の公開資料なし）

~~~diff
- 00aeabd8 ["INT_ADD", "register:40f0:8", ["const:aeabd8:8", "const:4:8"]]
- 00aeabd8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeaca0 ["INT_ADD", "register:40f0:8", ["const:aeaca0:8", "const:4:8"]]
+ 00aeaca0 ["CALL", null, ["callee:00bde040:8"]]
- 00aeabd8 bytes eecc0394
+ 00aeaca0 bytes e8cc0394
- 00aeabe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeabe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aeaca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeabe0 bytes 60aa03f9
+ 00aeaca8 bytes 600a04f9
- 00aeabc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeabc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeac8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aeac8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeabc4 bytes 68aa43f9
+ 00aeac8c bytes 680a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7516c9819af0ac89c19abd26666ec99"></a>

### [`00aeabf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabf4.md) → [`00aeacbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00aeac20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeace8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeacd0",
      "incomplete_value": true,
      "site": "00aeacd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac08",
      "incomplete_value": true,
      "site": "00aeac08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeaccc",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeacd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeac24"
      ]
    ],
    [
      "unmatched:00aeac10",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aeaccc",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeacd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeacec"
      ]
    ],
    [
      "00aeacd8",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeac08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabf4.md#insn-00aeac08) · [`00aeac18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabf4.md#insn-00aeac18) · [`00aeac20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabf4.md#insn-00aeac20)
- 新版 `00aeacd0`（命令位置の公開資料なし）

~~~diff
- 00aeac08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeac08 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aeacd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aeacd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeac08 bytes e80000b5
+ 00aeacd0 bytes e80000b5
- 00aeac18 ["INT_ADD", "register:40f0:8", ["const:aeac18:8", "const:4:8"]]
- 00aeac18 ["CALL", null, ["callee:00bde040:8"]]
- 00aeac18 bytes decc0394
- 00aeac20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeac20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeac20 bytes 60aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf21bc48e5e532e7eb18ab677b4f9ca"></a>

### [`00aeac34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac34.md) → [`00aeacfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacfc.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aead2c",
      "incomplete_value": true,
      "site": "00aead2c",
      "value": [
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
    "old": {
      "definition_site": "00aeac64",
      "incomplete_value": true,
      "site": "00aeac64",
      "value": [
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
      "definition_site": "00aead10",
      "incomplete_value": true,
      "site": "00aead10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac48",
      "incomplete_value": true,
      "site": "00aeac48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aead1c",
      "incomplete_value": false,
      "site": "00aead24",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac54",
      "incomplete_value": false,
      "site": "00aeac5c",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aead0c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead1c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aead2c",
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
      "00aead0c",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead1c",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aead2c",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeac5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac34.md#insn-00aeac5c) · [`00aeac64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac34.md#insn-00aeac64) · [`00aeac44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac34.md#insn-00aeac44)
- 新版 `00aead24`（命令位置の公開資料なし） · `00aead2c`（命令位置の公開資料なし） · `00aead0c`（命令位置の公開資料なし）

~~~diff
- 00aeac5c ["INT_ADD", "register:40f0:8", ["const:aeac5c:8", "const:4:8"]]
- 00aeac5c ["CALL", null, ["callee:00bde040:8"]]
+ 00aead24 ["INT_ADD", "register:40f0:8", ["const:aead24:8", "const:4:8"]]
+ 00aead24 ["CALL", null, ["callee:00bde040:8"]]
- 00aeac5c bytes cdcc0394
+ 00aead24 bytes c7cc0394
- 00aeac64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeac64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aead2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aead2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeac64 bytes 60aa03f9
+ 00aead2c bytes 600a04f9
- 00aeac44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeac44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aead0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aead0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeac44 bytes 68aa43f9
+ 00aead0c bytes 680a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f5a5d72f84e311b3b438c5ced33aa1"></a>

### [`00aeac78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac78.md) → [`00aead40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead40.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aead70",
      "incomplete_value": true,
      "site": "00aead70",
      "value": [
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
    "old": {
      "definition_site": "00aeaca8",
      "incomplete_value": true,
      "site": "00aeaca8",
      "value": [
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
      "definition_site": "00aead54",
      "incomplete_value": true,
      "site": "00aead54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac8c",
      "incomplete_value": true,
      "site": "00aeac8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aead5c",
      "incomplete_value": false,
      "site": "00aead68",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac94",
      "incomplete_value": false,
      "site": "00aeaca0",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aead50",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead5c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aead70",
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
      "00aead50",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead5c",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aead70",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac78.md#insn-00aeaca0) · [`00aeaca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac78.md#insn-00aeaca8) · [`00aeac88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeac78.md#insn-00aeac88)
- 新版 `00aead68`（命令位置の公開資料なし） · `00aead70`（命令位置の公開資料なし） · `00aead50`（命令位置の公開資料なし）

~~~diff
- 00aeaca0 ["INT_ADD", "register:40f0:8", ["const:aeaca0:8", "const:4:8"]]
- 00aeaca0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aead68 ["INT_ADD", "register:40f0:8", ["const:aead68:8", "const:4:8"]]
+ 00aead68 ["CALL", null, ["callee:00bde040:8"]]
- 00aeaca0 bytes bccc0394
+ 00aead68 bytes b6cc0394
- 00aeaca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeaca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aead70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aead70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaca8 bytes 60aa03f9
+ 00aead70 bytes 600a04f9
- 00aeac88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00aeac88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aead50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00aead50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeac88 bytes 68aa43f9
+ 00aead50 bytes 680a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88bd20dc0fc0c626c7cb1331f4068d9"></a>

### [`00aeacc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeacc8.md) → [`00aead90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeae18",
      "incomplete_value": true,
      "site": "00aeae18",
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
    "old": {
      "definition_site": "00aead50",
      "incomplete_value": true,
      "site": "00aead50",
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
    "new": null,
    "old": {
      "definition_site": "00aeacfc",
      "incomplete_value": true,
      "site": "00aead08",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aeacf8",
      "incomplete_value": true,
      "site": "00aead08",
      "value": [
        "live",
        "register:4008:8"
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
      "00aeada4",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeacfc",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae18",
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
      "00aeada4",
      "READ",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeadc4",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae18",
      "WRITE",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeacc8.md#insn-00aead08) · [`00aead50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeacc8.md#insn-00aead50) · [`00aeacdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeacc8.md#insn-00aeacdc)
- 新版 `00aeadd0`（命令位置の公開資料なし） · `00aeae18`（命令位置の公開資料なし） · `00aeada4`（命令位置の公開資料なし）

~~~diff
- 00aead08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aead08 ["INT_ADD", "register:40f0:8", ["const:aead08:8", "const:4:8"]]
- 00aead08 ["CALLIND", null, ["register:0:8"]]
+ 00aeadd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeadd0 ["INT_ADD", "register:40f0:8", ["const:aeadd0:8", "const:4:8"]]
+ 00aeadd0 ["CALLIND", null, ["register:0:8"]]
- 00aead08 bytes 00013fd6
+ 00aeadd0 bytes 00013fd6
- 00aead50 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aead50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:758:8"]]
- 00aead50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeae18 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeae18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
+ 00aeae18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aead50 bytes a0621d39
+ 00aeae18 bytes a0622039
- 00aeacdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:758:8"]]
- 00aeacdc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aeacdc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeada4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:818:8"]]
+ 00aeada4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeada4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aeacdc bytes a8625d39
+ 00aeada4 bytes a8626039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32cc821a791afdf9b9d5c3e7475dad92"></a>

### [`00aead64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aead64.md) → [`00aeae2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeae2c.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeae68",
      "incomplete_value": true,
      "site": "00aeae68",
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
    "old": {
      "definition_site": "00aeada0",
      "incomplete_value": true,
      "site": "00aeada0",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeaeb8",
      "incomplete_value": true,
      "site": "00aeaeb8",
      "value": [
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
    "old": {
      "definition_site": "00aeadf0",
      "incomplete_value": true,
      "site": "00aeadf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00aeae44",
      "incomplete_value": true,
      "site": "00aeae44",
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
      "definition_site": "00aead7c",
      "incomplete_value": true,
      "site": "00aead7c",
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
      "00aeae40",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae4c",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeae68",
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
      "00aeae40",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae4c",
      "READ",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeae68",
      "WRITE",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aead64.md#insn-00aead7c) · [`00aeada0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aead64.md#insn-00aeada0) · [`00aeadc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aead64.md#insn-00aeadc8)
- 新版 `00aeae44`（命令位置の公開資料なし） · `00aeae68`（命令位置の公開資料なし）

~~~diff
- 00aead7c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aead7c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00aeae44 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aeae44 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00aead7c bytes c10300b4
+ 00aeae44 bytes c10300b4
- 00aeada0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeada0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeada0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:758:8"]]
- 00aeada0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeae68 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeae68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeae68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
+ 00aeae68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeada0 bytes bf621d39
+ 00aeae68 bytes bf622039
- 00aeadc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeadc8 ["INT_ADD", "register:40f0:8", ["const:aeadc8:8", "const:4:8"]]
- 00aeadc8 ["CALLIND", null, ["register:0:8"]]
- 00aeadc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e133340510cf0872c358fee0b9d73d1"></a>

### [`00aeae04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae04.md) → [`00aeaecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaecc.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00aeaf0c",
      "incomplete_value": true,
      "site": "00aeaf0c",
      "value": [
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
    "old": {
      "definition_site": "00aeae44",
      "incomplete_value": true,
      "site": "00aeae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00aeaee8",
      "incomplete_value": true,
      "site": "00aeaee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae20",
      "incomplete_value": true,
      "site": "00aeae20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeaef0",
      "incomplete_value": false,
      "site": "00aeaf04",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae28",
      "incomplete_value": false,
      "site": "00aeae3c",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeaee0",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaef0",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeaf0c",
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
      "00aeaee0",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaef0",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeaf0c",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae04.md#insn-00aeae3c) · [`00aeae44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae04.md#insn-00aeae44) · [`00aeae18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae04.md#insn-00aeae18)
- 新版 `00aeaf04`（命令位置の公開資料なし） · `00aeaf0c`（命令位置の公開資料なし） · `00aeaee0`（命令位置の公開資料なし）

~~~diff
- 00aeae3c ["INT_ADD", "register:40f0:8", ["const:aeae3c:8", "const:4:8"]]
- 00aeae3c ["CALL", null, ["callee:00bde040:8"]]
+ 00aeaf04 ["INT_ADD", "register:40f0:8", ["const:aeaf04:8", "const:4:8"]]
+ 00aeaf04 ["CALL", null, ["callee:00bde040:8"]]
- 00aeae3c bytes 55cc0394
+ 00aeaf04 bytes 4fcc0394
- 00aeae44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00aeae44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaf0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00aeaf0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeae44 bytes 80aa03f9
+ 00aeaf0c bytes 800a04f9
- 00aeae18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00aeae18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeaee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00aeaee0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeae18 bytes 81aa43f9
+ 00aeaee0 bytes 810a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d16e55d411c5d0e266d2d66904c5373"></a>

### [`00aeae74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae74.md) → [`00aeaf3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf3c.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde030.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0e0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aeaf58",
      "incomplete_value": false,
      "site": "00aeaf5c",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae90",
      "incomplete_value": false,
      "site": "00aeae94",
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
      "definition_site": "00aeaf68",
      "incomplete_value": true,
      "site": "00aeaf74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeaea0",
      "incomplete_value": true,
      "site": "00aeaeac",
      "value": [
        "LOAD",
        "8",
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
      "00aeaf58",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeaf68",
      "DATA",
      [
        "storage",
        "010a0760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeaf58",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeaf68",
      "DATA",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae74.md#insn-00aeae94) · [`00aeae90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae74.md#insn-00aeae90) · [`00aeae9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae74.md#insn-00aeae9c)
- 新版 `00aeaf5c`（命令位置の公開資料なし） · `00aeaf58`（命令位置の公開資料なし） · `00aeaf64`（命令位置の公開資料なし）

~~~diff
- 00aeae94 ["INT_ADD", "register:40f0:8", ["const:aeae94:8", "const:4:8"]]
- 00aeae94 ["CALL", null, ["callee:00bde130:8"]]
+ 00aeaf5c ["INT_ADD", "register:40f0:8", ["const:aeaf5c:8", "const:4:8"]]
+ 00aeaf5c ["CALL", null, ["callee:00bde130:8"]]
- 00aeae94 bytes 7bcc0394
+ 00aeaf5c bytes 75cc0394
- 00aeae90 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeae90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeae90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeae90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf58 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aeaf58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeae90 bytes 001c1591
+ 00aeaf58 bytes 00501791
- 00aeae9c ["COPY", "tmp:0:8", ["const:760:8"]]
- 00aeae9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeae9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeae9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeaf64 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00aeaf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeaf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeaf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeae9c bytes 08811d91
+ 00aeaf64 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4c418725822443b4f237697d8f9ec75"></a>

### [`00aeaeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaeb0.md) → [`00aeaf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeafb8",
      "incomplete_value": true,
      "site": "00aeafb8",
      "value": [
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
    "old": {
      "definition_site": "00aeaef0",
      "incomplete_value": true,
      "site": "00aeaef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00aeaf94",
      "incomplete_value": true,
      "site": "00aeaf94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaecc",
      "incomplete_value": true,
      "site": "00aeaecc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeaf9c",
      "incomplete_value": false,
      "site": "00aeafb0",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaed4",
      "incomplete_value": false,
      "site": "00aeaee8",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeaf8c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaf9c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeafb8",
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
      "00aeaf8c",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaf9c",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeafb8",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaeb0.md#insn-00aeaee8) · [`00aeaef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaeb0.md#insn-00aeaef0) · [`00aeaec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaeb0.md#insn-00aeaec4)
- 新版 `00aeafb0`（命令位置の公開資料なし） · `00aeafb8`（命令位置の公開資料なし） · `00aeaf8c`（命令位置の公開資料なし）

~~~diff
- 00aeaee8 ["INT_ADD", "register:40f0:8", ["const:aeaee8:8", "const:4:8"]]
- 00aeaee8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeafb0 ["INT_ADD", "register:40f0:8", ["const:aeafb0:8", "const:4:8"]]
+ 00aeafb0 ["CALL", null, ["callee:00bde040:8"]]
- 00aeaee8 bytes 2acc0394
+ 00aeafb0 bytes 24cc0394
- 00aeaef0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00aeaef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeafb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00aeafb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaef0 bytes 80aa03f9
+ 00aeafb8 bytes 800a04f9
- 00aeaec4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00aeaec4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeaf8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00aeaf8c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeaec4 bytes 81aa43f9
+ 00aeaf8c bytes 810a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6e9508373ca7c80014bf45945e9cb3"></a>

### [`00aeaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf20.md) → [`00aeafe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeafe8.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aeb004",
      "incomplete_value": false,
      "site": "00aeb008",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaf3c",
      "incomplete_value": false,
      "site": "00aeaf40",
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
      "definition_site": "00aeb014",
      "incomplete_value": true,
      "site": "00aeb020",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeaf4c",
      "incomplete_value": true,
      "site": "00aeaf58",
      "value": [
        "LOAD",
        "8",
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
      "00aeb004",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aeb014",
      "DATA",
      [
        "storage",
        "010a0768",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb004",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aeb014",
      "DATA",
      [
        "storage",
        "010a0828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf20.md#insn-00aeaf40) · [`00aeaf3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf20.md#insn-00aeaf3c) · [`00aeaf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf20.md#insn-00aeaf48)
- 新版 `00aeb008`（命令位置の公開資料なし） · `00aeb004`（命令位置の公開資料なし） · `00aeb010`（命令位置の公開資料なし）

~~~diff
- 00aeaf40 ["INT_ADD", "register:40f0:8", ["const:aeaf40:8", "const:4:8"]]
- 00aeaf40 ["CALL", null, ["callee:00bde130:8"]]
+ 00aeb008 ["INT_ADD", "register:40f0:8", ["const:aeb008:8", "const:4:8"]]
+ 00aeb008 ["CALL", null, ["callee:00bde130:8"]]
- 00aeaf40 bytes 50cc0394
+ 00aeb008 bytes 4acc0394
- 00aeaf3c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aeaf3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb004 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aeb004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeaf3c bytes 00c81791
+ 00aeb004 bytes 00fc1991
- 00aeaf48 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00aeaf48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaf48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaf48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb010 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00aeb010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeaf48 bytes 08a11d91
+ 00aeb010 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-203211c606ac09217a8527d01bf8dafe"></a>

### [`00aeaf5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf5c.md) → [`00aeb024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb024.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb050",
      "incomplete_value": true,
      "site": "00aeb050",
      "value": [
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
      "definition_site": "00aeaf88",
      "incomplete_value": true,
      "site": "00aeaf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "00aeb038",
      "incomplete_value": true,
      "site": "00aeb038",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaf70",
      "incomplete_value": true,
      "site": "00aeaf70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb044",
      "incomplete_value": false,
      "site": "00aeb048",
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
            "const:69f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaf7c",
      "incomplete_value": false,
      "site": "00aeaf80",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb034",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb044",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb050",
      "WRITE",
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
      "00aeb034",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb044",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb050",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf5c.md#insn-00aeaf80) · [`00aeaf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf5c.md#insn-00aeaf88) · [`00aeaf6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf5c.md#insn-00aeaf6c)
- 新版 `00aeb048`（命令位置の公開資料なし） · `00aeb050`（命令位置の公開資料なし） · `00aeb034`（命令位置の公開資料なし）

~~~diff
- 00aeaf80 ["INT_ADD", "register:40f0:8", ["const:aeaf80:8", "const:4:8"]]
- 00aeaf80 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb048 ["INT_ADD", "register:40f0:8", ["const:aeb048:8", "const:4:8"]]
+ 00aeb048 ["CALL", null, ["callee:00bde040:8"]]
- 00aeaf80 bytes 04cc0394
+ 00aeb048 bytes fecb0394
- 00aeaf88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeaf88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaf88 bytes 60ba03f9
+ 00aeb050 bytes 601a04f9
- 00aeaf6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeaf6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb034 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb034 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeaf6c bytes 68ba43f9
+ 00aeb034 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f008f7da819a5a403016ce19aa07b5f3"></a>

### [`00aeaf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf9c.md) → [`00aeb064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb090",
      "incomplete_value": true,
      "site": "00aeb090",
      "value": [
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
      "definition_site": "00aeafc8",
      "incomplete_value": true,
      "site": "00aeafc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "00aeb078",
      "incomplete_value": true,
      "site": "00aeb078",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeafb0",
      "incomplete_value": true,
      "site": "00aeafb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb080",
      "incomplete_value": false,
      "site": "00aeb088",
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
            "const:69f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeafb8",
      "incomplete_value": false,
      "site": "00aeafc0",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb074",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb080",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb090",
      "WRITE",
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
      "00aeb074",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb080",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb090",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf9c.md#insn-00aeafc0) · [`00aeafc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf9c.md#insn-00aeafc8) · [`00aeafac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf9c.md#insn-00aeafac)
- 新版 `00aeb088`（命令位置の公開資料なし） · `00aeb090`（命令位置の公開資料なし） · `00aeb074`（命令位置の公開資料なし）

~~~diff
- 00aeafc0 ["INT_ADD", "register:40f0:8", ["const:aeafc0:8", "const:4:8"]]
- 00aeafc0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb088 ["INT_ADD", "register:40f0:8", ["const:aeb088:8", "const:4:8"]]
+ 00aeb088 ["CALL", null, ["callee:00bde040:8"]]
- 00aeafc0 bytes f4cb0394
+ 00aeb088 bytes eecb0394
- 00aeafc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeafc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeafc8 bytes 60ba03f9
+ 00aeb090 bytes 601a04f9
- 00aeafac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeafac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeafac bytes 68ba43f9
+ 00aeb074 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d7836624807975c1e342814d9c6f74"></a>

### [`00aeafdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeafdc.md) → [`00aeb0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb0d4",
      "incomplete_value": true,
      "site": "00aeb0d4",
      "value": [
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
      "definition_site": "00aeb00c",
      "incomplete_value": true,
      "site": "00aeb00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "00aeb0b8",
      "incomplete_value": true,
      "site": "00aeb0b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaff0",
      "incomplete_value": true,
      "site": "00aeaff0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb0c4",
      "incomplete_value": false,
      "site": "00aeb0cc",
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
            "const:69f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaffc",
      "incomplete_value": false,
      "site": "00aeb004",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb0b4",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb0c4",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb0d4",
      "WRITE",
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
      "00aeb0b4",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb0c4",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb0d4",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeafdc.md#insn-00aeb004) · [`00aeb00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeafdc.md#insn-00aeb00c) · [`00aeafec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeafdc.md#insn-00aeafec)
- 新版 `00aeb0cc`（命令位置の公開資料なし） · `00aeb0d4`（命令位置の公開資料なし） · `00aeb0b4`（命令位置の公開資料なし）

~~~diff
- 00aeb004 ["INT_ADD", "register:40f0:8", ["const:aeb004:8", "const:4:8"]]
- 00aeb004 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb0cc ["INT_ADD", "register:40f0:8", ["const:aeb0cc:8", "const:4:8"]]
+ 00aeb0cc ["CALL", null, ["callee:00bde040:8"]]
- 00aeb004 bytes e3cb0394
+ 00aeb0cc bytes ddcb0394
- 00aeb00c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeb00c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb00c bytes 60ba03f9
+ 00aeb0d4 bytes 601a04f9
- 00aeafec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeafec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb0b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeafec bytes 68ba43f9
+ 00aeb0b4 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bae4c363e4888644be867586ab0a6ec8"></a>

### [`00aeb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb020.md) → [`00aeb0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0e8.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb118",
      "incomplete_value": true,
      "site": "00aeb118",
      "value": [
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
      "definition_site": "00aeb050",
      "incomplete_value": true,
      "site": "00aeb050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "00aeb0fc",
      "incomplete_value": true,
      "site": "00aeb0fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb034",
      "incomplete_value": true,
      "site": "00aeb034",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb104",
      "incomplete_value": false,
      "site": "00aeb110",
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
            "const:69f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb03c",
      "incomplete_value": false,
      "site": "00aeb048",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb0f8",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb104",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb118",
      "WRITE",
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
      "00aeb0f8",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb104",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb118",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb020.md#insn-00aeb048) · [`00aeb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb020.md#insn-00aeb050) · [`00aeb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb020.md#insn-00aeb030)
- 新版 `00aeb110`（命令位置の公開資料なし） · `00aeb118`（命令位置の公開資料なし） · `00aeb0f8`（命令位置の公開資料なし）

~~~diff
- 00aeb048 ["INT_ADD", "register:40f0:8", ["const:aeb048:8", "const:4:8"]]
- 00aeb048 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb110 ["INT_ADD", "register:40f0:8", ["const:aeb110:8", "const:4:8"]]
+ 00aeb110 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb048 bytes d2cb0394
+ 00aeb110 bytes cccb0394
- 00aeb050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeb050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb050 bytes 60ba03f9
+ 00aeb118 bytes 601a04f9
- 00aeb030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00aeb030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb0f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00aeb0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb030 bytes 68ba43f9
+ 00aeb0f8 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38432a146be35711c9e5d03779db81be"></a>

### [`00aeb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb070.md) → [`00aeb138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb138.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb1c0",
      "incomplete_value": true,
      "site": "00aeb1c0",
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
      "definition_site": "00aeb0f8",
      "incomplete_value": true,
      "site": "00aeb0f8",
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
            "const:778:8"
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
      "definition_site": "00aeb16c",
      "incomplete_value": true,
      "site": "00aeb178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb0a4",
      "incomplete_value": true,
      "site": "00aeb0b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:770:8"
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
      "site": "00aeb108"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb14c",
      "READ",
      [
        "storage",
        "010a0778",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb158",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb0fc"
      ]
    ],
    [
      "00aeb16c",
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
      "00aeb14c",
      "READ",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb158",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb1c4"
      ]
    ],
    [
      "00aeb16c",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb070.md#insn-00aeb0b0) · [`00aeb0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb070.md#insn-00aeb0f8) · [`00aeb108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb070.md#insn-00aeb108)
- 新版 `00aeb178`（命令位置の公開資料なし） · `00aeb1c0`（命令位置の公開資料なし）

~~~diff
- 00aeb0b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb0b0 ["INT_ADD", "register:40f0:8", ["const:aeb0b0:8", "const:4:8"]]
- 00aeb0b0 ["CALLIND", null, ["register:0:8"]]
+ 00aeb178 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb178 ["INT_ADD", "register:40f0:8", ["const:aeb178:8", "const:4:8"]]
+ 00aeb178 ["CALLIND", null, ["register:0:8"]]
- 00aeb0b0 bytes 00013fd6
+ 00aeb178 bytes 00013fd6
- 00aeb0f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb0f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:778:8"]]
- 00aeb0f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeb1c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeb1c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
+ 00aeb1c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb0f8 bytes a0e21d39
+ 00aeb1c0 bytes a0e22039
- 00aeb108 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aeb108 ["RETURN", null, ["register:0:8"]]
- 00aeb108 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c136a12efc3530f85fe6b6176c0a10"></a>

### [`00aeb10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb10c.md) → [`00aeb1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb1d4.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 44.44% / 新版 36.36%

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
      "site": "00aeb148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb210"
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
      "00aeb1e8",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb1f4",
      "READ",
      [
        "storage",
        "010a0778",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeb148",
      "WRITE",
      [
        "storage",
        "010a0778",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb1e8",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb1f4",
      "READ",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb210",
      "WRITE",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb10c.md#insn-00aeb124) · [`00aeb144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb10c.md#insn-00aeb144) · [`00aeb148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb10c.md#insn-00aeb148)
- 新版 `00aeb1ec`（命令位置の公開資料なし）

~~~diff
- 00aeb124 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb124 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00aeb1ec ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aeb1ec ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00aeb124 bytes c10300b4
+ 00aeb1ec bytes c10300b4
- 00aeb144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb144 ["INT_ADD", "register:40f0:8", ["const:aeb144:8", "const:4:8"]]
- 00aeb144 ["CALLIND", null, ["register:0:8"]]
- 00aeb144 bytes 00013fd6
- 00aeb148 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb148 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb148 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:778:8"]]
- 00aeb148 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb148 bytes bfe21d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe76539d5ba20e60b7fe094223113509"></a>

### [`00aeb1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb1ac.md) → [`00aeb274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00aeb1ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb1ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb1b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb1ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb1b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb1c0",
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
      "00aeb274",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeb278",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aeb288",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb1ac.md#insn-00aeb1ac) · [`00aeb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb1ac.md#insn-00aeb1b0) · [`00aeb1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb1ac.md#insn-00aeb1c8)

~~~diff
- 00aeb1ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb1ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb1ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aeb1ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb1ac bytes f44fbea9
- 00aeb1b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb1b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb1b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb1b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb1b0 bytes fd7b01a9
- 00aeb1c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb1c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeb1c8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47b58feffff8004862c51227b6577506"></a>

### [`00aeb21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb21c.md) → [`00aeb2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb2e4.md) _ZN8firebase4util13integer_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aeb300",
      "incomplete_value": false,
      "site": "00aeb304",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb238",
      "incomplete_value": false,
      "site": "00aeb23c",
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
      "definition_site": "00aeb310",
      "incomplete_value": true,
      "site": "00aeb31c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb248",
      "incomplete_value": true,
      "site": "00aeb254",
      "value": [
        "LOAD",
        "8",
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
      "00aeb300",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeb310",
      "DATA",
      [
        "storage",
        "010a0780",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb300",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeb310",
      "DATA",
      [
        "storage",
        "010a0840",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb21c.md#insn-00aeb23c) · [`00aeb238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb21c.md#insn-00aeb238) · [`00aeb244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb21c.md#insn-00aeb244)
- 新版 `00aeb304`（命令位置の公開資料なし） · `00aeb300`（命令位置の公開資料なし） · `00aeb30c`（命令位置の公開資料なし）

~~~diff
- 00aeb23c ["INT_ADD", "register:40f0:8", ["const:aeb23c:8", "const:4:8"]]
- 00aeb23c ["CALL", null, ["callee:00bde130:8"]]
+ 00aeb304 ["INT_ADD", "register:40f0:8", ["const:aeb304:8", "const:4:8"]]
+ 00aeb304 ["CALL", null, ["callee:00bde130:8"]]
- 00aeb23c bytes 91cb0394
+ 00aeb304 bytes 8bcb0394
- 00aeb238 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeb238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb300 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aeb300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb238 bytes 001c1591
+ 00aeb300 bytes 00501791
- 00aeb244 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00aeb244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb30c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00aeb30c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb30c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb30c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb244 bytes 08011e91
+ 00aeb30c bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec3d32a1c83dc43bcdea9b9f83048d9"></a>

### [`00aeb258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb258.md) → [`00aeb320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb320.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00aeb298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb360"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb26c",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeb274",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb364"
      ]
    ],
    [
      "unmatched:00aeb27c",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aeb334",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb33c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb364"
      ]
    ],
    [
      "00aeb344",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb258.md#insn-00aeb274) · [`00aeb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb258.md#insn-00aeb290) · [`00aeb298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb258.md#insn-00aeb298)
- 新版 `00aeb358`（命令位置の公開資料なし）

~~~diff
- 00aeb274 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb274 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeb274 bytes 410100b5
- 00aeb290 ["INT_ADD", "register:40f0:8", ["const:aeb290:8", "const:4:8"]]
- 00aeb290 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb358 ["INT_ADD", "register:40f0:8", ["const:aeb358:8", "const:4:8"]]
+ 00aeb358 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb290 bytes 40cb0394
+ 00aeb358 bytes 3acb0394
- 00aeb298 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00aeb298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb298 bytes 80ba03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ea23306575bfd2264d420629e79faa"></a>

### [`00aeb304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb304.md) → [`00aeb3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb3cc.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb3f8",
      "incomplete_value": true,
      "site": "00aeb3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb330",
      "incomplete_value": true,
      "site": "00aeb330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00aeb3e0",
      "incomplete_value": true,
      "site": "00aeb3e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb318",
      "incomplete_value": true,
      "site": "00aeb318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb3ec",
      "incomplete_value": false,
      "site": "00aeb3f0",
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
            "const:289:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb324",
      "incomplete_value": false,
      "site": "00aeb328",
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
      "00aeb3dc",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb3ec",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb3f8",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb3dc",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb3ec",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb3f8",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb304.md#insn-00aeb328) · [`00aeb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb304.md#insn-00aeb330) · [`00aeb314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb304.md#insn-00aeb314)
- 新版 `00aeb3f0`（命令位置の公開資料なし） · `00aeb3f8`（命令位置の公開資料なし） · `00aeb3dc`（命令位置の公開資料なし）

~~~diff
- 00aeb328 ["INT_ADD", "register:40f0:8", ["const:aeb328:8", "const:4:8"]]
- 00aeb328 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb3f0 ["INT_ADD", "register:40f0:8", ["const:aeb3f0:8", "const:4:8"]]
+ 00aeb3f0 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb328 bytes 1acb0394
+ 00aeb3f0 bytes 14cb0394
- 00aeb330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb3f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb3f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb330 bytes 60ce03f9
+ 00aeb3f8 bytes 602e04f9
- 00aeb314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb3dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb3dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb314 bytes 68ce43f9
+ 00aeb3dc bytes 682e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8b0af8e3304b0874422611f66aa450"></a>

### [`00aeb344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb344.md) → [`00aeb40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb40c.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb438",
      "incomplete_value": true,
      "site": "00aeb438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb370",
      "incomplete_value": true,
      "site": "00aeb370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00aeb420",
      "incomplete_value": true,
      "site": "00aeb420",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb358",
      "incomplete_value": true,
      "site": "00aeb358",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb428",
      "incomplete_value": false,
      "site": "00aeb430",
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
            "const:289:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb360",
      "incomplete_value": false,
      "site": "00aeb368",
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
      "00aeb41c",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb428",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb438",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb41c",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb428",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb438",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb344.md#insn-00aeb368) · [`00aeb370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb344.md#insn-00aeb370) · [`00aeb354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb344.md#insn-00aeb354)
- 新版 `00aeb430`（命令位置の公開資料なし） · `00aeb438`（命令位置の公開資料なし） · `00aeb41c`（命令位置の公開資料なし）

~~~diff
- 00aeb368 ["INT_ADD", "register:40f0:8", ["const:aeb368:8", "const:4:8"]]
- 00aeb368 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb430 ["INT_ADD", "register:40f0:8", ["const:aeb430:8", "const:4:8"]]
+ 00aeb430 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb368 bytes 0acb0394
+ 00aeb430 bytes 04cb0394
- 00aeb370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb438 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb370 bytes 60ce03f9
+ 00aeb438 bytes 602e04f9
- 00aeb354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb41c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb41c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb354 bytes 68ce43f9
+ 00aeb41c bytes 682e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-798195fa9d414b1960cd4b1bdabb88f3"></a>

### [`00aeb384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb384.md) → [`00aeb44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb44c.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00aeb3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb47c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeb460",
      "incomplete_value": true,
      "site": "00aeb460",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb398",
      "incomplete_value": true,
      "site": "00aeb398",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeb45c",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeb3a4",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aeb3ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aeb45c",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb46c",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb474",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb384.md#insn-00aeb398) · [`00aeb3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb384.md#insn-00aeb3ac) · [`00aeb3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb384.md#insn-00aeb3b4)
- 新版 `00aeb460`（命令位置の公開資料なし）

~~~diff
- 00aeb398 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeb398 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aeb460 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aeb460 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeb398 bytes 080100b5
+ 00aeb460 bytes 080100b5
- 00aeb3ac ["INT_ADD", "register:40f0:8", ["const:aeb3ac:8", "const:4:8"]]
- 00aeb3ac ["CALL", null, ["callee:00bde040:8"]]
- 00aeb3ac bytes f9ca0394
- 00aeb3b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb3b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb3b4 bytes 60ce03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2d517736f542bacd8093efe5d1a0040"></a>

### [`00aeb3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb3c8.md) → [`00aeb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb490.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aeb4c0",
      "incomplete_value": true,
      "site": "00aeb4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3f8",
      "incomplete_value": true,
      "site": "00aeb3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00aeb4a4",
      "incomplete_value": true,
      "site": "00aeb4a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3dc",
      "incomplete_value": true,
      "site": "00aeb3dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb4ac",
      "incomplete_value": false,
      "site": "00aeb4b8",
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
            "const:289:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3e4",
      "incomplete_value": false,
      "site": "00aeb3f0",
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
      "00aeb4a0",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4ac",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb4c0",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb4a0",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4ac",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb4c0",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb3c8.md#insn-00aeb3f0) · [`00aeb3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb3c8.md#insn-00aeb3f8) · [`00aeb3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb3c8.md#insn-00aeb3d8)
- 新版 `00aeb4b8`（命令位置の公開資料なし） · `00aeb4c0`（命令位置の公開資料なし） · `00aeb4a0`（命令位置の公開資料なし）

~~~diff
- 00aeb3f0 ["INT_ADD", "register:40f0:8", ["const:aeb3f0:8", "const:4:8"]]
- 00aeb3f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb4b8 ["INT_ADD", "register:40f0:8", ["const:aeb4b8:8", "const:4:8"]]
+ 00aeb4b8 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb3f0 bytes e8ca0394
+ 00aeb4b8 bytes e2ca0394
- 00aeb3f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb3f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb3f8 bytes 60ce03f9
+ 00aeb4c0 bytes 602e04f9
- 00aeb3d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00aeb3d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb4a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00aeb4a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb3d8 bytes 68ce43f9
+ 00aeb4a0 bytes 682e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f0dfa5cbe3371fc3392247560a209ca"></a>

### [`00aeb418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb418.md) → [`00aeb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb4e0.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb41c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb418",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb41c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb420",
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
      "00aeb4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aeb4e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeb4e8",
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

- 旧版 [`00aeb418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb418.md#insn-00aeb418) · [`00aeb41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb418.md#insn-00aeb41c) · [`00aeb420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb418.md#insn-00aeb420)

~~~diff
- 00aeb418 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aeb418 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aeb418 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb418 bytes f50f1df8
- 00aeb41c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb41c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb41c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb41c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb41c bytes f44f01a9
- 00aeb420 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb420 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb420 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aeb420 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb420 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99635d3ec334e195e0c3c604d2820f99"></a>

### [`00aeb4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb4b4.md) → [`00aeb57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb57c.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb4f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb608",
      "incomplete_value": true,
      "site": "00aeb608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb540",
      "incomplete_value": true,
      "site": "00aeb540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "site": "00aeb5b8"
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
      "00aeb590",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb59c",
      "READ",
      [
        "storage",
        "010a07a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb5a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb4f4"
      ]
    ]
  ],
  "added": [
    [
      "00aeb590",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb59c",
      "READ",
      [
        "storage",
        "010a0860",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb5a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb5bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb4b4.md#insn-00aeb4cc) · [`00aeb4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb4b4.md#insn-00aeb4ec) · [`00aeb4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb4b4.md#insn-00aeb4f0)
- 新版 `00aeb594`（命令位置の公開資料なし）

~~~diff
- 00aeb4cc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb4cc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00aeb594 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aeb594 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00aeb4cc bytes c10300b4
+ 00aeb594 bytes c10300b4
- 00aeb4ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb4ec ["INT_ADD", "register:40f0:8", ["const:aeb4ec:8", "const:4:8"]]
- 00aeb4ec ["CALLIND", null, ["register:0:8"]]
- 00aeb4ec bytes 00013fd6
- 00aeb4f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb4f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb4f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a0:8"]]
- 00aeb4f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb4f0 bytes bf821e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a182da329933d2921268b7536e105631"></a>

### [`00aeb554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb554.md) → [`00aeb61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb61c.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00aeb65c",
      "incomplete_value": true,
      "site": "00aeb65c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb594",
      "incomplete_value": true,
      "site": "00aeb594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00aeb638",
      "incomplete_value": true,
      "site": "00aeb638",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb570",
      "incomplete_value": true,
      "site": "00aeb570",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb640",
      "incomplete_value": false,
      "site": "00aeb654",
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
            "const:289:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb578",
      "incomplete_value": false,
      "site": "00aeb58c",
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
      "00aeb630",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb640",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb65c",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb630",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb640",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb65c",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb554.md#insn-00aeb58c) · [`00aeb594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb554.md#insn-00aeb594) · [`00aeb568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb554.md#insn-00aeb568)
- 新版 `00aeb654`（命令位置の公開資料なし） · `00aeb65c`（命令位置の公開資料なし） · `00aeb630`（命令位置の公開資料なし）

~~~diff
- 00aeb58c ["INT_ADD", "register:40f0:8", ["const:aeb58c:8", "const:4:8"]]
- 00aeb58c ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb654 ["INT_ADD", "register:40f0:8", ["const:aeb654:8", "const:4:8"]]
+ 00aeb654 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb58c bytes 81ca0394
+ 00aeb654 bytes 7bca0394
- 00aeb594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00aeb594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb65c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
+ 00aeb65c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb594 bytes 80ce03f9
+ 00aeb65c bytes 802e04f9
- 00aeb568 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00aeb568 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
+ 00aeb630 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb568 bytes 81ce43f9
+ 00aeb630 bytes 812e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-108db333df5f9d2e77453948b719368b"></a>

### [`00aeb5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb5c4.md) → [`00aeb68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb68c.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5b0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde660.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aeb6a8",
      "incomplete_value": false,
      "site": "00aeb6ac",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb5e0",
      "incomplete_value": false,
      "site": "00aeb5e4",
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
      "definition_site": "00aeb6b8",
      "incomplete_value": true,
      "site": "00aeb6c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb5f0",
      "incomplete_value": true,
      "site": "00aeb5fc",
      "value": [
        "LOAD",
        "8",
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
      "00aeb6a8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeb6b8",
      "DATA",
      [
        "storage",
        "010a07a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb6a8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeb6b8",
      "DATA",
      [
        "storage",
        "010a0868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb5c4.md#insn-00aeb5e4) · [`00aeb5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb5c4.md#insn-00aeb5e0) · [`00aeb5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb5c4.md#insn-00aeb5ec)
- 新版 `00aeb6ac`（命令位置の公開資料なし） · `00aeb6a8`（命令位置の公開資料なし） · `00aeb6b4`（命令位置の公開資料なし）

~~~diff
- 00aeb5e4 ["INT_ADD", "register:40f0:8", ["const:aeb5e4:8", "const:4:8"]]
- 00aeb5e4 ["CALL", null, ["callee:00bde130:8"]]
+ 00aeb6ac ["INT_ADD", "register:40f0:8", ["const:aeb6ac:8", "const:4:8"]]
+ 00aeb6ac ["CALL", null, ["callee:00bde130:8"]]
- 00aeb5e4 bytes a7ca0394
+ 00aeb6ac bytes a1ca0394
- 00aeb5e0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeb5e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb5e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb5e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6a8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aeb6a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb5e0 bytes 001c1591
+ 00aeb6a8 bytes 00501791
- 00aeb5ec ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 00aeb5ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb5ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb5ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6b4 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00aeb6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb5ec bytes 08a11e91
+ 00aeb6b4 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e6ef1755adbde00f5c04aab2dec6bba"></a>

### [`00aeb600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb600.md) → [`00aeb6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb6c8.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb708",
      "incomplete_value": true,
      "site": "00aeb708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb640",
      "incomplete_value": true,
      "site": "00aeb640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00aeb6e4",
      "incomplete_value": true,
      "site": "00aeb6e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb61c",
      "incomplete_value": true,
      "site": "00aeb61c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb6ec",
      "incomplete_value": false,
      "site": "00aeb700",
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
            "const:289:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb624",
      "incomplete_value": false,
      "site": "00aeb638",
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
      "00aeb6dc",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb6ec",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb708",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb6dc",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb6ec",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb708",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb600.md#insn-00aeb638) · [`00aeb640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb600.md#insn-00aeb640) · [`00aeb614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb600.md#insn-00aeb614)
- 新版 `00aeb700`（命令位置の公開資料なし） · `00aeb708`（命令位置の公開資料なし） · `00aeb6dc`（命令位置の公開資料なし）

~~~diff
- 00aeb638 ["INT_ADD", "register:40f0:8", ["const:aeb638:8", "const:4:8"]]
- 00aeb638 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb700 ["INT_ADD", "register:40f0:8", ["const:aeb700:8", "const:4:8"]]
+ 00aeb700 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb638 bytes 56ca0394
+ 00aeb700 bytes 50ca0394
- 00aeb640 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00aeb640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb708 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
+ 00aeb708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb640 bytes 80ce03f9
+ 00aeb708 bytes 802e04f9
- 00aeb614 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00aeb614 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb6dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
+ 00aeb6dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb614 bytes 81ce43f9
+ 00aeb6dc bytes 812e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0030091688161a68c06fcb939092e7b4"></a>

### [`00aeb6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb6ec.md) → [`00aeb7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb7e0",
      "incomplete_value": true,
      "site": "00aeb7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb718",
      "incomplete_value": true,
      "site": "00aeb718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00aeb7c8",
      "incomplete_value": true,
      "site": "00aeb7c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb700",
      "incomplete_value": true,
      "site": "00aeb700",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aeb700"
      ],
      [
        "FALL_THROUGH",
        "00aeb7c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeb7c8",
      "incomplete_value": true,
      "site": "00aeb7e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb700",
      "incomplete_value": true,
      "site": "00aeb718",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aeb7c4",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7e0",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb7c4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7e0",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb6ec.md#insn-00aeb718) · [`00aeb6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb6ec.md#insn-00aeb6fc) · [`00aeb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb6ec.md#insn-00aeb710)
- 新版 `00aeb7e0`（命令位置の公開資料なし） · `00aeb7c4`（命令位置の公開資料なし） · `00aeb7d8`（命令位置の公開資料なし）

~~~diff
- 00aeb718 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00aeb718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb7e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb7e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb718 bytes 60ee03f9
+ 00aeb7e0 bytes 604e04f9
- 00aeb6fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00aeb6fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb7c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb7c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb6fc bytes 68ee43f9
+ 00aeb7c4 bytes 684e44f9
- 00aeb710 ["INT_ADD", "register:40f0:8", ["const:aeb710:8", "const:4:8"]]
- 00aeb710 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb7d8 ["INT_ADD", "register:40f0:8", ["const:aeb7d8:8", "const:4:8"]]
+ 00aeb7d8 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb710 bytes 20ca0394
+ 00aeb7d8 bytes 1aca0394
~~~


<a id="compare-2e917525fa9041d0a9765dd86cef40b3"></a>

### [`00aeb72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb72c.md) → [`00aeb7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7f4.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00aeb75c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb824"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeb808",
      "incomplete_value": true,
      "site": "00aeb808",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb740",
      "incomplete_value": true,
      "site": "00aeb740",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeb804",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeb74c",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aeb754",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aeb804",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb814",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "00aeb81c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb72c.md#insn-00aeb740) · [`00aeb754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb72c.md#insn-00aeb754) · [`00aeb75c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb72c.md#insn-00aeb75c)
- 新版 `00aeb808`（命令位置の公開資料なし）

~~~diff
- 00aeb740 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeb740 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aeb808 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aeb808 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeb740 bytes 080100b5
+ 00aeb808 bytes 080100b5
- 00aeb754 ["INT_ADD", "register:40f0:8", ["const:aeb754:8", "const:4:8"]]
- 00aeb754 ["CALL", null, ["callee:00bde040:8"]]
- 00aeb754 bytes 0fca0394
- 00aeb75c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00aeb75c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb75c bytes 60ee03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76faf7dd40060dba8b77fc92575f6da1"></a>

### [`00aeb770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb770.md) → [`00aeb838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb838.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb868"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb84c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb784",
      "incomplete_value": true,
      "site": "00aeb784",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeb848",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb84c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb7a4"
      ]
    ],
    [
      "unmatched:00aeb7a0",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb848",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb84c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb86c"
      ]
    ],
    [
      "00aeb868",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb770.md#insn-00aeb7a0) · [`00aeb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb770.md#insn-00aeb7b0)
- 新版 `00aeb868`（命令位置の公開資料なし）

~~~diff
- 00aeb7a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00aeb7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb7a0 bytes 60ee03f9
- 00aeb7b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aeb7b0 ["RETURN", null, ["register:0:8"]]
- 00aeb7b0 bytes c0035fd6
+ 00aeb868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb868 bytes 604e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-271b1f34585f7b34411f671ab13a5f04"></a>

### [`00aeb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb7c0.md) → [`00aeb888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "definition_site": "00aeb910",
      "incomplete_value": true,
      "site": "00aeb910",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb848",
      "incomplete_value": true,
      "site": "00aeb848",
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
            "const:7e0:8"
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
      "site": "00aeb800"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00aeb8c8"
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
      "00aeb89c",
      "READ",
      [
        "storage",
        "010a07e0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeb7f4",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb910",
      "WRITE",
      [
        "storage",
        "010a07e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb89c",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb8bc",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb910",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb7c0.md#insn-00aeb800) · [`00aeb848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb7c0.md#insn-00aeb848)
- 新版 `00aeb910`（命令位置の公開資料なし） · `00aeb8c8`（命令位置の公開資料なし）

~~~diff
- 00aeb800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb800 ["INT_ADD", "register:40f0:8", ["const:aeb800:8", "const:4:8"]]
- 00aeb800 ["CALLIND", null, ["register:0:8"]]
- 00aeb800 bytes 00013fd6
- 00aeb848 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb848 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e0:8"]]
- 00aeb848 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeb910 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeb910 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8a0:8"]]
+ 00aeb910 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb848 bytes a0821f39
+ 00aeb910 bytes a0822239
+ 00aeb8c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb8c8 ["INT_ADD", "register:40f0:8", ["const:aeb8c8:8", "const:4:8"]]
+ 00aeb8c8 ["CALLIND", null, ["register:0:8"]]
+ 00aeb8c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a072d768599e62801d9c7f5e919b9d"></a>

### [`00aeb85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb85c.md) → [`00aeb924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb924.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 30.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb85c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb860"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb85c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb860",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb864",
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
      "00aeb924",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aeb928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeb92c",
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

- 旧版 [`00aeb85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb85c.md#insn-00aeb85c) · [`00aeb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb85c.md#insn-00aeb860) · [`00aeb864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb85c.md#insn-00aeb864)

~~~diff
- 00aeb85c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aeb85c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aeb85c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb85c bytes f50f1df8
- 00aeb860 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb860 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb860 bytes f44f01a9
- 00aeb864 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb864 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb864 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aeb864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb864 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd265592365728f8410f1139024a1f11"></a>

### [`00aeb8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb8fc.md) → [`00aeb9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

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
      "site": "00aeb93c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeba04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb910",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeb918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeba08"
      ]
    ],
    [
      "unmatched:00aeb93c",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb9d8",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb9e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeba08"
      ]
    ],
    [
      "00aeba04",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb8fc.md#insn-00aeb918) · [`00aeb934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb8fc.md#insn-00aeb934) · [`00aeb93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeb8fc.md#insn-00aeb93c)
- 新版 `00aeb9fc`（命令位置の公開資料なし）

~~~diff
- 00aeb918 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb918 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aeb918 bytes 410100b5
- 00aeb934 ["INT_ADD", "register:40f0:8", ["const:aeb934:8", "const:4:8"]]
- 00aeb934 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeb9fc ["INT_ADD", "register:40f0:8", ["const:aeb9fc:8", "const:4:8"]]
+ 00aeb9fc ["CALL", null, ["callee:00bde040:8"]]
- 00aeb934 bytes 97c90394
+ 00aeb9fc bytes 91c90394
- 00aeb93c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00aeb93c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb93c bytes 80ee03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75611945275dec6e1d1e55387471579f"></a>

### [`00aeba18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba18.md) → [`00aebae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebae0.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aebafc",
      "incomplete_value": false,
      "site": "00aebb00",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeba34",
      "incomplete_value": false,
      "site": "00aeba38",
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
      "definition_site": "00aebb0c",
      "incomplete_value": true,
      "site": "00aebb18",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeba44",
      "incomplete_value": true,
      "site": "00aeba50",
      "value": [
        "LOAD",
        "8",
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
      "00aebafc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aebb0c",
      "DATA",
      [
        "storage",
        "010a07f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aebafc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aebb0c",
      "DATA",
      [
        "storage",
        "010a08b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba18.md#insn-00aeba38) · [`00aeba34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba18.md#insn-00aeba34) · [`00aeba40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba18.md#insn-00aeba40)
- 新版 `00aebb00`（命令位置の公開資料なし） · `00aebafc`（命令位置の公開資料なし） · `00aebb08`（命令位置の公開資料なし）

~~~diff
- 00aeba38 ["INT_ADD", "register:40f0:8", ["const:aeba38:8", "const:4:8"]]
- 00aeba38 ["CALL", null, ["callee:00bde130:8"]]
+ 00aebb00 ["INT_ADD", "register:40f0:8", ["const:aebb00:8", "const:4:8"]]
+ 00aebb00 ["CALL", null, ["callee:00bde130:8"]]
- 00aeba38 bytes 92c90394
+ 00aebb00 bytes 8cc90394
- 00aeba34 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aeba34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aebafc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aebafc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebafc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebafc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeba34 bytes 00c81791
+ 00aebafc bytes 00fc1991
- 00aeba40 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00aeba40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeba40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeba40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebb08 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 00aebb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeba40 bytes 08c11f91
+ 00aebb08 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96f61fb806ee89aa644929496e9513d"></a>

### [`00aeba54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba54.md) → [`00aebb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb1c.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00aeba80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aebb48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aebb30",
      "incomplete_value": true,
      "site": "00aebb30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeba68",
      "incomplete_value": true,
      "site": "00aeba68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aebb2c",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeba84"
      ]
    ],
    [
      "unmatched:00aeba74",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aebb2c",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebb4c"
      ]
    ],
    [
      "00aebb3c",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba54.md#insn-00aeba68) · [`00aeba78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba54.md#insn-00aeba78) · [`00aeba80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba54.md#insn-00aeba80)
- 新版 `00aebb30`（命令位置の公開資料なし）

~~~diff
- 00aeba68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeba68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aebb30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aebb30 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeba68 bytes e80000b5
+ 00aebb30 bytes e80000b5
- 00aeba78 ["INT_ADD", "register:40f0:8", ["const:aeba78:8", "const:4:8"]]
- 00aeba78 ["CALL", null, ["callee:00bde040:8"]]
- 00aeba78 bytes 46c90394
- 00aeba80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00aeba80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeba80 bytes 60fe03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f903398f9ed818c9c61b9de4fec34fd"></a>

### [`00aeba94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba94.md) → [`00aebb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00aebb88",
      "incomplete_value": true,
      "site": "00aebb88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebac0",
      "incomplete_value": true,
      "site": "00aebac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "definition_site": "00aebb70",
      "incomplete_value": true,
      "site": "00aebb70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebaa8",
      "incomplete_value": true,
      "site": "00aebaa8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aebb78",
      "incomplete_value": false,
      "site": "00aebb80",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebab0",
      "incomplete_value": false,
      "site": "00aebab8",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aebb6c",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb78",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebb88",
      "WRITE",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebb6c",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb78",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebb88",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba94.md#insn-00aebab8) · [`00aebac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba94.md#insn-00aebac0) · [`00aebaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba94.md#insn-00aebaa4)
- 新版 `00aebb80`（命令位置の公開資料なし） · `00aebb88`（命令位置の公開資料なし） · `00aebb6c`（命令位置の公開資料なし）

~~~diff
- 00aebab8 ["INT_ADD", "register:40f0:8", ["const:aebab8:8", "const:4:8"]]
- 00aebab8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aebb80 ["INT_ADD", "register:40f0:8", ["const:aebb80:8", "const:4:8"]]
+ 00aebb80 ["CALL", null, ["callee:00bde040:8"]]
- 00aebab8 bytes 36c90394
+ 00aebb80 bytes 30c90394
- 00aebac0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00aebac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebb88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00aebb88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebac0 bytes 60fe03f9
+ 00aebb88 bytes 605e04f9
- 00aebaa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00aebaa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebb6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00aebb6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebaa4 bytes 68fe43f9
+ 00aebb6c bytes 685e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8772263fa73fc62105c15ce475a3f87"></a>

### [`00aebad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebad4.md) → [`00aebb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00aebb04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aebbcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aebbb0",
      "incomplete_value": true,
      "site": "00aebbb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebae8",
      "incomplete_value": true,
      "site": "00aebae8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aebbac",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aebaf4",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aebafc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aebbac",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbbc",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebbc4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebad4.md#insn-00aebae8) · [`00aebafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebad4.md#insn-00aebafc) · [`00aebb04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebad4.md#insn-00aebb04)
- 新版 `00aebbb0`（命令位置の公開資料なし）

~~~diff
- 00aebae8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebae8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aebbb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aebbb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aebae8 bytes 080100b5
+ 00aebbb0 bytes 080100b5
- 00aebafc ["INT_ADD", "register:40f0:8", ["const:aebafc:8", "const:4:8"]]
- 00aebafc ["CALL", null, ["callee:00bde040:8"]]
- 00aebafc bytes 25c90394
- 00aebb04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00aebb04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebb04 bytes 60fe03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e2b11c6602cacc2216146f217b7927"></a>

### [`00aebb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb18.md) → [`00aebbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebbe0.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00aebb48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aebc10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aebbf4",
      "incomplete_value": true,
      "site": "00aebbf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebb2c",
      "incomplete_value": true,
      "site": "00aebb2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aebbf0",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aebb4c"
      ]
    ],
    [
      "unmatched:00aebb34",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aebbf0",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebc14"
      ]
    ],
    [
      "00aebbfc",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb18.md#insn-00aebb40) · [`00aebb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb18.md#insn-00aebb48) · [`00aebb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb18.md#insn-00aebb58)
- 新版 `00aebc08`（命令位置の公開資料なし）

~~~diff
- 00aebb40 ["INT_ADD", "register:40f0:8", ["const:aebb40:8", "const:4:8"]]
- 00aebb40 ["CALL", null, ["callee:00bde040:8"]]
+ 00aebc08 ["INT_ADD", "register:40f0:8", ["const:aebc08:8", "const:4:8"]]
+ 00aebc08 ["CALL", null, ["callee:00bde040:8"]]
- 00aebb40 bytes 14c90394
+ 00aebc08 bytes 0ec90394
- 00aebb48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00aebb48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebb48 bytes 60fe03f9
- 00aebb58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aebb58 ["RETURN", null, ["register:0:8"]]
- 00aebb58 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6a4e7fb0672ff51d4949601f3fee07"></a>

### [`00aebb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb68.md) → [`00aebc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebc30.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aebcb8",
      "incomplete_value": true,
      "site": "00aebcb8",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebbf0",
      "incomplete_value": true,
      "site": "00aebbf0",
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
            "const:800:8"
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
      "site": "00aebbc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aebc8c"
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
      "00aebc44",
      "READ",
      [
        "storage",
        "010a0800",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebc50",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aebbf4"
      ]
    ],
    [
      "unmatched:00aebb9c",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebc44",
      "READ",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebc50",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebcbc"
      ]
    ],
    [
      "00aebc64",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb68.md#insn-00aebba8) · [`00aebbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb68.md#insn-00aebbc4) · [`00aebbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebb68.md#insn-00aebbf0)
- 新版 `00aebc70`（命令位置の公開資料なし） · `00aebcb8`（命令位置の公開資料なし）

~~~diff
- 00aebba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebba8 ["INT_ADD", "register:40f0:8", ["const:aebba8:8", "const:4:8"]]
- 00aebba8 ["CALLIND", null, ["register:0:8"]]
+ 00aebc70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aebc70 ["INT_ADD", "register:40f0:8", ["const:aebc70:8", "const:4:8"]]
+ 00aebc70 ["CALLIND", null, ["register:0:8"]]
- 00aebba8 bytes 00013fd6
+ 00aebc70 bytes 00013fd6
- 00aebbc4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00aebbc4 bytes 20010054
- 00aebbf0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aebbf0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:800:8"]]
- 00aebbf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aebcb8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aebcb8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8c0:8"]]
+ 00aebcb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aebbf0 bytes a0022039
+ 00aebcb8 bytes a0022339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e203611d71bba29413bfbd27815dba25"></a>

### [`00aebc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebc04.md) → [`00aebccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebccc.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aebd08",
      "incomplete_value": true,
      "site": "00aebd08",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc40",
      "incomplete_value": true,
      "site": "00aebc40",
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
            "const:800:8"
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
      "definition_site": "00aebd58",
      "incomplete_value": true,
      "site": "00aebd58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc90",
      "incomplete_value": true,
      "site": "00aebc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "definition_site": "00aebce4",
      "incomplete_value": true,
      "site": "00aebce4",
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
      "definition_site": "00aebc1c",
      "incomplete_value": true,
      "site": "00aebc1c",
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
      "00aebce0",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebcec",
      "READ",
      [
        "storage",
        "010a0800",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebd08",
      "WRITE",
      [
        "storage",
        "010a0800",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aebce0",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebcec",
      "READ",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebd08",
      "WRITE",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebc04.md#insn-00aebc40) · [`00aebc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebc04.md#insn-00aebc8c) · [`00aebc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebc04.md#insn-00aebc90)
- 新版 `00aebd08`（命令位置の公開資料なし） · `00aebd54`（命令位置の公開資料なし） · `00aebd58`（命令位置の公開資料なし）

~~~diff
- 00aebc40 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aebc40 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aebc40 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:800:8"]]
- 00aebc40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aebd08 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aebd08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aebd08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8c0:8"]]
+ 00aebd08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aebc40 bytes bf022039
+ 00aebd08 bytes bf022339
- 00aebc8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebc8c ["INT_ADD", "register:40f0:8", ["const:aebc8c:8", "const:4:8"]]
- 00aebc8c ["CALLIND", null, ["register:0:8"]]
+ 00aebd54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aebd54 ["INT_ADD", "register:40f0:8", ["const:aebd54:8", "const:4:8"]]
+ 00aebd54 ["CALLIND", null, ["register:0:8"]]
- 00aebc8c bytes 00013fd6
+ 00aebd54 bytes 00013fd6
- 00aebc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00aebc90 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aebc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aebd58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00aebd58 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aebd58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aebc90 bytes 9ffe03f9
+ 00aebd58 bytes 9f5e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a2174ccaeb00e99dd3c05601fd8b82"></a>

### [`00aebca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebca4.md) → [`00aebd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00aebce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aebdac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebcc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebcb8",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aebcc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebdb0"
      ]
    ],
    [
      "unmatched:00aebcc8",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aebd80",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebd88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebdb0"
      ]
    ],
    [
      "00aebd90",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebca4.md#insn-00aebcc0) · [`00aebcdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebca4.md#insn-00aebcdc) · [`00aebce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebca4.md#insn-00aebce4)
- 新版 `00aebda4`（命令位置の公開資料なし）

~~~diff
- 00aebcc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aebcc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aebcc0 bytes 410100b5
- 00aebcdc ["INT_ADD", "register:40f0:8", ["const:aebcdc:8", "const:4:8"]]
- 00aebcdc ["CALL", null, ["callee:00bde040:8"]]
+ 00aebda4 ["INT_ADD", "register:40f0:8", ["const:aebda4:8", "const:4:8"]]
+ 00aebda4 ["CALL", null, ["callee:00bde040:8"]]
- 00aebcdc bytes adc80394
+ 00aebda4 bytes a7c80394
- 00aebce4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00aebce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebce4 bytes 80fe03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0e01143c329e584402fe5f8f5f82d6"></a>

### [`00aebd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd14.md) → [`00aebddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebddc.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5e0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde690.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aebdf8",
      "incomplete_value": false,
      "site": "00aebdfc",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd30",
      "incomplete_value": false,
      "site": "00aebd34",
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
      "definition_site": "00aebe08",
      "incomplete_value": true,
      "site": "00aebe14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebd40",
      "incomplete_value": true,
      "site": "00aebd4c",
      "value": [
        "LOAD",
        "8",
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
      "00aebdf8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aebe08",
      "DATA",
      [
        "storage",
        "010a0808",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebdf8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aebe08",
      "DATA",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd14.md#insn-00aebd34) · [`00aebd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd14.md#insn-00aebd30) · [`00aebd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd14.md#insn-00aebd3c)
- 新版 `00aebdfc`（命令位置の公開資料なし） · `00aebdf8`（命令位置の公開資料なし） · `00aebe04`（命令位置の公開資料なし）

~~~diff
- 00aebd34 ["INT_ADD", "register:40f0:8", ["const:aebd34:8", "const:4:8"]]
- 00aebd34 ["CALL", null, ["callee:00bde130:8"]]
+ 00aebdfc ["INT_ADD", "register:40f0:8", ["const:aebdfc:8", "const:4:8"]]
+ 00aebdfc ["CALL", null, ["callee:00bde130:8"]]
- 00aebd34 bytes d3c80394
+ 00aebdfc bytes cdc80394
- 00aebd30 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aebd30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebd30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebd30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aebdf8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aebdf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebdf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebdf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebd30 bytes 001c1591
+ 00aebdf8 bytes 00501791
- 00aebd3c ["COPY", "tmp:0:8", ["const:808:8"]]
- 00aebd3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aebd3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aebd3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebe04 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00aebe04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebe04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebe04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aebd3c bytes 08212091
+ 00aebe04 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c61daf8cc3028dde00ed45a1013df5b"></a>

### [`00aebd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd50.md) → [`00aebe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aebe58",
      "incomplete_value": true,
      "site": "00aebe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd90",
      "incomplete_value": true,
      "site": "00aebd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "definition_site": "00aebe34",
      "incomplete_value": true,
      "site": "00aebe34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd6c",
      "incomplete_value": true,
      "site": "00aebd6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aebe3c",
      "incomplete_value": false,
      "site": "00aebe50",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd74",
      "incomplete_value": false,
      "site": "00aebd88",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aebe2c",
      "READ",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebe3c",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebe58",
      "WRITE",
      [
        "storage",
        "010a07f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebe2c",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebe3c",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebe58",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd50.md#insn-00aebd88) · [`00aebd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd50.md#insn-00aebd90) · [`00aebd64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd50.md#insn-00aebd64)
- 新版 `00aebe50`（命令位置の公開資料なし） · `00aebe58`（命令位置の公開資料なし） · `00aebe2c`（命令位置の公開資料なし）

~~~diff
- 00aebd88 ["INT_ADD", "register:40f0:8", ["const:aebd88:8", "const:4:8"]]
- 00aebd88 ["CALL", null, ["callee:00bde040:8"]]
+ 00aebe50 ["INT_ADD", "register:40f0:8", ["const:aebe50:8", "const:4:8"]]
+ 00aebe50 ["CALL", null, ["callee:00bde040:8"]]
- 00aebd88 bytes 82c80394
+ 00aebe50 bytes 7cc80394
- 00aebd90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00aebd90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebe58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00aebe58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebd90 bytes 80fe03f9
+ 00aebe58 bytes 805e04f9
- 00aebd64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00aebd64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebe2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00aebe2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebd64 bytes 81fe43f9
+ 00aebe2c bytes 815e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866755f86d2235d45bb96c497792dfc1"></a>

### [`00aebdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebdfc.md) → [`00aebec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aebef0",
      "incomplete_value": true,
      "site": "00aebef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe28",
      "incomplete_value": true,
      "site": "00aebe28",
      "value": [
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
      "definition_site": "00aebed8",
      "incomplete_value": true,
      "site": "00aebed8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe10",
      "incomplete_value": true,
      "site": "00aebe10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aebe10"
      ],
      [
        "FALL_THROUGH",
        "00aebed8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebed8",
      "incomplete_value": true,
      "site": "00aebef0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe10",
      "incomplete_value": true,
      "site": "00aebe28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aebed4",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebef0",
      "WRITE",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebed4",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebef0",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebdfc.md#insn-00aebe28) · [`00aebe0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebdfc.md#insn-00aebe0c) · [`00aebe20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebdfc.md#insn-00aebe20)
- 新版 `00aebef0`（命令位置の公開資料なし） · `00aebed4`（命令位置の公開資料なし） · `00aebee8`（命令位置の公開資料なし）

~~~diff
- 00aebe28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00aebe28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebef0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
+ 00aebef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebe28 bytes 601204f9
+ 00aebef0 bytes 607204f9
- 00aebe0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00aebe0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebed4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
+ 00aebed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebe0c bytes 681244f9
+ 00aebed4 bytes 687244f9
- 00aebe20 ["INT_ADD", "register:40f0:8", ["const:aebe20:8", "const:4:8"]]
- 00aebe20 ["CALL", null, ["callee:00bde040:8"]]
+ 00aebee8 ["INT_ADD", "register:40f0:8", ["const:aebee8:8", "const:4:8"]]
+ 00aebee8 ["CALL", null, ["callee:00bde040:8"]]
- 00aebe20 bytes 5cc80394
+ 00aebee8 bytes 56c80394
~~~


<a id="compare-f091dfd9f4188c841eb2a375c5d93e87"></a>

### [`00aebe3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe3c.md) → [`00aebf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf04.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebe3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebe40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aebf14",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebf04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aebf08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aebf14",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe3c.md#insn-00aebe3c) · [`00aebe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe3c.md#insn-00aebe40) · [`00aebe50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe3c.md#insn-00aebe50)
- 新版 `00aebf18`（命令位置の公開資料なし）

~~~diff
- 00aebe3c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00aebe3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aebe3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aebe3c bytes f30f1ef8
- 00aebe40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebe40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebe40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aebe40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebe40 bytes fd7b01a9
- 00aebe50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebe50 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aebf18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aebf18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aebe50 bytes e80000b5
+ 00aebf18 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52b8f36aec095ef18c31914d8f6881d9"></a>

### [`00aebe7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe7c.md) → [`00aebf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00aebeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aebf74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aebf58",
      "incomplete_value": true,
      "site": "00aebf58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe90",
      "incomplete_value": true,
      "site": "00aebe90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aebf54",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aebe9c",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aebea4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aebf54",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebf64",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ],
    [
      "00aebf6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe7c.md#insn-00aebe90) · [`00aebea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe7c.md#insn-00aebea4) · [`00aebeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebe7c.md#insn-00aebeac)
- 新版 `00aebf58`（命令位置の公開資料なし）

~~~diff
- 00aebe90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebe90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aebf58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aebf58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aebe90 bytes 080100b5
+ 00aebf58 bytes 080100b5
- 00aebea4 ["INT_ADD", "register:40f0:8", ["const:aebea4:8", "const:4:8"]]
- 00aebea4 ["CALL", null, ["callee:00bde040:8"]]
- 00aebea4 bytes 3bc80394
- 00aebeac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00aebeac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebeac bytes 601204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89fb614ef2cc1b5cf467230b3cb31013"></a>

### [`00aebec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebec0.md) → [`00aebf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aebfb8",
      "incomplete_value": true,
      "site": "00aebfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebef0",
      "incomplete_value": true,
      "site": "00aebef0",
      "value": [
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
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebf9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebed4",
      "incomplete_value": true,
      "site": "00aebed4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aebed4"
      ],
      [
        "FALL_THROUGH",
        "00aebf9c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebfb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebed4",
      "incomplete_value": true,
      "site": "00aebef0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00aebf98",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebfb8",
      "WRITE",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebf98",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebfb8",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebec0.md#insn-00aebef0) · [`00aebed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebec0.md#insn-00aebed0) · [`00aebee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebec0.md#insn-00aebee8)
- 新版 `00aebfb8`（命令位置の公開資料なし） · `00aebf98`（命令位置の公開資料なし） · `00aebfb0`（命令位置の公開資料なし）

~~~diff
- 00aebef0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00aebef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
+ 00aebfb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebef0 bytes 601204f9
+ 00aebfb8 bytes 607204f9
- 00aebed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
- 00aebed0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebf98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
+ 00aebf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebed0 bytes 681244f9
+ 00aebf98 bytes 687244f9
- 00aebee8 ["INT_ADD", "register:40f0:8", ["const:aebee8:8", "const:4:8"]]
- 00aebee8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aebfb0 ["INT_ADD", "register:40f0:8", ["const:aebfb0:8", "const:4:8"]]
+ 00aebfb0 ["CALL", null, ["callee:00bde040:8"]]
- 00aebee8 bytes 2ac80394
+ 00aebfb0 bytes 24c80394
~~~


<a id="compare-3fce4e62ff4a30c813c16df3c5618e69"></a>

### [`00aebf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebf10.md) → [`00aebfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebfd8.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec060",
      "incomplete_value": true,
      "site": "00aec060",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf98",
      "incomplete_value": true,
      "site": "00aebf98",
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
      "definition_site": "00aec00c",
      "incomplete_value": true,
      "site": "00aec018",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf44",
      "incomplete_value": true,
      "site": "00aebf50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebf7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aebfec",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec00c",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec060",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aebfec",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec00c",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec060",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebf10.md#insn-00aebf50) · [`00aebf7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebf10.md#insn-00aebf7c) · [`00aebf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebf10.md#insn-00aebf98)
- 新版 `00aec018`（命令位置の公開資料なし） · `00aec060`（命令位置の公開資料なし）

~~~diff
- 00aebf50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebf50 ["INT_ADD", "register:40f0:8", ["const:aebf50:8", "const:4:8"]]
- 00aebf50 ["CALLIND", null, ["register:0:8"]]
+ 00aec018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec018 ["INT_ADD", "register:40f0:8", ["const:aec018:8", "const:4:8"]]
+ 00aec018 ["CALLIND", null, ["register:0:8"]]
- 00aebf50 bytes 00013fd6
+ 00aec018 bytes 00013fd6
- 00aebf7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebf7c ["INT_ADD", "register:40f0:8", ["const:aebf7c:8", "const:4:8"]]
- 00aebf7c ["CALLIND", null, ["register:0:8"]]
- 00aebf7c bytes 00013fd6
- 00aebf98 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aebf98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:828:8"]]
- 00aebf98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec060 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec060 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8e8:8"]]
+ 00aec060 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aebf98 bytes a0a22039
+ 00aec060 bytes a0a22339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95b5419e3163d5195a84dc965051696f"></a>

### [`00aebfac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebfac.md) → [`00aec074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aec0b0",
      "incomplete_value": true,
      "site": "00aec0b0",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebfe8",
      "incomplete_value": true,
      "site": "00aebfe8",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec100",
      "incomplete_value": true,
      "site": "00aec100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec038",
      "incomplete_value": true,
      "site": "00aec038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00aec08c",
      "incomplete_value": true,
      "site": "00aec08c",
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
      "definition_site": "00aebfc4",
      "incomplete_value": true,
      "site": "00aebfc4",
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
      "00aec088",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec094",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec0b0",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec088",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec094",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec0b0",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebfe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebfac.md#insn-00aebfe8) · [`00aec034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebfac.md#insn-00aec034) · [`00aec038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebfac.md#insn-00aec038)
- 新版 `00aec0b0`（命令位置の公開資料なし） · `00aec0fc`（命令位置の公開資料なし） · `00aec100`（命令位置の公開資料なし）

~~~diff
- 00aebfe8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aebfe8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aebfe8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:828:8"]]
- 00aebfe8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aec0b0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aec0b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aec0b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8e8:8"]]
+ 00aec0b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aebfe8 bytes bfa22039
+ 00aec0b0 bytes bfa22339
- 00aec034 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec034 ["INT_ADD", "register:40f0:8", ["const:aec034:8", "const:4:8"]]
- 00aec034 ["CALLIND", null, ["register:0:8"]]
+ 00aec0fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec0fc ["INT_ADD", "register:40f0:8", ["const:aec0fc:8", "const:4:8"]]
+ 00aec0fc ["CALLIND", null, ["register:0:8"]]
- 00aec034 bytes 00013fd6
+ 00aec0fc bytes 00013fd6
- 00aec038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
- 00aec038 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aec038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aec100 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
+ 00aec100 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aec100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aec038 bytes 9f1204f9
+ 00aec100 bytes 9f7204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e2410a822a48914bae0908253d66418"></a>

### [`00aec04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec04c.md) → [`00aec114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec114.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

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
      "site": "00aec08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aec154"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec060",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec158"
      ]
    ],
    [
      "unmatched:00aec08c",
      "WRITE",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec128",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec158"
      ]
    ],
    [
      "00aec154",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec04c.md#insn-00aec068) · [`00aec084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec04c.md#insn-00aec084) · [`00aec08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec04c.md#insn-00aec08c)
- 新版 `00aec14c`（命令位置の公開資料なし）

~~~diff
- 00aec068 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec068 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec068 bytes 410100b5
- 00aec084 ["INT_ADD", "register:40f0:8", ["const:aec084:8", "const:4:8"]]
- 00aec084 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec14c ["INT_ADD", "register:40f0:8", ["const:aec14c:8", "const:4:8"]]
+ 00aec14c ["CALL", null, ["callee:00bde040:8"]]
- 00aec084 bytes c3c70394
+ 00aec14c bytes bdc70394
- 00aec08c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
- 00aec08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec08c bytes 801204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f731cf4dfb9f0b1097fe7615f15495"></a>

### [`00aec0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0bc.md) → [`00aec184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5a0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde650.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aec1a0",
      "incomplete_value": false,
      "site": "00aec1a4",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec0d8",
      "incomplete_value": false,
      "site": "00aec0dc",
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
      "definition_site": "00aec1b0",
      "incomplete_value": true,
      "site": "00aec1bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec0e8",
      "incomplete_value": true,
      "site": "00aec0f4",
      "value": [
        "LOAD",
        "8",
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
      "00aec1a0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aec1b0",
      "DATA",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec1a0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aec1b0",
      "DATA",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0bc.md#insn-00aec0dc) · [`00aec0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0bc.md#insn-00aec0d8) · [`00aec0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0bc.md#insn-00aec0e4)
- 新版 `00aec1a4`（命令位置の公開資料なし） · `00aec1a0`（命令位置の公開資料なし） · `00aec1ac`（命令位置の公開資料なし）

~~~diff
- 00aec0dc ["INT_ADD", "register:40f0:8", ["const:aec0dc:8", "const:4:8"]]
- 00aec0dc ["CALL", null, ["callee:00bde130:8"]]
+ 00aec1a4 ["INT_ADD", "register:40f0:8", ["const:aec1a4:8", "const:4:8"]]
+ 00aec1a4 ["CALL", null, ["callee:00bde130:8"]]
- 00aec0dc bytes e9c70394
+ 00aec1a4 bytes e3c70394
- 00aec0d8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aec0d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec0d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec0d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec1a0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aec1a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec1a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec1a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec0d8 bytes 001c1591
+ 00aec1a0 bytes 00501791
- 00aec0e4 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00aec0e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec0e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec0e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec1ac ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00aec1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec0e4 bytes 08c12091
+ 00aec1ac bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6113d39b47df532043a732bb5cd13e8"></a>

### [`00aec0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0f8.md) → [`00aec1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

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
      "site": "00aec138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aec200"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec10c",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec114",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec204"
      ]
    ],
    [
      "unmatched:00aec138",
      "WRITE",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec1d4",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec1dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec204"
      ]
    ],
    [
      "00aec200",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0f8.md#insn-00aec114) · [`00aec130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0f8.md#insn-00aec130) · [`00aec138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0f8.md#insn-00aec138)
- 新版 `00aec1f8`（命令位置の公開資料なし）

~~~diff
- 00aec114 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec114 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aec114 bytes 410100b5
- 00aec130 ["INT_ADD", "register:40f0:8", ["const:aec130:8", "const:4:8"]]
- 00aec130 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec1f8 ["INT_ADD", "register:40f0:8", ["const:aec1f8:8", "const:4:8"]]
+ 00aec1f8 ["CALL", null, ["callee:00bde040:8"]]
- 00aec130 bytes 98c70394
+ 00aec1f8 bytes 92c70394
- 00aec138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
- 00aec138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec138 bytes 801204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

