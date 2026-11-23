# v15.7.2 → v15.7.3 · 最優先の変更候補 (68)

[一覧の目次](README.md)

<a id="compare-0222ae0ce4970ef541594e63bc02d35f"></a>

### [`00b538d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b538d4.md) → [`00b5399c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5399c.md) _ZN8firebase13remote_config8internal15config_settings11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b539b8",
      "incomplete_value": false,
      "site": "00b539bc",
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
      "definition_site": "00b538f0",
      "incomplete_value": false,
      "site": "00b538f4",
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
      "definition_site": "00b539c8",
      "incomplete_value": true,
      "site": "00b539d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53900",
      "incomplete_value": true,
      "site": "00b5390c",
      "value": [
        "LOAD",
        "8",
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
      "00b539b8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b539c8",
      "DATA",
      [
        "storage",
        "010a11e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b539b8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b539c8",
      "DATA",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b538f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b538d4.md#insn-00b538f4) · [`00b538f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b538d4.md#insn-00b538f0) · [`00b538fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b538d4.md#insn-00b538fc)
- 新版 `00b539bc`（命令位置の公開資料なし） · `00b539b8`（命令位置の公開資料なし） · `00b539c4`（命令位置の公開資料なし）

~~~diff
- 00b538f4 ["INT_ADD", "register:40f0:8", ["const:b538f4:8", "const:4:8"]]
- 00b538f4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b539bc ["INT_ADD", "register:40f0:8", ["const:b539bc:8", "const:4:8"]]
+ 00b539bc ["CALL", null, ["callee:00bde130:8"]]
- 00b538f4 bytes e3290294
+ 00b539bc bytes dd290294
- 00b538f0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b538f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b538f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b538f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b539b8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b539b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b539b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b539b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b538f0 bytes 001c1591
+ 00b539b8 bytes 00501791
- 00b538fc ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00b538fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b538fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b538fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b539c4 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00b539c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b539c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b539c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b538fc bytes 08810791
+ 00b539c4 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ca3966fe78c47a5e850dedc8bded4ac"></a>

### [`00b53910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53910.md) → [`00b539d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b539d8.md) _ZN8firebase13remote_config8internal15config_settings13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53a18",
      "incomplete_value": true,
      "site": "00b53a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53950",
      "incomplete_value": true,
      "site": "00b53950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:1d0:8"
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
      "definition_site": "00b539f4",
      "incomplete_value": true,
      "site": "00b539f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5392c",
      "incomplete_value": true,
      "site": "00b5392c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b539fc",
      "incomplete_value": false,
      "site": "00b53a10",
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
            "const:ea4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53934",
      "incomplete_value": false,
      "site": "00b53948",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b539ec",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b539fc",
      "PARAM",
      [
        "storage",
        "002a7f38",
        null,
        "string"
      ]
    ],
    [
      "00b53a18",
      "WRITE",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b539ec",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b539fc",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b53a18",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53910.md#insn-00b53948) · [`00b53950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53910.md#insn-00b53950) · [`00b53924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53910.md#insn-00b53924)
- 新版 `00b53a10`（命令位置の公開資料なし） · `00b53a18`（命令位置の公開資料なし） · `00b539ec`（命令位置の公開資料なし）

~~~diff
- 00b53948 ["INT_ADD", "register:40f0:8", ["const:b53948:8", "const:4:8"]]
- 00b53948 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53a10 ["INT_ADD", "register:40f0:8", ["const:b53a10:8", "const:4:8"]]
+ 00b53a10 ["CALL", null, ["callee:00bde040:8"]]
- 00b53948 bytes 92290294
+ 00b53a10 bytes 8c290294
- 00b53950 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1d0:8"]]
- 00b53950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
+ 00b53a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53950 bytes 80ea00f9
+ 00b53a18 bytes 804a01f9
- 00b53924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1d0:8"]]
- 00b53924 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b539ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
+ 00b539ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53924 bytes 81ea40f9
+ 00b539ec bytes 814a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688d21e3c2d962bcf2d310c4c1bc5775"></a>

### [`00b539bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539bc.md) → [`00b53a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a84.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

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
      "definition_site": "00b53ab0",
      "incomplete_value": true,
      "site": "00b53ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539e8",
      "incomplete_value": true,
      "site": "00b539e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "definition_site": "00b53a98",
      "incomplete_value": true,
      "site": "00b53a98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539d0",
      "incomplete_value": true,
      "site": "00b539d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53aa4",
      "incomplete_value": false,
      "site": "00b53aa8",
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
            "const:e6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539dc",
      "incomplete_value": false,
      "site": "00b539e0",
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
            "const:f01:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53a94",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53aa4",
      "PARAM",
      [
        "storage",
        "002a8f01",
        null,
        "string"
      ]
    ],
    [
      "00b53ab0",
      "WRITE",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53a94",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53aa4",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53ab0",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b539e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539bc.md#insn-00b539e0) · [`00b539e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539bc.md#insn-00b539e8) · [`00b539cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539bc.md#insn-00b539cc)
- 新版 `00b53aa8`（命令位置の公開資料なし） · `00b53ab0`（命令位置の公開資料なし） · `00b53a94`（命令位置の公開資料なし）

~~~diff
- 00b539e0 ["INT_ADD", "register:40f0:8", ["const:b539e0:8", "const:4:8"]]
- 00b539e0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53aa8 ["INT_ADD", "register:40f0:8", ["const:b53aa8:8", "const:4:8"]]
+ 00b53aa8 ["CALL", null, ["callee:00bde040:8"]]
- 00b539e0 bytes 6c290294
+ 00b53aa8 bytes 66290294
- 00b539e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b539e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53ab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b539e8 bytes 60fe00f9
+ 00b53ab0 bytes 605e01f9
- 00b539cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b539cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53a94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b539cc bytes 68fe40f9
+ 00b53a94 bytes 685e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e182f3650d97a0d9bc8700f6712d1d53"></a>

### [`00b539fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539fc.md) → [`00b53ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ac4.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

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
      "site": "00b53a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53af0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53ad8",
      "incomplete_value": true,
      "site": "00b53ad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a10",
      "incomplete_value": true,
      "site": "00b53a10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b53ad4",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53a2c"
      ]
    ],
    [
      "unmatched:00b53a18",
      "PARAM",
      [
        "storage",
        "002a8f01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b53ad4",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53af4"
      ]
    ],
    [
      "00b53ae0",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539fc.md#insn-00b53a10) · [`00b53a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539fc.md#insn-00b53a20) · [`00b53a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b539fc.md#insn-00b53a28)
- 新版 `00b53ad8`（命令位置の公開資料なし）

~~~diff
- 00b53a10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53a10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b53ad8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b53ad8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53a10 bytes e80000b5
+ 00b53ad8 bytes e80000b5
- 00b53a20 ["INT_ADD", "register:40f0:8", ["const:b53a20:8", "const:4:8"]]
- 00b53a20 ["CALL", null, ["callee:00bde040:8"]]
- 00b53a20 bytes 5c290294
- 00b53a28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b53a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53a28 bytes 60fe00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abe3ff815323fd06dea6134b83d1e98d"></a>

### [`00b53a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a3c.md) → [`00b53b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b04.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b53b34",
      "incomplete_value": true,
      "site": "00b53b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a6c",
      "incomplete_value": true,
      "site": "00b53a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "definition_site": "00b53b18",
      "incomplete_value": true,
      "site": "00b53b18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a50",
      "incomplete_value": true,
      "site": "00b53a50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53b24",
      "incomplete_value": false,
      "site": "00b53b2c",
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
            "const:e6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a5c",
      "incomplete_value": false,
      "site": "00b53a64",
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
            "const:f01:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53b14",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b24",
      "PARAM",
      [
        "storage",
        "002a8f01",
        null,
        "string"
      ]
    ],
    [
      "00b53b34",
      "WRITE",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b14",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b24",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53b34",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a3c.md#insn-00b53a64) · [`00b53a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a3c.md#insn-00b53a6c) · [`00b53a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a3c.md#insn-00b53a4c)
- 新版 `00b53b2c`（命令位置の公開資料なし） · `00b53b34`（命令位置の公開資料なし） · `00b53b14`（命令位置の公開資料なし）

~~~diff
- 00b53a64 ["INT_ADD", "register:40f0:8", ["const:b53a64:8", "const:4:8"]]
- 00b53a64 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53b2c ["INT_ADD", "register:40f0:8", ["const:b53b2c:8", "const:4:8"]]
+ 00b53b2c ["CALL", null, ["callee:00bde040:8"]]
- 00b53a64 bytes 4b290294
+ 00b53b2c bytes 45290294
- 00b53a6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b53a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53a6c bytes 60fe00f9
+ 00b53b34 bytes 605e01f9
- 00b53a4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b53a4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53a4c bytes 68fe40f9
+ 00b53b14 bytes 685e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3663cab3d14372601d10c31c67f61f"></a>

### [`00b53a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a80.md) → [`00b53b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b48.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53b78",
      "incomplete_value": true,
      "site": "00b53b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ab0",
      "incomplete_value": true,
      "site": "00b53ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a94",
      "incomplete_value": true,
      "site": "00b53a94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53b64",
      "incomplete_value": false,
      "site": "00b53b70",
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
            "const:e6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a9c",
      "incomplete_value": false,
      "site": "00b53aa8",
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
            "const:f01:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53b58",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b64",
      "PARAM",
      [
        "storage",
        "002a8f01",
        null,
        "string"
      ]
    ],
    [
      "00b53b78",
      "WRITE",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b58",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b64",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53b78",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a80.md#insn-00b53aa8) · [`00b53ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a80.md#insn-00b53ab0) · [`00b53a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53a80.md#insn-00b53a90)
- 新版 `00b53b70`（命令位置の公開資料なし） · `00b53b78`（命令位置の公開資料なし） · `00b53b58`（命令位置の公開資料なし）

~~~diff
- 00b53aa8 ["INT_ADD", "register:40f0:8", ["const:b53aa8:8", "const:4:8"]]
- 00b53aa8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53b70 ["INT_ADD", "register:40f0:8", ["const:b53b70:8", "const:4:8"]]
+ 00b53b70 ["CALL", null, ["callee:00bde040:8"]]
- 00b53aa8 bytes 3a290294
+ 00b53b70 bytes 34290294
- 00b53ab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b53ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53ab0 bytes 60fe00f9
+ 00b53b78 bytes 605e01f9
- 00b53a90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00b53a90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
+ 00b53b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53a90 bytes 68fe40f9
+ 00b53b58 bytes 685e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89d1bf9567606ab83748e3a2e5a9b70"></a>

### [`00b53ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ad0.md) → [`00b53b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b98.md) _ZN8firebase13remote_config8internal23config_settings_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

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
      "definition_site": "00b53bf0",
      "incomplete_value": true,
      "site": "00b53bf0",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b28",
      "incomplete_value": true,
      "site": "00b53b28",
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
            "const:200:8"
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
      "definition_site": "00b53b04",
      "incomplete_value": true,
      "site": "00b53b10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:1f8:8"
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
      "definition_site": "00b53b00",
      "incomplete_value": true,
      "site": "00b53b10",
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
      "00b53bac",
      "READ",
      [
        "storage",
        "010a1200",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b53b04",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53bf0",
      "WRITE",
      [
        "storage",
        "010a1200",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53bac",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53bcc",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53bf0",
      "WRITE",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ad0.md#insn-00b53b10) · [`00b53b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ad0.md#insn-00b53b28) · [`00b53ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ad0.md#insn-00b53ae4)
- 新版 `00b53bd8`（命令位置の公開資料なし） · `00b53bf0`（命令位置の公開資料なし） · `00b53bac`（命令位置の公開資料なし）

~~~diff
- 00b53b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53b10 ["INT_ADD", "register:40f0:8", ["const:b53b10:8", "const:4:8"]]
- 00b53b10 ["CALLIND", null, ["register:0:8"]]
+ 00b53bd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53bd8 ["INT_ADD", "register:40f0:8", ["const:b53bd8:8", "const:4:8"]]
+ 00b53bd8 ["CALLIND", null, ["register:0:8"]]
- 00b53b10 bytes 00013fd6
+ 00b53bd8 bytes 00013fd6
- 00b53b28 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53b28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:200:8"]]
- 00b53b28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53bf0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53bf0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2c0:8"]]
+ 00b53bf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53b28 bytes a0020839
+ 00b53bf0 bytes a0020b39
- 00b53ae4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:200:8"]]
- 00b53ae4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53ae4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53bac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2c0:8"]]
+ 00b53bac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53bac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53ae4 bytes a8024839
+ 00b53bac bytes a8024b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51a637244217824f3ef53a7976e9db9e"></a>

### [`00b53b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53b3c.md) → [`00b53c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c04.md) _ZN8firebase13remote_config8internal23config_settings_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b53c40",
      "incomplete_value": true,
      "site": "00b53c40",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b78",
      "incomplete_value": true,
      "site": "00b53b78",
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
            "const:200:8"
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
      "definition_site": "00b53c60",
      "incomplete_value": true,
      "site": "00b53c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b98",
      "incomplete_value": true,
      "site": "00b53b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "definition_site": "00b53c1c",
      "incomplete_value": true,
      "site": "00b53c1c",
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
      "definition_site": "00b53b54",
      "incomplete_value": true,
      "site": "00b53b54",
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
      "00b53c18",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c24",
      "READ",
      [
        "storage",
        "010a1200",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c40",
      "WRITE",
      [
        "storage",
        "010a1200",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53c18",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c24",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c40",
      "WRITE",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53b3c.md#insn-00b53b78) · [`00b53b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53b3c.md#insn-00b53b94) · [`00b53b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53b3c.md#insn-00b53b98)
- 新版 `00b53c40`（命令位置の公開資料なし） · `00b53c5c`（命令位置の公開資料なし） · `00b53c60`（命令位置の公開資料なし）

~~~diff
- 00b53b78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53b78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53b78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:200:8"]]
- 00b53b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b53c40 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b53c40 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b53c40 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2c0:8"]]
+ 00b53c40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53b78 bytes bf020839
+ 00b53c40 bytes bf020b39
- 00b53b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53b94 ["INT_ADD", "register:40f0:8", ["const:b53b94:8", "const:4:8"]]
- 00b53b94 ["CALLIND", null, ["register:0:8"]]
+ 00b53c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53c5c ["INT_ADD", "register:40f0:8", ["const:b53c5c:8", "const:4:8"]]
+ 00b53c5c ["CALLIND", null, ["register:0:8"]]
- 00b53b94 bytes 00013fd6
+ 00b53c5c bytes 00013fd6
- 00b53b98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00b53b98 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b53b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b53c60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
+ 00b53c60 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b53c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b53b98 bytes 9ffe00f9
+ 00b53c60 bytes 9f5e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db40e73565369bc1cfc7b2ae159bd6ad"></a>

### [`00b53bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53bac.md) → [`00b53c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c74.md) _ZN8firebase13remote_config8internal23config_settings_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b53bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53cb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53bc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53bc0",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53cb8"
      ]
    ],
    [
      "unmatched:00b53bd0",
      "PARAM",
      [
        "storage",
        "002a8f01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b53c88",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53cb8"
      ]
    ],
    [
      "00b53c98",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53bac.md#insn-00b53bc8) · [`00b53be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53bac.md#insn-00b53be4) · [`00b53bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53bac.md#insn-00b53bec)
- 新版 `00b53cac`（命令位置の公開資料なし）

~~~diff
- 00b53bc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53bc8 bytes 410100b5
- 00b53be4 ["INT_ADD", "register:40f0:8", ["const:b53be4:8", "const:4:8"]]
- 00b53be4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53cac ["INT_ADD", "register:40f0:8", ["const:b53cac:8", "const:4:8"]]
+ 00b53cac ["CALL", null, ["callee:00bde040:8"]]
- 00b53be4 bytes eb280294
+ 00b53cac bytes e5280294
- 00b53bec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00b53bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53bec bytes 80fe00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-108f3267bdf34622d2152986d83ff1a8"></a>

### [`00b53c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c1c.md) → [`00b53ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ce4.md) _ZN8firebase13remote_config8internal23config_settings_builder11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b53d00",
      "incomplete_value": false,
      "site": "00b53d04",
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
      "definition_site": "00b53c38",
      "incomplete_value": false,
      "site": "00b53c3c",
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
      "definition_site": "00b53d10",
      "incomplete_value": true,
      "site": "00b53d1c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53c48",
      "incomplete_value": true,
      "site": "00b53c54",
      "value": [
        "LOAD",
        "8",
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
      "00b53d00",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53d10",
      "DATA",
      [
        "storage",
        "010a1208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53d00",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53d10",
      "DATA",
      [
        "storage",
        "010a12c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c1c.md#insn-00b53c3c) · [`00b53c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c1c.md#insn-00b53c38) · [`00b53c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c1c.md#insn-00b53c44)
- 新版 `00b53d04`（命令位置の公開資料なし） · `00b53d00`（命令位置の公開資料なし） · `00b53d0c`（命令位置の公開資料なし）

~~~diff
- 00b53c3c ["INT_ADD", "register:40f0:8", ["const:b53c3c:8", "const:4:8"]]
- 00b53c3c ["CALL", null, ["callee:00bde130:8"]]
+ 00b53d04 ["INT_ADD", "register:40f0:8", ["const:b53d04:8", "const:4:8"]]
+ 00b53d04 ["CALL", null, ["callee:00bde130:8"]]
- 00b53c3c bytes 11290294
+ 00b53d04 bytes 0b290294
- 00b53c38 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b53c38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53c38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53c38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53d00 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b53d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53c38 bytes 001c1591
+ 00b53d00 bytes 00501791
- 00b53c44 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00b53c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53d0c ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00b53d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53c44 bytes 08210891
+ 00b53d0c bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7088bb1c2b74459684e4f13b181efdd2"></a>

### [`00b53c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c58.md) → [`00b53d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d20.md) _ZN8firebase13remote_config8internal23config_settings_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

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
      "site": "00b53c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53c58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53c6c",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53d24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53d34",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c58.md#insn-00b53c58) · [`00b53c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c58.md#insn-00b53c5c) · [`00b53c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53c58.md#insn-00b53c74)

~~~diff
- 00b53c58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53c58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53c58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53c58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53c58 bytes f44fbea9
- 00b53c5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53c5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53c5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53c5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53c5c bytes fd7b01a9
- 00b53c74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53c74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53c74 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f4eba9592d74a1637afd847220a7e1"></a>

### [`00b53d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d04.md) → [`00b53dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53dcc.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b53d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53df8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53de0",
      "incomplete_value": true,
      "site": "00b53de0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d18",
      "incomplete_value": true,
      "site": "00b53d18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b53ddc",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53d24",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53d28",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b53ddc",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53dec",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53df0",
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

- 旧版 [`00b53d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d04.md#insn-00b53d18) · [`00b53d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d04.md#insn-00b53d28) · [`00b53d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d04.md#insn-00b53d30)
- 新版 `00b53de0`（命令位置の公開資料なし）

~~~diff
- 00b53d18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53d18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b53de0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b53de0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53d18 bytes e80000b5
+ 00b53de0 bytes e80000b5
- 00b53d28 ["INT_ADD", "register:40f0:8", ["const:b53d28:8", "const:4:8"]]
- 00b53d28 ["CALL", null, ["callee:00bde040:8"]]
- 00b53d28 bytes 9a280294
- 00b53d30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53d30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53d30 bytes 601a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d423d1b260eb07602655ed43bad81bd6"></a>

### [`00b53d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d44.md) → [`00b53e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e0c.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

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
      "definition_site": "00b53e38",
      "incomplete_value": true,
      "site": "00b53e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d70",
      "incomplete_value": true,
      "site": "00b53d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "definition_site": "00b53e20",
      "incomplete_value": true,
      "site": "00b53e20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d58",
      "incomplete_value": true,
      "site": "00b53d58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53e28",
      "incomplete_value": false,
      "site": "00b53e30",
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
            "const:eb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d60",
      "incomplete_value": false,
      "site": "00b53d68",
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
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53e1c",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e28",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ],
    [
      "00b53e38",
      "WRITE",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53e1c",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e28",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53e38",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d44.md#insn-00b53d68) · [`00b53d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d44.md#insn-00b53d70) · [`00b53d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d44.md#insn-00b53d54)
- 新版 `00b53e30`（命令位置の公開資料なし） · `00b53e38`（命令位置の公開資料なし） · `00b53e1c`（命令位置の公開資料なし）

~~~diff
- 00b53d68 ["INT_ADD", "register:40f0:8", ["const:b53d68:8", "const:4:8"]]
- 00b53d68 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53e30 ["INT_ADD", "register:40f0:8", ["const:b53e30:8", "const:4:8"]]
+ 00b53e30 ["CALL", null, ["callee:00bde040:8"]]
- 00b53d68 bytes 8a280294
+ 00b53e30 bytes 84280294
- 00b53d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
+ 00b53e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53d70 bytes 601a01f9
+ 00b53e38 bytes 607a01f9
- 00b53d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53d54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53e1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
+ 00b53e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53d54 bytes 681a41f9
+ 00b53e1c bytes 687a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cee8a3d94f9820f54d898da03312588f"></a>

### [`00b53d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d84.md) → [`00b53e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e4c.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b53db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53e7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53e60",
      "incomplete_value": true,
      "site": "00b53e60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d98",
      "incomplete_value": true,
      "site": "00b53d98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b53e5c",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53da4",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53dac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b53e5c",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e6c",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53e74",
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

- 旧版 [`00b53d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d84.md#insn-00b53d98) · [`00b53dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d84.md#insn-00b53dac) · [`00b53db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53d84.md#insn-00b53db4)
- 新版 `00b53e60`（命令位置の公開資料なし）

~~~diff
- 00b53d98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53d98 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b53e60 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b53e60 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53d98 bytes 080100b5
+ 00b53e60 bytes 080100b5
- 00b53dac ["INT_ADD", "register:40f0:8", ["const:b53dac:8", "const:4:8"]]
- 00b53dac ["CALL", null, ["callee:00bde040:8"]]
- 00b53dac bytes 79280294
- 00b53db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53db4 bytes 601a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05f8efa312d9c3ab5c80e3a7366661c8"></a>

### [`00b53dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53dc8.md) → [`00b53e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e90.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53ec0",
      "incomplete_value": true,
      "site": "00b53ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53df8",
      "incomplete_value": true,
      "site": "00b53df8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "definition_site": "00b53ea4",
      "incomplete_value": true,
      "site": "00b53ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ddc",
      "incomplete_value": true,
      "site": "00b53ddc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53eac",
      "incomplete_value": false,
      "site": "00b53eb8",
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
            "const:eb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53de4",
      "incomplete_value": false,
      "site": "00b53df0",
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
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53ea0",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53eac",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ],
    [
      "00b53ec0",
      "WRITE",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ea0",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53eac",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53ec0",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53dc8.md#insn-00b53df0) · [`00b53df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53dc8.md#insn-00b53df8) · [`00b53dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53dc8.md#insn-00b53dd8)
- 新版 `00b53eb8`（命令位置の公開資料なし） · `00b53ec0`（命令位置の公開資料なし） · `00b53ea0`（命令位置の公開資料なし）

~~~diff
- 00b53df0 ["INT_ADD", "register:40f0:8", ["const:b53df0:8", "const:4:8"]]
- 00b53df0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53eb8 ["INT_ADD", "register:40f0:8", ["const:b53eb8:8", "const:4:8"]]
+ 00b53eb8 ["CALL", null, ["callee:00bde040:8"]]
- 00b53df0 bytes 68280294
+ 00b53eb8 bytes 62280294
- 00b53df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
+ 00b53ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53df8 bytes 601a01f9
+ 00b53ec0 bytes 607a01f9
- 00b53dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:230:8"]]
- 00b53dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
+ 00b53ea0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53dd8 bytes 681a41f9
+ 00b53ea0 bytes 687a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e3e1740b37f4270edb51f9f35ebfd6"></a>

### [`00b53e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e18.md) → [`00b53ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ee0.md) _ZN8firebase13remote_config8internal19throttled_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b53f38",
      "incomplete_value": true,
      "site": "00b53f38",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e70",
      "incomplete_value": true,
      "site": "00b53e70",
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
            "const:238:8"
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
      "definition_site": "00b53f14",
      "incomplete_value": true,
      "site": "00b53f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e4c",
      "incomplete_value": true,
      "site": "00b53e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
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
      "00b53ef4",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53f14",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f38",
      "WRITE",
      [
        "storage",
        "010a1238",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53ef4",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53f14",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f38",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e18.md#insn-00b53e58) · [`00b53e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e18.md#insn-00b53e70) · [`00b53e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e18.md#insn-00b53e2c)
- 新版 `00b53f20`（命令位置の公開資料なし） · `00b53f38`（命令位置の公開資料なし） · `00b53ef4`（命令位置の公開資料なし）

~~~diff
- 00b53e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53e58 ["INT_ADD", "register:40f0:8", ["const:b53e58:8", "const:4:8"]]
- 00b53e58 ["CALLIND", null, ["register:0:8"]]
+ 00b53f20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53f20 ["INT_ADD", "register:40f0:8", ["const:b53f20:8", "const:4:8"]]
+ 00b53f20 ["CALLIND", null, ["register:0:8"]]
- 00b53e58 bytes 00013fd6
+ 00b53f20 bytes 00013fd6
- 00b53e70 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53e70 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:238:8"]]
- 00b53e70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53f38 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53f38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2f8:8"]]
+ 00b53f38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53e70 bytes a0e20839
+ 00b53f38 bytes a0e20b39
- 00b53e2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:238:8"]]
- 00b53e2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53e2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53ef4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2f8:8"]]
+ 00b53ef4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ef4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53e2c bytes a8e24839
+ 00b53ef4 bytes a8e24b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0436f8af8dc2fd7691b5c0dff8668f73"></a>

### [`00b53e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e84.md) → [`00b53f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53f4c.md) _ZN8firebase13remote_config8internal19throttled_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53f88",
      "incomplete_value": true,
      "site": "00b53f88",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ec0",
      "incomplete_value": true,
      "site": "00b53ec0",
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
            "const:238:8"
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
      "definition_site": "00b53fa8",
      "incomplete_value": true,
      "site": "00b53fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ee0",
      "incomplete_value": true,
      "site": "00b53ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53e9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53e98",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53e9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53fac"
      ]
    ],
    [
      "00b53f6c",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53f60",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53fac"
      ]
    ],
    [
      "00b53f6c",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e84.md#insn-00b53e9c) · [`00b53ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e84.md#insn-00b53ec0) · [`00b53edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53e84.md#insn-00b53edc)
- 新版 `00b53f88`（命令位置の公開資料なし） · `00b53fa4`（命令位置の公開資料なし）

~~~diff
- 00b53e9c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53e9c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b53e9c bytes 410200b4
- 00b53ec0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53ec0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53ec0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:238:8"]]
- 00b53ec0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b53f88 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b53f88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b53f88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2f8:8"]]
+ 00b53f88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53ec0 bytes bfe20839
+ 00b53f88 bytes bfe20b39
- 00b53edc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53edc ["INT_ADD", "register:40f0:8", ["const:b53edc:8", "const:4:8"]]
- 00b53edc ["CALLIND", null, ["register:0:8"]]
+ 00b53fa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53fa4 ["INT_ADD", "register:40f0:8", ["const:b53fa4:8", "const:4:8"]]
+ 00b53fa4 ["CALLIND", null, ["register:0:8"]]
- 00b53edc bytes 00013fd6
+ 00b53fa4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9035d57ce9db519e61b343c854799e0b"></a>

### [`00b53ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ef4.md) → [`00b53fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53fbc.md) _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b53f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53ffc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53f08",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53f10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54000"
      ]
    ],
    [
      "unmatched:00b53f18",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b53fd0",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54000"
      ]
    ],
    [
      "00b53fe0",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ef4.md#insn-00b53f10) · [`00b53f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ef4.md#insn-00b53f2c) · [`00b53f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53ef4.md#insn-00b53f34)
- 新版 `00b53ff4`（命令位置の公開資料なし）

~~~diff
- 00b53f10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53f10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53f10 bytes 410100b5
- 00b53f2c ["INT_ADD", "register:40f0:8", ["const:b53f2c:8", "const:4:8"]]
- 00b53f2c ["CALL", null, ["callee:00bde040:8"]]
+ 00b53ff4 ["INT_ADD", "register:40f0:8", ["const:b53ff4:8", "const:4:8"]]
+ 00b53ff4 ["CALL", null, ["callee:00bde040:8"]]
- 00b53f2c bytes 19280294
+ 00b53ff4 bytes 13280294
- 00b53f34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:230:8"]]
- 00b53f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53f34 bytes 801a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7203bcb3dd870f362f054b86017c2d1"></a>

### [`00b53fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53fa0.md) → [`00b54068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54068.md) _ZN8firebase13remote_config8internal19throttled_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b53fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b540a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53fb4",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b540ac"
      ]
    ],
    [
      "unmatched:00b53fc4",
      "PARAM",
      [
        "storage",
        "002a8f4b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5407c",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b540ac"
      ]
    ],
    [
      "00b5408c",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53fa0.md#insn-00b53fbc) · [`00b53fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53fa0.md#insn-00b53fd8) · [`00b53fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53fa0.md#insn-00b53fe0)
- 新版 `00b540a0`（命令位置の公開資料なし）

~~~diff
- 00b53fbc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53fbc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53fbc bytes 410100b5
- 00b53fd8 ["INT_ADD", "register:40f0:8", ["const:b53fd8:8", "const:4:8"]]
- 00b53fd8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b540a0 ["INT_ADD", "register:40f0:8", ["const:b540a0:8", "const:4:8"]]
+ 00b540a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b53fd8 bytes ee270294
+ 00b540a0 bytes e8270294
- 00b53fe0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:230:8"]]
- 00b53fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53fe0 bytes 801a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b64a9908c29a8e03c8fef4524a8095"></a>

### [`00b5408c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5408c.md) → [`00b54154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54154.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

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
      "definition_site": "00b54180",
      "incomplete_value": true,
      "site": "00b54180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b540b8",
      "incomplete_value": true,
      "site": "00b540b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "00b54168",
      "incomplete_value": true,
      "site": "00b54168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b540a0",
      "incomplete_value": true,
      "site": "00b540a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54170",
      "incomplete_value": false,
      "site": "00b54178",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b540a8",
      "incomplete_value": false,
      "site": "00b540b0",
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
      "00b54164",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54170",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ],
    [
      "00b54180",
      "WRITE",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54164",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54170",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54180",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b540b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5408c.md#insn-00b540b0) · [`00b540b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5408c.md#insn-00b540b8) · [`00b5409c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5408c.md#insn-00b5409c)
- 新版 `00b54178`（命令位置の公開資料なし） · `00b54180`（命令位置の公開資料なし） · `00b54164`（命令位置の公開資料なし）

~~~diff
- 00b540b0 ["INT_ADD", "register:40f0:8", ["const:b540b0:8", "const:4:8"]]
- 00b540b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54178 ["INT_ADD", "register:40f0:8", ["const:b54178:8", "const:4:8"]]
+ 00b54178 ["CALL", null, ["callee:00bde040:8"]]
- 00b540b0 bytes b8270294
+ 00b54178 bytes b2270294
- 00b540b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b540b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
+ 00b54180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b540b8 bytes 602a01f9
+ 00b54180 bytes 608a01f9
- 00b5409c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b5409c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
+ 00b54164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5409c bytes 682a41f9
+ 00b54164 bytes 688a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae0a47e533ef39e6dca157b23c423fc"></a>

### [`00b54110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54110.md) → [`00b541d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b541d8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54208",
      "incomplete_value": true,
      "site": "00b54208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54140",
      "incomplete_value": true,
      "site": "00b54140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "00b541ec",
      "incomplete_value": true,
      "site": "00b541ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54124",
      "incomplete_value": true,
      "site": "00b54124",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b541f4",
      "incomplete_value": false,
      "site": "00b54200",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5412c",
      "incomplete_value": false,
      "site": "00b54138",
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
      "00b541e8",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541f4",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ],
    [
      "00b54208",
      "WRITE",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b541e8",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541f4",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54208",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54110.md#insn-00b54138) · [`00b54140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54110.md#insn-00b54140) · [`00b54120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54110.md#insn-00b54120)
- 新版 `00b54200`（命令位置の公開資料なし） · `00b54208`（命令位置の公開資料なし） · `00b541e8`（命令位置の公開資料なし）

~~~diff
- 00b54138 ["INT_ADD", "register:40f0:8", ["const:b54138:8", "const:4:8"]]
- 00b54138 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54200 ["INT_ADD", "register:40f0:8", ["const:b54200:8", "const:4:8"]]
+ 00b54200 ["CALL", null, ["callee:00bde040:8"]]
- 00b54138 bytes 96270294
+ 00b54200 bytes 90270294
- 00b54140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b54140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
+ 00b54208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54140 bytes 602a01f9
+ 00b54208 bytes 608a01f9
- 00b54120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b54120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b541e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
+ 00b541e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54120 bytes 682a41f9
+ 00b541e8 bytes 688a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a74d797b0c4eb44602c2c7b737f673"></a>

### [`00b541cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b541cc.md) → [`00b54294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54294.md) _ZN8firebase13remote_config8internal26jni_config_update_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b542d0"
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
      "00b542a8",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542b4",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined1"
      ]
    ],
    [
      "00b542bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5420c"
      ]
    ]
  ],
  "added": [
    [
      "00b542a8",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542b4",
      "READ",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ],
    [
      "00b542bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b542d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b541e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b541cc.md#insn-00b541e4) · [`00b54204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b541cc.md#insn-00b54204) · [`00b54208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b541cc.md#insn-00b54208)
- 新版 `00b542ac`（命令位置の公開資料なし）

~~~diff
- 00b541e4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b541e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b542ac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b542ac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b541e4 bytes 410200b4
+ 00b542ac bytes 410200b4
- 00b54204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54204 ["INT_ADD", "register:40f0:8", ["const:b54204:8", "const:4:8"]]
- 00b54204 ["CALLIND", null, ["register:0:8"]]
- 00b54204 bytes 00013fd6
- 00b54208 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54208 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54208 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:258:8"]]
- 00b54208 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54208 bytes bf620939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ccc3714b4f5b64649fcacc434a59d7"></a>

### [`00b5423c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5423c.md) → [`00b54304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54304.md) _ZN8firebase13remote_config8internal26jni_config_update_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54344",
      "incomplete_value": true,
      "site": "00b54344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5427c",
      "incomplete_value": true,
      "site": "00b5427c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "00b54320",
      "incomplete_value": true,
      "site": "00b54320",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54258",
      "incomplete_value": true,
      "site": "00b54258",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54328",
      "incomplete_value": false,
      "site": "00b5433c",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54260",
      "incomplete_value": false,
      "site": "00b54274",
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
      "00b54318",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54328",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ],
    [
      "00b54344",
      "WRITE",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54318",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54328",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54344",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5423c.md#insn-00b54274) · [`00b5427c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5423c.md#insn-00b5427c) · [`00b54250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5423c.md#insn-00b54250)
- 新版 `00b5433c`（命令位置の公開資料なし） · `00b54344`（命令位置の公開資料なし） · `00b54318`（命令位置の公開資料なし）

~~~diff
- 00b54274 ["INT_ADD", "register:40f0:8", ["const:b54274:8", "const:4:8"]]
- 00b54274 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5433c ["INT_ADD", "register:40f0:8", ["const:b5433c:8", "const:4:8"]]
+ 00b5433c ["CALL", null, ["callee:00bde040:8"]]
- 00b54274 bytes 47270294
+ 00b5433c bytes 41270294
- 00b5427c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b5427c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
+ 00b54344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5427c bytes 802a01f9
+ 00b54344 bytes 808a01f9
- 00b54250 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b54250 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
+ 00b54318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54250 bytes 812a41f9
+ 00b54318 bytes 818a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c4720b73489a587aef4cd32aaccc68"></a>

### [`00b542e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542e8.md) → [`00b543b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b543b0.md) _ZN8firebase13remote_config8internal26jni_config_update_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b54328"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b543f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54304"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b542fc",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b543f4"
      ]
    ],
    [
      "unmatched:00b5430c",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b543c4",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b543cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b543f4"
      ]
    ],
    [
      "00b543d4",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542e8.md#insn-00b54304) · [`00b54320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542e8.md#insn-00b54320) · [`00b54328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542e8.md#insn-00b54328)
- 新版 `00b543e8`（命令位置の公開資料なし）

~~~diff
- 00b54304 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b54304 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b54304 bytes 410100b5
- 00b54320 ["INT_ADD", "register:40f0:8", ["const:b54320:8", "const:4:8"]]
- 00b54320 ["CALL", null, ["callee:00bde040:8"]]
+ 00b543e8 ["INT_ADD", "register:40f0:8", ["const:b543e8:8", "const:4:8"]]
+ 00b543e8 ["CALL", null, ["callee:00bde040:8"]]
- 00b54320 bytes 1c270294
+ 00b543e8 bytes 16270294
- 00b54328 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 00b54328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54328 bytes 802a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db83bade52ed02a045e41ba3b6ce85ec"></a>

### [`00b54358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54358.md) → [`00b54420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54420.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b5443c",
      "incomplete_value": false,
      "site": "00b54440",
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
      "definition_site": "00b54374",
      "incomplete_value": false,
      "site": "00b54378",
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
      "definition_site": "00b5444c",
      "incomplete_value": true,
      "site": "00b54458",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54384",
      "incomplete_value": true,
      "site": "00b54390",
      "value": [
        "LOAD",
        "8",
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
      "00b5443c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5444c",
      "DATA",
      [
        "storage",
        "010a1268",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5443c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5444c",
      "DATA",
      [
        "storage",
        "010a1328",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54358.md#insn-00b54378) · [`00b54374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54358.md#insn-00b54374) · [`00b54380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54358.md#insn-00b54380)
- 新版 `00b54440`（命令位置の公開資料なし） · `00b5443c`（命令位置の公開資料なし） · `00b54448`（命令位置の公開資料なし）

~~~diff
- 00b54378 ["INT_ADD", "register:40f0:8", ["const:b54378:8", "const:4:8"]]
- 00b54378 ["CALL", null, ["callee:00bde130:8"]]
+ 00b54440 ["INT_ADD", "register:40f0:8", ["const:b54440:8", "const:4:8"]]
+ 00b54440 ["CALL", null, ["callee:00bde130:8"]]
- 00b54378 bytes 42270294
+ 00b54440 bytes 3c270294
- 00b54374 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b54374 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54374 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54374 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5443c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5443c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5443c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5443c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54374 bytes 00c81791
+ 00b5443c bytes 00fc1991
- 00b54380 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00b54380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54448 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00b54448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54380 bytes 08a10991
+ 00b54448 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71bf135cf5a81624ffda825c5657196a"></a>

### [`00b543d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b543d4.md) → [`00b5449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5449c.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b54400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b544c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b544b0",
      "incomplete_value": true,
      "site": "00b544b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b543e8",
      "incomplete_value": true,
      "site": "00b543e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b544ac",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b543f0",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b543f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b544ac",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b544b8",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ],
    [
      "00b544c0",
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

- 旧版 [`00b543e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b543d4.md#insn-00b543e8) · [`00b543f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b543d4.md#insn-00b543f8) · [`00b54400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b543d4.md#insn-00b54400)
- 新版 `00b544b0`（命令位置の公開資料なし）

~~~diff
- 00b543e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b543e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b544b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b544b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b543e8 bytes e80000b5
+ 00b544b0 bytes e80000b5
- 00b543f8 ["INT_ADD", "register:40f0:8", ["const:b543f8:8", "const:4:8"]]
- 00b543f8 ["CALL", null, ["callee:00bde040:8"]]
- 00b543f8 bytes e6260294
- 00b54400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:270:8"]]
- 00b54400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54400 bytes 603a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1a7aee3417fdb465d3c6746a0d61cf"></a>

### [`00b54414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54414.md) → [`00b544dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b544dc.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b5450c",
      "incomplete_value": true,
      "site": "00b5450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54444",
      "incomplete_value": true,
      "site": "00b54444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "definition_site": "00b544f0",
      "incomplete_value": true,
      "site": "00b544f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54428",
      "incomplete_value": true,
      "site": "00b54428",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b544fc",
      "incomplete_value": false,
      "site": "00b54504",
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
            "const:179:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54434",
      "incomplete_value": false,
      "site": "00b5443c",
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
            "const:173:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b544ec",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00b544fc",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ],
    [
      "00b5450c",
      "WRITE",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b544ec",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b544fc",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ],
    [
      "00b5450c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5443c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54414.md#insn-00b5443c) · [`00b54444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54414.md#insn-00b54444) · [`00b54424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54414.md#insn-00b54424)
- 新版 `00b54504`（命令位置の公開資料なし） · `00b5450c`（命令位置の公開資料なし） · `00b544ec`（命令位置の公開資料なし）

~~~diff
- 00b5443c ["INT_ADD", "register:40f0:8", ["const:b5443c:8", "const:4:8"]]
- 00b5443c ["CALL", null, ["callee:00bde040:8"]]
+ 00b54504 ["INT_ADD", "register:40f0:8", ["const:b54504:8", "const:4:8"]]
+ 00b54504 ["CALL", null, ["callee:00bde040:8"]]
- 00b5443c bytes d5260294
+ 00b54504 bytes cf260294
- 00b54444 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:270:8"]]
- 00b54444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5450c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b5450c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54444 bytes 603a01f9
+ 00b5450c bytes 609a01f9
- 00b54424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:270:8"]]
- 00b54424 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b544ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b544ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54424 bytes 683a41f9
+ 00b544ec bytes 689a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3ffdb82ca260c400909495ea817b46"></a>

### [`00b54458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54458.md) → [`00b54520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54520.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b54488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54550"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5446c",
      "incomplete_value": true,
      "site": "00b5446c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b54530",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54474",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b54488",
      "WRITE",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54530",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5453c",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ],
    [
      "00b54550",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5446c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54458.md#insn-00b5446c) · [`00b54480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54458.md#insn-00b54480) · [`00b54488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54458.md#insn-00b54488)
- 新版 `00b54534`（命令位置の公開資料なし） · `00b54548`（命令位置の公開資料なし）

~~~diff
- 00b5446c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5446c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b54534 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b54534 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5446c bytes 080100b5
+ 00b54534 bytes 080100b5
- 00b54480 ["INT_ADD", "register:40f0:8", ["const:b54480:8", "const:4:8"]]
- 00b54480 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54548 ["INT_ADD", "register:40f0:8", ["const:b54548:8", "const:4:8"]]
+ 00b54548 ["CALL", null, ["callee:00bde040:8"]]
- 00b54480 bytes c4260294
+ 00b54548 bytes be260294
- 00b54488 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:270:8"]]
- 00b54488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54488 bytes 603a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4325ec95e283c01326c0a39be4bf15e"></a>

### [`00b544a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b544a8.md) → [`00b54570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54570.md) _ZN8firebase13remote_config8internal13config_update15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b545c8",
      "incomplete_value": true,
      "site": "00b545c8",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54500",
      "incomplete_value": true,
      "site": "00b54500",
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
            "const:278:8"
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
      "definition_site": "00b545a4",
      "incomplete_value": true,
      "site": "00b545b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544dc",
      "incomplete_value": true,
      "site": "00b544e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
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
      "00b54584",
      "READ",
      [
        "storage",
        "010a1278",
        null,
        "undefined1"
      ]
    ],
    [
      "00b545a4",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00b545c8",
      "WRITE",
      [
        "storage",
        "010a1278",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b54584",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b545a4",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b545c8",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b544e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b544a8.md#insn-00b544e8) · [`00b54500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b544a8.md#insn-00b54500) · [`00b544bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b544a8.md#insn-00b544bc)
- 新版 `00b545b0`（命令位置の公開資料なし） · `00b545c8`（命令位置の公開資料なし） · `00b54584`（命令位置の公開資料なし）

~~~diff
- 00b544e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b544e8 ["INT_ADD", "register:40f0:8", ["const:b544e8:8", "const:4:8"]]
- 00b544e8 ["CALLIND", null, ["register:0:8"]]
+ 00b545b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b545b0 ["INT_ADD", "register:40f0:8", ["const:b545b0:8", "const:4:8"]]
+ 00b545b0 ["CALLIND", null, ["register:0:8"]]
- 00b544e8 bytes 00013fd6
+ 00b545b0 bytes 00013fd6
- 00b54500 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b54500 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:278:8"]]
- 00b54500 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b545c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b545c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:338:8"]]
+ 00b545c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b54500 bytes a0e20939
+ 00b545c8 bytes a0e20c39
- 00b544bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:278:8"]]
- 00b544bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b544bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b54584 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
+ 00b54584 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b54584 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b544bc bytes a8e24939
+ 00b54584 bytes a8e24c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e445f4856cf7d1106835c072a789f3"></a>

### [`00b54514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54514.md) → [`00b545dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b545dc.md) _ZN8firebase13remote_config8internal13config_update12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b54618",
      "incomplete_value": true,
      "site": "00b54618",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54550",
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
            "const:278:8"
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
      "definition_site": "00b54638",
      "incomplete_value": true,
      "site": "00b54638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54570",
      "incomplete_value": true,
      "site": "00b54570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "definition_site": "00b545f4",
      "incomplete_value": true,
      "site": "00b545f4",
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
      "definition_site": "00b5452c",
      "incomplete_value": true,
      "site": "00b5452c",
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
      "00b545f0",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00b545fc",
      "READ",
      [
        "storage",
        "010a1278",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54618",
      "WRITE",
      [
        "storage",
        "010a1278",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b545f0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b545fc",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54618",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54514.md#insn-00b54550) · [`00b5456c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54514.md#insn-00b5456c) · [`00b54570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54514.md#insn-00b54570)
- 新版 `00b54618`（命令位置の公開資料なし） · `00b54634`（命令位置の公開資料なし） · `00b54638`（命令位置の公開資料なし）

~~~diff
- 00b54550 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54550 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54550 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:278:8"]]
- 00b54550 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b54618 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b54618 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b54618 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:338:8"]]
+ 00b54618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54550 bytes bfe20939
+ 00b54618 bytes bfe20c39
- 00b5456c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5456c ["INT_ADD", "register:40f0:8", ["const:b5456c:8", "const:4:8"]]
- 00b5456c ["CALLIND", null, ["register:0:8"]]
+ 00b54634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54634 ["INT_ADD", "register:40f0:8", ["const:b54634:8", "const:4:8"]]
+ 00b54634 ["CALLIND", null, ["register:0:8"]]
- 00b5456c bytes 00013fd6
+ 00b54634 bytes 00013fd6
- 00b54570 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:270:8"]]
- 00b54570 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b54570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b54638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b54638 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b54638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b54570 bytes 9f3a01f9
+ 00b54638 bytes 9f9a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c3fb9ce7e2df4557ef006d404534a7"></a>

### [`00b54584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54584.md) → [`00b5464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5464c.md) _ZN8firebase13remote_config8internal13config_update14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b545c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5468c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54598",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b545a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54690"
      ]
    ],
    [
      "unmatched:00b545a8",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b54660",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54690"
      ]
    ],
    [
      "00b54670",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b545a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54584.md#insn-00b545a0) · [`00b545bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54584.md#insn-00b545bc) · [`00b545c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54584.md#insn-00b545c4)
- 新版 `00b54684`（命令位置の公開資料なし）

~~~diff
- 00b545a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b545a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b545a0 bytes 410100b5
- 00b545bc ["INT_ADD", "register:40f0:8", ["const:b545bc:8", "const:4:8"]]
- 00b545bc ["CALL", null, ["callee:00bde040:8"]]
+ 00b54684 ["INT_ADD", "register:40f0:8", ["const:b54684:8", "const:4:8"]]
+ 00b54684 ["CALL", null, ["callee:00bde040:8"]]
- 00b545bc bytes 75260294
+ 00b54684 bytes 6f260294
- 00b545c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:270:8"]]
- 00b545c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b545c4 bytes 803a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5179b73c96357f539baba0014190339"></a>

### [`00b545f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b545f4.md) → [`00b546bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546bc.md) _ZN8firebase13remote_config8internal13config_update11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b546d8",
      "incomplete_value": false,
      "site": "00b546dc",
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
      "definition_site": "00b54610",
      "incomplete_value": false,
      "site": "00b54614",
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
      "definition_site": "00b546e8",
      "incomplete_value": true,
      "site": "00b546f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54620",
      "incomplete_value": true,
      "site": "00b5462c",
      "value": [
        "LOAD",
        "8",
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
      "00b546d8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b546e8",
      "DATA",
      [
        "storage",
        "010a1280",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b546d8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b546e8",
      "DATA",
      [
        "storage",
        "010a1340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b545f4.md#insn-00b54614) · [`00b54610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b545f4.md#insn-00b54610) · [`00b5461c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b545f4.md#insn-00b5461c)
- 新版 `00b546dc`（命令位置の公開資料なし） · `00b546d8`（命令位置の公開資料なし） · `00b546e4`（命令位置の公開資料なし）

~~~diff
- 00b54614 ["INT_ADD", "register:40f0:8", ["const:b54614:8", "const:4:8"]]
- 00b54614 ["CALL", null, ["callee:00bde130:8"]]
+ 00b546dc ["INT_ADD", "register:40f0:8", ["const:b546dc:8", "const:4:8"]]
+ 00b546dc ["CALL", null, ["callee:00bde130:8"]]
- 00b54614 bytes 9b260294
+ 00b546dc bytes 95260294
- 00b54610 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b54610 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54610 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54610 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b546d8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b546d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b546d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b546d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54610 bytes 001c1591
+ 00b546d8 bytes 00501791
- 00b5461c ["COPY", "tmp:0:8", ["const:280:8"]]
- 00b5461c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5461c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5461c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b546e4 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00b546e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b546e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b546e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5461c bytes 08010a91
+ 00b546e4 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe24105c61f54473f1d7c413b690c09f"></a>

### [`00b54630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54630.md) → [`00b546f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546f8.md) _ZN8firebase13remote_config8internal13config_update13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b54670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54738"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5464c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54644",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5464c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5473c"
      ]
    ],
    [
      "unmatched:00b54654",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5470c",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5473c"
      ]
    ],
    [
      "00b5471c",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5464c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54630.md#insn-00b5464c) · [`00b54668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54630.md#insn-00b54668) · [`00b54670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54630.md#insn-00b54670)
- 新版 `00b54730`（命令位置の公開資料なし）

~~~diff
- 00b5464c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5464c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5464c bytes 410100b5
- 00b54668 ["INT_ADD", "register:40f0:8", ["const:b54668:8", "const:4:8"]]
- 00b54668 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54730 ["INT_ADD", "register:40f0:8", ["const:b54730:8", "const:4:8"]]
+ 00b54730 ["CALL", null, ["callee:00bde040:8"]]
- 00b54668 bytes 4a260294
+ 00b54730 bytes 44260294
- 00b54670 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:270:8"]]
- 00b54670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54670 bytes 803a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d934c836b4c50bb493407274fd535d07"></a>

### [`00b546a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546a0.md) → [`00b54768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54768.md) _ZN8firebase13remote_config8internal13config_update10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b54784",
      "incomplete_value": false,
      "site": "00b54788",
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
      "definition_site": "00b546bc",
      "incomplete_value": false,
      "site": "00b546c0",
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
      "definition_site": "00b54794",
      "incomplete_value": true,
      "site": "00b547a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b546cc",
      "incomplete_value": true,
      "site": "00b546d8",
      "value": [
        "LOAD",
        "8",
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
      "00b54784",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b54794",
      "DATA",
      [
        "storage",
        "010a1288",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54784",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b54794",
      "DATA",
      [
        "storage",
        "010a1348",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b546c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546a0.md#insn-00b546c0) · [`00b546bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546a0.md#insn-00b546bc) · [`00b546c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546a0.md#insn-00b546c8)
- 新版 `00b54788`（命令位置の公開資料なし） · `00b54784`（命令位置の公開資料なし） · `00b54790`（命令位置の公開資料なし）

~~~diff
- 00b546c0 ["INT_ADD", "register:40f0:8", ["const:b546c0:8", "const:4:8"]]
- 00b546c0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b54788 ["INT_ADD", "register:40f0:8", ["const:b54788:8", "const:4:8"]]
+ 00b54788 ["CALL", null, ["callee:00bde130:8"]]
- 00b546c0 bytes 70260294
+ 00b54788 bytes 6a260294
- 00b546bc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b546bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b546bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b546bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54784 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b54784 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54784 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54784 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b546bc bytes 00c81791
+ 00b54784 bytes 00fc1991
- 00b546c8 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00b546c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b546c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b546c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54790 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00b54790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b546c8 bytes 08210a91
+ 00b54790 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b702bb1d17af92a1650aed85b7a640"></a>

### [`00b546dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546dc.md) → [`00b547a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547a4.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

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
      "definition_site": "00b547d0",
      "incomplete_value": true,
      "site": "00b547d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54708",
      "incomplete_value": true,
      "site": "00b54708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b547b8",
      "incomplete_value": true,
      "site": "00b547b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b546f0",
      "incomplete_value": true,
      "site": "00b546f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b547c4",
      "incomplete_value": false,
      "site": "00b547c8",
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
            "const:916:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b546fc",
      "incomplete_value": false,
      "site": "00b54700",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b547b4",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b547c4",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b547d0",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b547b4",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b547c4",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b547d0",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546dc.md#insn-00b54700) · [`00b54708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546dc.md#insn-00b54708) · [`00b546ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b546dc.md#insn-00b546ec)
- 新版 `00b547c8`（命令位置の公開資料なし） · `00b547d0`（命令位置の公開資料なし） · `00b547b4`（命令位置の公開資料なし）

~~~diff
- 00b54700 ["INT_ADD", "register:40f0:8", ["const:b54700:8", "const:4:8"]]
- 00b54700 ["CALL", null, ["callee:00bde040:8"]]
+ 00b547c8 ["INT_ADD", "register:40f0:8", ["const:b547c8:8", "const:4:8"]]
+ 00b547c8 ["CALL", null, ["callee:00bde040:8"]]
- 00b54700 bytes 24260294
+ 00b547c8 bytes 1e260294
- 00b54708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b54708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b547d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b547d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54708 bytes 604a01f9
+ 00b547d0 bytes 60aa01f9
- 00b546ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b546ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b547b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b547b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b546ec bytes 684a41f9
+ 00b547b4 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe8b7fa54a57f41977c9816d3385f8c"></a>

### [`00b5475c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5475c.md) → [`00b54824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54824.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00b5478c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54854"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b54838",
      "incomplete_value": true,
      "site": "00b54838",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54770",
      "incomplete_value": true,
      "site": "00b54770",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b54834",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5477c",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b54784",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b54834",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54844",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b5484c",
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

- 旧版 [`00b54770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5475c.md#insn-00b54770) · [`00b54784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5475c.md#insn-00b54784) · [`00b5478c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5475c.md#insn-00b5478c)
- 新版 `00b54838`（命令位置の公開資料なし）

~~~diff
- 00b54770 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b54770 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b54838 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b54838 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b54770 bytes 080100b5
+ 00b54838 bytes 080100b5
- 00b54784 ["INT_ADD", "register:40f0:8", ["const:b54784:8", "const:4:8"]]
- 00b54784 ["CALL", null, ["callee:00bde040:8"]]
- 00b54784 bytes 03260294
- 00b5478c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b5478c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5478c bytes 604a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146f48a3860bfe23f192d54feca10d2d"></a>

### [`00b547a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547a0.md) → [`00b54868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54868.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54898",
      "incomplete_value": true,
      "site": "00b54898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547d0",
      "incomplete_value": true,
      "site": "00b547d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b5487c",
      "incomplete_value": true,
      "site": "00b5487c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547b4",
      "incomplete_value": true,
      "site": "00b547b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54884",
      "incomplete_value": false,
      "site": "00b54890",
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
            "const:916:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547bc",
      "incomplete_value": false,
      "site": "00b547c8",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54878",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54884",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54898",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54878",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54884",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54898",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b547c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547a0.md#insn-00b547c8) · [`00b547d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547a0.md#insn-00b547d0) · [`00b547b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547a0.md#insn-00b547b0)
- 新版 `00b54890`（命令位置の公開資料なし） · `00b54898`（命令位置の公開資料なし） · `00b54878`（命令位置の公開資料なし）

~~~diff
- 00b547c8 ["INT_ADD", "register:40f0:8", ["const:b547c8:8", "const:4:8"]]
- 00b547c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54890 ["INT_ADD", "register:40f0:8", ["const:b54890:8", "const:4:8"]]
+ 00b54890 ["CALL", null, ["callee:00bde040:8"]]
- 00b547c8 bytes f2250294
+ 00b54890 bytes ec250294
- 00b547d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b547d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b54898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b547d0 bytes 604a01f9
+ 00b54898 bytes 60aa01f9
- 00b547b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b547b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b54878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b547b0 bytes 684a41f9
+ 00b54878 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2619ced88c0e537a266356fcbdcb86"></a>

### [`00b547f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547f0.md) → [`00b548b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b548b8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "site": "00b547f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b547f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b547f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b547f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b547f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b547f8",
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
      "00b548b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b548bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b548c0",
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

- 旧版 [`00b547f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547f0.md#insn-00b547f0) · [`00b547f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547f0.md#insn-00b547f4) · [`00b547f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b547f0.md#insn-00b547f8)

~~~diff
- 00b547f0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b547f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b547f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b547f0 bytes f50f1df8
- 00b547f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b547f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b547f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b547f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b547f4 bytes f44f01a9
- 00b547f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b547f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b547f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b547f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b547f8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe99ad093990e50b71a1eabc3a12480"></a>

### [`00b5485c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5485c.md) → [`00b54924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54924.md) _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b54960",
      "incomplete_value": true,
      "site": "00b54960",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54898",
      "incomplete_value": true,
      "site": "00b54898",
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
            "const:298:8"
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
      "definition_site": "00b54980",
      "incomplete_value": true,
      "site": "00b54980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548b8",
      "incomplete_value": true,
      "site": "00b548b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b5493c",
      "incomplete_value": true,
      "site": "00b5493c",
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
      "definition_site": "00b54874",
      "incomplete_value": true,
      "site": "00b54874",
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
      "00b54938",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54944",
      "READ",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54960",
      "WRITE",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b54938",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54944",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54960",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5485c.md#insn-00b54898) · [`00b548b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5485c.md#insn-00b548b4) · [`00b548b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5485c.md#insn-00b548b8)
- 新版 `00b54960`（命令位置の公開資料なし） · `00b5497c`（命令位置の公開資料なし） · `00b54980`（命令位置の公開資料なし）

~~~diff
- 00b54898 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54898 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54898 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:298:8"]]
- 00b54898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b54960 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b54960 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b54960 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
+ 00b54960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54898 bytes bf620a39
+ 00b54960 bytes bf620d39
- 00b548b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b548b4 ["INT_ADD", "register:40f0:8", ["const:b548b4:8", "const:4:8"]]
- 00b548b4 ["CALLIND", null, ["register:0:8"]]
+ 00b5497c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5497c ["INT_ADD", "register:40f0:8", ["const:b5497c:8", "const:4:8"]]
+ 00b5497c ["CALLIND", null, ["register:0:8"]]
- 00b548b4 bytes 00013fd6
+ 00b5497c bytes 00013fd6
- 00b548b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b548b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b548b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b54980 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54980 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b54980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b548b8 bytes 9f4a01f9
+ 00b54980 bytes 9faa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06add5c9e0a1587c2838b0a901138ee7"></a>

### [`00b548cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b548cc.md) → [`00b54994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54994.md) _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b549d4",
      "incomplete_value": true,
      "site": "00b549d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5490c",
      "incomplete_value": true,
      "site": "00b5490c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b549b0",
      "incomplete_value": true,
      "site": "00b549b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548e8",
      "incomplete_value": true,
      "site": "00b548e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b549b8",
      "incomplete_value": false,
      "site": "00b549cc",
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
            "const:916:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548f0",
      "incomplete_value": false,
      "site": "00b54904",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b549a8",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b549b8",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b549d4",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b549a8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b549b8",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b549d4",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b548cc.md#insn-00b54904) · [`00b5490c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b548cc.md#insn-00b5490c) · [`00b548e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b548cc.md#insn-00b548e0)
- 新版 `00b549cc`（命令位置の公開資料なし） · `00b549d4`（命令位置の公開資料なし） · `00b549a8`（命令位置の公開資料なし）

~~~diff
- 00b54904 ["INT_ADD", "register:40f0:8", ["const:b54904:8", "const:4:8"]]
- 00b54904 ["CALL", null, ["callee:00bde040:8"]]
+ 00b549cc ["INT_ADD", "register:40f0:8", ["const:b549cc:8", "const:4:8"]]
+ 00b549cc ["CALL", null, ["callee:00bde040:8"]]
- 00b54904 bytes a3250294
+ 00b549cc bytes 9d250294
- 00b5490c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b5490c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b549d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b549d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5490c bytes 804a01f9
+ 00b549d4 bytes 80aa01f9
- 00b548e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b548e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b549a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b549a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b548e0 bytes 814a41f9
+ 00b549a8 bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3738d5d2ab7eee77d8ba7495a879c0"></a>

### [`00b5493c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5493c.md) → [`00b54a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a04.md) _ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b54a20",
      "incomplete_value": false,
      "site": "00b54a24",
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
      "definition_site": "00b54958",
      "incomplete_value": false,
      "site": "00b5495c",
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
      "definition_site": "00b54a30",
      "incomplete_value": true,
      "site": "00b54a3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54968",
      "incomplete_value": true,
      "site": "00b54974",
      "value": [
        "LOAD",
        "8",
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
      "00b54a20",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b54a30",
      "DATA",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54a20",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b54a30",
      "DATA",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5493c.md#insn-00b5495c) · [`00b54958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5493c.md#insn-00b54958) · [`00b54964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5493c.md#insn-00b54964)
- 新版 `00b54a24`（命令位置の公開資料なし） · `00b54a20`（命令位置の公開資料なし） · `00b54a2c`（命令位置の公開資料なし）

~~~diff
- 00b5495c ["INT_ADD", "register:40f0:8", ["const:b5495c:8", "const:4:8"]]
- 00b5495c ["CALL", null, ["callee:00bde130:8"]]
+ 00b54a24 ["INT_ADD", "register:40f0:8", ["const:b54a24:8", "const:4:8"]]
+ 00b54a24 ["CALL", null, ["callee:00bde130:8"]]
- 00b5495c bytes c9250294
+ 00b54a24 bytes c3250294
- 00b54958 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b54958 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54958 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54958 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54a20 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b54a20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54a20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54a20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54958 bytes 001c1591
+ 00b54a20 bytes 00501791
- 00b54964 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00b54964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54a2c ["COPY", "tmp:0:8", ["const:360:8"]]
+ 00b54a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54964 bytes 08810a91
+ 00b54a2c bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f4ebefdff10365bcb62b84af61b420f"></a>

### [`00b54978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54978.md) → [`00b54a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a40.md) _ZN8firebase13remote_config8internal35config_update_listener_registration13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54a80",
      "incomplete_value": true,
      "site": "00b54a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b549b8",
      "incomplete_value": true,
      "site": "00b549b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b54a5c",
      "incomplete_value": true,
      "site": "00b54a5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54994",
      "incomplete_value": true,
      "site": "00b54994",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54a64",
      "incomplete_value": false,
      "site": "00b54a78",
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
            "const:916:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5499c",
      "incomplete_value": false,
      "site": "00b549b0",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54a54",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54a64",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54a80",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54a54",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54a64",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54a80",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b549b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54978.md#insn-00b549b0) · [`00b549b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54978.md#insn-00b549b8) · [`00b5498c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54978.md#insn-00b5498c)
- 新版 `00b54a78`（命令位置の公開資料なし） · `00b54a80`（命令位置の公開資料なし） · `00b54a54`（命令位置の公開資料なし）

~~~diff
- 00b549b0 ["INT_ADD", "register:40f0:8", ["const:b549b0:8", "const:4:8"]]
- 00b549b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b54a78 ["INT_ADD", "register:40f0:8", ["const:b54a78:8", "const:4:8"]]
+ 00b54a78 ["CALL", null, ["callee:00bde040:8"]]
- 00b549b0 bytes 78250294
+ 00b54a78 bytes 72250294
- 00b549b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b549b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54a80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54a80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b549b8 bytes 804a01f9
+ 00b54a80 bytes 80aa01f9
- 00b5498c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b5498c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54a54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54a54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5498c bytes 814a41f9
+ 00b54a54 bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d0698fe152acc0696c37caabc35d85"></a>

### [`00b549e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b549e8.md) → [`00b54ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54ab0.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b54acc",
      "incomplete_value": false,
      "site": "00b54ad0",
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
      "definition_site": "00b54a04",
      "incomplete_value": false,
      "site": "00b54a08",
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
      "definition_site": "00b54adc",
      "incomplete_value": true,
      "site": "00b54ae8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54a14",
      "incomplete_value": true,
      "site": "00b54a20",
      "value": [
        "LOAD",
        "8",
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
      "00b54acc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b54adc",
      "DATA",
      [
        "storage",
        "010a12a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54acc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b54adc",
      "DATA",
      [
        "storage",
        "010a1368",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b549e8.md#insn-00b54a08) · [`00b54a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b549e8.md#insn-00b54a04) · [`00b54a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b549e8.md#insn-00b54a10)
- 新版 `00b54ad0`（命令位置の公開資料なし） · `00b54acc`（命令位置の公開資料なし） · `00b54ad8`（命令位置の公開資料なし）

~~~diff
- 00b54a08 ["INT_ADD", "register:40f0:8", ["const:b54a08:8", "const:4:8"]]
- 00b54a08 ["CALL", null, ["callee:00bde130:8"]]
+ 00b54ad0 ["INT_ADD", "register:40f0:8", ["const:b54ad0:8", "const:4:8"]]
+ 00b54ad0 ["CALL", null, ["callee:00bde130:8"]]
- 00b54a08 bytes 9e250294
+ 00b54ad0 bytes 98250294
- 00b54a04 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b54a04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54acc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b54acc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54acc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54acc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54a04 bytes 00c81791
+ 00b54acc bytes 00fc1991
- 00b54a10 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00b54a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54ad8 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00b54ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54a10 bytes 08a10a91
+ 00b54ad8 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d91f7795b06a4f738378a155345c32"></a>

### [`00b54a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54a2c.md) → [`00b54af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54af4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0770.md) · 呼出先 22件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00be0820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0820.md) · 呼出先 22件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 51.21% / 新版 51.21%

CFGの説明率　旧版 31.94% / 新版 31.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 27件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 30件, `unresolved_store_alignment` 28件

アドレスに依存する影響 `branch_value` 4件, `call_argument_candidate` 5件, `store_condition` 2件, `store_destination` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54aac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54b5c",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b54ab4",
      "DATA",
      [
        "storage",
        "010a12b0",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "unmatched:00b54ab4",
      "DATA",
      [
        "storage",
        "010a12b4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54b5c",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b54b7c",
      "DATA",
      [
        "storage",
        "010a1370",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00b54b7c",
      "DATA",
      [
        "storage",
        "010a1374",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54a2c.md#insn-00b54aa8) · [`00b54aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54a2c.md#insn-00b54aac) · [`00b54ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54a2c.md#insn-00b54ab0)

~~~diff
- 00b54aa8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:30:8"]]
- 00b54aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54aa8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54aa8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b54aa8 bytes 408301ad
- 00b54aac ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:10:8"]]
- 00b54aac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54aac ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54aac ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b54aac bytes 408300ad
- 00b54ab0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b54ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54ab0 bytes 4003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3379996a8b60f1a142a4a5d7c154fd02"></a>

### [`00b55638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55638.md) → [`00b55700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55700.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0830.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00be08e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08e0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.90% / 新版 61.90%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5563c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5563c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55638",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5563c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55640",
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
      "00b55700",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55704",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55708",
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

- 旧版 [`00b55638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55638.md#insn-00b55638) · [`00b5563c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55638.md#insn-00b5563c) · [`00b55640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55638.md#insn-00b55640)

~~~diff
- 00b55638 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b55638 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b55638 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b55638 bytes f50f1df8
- 00b5563c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5563c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5563c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5563c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5563c bytes f44f01a9
- 00b55640 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55640 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55640 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8560a874703ce5c17bf667bcfc5ad88"></a>

### [`00b556a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b556a8.md) → [`00b55770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55770.md) FUN_00b55770

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 69.23% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b556bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b556a8.md#insn-00b556bc) · [`00b556cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b556a8.md#insn-00b556cc) · [`00b556d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b556a8.md#insn-00b556d8)
- 新版 `00b55784`（命令位置の公開資料なし） · `00b55794`（命令位置の公開資料なし） · `00b557a0`（命令位置の公開資料なし）

~~~diff
- 00b556bc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b556bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b55784 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b55784 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b556bc bytes 540200b4
+ 00b55784 bytes 540200b4
- 00b556cc ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 00b55794 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b556cc bytes 40020054
+ 00b55794 bytes 40020054
- 00b556d8 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b556d8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b556d8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b556d8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b557a0 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00b557a0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b557a0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b557a0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b556d8 bytes c9000037
+ 00b557a0 bytes c9000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869d166ff564304d56902f5b8e36a868"></a>

### [`00b5572c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5572c.md) → [`00b557f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b557f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0780.md) · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md) [`00bddcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcd0.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) [`00bddf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00be0830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0830.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 30.23% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5572c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5572c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5572c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55730",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55734",
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
      "00b557f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b557f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b557fc",
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

- 旧版 [`00b5572c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5572c.md#insn-00b5572c) · [`00b55730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5572c.md#insn-00b55730) · [`00b55734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5572c.md#insn-00b55734)

~~~diff
- 00b5572c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5572c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5572c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5572c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5572c bytes f657bda9
- 00b55730 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55730 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55730 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b55730 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55730 bytes f44f01a9
- 00b55734 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55734 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55734 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55734 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55734 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efeb90dab83398632953869c92356ce0"></a>

### [`00b5589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5589c.md) → [`00b55964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55964.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0700.md) · 呼出先 7件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde050.md)
- 新版 呼出元 1件 [`00be07b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07b0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 20.45% / 新版 20.45%

CFGの説明率　旧版 8.00% / 新版 7.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 26件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b558a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b558a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b558a8",
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
      "00b55968",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5596c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55970",
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

- 旧版 [`00b558a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5589c.md#insn-00b558a0) · [`00b558a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5589c.md#insn-00b558a4) · [`00b558a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b5589c.md#insn-00b558a8)

~~~diff
- 00b558a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b558a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b558a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b558a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b558a0 bytes f65702a9
- 00b558a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b558a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b558a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b558a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b558a4 bytes f44f03a9
- 00b558a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b558a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b558a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b558a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b558a8 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9484995c1145f5a649b50e57b2cc4a"></a>

### [`00b55c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md) → [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b563e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b563e8.md) · 呼出先 6件 [`00b55d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55d70.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00b564b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md) · 呼出先 6件 [`00b55e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.51% / 新版 84.51%

CFGの説明率　旧版 17.86% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55c48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55c48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55c6c",
      "WRITE",
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
      "00b55d0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b55d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55d34",
      "WRITE",
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

- 旧版 [`00b55c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md#insn-00b55c44) · [`00b55c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md#insn-00b55c48) · [`00b55c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md#insn-00b55c6c)

~~~diff
- 00b55c44 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b55c44 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b55c44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b55c44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55c44 bytes f85f05a9
- 00b55c48 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b55c48 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b55c48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b55c48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55c48 bytes f65706a9
- 00b55c6c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b55c6c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b55c6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b55c6c bytes a8831cf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a519cd2e39e44ff2ccc1dbe1db326d3"></a>

### [`00b55d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55d70.md) → [`00b55e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md) FUN_00b55e38

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b55c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md) [`00b59740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59740.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`0056c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c6c4.md) [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 2件 [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) [`00b59808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59808.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.39% / 新版 69.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55d70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55d74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55d78",
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
      "00b55e38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55e40",
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

- 旧版 [`00b55d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55d70.md#insn-00b55d70) · [`00b55d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55d70.md#insn-00b55d74) · [`00b55d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55d70.md#insn-00b55d78)

~~~diff
- 00b55d70 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b55d70 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b55d70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b55d70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b55d70 bytes f657bda9
- 00b55d74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55d74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55d74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b55d74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55d74 bytes f44f01a9
- 00b55d78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55d78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55d78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55d78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55d78 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a72e6962201968adac2b06349fc5aacb"></a>

### [`00b55f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55f64.md) → [`00b5602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b57ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57ffc.md) [`00be07c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07c0.md) · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md)
- 新版 呼出元 2件 [`00b580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md) [`00be0870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0870.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.13% / 新版 72.13%

CFGの説明率　旧版 38.10% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55f70",
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
      "00b56030",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b56034",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56038",
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

- 旧版 [`00b55f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55f64.md#insn-00b55f68) · [`00b55f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55f64.md#insn-00b55f6c) · [`00b55f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55f64.md#insn-00b55f70)

~~~diff
- 00b55f68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b55f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b55f68 bytes f71300f9
- 00b55f6c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b55f6c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b55f6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b55f6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55f6c bytes f65703a9
- 00b55f70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55f70 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55f70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b55f70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55f70 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044dffcb4747962b587cd3325abe9564"></a>

### [`00b563e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b563e8.md) → [`00b564b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17EnsureInitializedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0650.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b55c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55c40.md) [`00b5a1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a1e0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be0700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0700.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) [`00b5a2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a2a8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b564f4",
      "incomplete_value": true,
      "site": "00b56508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5642c",
      "incomplete_value": true,
      "site": "00b56440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56530",
      "incomplete_value": true,
      "site": "00b56538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56468",
      "incomplete_value": true,
      "site": "00b56470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
              ]
            ]
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
      "definition_site": "00b5655c",
      "incomplete_value": false,
      "site": "00b56570",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56494",
      "incomplete_value": false,
      "site": "00b564a8",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b564f4",
      "READ",
      [
        "storage",
        "00c1ba58",
        null,
        "pointer"
      ]
    ],
    [
      "00b564f4",
      "PARAM",
      [
        "storage",
        "00b5a1e0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00b56530",
      "READ",
      [
        "storage",
        "010a10d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b564f4",
      "READ",
      [
        "storage",
        "00c1bb08",
        null,
        "pointer"
      ]
    ],
    [
      "00b564f4",
      "PARAM",
      [
        "storage",
        "00b5a2a8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00b56530",
      "READ",
      [
        "storage",
        "010a1190",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b563e8.md#insn-00b56440) · [`00b56470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b563e8.md#insn-00b56470) · [`00b564a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b563e8.md#insn-00b564a8)
- 新版 `00b56508`（命令位置の公開資料なし） · `00b56538`（命令位置の公開資料なし） · `00b56570`（命令位置の公開資料なし）

~~~diff
- 00b56440 ["INT_ADD", "register:40f0:8", ["const:b56440:8", "const:4:8"]]
- 00b56440 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b56508 ["INT_ADD", "register:40f0:8", ["const:b56508:8", "const:4:8"]]
+ 00b56508 ["CALL", null, ["callee:00bddf70:8"]]
- 00b56440 bytes a01e0294
+ 00b56508 bytes 9a1e0294
- 00b56470 ["INT_ADD", "register:40f0:8", ["const:b56470:8", "const:4:8"]]
- 00b56470 ["CALL", null, ["callee:0047495c:8"]]
+ 00b56538 ["INT_ADD", "register:40f0:8", ["const:b56538:8", "const:4:8"]]
+ 00b56538 ["CALL", null, ["callee:0047495c:8"]]
- 00b56470 bytes 3b79e497
+ 00b56538 bytes 0979e497
- 00b564a8 ["INT_ADD", "register:40f0:8", ["const:b564a8:8", "const:4:8"]]
- 00b564a8 ["CALL", null, ["callee:00be08a0:8"]]
+ 00b56570 ["INT_ADD", "register:40f0:8", ["const:b56570:8", "const:4:8"]]
+ 00b56570 ["CALL", null, ["callee:00be08a0:8"]]
- 00b564a8 bytes d2280294
+ 00b56570 bytes cc280294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5297b70014a89723765c621cd5dfdf0"></a>

### [`00b56684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56684.md) → [`00b5674c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5674c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be06c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06c0.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0770.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b566ac",
      "incomplete_value": true,
      "site": "00b566b0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b566b4",
      "incomplete_value": true,
      "site": "00b566bc",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b566d4",
      "incomplete_value": true,
      "site": "00b566d8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b566b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56684.md#insn-00b566b0) · [`00b566bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56684.md#insn-00b566bc) · [`00b566d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56684.md#insn-00b566d8)
- 新版 `00b56778`（命令位置の公開資料なし） · `00b56784`（命令位置の公開資料なし） · `00b567a0`（命令位置の公開資料なし）

~~~diff
- 00b566b0 ["INT_ADD", "register:40f0:8", ["const:b566b0:8", "const:4:8"]]
- 00b566b0 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b56778 ["INT_ADD", "register:40f0:8", ["const:b56778:8", "const:4:8"]]
+ 00b56778 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b566b0 bytes 201d0294
+ 00b56778 bytes 1a1d0294
- 00b566bc ["INT_ADD", "register:40f0:8", ["const:b566bc:8", "const:4:8"]]
- 00b566bc ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b56784 ["INT_ADD", "register:40f0:8", ["const:b56784:8", "const:4:8"]]
+ 00b56784 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b566bc bytes 951d0294
+ 00b56784 bytes 8f1d0294
- 00b566d8 ["INT_ADD", "register:40f0:8", ["const:b566d8:8", "const:4:8"]]
- 00b566d8 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b567a0 ["INT_ADD", "register:40f0:8", ["const:b567a0:8", "const:4:8"]]
+ 00b567a0 ["CALL", null, ["callee:00bddea0:8"]]
- 00b566d8 bytes c61d0294
+ 00b567a0 bytes c01d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb45b6f02a55ee17c0379ddc8487878"></a>

### [`00b56714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56714.md) → [`00b567dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal8ActivateEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0740.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b55e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md) [`00b5a394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a394.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be07f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07f0.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) [`00b5a45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a45c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 14.29% / 新版 17.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5674c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b567f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b567fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5674c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b56820",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00b56820",
      "PARAM",
      [
        "storage",
        "00b5a394",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b56814",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b56820",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b56820",
      "PARAM",
      [
        "storage",
        "00b5a45c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5674c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56714.md#insn-00b5674c) · [`00b5676c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56714.md#insn-00b5676c) · [`00b56778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56714.md#insn-00b56778)
- 新版 `00b56834`（命令位置の公開資料なし） · `00b56840`（命令位置の公開資料なし）

~~~diff
- 00b5674c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b5674c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5674c bytes e82700f9
- 00b5676c ["INT_ADD", "register:40f0:8", ["const:b5676c:8", "const:4:8"]]
- 00b5676c ["CALL", null, ["callee:00bddf70:8"]]
+ 00b56834 ["INT_ADD", "register:40f0:8", ["const:b56834:8", "const:4:8"]]
+ 00b56834 ["CALL", null, ["callee:00bddf70:8"]]
- 00b5676c bytes d51d0294
+ 00b56834 bytes cf1d0294
- 00b56778 ["INT_ADD", "register:40f0:8", ["const:b56778:8", "const:4:8"]]
- 00b56778 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b56840 ["INT_ADD", "register:40f0:8", ["const:b56840:8", "const:4:8"]]
+ 00b56840 ["CALL", null, ["callee:00bddf30:8"]]
- 00b56778 bytes c21d0294
+ 00b56840 bytes bc1d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-456ba616a0948c2a9b78a83774c03378"></a>

### [`00b569b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b569b0.md) → [`00b56a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56a78.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0680.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be0730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0730.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b569b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b569b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b569b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b569b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b569b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b569b8",
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
      "00b56a78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b56a80",
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

- 旧版 [`00b569b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b569b0.md#insn-00b569b0) · [`00b569b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b569b0.md#insn-00b569b4) · [`00b569b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b569b0.md#insn-00b569b8)

~~~diff
- 00b569b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b569b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b569b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b569b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b569b0 bytes f657bda9
- 00b569b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b569b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b569b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b569b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b569b4 bytes f44f01a9
- 00b569b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b569b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b569b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b569b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b569b8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3f2246782180225bebeed90d8801ca"></a>

### [`00b56a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56a40.md) → [`00b56b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0640.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b55e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md) [`00b5a394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a394.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be06f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06f0.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) [`00b5a45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a45c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 30.77% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56b4c",
      "incomplete_value": true,
      "site": "00b56b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56a84",
      "incomplete_value": true,
      "site": "00b56a98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56b88",
      "incomplete_value": true,
      "site": "00b56b90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56ac0",
      "incomplete_value": true,
      "site": "00b56ac8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
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
      "definition_site": "00b56bb4",
      "incomplete_value": false,
      "site": "00b56bc8",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56aec",
      "incomplete_value": false,
      "site": "00b56b00",
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
            "const:ebf:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56b4c",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00b56b4c",
      "PARAM",
      [
        "storage",
        "00b5a394",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b56b88",
      "READ",
      [
        "storage",
        "010a10e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56b4c",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b56b4c",
      "PARAM",
      [
        "storage",
        "00b5a45c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b56b88",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56a40.md#insn-00b56a98) · [`00b56ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56a40.md#insn-00b56ac8) · [`00b56b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56a40.md#insn-00b56b00)
- 新版 `00b56b60`（命令位置の公開資料なし） · `00b56b90`（命令位置の公開資料なし） · `00b56bc8`（命令位置の公開資料なし）

~~~diff
- 00b56a98 ["INT_ADD", "register:40f0:8", ["const:b56a98:8", "const:4:8"]]
- 00b56a98 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b56b60 ["INT_ADD", "register:40f0:8", ["const:b56b60:8", "const:4:8"]]
+ 00b56b60 ["CALL", null, ["callee:00bddf70:8"]]
- 00b56a98 bytes 0a1d0294
+ 00b56b60 bytes 041d0294
- 00b56ac8 ["INT_ADD", "register:40f0:8", ["const:b56ac8:8", "const:4:8"]]
- 00b56ac8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b56b90 ["INT_ADD", "register:40f0:8", ["const:b56b90:8", "const:4:8"]]
+ 00b56b90 ["CALL", null, ["callee:0047495c:8"]]
- 00b56ac8 bytes a577e497
+ 00b56b90 bytes 7377e497
- 00b56b00 ["INT_ADD", "register:40f0:8", ["const:b56b00:8", "const:4:8"]]
- 00b56b00 ["CALL", null, ["callee:00be08b0:8"]]
+ 00b56bc8 ["INT_ADD", "register:40f0:8", ["const:b56bc8:8", "const:4:8"]]
+ 00b56bc8 ["CALL", null, ["callee:00be08b0:8"]]
- 00b56b00 bytes 40270294
+ 00b56bc8 bytes 3a270294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0137aa1354711a3f955fdf1af0d3b461"></a>

### [`00b56cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56cdc.md) → [`00b56da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56da4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26FetchAndActivateLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06b0.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0760.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56ce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56ce4",
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
      "00b56da4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56da8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b56dac",
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

- 旧版 [`00b56cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56cdc.md#insn-00b56cdc) · [`00b56ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56cdc.md#insn-00b56ce0) · [`00b56ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56cdc.md#insn-00b56ce4)

~~~diff
- 00b56cdc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56cdc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56cdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b56cdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56cdc bytes f657bda9
- 00b56ce0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56ce0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56ce0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56ce0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56ce0 bytes f44f01a9
- 00b56ce4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56ce4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56ce4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56ce4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8854bd21c0aed97a7a1feefd3c712cf"></a>

### [`00b56d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56d6c.md) → [`00b56e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56e34.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal5FetchEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06e0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b5606c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b5606c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00be0790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0790.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b56134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56134.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 29.73% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56d80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56d7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56d84",
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
      "00b56e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56e48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b56e4c",
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

- 旧版 [`00b56d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56d6c.md#insn-00b56d7c) · [`00b56d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56d6c.md#insn-00b56d80) · [`00b56d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56d6c.md#insn-00b56d84)

~~~diff
- 00b56d7c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56d7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56d7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b56d7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56d7c bytes f65708a9
- 00b56d80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56d80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56d80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b56d80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56d80 bytes f44f09a9
- 00b56d84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56d84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56d84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b56d84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56d84 bytes fd7b0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a26d01bed8b674468e5edbabeece2d"></a>

### [`00b57004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57004.md) → [`00b570cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b570cc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0620.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be06d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06d0.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b57004",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b57008",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5700c",
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
      "00b570cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b570d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b570d4",
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

- 旧版 [`00b57004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57004.md#insn-00b57004) · [`00b57008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57004.md#insn-00b57008) · [`00b5700c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57004.md#insn-00b5700c)

~~~diff
- 00b57004 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b57004 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b57004 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b57004 bytes f50f1df8
- 00b57008 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b57008 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b57008 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b57008 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b57008 bytes f44f01a9
- 00b5700c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5700c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5700c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5700c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5700c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02143c49ae7300242495639b26940878"></a>

### [`00b57094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57094.md) → [`00b5715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0610.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b560ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00be06c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06c0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 75.86% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b570cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57194"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b571a0",
      "incomplete_value": true,
      "site": "00b571ac",
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
      "unmatched:00b570cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b571d4",
      "READ",
      [
        "storage",
        "010a10e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b572d4",
      "READ",
      [
        "storage",
        "00c1ba38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b57194",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b571d4",
      "READ",
      [
        "storage",
        "010a11a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b572d4",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b570cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57094.md#insn-00b570cc) · [`00b570e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57094.md#insn-00b570e4) · [`00b57100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57094.md#insn-00b57100)
- 新版 `00b571ac`（命令位置の公開資料なし） · `00b571c8`（命令位置の公開資料なし）

~~~diff
- 00b570cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b570cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b570cc bytes e82700f9
- 00b570e4 ["INT_ADD", "register:40f0:8", ["const:b570e4:8", "const:4:8"]]
- 00b570e4 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b571ac ["INT_ADD", "register:40f0:8", ["const:b571ac:8", "const:4:8"]]
+ 00b571ac ["CALL", null, ["callee:00bddf70:8"]]
- 00b570e4 bytes 771b0294
+ 00b571ac bytes 711b0294
- 00b57100 ["INT_ADD", "register:40f0:8", ["const:b57100:8", "const:4:8"]]
- 00b57100 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b571c8 ["INT_ADD", "register:40f0:8", ["const:b571c8:8", "const:4:8"]]
+ 00b571c8 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b57100 bytes 001c0294
+ 00b571c8 bytes fa1b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5af2dac61a9474fa6341bf1c4455a9"></a>

### [`00b5732c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b5732c.md) → [`00b573f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_21ConfigKeyValueVariantEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0600.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00b560ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be06b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06b0.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 67.01% / 新版 63.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b578cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57994"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b576c8",
      "incomplete_value": false,
      "site": "00b576cc",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57600",
      "incomplete_value": false,
      "site": "00b57604",
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
            "const:98b:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b574ec",
      "DATA",
      [
        "storage",
        "002f8b4a",
        "switchD_00b5742c::switchdataD_002f8b4a",
        "byte"
      ]
    ],
    [
      "00b576c8",
      "PARAM",
      [
        "storage",
        "0029898b",
        null,
        "string"
      ]
    ],
    [
      "00b577d4",
      "READ",
      [
        "storage",
        "010a10f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b574ec",
      "DATA",
      [
        "storage",
        "002f8b4a",
        "switchD_00b574f4::switchdataD_002f8b4a",
        "byte"
      ]
    ],
    [
      "00b576c8",
      "PARAM",
      [
        "storage",
        "00298a18",
        null,
        "string"
      ]
    ],
    [
      "00b577d4",
      "READ",
      [
        "storage",
        "010a11b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b5732c.md#insn-00b57604) · [`00b576c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b5732c.md#insn-00b576c8) · [`00b576d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b5732c.md#insn-00b576d4)
- 新版 `00b576cc`（命令位置の公開資料なし） · `00b57790`（命令位置の公開資料なし） · `00b5779c`（命令位置の公開資料なし）

~~~diff
- 00b57604 ["INT_ADD", "register:40f0:8", ["const:b57604:8", "const:4:8"]]
- 00b57604 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b576cc ["INT_ADD", "register:40f0:8", ["const:b576cc:8", "const:4:8"]]
+ 00b576cc ["CALL", null, ["callee:00bdddf0:8"]]
- 00b57604 bytes cf190294
+ 00b576cc bytes c9190294
- 00b576c8 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
+ 00b57790 ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 00b576c8 bytes e0010054
+ 00b57790 bytes e0010054
- 00b576d4 ["INT_ADD", "register:40f0:8", ["const:b576d4:8", "const:4:8"]]
- 00b576d4 ["CALL", null, ["callee:00bde6f0:8"]]
+ 00b5779c ["INT_ADD", "register:40f0:8", ["const:b5779c:8", "const:4:8"]]
+ 00b5779c ["CALL", null, ["callee:00bde6f0:8"]]
- 00b576d4 bytes db1b0294
+ 00b5779c bytes d51b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fffb4c720245d67883fcda0565d1012"></a>

### [`00b57a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57a40.md) → [`00b57b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be05f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05f0.md) · 呼出先 21件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00b560ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06a0.md) · 呼出先 21件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 57.81% / 新版 60.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57c9c"
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
      "00b57cfc",
      "READ",
      [
        "storage",
        "010a10f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b57cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57dd4"
      ]
    ],
    [
      "unmatched:00b57cfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b57cec"
      ]
    ]
  ],
  "added": [
    [
      "00b57cfc",
      "READ",
      [
        "storage",
        "010a11b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57dd4"
      ]
    ],
    [
      "00b57dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57db4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57a40.md#insn-00b57aa4) · [`00b57b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57a40.md#insn-00b57b0c) · [`00b57b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57a40.md#insn-00b57b40)
- 新版 `00b57b6c`（命令位置の公開資料なし） · `00b57c08`（命令位置の公開資料なし）

~~~diff
- 00b57aa4 ["INT_ADD", "register:40f0:8", ["const:b57aa4:8", "const:4:8"]]
- 00b57aa4 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b57b6c ["INT_ADD", "register:40f0:8", ["const:b57b6c:8", "const:4:8"]]
+ 00b57b6c ["CALL", null, ["callee:00bddf30:8"]]
- 00b57aa4 bytes f7180294
+ 00b57b6c bytes f1180294
- 00b57b0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b57b0c ["INT_ADD", "register:40f0:8", ["const:b57b0c:8", "const:4:8"]]
- 00b57b0c ["CALLIND", null, ["register:0:8"]]
- 00b57b0c bytes 00013fd6
- 00b57b40 ["INT_ADD", "register:40f0:8", ["const:b57b40:8", "const:4:8"]]
- 00b57b40 ["CALL", null, ["callee:0047495c:8"]]
+ 00b57c08 ["INT_ADD", "register:40f0:8", ["const:b57c08:8", "const:4:8"]]
+ 00b57c08 ["CALL", null, ["callee:0047495c:8"]]
- 00b57b40 bytes 8773e497
+ 00b57c08 bytes 5573e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fea94cd5f2990e862ce0550fd987502"></a>

### [`00b57ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57ffc.md) → [`00b580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17SetConfigSettingsENS0_14ConfigSettingsE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0670.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00b55f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55f64.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be0720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0720.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b5602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.25% / 新版 77.25%

CFGの説明率　旧版 15.15% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b581b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b581bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58038",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58078",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5807c",
      "READ",
      [
        "storage",
        "010a1208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b58100",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b58140",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58144",
      "READ",
      [
        "storage",
        "010a12c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57ffc.md#insn-00b58038) · [`00b58050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57ffc.md#insn-00b58050) · [`00b5806c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57ffc.md#insn-00b5806c)
- 新版 `00b58118`（命令位置の公開資料なし） · `00b58134`（命令位置の公開資料なし）

~~~diff
- 00b58038 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b58038 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b58038 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b58038 bytes a8831af8
- 00b58050 ["INT_ADD", "register:40f0:8", ["const:b58050:8", "const:4:8"]]
- 00b58050 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b58118 ["INT_ADD", "register:40f0:8", ["const:b58118:8", "const:4:8"]]
+ 00b58118 ["CALL", null, ["callee:00bddf70:8"]]
- 00b58050 bytes 9c170294
+ 00b58118 bytes 96170294
- 00b5806c ["INT_ADD", "register:40f0:8", ["const:b5806c:8", "const:4:8"]]
- 00b5806c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b58134 ["INT_ADD", "register:40f0:8", ["const:b58134:8", "const:4:8"]]
+ 00b58134 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5806c bytes 25180294
+ 00b58134 bytes 1f180294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7723936d3a5d64f5673d660d77d67322"></a>

### [`00b58450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58450.md) → [`00b58518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58518.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17GetConfigSettingsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0660.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c6c4.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00be0710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0710.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58454"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58450",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58454",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58458",
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
      "00b58518",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5851c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58520",
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

- 旧版 [`00b58450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58450.md#insn-00b58450) · [`00b58454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58450.md#insn-00b58454) · [`00b58458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58450.md#insn-00b58458)

~~~diff
- 00b58450 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b58450 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b58450 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b58450 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58450 bytes f85fbca9
- 00b58454 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b58454 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b58454 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58454 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58454 bytes f65701a9
- 00b58458 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58458 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58458 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58458 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c598e717267340b4d4381f421616cbed"></a>

### [`00b58538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58538.md) → [`00b58600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be05e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05e0.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00be0690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0690.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58644",
      "incomplete_value": true,
      "site": "00b58654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5857c",
      "incomplete_value": true,
      "site": "00b5858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:188:8"
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
      "definition_site": "00b586a0",
      "incomplete_value": false,
      "site": "00b586a8",
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
            "const:873:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b585d8",
      "incomplete_value": false,
      "site": "00b585e0",
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
            "const:7e6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b58644",
      "READ",
      [
        "storage",
        "010a1188",
        null,
        "undefined8"
      ]
    ],
    [
      "00b586a0",
      "PARAM",
      [
        "storage",
        "0029a7e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58644",
      "READ",
      [
        "storage",
        "010a1248",
        null,
        "undefined8"
      ]
    ],
    [
      "00b586a0",
      "PARAM",
      [
        "storage",
        "0029a873",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5858c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58538.md#insn-00b5858c) · [`00b585e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58538.md#insn-00b585e0) · [`00b58628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58538.md#insn-00b58628)
- 新版 `00b58654`（命令位置の公開資料なし） · `00b586a8`（命令位置の公開資料なし）

~~~diff
- 00b5858c ["INT_ADD", "register:40f0:8", ["const:b5858c:8", "const:4:8"]]
- 00b5858c ["CALL", null, ["callee:00474b70:8"]]
+ 00b58654 ["INT_ADD", "register:40f0:8", ["const:b58654:8", "const:4:8"]]
+ 00b58654 ["CALL", null, ["callee:00474b70:8"]]
- 00b5858c bytes 7971e497
+ 00b58654 bytes 4771e497
- 00b585e0 ["INT_ADD", "register:40f0:8", ["const:b585e0:8", "const:4:8"]]
- 00b585e0 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b586a8 ["INT_ADD", "register:40f0:8", ["const:b586a8:8", "const:4:8"]]
+ 00b586a8 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b585e0 bytes d8150294
+ 00b586a8 bytes d2150294
- 00b58628 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b58628 ["RETURN", null, ["register:0:8"]]
- 00b58628 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309822cd2abb09bcf0718f84c354567b"></a>

### [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md) → [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) FUN_00b586f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b58538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58538.md) [`00b587e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b587e4.md) [`00b588d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b588d8.md) [`00b589d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b589d8.md) [`00b58b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58b48.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 5件 [`00b58600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md) [`00b588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b588ac.md) [`00b589a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md) [`00b58aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md) [`00b58c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.18% / 新版 88.18%

CFGの説明率　旧版 61.90% / 新版 61.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5862c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5862c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58630"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5862c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58630",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58634",
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
      "00b586f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b586f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b586fc",
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

- 旧版 [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md#insn-00b5862c) · [`00b58630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md#insn-00b58630) · [`00b58634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md#insn-00b58634)

~~~diff
- 00b5862c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5862c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5862c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5862c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5862c bytes f85fbca9
- 00b58630 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b58630 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b58630 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58630 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58630 bytes f65701a9
- 00b58634 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58634 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58634 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58634 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58634 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30b8268cab518b2ae2676bde172c5092"></a>

### [`00b588d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b588d8.md) → [`00b589a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetDoubleEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0750.md) · 呼出先 4件 [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2b0.md)
- 新版 呼出元 1件 [`00be0800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0800.md) · 呼出先 4件 [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

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
      "definition_site": "00b589e4",
      "incomplete_value": true,
      "site": "00b589f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5891c",
      "incomplete_value": true,
      "site": "00b5892c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:170:8"
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
      "definition_site": "00b58a40",
      "incomplete_value": false,
      "site": "00b58a48",
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
            "const:e8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58978",
      "incomplete_value": false,
      "site": "00b58980",
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
            "const:e01:8"
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
      "00b589e4",
      "READ",
      [
        "storage",
        "010a1170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58a40",
      "PARAM",
      [
        "storage",
        "0029de01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b589e4",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58a40",
      "PARAM",
      [
        "storage",
        "0029de8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5892c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b588d8.md#insn-00b5892c) · [`00b58980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b588d8.md#insn-00b58980) · [`00b588fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b588d8.md#insn-00b588fc)
- 新版 `00b589f4`（命令位置の公開資料なし） · `00b58a48`（命令位置の公開資料なし） · `00b589c4`（命令位置の公開資料なし）

~~~diff
- 00b5892c ["INT_ADD", "register:40f0:8", ["const:b5892c:8", "const:4:8"]]
- 00b5892c ["CALL", null, ["callee:00bde360:8"]]
+ 00b589f4 ["INT_ADD", "register:40f0:8", ["const:b589f4:8", "const:4:8"]]
+ 00b589f4 ["CALL", null, ["callee:00bde360:8"]]
- 00b5892c bytes 61160294
+ 00b589f4 bytes 5b160294
- 00b58980 ["INT_ADD", "register:40f0:8", ["const:b58980:8", "const:4:8"]]
- 00b58980 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b58a48 ["INT_ADD", "register:40f0:8", ["const:b58a48:8", "const:4:8"]]
+ 00b58a48 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b58980 bytes f0140294
+ 00b58a48 bytes ea140294
- 00b588fc ["INT_ADD", "register:40f0:8", ["const:b588fc:8", "const:4:8"]]
- 00b588fc ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b589c4 ["INT_ADD", "register:40f0:8", ["const:b589c4:8", "const:4:8"]]
+ 00b589c4 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b588fc bytes 01160294
+ 00b589c4 bytes fb150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45bfae3be07922b1ea71ba02de3ce8e0"></a>

### [`00b589d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b589d8.md) → [`00b58aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetStringEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0760.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0810.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

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
      "definition_site": "00b58b08",
      "incomplete_value": true,
      "site": "00b58b14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58a40",
      "incomplete_value": true,
      "site": "00b58a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:178:8"
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
      "definition_site": "00b58b70",
      "incomplete_value": false,
      "site": "00b58b78",
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
            "const:70b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58aa8",
      "incomplete_value": false,
      "site": "00b58ab0",
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
            "const:67e:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b58b08",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58b70",
      "PARAM",
      [
        "storage",
        "0029967e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58b08",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58b70",
      "PARAM",
      [
        "storage",
        "0029970b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b589d8.md#insn-00b58a4c) · [`00b58ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b589d8.md#insn-00b58ab0) · [`00b58a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b589d8.md#insn-00b58a1c)
- 新版 `00b58b14`（命令位置の公開資料なし） · `00b58b78`（命令位置の公開資料なし） · `00b58ae4`（命令位置の公開資料なし）

~~~diff
- 00b58a4c ["INT_ADD", "register:40f0:8", ["const:b58a4c:8", "const:4:8"]]
- 00b58a4c ["CALL", null, ["callee:0047495c:8"]]
+ 00b58b14 ["INT_ADD", "register:40f0:8", ["const:b58b14:8", "const:4:8"]]
+ 00b58b14 ["CALL", null, ["callee:0047495c:8"]]
- 00b58a4c bytes c46fe497
+ 00b58b14 bytes 926fe497
- 00b58ab0 ["INT_ADD", "register:40f0:8", ["const:b58ab0:8", "const:4:8"]]
- 00b58ab0 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b58b78 ["INT_ADD", "register:40f0:8", ["const:b58b78:8", "const:4:8"]]
+ 00b58b78 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b58ab0 bytes a4140294
+ 00b58b78 bytes 9e140294
- 00b58a1c ["INT_ADD", "register:40f0:8", ["const:b58a1c:8", "const:4:8"]]
- 00b58a1c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b58ae4 ["INT_ADD", "register:40f0:8", ["const:b58ae4:8", "const:4:8"]]
+ 00b58ae4 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b58a1c bytes b9150294
+ 00b58ae4 bytes b3150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bd27f413077a58d7ed75a78b2c1e00"></a>

### [`00b58b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58b48.md) → [`00b58c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetDataEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0710.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b5862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b5862c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be07c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07c0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

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
      "definition_site": "00b58c78",
      "incomplete_value": true,
      "site": "00b58c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58bb0",
      "incomplete_value": true,
      "site": "00b58bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:180:8"
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
      "definition_site": "00b58ce0",
      "incomplete_value": false,
      "site": "00b58ce8",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58c18",
      "incomplete_value": false,
      "site": "00b58c20",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b58c78",
      "READ",
      [
        "storage",
        "010a1180",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58ce0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58c78",
      "READ",
      [
        "storage",
        "010a1240",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58ce0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58b48.md#insn-00b58bbc) · [`00b58c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58b48.md#insn-00b58c20) · [`00b58b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58b48.md#insn-00b58b8c)
- 新版 `00b58c84`（命令位置の公開資料なし） · `00b58ce8`（命令位置の公開資料なし） · `00b58c54`（命令位置の公開資料なし）

~~~diff
- 00b58bbc ["INT_ADD", "register:40f0:8", ["const:b58bbc:8", "const:4:8"]]
- 00b58bbc ["CALL", null, ["callee:0047495c:8"]]
+ 00b58c84 ["INT_ADD", "register:40f0:8", ["const:b58c84:8", "const:4:8"]]
+ 00b58c84 ["CALL", null, ["callee:0047495c:8"]]
- 00b58bbc bytes 686fe497
+ 00b58c84 bytes 366fe497
- 00b58c20 ["INT_ADD", "register:40f0:8", ["const:b58c20:8", "const:4:8"]]
- 00b58c20 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b58ce8 ["INT_ADD", "register:40f0:8", ["const:b58ce8:8", "const:4:8"]]
+ 00b58ce8 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b58c20 bytes 48140294
+ 00b58ce8 bytes 42140294
- 00b58b8c ["INT_ADD", "register:40f0:8", ["const:b58b8c:8", "const:4:8"]]
- 00b58b8c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b58c54 ["INT_ADD", "register:40f0:8", ["const:b58c54:8", "const:4:8"]]
+ 00b58c54 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b58b8c bytes 5d150294
+ 00b58c54 bytes 57150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11503dacd9f5b31d69e20088b94bc123"></a>

### [`00b58fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58fa4.md) → [`00b5906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b5906c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal6GetAllEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be06f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06f0.md) · 呼出先 26件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`0056c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c6c4.md) [`0084c0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c0cc.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`00be07a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07a0.md) · 呼出先 26件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`0084c0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c0cc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b590c4",
      "incomplete_value": true,
      "site": "00b590cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58ffc",
      "incomplete_value": true,
      "site": "00b59004",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:128:8"
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
      "definition_site": "00b59214",
      "incomplete_value": true,
      "site": "00b59224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5914c",
      "incomplete_value": true,
      "site": "00b5915c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b59234",
      "incomplete_value": true,
      "site": "00b59240",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5916c",
      "incomplete_value": true,
      "site": "00b59178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:168:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b590c4",
      "READ",
      [
        "storage",
        "010a1128",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59214",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59234",
      "READ",
      [
        "storage",
        "010a1168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b590c4",
      "READ",
      [
        "storage",
        "010a11e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59214",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59234",
      "READ",
      [
        "storage",
        "010a1228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58fa4.md#insn-00b59004) · [`00b5915c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58fa4.md#insn-00b5915c) · [`00b59178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58fa4.md#insn-00b59178)
- 新版 `00b590cc`（命令位置の公開資料なし） · `00b59224`（命令位置の公開資料なし） · `00b59240`（命令位置の公開資料なし）

~~~diff
- 00b59004 ["INT_ADD", "register:40f0:8", ["const:b59004:8", "const:4:8"]]
- 00b59004 ["CALL", null, ["callee:0047495c:8"]]
+ 00b590cc ["INT_ADD", "register:40f0:8", ["const:b590cc:8", "const:4:8"]]
+ 00b590cc ["CALL", null, ["callee:0047495c:8"]]
- 00b59004 bytes 566ee497
+ 00b590cc bytes 246ee497
- 00b5915c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5915c ["INT_ADD", "register:40f0:8", ["const:b5915c:8", "const:4:8"]]
- 00b5915c ["CALLIND", null, ["register:0:8"]]
+ 00b59224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59224 ["INT_ADD", "register:40f0:8", ["const:b59224:8", "const:4:8"]]
+ 00b59224 ["CALLIND", null, ["register:0:8"]]
- 00b5915c bytes 00013fd6
+ 00b59224 bytes 00013fd6
- 00b59178 ["INT_ADD", "register:40f0:8", ["const:b59178:8", "const:4:8"]]
- 00b59178 ["CALL", null, ["callee:0056c6c4:8"]]
+ 00b59240 ["INT_ADD", "register:40f0:8", ["const:b59240:8", "const:4:8"]]
+ 00b59240 ["CALL", null, ["callee:0056c6c4:8"]]
- 00b59178 bytes 534de897
+ 00b59240 bytes 214de897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-084d9088fb52162496d46d0dece5774b"></a>

### [`00b597c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b597c0.md) → [`00b59888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17Remote

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06a0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00b59f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f64.md) [`00b5a59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a59c.md) [`00b5a5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a5a0.md)
- 新版 呼出元 1件 [`00be0750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0750.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b5a02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md) [`00b5a664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a664.md) [`00b5a668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a668.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 23.08% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5997c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b598a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59984"
      ]
    ],
    [
      "unmatched:00b598ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59990"
      ]
    ],
    [
      "unmatched:00b598b8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5998c"
      ]
    ]
  ],
  "added": [
    [
      "00b59970",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59984"
      ]
    ],
    [
      "00b59974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59990"
      ]
    ],
    [
      "00b59980",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5998c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5984c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b597c0.md#insn-00b5984c) · [`00b59874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b597c0.md#insn-00b59874) · [`00b598a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b597c0.md#insn-00b598a8)
- 新版 `00b59914`（命令位置の公開資料なし）

~~~diff
- 00b5984c ["BRANCH", null, ["local:b9:8"]]
+ 00b59914 ["BRANCH", null, ["local:b11:8"]]
- 00b5984c bytes 14000014
+ 00b59914 bytes 14000014
- 00b59874 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b59874 ["INT_ADD", "register:40f0:8", ["const:b59874:8", "const:4:8"]]
- 00b59874 ["CALLIND", null, ["register:0:8"]]
- 00b59874 bytes 20013fd6
- 00b598a8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b598a8 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee806eb01e9f62e0a9448a1e05160054"></a>

### [`00b59e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59e44.md) → [`00b59f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59f0c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0850.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00be0900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0900.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 80.65% / 新版 80.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b59f4c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b59e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59e44.md#insn-00b59e84) · [`00b59e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59e44.md#insn-00b59e88)
- 新版 `00b59f4c`（命令位置の公開資料なし）

~~~diff
- 00b59e84 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b59e84 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b59e84 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b59e84 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b59e84 bytes 7801899a
- 00b59e88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b59e88 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b59e88 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b59e88 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00b59e88 bytes 5515829a
+ 00b59f4c ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00b59f4c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b59f4c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b59f4c ["COPY", "register:40c0:8", ["tmp:0:8"]]
+ 00b59f4c bytes 7801899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f82560714e6bda6ab288d22ee9af24"></a>

### [`00b59f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f90.md) → [`00b5a058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a058.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12Fut

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07d0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0880.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b59ffc",
      "incomplete_value": false,
      "site": "00b5a000",
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
      "definition_site": "00b5a004",
      "incomplete_value": true,
      "site": "00b5a014",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5a008",
      "incomplete_value": true,
      "site": "00b5a014",
      "value": [
        "live",
        "register:40b0:8"
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
      "unmatched:00b59ffc",
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
      "00b5a0c4",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f90.md#insn-00b5a000) · [`00b5a014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f90.md#insn-00b5a014) · [`00b59fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f90.md#insn-00b59fc4)
- 新版 `00b5a0c8`（命令位置の公開資料なし） · `00b5a0dc`（命令位置の公開資料なし） · `00b5a08c`（命令位置の公開資料なし）

~~~diff
- 00b5a000 ["INT_ADD", "register:40f0:8", ["const:b5a000:8", "const:4:8"]]
- 00b5a000 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5a0c8 ["INT_ADD", "register:40f0:8", ["const:b5a0c8:8", "const:4:8"]]
+ 00b5a0c8 ["CALL", null, ["callee:00bde130:8"]]
- 00b5a000 bytes 20100294
+ 00b5a0c8 bytes 1a100294
- 00b5a014 ["INT_ADD", "register:40f0:8", ["const:b5a014:8", "const:4:8"]]
- 00b5a014 ["CALL", null, ["callee:00bddfa0:8"]]
+ 00b5a0dc ["INT_ADD", "register:40f0:8", ["const:b5a0dc:8", "const:4:8"]]
+ 00b5a0dc ["CALL", null, ["callee:00bddfa0:8"]]
- 00b5a014 bytes b70f0294
+ 00b5a0dc bytes b10f0294
- 00b59fc4 ["INT_ADD", "register:40f0:8", ["const:b59fc4:8", "const:4:8"]]
- 00b59fc4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5a08c ["INT_ADD", "register:40f0:8", ["const:b5a08c:8", "const:4:8"]]
+ 00b5a08c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b59fc4 bytes d70e0294
+ 00b5a08c bytes d10e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54f66c82e9708acc35507d853ebc6b59"></a>

### [`00b5a0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a0bc.md) → [`00b5a184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a184.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIbZNS0_26CompleteWithResultInternalIbEEvRKNS_12FutureHandleEiPKcRKT_EUlPbE_EEvS5_i

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07e0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0890.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.30% / 新版 86.30%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a0c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a0c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a0c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a0c4",
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
      "00b5a184",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5a188",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5a18c",
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

- 旧版 [`00b5a0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a0bc.md#insn-00b5a0bc) · [`00b5a0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a0bc.md#insn-00b5a0c0) · [`00b5a0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a0bc.md#insn-00b5a0c4)

~~~diff
- 00b5a0bc ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b5a0bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b5a0bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a0bc bytes f90f1bf8
- 00b5a0c0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5a0c0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5a0c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a0c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a0c0 bytes f85f01a9
- 00b5a0c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5a0c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5a0c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a0c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a0c4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d52acf764f093116911569a62caa8ab"></a>

### [`00b5a1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a1ec.md) → [`00b5a2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a2b4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiP

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07f0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be08a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08a0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 25.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a1f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a1f4",
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
      "00b5a2b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5a2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5a2bc",
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

- 旧版 [`00b5a1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a1ec.md#insn-00b5a1ec) · [`00b5a1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a1ec.md#insn-00b5a1f0) · [`00b5a1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a1ec.md#insn-00b5a1f4)

~~~diff
- 00b5a1ec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5a1ec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5a1ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5a1ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a1ec bytes f85fbca9
- 00b5a1f0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5a1f0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5a1f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a1f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a1f0 bytes f65701a9
- 00b5a1f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a1f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a1f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a1f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a1f4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b7e89fd4d9802dd27015dbb99863f00"></a>

### [`00b5a2f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a2f4.md) → [`00b5a3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a3bc.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0810.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be08c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08c0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5a314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a2f4.md#insn-00b5a314) · [`00b5a328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a2f4.md#insn-00b5a328) · [`00b5a33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a2f4.md#insn-00b5a33c)
- 新版 `00b5a3dc`（命令位置の公開資料なし） · `00b5a3f0`（命令位置の公開資料なし） · `00b5a404`（命令位置の公開資料なし）

~~~diff
- 00b5a314 ["INT_ADD", "register:40f0:8", ["const:b5a314:8", "const:4:8"]]
- 00b5a314 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5a3dc ["INT_ADD", "register:40f0:8", ["const:b5a3dc:8", "const:4:8"]]
+ 00b5a3dc ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5a314 bytes 7f0e0294
+ 00b5a3dc bytes 790e0294
- 00b5a328 ["INT_ADD", "register:40f0:8", ["const:b5a328:8", "const:4:8"]]
- 00b5a328 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b5a3f0 ["INT_ADD", "register:40f0:8", ["const:b5a3f0:8", "const:4:8"]]
+ 00b5a3f0 ["CALL", null, ["callee:00bddf30:8"]]
- 00b5a328 bytes d60e0294
+ 00b5a3f0 bytes d00e0294
- 00b5a33c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5a33c ["INT_ADD", "register:40f0:8", ["const:b5a33c:8", "const:4:8"]]
- 00b5a33c ["CALLIND", null, ["register:0:8"]]
+ 00b5a404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5a404 ["INT_ADD", "register:40f0:8", ["const:b5a404:8", "const:4:8"]]
+ 00b5a404 ["CALLIND", null, ["register:0:8"]]
- 00b5a33c bytes 00013fd6
+ 00b5a404 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd6ec0f54fdd972c9f3627abb07479de"></a>

### [`00b5a3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a3a0.md) → [`00b5a468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a468.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0800.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be08b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08b0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a3a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a3a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a3a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a3a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a3a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a3a8",
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
      "00b5a468",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5a46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5a470",
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

- 旧版 [`00b5a3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a3a0.md#insn-00b5a3a0) · [`00b5a3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a3a0.md#insn-00b5a3a4) · [`00b5a3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a3a0.md#insn-00b5a3a8)

~~~diff
- 00b5a3a0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5a3a0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5a3a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5a3a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a3a0 bytes f85fbca9
- 00b5a3a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5a3a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5a3a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a3a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a3a4 bytes f65701a9
- 00b5a3a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a3a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a3a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a3a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a3a8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f9a029e1921d7757c20bb84f5212f1"></a>

### [`00b5a4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a4a8.md) → [`00b5a570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a570.md) _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0820.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be08d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08d0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5a5bc",
      "incomplete_value": true,
      "site": "00b5a5c0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a4a8.md#insn-00b5a4f8) · [`00b5a4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a4a8.md#insn-00b5a4c8) · [`00b5a4dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a4a8.md#insn-00b5a4dc)
- 新版 `00b5a5c0`（命令位置の公開資料なし） · `00b5a590`（命令位置の公開資料なし） · `00b5a5a4`（命令位置の公開資料なし）

~~~diff
- 00b5a4f8 ["INT_ADD", "register:40f0:8", ["const:b5a4f8:8", "const:4:8"]]
- 00b5a4f8 ["CALL", null, ["callee:00bddf20:8"]]
+ 00b5a5c0 ["INT_ADD", "register:40f0:8", ["const:b5a5c0:8", "const:4:8"]]
+ 00b5a5c0 ["CALL", null, ["callee:00bddf20:8"]]
- 00b5a4f8 bytes 5e0e0294
+ 00b5a5c0 bytes 580e0294
- 00b5a4c8 ["INT_ADD", "register:40f0:8", ["const:b5a4c8:8", "const:4:8"]]
- 00b5a4c8 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5a590 ["INT_ADD", "register:40f0:8", ["const:b5a590:8", "const:4:8"]]
+ 00b5a590 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5a4c8 bytes 120e0294
+ 00b5a590 bytes 0c0e0294
- 00b5a4dc ["INT_ADD", "register:40f0:8", ["const:b5a4dc:8", "const:4:8"]]
- 00b5a4dc ["CALL", null, ["callee:00bddf30:8"]]
+ 00b5a5a4 ["INT_ADD", "register:40f0:8", ["const:b5a5a4:8", "const:4:8"]]
+ 00b5a5a4 ["CALL", null, ["callee:00bddf30:8"]]
- 00b5a4dc bytes 690e0294
+ 00b5a5a4 bytes 630e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b52aff6cac07b3d2acffd484785722b"></a>

### [`00b5a54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a54c.md) → [`00b5a614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a614.md) FUN_00b5a614

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a630",
      "incomplete_value": false,
      "site": "00b5a634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a568",
      "incomplete_value": false,
      "site": "00b5a56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "00b5a634",
      "DATA",
      [
        "storage",
        "00c11980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b5a634",
      "DATA",
      [
        "storage",
        "00c11a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a54c.md#insn-00b5a560) · [`00b5a568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a54c.md#insn-00b5a568)
- 新版 `00b5a628`（命令位置の公開資料なし） · `00b5a630`（命令位置の公開資料なし）

~~~diff
- 00b5a560 ["INT_ADD", "register:40f0:8", ["const:b5a560:8", "const:4:8"]]
- 00b5a560 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b5a628 ["INT_ADD", "register:40f0:8", ["const:b5a628:8", "const:4:8"]]
+ 00b5a628 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b5a560 bytes 78020294
+ 00b5a628 bytes 72020294
- 00b5a568 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00b5a568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5a630 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00b5a630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5a568 bytes 08012691
+ 00b5a630 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8d07e458905ab0e4d39e29f6f05a93"></a>

### [`00b5a584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a584.md) → [`00b5a64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a64c.md) FUN_00b5a64c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a650",
      "incomplete_value": false,
      "site": "00b5a654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a588",
      "incomplete_value": false,
      "site": "00b5a58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "00b5a654",
      "DATA",
      [
        "storage",
        "00c11980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b5a654",
      "DATA",
      [
        "storage",
        "00c11a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a584.md#insn-00b5a588)
- 新版 `00b5a650`（命令位置の公開資料なし）

~~~diff
- 00b5a588 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00b5a588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5a650 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00b5a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5a588 bytes 08012691
+ 00b5a650 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4493eb6d93db306454820ddc2fb8eb5b"></a>

### [`00b5a5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a5a4.md) → [`00b5a66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a66c.md) FUN_00b5a66c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde470.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5a688",
      "incomplete_value": true,
      "site": "00b5a690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a5c0",
      "incomplete_value": true,
      "site": "00b5a5c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a0:8"
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
      "definition_site": "00b5a6a4",
      "incomplete_value": false,
      "site": "00b5a6a8",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a5dc",
      "incomplete_value": true,
      "site": "00b5a5e0",
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
            "const:44b:8"
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
      "unmatched:00b5a5c0",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5a5dc",
      "PARAM",
      [
        "storage",
        "0029244b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5a688",
      "READ",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a6a4",
      "PARAM",
      [
        "storage",
        "002924d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a5a4.md#insn-00b5a5c8) · [`00b5a5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a5a4.md#insn-00b5a5e0) · [`00b5a5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a5a4.md#insn-00b5a5b4)
- 新版 `00b5a690`（命令位置の公開資料なし） · `00b5a6a8`（命令位置の公開資料なし） · `00b5a67c`（命令位置の公開資料なし）

~~~diff
- 00b5a5c8 ["INT_ADD", "register:40f0:8", ["const:b5a5c8:8", "const:4:8"]]
- 00b5a5c8 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5a690 ["INT_ADD", "register:40f0:8", ["const:b5a690:8", "const:4:8"]]
+ 00b5a690 ["CALL", null, ["callee:00551e14:8"]]
- 00b5a5c8 bytes 13dee797
+ 00b5a690 bytes e1dde797
- 00b5a5e0 ["INT_ADD", "register:40f0:8", ["const:b5a5e0:8", "const:4:8"]]
- 00b5a5e0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5a6a8 ["INT_ADD", "register:40f0:8", ["const:b5a6a8:8", "const:4:8"]]
+ 00b5a6a8 ["CALL", null, ["callee:00bde130:8"]]
- 00b5a5e0 bytes a80e0294
+ 00b5a6a8 bytes a20e0294
- 00b5a5b4 ["INT_ADD", "register:40f0:8", ["const:b5a5b4:8", "const:4:8"]]
- 00b5a5b4 ["CALL", null, ["callee:00bde470:8"]]
+ 00b5a67c ["INT_ADD", "register:40f0:8", ["const:b5a67c:8", "const:4:8"]]
+ 00b5a67c ["CALL", null, ["callee:00bde470:8"]]
- 00b5a5b4 bytes 830f0294
+ 00b5a67c bytes 7d0f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2c232f4e6a28a11cf584ebdef6c269"></a>

### [`00b5a628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a628.md) → [`00b5a6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a6f0.md) _INIT_280

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b54a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54a24.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b54aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54aec.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a62c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a62c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a628",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a62c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5a700",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5a6f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5a6f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5a700",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a628.md#insn-00b5a628) · [`00b5a62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a628.md#insn-00b5a62c) · [`00b5a644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a628.md#insn-00b5a644)

~~~diff
- 00b5a628 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b5a628 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5a628 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a628 bytes f30f1ef8
- 00b5a62c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5a62c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5a62c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a62c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a62c bytes fd7b01a9
- 00b5a644 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5a644 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5a644 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00b5a644 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:4:8"]]
- 00b5a644 bytes 1f4400b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2283f2099c1db83e22b466c188541e"></a>

### [`00b5a684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a684.md) → [`00b5a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a74c.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b5a92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a92c.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b5a9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9f4.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a754",
      "incomplete_value": true,
      "site": "00b5a758",
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
      "definition_site": "00b5a68c",
      "incomplete_value": true,
      "site": "00b5a690",
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
      "00b5a750",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a758",
      "DATA",
      [
        "storage",
        "00c11a00",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b5a770",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5a750",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a758",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b5a770",
      "READ",
      [
        "storage",
        "00c1baa0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a684.md#insn-00b5a688) · [`00b5a6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a684.md#insn-00b5a6a0) · [`00b5a6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a684.md#insn-00b5a6a8)
- 新版 `00b5a750`（命令位置の公開資料なし） · `00b5a768`（命令位置の公開資料なし） · `00b5a770`（命令位置の公開資料なし）

~~~diff
- 00b5a688 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f8:8"]]
- 00b5a688 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a750 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
+ 00b5a750 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a688 bytes 29fd44f9
+ 00b5a750 bytes 295545f9
- 00b5a6a0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5a6a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5a768 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5a768 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5a6a0 bytes e90000b4
+ 00b5a768 bytes e90000b4
- 00b5a6a8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
- 00b5a6a8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a770 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:aa0:8"]]
+ 00b5a770 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a6a8 bytes 42f844f9
+ 00b5a770 bytes 425045f9
~~~


<a id="compare-bab0023b76965b2cd86c3180465ab40c"></a>

### [`00b5a740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a740.md) → [`00b5a808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a808.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC2EPNS0_8internal40ConfigUpdateListenerRegistrationInternalE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0580.md) · 呼出先 2件 [`00b5a92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a92c.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md)
- 新版 呼出元 1件 [`00be0630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0630.md) · 呼出先 2件 [`00b5a9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9f4.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a818",
      "incomplete_value": true,
      "site": "00b5a818",
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
      "definition_site": "00b5a750",
      "incomplete_value": true,
      "site": "00b5a750",
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
      "00b5a80c",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a818",
      "DATA",
      [
        "storage",
        "00c11a00",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b5a76c",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5a80c",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a818",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b5a834",
      "READ",
      [
        "storage",
        "00c1baa0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a740.md#insn-00b5a744) · [`00b5a754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a740.md#insn-00b5a754) · [`00b5a764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a740.md#insn-00b5a764)
- 新版 `00b5a80c`（命令位置の公開資料なし） · `00b5a81c`（命令位置の公開資料なし） · `00b5a82c`（命令位置の公開資料なし）

~~~diff
- 00b5a744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f8:8"]]
- 00b5a744 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a80c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
+ 00b5a80c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a744 bytes 29fd44f9
+ 00b5a80c bytes 295545f9
- 00b5a754 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5a754 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5a81c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b5a81c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5a754 bytes 410100b4
+ 00b5a81c bytes 410100b4
- 00b5a764 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5a764 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5a82c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5a82c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5a764 bytes e90000b4
+ 00b5a82c bytes e90000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe6643845c759fab8bac68d31425530"></a>

### [`00b5a7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a7cc.md) → [`00b5a894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a894.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a8b0",
      "incomplete_value": true,
      "site": "00b5a8b4",
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
      "definition_site": "00b5a7e8",
      "incomplete_value": true,
      "site": "00b5a7ec",
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
      "00b5a8a8",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8b4",
      "DATA",
      [
        "storage",
        "00c11a00",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b5a8a8",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8b4",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a7cc.md#insn-00b5a7e0) · [`00b5a7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a7cc.md#insn-00b5a7fc)
- 新版 `00b5a8a8`（命令位置の公開資料なし） · `00b5a8c4`（命令位置の公開資料なし）

~~~diff
- 00b5a7e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f8:8"]]
- 00b5a7e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a8a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
+ 00b5a8a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a7e0 bytes 29fd44f9
+ 00b5a8a8 bytes 295545f9
- 00b5a7fc ["INT_ADD", "register:40f0:8", ["const:b5a7fc:8", "const:4:8"]]
- 00b5a7fc ["CALL", null, ["callee:00bddd60:8"]]
+ 00b5a8c4 ["INT_ADD", "register:40f0:8", ["const:b5a8c4:8", "const:4:8"]]
+ 00b5a8c4 ["CALL", null, ["callee:00bddd60:8"]]
- 00b5a7fc bytes 2d0d0294
+ 00b5a8c4 bytes 270d0294
~~~


<a id="compare-04c4e9b9e85027865b7f39dc33c12a2a"></a>

### [`00b5a814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a814.md) → [`00b5a8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a8dc.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b5a92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a92c.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b5a9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9f4.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a834"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5a8fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5a920",
      "incomplete_value": true,
      "site": "00b5a92c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b5a834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a90c"
      ]
    ],
    [
      "00b5a920",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a920",
      "PARAM",
      [
        "storage",
        "00b5a92c",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5a8fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a90c"
      ]
    ],
    [
      "00b5a920",
      "READ",
      [
        "storage",
        "00c1baa0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a920",
      "PARAM",
      [
        "storage",
        "00b5a9f4",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a814.md#insn-00b5a834) · [`00b5a864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a814.md#insn-00b5a864)
- 新版 `00b5a92c`（命令位置の公開資料なし） · `00b5a8fc`（命令位置の公開資料なし）

~~~diff
- 00b5a834 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5a834 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5a834 bytes 880000b4
- 00b5a864 ["INT_ADD", "register:40f0:8", ["const:b5a864:8", "const:4:8"]]
- 00b5a864 ["CALL", null, ["callee:00bddd50:8"]]
+ 00b5a92c ["INT_ADD", "register:40f0:8", ["const:b5a92c:8", "const:4:8"]]
+ 00b5a92c ["CALL", null, ["callee:00bddd50:8"]]
- 00b5a864 bytes 0f0d0294
+ 00b5a92c bytes 090d0294
+ 00b5a8fc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5a8fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5a8fc bytes 880000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d15cd574bb50678832ccb78e84fbeabe"></a>

### [`00b5aab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aab0.md) → [`00b5ab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda70.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md)
- 新版 呼出元 1件 [`00bddb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb20.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 68.63% / 新版 67.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ac80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5ad48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5abc4",
      "incomplete_value": true,
      "site": "00b5abc4",
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
      "definition_site": "00b5aafc",
      "incomplete_value": true,
      "site": "00b5aafc",
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
      "00b5ab94",
      "READ",
      [
        "storage",
        "00c1ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00b5aba0",
      "READ",
      [
        "storage",
        "010a1318",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5abac",
      "READ",
      [
        "storage",
        "010a1318",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ab94",
      "READ",
      [
        "storage",
        "00c1bb20",
        null,
        "pointer"
      ]
    ],
    [
      "00b5aba0",
      "READ",
      [
        "storage",
        "010a13d8",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5abac",
      "READ",
      [
        "storage",
        "010a13d8",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5aae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aab0.md#insn-00b5aae0) · [`00b5aafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aab0.md#insn-00b5aafc) · [`00b5ab10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aab0.md#insn-00b5ab10)
- 新版 `00b5aba8`（命令位置の公開資料なし） · `00b5abc4`（命令位置の公開資料なし）

~~~diff
- 00b5aae0 ["INT_ADD", "register:40f0:8", ["const:b5aae0:8", "const:4:8"]]
- 00b5aae0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5aba8 ["INT_ADD", "register:40f0:8", ["const:b5aba8:8", "const:4:8"]]
+ 00b5aba8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5aae0 bytes 100c0294
+ 00b5aba8 bytes 0a0c0294
- 00b5aafc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5aafc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b5abc4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5abc4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5aafc bytes c90100b4
+ 00b5abc4 bytes c90100b4
- 00b5ab10 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b5ab10 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b5ab10 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b5ab10 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b5ab10 bytes 0831899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1363f5f71d95dd0dbb4f9a6283faa4e"></a>

### [`00b5accc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5accc.md) → [`00b5ad94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ad94.md) _ZN8firebase4auth4Auth8FindAuthEPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 53.85% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5adc4",
      "incomplete_value": true,
      "site": "00b5adc4",
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
      "definition_site": "00b5acfc",
      "incomplete_value": true,
      "site": "00b5acfc",
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
      "definition_site": "00b5adb0",
      "incomplete_value": true,
      "site": "00b5adb4",
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ad4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ada4",
      "READ",
      [
        "storage",
        "00c1ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00b5adac",
      "READ",
      [
        "storage",
        "010a1318",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5adbc",
      "READ",
      [
        "storage",
        "00c1ba78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5ada4",
      "READ",
      [
        "storage",
        "00c1bb20",
        null,
        "pointer"
      ]
    ],
    [
      "00b5adac",
      "READ",
      [
        "storage",
        "010a13d8",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5adbc",
      "READ",
      [
        "storage",
        "00c1bb28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5acec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5accc.md#insn-00b5acec) · [`00b5acfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5accc.md#insn-00b5acfc) · [`00b5ad4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5accc.md#insn-00b5ad4c)
- 新版 `00b5adb4`（命令位置の公開資料なし） · `00b5adc4`（命令位置の公開資料なし）

~~~diff
- 00b5acec ["INT_ADD", "register:40f0:8", ["const:b5acec:8", "const:4:8"]]
- 00b5acec ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5adb4 ["INT_ADD", "register:40f0:8", ["const:b5adb4:8", "const:4:8"]]
+ 00b5adb4 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5acec bytes 8d0b0294
+ 00b5adb4 bytes 870b0294
- 00b5acfc ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b5acfc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b5adc4 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b5adc4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5acfc bytes ca0100b4
+ 00b5adc4 bytes ca0100b4
- 00b5ad4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5ad4c ["RETURN", null, ["register:0:8"]]
- 00b5ad4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-962c1468e0e1f2e37210774cd06a2fdc"></a>

### [`00b5ad5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ad5c.md) → [`00b5ae24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md) _ZN8firebase4auth4AuthC2EPNS_3AppEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0990.md) · 呼出先 10件 [`00b5c378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c378.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md)
- 新版 呼出元 1件 [`00be0a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a40.md) · 呼出先 10件 [`00b5c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ad8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ae24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5ae54"
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
      "unmatched:00b5ad8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5adac",
      "PARAM",
      [
        "storage",
        "0029efa7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5add0",
      "PARAM",
      [
        "storage",
        "002ab1a6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5ae54",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b5ae74",
      "PARAM",
      [
        "storage",
        "0029f034",
        null,
        "string"
      ]
    ],
    [
      "00b5ae98",
      "PARAM",
      [
        "storage",
        "002ab1ac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ad8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ad5c.md#insn-00b5ad8c) · [`00b5adb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ad5c.md#insn-00b5adb0) · [`00b5adc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ad5c.md#insn-00b5adc8)
- 新版 `00b5ae78`（命令位置の公開資料なし） · `00b5ae90`（命令位置の公開資料なし）

~~~diff
- 00b5ad8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5ad8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5ad8c bytes e80f00f9
- 00b5adb0 ["INT_ADD", "register:40f0:8", ["const:b5adb0:8", "const:4:8"]]
- 00b5adb0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5ae78 ["INT_ADD", "register:40f0:8", ["const:b5ae78:8", "const:4:8"]]
+ 00b5ae78 ["CALL", null, ["callee:00bde130:8"]]
- 00b5adb0 bytes b40c0294
+ 00b5ae78 bytes ae0c0294
- 00b5adc8 ["INT_ADD", "register:40f0:8", ["const:b5adc8:8", "const:4:8"]]
- 00b5adc8 ["CALL", null, ["callee:00be09f0:8"]]
+ 00b5ae90 ["INT_ADD", "register:40f0:8", ["const:b5ae90:8", "const:4:8"]]
+ 00b5ae90 ["CALL", null, ["callee:00be09f0:8"]]
- 00b5adc8 bytes de160294
+ 00b5ae90 bytes d8160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05365ac769f557d659cb629b54fe31fa"></a>

### [`00b5ae80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ae80.md) → [`00b5af48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5af48.md) _ZN8firebase4auth8AuthDataC2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be09a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09a0.md) · 呼出先 3件 [`00bddce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddce0.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md) [`00be08b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08b0.md)
- 新版 呼出元 1件 [`00be0a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a50.md) · 呼出先 3件 [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) [`00be0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0960.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.41% / 新版 57.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ae80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ae80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ae84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5ae80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5ae84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5ae88",
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
      "00b5af48",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5af4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5af50",
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

- 旧版 [`00b5ae80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ae80.md#insn-00b5ae80) · [`00b5ae84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ae80.md#insn-00b5ae84) · [`00b5ae88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ae80.md#insn-00b5ae88)

~~~diff
- 00b5ae80 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5ae80 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5ae80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5ae80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5ae80 bytes f85fbca9
- 00b5ae84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5ae84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5ae84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5ae84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5ae84 bytes f65701a9
- 00b5ae88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5ae88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5ae88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5ae88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5ae88 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36e54fe5bca500309dac0dfcc30b6a9"></a>

### [`00b5b008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b008.md) → [`00b5b0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b0d0.md) _ZN8firebase4auth4Auth14DeleteInternalEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0930.md) · 呼出先 14件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00be09e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09e0.md) · 呼出先 14件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.67% / 新版 84.67%

CFGの説明率　旧版 66.07% / 新版 71.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b00c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b008",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b010",
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
      "00b5b0d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b0d8",
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

- 旧版 [`00b5b008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b008.md#insn-00b5b008) · [`00b5b00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b008.md#insn-00b5b00c) · [`00b5b010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b008.md#insn-00b5b010)

~~~diff
- 00b5b008 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5b008 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b008 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5b008 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5b008 bytes f657bda9
- 00b5b00c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b00c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b00c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5b00c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b00c bytes f44f01a9
- 00b5b010 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5b010 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5b010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5b010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b010 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-581031a01d3782b54fc0d6449a0ccf69"></a>

### [`00b5b3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b3c8.md) → [`00b5b490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b490.md) _ZN8firebase4auth4Auth3appEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0980.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00be0a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a30.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b4ac",
      "incomplete_value": false,
      "site": "00b5b4b0",
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
            "const:ff1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b3e4",
      "incomplete_value": false,
      "site": "00b5b3e8",
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
            "const:f64:8"
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
      "00b5b4ac",
      "PARAM",
      [
        "storage",
        "002a0f64",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5b4ac",
      "PARAM",
      [
        "storage",
        "002a0ff1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b3c8.md#insn-00b5b3e8) · [`00b5b3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b3c8.md#insn-00b5b3e4)
- 新版 `00b5b4b0`（命令位置の公開資料なし） · `00b5b4ac`（命令位置の公開資料なし）

~~~diff
- 00b5b3e8 ["INT_ADD", "register:40f0:8", ["const:b5b3e8:8", "const:4:8"]]
- 00b5b3e8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5b4b0 ["INT_ADD", "register:40f0:8", ["const:b5b4b0:8", "const:4:8"]]
+ 00b5b4b0 ["CALL", null, ["callee:00bde130:8"]]
- 00b5b3e8 bytes 260b0294
+ 00b5b4b0 bytes 200b0294
- 00b5b3e4 ["COPY", "tmp:0:8", ["const:f64:8"]]
- 00b5b3e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b3e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b3e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4ac ["COPY", "tmp:0:8", ["const:ff1:8"]]
+ 00b5b4ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5b3e4 bytes 00903d91
+ 00b5b4ac bytes 00c43f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09e899d737030403f1b0fa24dd551b3b"></a>

### [`00b5b400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b400.md) → [`00b5b4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b4c8.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00be09f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0aa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b640",
      "incomplete_value": false,
      "site": "00b5b644",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b578",
      "incomplete_value": false,
      "site": "00b5b57c",
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
            "const:f84:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5b640",
      "PARAM",
      [
        "storage",
        "002a7f84",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5b640",
      "PARAM",
      [
        "storage",
        "002a7ef0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b400.md#insn-00b5b57c) · [`00b5b43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b400.md#insn-00b5b43c) · [`00b5b4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b400.md#insn-00b5b4c0)
- 新版 `00b5b644`（命令位置の公開資料なし） · `00b5b504`（命令位置の公開資料なし） · `00b5b588`（命令位置の公開資料なし）

~~~diff
- 00b5b57c ["INT_ADD", "register:40f0:8", ["const:b5b57c:8", "const:4:8"]]
- 00b5b57c ["CALL", null, ["callee:00bde130:8"]]
+ 00b5b644 ["INT_ADD", "register:40f0:8", ["const:b5b644:8", "const:4:8"]]
+ 00b5b644 ["CALL", null, ["callee:00bde130:8"]]
- 00b5b57c bytes c10a0294
+ 00b5b644 bytes bb0a0294
- 00b5b43c ["INT_ADD", "register:40f0:8", ["const:b5b43c:8", "const:4:8"]]
- 00b5b43c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5b504 ["INT_ADD", "register:40f0:8", ["const:b5b504:8", "const:4:8"]]
+ 00b5b504 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5b43c bytes b9090294
+ 00b5b504 bytes b3090294
- 00b5b4c0 ["INT_ADD", "register:40f0:8", ["const:b5b4c0:8", "const:4:8"]]
- 00b5b4c0 ["CALL", null, ["callee:00be0aa0:8"]]
+ 00b5b588 ["INT_ADD", "register:40f0:8", ["const:b5b588:8", "const:4:8"]]
+ 00b5b588 ["CALL", null, ["callee:00be0aa0:8"]]
- 00b5b4c0 bytes 4c150294
+ 00b5b588 bytes 46150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c478e88450270ce3033e0818e8924e"></a>

### [`00b5b5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b5d0.md) → [`00b5b698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b698.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00be08e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0990.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 82.69% / 新版 79.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b76c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5b7c0"
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
      "unmatched:00b5b6f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b7d8"
      ]
    ],
    [
      "00b5b818",
      "PARAM",
      [
        "storage",
        "002a7f84",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5b76c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b850"
      ]
    ]
  ],
  "added": [
    [
      "00b5b7c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b7d8"
      ]
    ],
    [
      "00b5b818",
      "PARAM",
      [
        "storage",
        "002a7ef0",
        null,
        "string"
      ]
    ],
    [
      "00b5b834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b850"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b5d0.md#insn-00b5b6f8) · [`00b5b754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b5d0.md#insn-00b5b754) · [`00b5b76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b5d0.md#insn-00b5b76c)
- 新版 `00b5b81c`（命令位置の公開資料なし）

~~~diff
- 00b5b6f8 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00b5b6f8 bytes c0000054
- 00b5b754 ["INT_ADD", "register:40f0:8", ["const:b5b754:8", "const:4:8"]]
- 00b5b754 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5b81c ["INT_ADD", "register:40f0:8", ["const:b5b81c:8", "const:4:8"]]
+ 00b5b81c ["CALL", null, ["callee:00bde130:8"]]
- 00b5b754 bytes 4b0a0294
+ 00b5b81c bytes 450a0294
- 00b5b76c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5b76c ["CBRANCH", null, ["local:b33:8", "tmp:0:1"]]
- 00b5b76c bytes e1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-900b87deaebf1c6fbb50a105ac16a3a5"></a>

### [`00b5b8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b8bc.md) → [`00b5b984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b984.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0960.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00be0900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0900.md)
- 新版 呼出元 1件 [`00be0a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a10.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be09b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 57.89% / 新版 62.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b8d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b944"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b8d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bac8"
      ]
    ],
    [
      "unmatched:00b5b944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ba1c"
      ]
    ],
    [
      "unmatched:00b5b980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ba88"
      ]
    ]
  ],
  "added": [
    [
      "00b5b99c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bac8"
      ]
    ],
    [
      "00b5ba0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ba1c"
      ]
    ],
    [
      "00b5ba48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5ba88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b8bc.md#insn-00b5b8d4) · [`00b5b944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b8bc.md#insn-00b5b944) · [`00b5b980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b8bc.md#insn-00b5b980)

~~~diff
- 00b5b8d4 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00b5b8d4 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00b5b8d4 bytes 780900b4
- 00b5b944 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b5b944 bytes 80000054
- 00b5b980 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 00b5b980 bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41928b3b334b00698a681096b30a3f2f"></a>

### [`00b5ba8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5ba8c.md) → [`00b5bb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bb54.md) FUN_00b5bb54

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ba94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5bb5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b5ba94"
      ],
      [
        "FALL_THROUGH",
        "00b5bb5c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b5bb5c",
      "incomplete_value": true,
      "site": "00b5bb60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ba94",
      "incomplete_value": true,
      "site": "00b5ba98",
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
              [
                "live",
                "register:4000:8"
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
      "unmatched:00b5ba94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bb68"
      ]
    ]
  ],
  "added": [
    [
      "00b5bb5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bb68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ba94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5ba8c.md#insn-00b5ba94) · [`00b5ba8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5ba8c.md#insn-00b5ba8c)
- 新版 `00b5bb5c`（命令位置の公開資料なし）

~~~diff
- 00b5ba94 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b5ba94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5ba94 bytes 600000b4
+ 00b5bb5c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b5bb5c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5bb5c bytes 600000b4
- 00b5ba8c ["COPY", "register:4040:8", ["register:4000:8"]]
- 00b5ba8c bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57af163d3fe49b82bd168f0d514526b"></a>

### [`00b5baa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5baa8.md) → [`00b5bb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bb70.md) _ZN8firebase4auth15IdTokenListenerD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0960.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5bb90",
      "incomplete_value": true,
      "site": "00b5bb90",
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
      "definition_site": "00b5bac8",
      "incomplete_value": true,
      "site": "00b5bac8",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5bb9c"
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
      "00b5bb80",
      "READ",
      [
        "storage",
        "00c1ba80",
        null,
        "pointer"
      ]
    ],
    [
      "00b5bb90",
      "DATA",
      [
        "storage",
        "00c11a58",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "unmatched:00b5bad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bbb0"
      ]
    ]
  ],
  "added": [
    [
      "00b5bb80",
      "READ",
      [
        "storage",
        "00c1bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00b5bb90",
      "DATA",
      [
        "storage",
        "00c11b08",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00b5bb9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bbb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5baa8.md#insn-00b5bad4) · [`00b5bab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5baa8.md#insn-00b5bab8)
- 新版 `00b5bb9c`（命令位置の公開資料なし） · `00b5bb80`（命令位置の公開資料なし）

~~~diff
- 00b5bad4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b5bad4 bytes a0000054
+ 00b5bb9c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b5bb9c bytes a0000054
- 00b5bab8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a80:8"]]
- 00b5bab8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5bb80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00b5bb80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5bab8 bytes 084145f9
+ 00b5bb80 bytes 089945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171d810a09772a0aea6941671cc10ccc"></a>

### [`00b5bb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bb20.md) → [`00b5bbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bbe8.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0910.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be09c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09c0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bc20",
      "incomplete_value": true,
      "site": "00b5bc24",
      "value": [
        "live",
        "register:8:8"
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
      "definition_site": "00b5bc18",
      "incomplete_value": true,
      "site": "00b5bc24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "definition_site": "00b5bc38",
      "incomplete_value": false,
      "site": "00b5bc3c",
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
            "const:372:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bb70",
      "incomplete_value": false,
      "site": "00b5bb74",
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
            "const:37b:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b5bb70",
      "PARAM",
      [
        "storage",
        "002ac37b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5bc38",
      "PARAM",
      [
        "storage",
        "002ac372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bb20.md#insn-00b5bb5c) · [`00b5bb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bb20.md#insn-00b5bb74) · [`00b5bb4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bb20.md#insn-00b5bb4c)
- 新版 `00b5bc24`（命令位置の公開資料なし） · `00b5bc3c`（命令位置の公開資料なし） · `00b5bc14`（命令位置の公開資料なし）

~~~diff
- 00b5bb5c ["INT_ADD", "register:40f0:8", ["const:b5bb5c:8", "const:4:8"]]
- 00b5bb5c ["CALL", null, ["callee:00be0ab0:8"]]
+ 00b5bc24 ["INT_ADD", "register:40f0:8", ["const:b5bc24:8", "const:4:8"]]
+ 00b5bc24 ["CALL", null, ["callee:00be0ab0:8"]]
- 00b5bb5c bytes a9130294
+ 00b5bc24 bytes a3130294
- 00b5bb74 ["INT_ADD", "register:40f0:8", ["const:b5bb74:8", "const:4:8"]]
- 00b5bb74 ["CALL", null, ["callee:00bde260:8"]]
+ 00b5bc3c ["INT_ADD", "register:40f0:8", ["const:b5bc3c:8", "const:4:8"]]
+ 00b5bc3c ["CALL", null, ["callee:00bde260:8"]]
- 00b5bb74 bytes 8f090294
+ 00b5bc3c bytes 89090294
- 00b5bb4c ["INT_ADD", "register:40f0:8", ["const:b5bb4c:8", "const:4:8"]]
- 00b5bb4c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5bc14 ["INT_ADD", "register:40f0:8", ["const:b5bc14:8", "const:4:8"]]
+ 00b5bc14 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5bb4c bytes f5070294
+ 00b5bc14 bytes ef070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7471517b3fabf583abd9e9b36088e3dd"></a>

### [`00b5bd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bd48.md) → [`00b5be10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5be10.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be08f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08f0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be09a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09a0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 58.06% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bdd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5be08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5be98"
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
      "unmatched:00b5bd98",
      "PARAM",
      [
        "storage",
        "002965d8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5bdd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bf3c"
      ]
    ],
    [
      "unmatched:00b5be08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bf0c"
      ]
    ]
  ],
  "added": [
    [
      "00b5be60",
      "PARAM",
      [
        "storage",
        "00296665",
        null,
        "string"
      ]
    ],
    [
      "00b5be98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bf3c"
      ]
    ],
    [
      "00b5bed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bf0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bd84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bd48.md#insn-00b5bd84) · [`00b5bd9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bd48.md#insn-00b5bd9c) · [`00b5bdd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bd48.md#insn-00b5bdd0)
- 新版 `00b5be4c`（命令位置の公開資料なし） · `00b5be64`（命令位置の公開資料なし）

~~~diff
- 00b5bd84 ["INT_ADD", "register:40f0:8", ["const:b5bd84:8", "const:4:8"]]
- 00b5bd84 ["CALL", null, ["callee:00be0a90:8"]]
+ 00b5be4c ["INT_ADD", "register:40f0:8", ["const:b5be4c:8", "const:4:8"]]
+ 00b5be4c ["CALL", null, ["callee:00be0a90:8"]]
- 00b5bd84 bytes 17130294
+ 00b5be4c bytes 11130294
- 00b5bd9c ["INT_ADD", "register:40f0:8", ["const:b5bd9c:8", "const:4:8"]]
- 00b5bd9c ["CALL", null, ["callee:00bde260:8"]]
+ 00b5be64 ["INT_ADD", "register:40f0:8", ["const:b5be64:8", "const:4:8"]]
+ 00b5be64 ["CALL", null, ["callee:00bde260:8"]]
- 00b5bd9c bytes 05090294
+ 00b5be64 bytes ff080294
- 00b5bdd0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5bdd0 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b5bdd0 bytes 21050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4968113d00da3b7ab36e4934f800f730"></a>

### [`00b5bf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bf70.md) → [`00b5c038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c038.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c084",
      "incomplete_value": true,
      "site": "00b5c08c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bfc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bf70.md#insn-00b5bfc4) · [`00b5bf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bf70.md#insn-00b5bf90) · [`00b5bf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bf70.md#insn-00b5bf9c)
- 新版 `00b5c08c`（命令位置の公開資料なし） · `00b5c058`（命令位置の公開資料なし） · `00b5c064`（命令位置の公開資料なし）

~~~diff
- 00b5bfc4 ["INT_ADD", "register:40f0:8", ["const:b5bfc4:8", "const:4:8"]]
- 00b5bfc4 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b5c08c ["INT_ADD", "register:40f0:8", ["const:b5c08c:8", "const:4:8"]]
+ 00b5c08c ["CALL", null, ["callee:00bddea0:8"]]
- 00b5bfc4 bytes 8b070294
+ 00b5c08c bytes 85070294
- 00b5bf90 ["INT_ADD", "register:40f0:8", ["const:b5bf90:8", "const:4:8"]]
- 00b5bf90 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5c058 ["INT_ADD", "register:40f0:8", ["const:b5c058:8", "const:4:8"]]
+ 00b5c058 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5bf90 bytes e4060294
+ 00b5c058 bytes de060294
- 00b5bf9c ["INT_ADD", "register:40f0:8", ["const:b5bf9c:8", "const:4:8"]]
- 00b5bf9c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b5c064 ["INT_ADD", "register:40f0:8", ["const:b5c064:8", "const:4:8"]]
+ 00b5c064 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b5bf9c bytes e5060294
+ 00b5c064 bytes df060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

