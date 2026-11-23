# v15.7.3 → v15.7.4 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-58b895b02d1145f9551b235747583df0"></a>

### [`00b63b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md) → [`00b63b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b58.md) _ZN8firebase4auth27too_many_requests_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63b74",
      "incomplete_value": false,
      "site": "00b63b78",
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
    "old": {
      "definition_site": "00b63b30",
      "incomplete_value": false,
      "site": "00b63b34",
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
      "00b63b74",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b63b84",
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
      "00b63b74",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b63b84",
      "DATA",
      [
        "storage",
        "010a1718",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md#insn-00b63b34) · [`00b63b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md#insn-00b63b30) · [`00b63b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md#insn-00b63b3c)
- 新版 `00b63b78`（命令位置の公開資料なし） · `00b63b74`（命令位置の公開資料なし） · `00b63b80`（命令位置の公開資料なし）

~~~diff
- 00b63b34 ["INT_ADD", "register:40f0:8", ["const:b63b34:8", "const:4:8"]]
- 00b63b34 ["CALL", null, ["callee:00bde180:8"]]
+ 00b63b78 ["INT_ADD", "register:40f0:8", ["const:b63b78:8", "const:4:8"]]
+ 00b63b78 ["CALL", null, ["callee:00bde180:8"]]
- 00b63b34 bytes 7fe90194
+ 00b63b78 bytes 82e90194
- 00b63b30 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b63b30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63b30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63b30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63b74 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b63b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63b30 bytes 00fc1991
+ 00b63b74 bytes 00c81791
- 00b63b3c ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00b63b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63b80 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00b63b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63b3c bytes 08611b91
+ 00b63b80 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e990be3182ac4fdcc8b3ddc5cfcb14d"></a>

### [`00b63b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b50.md) → [`00b63b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b94.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b63b7c",
      "incomplete_value": true,
      "site": "00b63b7c",
      "value": [
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
    "old": {
      "definition_site": "00b63b64",
      "incomplete_value": true,
      "site": "00b63b64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b63b70",
      "incomplete_value": false,
      "site": "00b63b74",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63ba4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bb4",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63bc0",
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
      "00b63ba4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bb4",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63bc0",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b50.md#insn-00b63b74) · [`00b63b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b50.md#insn-00b63b7c) · [`00b63b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b50.md#insn-00b63b60)
- 新版 `00b63bb8`（命令位置の公開資料なし） · `00b63bc0`（命令位置の公開資料なし） · `00b63ba4`（命令位置の公開資料なし）

~~~diff
- 00b63b74 ["INT_ADD", "register:40f0:8", ["const:b63b74:8", "const:4:8"]]
- 00b63b74 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63bb8 ["INT_ADD", "register:40f0:8", ["const:b63bb8:8", "const:4:8"]]
+ 00b63bb8 ["CALL", null, ["callee:00bde090:8"]]
- 00b63b74 bytes 33e90194
+ 00b63bb8 bytes 36e90194
- 00b63b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63b7c bytes 607203f9
+ 00b63bc0 bytes 609203f9
- 00b63b60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63ba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63ba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63b60 bytes 687243f9
+ 00b63ba4 bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e298b17b973b7d7d37b2a20c3fa708"></a>

### [`00b63b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b90.md) → [`00b63bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63bd4.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b63bbc",
      "incomplete_value": true,
      "site": "00b63bbc",
      "value": [
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
    "old": {
      "definition_site": "00b63ba4",
      "incomplete_value": true,
      "site": "00b63ba4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b63bac",
      "incomplete_value": false,
      "site": "00b63bb4",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63be4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bf0",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63c00",
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
      "00b63be4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bf0",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63c00",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b90.md#insn-00b63bb4) · [`00b63bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b90.md#insn-00b63bbc) · [`00b63ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b90.md#insn-00b63ba0)
- 新版 `00b63bf8`（命令位置の公開資料なし） · `00b63c00`（命令位置の公開資料なし） · `00b63be4`（命令位置の公開資料なし）

~~~diff
- 00b63bb4 ["INT_ADD", "register:40f0:8", ["const:b63bb4:8", "const:4:8"]]
- 00b63bb4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63bf8 ["INT_ADD", "register:40f0:8", ["const:b63bf8:8", "const:4:8"]]
+ 00b63bf8 ["CALL", null, ["callee:00bde090:8"]]
- 00b63bb4 bytes 23e90194
+ 00b63bf8 bytes 26e90194
- 00b63bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63bbc bytes 607203f9
+ 00b63c00 bytes 609203f9
- 00b63ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63be4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63be4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63ba0 bytes 687243f9
+ 00b63be4 bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04eb3324ed5b79f9da05c17f49b124da"></a>

### [`00b63bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63bd0.md) → [`00b63c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c14.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b63c44",
      "incomplete_value": true,
      "site": "00b63c44",
      "value": [
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
      "definition_site": "00b63c28",
      "incomplete_value": true,
      "site": "00b63c28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63be4",
      "incomplete_value": true,
      "site": "00b63be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63c34",
      "incomplete_value": false,
      "site": "00b63c3c",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63c24",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c34",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63c44",
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
      "00b63c24",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c34",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63c44",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63bd0.md#insn-00b63bf8) · [`00b63c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63bd0.md#insn-00b63c00) · [`00b63be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63bd0.md#insn-00b63be0)
- 新版 `00b63c3c`（命令位置の公開資料なし） · `00b63c44`（命令位置の公開資料なし） · `00b63c24`（命令位置の公開資料なし）

~~~diff
- 00b63bf8 ["INT_ADD", "register:40f0:8", ["const:b63bf8:8", "const:4:8"]]
- 00b63bf8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63c3c ["INT_ADD", "register:40f0:8", ["const:b63c3c:8", "const:4:8"]]
+ 00b63c3c ["CALL", null, ["callee:00bde090:8"]]
- 00b63bf8 bytes 12e90194
+ 00b63c3c bytes 15e90194
- 00b63c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63c00 bytes 607203f9
+ 00b63c44 bytes 609203f9
- 00b63be0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63be0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63c24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63c24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63be0 bytes 687243f9
+ 00b63c24 bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61993d09bb40af9061523e508351b537"></a>

### [`00b63c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c14.md) → [`00b63c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c58.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b63c44",
      "incomplete_value": true,
      "site": "00b63c44",
      "value": [
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
    "old": {
      "definition_site": "00b63c28",
      "incomplete_value": true,
      "site": "00b63c28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b63c30",
      "incomplete_value": false,
      "site": "00b63c3c",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63c68",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c74",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63c88",
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
      "00b63c68",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c74",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63c88",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c14.md#insn-00b63c3c) · [`00b63c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c14.md#insn-00b63c44) · [`00b63c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c14.md#insn-00b63c24)
- 新版 `00b63c80`（命令位置の公開資料なし） · `00b63c88`（命令位置の公開資料なし） · `00b63c68`（命令位置の公開資料なし）

~~~diff
- 00b63c3c ["INT_ADD", "register:40f0:8", ["const:b63c3c:8", "const:4:8"]]
- 00b63c3c ["CALL", null, ["callee:00bde090:8"]]
+ 00b63c80 ["INT_ADD", "register:40f0:8", ["const:b63c80:8", "const:4:8"]]
+ 00b63c80 ["CALL", null, ["callee:00bde090:8"]]
- 00b63c3c bytes 01e90194
+ 00b63c80 bytes 04e90194
- 00b63c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63c44 bytes 607203f9
+ 00b63c88 bytes 609203f9
- 00b63c24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63c24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b63c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63c24 bytes 687243f9
+ 00b63c68 bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb2ca491dcf7d31ebd4cd34dee3ccd4f"></a>

### [`00b63c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c64.md) → [`00b63ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ca8.md) _ZN8firebase4auth18firebase_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b63cbc",
      "incomplete_value": true,
      "site": "00b63cbc",
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
    "old": {
      "definition_site": "00b63c98",
      "incomplete_value": true,
      "site": "00b63ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b63cbc",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63cdc",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63d00",
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
      "00b63cbc",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63cdc",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63d00",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c64.md#insn-00b63c78) · [`00b63ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c64.md#insn-00b63ca4) · [`00b63cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c64.md#insn-00b63cbc)
- 新版 `00b63cbc`（命令位置の公開資料なし） · `00b63ce8`（命令位置の公開資料なし） · `00b63d00`（命令位置の公開資料なし）

~~~diff
- 00b63c78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e8:8"]]
- 00b63c78 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b63c78 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b63cbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 00b63cbc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b63cbc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b63c78 bytes a8a25b39
+ 00b63cbc bytes a8a25c39
- 00b63ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63ca4 ["INT_ADD", "register:40f0:8", ["const:b63ca4:8", "const:4:8"]]
- 00b63ca4 ["CALLIND", null, ["register:0:8"]]
+ 00b63ce8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63ce8 ["INT_ADD", "register:40f0:8", ["const:b63ce8:8", "const:4:8"]]
+ 00b63ce8 ["CALLIND", null, ["register:0:8"]]
- 00b63ca4 bytes 00013fd6
+ 00b63ce8 bytes 00013fd6
- 00b63cbc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63cbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e8:8"]]
- 00b63cbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b63d00 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b63d00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:728:8"]]
+ 00b63d00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63cbc bytes a0a21b39
+ 00b63d00 bytes a0a21c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-843d7b3dfb832e3b2cc043ceb7a4d874"></a>

### [`00b63cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63cd0.md) → [`00b63d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d14.md) _ZN8firebase4auth18firebase_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b63d50",
      "incomplete_value": true,
      "site": "00b63d50",
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
    "old": {
      "definition_site": "00b63d0c",
      "incomplete_value": true,
      "site": "00b63d0c",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b63d70",
      "incomplete_value": true,
      "site": "00b63d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63d2c",
      "incomplete_value": true,
      "site": "00b63d2c",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63d2c",
      "incomplete_value": true,
      "site": "00b63d2c",
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
      "definition_site": "00b63ce8",
      "incomplete_value": true,
      "site": "00b63ce8",
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
      "00b63d28",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63d34",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63d50",
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
      "00b63d28",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63d34",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63d50",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63cd0.md#insn-00b63ce4) · [`00b63d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63cd0.md#insn-00b63d0c) · [`00b63d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63cd0.md#insn-00b63d28)
- 新版 `00b63d28`（命令位置の公開資料なし） · `00b63d50`（命令位置の公開資料なし） · `00b63d6c`（命令位置の公開資料なし）

~~~diff
- 00b63ce4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63ce4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63d28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b63d28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63ce4 bytes 817243f9
+ 00b63d28 bytes 819243f9
- 00b63d0c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b63d0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b63d0c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6e8:8"]]
- 00b63d0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b63d50 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b63d50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b63d50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:728:8"]]
+ 00b63d50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b63d0c bytes bfa21b39
+ 00b63d50 bytes bfa21c39
- 00b63d28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63d28 ["INT_ADD", "register:40f0:8", ["const:b63d28:8", "const:4:8"]]
- 00b63d28 ["CALLIND", null, ["register:0:8"]]
+ 00b63d6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63d6c ["INT_ADD", "register:40f0:8", ["const:b63d6c:8", "const:4:8"]]
+ 00b63d6c ["CALLIND", null, ["register:0:8"]]
- 00b63d28 bytes 00013fd6
+ 00b63d6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fc5e1f0c10a4483da12c599c4e1bb2"></a>

### [`00b63d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63d40.md) → [`00b63d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d84.md) _ZN8firebase4auth18firebase_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b63dc4",
      "incomplete_value": true,
      "site": "00b63dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63d80",
      "incomplete_value": true,
      "site": "00b63d80",
      "value": [
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
      "definition_site": "00b63da0",
      "incomplete_value": true,
      "site": "00b63da0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63d5c",
      "incomplete_value": true,
      "site": "00b63d5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63da8",
      "incomplete_value": false,
      "site": "00b63dbc",
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
    "old": {
      "definition_site": "00b63d64",
      "incomplete_value": false,
      "site": "00b63d78",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63d98",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63da8",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63dc4",
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
      "00b63d98",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63da8",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63dc4",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63d40.md#insn-00b63d78) · [`00b63d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63d40.md#insn-00b63d80) · [`00b63d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63d40.md#insn-00b63d54)
- 新版 `00b63dbc`（命令位置の公開資料なし） · `00b63dc4`（命令位置の公開資料なし） · `00b63d98`（命令位置の公開資料なし）

~~~diff
- 00b63d78 ["INT_ADD", "register:40f0:8", ["const:b63d78:8", "const:4:8"]]
- 00b63d78 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63dbc ["INT_ADD", "register:40f0:8", ["const:b63dbc:8", "const:4:8"]]
+ 00b63dbc ["CALL", null, ["callee:00bde090:8"]]
- 00b63d78 bytes b2e80194
+ 00b63dbc bytes b5e80194
- 00b63d80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63dc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b63dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63d80 bytes 807203f9
+ 00b63dc4 bytes 809203f9
- 00b63d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63d54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63d98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b63d98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63d54 bytes 817243f9
+ 00b63d98 bytes 819243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b9c441b5d66c9697bbbd14d07d738a"></a>

### [`00b63db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md) → [`00b63df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63df4.md) _ZN8firebase4auth18firebase_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63e10",
      "incomplete_value": false,
      "site": "00b63e14",
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
    "old": {
      "definition_site": "00b63dcc",
      "incomplete_value": false,
      "site": "00b63dd0",
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
      "00b63e10",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63e20",
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
      "00b63e10",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63e20",
      "DATA",
      [
        "storage",
        "010a1730",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md#insn-00b63dd0) · [`00b63dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md#insn-00b63dcc) · [`00b63dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md#insn-00b63dd8)
- 新版 `00b63e14`（命令位置の公開資料なし） · `00b63e10`（命令位置の公開資料なし） · `00b63e1c`（命令位置の公開資料なし）

~~~diff
- 00b63dd0 ["INT_ADD", "register:40f0:8", ["const:b63dd0:8", "const:4:8"]]
- 00b63dd0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b63e14 ["INT_ADD", "register:40f0:8", ["const:b63e14:8", "const:4:8"]]
+ 00b63e14 ["CALL", null, ["callee:00bde180:8"]]
- 00b63dd0 bytes d8e80194
+ 00b63e14 bytes dbe80194
- 00b63dcc ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b63dcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63dcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63dcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63e10 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b63e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63dcc bytes 00501791
+ 00b63e10 bytes 001c1591
- 00b63dd8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 00b63dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63e1c ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00b63e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63dd8 bytes 08c11b91
+ 00b63e1c bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e34d48001d04bc45dc2cf278cebad5c9"></a>

### [`00b63dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63dec.md) → [`00b63e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63e30.md) _ZN8firebase4auth18firebase_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b63e70",
      "incomplete_value": true,
      "site": "00b63e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63e2c",
      "incomplete_value": true,
      "site": "00b63e2c",
      "value": [
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
      "definition_site": "00b63e4c",
      "incomplete_value": true,
      "site": "00b63e4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63e08",
      "incomplete_value": true,
      "site": "00b63e08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63e08"
      ],
      [
        "FALL_THROUGH",
        "00b63e4c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63e4c",
      "incomplete_value": true,
      "site": "00b63e70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63e08",
      "incomplete_value": true,
      "site": "00b63e2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63e44",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63e54",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63e70",
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
      "00b63e44",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63e54",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63e70",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63dec.md#insn-00b63e2c) · [`00b63e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63dec.md#insn-00b63e00) · [`00b63e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63dec.md#insn-00b63e10)
- 新版 `00b63e70`（命令位置の公開資料なし） · `00b63e44`（命令位置の公開資料なし） · `00b63e54`（命令位置の公開資料なし）

~~~diff
- 00b63e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63e70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b63e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63e2c bytes 807203f9
+ 00b63e70 bytes 809203f9
- 00b63e00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63e00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63e44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b63e44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63e00 bytes 817243f9
+ 00b63e44 bytes 819243f9
- 00b63e10 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00b63e10 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b63e10 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b63e10 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b63e54 ["COPY", "tmp:0:8", ["const:483:8"]]
+ 00b63e54 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b63e54 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b63e54 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b63e10 bytes 63401491
+ 00b63e54 bytes 630c1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25dbb6ddfe9708e595925eea7c744a8"></a>

### [`00b63e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e5c.md) → [`00b63ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ea0.md) _ZN8firebase4auth18firebase_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b63e78",
      "incomplete_value": false,
      "site": "00b63e7c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b63e88",
      "incomplete_value": true,
      "site": "00b63e94",
      "value": [
        "LOAD",
        "8",
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
      "00b63ebc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b63ecc",
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
      "00b63ebc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b63ecc",
      "DATA",
      [
        "storage",
        "010a1738",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e5c.md#insn-00b63e7c) · [`00b63e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e5c.md#insn-00b63e78) · [`00b63e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e5c.md#insn-00b63e84)
- 新版 `00b63ec0`（命令位置の公開資料なし） · `00b63ebc`（命令位置の公開資料なし） · `00b63ec8`（命令位置の公開資料なし）

~~~diff
- 00b63e7c ["INT_ADD", "register:40f0:8", ["const:b63e7c:8", "const:4:8"]]
- 00b63e7c ["CALL", null, ["callee:00bde180:8"]]
+ 00b63ec0 ["INT_ADD", "register:40f0:8", ["const:b63ec0:8", "const:4:8"]]
+ 00b63ec0 ["CALL", null, ["callee:00bde180:8"]]
- 00b63e7c bytes ade80194
+ 00b63ec0 bytes b0e80194
- 00b63e78 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b63e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63ebc ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b63ebc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63ebc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63ebc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63e78 bytes 00fc1991
+ 00b63ebc bytes 00c81791
- 00b63e84 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00b63e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63ec8 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00b63ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63e84 bytes 08e11b91
+ 00b63ec8 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddfdfeb7fda58c28936b0182751b99ff"></a>

### [`00b63e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e98.md) → [`00b63edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63edc.md) _ZN8firebase4auth20CacheCommonMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c40.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 1件 [`00be0c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c90.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.09% / 新版 83.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `store_condition` 1件, `store_destination` 15件

アドレスに依存する影響 `branch_value` 12件, `store_condition` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b63f20",
      "incomplete_value": true,
      "site": "00b63f20",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63edc",
      "incomplete_value": true,
      "site": "00b63edc",
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
            "const:660:8"
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
      "definition_site": "00b63f78",
      "incomplete_value": true,
      "site": "00b63f78",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63f34",
      "incomplete_value": true,
      "site": "00b63f34",
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
            "const:500:8"
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
      "definition_site": "00b63fd0",
      "incomplete_value": true,
      "site": "00b63fd0",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63f8c",
      "incomplete_value": true,
      "site": "00b63f8c",
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
      "00b63ef4",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63f20",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63f38",
      "PARAM",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63ef4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63f20",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63f38",
      "PARAM",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e98.md#insn-00b63edc) · [`00b63f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e98.md#insn-00b63f14) · [`00b63f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e98.md#insn-00b63f34)
- 新版 `00b63f20`（命令位置の公開資料なし） · `00b63f58`（命令位置の公開資料なし） · `00b63f78`（命令位置の公開資料なし）

~~~diff
- 00b63edc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:660:8"]]
- 00b63edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63f20 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
+ 00b63f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63edc bytes a03203f9
+ 00b63f20 bytes a05203f9
- 00b63f14 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00b63f58 ["COPY", "register:4018:8", ["const:2a2000:8"]]
- 00b63f14 bytes e3b9ffd0
+ 00b63f58 bytes e3b9fff0
- 00b63f34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:500:8"]]
- 00b63f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63f78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:540:8"]]
+ 00b63f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63f34 bytes a08202f9
+ 00b63f78 bytes a0a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de72b4f0a05aa7d3b91fbdfc5766195b"></a>

### [`00b643f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b643f4.md) → [`00b64438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64438.md) _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c50.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ca0.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.27% / 新版 63.27%

CFGの説明率　旧版 32.65% / 新版 32.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6447c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6444c",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b64454"
      ]
    ],
    [
      "00b6445c",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6444c",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64498"
      ]
    ],
    [
      "00b6445c",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b643f4.md#insn-00b64418) · [`00b6441c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b643f4.md#insn-00b6441c) · [`00b64430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b643f4.md#insn-00b64430)
- 新版 `00b6445c`（命令位置の公開資料なし）

~~~diff
- 00b64418 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
- 00b64418 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b64418 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6445c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:548:8"]]
+ 00b6445c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6445c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b64418 bytes a8225439
+ 00b6445c bytes a8225539
- 00b6441c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b6441c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6441c bytes c8000034
- 00b64430 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b64430 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b64430 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:508:8"]]
- 00b64430 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b64430 bytes bf221439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a30cff74b43d4ff8df5877872a605166"></a>

### [`00b6488c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md) → [`00b648d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md) _ZN8firebase4auth22ErrorCodeFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d30.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00be0d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d80.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 83.40% / 新版 83.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b64a54",
      "incomplete_value": true,
      "site": "00b64a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64a10",
      "incomplete_value": true,
      "site": "00b64a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b64a80",
      "incomplete_value": true,
      "site": "00b64a80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4088:8"
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
      "definition_site": "00b64a3c",
      "incomplete_value": true,
      "site": "00b64a3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4088:8"
              ],
              [
                "leaf",
                "const:5e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b64a80",
      "incomplete_value": false,
      "site": "00b64a80",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64a3c",
      "incomplete_value": false,
      "site": "00b64a3c",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b64914",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64934",
      "READ",
      [
        "storage",
        "010a1690",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6497c",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b64914",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64934",
      "READ",
      [
        "storage",
        "010a16d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b649c4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b648e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md#insn-00b648e0) · [`00b648fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md#insn-00b648fc) · [`00b64a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md#insn-00b64a44)
- 新版 `00b64924`（命令位置の公開資料なし） · `00b64940`（命令位置の公開資料なし） · `00b64a88`（命令位置の公開資料なし）

~~~diff
- 00b648e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b648e0 ["INT_ADD", "register:40f0:8", ["const:b648e0:8", "const:4:8"]]
- 00b648e0 ["CALLIND", null, ["register:0:8"]]
+ 00b64924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64924 ["INT_ADD", "register:40f0:8", ["const:b64924:8", "const:4:8"]]
+ 00b64924 ["CALLIND", null, ["register:0:8"]]
- 00b648e0 bytes 00013fd6
+ 00b64924 bytes 00013fd6
- 00b648fc ["INT_ADD", "register:40f0:8", ["const:b648fc:8", "const:4:8"]]
- 00b648fc ["CALL", null, ["callee:0047495c:8"]]
+ 00b64940 ["INT_ADD", "register:40f0:8", ["const:b64940:8", "const:4:8"]]
+ 00b64940 ["CALL", null, ["callee:0047495c:8"]]
- 00b648fc bytes 1840e497
+ 00b64940 bytes 0740e497
- 00b64a44 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:640:8"]]
- 00b64a44 ["LOAD", "register:4060:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b64a88 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:680:8"]]
+ 00b64a88 ["LOAD", "register:4060:8", ["const:1b1:8", "tmp:0:8"]]
- 00b64a44 bytes 8c2143f9
+ 00b64a88 bytes 8c4143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b072962b492f78ccf51cde2435c4773b"></a>

### [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) → [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) _ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`00b5e75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e75c.md) [`00b5ef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ef24.md) [`00b5f194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f194.md) [`00b5f320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f320.md) [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) · 呼出先 11件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bddb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb70.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md)
- 新版 呼出元 11件 [`00b5e7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md) [`00b5ef68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md) [`00b5f1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md) [`00b5f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md) [`00b5f5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) · 呼出先 11件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bddbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbc0.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "definition_site": "00b64f58",
      "incomplete_value": true,
      "site": "00b64f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b64f14",
      "incomplete_value": true,
      "site": "00b64f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:510:8"
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
      "definition_site": "00b64ff4",
      "incomplete_value": true,
      "site": "00b65000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64fb0",
      "incomplete_value": true,
      "site": "00b64fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b64f58",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64ff4",
      "READ",
      [
        "storage",
        "010a1518",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65034",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b64f58",
      "READ",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64ff4",
      "READ",
      [
        "storage",
        "010a1558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65034",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md#insn-00b64f20) · [`00b64f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md#insn-00b64f64) · [`00b64fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md#insn-00b64fbc)
- 新版 `00b64f64`（命令位置の公開資料なし） · `00b64fa8`（命令位置の公開資料なし） · `00b65000`（命令位置の公開資料なし）

~~~diff
- 00b64f20 ["INT_ADD", "register:40f0:8", ["const:b64f20:8", "const:4:8"]]
- 00b64f20 ["CALL", null, ["callee:0047495c:8"]]
+ 00b64f64 ["INT_ADD", "register:40f0:8", ["const:b64f64:8", "const:4:8"]]
+ 00b64f64 ["CALL", null, ["callee:0047495c:8"]]
- 00b64f20 bytes 8f3ee497
+ 00b64f64 bytes 7e3ee497
- 00b64f64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64f64 ["INT_ADD", "register:40f0:8", ["const:b64f64:8", "const:4:8"]]
- 00b64f64 ["CALLIND", null, ["register:0:8"]]
+ 00b64fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64fa8 ["INT_ADD", "register:40f0:8", ["const:b64fa8:8", "const:4:8"]]
+ 00b64fa8 ["CALLIND", null, ["register:0:8"]]
- 00b64f64 bytes 00013fd6
+ 00b64fa8 bytes 00013fd6
- 00b64fbc ["INT_ADD", "register:40f0:8", ["const:b64fbc:8", "const:4:8"]]
- 00b64fbc ["CALL", null, ["callee:0047495c:8"]]
+ 00b65000 ["INT_ADD", "register:40f0:8", ["const:b65000:8", "const:4:8"]]
+ 00b65000 ["CALL", null, ["callee:0047495c:8"]]
- 00b64fbc bytes 683ee497
+ 00b65000 bytes 573ee497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78bd631e140a65818b26c3c5aeeb5e33"></a>

### [`00b65088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65088.md) → [`00b650cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b650cc.md) _ZN8firebase4auth22ReadAdditionalUserInfoEP7_JNIEnvP8_jobjectPNS0_18AdditionalUserInfoE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d40.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d90.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65104",
      "incomplete_value": true,
      "site": "00b65110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b650c0",
      "incomplete_value": true,
      "site": "00b650cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
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
      "00b65104",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65120",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6513c",
      "READ",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65104",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65120",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6513c",
      "READ",
      [
        "storage",
        "010a1590",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b650cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65088.md#insn-00b650cc) · [`00b65110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65088.md#insn-00b65110) · [`00b650bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65088.md#insn-00b650bc)
- 新版 `00b65110`（命令位置の公開資料なし） · `00b65154`（命令位置の公開資料なし） · `00b65100`（命令位置の公開資料なし）

~~~diff
- 00b650cc ["INT_ADD", "register:40f0:8", ["const:b650cc:8", "const:4:8"]]
- 00b650cc ["CALL", null, ["callee:0047495c:8"]]
+ 00b65110 ["INT_ADD", "register:40f0:8", ["const:b65110:8", "const:4:8"]]
+ 00b65110 ["CALL", null, ["callee:0047495c:8"]]
- 00b650cc bytes 243ee497
+ 00b65110 bytes 133ee497
- 00b65110 ["INT_ADD", "register:40f0:8", ["const:b65110:8", "const:4:8"]]
- 00b65110 ["CALL", null, ["callee:00bde0e0:8"]]
+ 00b65154 ["INT_ADD", "register:40f0:8", ["const:b65154:8", "const:4:8"]]
+ 00b65154 ["CALL", null, ["callee:00bde0e0:8"]]
- 00b65110 bytes e0e30194
+ 00b65154 bytes e3e30194
- 00b650bc ["COPY", "tmp:0:8", ["const:540:8"]]
- 00b650bc ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00b650bc ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00b650bc ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00b65100 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00b65100 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b65100 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b65100 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00b650bc bytes 39031591
+ 00b65100 bytes 39031691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8fa07525827b69e7649ffac9b2f66e"></a>

### [`00b65514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65514.md) → [`00b65558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65558.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65584",
      "incomplete_value": true,
      "site": "00b65584",
      "value": [
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
      "definition_site": "00b65540",
      "incomplete_value": true,
      "site": "00b65540",
      "value": [
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
    "old": {
      "definition_site": "00b65528",
      "incomplete_value": true,
      "site": "00b65528",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65578",
      "incomplete_value": false,
      "site": "00b6557c",
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
    "old": {
      "definition_site": "00b65534",
      "incomplete_value": false,
      "site": "00b65538",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65568",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65578",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b65584",
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
      "00b65568",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65578",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b65584",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65514.md#insn-00b65538) · [`00b65540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65514.md#insn-00b65540) · [`00b65524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65514.md#insn-00b65524)
- 新版 `00b6557c`（命令位置の公開資料なし） · `00b65584`（命令位置の公開資料なし） · `00b65568`（命令位置の公開資料なし）

~~~diff
- 00b65538 ["INT_ADD", "register:40f0:8", ["const:b65538:8", "const:4:8"]]
- 00b65538 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6557c ["INT_ADD", "register:40f0:8", ["const:b6557c:8", "const:4:8"]]
+ 00b6557c ["CALL", null, ["callee:00bde090:8"]]
- 00b65538 bytes c2e20194
+ 00b6557c bytes c5e20194
- 00b65540 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b65540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65540 bytes 608203f9
+ 00b65584 bytes 60a203f9
- 00b65524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b65524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65568 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65568 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65524 bytes 688243f9
+ 00b65568 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a96b92a75a0d360a0429bd56444a31a"></a>

### [`00b65554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65554.md) → [`00b65598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65598.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b65580",
      "incomplete_value": true,
      "site": "00b65580",
      "value": [
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
    "old": {
      "definition_site": "00b65568",
      "incomplete_value": true,
      "site": "00b65568",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b65570",
      "incomplete_value": false,
      "site": "00b65578",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b655a8",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655b4",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b655c4",
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
      "00b655a8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655b4",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b655c4",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65554.md#insn-00b65578) · [`00b65580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65554.md#insn-00b65580) · [`00b65564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65554.md#insn-00b65564)
- 新版 `00b655bc`（命令位置の公開資料なし） · `00b655c4`（命令位置の公開資料なし） · `00b655a8`（命令位置の公開資料なし）

~~~diff
- 00b65578 ["INT_ADD", "register:40f0:8", ["const:b65578:8", "const:4:8"]]
- 00b65578 ["CALL", null, ["callee:00bde090:8"]]
+ 00b655bc ["INT_ADD", "register:40f0:8", ["const:b655bc:8", "const:4:8"]]
+ 00b655bc ["CALL", null, ["callee:00bde090:8"]]
- 00b65578 bytes b2e20194
+ 00b655bc bytes b5e20194
- 00b65580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b65580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b655c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b655c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65580 bytes 608203f9
+ 00b655c4 bytes 60a203f9
- 00b65564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b65564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b655a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b655a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65564 bytes 688243f9
+ 00b655a8 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff10acc81ad04ee38cd80eb735fea438"></a>

### [`00b65594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65594.md) → [`00b655d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b655d8.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00b65608",
      "incomplete_value": true,
      "site": "00b65608",
      "value": [
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
    "old": {
      "definition_site": "00b655a8",
      "incomplete_value": true,
      "site": "00b655a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b655a8"
      ],
      [
        "FALL_THROUGH",
        "00b655ec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b655ec",
      "incomplete_value": true,
      "site": "00b65608",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655a8",
      "incomplete_value": true,
      "site": "00b655c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b655e8",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655f8",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b65608",
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
      "00b655e8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655f8",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b65608",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b655c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65594.md#insn-00b655c4) · [`00b655a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65594.md#insn-00b655a4) · [`00b655ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65594.md#insn-00b655ac)
- 新版 `00b65608`（命令位置の公開資料なし） · `00b655e8`（命令位置の公開資料なし） · `00b655f0`（命令位置の公開資料なし）

~~~diff
- 00b655c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b655c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b655c4 bytes 608203f9
+ 00b65608 bytes 60a203f9
- 00b655a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b655a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b655e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b655e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b655a4 bytes 688243f9
+ 00b655e8 bytes 68a243f9
- 00b655ac ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b655f0 ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b655ac bytes 03bafff0
+ 00b655f0 bytes 23baff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6f02aa5f33ad4fe98f688e2da222213"></a>

### [`00b655d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b655d8.md) → [`00b6561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6561c.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b6564c",
      "incomplete_value": true,
      "site": "00b6564c",
      "value": [
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
      "definition_site": "00b65608",
      "incomplete_value": true,
      "site": "00b65608",
      "value": [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65638",
      "incomplete_value": false,
      "site": "00b65644",
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
    "old": {
      "definition_site": "00b655f4",
      "incomplete_value": false,
      "site": "00b65600",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6562c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65638",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b6564c",
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
      "00b6562c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65638",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b6564c",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b655d8.md#insn-00b65600) · [`00b65608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b655d8.md#insn-00b65608) · [`00b655e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b655d8.md#insn-00b655e8)
- 新版 `00b65644`（命令位置の公開資料なし） · `00b6564c`（命令位置の公開資料なし） · `00b6562c`（命令位置の公開資料なし）

~~~diff
- 00b65600 ["INT_ADD", "register:40f0:8", ["const:b65600:8", "const:4:8"]]
- 00b65600 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65644 ["INT_ADD", "register:40f0:8", ["const:b65644:8", "const:4:8"]]
+ 00b65644 ["CALL", null, ["callee:00bde090:8"]]
- 00b65600 bytes 90e20194
+ 00b65644 bytes 93e20194
- 00b65608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b65608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6564c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b6564c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65608 bytes 608203f9
+ 00b6564c bytes 60a203f9
- 00b655e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b655e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6562c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b6562c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b655e8 bytes 688243f9
+ 00b6562c bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31a52bff683b1452a6f677faa8c0ba51"></a>

### [`00b65628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65628.md) → [`00b6566c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6566c.md) _ZN8firebase4auth10credential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b65680",
      "incomplete_value": true,
      "site": "00b65680",
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
    "old": {
      "definition_site": "00b6565c",
      "incomplete_value": true,
      "site": "00b65668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b65680",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b656a0",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656c4",
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
      "00b65680",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b656a0",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656c4",
      "WRITE",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6563c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65628.md#insn-00b6563c) · [`00b65668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65628.md#insn-00b65668) · [`00b65680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65628.md#insn-00b65680)
- 新版 `00b65680`（命令位置の公開資料なし） · `00b656ac`（命令位置の公開資料なし） · `00b656c4`（命令位置の公開資料なし）

~~~diff
- 00b6563c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:708:8"]]
- 00b6563c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6563c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b65680 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:748:8"]]
+ 00b65680 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b65680 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6563c bytes a8225c39
+ 00b65680 bytes a8225d39
- 00b65668 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65668 ["INT_ADD", "register:40f0:8", ["const:b65668:8", "const:4:8"]]
- 00b65668 ["CALLIND", null, ["register:0:8"]]
+ 00b656ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b656ac ["INT_ADD", "register:40f0:8", ["const:b656ac:8", "const:4:8"]]
+ 00b656ac ["CALLIND", null, ["register:0:8"]]
- 00b65668 bytes 00013fd6
+ 00b656ac bytes 00013fd6
- 00b65680 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65680 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:708:8"]]
- 00b65680 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b656c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b656c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
+ 00b656c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65680 bytes a0221c39
+ 00b656c4 bytes a0221d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76689c71c876fdebd5cbfb49e6bcdf50"></a>

### [`00b65694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65694.md) → [`00b656d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b656d8.md) _ZN8firebase4auth10credential12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b65714",
      "incomplete_value": true,
      "site": "00b65714",
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
    "old": {
      "definition_site": "00b656d0",
      "incomplete_value": true,
      "site": "00b656d0",
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
      "definition_site": "00b65734",
      "incomplete_value": true,
      "site": "00b65734",
      "value": [
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
      "definition_site": "00b656f0",
      "incomplete_value": true,
      "site": "00b656f0",
      "value": [
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
      "definition_site": "00b656f0",
      "incomplete_value": true,
      "site": "00b656f0",
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
      "definition_site": "00b656ac",
      "incomplete_value": true,
      "site": "00b656ac",
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
      "00b656ec",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656f8",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65714",
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
      "00b656ec",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656f8",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65714",
      "WRITE",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b656a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65694.md#insn-00b656a8) · [`00b656d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65694.md#insn-00b656d0) · [`00b656ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65694.md#insn-00b656ec)
- 新版 `00b656ec`（命令位置の公開資料なし） · `00b65714`（命令位置の公開資料なし） · `00b65730`（命令位置の公開資料なし）

~~~diff
- 00b656a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b656a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b656ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b656ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b656a8 bytes 818243f9
+ 00b656ec bytes 81a243f9
- 00b656d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b656d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b656d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:708:8"]]
- 00b656d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65714 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65714 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65714 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
+ 00b65714 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b656d0 bytes bf221c39
+ 00b65714 bytes bf221d39
- 00b656ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b656ec ["INT_ADD", "register:40f0:8", ["const:b656ec:8", "const:4:8"]]
- 00b656ec ["CALLIND", null, ["register:0:8"]]
+ 00b65730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65730 ["INT_ADD", "register:40f0:8", ["const:b65730:8", "const:4:8"]]
+ 00b65730 ["CALLIND", null, ["register:0:8"]]
- 00b656ec bytes 00013fd6
+ 00b65730 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b0177ba77c1704716b27d1e5adf4a0"></a>

### [`00b65704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65704.md) → [`00b65748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65748.md) _ZN8firebase4auth10credential14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
    "old": {
      "definition_site": "00b65744",
      "incomplete_value": true,
      "site": "00b65744",
      "value": [
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
    "old": {
      "definition_site": "00b65720",
      "incomplete_value": true,
      "site": "00b65720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b65728",
      "incomplete_value": false,
      "site": "00b6573c",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6575c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6576c",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b65788",
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
      "00b6575c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6576c",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b65788",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6573c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65704.md#insn-00b6573c) · [`00b65744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65704.md#insn-00b65744) · [`00b65718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65704.md#insn-00b65718)
- 新版 `00b65780`（命令位置の公開資料なし） · `00b65788`（命令位置の公開資料なし） · `00b6575c`（命令位置の公開資料なし）

~~~diff
- 00b6573c ["INT_ADD", "register:40f0:8", ["const:b6573c:8", "const:4:8"]]
- 00b6573c ["CALL", null, ["callee:00bde090:8"]]
+ 00b65780 ["INT_ADD", "register:40f0:8", ["const:b65780:8", "const:4:8"]]
+ 00b65780 ["CALL", null, ["callee:00bde090:8"]]
- 00b6573c bytes 41e20194
+ 00b65780 bytes 44e20194
- 00b65744 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b65744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65744 bytes 808203f9
+ 00b65788 bytes 80a203f9
- 00b65718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b65718 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6575c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b6575c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65718 bytes 818243f9
+ 00b6575c bytes 81a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a8ecb19fe2ad73945499b339c7fc44f"></a>

### [`00b65774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65774.md) → [`00b657b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657b8.md) _ZN8firebase4auth10credential11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b65790",
      "incomplete_value": false,
      "site": "00b65794",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b657a0",
      "incomplete_value": true,
      "site": "00b657ac",
      "value": [
        "LOAD",
        "8",
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
      "00b657d4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b657e4",
      "DATA",
      [
        "storage",
        "010a1710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b657d4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b657e4",
      "DATA",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65774.md#insn-00b65794) · [`00b65790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65774.md#insn-00b65790) · [`00b6579c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65774.md#insn-00b6579c)
- 新版 `00b657d8`（命令位置の公開資料なし） · `00b657d4`（命令位置の公開資料なし） · `00b657e0`（命令位置の公開資料なし）

~~~diff
- 00b65794 ["INT_ADD", "register:40f0:8", ["const:b65794:8", "const:4:8"]]
- 00b65794 ["CALL", null, ["callee:00bde180:8"]]
+ 00b657d8 ["INT_ADD", "register:40f0:8", ["const:b657d8:8", "const:4:8"]]
+ 00b657d8 ["CALL", null, ["callee:00bde180:8"]]
- 00b65794 bytes 67e20194
+ 00b657d8 bytes 6ae20194
- 00b65790 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b65790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b657d4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b657d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b657d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b657d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65790 bytes 00501791
+ 00b657d4 bytes 001c1591
- 00b6579c ["COPY", "tmp:0:8", ["const:710:8"]]
- 00b6579c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6579c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6579c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b657e0 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00b657e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b657e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b657e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6579c bytes 08411c91
+ 00b657e0 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb926991af0b4243df1619a860bce01"></a>

### [`00b657b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b657b0.md) → [`00b657f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657f4.md) _ZN8firebase4auth10credential13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b657f0",
      "incomplete_value": true,
      "site": "00b657f0",
      "value": [
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
    "old": {
      "definition_site": "00b657cc",
      "incomplete_value": true,
      "site": "00b657cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
    "old": {
      "definition_site": "00b657d4",
      "incomplete_value": false,
      "site": "00b657e8",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65818",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b65834",
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
      "00b65808",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65818",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00b65834",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b657b0.md#insn-00b657e8) · [`00b657f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b657b0.md#insn-00b657f0) · [`00b657c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b657b0.md#insn-00b657c4)
- 新版 `00b6582c`（命令位置の公開資料なし） · `00b65834`（命令位置の公開資料なし） · `00b65808`（命令位置の公開資料なし）

~~~diff
- 00b657e8 ["INT_ADD", "register:40f0:8", ["const:b657e8:8", "const:4:8"]]
- 00b657e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6582c ["INT_ADD", "register:40f0:8", ["const:b6582c:8", "const:4:8"]]
+ 00b6582c ["CALL", null, ["callee:00bde090:8"]]
- 00b657e8 bytes 16e20194
+ 00b6582c bytes 19e20194
- 00b657f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b657f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b657f0 bytes 808203f9
+ 00b65834 bytes 80a203f9
- 00b657c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b657c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65808 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b657c4 bytes 818243f9
+ 00b65808 bytes 81a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-089eb7d5654a76c262ea0ba5a6203176"></a>

### [`00b65820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md) → [`00b65864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65864.md) _ZN8firebase4auth10credential10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65880",
      "incomplete_value": false,
      "site": "00b65884",
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
    "old": {
      "definition_site": "00b6583c",
      "incomplete_value": false,
      "site": "00b65840",
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
      "00b65880",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65890",
      "DATA",
      [
        "storage",
        "010a1718",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65880",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65890",
      "DATA",
      [
        "storage",
        "010a1758",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md#insn-00b65840) · [`00b6583c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md#insn-00b6583c) · [`00b65848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md#insn-00b65848)
- 新版 `00b65884`（命令位置の公開資料なし） · `00b65880`（命令位置の公開資料なし） · `00b6588c`（命令位置の公開資料なし）

~~~diff
- 00b65840 ["INT_ADD", "register:40f0:8", ["const:b65840:8", "const:4:8"]]
- 00b65840 ["CALL", null, ["callee:00bde180:8"]]
+ 00b65884 ["INT_ADD", "register:40f0:8", ["const:b65884:8", "const:4:8"]]
+ 00b65884 ["CALL", null, ["callee:00bde180:8"]]
- 00b65840 bytes 3ce20194
+ 00b65884 bytes 3fe20194
- 00b6583c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6583c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6583c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6583c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65880 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b65880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6583c bytes 00fc1991
+ 00b65880 bytes 00c81791
- 00b65848 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00b65848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6588c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00b6588c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6588c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6588c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65848 bytes 08611c91
+ 00b6588c bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca058d3ba3c2280e567d64aa06306e3a"></a>

### [`00b6585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6585c.md) → [`00b658a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658a0.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b65888",
      "incomplete_value": true,
      "site": "00b65888",
      "value": [
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
    "old": {
      "definition_site": "00b65870",
      "incomplete_value": true,
      "site": "00b65870",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6587c",
      "incomplete_value": false,
      "site": "00b65880",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b658b0",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658c0",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b658cc",
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
      "00b658b0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658c0",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b658cc",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6585c.md#insn-00b65880) · [`00b65888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6585c.md#insn-00b65888) · [`00b6586c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6585c.md#insn-00b6586c)
- 新版 `00b658c4`（命令位置の公開資料なし） · `00b658cc`（命令位置の公開資料なし） · `00b658b0`（命令位置の公開資料なし）

~~~diff
- 00b65880 ["INT_ADD", "register:40f0:8", ["const:b65880:8", "const:4:8"]]
- 00b65880 ["CALL", null, ["callee:00bde090:8"]]
+ 00b658c4 ["INT_ADD", "register:40f0:8", ["const:b658c4:8", "const:4:8"]]
+ 00b658c4 ["CALL", null, ["callee:00bde090:8"]]
- 00b65880 bytes f0e10194
+ 00b658c4 bytes f3e10194
- 00b65888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b65888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b658cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b658cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65888 bytes 609203f9
+ 00b658cc bytes 60b203f9
- 00b6586c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b6586c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b658b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b658b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6586c bytes 689243f9
+ 00b658b0 bytes 68b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ef5090c6800caef82411443c4c7b8d"></a>

### [`00b6589c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6589c.md) → [`00b658e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658e0.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b6590c",
      "incomplete_value": true,
      "site": "00b6590c",
      "value": [
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
    "old": {
      "definition_site": "00b658c8",
      "incomplete_value": true,
      "site": "00b658c8",
      "value": [
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
    "old": {
      "definition_site": "00b658b0",
      "incomplete_value": true,
      "site": "00b658b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b658fc",
      "incomplete_value": false,
      "site": "00b65904",
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
    "old": {
      "definition_site": "00b658b8",
      "incomplete_value": false,
      "site": "00b658c0",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b658f0",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658fc",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b6590c",
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
      "00b658f0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658fc",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b6590c",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6589c.md#insn-00b658c0) · [`00b658c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6589c.md#insn-00b658c8) · [`00b658ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6589c.md#insn-00b658ac)
- 新版 `00b65904`（命令位置の公開資料なし） · `00b6590c`（命令位置の公開資料なし） · `00b658f0`（命令位置の公開資料なし）

~~~diff
- 00b658c0 ["INT_ADD", "register:40f0:8", ["const:b658c0:8", "const:4:8"]]
- 00b658c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65904 ["INT_ADD", "register:40f0:8", ["const:b65904:8", "const:4:8"]]
+ 00b65904 ["CALL", null, ["callee:00bde090:8"]]
- 00b658c0 bytes e0e10194
+ 00b65904 bytes e3e10194
- 00b658c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b658c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6590c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b6590c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b658c8 bytes 609203f9
+ 00b6590c bytes 60b203f9
- 00b658ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b658ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b658f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b658f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b658ac bytes 689243f9
+ 00b658f0 bytes 68b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c61288ab3673696346a414dec2d211e5"></a>

### [`00b658dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b658dc.md) → [`00b65920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65920.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b6590c",
      "incomplete_value": true,
      "site": "00b6590c",
      "value": [
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
    "old": {
      "definition_site": "00b658f0",
      "incomplete_value": true,
      "site": "00b658f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b658fc",
      "incomplete_value": false,
      "site": "00b65904",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65930",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65940",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65950",
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
      "00b65930",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65940",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b65950",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b658dc.md#insn-00b65904) · [`00b6590c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b658dc.md#insn-00b6590c) · [`00b658ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b658dc.md#insn-00b658ec)
- 新版 `00b65948`（命令位置の公開資料なし） · `00b65950`（命令位置の公開資料なし） · `00b65930`（命令位置の公開資料なし）

~~~diff
- 00b65904 ["INT_ADD", "register:40f0:8", ["const:b65904:8", "const:4:8"]]
- 00b65904 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65948 ["INT_ADD", "register:40f0:8", ["const:b65948:8", "const:4:8"]]
+ 00b65948 ["CALL", null, ["callee:00bde090:8"]]
- 00b65904 bytes cfe10194
+ 00b65948 bytes d2e10194
- 00b6590c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b6590c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6590c bytes 609203f9
+ 00b65950 bytes 60b203f9
- 00b658ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b658ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b658ec bytes 689243f9
+ 00b65930 bytes 68b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ba14b2d3f43bb3ed32b7a0f310d9f0"></a>

### [`00b65920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65920.md) → [`00b65964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65964.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65994",
      "incomplete_value": true,
      "site": "00b65994",
      "value": [
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
      "definition_site": "00b65980",
      "incomplete_value": false,
      "site": "00b6598c",
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
    "old": {
      "definition_site": "00b6593c",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65974",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65980",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65994",
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
      "00b65974",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65980",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b65994",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65920.md#insn-00b65948) · [`00b65950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65920.md#insn-00b65950) · [`00b65930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65920.md#insn-00b65930)
- 新版 `00b6598c`（命令位置の公開資料なし） · `00b65994`（命令位置の公開資料なし） · `00b65974`（命令位置の公開資料なし）

~~~diff
- 00b65948 ["INT_ADD", "register:40f0:8", ["const:b65948:8", "const:4:8"]]
- 00b65948 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6598c ["INT_ADD", "register:40f0:8", ["const:b6598c:8", "const:4:8"]]
+ 00b6598c ["CALL", null, ["callee:00bde090:8"]]
- 00b65948 bytes bee10194
+ 00b6598c bytes c1e10194
- 00b65950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b65950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65950 bytes 609203f9
+ 00b65994 bytes 60b203f9
- 00b65930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b65930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65930 bytes 689243f9
+ 00b65974 bytes 68b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c17bbae3dd5c1ff2132a06a6e6b70a74"></a>

### [`00b65970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65970.md) → [`00b659b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b659b4.md) _ZN8firebase4auth9emailcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b65a0c",
      "incomplete_value": true,
      "site": "00b65a0c",
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
    "old": {
      "definition_site": "00b659c8",
      "incomplete_value": true,
      "site": "00b659c8",
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
    "old": {
      "definition_site": "00b659a4",
      "incomplete_value": true,
      "site": "00b659b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b659c8",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b659e8",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a0c",
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
      "00b659c8",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b659e8",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a0c",
      "WRITE",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65970.md#insn-00b65984) · [`00b659b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65970.md#insn-00b659b0) · [`00b659c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65970.md#insn-00b659c8)
- 新版 `00b659c8`（命令位置の公開資料なし） · `00b659f4`（命令位置の公開資料なし） · `00b65a0c`（命令位置の公開資料なし）

~~~diff
- 00b65984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00b65984 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65984 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b659c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:768:8"]]
+ 00b659c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b659c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65984 bytes a8a25c39
+ 00b659c8 bytes a8a25d39
- 00b659b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b659b0 ["INT_ADD", "register:40f0:8", ["const:b659b0:8", "const:4:8"]]
- 00b659b0 ["CALLIND", null, ["register:0:8"]]
+ 00b659f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b659f4 ["INT_ADD", "register:40f0:8", ["const:b659f4:8", "const:4:8"]]
+ 00b659f4 ["CALLIND", null, ["register:0:8"]]
- 00b659b0 bytes 00013fd6
+ 00b659f4 bytes 00013fd6
- 00b659c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b659c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:728:8"]]
- 00b659c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65a0c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65a0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:768:8"]]
+ 00b65a0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b659c8 bytes a0a21c39
+ 00b65a0c bytes a0a21d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a0bed07dce17005628d34ba8f5ae0c0"></a>

### [`00b659dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b659dc.md) → [`00b65a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md) _ZN8firebase4auth9emailcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b65a18",
      "incomplete_value": true,
      "site": "00b65a18",
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
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00b65a38",
      "incomplete_value": true,
      "site": "00b65a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
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
    "old": {
      "definition_site": "00b659f4",
      "incomplete_value": true,
      "site": "00b659f4",
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
      "00b65a34",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a40",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65a5c",
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
      "00b65a34",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a40",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65a5c",
      "WRITE",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b659f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b659dc.md#insn-00b659f0) · [`00b65a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b659dc.md#insn-00b65a18) · [`00b65a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b659dc.md#insn-00b65a34)
- 新版 `00b65a34`（命令位置の公開資料なし） · `00b65a5c`（命令位置の公開資料なし） · `00b65a78`（命令位置の公開資料なし）

~~~diff
- 00b659f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b659f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b65a34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b659f0 bytes 819243f9
+ 00b65a34 bytes 81b243f9
- 00b65a18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65a18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65a18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:728:8"]]
- 00b65a18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65a5c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65a5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65a5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:768:8"]]
+ 00b65a5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65a18 bytes bfa21c39
+ 00b65a5c bytes bfa21d39
- 00b65a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65a34 ["INT_ADD", "register:40f0:8", ["const:b65a34:8", "const:4:8"]]
- 00b65a34 ["CALLIND", null, ["register:0:8"]]
+ 00b65a78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65a78 ["INT_ADD", "register:40f0:8", ["const:b65a78:8", "const:4:8"]]
+ 00b65a78 ["CALLIND", null, ["register:0:8"]]
- 00b65a34 bytes 00013fd6
+ 00b65a78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc139ac14b4d85a02edbc6ef7e016183"></a>

### [`00b65a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65a4c.md) → [`00b65a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md) _ZN8firebase4auth9emailcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b65ad0",
      "incomplete_value": true,
      "site": "00b65ad0",
      "value": [
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
    "old": {
      "definition_site": "00b65a8c",
      "incomplete_value": true,
      "site": "00b65a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b65aac",
      "incomplete_value": true,
      "site": "00b65aac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a68",
      "incomplete_value": true,
      "site": "00b65a68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65ab4",
      "incomplete_value": false,
      "site": "00b65ac8",
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
    "old": {
      "definition_site": "00b65a70",
      "incomplete_value": false,
      "site": "00b65a84",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65aa4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ab4",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65ad0",
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
      "00b65aa4",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ab4",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b65ad0",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65a4c.md#insn-00b65a84) · [`00b65a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65a4c.md#insn-00b65a8c) · [`00b65a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65a4c.md#insn-00b65a60)
- 新版 `00b65ac8`（命令位置の公開資料なし） · `00b65ad0`（命令位置の公開資料なし） · `00b65aa4`（命令位置の公開資料なし）

~~~diff
- 00b65a84 ["INT_ADD", "register:40f0:8", ["const:b65a84:8", "const:4:8"]]
- 00b65a84 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65ac8 ["INT_ADD", "register:40f0:8", ["const:b65ac8:8", "const:4:8"]]
+ 00b65ac8 ["CALL", null, ["callee:00bde090:8"]]
- 00b65a84 bytes 6fe10194
+ 00b65ac8 bytes 72e10194
- 00b65a8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b65a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b65ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65a8c bytes 809203f9
+ 00b65ad0 bytes 80b203f9
- 00b65a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b65a60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65aa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b65aa4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65a60 bytes 819243f9
+ 00b65aa4 bytes 81b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a372d5f0d2c7efc318cb7b3767d31fb8"></a>

### [`00b65abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65abc.md) → [`00b65b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b65ad8",
      "incomplete_value": false,
      "site": "00b65adc",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b65ae8",
      "incomplete_value": true,
      "site": "00b65af4",
      "value": [
        "LOAD",
        "8",
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
      "00b65b1c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b65b2c",
      "DATA",
      [
        "storage",
        "010a1730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65b1c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65b2c",
      "DATA",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65abc.md#insn-00b65adc) · [`00b65ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65abc.md#insn-00b65ad8) · [`00b65ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65abc.md#insn-00b65ae4)
- 新版 `00b65b20`（命令位置の公開資料なし） · `00b65b1c`（命令位置の公開資料なし） · `00b65b28`（命令位置の公開資料なし）

~~~diff
- 00b65adc ["INT_ADD", "register:40f0:8", ["const:b65adc:8", "const:4:8"]]
- 00b65adc ["CALL", null, ["callee:00bde180:8"]]
+ 00b65b20 ["INT_ADD", "register:40f0:8", ["const:b65b20:8", "const:4:8"]]
+ 00b65b20 ["CALL", null, ["callee:00bde180:8"]]
- 00b65adc bytes 95e10194
+ 00b65b20 bytes 98e10194
- 00b65ad8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b65ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65b1c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b65b1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65ad8 bytes 00501791
+ 00b65b1c bytes 001c1591
- 00b65ae4 ["COPY", "tmp:0:8", ["const:730:8"]]
- 00b65ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65b28 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00b65b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65ae4 bytes 08c11c91
+ 00b65b28 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf361824abb8c530535b8e2213795625"></a>

### [`00b65af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65af8.md) → [`00b65b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md) _ZN8firebase4auth9emailcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65b7c",
      "incomplete_value": true,
      "site": "00b65b7c",
      "value": [
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
    "old": {
      "definition_site": "00b65b38",
      "incomplete_value": true,
      "site": "00b65b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b65b58",
      "incomplete_value": true,
      "site": "00b65b58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b14",
      "incomplete_value": true,
      "site": "00b65b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "site": "00b65b74",
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
    "old": {
      "definition_site": "00b65b1c",
      "incomplete_value": false,
      "site": "00b65b30",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b60",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65b7c",
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
      "00b65b50",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b60",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00b65b7c",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65af8.md#insn-00b65b30) · [`00b65b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65af8.md#insn-00b65b38) · [`00b65b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65af8.md#insn-00b65b0c)
- 新版 `00b65b74`（命令位置の公開資料なし） · `00b65b7c`（命令位置の公開資料なし） · `00b65b50`（命令位置の公開資料なし）

~~~diff
- 00b65b30 ["INT_ADD", "register:40f0:8", ["const:b65b30:8", "const:4:8"]]
- 00b65b30 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65b74 ["INT_ADD", "register:40f0:8", ["const:b65b74:8", "const:4:8"]]
+ 00b65b74 ["CALL", null, ["callee:00bde090:8"]]
- 00b65b30 bytes 44e10194
+ 00b65b74 bytes 47e10194
- 00b65b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b65b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65b7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b65b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b38 bytes 809203f9
+ 00b65b7c bytes 80b203f9
- 00b65b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b65b0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65b50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b65b50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65b0c bytes 819243f9
+ 00b65b50 bytes 81b243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e74c5745dc98d1f90eb81ccac0330281"></a>

### [`00b65b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65b68.md) → [`00b65bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b65b84",
      "incomplete_value": false,
      "site": "00b65b88",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b65b94",
      "incomplete_value": true,
      "site": "00b65ba0",
      "value": [
        "LOAD",
        "8",
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
      "00b65bc8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65bd8",
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
      "00b65bc8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65bd8",
      "DATA",
      [
        "storage",
        "010a1778",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65b68.md#insn-00b65b88) · [`00b65b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65b68.md#insn-00b65b84) · [`00b65b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65b68.md#insn-00b65b90)
- 新版 `00b65bcc`（命令位置の公開資料なし） · `00b65bc8`（命令位置の公開資料なし） · `00b65bd4`（命令位置の公開資料なし）

~~~diff
- 00b65b88 ["INT_ADD", "register:40f0:8", ["const:b65b88:8", "const:4:8"]]
- 00b65b88 ["CALL", null, ["callee:00bde180:8"]]
+ 00b65bcc ["INT_ADD", "register:40f0:8", ["const:b65bcc:8", "const:4:8"]]
+ 00b65bcc ["CALL", null, ["callee:00bde180:8"]]
- 00b65b88 bytes 6ae10194
+ 00b65bcc bytes 6de10194
- 00b65b84 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b65b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65bc8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b65bc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65bc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65bc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65b84 bytes 00fc1991
+ 00b65bc8 bytes 00c81791
- 00b65b90 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00b65b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65bd4 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00b65bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65b90 bytes 08e11c91
+ 00b65bd4 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2752c96bb2b65814103082d60f0d10"></a>

### [`00b65ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ba4.md) → [`00b65be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b65bd0",
      "incomplete_value": true,
      "site": "00b65bd0",
      "value": [
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
    "old": {
      "definition_site": "00b65bb8",
      "incomplete_value": true,
      "site": "00b65bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65bb8"
      ],
      [
        "FALL_THROUGH",
        "00b65bfc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65bfc",
      "incomplete_value": true,
      "site": "00b65c14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bb8",
      "incomplete_value": true,
      "site": "00b65bd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65bf8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c14",
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
      "00b65bf8",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c14",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ba4.md#insn-00b65bd0) · [`00b65bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ba4.md#insn-00b65bb4) · [`00b65bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ba4.md#insn-00b65bc8)
- 新版 `00b65c14`（命令位置の公開資料なし） · `00b65bf8`（命令位置の公開資料なし） · `00b65c0c`（命令位置の公開資料なし）

~~~diff
- 00b65bd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65c14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65bd0 bytes 60a203f9
+ 00b65c14 bytes 60c203f9
- 00b65bb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65bf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65bf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65bb4 bytes 68a243f9
+ 00b65bf8 bytes 68c243f9
- 00b65bc8 ["INT_ADD", "register:40f0:8", ["const:b65bc8:8", "const:4:8"]]
- 00b65bc8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65c0c ["INT_ADD", "register:40f0:8", ["const:b65c0c:8", "const:4:8"]]
+ 00b65c0c ["CALL", null, ["callee:00bde090:8"]]
- 00b65bc8 bytes 1ee10194
+ 00b65c0c bytes 21e10194
~~~


<a id="compare-83a18288d1d12652a27e600736df749b"></a>

### [`00b65be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65be4.md) → [`00b65c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65c54",
      "incomplete_value": true,
      "site": "00b65c54",
      "value": [
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
    "old": {
      "definition_site": "00b65c10",
      "incomplete_value": true,
      "site": "00b65c10",
      "value": [
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
    "old": {
      "definition_site": "00b65bf8",
      "incomplete_value": true,
      "site": "00b65bf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65bf8"
      ],
      [
        "FALL_THROUGH",
        "00b65c3c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65c3c",
      "incomplete_value": true,
      "site": "00b65c54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bf8",
      "incomplete_value": true,
      "site": "00b65c10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65c38",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c54",
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
      "00b65c38",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c54",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65be4.md#insn-00b65c10) · [`00b65bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65be4.md#insn-00b65bf4) · [`00b65c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65be4.md#insn-00b65c08)
- 新版 `00b65c54`（命令位置の公開資料なし） · `00b65c38`（命令位置の公開資料なし） · `00b65c4c`（命令位置の公開資料なし）

~~~diff
- 00b65c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c10 bytes 60a203f9
+ 00b65c54 bytes 60c203f9
- 00b65bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65bf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65c38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65bf4 bytes 68a243f9
+ 00b65c38 bytes 68c243f9
- 00b65c08 ["INT_ADD", "register:40f0:8", ["const:b65c08:8", "const:4:8"]]
- 00b65c08 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65c4c ["INT_ADD", "register:40f0:8", ["const:b65c4c:8", "const:4:8"]]
+ 00b65c4c ["CALL", null, ["callee:00bde090:8"]]
- 00b65c08 bytes 0ee10194
+ 00b65c4c bytes 11e10194
~~~


<a id="compare-6e40d0a4e827d4918e72df930ac828fe"></a>

### [`00b65c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c24.md) → [`00b65c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c68.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65c98",
      "incomplete_value": true,
      "site": "00b65c98",
      "value": [
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
    "old": {
      "definition_site": "00b65c54",
      "incomplete_value": true,
      "site": "00b65c54",
      "value": [
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
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c38",
      "incomplete_value": true,
      "site": "00b65c38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65c38"
      ],
      [
        "FALL_THROUGH",
        "00b65c7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c38",
      "incomplete_value": true,
      "site": "00b65c54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65c78",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c98",
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
      "00b65c78",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c98",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c24.md#insn-00b65c54) · [`00b65c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c24.md#insn-00b65c34) · [`00b65c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c24.md#insn-00b65c4c)
- 新版 `00b65c98`（命令位置の公開資料なし） · `00b65c78`（命令位置の公開資料なし） · `00b65c90`（命令位置の公開資料なし）

~~~diff
- 00b65c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c54 bytes 60a203f9
+ 00b65c98 bytes 60c203f9
- 00b65c34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65c34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65c34 bytes 68a243f9
+ 00b65c78 bytes 68c243f9
- 00b65c4c ["INT_ADD", "register:40f0:8", ["const:b65c4c:8", "const:4:8"]]
- 00b65c4c ["CALL", null, ["callee:00bde090:8"]]
+ 00b65c90 ["INT_ADD", "register:40f0:8", ["const:b65c90:8", "const:4:8"]]
+ 00b65c90 ["CALL", null, ["callee:00bde090:8"]]
- 00b65c4c bytes fde00194
+ 00b65c90 bytes 00e10194
~~~


<a id="compare-8e97aa3b7119754953cfeb07b40b42e3"></a>

### [`00b65c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c68.md) → [`00b65cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65cdc",
      "incomplete_value": true,
      "site": "00b65cdc",
      "value": [
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
    "old": {
      "definition_site": "00b65c98",
      "incomplete_value": true,
      "site": "00b65c98",
      "value": [
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
    "old": {
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65c7c"
      ],
      [
        "FALL_THROUGH",
        "00b65cc0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65cc0",
      "incomplete_value": true,
      "site": "00b65cdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65cbc",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65cdc",
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
      "00b65cbc",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65cdc",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c68.md#insn-00b65c98) · [`00b65c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c68.md#insn-00b65c78) · [`00b65c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c68.md#insn-00b65c90)
- 新版 `00b65cdc`（命令位置の公開資料なし） · `00b65cbc`（命令位置の公開資料なし） · `00b65cd4`（命令位置の公開資料なし）

~~~diff
- 00b65c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c98 bytes 60a203f9
+ 00b65cdc bytes 60c203f9
- 00b65c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b65cbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65c78 bytes 68a243f9
+ 00b65cbc bytes 68c243f9
- 00b65c90 ["INT_ADD", "register:40f0:8", ["const:b65c90:8", "const:4:8"]]
- 00b65c90 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65cd4 ["INT_ADD", "register:40f0:8", ["const:b65cd4:8", "const:4:8"]]
+ 00b65cd4 ["CALL", null, ["callee:00bde090:8"]]
- 00b65c90 bytes ece00194
+ 00b65cd4 bytes efe00194
~~~


<a id="compare-150e4f9a3c150cc2c4fd972af1193a07"></a>

### [`00b65cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65cb8.md) → [`00b65cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cfc.md) _ZN8firebase4auth12facebookcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b65d54",
      "incomplete_value": true,
      "site": "00b65d54",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d10",
      "incomplete_value": true,
      "site": "00b65d10",
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
      "definition_site": "00b65d30",
      "incomplete_value": true,
      "site": "00b65d3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b65cec",
      "incomplete_value": true,
      "site": "00b65cf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b65d10",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65d30",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d54",
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
      "00b65d10",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65d30",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d54",
      "WRITE",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65cb8.md#insn-00b65ccc) · [`00b65cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65cb8.md#insn-00b65cf8) · [`00b65d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65cb8.md#insn-00b65d10)
- 新版 `00b65d10`（命令位置の公開資料なし） · `00b65d3c`（命令位置の公開資料なし） · `00b65d54`（命令位置の公開資料なし）

~~~diff
- 00b65ccc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:748:8"]]
- 00b65ccc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65ccc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b65d10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00b65d10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b65d10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65ccc bytes a8225d39
+ 00b65d10 bytes a8225e39
- 00b65cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65cf8 ["INT_ADD", "register:40f0:8", ["const:b65cf8:8", "const:4:8"]]
- 00b65cf8 ["CALLIND", null, ["register:0:8"]]
+ 00b65d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65d3c ["INT_ADD", "register:40f0:8", ["const:b65d3c:8", "const:4:8"]]
+ 00b65d3c ["CALLIND", null, ["register:0:8"]]
- 00b65cf8 bytes 00013fd6
+ 00b65d3c bytes 00013fd6
- 00b65d10 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65d10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
- 00b65d10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65d54 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65d54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
+ 00b65d54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65d10 bytes a0221d39
+ 00b65d54 bytes a0221e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06bb533779e2b647e9c75b710b11d3b7"></a>

### [`00b65d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d24.md) → [`00b65d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md) _ZN8firebase4auth12facebookcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b65da4",
      "incomplete_value": true,
      "site": "00b65da4",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d60",
      "incomplete_value": true,
      "site": "00b65d60",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b65dc4",
      "incomplete_value": true,
      "site": "00b65dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d80",
      "incomplete_value": true,
      "site": "00b65d80",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65d80",
      "incomplete_value": true,
      "site": "00b65d80",
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
      "definition_site": "00b65d3c",
      "incomplete_value": true,
      "site": "00b65d3c",
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
      "00b65d7c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d88",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65da4",
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
      "00b65d7c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d88",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65da4",
      "WRITE",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d24.md#insn-00b65d38) · [`00b65d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d24.md#insn-00b65d60) · [`00b65d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d24.md#insn-00b65d7c)
- 新版 `00b65d7c`（命令位置の公開資料なし） · `00b65da4`（命令位置の公開資料なし） · `00b65dc0`（命令位置の公開資料なし）

~~~diff
- 00b65d38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65d38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65d7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b65d7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65d38 bytes 81a243f9
+ 00b65d7c bytes 81c243f9
- 00b65d60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65d60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65d60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
- 00b65d60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65da4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65da4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65da4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
+ 00b65da4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65d60 bytes bf221d39
+ 00b65da4 bytes bf221e39
- 00b65d7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65d7c ["INT_ADD", "register:40f0:8", ["const:b65d7c:8", "const:4:8"]]
- 00b65d7c ["CALLIND", null, ["register:0:8"]]
+ 00b65dc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65dc0 ["INT_ADD", "register:40f0:8", ["const:b65dc0:8", "const:4:8"]]
+ 00b65dc0 ["CALLIND", null, ["register:0:8"]]
- 00b65d7c bytes 00013fd6
+ 00b65dc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81cf412b9f10f4206cc5fb0bc8974def"></a>

### [`00b65d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d94.md) → [`00b65dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md) _ZN8firebase4auth12facebookcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b65e18",
      "incomplete_value": true,
      "site": "00b65e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65dd4",
      "incomplete_value": true,
      "site": "00b65dd4",
      "value": [
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
      "definition_site": "00b65df4",
      "incomplete_value": true,
      "site": "00b65df4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65db0",
      "incomplete_value": true,
      "site": "00b65db0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65db0"
      ],
      [
        "FALL_THROUGH",
        "00b65df4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65df4",
      "incomplete_value": true,
      "site": "00b65e18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65db0",
      "incomplete_value": true,
      "site": "00b65dd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65dec",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e18",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e2c",
      "PARAM",
      [
        "storage",
        "00c123a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b65dec",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e18",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e2c",
      "PARAM",
      [
        "storage",
        "00c123f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d94.md#insn-00b65dd4) · [`00b65da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d94.md#insn-00b65da8) · [`00b65dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d94.md#insn-00b65dcc)
- 新版 `00b65e18`（命令位置の公開資料なし） · `00b65dec`（命令位置の公開資料なし） · `00b65e10`（命令位置の公開資料なし）

~~~diff
- 00b65dd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65e18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b65e18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65dd4 bytes 80a203f9
+ 00b65e18 bytes 80c203f9
- 00b65da8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65da8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65dec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b65dec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65da8 bytes 81a243f9
+ 00b65dec bytes 81c243f9
- 00b65dcc ["INT_ADD", "register:40f0:8", ["const:b65dcc:8", "const:4:8"]]
- 00b65dcc ["CALL", null, ["callee:00bde090:8"]]
+ 00b65e10 ["INT_ADD", "register:40f0:8", ["const:b65e10:8", "const:4:8"]]
+ 00b65e10 ["CALL", null, ["callee:00bde090:8"]]
- 00b65dcc bytes 9de00194
+ 00b65e10 bytes a0e00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daff7c72ba85c5ce8e9c56ab44282700"></a>

### [`00b65e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e04.md) → [`00b65e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e48.md) _ZN8firebase4auth12facebookcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b65e64",
      "incomplete_value": false,
      "site": "00b65e68",
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
    "old": {
      "definition_site": "00b65e20",
      "incomplete_value": false,
      "site": "00b65e24",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65e74",
      "incomplete_value": true,
      "site": "00b65e80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65e30",
      "incomplete_value": true,
      "site": "00b65e3c",
      "value": [
        "LOAD",
        "8",
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
      "00b65e64",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b65e74",
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
      "00b65e64",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65e74",
      "DATA",
      [
        "storage",
        "010a1790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e04.md#insn-00b65e24) · [`00b65e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e04.md#insn-00b65e20) · [`00b65e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e04.md#insn-00b65e2c)
- 新版 `00b65e68`（命令位置の公開資料なし） · `00b65e64`（命令位置の公開資料なし） · `00b65e70`（命令位置の公開資料なし）

~~~diff
- 00b65e24 ["INT_ADD", "register:40f0:8", ["const:b65e24:8", "const:4:8"]]
- 00b65e24 ["CALL", null, ["callee:00bde180:8"]]
+ 00b65e68 ["INT_ADD", "register:40f0:8", ["const:b65e68:8", "const:4:8"]]
+ 00b65e68 ["CALL", null, ["callee:00bde180:8"]]
- 00b65e24 bytes c3e00194
+ 00b65e68 bytes c6e00194
- 00b65e20 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b65e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65e64 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b65e64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65e20 bytes 00501791
+ 00b65e64 bytes 001c1591
- 00b65e2c ["COPY", "tmp:0:8", ["const:750:8"]]
- 00b65e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65e70 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00b65e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65e2c bytes 08411d91
+ 00b65e70 bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-599cabc18ce3c2861b9ddd925f69ca1d"></a>

### [`00b65e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e40.md) → [`00b65e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md) _ZN8firebase4auth12facebookcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65ec4",
      "incomplete_value": true,
      "site": "00b65ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e80",
      "incomplete_value": true,
      "site": "00b65e80",
      "value": [
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
      "definition_site": "00b65ea0",
      "incomplete_value": true,
      "site": "00b65ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e5c",
      "incomplete_value": true,
      "site": "00b65e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65e5c"
      ],
      [
        "FALL_THROUGH",
        "00b65ea0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65ea0",
      "incomplete_value": true,
      "site": "00b65ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e5c",
      "incomplete_value": true,
      "site": "00b65e80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65e98",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ec4",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65edc",
      "PARAM",
      [
        "storage",
        "010a1758",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65e98",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ec4",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65edc",
      "PARAM",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e40.md#insn-00b65e80) · [`00b65e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e40.md#insn-00b65e54) · [`00b65e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e40.md#insn-00b65e78)
- 新版 `00b65ec4`（命令位置の公開資料なし） · `00b65e98`（命令位置の公開資料なし） · `00b65ebc`（命令位置の公開資料なし）

~~~diff
- 00b65e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65ec4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b65ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e80 bytes 80a203f9
+ 00b65ec4 bytes 80c203f9
- 00b65e54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65e54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65e98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b65e98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65e54 bytes 81a243f9
+ 00b65e98 bytes 81c243f9
- 00b65e78 ["INT_ADD", "register:40f0:8", ["const:b65e78:8", "const:4:8"]]
- 00b65e78 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65ebc ["INT_ADD", "register:40f0:8", ["const:b65ebc:8", "const:4:8"]]
+ 00b65ebc ["CALL", null, ["callee:00bde090:8"]]
- 00b65e78 bytes 72e00194
+ 00b65ebc bytes 75e00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c7eeca99de76d869880fcdcd738cb3c"></a>

### [`00b65eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eb0.md) → [`00b65ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ef4.md) _ZN8firebase4auth12facebookcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b65f10",
      "incomplete_value": false,
      "site": "00b65f14",
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
    "old": {
      "definition_site": "00b65ecc",
      "incomplete_value": false,
      "site": "00b65ed0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65f20",
      "incomplete_value": true,
      "site": "00b65f2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65edc",
      "incomplete_value": true,
      "site": "00b65ee8",
      "value": [
        "LOAD",
        "8",
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
      "00b65f10",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65f20",
      "DATA",
      [
        "storage",
        "010a1758",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65f10",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65f20",
      "DATA",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eb0.md#insn-00b65ed0) · [`00b65ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eb0.md#insn-00b65ecc) · [`00b65ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eb0.md#insn-00b65ed8)
- 新版 `00b65f14`（命令位置の公開資料なし） · `00b65f10`（命令位置の公開資料なし） · `00b65f1c`（命令位置の公開資料なし）

~~~diff
- 00b65ed0 ["INT_ADD", "register:40f0:8", ["const:b65ed0:8", "const:4:8"]]
- 00b65ed0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b65f14 ["INT_ADD", "register:40f0:8", ["const:b65f14:8", "const:4:8"]]
+ 00b65f14 ["CALL", null, ["callee:00bde180:8"]]
- 00b65ed0 bytes 98e00194
+ 00b65f14 bytes 9be00194
- 00b65ecc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b65ecc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65ecc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65ecc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65f10 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b65f10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65ecc bytes 00fc1991
+ 00b65f10 bytes 00c81791
- 00b65ed8 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00b65ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65f1c ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00b65f1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65f1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65f1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65ed8 bytes 08611d91
+ 00b65f1c bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5181a47a57e81ed2829b06431e9e90f"></a>

### [`00b65eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eec.md) → [`00b65f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f30.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b65f5c",
      "incomplete_value": true,
      "site": "00b65f5c",
      "value": [
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
    "old": {
      "definition_site": "00b65f18",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
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
      "definition_site": "00b65f44",
      "incomplete_value": true,
      "site": "00b65f44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f00",
      "incomplete_value": true,
      "site": "00b65f00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65f00"
      ],
      [
        "FALL_THROUGH",
        "00b65f44"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65f44",
      "incomplete_value": true,
      "site": "00b65f5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f00",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65f40",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f5c",
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
      "00b65f40",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f5c",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eec.md#insn-00b65f18) · [`00b65efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eec.md#insn-00b65efc) · [`00b65f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eec.md#insn-00b65f10)
- 新版 `00b65f5c`（命令位置の公開資料なし） · `00b65f40`（命令位置の公開資料なし） · `00b65f54`（命令位置の公開資料なし）

~~~diff
- 00b65f18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65f5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f18 bytes 60b203f9
+ 00b65f5c bytes 60d203f9
- 00b65efc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65efc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65f40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65f40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65efc bytes 68b243f9
+ 00b65f40 bytes 68d243f9
- 00b65f10 ["INT_ADD", "register:40f0:8", ["const:b65f10:8", "const:4:8"]]
- 00b65f10 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65f54 ["INT_ADD", "register:40f0:8", ["const:b65f54:8", "const:4:8"]]
+ 00b65f54 ["CALL", null, ["callee:00bde090:8"]]
- 00b65f10 bytes 4ce00194
+ 00b65f54 bytes 4fe00194
~~~


<a id="compare-fcf46e84b5bbb467ccf485ff222ea529"></a>

### [`00b65f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f2c.md) → [`00b65f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b65f58",
      "incomplete_value": true,
      "site": "00b65f58",
      "value": [
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
    "old": {
      "definition_site": "00b65f40",
      "incomplete_value": true,
      "site": "00b65f40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65f40"
      ],
      [
        "FALL_THROUGH",
        "00b65f84"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65f84",
      "incomplete_value": true,
      "site": "00b65f9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f40",
      "incomplete_value": true,
      "site": "00b65f58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65f80",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f9c",
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
      "00b65f80",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f9c",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f2c.md#insn-00b65f58) · [`00b65f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f2c.md#insn-00b65f3c) · [`00b65f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f2c.md#insn-00b65f50)
- 新版 `00b65f9c`（命令位置の公開資料なし） · `00b65f80`（命令位置の公開資料なし） · `00b65f94`（命令位置の公開資料なし）

~~~diff
- 00b65f58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f58 bytes 60b203f9
+ 00b65f9c bytes 60d203f9
- 00b65f3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65f3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65f80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65f80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65f3c bytes 68b243f9
+ 00b65f80 bytes 68d243f9
- 00b65f50 ["INT_ADD", "register:40f0:8", ["const:b65f50:8", "const:4:8"]]
- 00b65f50 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65f94 ["INT_ADD", "register:40f0:8", ["const:b65f94:8", "const:4:8"]]
+ 00b65f94 ["CALL", null, ["callee:00bde090:8"]]
- 00b65f50 bytes 3ce00194
+ 00b65f94 bytes 3fe00194
~~~


<a id="compare-a3d78a518cd7f7a6579be43e1c49a94f"></a>

### [`00b65f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f6c.md) → [`00b65fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b65f80",
      "incomplete_value": true,
      "site": "00b65f80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65f80"
      ],
      [
        "FALL_THROUGH",
        "00b65fc4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65fc4",
      "incomplete_value": true,
      "site": "00b65fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f80",
      "incomplete_value": true,
      "site": "00b65f9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65fc0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fe0",
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
      "00b65fc0",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fe0",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f6c.md#insn-00b65f9c) · [`00b65f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f6c.md#insn-00b65f7c) · [`00b65f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f6c.md#insn-00b65f94)
- 新版 `00b65fe0`（命令位置の公開資料なし） · `00b65fc0`（命令位置の公開資料なし） · `00b65fd8`（命令位置の公開資料なし）

~~~diff
- 00b65f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f9c bytes 60b203f9
+ 00b65fe0 bytes 60d203f9
- 00b65f7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65f7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65fc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b65fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65f7c bytes 68b243f9
+ 00b65fc0 bytes 68d243f9
- 00b65f94 ["INT_ADD", "register:40f0:8", ["const:b65f94:8", "const:4:8"]]
- 00b65f94 ["CALL", null, ["callee:00bde090:8"]]
+ 00b65fd8 ["INT_ADD", "register:40f0:8", ["const:b65fd8:8", "const:4:8"]]
+ 00b65fd8 ["CALL", null, ["callee:00bde090:8"]]
- 00b65f94 bytes 2be00194
+ 00b65fd8 bytes 2ee00194
~~~


<a id="compare-133eb118629e8d8acf6d75328c91c300"></a>

### [`00b65fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65fb0.md) → [`00b65ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b66024",
      "incomplete_value": true,
      "site": "00b66024",
      "value": [
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b65fc4"
      ],
      [
        "FALL_THROUGH",
        "00b66008"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66008",
      "incomplete_value": true,
      "site": "00b66024",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "site": "00b65fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66004",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66024",
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
      "00b66004",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66024",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65fb0.md#insn-00b65fe0) · [`00b65fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65fb0.md#insn-00b65fc0) · [`00b65fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65fb0.md#insn-00b65fd8)
- 新版 `00b66024`（命令位置の公開資料なし） · `00b66004`（命令位置の公開資料なし） · `00b6601c`（命令位置の公開資料なし）

~~~diff
- 00b65fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b66024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65fe0 bytes 60b203f9
+ 00b66024 bytes 60d203f9
- 00b65fc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b66004 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65fc0 bytes 68b243f9
+ 00b66004 bytes 68d243f9
- 00b65fd8 ["INT_ADD", "register:40f0:8", ["const:b65fd8:8", "const:4:8"]]
- 00b65fd8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6601c ["INT_ADD", "register:40f0:8", ["const:b6601c:8", "const:4:8"]]
+ 00b6601c ["CALL", null, ["callee:00bde090:8"]]
- 00b65fd8 bytes 1ae00194
+ 00b6601c bytes 1de00194
~~~


<a id="compare-b02d7ad68341dbab9e333d362d45344c"></a>

### [`00b65ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ff4.md) → [`00b66038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66038.md) _ZN8firebase4auth10githubcred8GetClassEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b6603c",
      "incomplete_value": true,
      "site": "00b66040",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ff8",
      "incomplete_value": true,
      "site": "00b65ffc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:760:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6603c",
      "READ",
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
      "00b6603c",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ff4.md#insn-00b65ff8)
- 新版 `00b6603c`（命令位置の公開資料なし）

~~~diff
- 00b65ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:760:8"]]
- 00b65ff8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6603c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7a0:8"]]
+ 00b6603c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65ff8 bytes 00b143f9
+ 00b6603c bytes 00d143f9
~~~


<a id="compare-a0467db5746cb05afdf7905a5290e10b"></a>

### [`00b66000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66000.md) → [`00b66044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66044.md) _ZN8firebase4auth10githubcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b6609c",
      "incomplete_value": true,
      "site": "00b6609c",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66058",
      "incomplete_value": true,
      "site": "00b66058",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66078",
      "incomplete_value": true,
      "site": "00b66084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b66034",
      "incomplete_value": true,
      "site": "00b66040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b66058",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66078",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6609c",
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
      "00b66058",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66078",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6609c",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66000.md#insn-00b66014) · [`00b66040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66000.md#insn-00b66040) · [`00b66058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66000.md#insn-00b66058)
- 新版 `00b66058`（命令位置の公開資料なし） · `00b66084`（命令位置の公開資料なし） · `00b6609c`（命令位置の公開資料なし）

~~~diff
- 00b66014 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:768:8"]]
- 00b66014 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66014 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b66058 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a8:8"]]
+ 00b66058 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b66058 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66014 bytes a8a25d39
+ 00b66058 bytes a8a25e39
- 00b66040 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66040 ["INT_ADD", "register:40f0:8", ["const:b66040:8", "const:4:8"]]
- 00b66040 ["CALLIND", null, ["register:0:8"]]
+ 00b66084 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66084 ["INT_ADD", "register:40f0:8", ["const:b66084:8", "const:4:8"]]
+ 00b66084 ["CALLIND", null, ["register:0:8"]]
- 00b66040 bytes 00013fd6
+ 00b66084 bytes 00013fd6
- 00b66058 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66058 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:768:8"]]
- 00b66058 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6609c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6609c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a8:8"]]
+ 00b6609c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66058 bytes a0a21d39
+ 00b6609c bytes a0a21e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fe8f5e0904366c2dca68327b103e64a"></a>

### [`00b6606c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6606c.md) → [`00b660b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md) _ZN8firebase4auth10githubcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660a8",
      "incomplete_value": true,
      "site": "00b660a8",
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
      "definition_site": "00b6610c",
      "incomplete_value": true,
      "site": "00b6610c",
      "value": [
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
    "old": {
      "definition_site": "00b660c8",
      "incomplete_value": true,
      "site": "00b660c8",
      "value": [
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
      "definition_site": "00b660c8",
      "incomplete_value": true,
      "site": "00b660c8",
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
      "definition_site": "00b66084",
      "incomplete_value": true,
      "site": "00b66084",
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
      "00b660c4",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660d0",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b660ec",
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
      "00b660c4",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660d0",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b660ec",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6606c.md#insn-00b66080) · [`00b660a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6606c.md#insn-00b660a8) · [`00b660c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6606c.md#insn-00b660c4)
- 新版 `00b660c4`（命令位置の公開資料なし） · `00b660ec`（命令位置の公開資料なし） · `00b66108`（命令位置の公開資料なし）

~~~diff
- 00b66080 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b66080 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b660c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b660c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66080 bytes 81b243f9
+ 00b660c4 bytes 81d243f9
- 00b660a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b660a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b660a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:768:8"]]
- 00b660a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b660ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b660ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b660ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a8:8"]]
+ 00b660ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b660a8 bytes bfa21d39
+ 00b660ec bytes bfa21e39
- 00b660c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b660c4 ["INT_ADD", "register:40f0:8", ["const:b660c4:8", "const:4:8"]]
- 00b660c4 ["CALLIND", null, ["register:0:8"]]
+ 00b66108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66108 ["INT_ADD", "register:40f0:8", ["const:b66108:8", "const:4:8"]]
+ 00b66108 ["CALLIND", null, ["register:0:8"]]
- 00b660c4 bytes 00013fd6
+ 00b66108 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f45440e1f802f76e80be87342a3a52"></a>

### [`00b660dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b660dc.md) → [`00b66120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md) _ZN8firebase4auth10githubcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
    "old": {
      "definition_site": "00b6611c",
      "incomplete_value": true,
      "site": "00b6611c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b660f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b660f8"
      ],
      [
        "FALL_THROUGH",
        "00b6613c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6613c",
      "incomplete_value": true,
      "site": "00b66160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b6611c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66134",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66160",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66174",
      "PARAM",
      [
        "storage",
        "00c123c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b66134",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66160",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66174",
      "PARAM",
      [
        "storage",
        "00c12410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6611c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b660dc.md#insn-00b6611c) · [`00b660f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b660dc.md#insn-00b660f0) · [`00b66114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b660dc.md#insn-00b66114)
- 新版 `00b66160`（命令位置の公開資料なし） · `00b66134`（命令位置の公開資料なし） · `00b66158`（命令位置の公開資料なし）

~~~diff
- 00b6611c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b6611c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b66160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6611c bytes 80b203f9
+ 00b66160 bytes 80d203f9
- 00b660f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b660f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66134 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b66134 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b660f0 bytes 81b243f9
+ 00b66134 bytes 81d243f9
- 00b66114 ["INT_ADD", "register:40f0:8", ["const:b66114:8", "const:4:8"]]
- 00b66114 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66158 ["INT_ADD", "register:40f0:8", ["const:b66158:8", "const:4:8"]]
+ 00b66158 ["CALL", null, ["callee:00bde090:8"]]
- 00b66114 bytes cbdf0194
+ 00b66158 bytes cedf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f2fe334ccb76b9da4612ad8ce868e4"></a>

### [`00b6614c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6614c.md) → [`00b66190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66190.md) _ZN8firebase4auth10githubcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b661ac",
      "incomplete_value": false,
      "site": "00b661b0",
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
    "old": {
      "definition_site": "00b66168",
      "incomplete_value": false,
      "site": "00b6616c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b661bc",
      "incomplete_value": true,
      "site": "00b661c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66178",
      "incomplete_value": true,
      "site": "00b66184",
      "value": [
        "LOAD",
        "8",
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
      "00b661ac",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b661bc",
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
      "00b661ac",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b661bc",
      "DATA",
      [
        "storage",
        "010a17b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6616c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6614c.md#insn-00b6616c) · [`00b66168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6614c.md#insn-00b66168) · [`00b66174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6614c.md#insn-00b66174)
- 新版 `00b661b0`（命令位置の公開資料なし） · `00b661ac`（命令位置の公開資料なし） · `00b661b8`（命令位置の公開資料なし）

~~~diff
- 00b6616c ["INT_ADD", "register:40f0:8", ["const:b6616c:8", "const:4:8"]]
- 00b6616c ["CALL", null, ["callee:00bde180:8"]]
+ 00b661b0 ["INT_ADD", "register:40f0:8", ["const:b661b0:8", "const:4:8"]]
+ 00b661b0 ["CALL", null, ["callee:00bde180:8"]]
- 00b6616c bytes f1df0194
+ 00b661b0 bytes f4df0194
- 00b66168 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b66168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b661ac ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b661ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b661ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b661ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66168 bytes 00501791
+ 00b661ac bytes 001c1591
- 00b66174 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00b66174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b661b8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00b661b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b661b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b661b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66174 bytes 08c11d91
+ 00b661b8 bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb96a8a74e924051a7b4e00923a14ae"></a>

### [`00b66188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66188.md) → [`00b661cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md) _ZN8firebase4auth10githubcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b6620c",
      "incomplete_value": true,
      "site": "00b6620c",
      "value": [
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
    "old": {
      "definition_site": "00b661c8",
      "incomplete_value": true,
      "site": "00b661c8",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b661e8",
      "incomplete_value": true,
      "site": "00b661e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b661a4",
      "incomplete_value": true,
      "site": "00b661a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b661a4"
      ],
      [
        "FALL_THROUGH",
        "00b661e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b661e8",
      "incomplete_value": true,
      "site": "00b6620c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b661a4",
      "incomplete_value": true,
      "site": "00b661c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b661e0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6620c",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66224",
      "PARAM",
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
      "00b661e0",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6620c",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66224",
      "PARAM",
      [
        "storage",
        "010a17b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b661c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66188.md#insn-00b661c8) · [`00b6619c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66188.md#insn-00b6619c) · [`00b661c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66188.md#insn-00b661c0)
- 新版 `00b6620c`（命令位置の公開資料なし） · `00b661e0`（命令位置の公開資料なし） · `00b66204`（命令位置の公開資料なし）

~~~diff
- 00b661c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b661c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6620c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b6620c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b661c8 bytes 80b203f9
+ 00b6620c bytes 80d203f9
- 00b6619c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b6619c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b661e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b661e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6619c bytes 81b243f9
+ 00b661e0 bytes 81d243f9
- 00b661c0 ["INT_ADD", "register:40f0:8", ["const:b661c0:8", "const:4:8"]]
- 00b661c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66204 ["INT_ADD", "register:40f0:8", ["const:b66204:8", "const:4:8"]]
+ 00b66204 ["CALL", null, ["callee:00bde090:8"]]
- 00b661c0 bytes a0df0194
+ 00b66204 bytes a3df0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bdb7c016ca89ab44882e9f5cd7fdc0c"></a>

### [`00b661f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b661f8.md) → [`00b6623c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6623c.md) _ZN8firebase4auth10githubcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b66258",
      "incomplete_value": false,
      "site": "00b6625c",
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
    "old": {
      "definition_site": "00b66214",
      "incomplete_value": false,
      "site": "00b66218",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66268",
      "incomplete_value": true,
      "site": "00b66274",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66224",
      "incomplete_value": true,
      "site": "00b66230",
      "value": [
        "LOAD",
        "8",
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
      "00b66258",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b66268",
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
      "00b66258",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b66268",
      "DATA",
      [
        "storage",
        "010a17b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b661f8.md#insn-00b66218) · [`00b66214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b661f8.md#insn-00b66214) · [`00b66220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b661f8.md#insn-00b66220)
- 新版 `00b6625c`（命令位置の公開資料なし） · `00b66258`（命令位置の公開資料なし） · `00b66264`（命令位置の公開資料なし）

~~~diff
- 00b66218 ["INT_ADD", "register:40f0:8", ["const:b66218:8", "const:4:8"]]
- 00b66218 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6625c ["INT_ADD", "register:40f0:8", ["const:b6625c:8", "const:4:8"]]
+ 00b6625c ["CALL", null, ["callee:00bde180:8"]]
- 00b66218 bytes c6df0194
+ 00b6625c bytes c9df0194
- 00b66214 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b66214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66258 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b66258 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66258 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66258 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66214 bytes 00fc1991
+ 00b66258 bytes 00c81791
- 00b66220 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00b66220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66264 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00b66264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66220 bytes 08e11d91
+ 00b66264 bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fefd2b0b4e0905c3d29aa227b7084dd"></a>

### [`00b66234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66234.md) → [`00b66278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66260",
      "incomplete_value": true,
      "site": "00b66260",
      "value": [
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
    "old": {
      "definition_site": "00b66248",
      "incomplete_value": true,
      "site": "00b66248",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66248"
      ],
      [
        "FALL_THROUGH",
        "00b6628c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6628c",
      "incomplete_value": true,
      "site": "00b662a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66248",
      "incomplete_value": true,
      "site": "00b66260",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66288",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662a4",
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
      "00b66288",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662a4",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66234.md#insn-00b66260) · [`00b66244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66234.md#insn-00b66244) · [`00b66258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66234.md#insn-00b66258)
- 新版 `00b662a4`（命令位置の公開資料なし） · `00b66288`（命令位置の公開資料なし） · `00b6629c`（命令位置の公開資料なし）

~~~diff
- 00b66260 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b66260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b662a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b662a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66260 bytes 60c203f9
+ 00b662a4 bytes 60e203f9
- 00b66244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b66244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66288 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66244 bytes 68c243f9
+ 00b66288 bytes 68e243f9
- 00b66258 ["INT_ADD", "register:40f0:8", ["const:b66258:8", "const:4:8"]]
- 00b66258 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6629c ["INT_ADD", "register:40f0:8", ["const:b6629c:8", "const:4:8"]]
+ 00b6629c ["CALL", null, ["callee:00bde090:8"]]
- 00b66258 bytes 7adf0194
+ 00b6629c bytes 7ddf0194
~~~


<a id="compare-f0d91b072f04df8ebef57885cfcc4bc4"></a>

### [`00b66274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66274.md) → [`00b662b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b662a0",
      "incomplete_value": true,
      "site": "00b662a0",
      "value": [
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
    "old": {
      "definition_site": "00b66288",
      "incomplete_value": true,
      "site": "00b66288",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66288"
      ],
      [
        "FALL_THROUGH",
        "00b662cc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b662cc",
      "incomplete_value": true,
      "site": "00b662e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66288",
      "incomplete_value": true,
      "site": "00b662a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b662c8",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662e4",
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
      "00b662c8",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662e4",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b662a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66274.md#insn-00b662a0) · [`00b66284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66274.md#insn-00b66284) · [`00b66298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66274.md#insn-00b66298)
- 新版 `00b662e4`（命令位置の公開資料なし） · `00b662c8`（命令位置の公開資料なし） · `00b662dc`（命令位置の公開資料なし）

~~~diff
- 00b662a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b662a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b662e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b662e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b662a0 bytes 60c203f9
+ 00b662e4 bytes 60e203f9
- 00b66284 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b66284 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b662c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b662c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66284 bytes 68c243f9
+ 00b662c8 bytes 68e243f9
- 00b66298 ["INT_ADD", "register:40f0:8", ["const:b66298:8", "const:4:8"]]
- 00b66298 ["CALL", null, ["callee:00bde090:8"]]
+ 00b662dc ["INT_ADD", "register:40f0:8", ["const:b662dc:8", "const:4:8"]]
+ 00b662dc ["CALL", null, ["callee:00bde090:8"]]
- 00b66298 bytes 6adf0194
+ 00b662dc bytes 6ddf0194
~~~


<a id="compare-ce0f4936ea0d8428bb024c5856f9b209"></a>

### [`00b662b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662b4.md) → [`00b662f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b662c8",
      "incomplete_value": true,
      "site": "00b662c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b662c8"
      ],
      [
        "FALL_THROUGH",
        "00b6630c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6630c",
      "incomplete_value": true,
      "site": "00b66328",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662c8",
      "incomplete_value": true,
      "site": "00b662e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66308",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66328",
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
      "00b66308",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66328",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b662e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662b4.md#insn-00b662e4) · [`00b662c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662b4.md#insn-00b662c4) · [`00b662dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662b4.md#insn-00b662dc)
- 新版 `00b66328`（命令位置の公開資料なし） · `00b66308`（命令位置の公開資料なし） · `00b66320`（命令位置の公開資料なし）

~~~diff
- 00b662e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b662e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b662e4 bytes 60c203f9
+ 00b66328 bytes 60e203f9
- 00b662c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b662c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66308 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b662c4 bytes 68c243f9
+ 00b66308 bytes 68e243f9
- 00b662dc ["INT_ADD", "register:40f0:8", ["const:b662dc:8", "const:4:8"]]
- 00b662dc ["CALL", null, ["callee:00bde090:8"]]
+ 00b66320 ["INT_ADD", "register:40f0:8", ["const:b66320:8", "const:4:8"]]
+ 00b66320 ["CALL", null, ["callee:00bde090:8"]]
- 00b662dc bytes 59df0194
+ 00b66320 bytes 5cdf0194
~~~


<a id="compare-6fe2d11f91193c8162a94337ea15cb29"></a>

### [`00b662f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662f8.md) → [`00b6633c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b6636c",
      "incomplete_value": true,
      "site": "00b6636c",
      "value": [
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
      "definition_site": "00b66350",
      "incomplete_value": true,
      "site": "00b66350",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b6630c"
      ],
      [
        "FALL_THROUGH",
        "00b66350"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66350",
      "incomplete_value": true,
      "site": "00b6636c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "site": "00b66328",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6634c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6636c",
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
      "00b6634c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6636c",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662f8.md#insn-00b66328) · [`00b66308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662f8.md#insn-00b66308) · [`00b66320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662f8.md#insn-00b66320)
- 新版 `00b6636c`（命令位置の公開資料なし） · `00b6634c`（命令位置の公開資料なし） · `00b66364`（命令位置の公開資料なし）

~~~diff
- 00b66328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b66328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6636c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b6636c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66328 bytes 60c203f9
+ 00b6636c bytes 60e203f9
- 00b66308 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b66308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6634c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b6634c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66308 bytes 68c243f9
+ 00b6634c bytes 68e243f9
- 00b66320 ["INT_ADD", "register:40f0:8", ["const:b66320:8", "const:4:8"]]
- 00b66320 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66364 ["INT_ADD", "register:40f0:8", ["const:b66364:8", "const:4:8"]]
+ 00b66364 ["CALL", null, ["callee:00bde090:8"]]
- 00b66320 bytes 48df0194
+ 00b66364 bytes 4bdf0194
~~~


<a id="compare-bf4c933706c4a02d9166b7abfdab0f79"></a>

### [`00b66348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66348.md) → [`00b6638c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md) _ZN8firebase4auth10googlecred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b663a0",
      "incomplete_value": true,
      "site": "00b663a0",
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
            "const:788:8"
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
    "old": {
      "definition_site": "00b6637c",
      "incomplete_value": true,
      "site": "00b66388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b663a0",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b663c0",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663e4",
      "WRITE",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b663a0",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b663c0",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663e4",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66348.md#insn-00b6635c) · [`00b66388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66348.md#insn-00b66388) · [`00b663a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66348.md#insn-00b663a0)
- 新版 `00b663a0`（命令位置の公開資料なし） · `00b663cc`（命令位置の公開資料なし） · `00b663e4`（命令位置の公開資料なし）

~~~diff
- 00b6635c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
- 00b6635c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6635c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b663a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b663a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b663a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6635c bytes a8225e39
+ 00b663a0 bytes a8225f39
- 00b66388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66388 ["INT_ADD", "register:40f0:8", ["const:b66388:8", "const:4:8"]]
- 00b66388 ["CALLIND", null, ["register:0:8"]]
+ 00b663cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b663cc ["INT_ADD", "register:40f0:8", ["const:b663cc:8", "const:4:8"]]
+ 00b663cc ["CALLIND", null, ["register:0:8"]]
- 00b66388 bytes 00013fd6
+ 00b663cc bytes 00013fd6
- 00b663a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b663a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
- 00b663a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b663e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b663e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b663e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b663a0 bytes a0221e39
+ 00b663e4 bytes a0221f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a73934d3e0337f25a7553a0b24ee22"></a>

### [`00b663b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b663b4.md) → [`00b663f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md) _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b66434",
      "incomplete_value": true,
      "site": "00b66434",
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
    "old": {
      "definition_site": "00b663f0",
      "incomplete_value": true,
      "site": "00b663f0",
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
            "const:788:8"
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
      "definition_site": "00b66454",
      "incomplete_value": true,
      "site": "00b66454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66410",
      "incomplete_value": true,
      "site": "00b66410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "00b66410",
      "incomplete_value": true,
      "site": "00b66410",
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
      "definition_site": "00b663cc",
      "incomplete_value": true,
      "site": "00b663cc",
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
      "00b6640c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66418",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66434",
      "WRITE",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6640c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66418",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66434",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b663c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b663b4.md#insn-00b663c8) · [`00b663f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b663b4.md#insn-00b663f0) · [`00b6640c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b663b4.md#insn-00b6640c)
- 新版 `00b6640c`（命令位置の公開資料なし） · `00b66434`（命令位置の公開資料なし） · `00b66450`（命令位置の公開資料なし）

~~~diff
- 00b663c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b663c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6640c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b6640c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b663c8 bytes 81c243f9
+ 00b6640c bytes 81e243f9
- 00b663f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b663f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b663f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
- 00b663f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66434 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66434 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66434 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b66434 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b663f0 bytes bf221e39
+ 00b66434 bytes bf221f39
- 00b6640c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6640c ["INT_ADD", "register:40f0:8", ["const:b6640c:8", "const:4:8"]]
- 00b6640c ["CALLIND", null, ["register:0:8"]]
+ 00b66450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66450 ["INT_ADD", "register:40f0:8", ["const:b66450:8", "const:4:8"]]
+ 00b66450 ["CALLIND", null, ["register:0:8"]]
- 00b6640c bytes 00013fd6
+ 00b66450 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6947d7cf1809d01058a2f6f24e6315c3"></a>

### [`00b66424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66424.md) → [`00b66468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md) _ZN8firebase4auth10googlecred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b664a8",
      "incomplete_value": true,
      "site": "00b664a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66464",
      "incomplete_value": true,
      "site": "00b66464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "00b66484",
      "incomplete_value": true,
      "site": "00b66484",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66440",
      "incomplete_value": true,
      "site": "00b66440",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66440"
      ],
      [
        "FALL_THROUGH",
        "00b66484"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66484",
      "incomplete_value": true,
      "site": "00b664a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66440",
      "incomplete_value": true,
      "site": "00b66464",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6647c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b664a8",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b664bc",
      "PARAM",
      [
        "storage",
        "00c123d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6647c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b664a8",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b664bc",
      "PARAM",
      [
        "storage",
        "00c12428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66424.md#insn-00b66464) · [`00b66438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66424.md#insn-00b66438) · [`00b6645c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66424.md#insn-00b6645c)
- 新版 `00b664a8`（命令位置の公開資料なし） · `00b6647c`（命令位置の公開資料なし） · `00b664a0`（命令位置の公開資料なし）

~~~diff
- 00b66464 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b66464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b664a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b664a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66464 bytes 80c203f9
+ 00b664a8 bytes 80e203f9
- 00b66438 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b66438 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6647c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b6647c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66438 bytes 81c243f9
+ 00b6647c bytes 81e243f9
- 00b6645c ["INT_ADD", "register:40f0:8", ["const:b6645c:8", "const:4:8"]]
- 00b6645c ["CALL", null, ["callee:00bde090:8"]]
+ 00b664a0 ["INT_ADD", "register:40f0:8", ["const:b664a0:8", "const:4:8"]]
+ 00b664a0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6645c bytes f9de0194
+ 00b664a0 bytes fcde0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6726d05995fe6ee0c4d49446a4ce8cda"></a>

### [`00b66494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md) → [`00b664d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b664d8.md) _ZN8firebase4auth10googlecred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b664f4",
      "incomplete_value": false,
      "site": "00b664f8",
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
    "old": {
      "definition_site": "00b664b0",
      "incomplete_value": false,
      "site": "00b664b4",
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
      "00b664f4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66504",
      "DATA",
      [
        "storage",
        "010a1790",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b664f4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66504",
      "DATA",
      [
        "storage",
        "010a17d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b664b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md#insn-00b664b4) · [`00b664b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md#insn-00b664b0) · [`00b664bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md#insn-00b664bc)
- 新版 `00b664f8`（命令位置の公開資料なし） · `00b664f4`（命令位置の公開資料なし） · `00b66500`（命令位置の公開資料なし）

~~~diff
- 00b664b4 ["INT_ADD", "register:40f0:8", ["const:b664b4:8", "const:4:8"]]
- 00b664b4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b664f8 ["INT_ADD", "register:40f0:8", ["const:b664f8:8", "const:4:8"]]
+ 00b664f8 ["CALL", null, ["callee:00bde180:8"]]
- 00b664b4 bytes 1fdf0194
+ 00b664f8 bytes 22df0194
- 00b664b0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b664b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b664b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b664b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b664f4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b664f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b664f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b664f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b664b0 bytes 00501791
+ 00b664f4 bytes 001c1591
- 00b664bc ["COPY", "tmp:0:8", ["const:790:8"]]
- 00b664bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b664bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b664bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66500 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00b66500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b664bc bytes 08411e91
+ 00b66500 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e11718c99450da3956cf7d502b94c011"></a>

### [`00b664d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b664d0.md) → [`00b66514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md) _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b66554",
      "incomplete_value": true,
      "site": "00b66554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66510",
      "incomplete_value": true,
      "site": "00b66510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "00b66530",
      "incomplete_value": true,
      "site": "00b66530",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b664ec",
      "incomplete_value": true,
      "site": "00b664ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b664ec"
      ],
      [
        "FALL_THROUGH",
        "00b66530"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66530",
      "incomplete_value": true,
      "site": "00b66554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b664ec",
      "incomplete_value": true,
      "site": "00b66510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66528",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66554",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6656c",
      "PARAM",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66528",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66554",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6656c",
      "PARAM",
      [
        "storage",
        "010a17d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b664d0.md#insn-00b66510) · [`00b664e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b664d0.md#insn-00b664e4) · [`00b66508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b664d0.md#insn-00b66508)
- 新版 `00b66554`（命令位置の公開資料なし） · `00b66528`（命令位置の公開資料なし） · `00b6654c`（命令位置の公開資料なし）

~~~diff
- 00b66510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b66510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66510 bytes 80c203f9
+ 00b66554 bytes 80e203f9
- 00b664e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b664e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66528 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66528 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b664e4 bytes 81c243f9
+ 00b66528 bytes 81e243f9
- 00b66508 ["INT_ADD", "register:40f0:8", ["const:b66508:8", "const:4:8"]]
- 00b66508 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6654c ["INT_ADD", "register:40f0:8", ["const:b6654c:8", "const:4:8"]]
+ 00b6654c ["CALL", null, ["callee:00bde090:8"]]
- 00b66508 bytes cede0194
+ 00b6654c bytes d1de0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a0aa804d9fe8b254209c85f68fcf96c"></a>

### [`00b66540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66540.md) → [`00b66584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md) _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b6655c",
      "incomplete_value": false,
      "site": "00b66560",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6656c",
      "incomplete_value": true,
      "site": "00b66578",
      "value": [
        "LOAD",
        "8",
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
      "00b665a0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b665b0",
      "DATA",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b665a0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b665b0",
      "DATA",
      [
        "storage",
        "010a17d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66540.md#insn-00b66560) · [`00b6655c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66540.md#insn-00b6655c) · [`00b66568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66540.md#insn-00b66568)
- 新版 `00b665a4`（命令位置の公開資料なし） · `00b665a0`（命令位置の公開資料なし） · `00b665ac`（命令位置の公開資料なし）

~~~diff
- 00b66560 ["INT_ADD", "register:40f0:8", ["const:b66560:8", "const:4:8"]]
- 00b66560 ["CALL", null, ["callee:00bde180:8"]]
+ 00b665a4 ["INT_ADD", "register:40f0:8", ["const:b665a4:8", "const:4:8"]]
+ 00b665a4 ["CALL", null, ["callee:00bde180:8"]]
- 00b66560 bytes f4de0194
+ 00b665a4 bytes f7de0194
- 00b6655c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6655c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6655c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6655c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b665a0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b665a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b665a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b665a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6655c bytes 00fc1991
+ 00b665a0 bytes 00c81791
- 00b66568 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00b66568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b665ac ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00b665ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b665ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b665ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66568 bytes 08611e91
+ 00b665ac bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9afeec42099dcc388d9a2d04e35bf45"></a>

### [`00b6657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6657c.md) → [`00b665c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b665ec",
      "incomplete_value": true,
      "site": "00b665ec",
      "value": [
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
    "old": {
      "definition_site": "00b665a8",
      "incomplete_value": true,
      "site": "00b665a8",
      "value": [
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
      "definition_site": "00b665d4",
      "incomplete_value": true,
      "site": "00b665d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66590",
      "incomplete_value": true,
      "site": "00b66590",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b665e0",
      "incomplete_value": false,
      "site": "00b665e4",
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
    "old": {
      "definition_site": "00b6659c",
      "incomplete_value": false,
      "site": "00b665a0",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b665d0",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b665e0",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b665ec",
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
      "00b665d0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b665e0",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b665ec",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b665a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6657c.md#insn-00b665a0) · [`00b665a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6657c.md#insn-00b665a8) · [`00b6658c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6657c.md#insn-00b6658c)
- 新版 `00b665e4`（命令位置の公開資料なし） · `00b665ec`（命令位置の公開資料なし） · `00b665d0`（命令位置の公開資料なし）

~~~diff
- 00b665a0 ["INT_ADD", "register:40f0:8", ["const:b665a0:8", "const:4:8"]]
- 00b665a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b665e4 ["INT_ADD", "register:40f0:8", ["const:b665e4:8", "const:4:8"]]
+ 00b665e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b665a0 bytes a8de0194
+ 00b665e4 bytes abde0194
- 00b665a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b665a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b665ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b665ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b665a8 bytes 60d203f9
+ 00b665ec bytes 60f203f9
- 00b6658c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b6658c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b665d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b665d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6658c bytes 68d243f9
+ 00b665d0 bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5bce3f7c5ef68b4ea483c1de8ad524"></a>

### [`00b665bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665bc.md) → [`00b66600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b665e8",
      "incomplete_value": true,
      "site": "00b665e8",
      "value": [
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
    "old": {
      "definition_site": "00b665d0",
      "incomplete_value": true,
      "site": "00b665d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b665d8",
      "incomplete_value": false,
      "site": "00b665e0",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66610",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6661c",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b6662c",
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
      "00b66610",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6661c",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b6662c",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b665e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665bc.md#insn-00b665e0) · [`00b665e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665bc.md#insn-00b665e8) · [`00b665cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665bc.md#insn-00b665cc)
- 新版 `00b66624`（命令位置の公開資料なし） · `00b6662c`（命令位置の公開資料なし） · `00b66610`（命令位置の公開資料なし）

~~~diff
- 00b665e0 ["INT_ADD", "register:40f0:8", ["const:b665e0:8", "const:4:8"]]
- 00b665e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66624 ["INT_ADD", "register:40f0:8", ["const:b66624:8", "const:4:8"]]
+ 00b66624 ["CALL", null, ["callee:00bde090:8"]]
- 00b665e0 bytes 98de0194
+ 00b66624 bytes 9bde0194
- 00b665e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b665e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6662c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b6662c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b665e8 bytes 60d203f9
+ 00b6662c bytes 60f203f9
- 00b665cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b665cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66610 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b665cc bytes 68d243f9
+ 00b66610 bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1e6de51df7b848e3f9e1725b00200d9"></a>

### [`00b665fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665fc.md) → [`00b66640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66610",
      "incomplete_value": true,
      "site": "00b66610",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:fed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66650",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66660",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b66670",
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
      "00b66650",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66660",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b66670",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665fc.md#insn-00b66624) · [`00b6662c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665fc.md#insn-00b6662c) · [`00b6660c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665fc.md#insn-00b6660c)
- 新版 `00b66668`（命令位置の公開資料なし） · `00b66670`（命令位置の公開資料なし） · `00b66650`（命令位置の公開資料なし）

~~~diff
- 00b66624 ["INT_ADD", "register:40f0:8", ["const:b66624:8", "const:4:8"]]
- 00b66624 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66668 ["INT_ADD", "register:40f0:8", ["const:b66668:8", "const:4:8"]]
+ 00b66668 ["CALL", null, ["callee:00bde090:8"]]
- 00b66624 bytes 87de0194
+ 00b66668 bytes 8ade0194
- 00b6662c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b6662c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66670 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6662c bytes 60d203f9
+ 00b66670 bytes 60f203f9
- 00b6660c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b6660c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66650 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6660c bytes 68d243f9
+ 00b66650 bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c87f95f08b4fbc8140ab2b61ccd029fc"></a>

### [`00b66640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66640.md) → [`00b66684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00b666b4",
      "incomplete_value": true,
      "site": "00b666b4",
      "value": [
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b66654"
      ],
      [
        "FALL_THROUGH",
        "00b66698"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66698",
      "incomplete_value": true,
      "site": "00b666b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "site": "00b66670",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66694",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666a0",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b666b4",
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
      "00b66694",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666a0",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b666b4",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66640.md#insn-00b66670) · [`00b66650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66640.md#insn-00b66650) · [`00b66658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66640.md#insn-00b66658)
- 新版 `00b666b4`（命令位置の公開資料なし） · `00b66694`（命令位置の公開資料なし） · `00b6669c`（命令位置の公開資料なし）

~~~diff
- 00b66670 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b66670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b666b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b666b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66670 bytes 60d203f9
+ 00b666b4 bytes 60f203f9
- 00b66650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b66650 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66694 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66650 bytes 68d243f9
+ 00b66694 bytes 68f243f9
- 00b66658 ["COPY", "register:4018:8", ["const:2a2000:8"]]
+ 00b6669c ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b66658 bytes e3b9ff90
+ 00b6669c bytes e3b9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d341c7b6539fdad41e75496dc2350593"></a>

### [`00b66690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66690.md) → [`00b666d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md) _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b6672c",
      "incomplete_value": true,
      "site": "00b6672c",
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
    "old": {
      "definition_site": "00b666e8",
      "incomplete_value": true,
      "site": "00b666e8",
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
            "const:7a8:8"
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
      "definition_site": "00b66708",
      "incomplete_value": true,
      "site": "00b66714",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b666c4",
      "incomplete_value": true,
      "site": "00b666d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b666e8",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66708",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6672c",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b666e8",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66708",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6672c",
      "WRITE",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b666a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66690.md#insn-00b666a4) · [`00b666d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66690.md#insn-00b666d0) · [`00b666e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66690.md#insn-00b666e8)
- 新版 `00b666e8`（命令位置の公開資料なし） · `00b66714`（命令位置の公開資料なし） · `00b6672c`（命令位置の公開資料なし）

~~~diff
- 00b666a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a8:8"]]
- 00b666a4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b666a4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b666e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b666e8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b666e8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b666a4 bytes a8a25e39
+ 00b666e8 bytes a8a25f39
- 00b666d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b666d0 ["INT_ADD", "register:40f0:8", ["const:b666d0:8", "const:4:8"]]
- 00b666d0 ["CALLIND", null, ["register:0:8"]]
+ 00b66714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66714 ["INT_ADD", "register:40f0:8", ["const:b66714:8", "const:4:8"]]
+ 00b66714 ["CALLIND", null, ["register:0:8"]]
- 00b666d0 bytes 00013fd6
+ 00b66714 bytes 00013fd6
- 00b666e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b666e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a8:8"]]
- 00b666e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6672c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6672c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b6672c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b666e8 bytes a0a21e39
+ 00b6672c bytes a0a21f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9843f882dd451af5716b01567fbb11a"></a>

### [`00b666fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b666fc.md) → [`00b66740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md) _ZN8firebase4auth13playgamescred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b66738",
      "incomplete_value": true,
      "site": "00b66738",
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
            "const:7a8:8"
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
    "old": {
      "definition_site": "00b66758",
      "incomplete_value": true,
      "site": "00b66758",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00b66714",
      "incomplete_value": true,
      "site": "00b66714",
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
      "00b66754",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66760",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6677c",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66754",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66760",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6677c",
      "WRITE",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b666fc.md#insn-00b66710) · [`00b66738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b666fc.md#insn-00b66738) · [`00b66754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b666fc.md#insn-00b66754)
- 新版 `00b66754`（命令位置の公開資料なし） · `00b6677c`（命令位置の公開資料なし） · `00b66798`（命令位置の公開資料なし）

~~~diff
- 00b66710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b66710 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66754 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b66754 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66710 bytes 81d243f9
+ 00b66754 bytes 81f243f9
- 00b66738 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66738 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66738 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a8:8"]]
- 00b66738 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6677c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6677c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6677c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b6677c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66738 bytes bfa21e39
+ 00b6677c bytes bfa21f39
- 00b66754 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66754 ["INT_ADD", "register:40f0:8", ["const:b66754:8", "const:4:8"]]
- 00b66754 ["CALLIND", null, ["register:0:8"]]
+ 00b66798 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66798 ["INT_ADD", "register:40f0:8", ["const:b66798:8", "const:4:8"]]
+ 00b66798 ["CALLIND", null, ["register:0:8"]]
- 00b66754 bytes 00013fd6
+ 00b66798 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f977512aa178b0570413c330a251021"></a>

### [`00b6676c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6676c.md) → [`00b667b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md) _ZN8firebase4auth13playgamescred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
    "old": {
      "definition_site": "00b667ac",
      "incomplete_value": true,
      "site": "00b667ac",
      "value": [
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
    "old": {
      "definition_site": "00b66788",
      "incomplete_value": true,
      "site": "00b66788",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66790",
      "incomplete_value": false,
      "site": "00b667a4",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b667c4",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b667d4",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b667f0",
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
      "00b667c4",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b667d4",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b667f0",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b667a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6676c.md#insn-00b667a4) · [`00b667ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6676c.md#insn-00b667ac) · [`00b66780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6676c.md#insn-00b66780)
- 新版 `00b667e8`（命令位置の公開資料なし） · `00b667f0`（命令位置の公開資料なし） · `00b667c4`（命令位置の公開資料なし）

~~~diff
- 00b667a4 ["INT_ADD", "register:40f0:8", ["const:b667a4:8", "const:4:8"]]
- 00b667a4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b667e8 ["INT_ADD", "register:40f0:8", ["const:b667e8:8", "const:4:8"]]
+ 00b667e8 ["CALL", null, ["callee:00bde090:8"]]
- 00b667a4 bytes 27de0194
+ 00b667e8 bytes 2ade0194
- 00b667ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b667ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b667f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b667f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b667ac bytes 80d203f9
+ 00b667f0 bytes 80f203f9
- 00b66780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b66780 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b667c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b667c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66780 bytes 81d243f9
+ 00b667c4 bytes 81f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ddb23af91248c54a39e9b5427e709e"></a>

### [`00b667dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b667dc.md) → [`00b66820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66820.md) _ZN8firebase4auth13playgamescred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b6684c",
      "incomplete_value": true,
      "site": "00b66858",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66808",
      "incomplete_value": true,
      "site": "00b66814",
      "value": [
        "LOAD",
        "8",
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
      "00b6683c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6684c",
      "DATA",
      [
        "storage",
        "010a17b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6683c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6684c",
      "DATA",
      [
        "storage",
        "010a17f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b667f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b667dc.md#insn-00b667f8) · [`00b667fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b667dc.md#insn-00b667fc) · [`00b66804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b667dc.md#insn-00b66804)
- 新版 `00b6683c`（命令位置の公開資料なし） · `00b66840`（命令位置の公開資料なし） · `00b66848`（命令位置の公開資料なし）

~~~diff
- 00b667f8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b667f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b667f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b667f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6683c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6683c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6683c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6683c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b667f8 bytes 00501791
+ 00b6683c bytes 001c1591
- 00b667fc ["INT_ADD", "register:40f0:8", ["const:b667fc:8", "const:4:8"]]
- 00b667fc ["CALL", null, ["callee:00bde180:8"]]
+ 00b66840 ["INT_ADD", "register:40f0:8", ["const:b66840:8", "const:4:8"]]
+ 00b66840 ["CALL", null, ["callee:00bde180:8"]]
- 00b667fc bytes 4dde0194
+ 00b66840 bytes 50de0194
- 00b66804 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00b66804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66848 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b66848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66804 bytes 08c11e91
+ 00b66848 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f5de69805e3f8d0c252ff3ca56444b9"></a>

### [`00b66818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66818.md) → [`00b6685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md) _ZN8firebase4auth13playgamescred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66858",
      "incomplete_value": true,
      "site": "00b66858",
      "value": [
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
    "old": {
      "definition_site": "00b66834",
      "incomplete_value": true,
      "site": "00b66834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6683c",
      "incomplete_value": false,
      "site": "00b66850",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66870",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66880",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b6689c",
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
      "00b66870",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66880",
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      "00b6689c",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66818.md#insn-00b66850) · [`00b66858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66818.md#insn-00b66858) · [`00b6682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66818.md#insn-00b6682c)
- 新版 `00b66894`（命令位置の公開資料なし） · `00b6689c`（命令位置の公開資料なし） · `00b66870`（命令位置の公開資料なし）

~~~diff
- 00b66850 ["INT_ADD", "register:40f0:8", ["const:b66850:8", "const:4:8"]]
- 00b66850 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66894 ["INT_ADD", "register:40f0:8", ["const:b66894:8", "const:4:8"]]
+ 00b66894 ["CALL", null, ["callee:00bde090:8"]]
- 00b66850 bytes fcdd0194
+ 00b66894 bytes ffdd0194
- 00b66858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b66858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6689c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b6689c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66858 bytes 80d203f9
+ 00b6689c bytes 80f203f9
- 00b6682c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b6682c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66870 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b66870 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6682c bytes 81d243f9
+ 00b66870 bytes 81f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb227edcaf1277f58a8699fee0b05def"></a>

### [`00b66888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md) → [`00b668cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b668a4",
      "incomplete_value": false,
      "site": "00b668a8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b668b4",
      "incomplete_value": true,
      "site": "00b668c0",
      "value": [
        "LOAD",
        "8",
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
      "00b668e8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b668f8",
      "DATA",
      [
        "storage",
        "010a17b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b668e8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b668f8",
      "DATA",
      [
        "storage",
        "010a17f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b668a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md#insn-00b668a8) · [`00b668a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md#insn-00b668a4) · [`00b668b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md#insn-00b668b0)
- 新版 `00b668ec`（命令位置の公開資料なし） · `00b668e8`（命令位置の公開資料なし） · `00b668f4`（命令位置の公開資料なし）

~~~diff
- 00b668a8 ["INT_ADD", "register:40f0:8", ["const:b668a8:8", "const:4:8"]]
- 00b668a8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b668ec ["INT_ADD", "register:40f0:8", ["const:b668ec:8", "const:4:8"]]
+ 00b668ec ["CALL", null, ["callee:00bde180:8"]]
- 00b668a8 bytes 22de0194
+ 00b668ec bytes 25de0194
- 00b668a4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b668a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b668a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b668a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b668e8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b668e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b668e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b668e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b668a4 bytes 00fc1991
+ 00b668e8 bytes 00c81791
- 00b668b0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00b668b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b668b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b668b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b668f4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00b668f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b668f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b668f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b668b0 bytes 08e11e91
+ 00b668f4 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-461bdbdd8c7acc42ac01998fa5719098"></a>

### [`00b668c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b668c4.md) → [`00b66908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b668f0",
      "incomplete_value": true,
      "site": "00b668f0",
      "value": [
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
    "old": {
      "definition_site": "00b668d8",
      "incomplete_value": true,
      "site": "00b668d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b668e4",
      "incomplete_value": false,
      "site": "00b668e8",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66918",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66928",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66934",
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
      "00b66918",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66928",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66934",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b668e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b668c4.md#insn-00b668e8) · [`00b668f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b668c4.md#insn-00b668f0) · [`00b668d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b668c4.md#insn-00b668d4)
- 新版 `00b6692c`（命令位置の公開資料なし） · `00b66934`（命令位置の公開資料なし） · `00b66918`（命令位置の公開資料なし）

~~~diff
- 00b668e8 ["INT_ADD", "register:40f0:8", ["const:b668e8:8", "const:4:8"]]
- 00b668e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6692c ["INT_ADD", "register:40f0:8", ["const:b6692c:8", "const:4:8"]]
+ 00b6692c ["CALL", null, ["callee:00bde090:8"]]
- 00b668e8 bytes d6dd0194
+ 00b6692c bytes d9dd0194
- 00b668f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b668f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66934 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b66934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b668f0 bytes 60e203f9
+ 00b66934 bytes 600204f9
- 00b668d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b668d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66918 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b66918 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b668d4 bytes 68e243f9
+ 00b66918 bytes 680244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733edda63ead420380777780ec6852ae"></a>

### [`00b66904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66904.md) → [`00b66948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66930",
      "incomplete_value": true,
      "site": "00b66930",
      "value": [
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
    "old": {
      "definition_site": "00b66918",
      "incomplete_value": true,
      "site": "00b66918",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66920",
      "incomplete_value": false,
      "site": "00b66928",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66958",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66964",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66974",
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
      "00b66958",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66964",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66974",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66904.md#insn-00b66928) · [`00b66930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66904.md#insn-00b66930) · [`00b66914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66904.md#insn-00b66914)
- 新版 `00b6696c`（命令位置の公開資料なし） · `00b66974`（命令位置の公開資料なし） · `00b66958`（命令位置の公開資料なし）

~~~diff
- 00b66928 ["INT_ADD", "register:40f0:8", ["const:b66928:8", "const:4:8"]]
- 00b66928 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6696c ["INT_ADD", "register:40f0:8", ["const:b6696c:8", "const:4:8"]]
+ 00b6696c ["CALL", null, ["callee:00bde090:8"]]
- 00b66928 bytes c6dd0194
+ 00b6696c bytes c9dd0194
- 00b66930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b66974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66930 bytes 60e203f9
+ 00b66974 bytes 600204f9
- 00b66914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b66958 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66914 bytes 68e243f9
+ 00b66958 bytes 680244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-372951918757e9af34d3c58d38bf2396"></a>

### [`00b66944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66944.md) → [`00b66988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66958",
      "incomplete_value": true,
      "site": "00b66958",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66998",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669a8",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b669b8",
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
      "00b66998",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669a8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b669b8",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6696c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66944.md#insn-00b6696c) · [`00b66974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66944.md#insn-00b66974) · [`00b66954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66944.md#insn-00b66954)
- 新版 `00b669b0`（命令位置の公開資料なし） · `00b669b8`（命令位置の公開資料なし） · `00b66998`（命令位置の公開資料なし）

~~~diff
- 00b6696c ["INT_ADD", "register:40f0:8", ["const:b6696c:8", "const:4:8"]]
- 00b6696c ["CALL", null, ["callee:00bde090:8"]]
+ 00b669b0 ["INT_ADD", "register:40f0:8", ["const:b669b0:8", "const:4:8"]]
+ 00b669b0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6696c bytes b5dd0194
+ 00b669b0 bytes b8dd0194
- 00b66974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b669b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b669b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66974 bytes 60e203f9
+ 00b669b8 bytes 600204f9
- 00b66954 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66954 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b66998 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66954 bytes 68e243f9
+ 00b66998 bytes 680244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0d45a496d50b276f48119107700cac"></a>

### [`00b66988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66988.md) → [`00b669cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b669a4",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b669dc",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669e8",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b669fc",
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
      "00b669dc",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669e8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b669fc",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66988.md#insn-00b669b0) · [`00b669b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66988.md#insn-00b669b8) · [`00b66998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66988.md#insn-00b66998)
- 新版 `00b669f4`（命令位置の公開資料なし） · `00b669fc`（命令位置の公開資料なし） · `00b669dc`（命令位置の公開資料なし）

~~~diff
- 00b669b0 ["INT_ADD", "register:40f0:8", ["const:b669b0:8", "const:4:8"]]
- 00b669b0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b669f4 ["INT_ADD", "register:40f0:8", ["const:b669f4:8", "const:4:8"]]
+ 00b669f4 ["CALL", null, ["callee:00bde090:8"]]
- 00b669b0 bytes a4dd0194
+ 00b669f4 bytes a7dd0194
- 00b669b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b669b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b669fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b669fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b669b8 bytes 60e203f9
+ 00b669fc bytes 600204f9
- 00b66998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66998 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b669dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00b669dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66998 bytes 68e243f9
+ 00b669dc bytes 680244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b55fd9058b965d68826ad93be51f33"></a>

### [`00b669d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b669d8.md) → [`00b66a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md) _ZN8firebase4auth11twittercred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b66a30",
      "incomplete_value": true,
      "site": "00b66a30",
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
    "old": {
      "definition_site": "00b66a0c",
      "incomplete_value": true,
      "site": "00b66a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b66a30",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a50",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a74",
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
      "00b66a30",
      "READ",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a50",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a74",
      "WRITE",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b669d8.md#insn-00b669ec) · [`00b66a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b669d8.md#insn-00b66a18) · [`00b66a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b669d8.md#insn-00b66a30)
- 新版 `00b66a30`（命令位置の公開資料なし） · `00b66a5c`（命令位置の公開資料なし） · `00b66a74`（命令位置の公開資料なし）

~~~diff
- 00b669ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c8:8"]]
- 00b669ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b669ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b66a30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00b66a30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b66a30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b669ec bytes a8225f39
+ 00b66a30 bytes a8226039
- 00b66a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66a18 ["INT_ADD", "register:40f0:8", ["const:b66a18:8", "const:4:8"]]
- 00b66a18 ["CALLIND", null, ["register:0:8"]]
+ 00b66a5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66a5c ["INT_ADD", "register:40f0:8", ["const:b66a5c:8", "const:4:8"]]
+ 00b66a5c ["CALLIND", null, ["register:0:8"]]
- 00b66a18 bytes 00013fd6
+ 00b66a5c bytes 00013fd6
- 00b66a30 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66a30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c8:8"]]
- 00b66a30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66a74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66a74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:808:8"]]
+ 00b66a74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66a30 bytes a0221f39
+ 00b66a74 bytes a0222039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df53fcaf0dcacef64ec5ef77c0447667"></a>

### [`00b66a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66a44.md) → [`00b66a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md) _ZN8firebase4auth11twittercred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b66a80",
      "incomplete_value": true,
      "site": "00b66a80",
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
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00b66aa0",
      "incomplete_value": true,
      "site": "00b66aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
    "old": {
      "definition_site": "00b66a5c",
      "incomplete_value": true,
      "site": "00b66a5c",
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
      "00b66a9c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66aa8",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66ac4",
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
      "00b66a9c",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66aa8",
      "READ",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66ac4",
      "WRITE",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66a44.md#insn-00b66a58) · [`00b66a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66a44.md#insn-00b66a80) · [`00b66a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66a44.md#insn-00b66a9c)
- 新版 `00b66a9c`（命令位置の公開資料なし） · `00b66ac4`（命令位置の公開資料なし） · `00b66ae0`（命令位置の公開資料なし）

~~~diff
- 00b66a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66a58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66a9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00b66a9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66a58 bytes 81e243f9
+ 00b66a9c bytes 810244f9
- 00b66a80 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66a80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66a80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c8:8"]]
- 00b66a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66ac4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66ac4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66ac4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:808:8"]]
+ 00b66ac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66a80 bytes bf221f39
+ 00b66ac4 bytes bf222039
- 00b66a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66a9c ["INT_ADD", "register:40f0:8", ["const:b66a9c:8", "const:4:8"]]
- 00b66a9c ["CALLIND", null, ["register:0:8"]]
+ 00b66ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66ae0 ["INT_ADD", "register:40f0:8", ["const:b66ae0:8", "const:4:8"]]
+ 00b66ae0 ["CALLIND", null, ["register:0:8"]]
- 00b66a9c bytes 00013fd6
+ 00b66ae0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a407236bc37b7cb73b90dc1dc2bc4e57"></a>

### [`00b66ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ab4.md) → [`00b66af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md) _ZN8firebase4auth11twittercred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b66b38",
      "incomplete_value": true,
      "site": "00b66b38",
      "value": [
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
      "definition_site": "00b66af4",
      "incomplete_value": true,
      "site": "00b66af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "00b66b14",
      "incomplete_value": true,
      "site": "00b66b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ad0",
      "incomplete_value": true,
      "site": "00b66ad0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66b1c",
      "incomplete_value": false,
      "site": "00b66b30",
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
    "old": {
      "definition_site": "00b66ad8",
      "incomplete_value": false,
      "site": "00b66aec",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66b0c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b1c",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66b38",
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
      "00b66b0c",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b1c",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66b38",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ab4.md#insn-00b66aec) · [`00b66af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ab4.md#insn-00b66af4) · [`00b66ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ab4.md#insn-00b66ac8)
- 新版 `00b66b30`（命令位置の公開資料なし） · `00b66b38`（命令位置の公開資料なし） · `00b66b0c`（命令位置の公開資料なし）

~~~diff
- 00b66aec ["INT_ADD", "register:40f0:8", ["const:b66aec:8", "const:4:8"]]
- 00b66aec ["CALL", null, ["callee:00bde090:8"]]
+ 00b66b30 ["INT_ADD", "register:40f0:8", ["const:b66b30:8", "const:4:8"]]
+ 00b66b30 ["CALL", null, ["callee:00bde090:8"]]
- 00b66aec bytes 55dd0194
+ 00b66b30 bytes 58dd0194
- 00b66af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00b66b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66af4 bytes 80e203f9
+ 00b66b38 bytes 800204f9
- 00b66ac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66ac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00b66b0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66ac8 bytes 81e243f9
+ 00b66b0c bytes 810244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ad63f91985920d9d855fa9fb09e556"></a>

### [`00b66b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b24.md) → [`00b66b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b66b40",
      "incomplete_value": false,
      "site": "00b66b44",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66b50",
      "incomplete_value": true,
      "site": "00b66b5c",
      "value": [
        "LOAD",
        "8",
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
      "00b66b84",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66b94",
      "DATA",
      [
        "storage",
        "010a17d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66b84",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66b94",
      "DATA",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b24.md#insn-00b66b44) · [`00b66b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b24.md#insn-00b66b40) · [`00b66b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b24.md#insn-00b66b4c)
- 新版 `00b66b88`（命令位置の公開資料なし） · `00b66b84`（命令位置の公開資料なし） · `00b66b90`（命令位置の公開資料なし）

~~~diff
- 00b66b44 ["INT_ADD", "register:40f0:8", ["const:b66b44:8", "const:4:8"]]
- 00b66b44 ["CALL", null, ["callee:00bde180:8"]]
+ 00b66b88 ["INT_ADD", "register:40f0:8", ["const:b66b88:8", "const:4:8"]]
+ 00b66b88 ["CALL", null, ["callee:00bde180:8"]]
- 00b66b44 bytes 7bdd0194
+ 00b66b88 bytes 7edd0194
- 00b66b40 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b66b40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66b84 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b66b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66b40 bytes 00501791
+ 00b66b84 bytes 001c1591
- 00b66b4c ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00b66b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66b90 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00b66b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66b4c bytes 08411f91
+ 00b66b90 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745105b7518c9ce081ab44301f180002"></a>

### [`00b66b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b60.md) → [`00b66ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md) _ZN8firebase4auth11twittercred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66ba0",
      "incomplete_value": true,
      "site": "00b66ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
    "old": {
      "definition_site": "00b66b7c",
      "incomplete_value": true,
      "site": "00b66b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66b84",
      "incomplete_value": false,
      "site": "00b66b98",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66bb8",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66bc8",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66be4",
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
      "00b66bb8",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66bc8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66be4",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b60.md#insn-00b66b98) · [`00b66ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b60.md#insn-00b66ba0) · [`00b66b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b60.md#insn-00b66b74)
- 新版 `00b66bdc`（命令位置の公開資料なし） · `00b66be4`（命令位置の公開資料なし） · `00b66bb8`（命令位置の公開資料なし）

~~~diff
- 00b66b98 ["INT_ADD", "register:40f0:8", ["const:b66b98:8", "const:4:8"]]
- 00b66b98 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66bdc ["INT_ADD", "register:40f0:8", ["const:b66bdc:8", "const:4:8"]]
+ 00b66bdc ["CALL", null, ["callee:00bde090:8"]]
- 00b66b98 bytes 2add0194
+ 00b66bdc bytes 2ddd0194
- 00b66ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00b66be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66ba0 bytes 80e203f9
+ 00b66be4 bytes 800204f9
- 00b66b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66bb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00b66bb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66b74 bytes 81e243f9
+ 00b66bb8 bytes 810244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bae8921bf69c4d73893bfd1632554e09"></a>

### [`00b66bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66bd0.md) → [`00b66c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00b66bec",
      "incomplete_value": false,
      "site": "00b66bf0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66bfc",
      "incomplete_value": true,
      "site": "00b66c08",
      "value": [
        "LOAD",
        "8",
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
      "00b66c30",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b66c40",
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
      "00b66c30",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b66c40",
      "DATA",
      [
        "storage",
        "010a1818",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66bd0.md#insn-00b66bf0) · [`00b66bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66bd0.md#insn-00b66bec) · [`00b66bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66bd0.md#insn-00b66bf8)
- 新版 `00b66c34`（命令位置の公開資料なし） · `00b66c30`（命令位置の公開資料なし） · `00b66c3c`（命令位置の公開資料なし）

~~~diff
- 00b66bf0 ["INT_ADD", "register:40f0:8", ["const:b66bf0:8", "const:4:8"]]
- 00b66bf0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b66c34 ["INT_ADD", "register:40f0:8", ["const:b66c34:8", "const:4:8"]]
+ 00b66c34 ["CALL", null, ["callee:00bde180:8"]]
- 00b66bf0 bytes 50dd0194
+ 00b66c34 bytes 53dd0194
- 00b66bec ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b66bec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66bec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66bec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66c30 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b66c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66bec bytes 00fc1991
+ 00b66c30 bytes 00c81791
- 00b66bf8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00b66bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66c3c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00b66c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66bf8 bytes 08611f91
+ 00b66c3c bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf6cec4efb367fc2ec30df8ba250e82"></a>

### [`00b66c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c0c.md) → [`00b66c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66c38",
      "incomplete_value": true,
      "site": "00b66c38",
      "value": [
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
    "old": {
      "definition_site": "00b66c20",
      "incomplete_value": true,
      "site": "00b66c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66c2c",
      "incomplete_value": false,
      "site": "00b66c30",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66c60",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c70",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66c7c",
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
      "00b66c60",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c70",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66c7c",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c0c.md#insn-00b66c30) · [`00b66c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c0c.md#insn-00b66c38) · [`00b66c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c0c.md#insn-00b66c1c)
- 新版 `00b66c74`（命令位置の公開資料なし） · `00b66c7c`（命令位置の公開資料なし） · `00b66c60`（命令位置の公開資料なし）

~~~diff
- 00b66c30 ["INT_ADD", "register:40f0:8", ["const:b66c30:8", "const:4:8"]]
- 00b66c30 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66c74 ["INT_ADD", "register:40f0:8", ["const:b66c74:8", "const:4:8"]]
+ 00b66c74 ["CALL", null, ["callee:00bde090:8"]]
- 00b66c30 bytes 04dd0194
+ 00b66c74 bytes 07dd0194
- 00b66c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66c7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66c7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66c38 bytes 60f203f9
+ 00b66c7c bytes 601204f9
- 00b66c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66c1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66c60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66c60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66c1c bytes 68f243f9
+ 00b66c60 bytes 681244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c8b37164e5dc2e25895c89cd55d8e9"></a>

### [`00b66c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c4c.md) → [`00b66c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66c78",
      "incomplete_value": true,
      "site": "00b66c78",
      "value": [
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
    "old": {
      "definition_site": "00b66c60",
      "incomplete_value": true,
      "site": "00b66c60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66c68",
      "incomplete_value": false,
      "site": "00b66c70",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66ca0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cac",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66cbc",
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
      "00b66ca0",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cac",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66cbc",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c4c.md#insn-00b66c70) · [`00b66c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c4c.md#insn-00b66c78) · [`00b66c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c4c.md#insn-00b66c5c)
- 新版 `00b66cb4`（命令位置の公開資料なし） · `00b66cbc`（命令位置の公開資料なし） · `00b66ca0`（命令位置の公開資料なし）

~~~diff
- 00b66c70 ["INT_ADD", "register:40f0:8", ["const:b66c70:8", "const:4:8"]]
- 00b66c70 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
+ 00b66cb4 ["CALL", null, ["callee:00bde090:8"]]
- 00b66c70 bytes f4dc0194
+ 00b66cb4 bytes f7dc0194
- 00b66c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66c78 bytes 60f203f9
+ 00b66cbc bytes 601204f9
- 00b66c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66c5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66ca0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66c5c bytes 68f243f9
+ 00b66ca0 bytes 681244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b3f142948532871f85d1ce03e301e2"></a>

### [`00b66c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c8c.md) → [`00b66cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66ca0",
      "incomplete_value": true,
      "site": "00b66ca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:fd7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66ce0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cf0",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66d00",
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
      "00b66ce0",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cf0",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66d00",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c8c.md#insn-00b66cb4) · [`00b66cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c8c.md#insn-00b66cbc) · [`00b66c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c8c.md#insn-00b66c9c)
- 新版 `00b66cf8`（命令位置の公開資料なし） · `00b66d00`（命令位置の公開資料なし） · `00b66ce0`（命令位置の公開資料なし）

~~~diff
- 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
- 00b66cb4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66cf8 ["INT_ADD", "register:40f0:8", ["const:b66cf8:8", "const:4:8"]]
+ 00b66cf8 ["CALL", null, ["callee:00bde090:8"]]
- 00b66cb4 bytes e3dc0194
+ 00b66cf8 bytes e6dc0194
- 00b66cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66cbc bytes 60f203f9
+ 00b66d00 bytes 601204f9
- 00b66c9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66c9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66c9c bytes 68f243f9
+ 00b66ce0 bytes 681244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a43afad5eb27466f532371c0e628a78"></a>

### [`00b66cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66cd0.md) → [`00b66d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
    "old": {
      "definition_site": "00b66cec",
      "incomplete_value": false,
      "site": "00b66cf8",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66d24",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d30",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66d44",
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
      "00b66d24",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d30",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66d44",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66cd0.md#insn-00b66cf8) · [`00b66d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66cd0.md#insn-00b66d00) · [`00b66ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66cd0.md#insn-00b66ce0)
- 新版 `00b66d3c`（命令位置の公開資料なし） · `00b66d44`（命令位置の公開資料なし） · `00b66d24`（命令位置の公開資料なし）

~~~diff
- 00b66cf8 ["INT_ADD", "register:40f0:8", ["const:b66cf8:8", "const:4:8"]]
- 00b66cf8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66d3c ["INT_ADD", "register:40f0:8", ["const:b66d3c:8", "const:4:8"]]
+ 00b66d3c ["CALL", null, ["callee:00bde090:8"]]
- 00b66cf8 bytes d2dc0194
+ 00b66d3c bytes d5dc0194
- 00b66d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66d00 bytes 60f203f9
+ 00b66d44 bytes 601204f9
- 00b66ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b66ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00b66d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66ce0 bytes 68f243f9
+ 00b66d24 bytes 681244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602bd1e343d66489c684e69e058800d4"></a>

### [`00b66d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d20.md) → [`00b66d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
    "old": {
      "definition_site": "00b66d78",
      "incomplete_value": true,
      "site": "00b66d78",
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
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b66d54",
      "incomplete_value": true,
      "site": "00b66d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b66d78",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66d98",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66dbc",
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
      "00b66d78",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66d98",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66dbc",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d20.md#insn-00b66d34) · [`00b66d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d20.md#insn-00b66d60) · [`00b66d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d20.md#insn-00b66d78)
- 新版 `00b66d78`（命令位置の公開資料なし） · `00b66da4`（命令位置の公開資料なし） · `00b66dbc`（命令位置の公開資料なし）

~~~diff
- 00b66d34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e8:8"]]
- 00b66d34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66d34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b66d78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:828:8"]]
+ 00b66d78 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b66d78 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66d34 bytes a8a25f39
+ 00b66d78 bytes a8a26039
- 00b66d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66d60 ["INT_ADD", "register:40f0:8", ["const:b66d60:8", "const:4:8"]]
- 00b66d60 ["CALLIND", null, ["register:0:8"]]
+ 00b66da4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66da4 ["INT_ADD", "register:40f0:8", ["const:b66da4:8", "const:4:8"]]
+ 00b66da4 ["CALLIND", null, ["register:0:8"]]
- 00b66d60 bytes 00013fd6
+ 00b66da4 bytes 00013fd6
- 00b66d78 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66d78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e8:8"]]
- 00b66d78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66dbc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66dbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:828:8"]]
+ 00b66dbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66d78 bytes a0a21f39
+ 00b66dbc bytes a0a22039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a8d42a75370cbd2742219489ddacc3e"></a>

### [`00b66d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d8c.md) → [`00b66dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b66e0c",
      "incomplete_value": true,
      "site": "00b66e0c",
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
    "old": {
      "definition_site": "00b66dc8",
      "incomplete_value": true,
      "site": "00b66dc8",
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
      "definition_site": "00b66e2c",
      "incomplete_value": true,
      "site": "00b66e2c",
      "value": [
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
    "old": {
      "definition_site": "00b66de8",
      "incomplete_value": true,
      "site": "00b66de8",
      "value": [
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
      "definition_site": "00b66de8",
      "incomplete_value": true,
      "site": "00b66de8",
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
      "definition_site": "00b66da4",
      "incomplete_value": true,
      "site": "00b66da4",
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
      "00b66de4",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66df0",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66e0c",
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
      "00b66de4",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66df0",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66e0c",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d8c.md#insn-00b66da0) · [`00b66dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d8c.md#insn-00b66dc8) · [`00b66de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d8c.md#insn-00b66de4)
- 新版 `00b66de4`（命令位置の公開資料なし） · `00b66e0c`（命令位置の公開資料なし） · `00b66e28`（命令位置の公開資料なし）

~~~diff
- 00b66da0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b66da0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66de4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00b66de4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66da0 bytes 81f243f9
+ 00b66de4 bytes 811244f9
- 00b66dc8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66dc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66dc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
- 00b66dc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66e0c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66e0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66e0c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:828:8"]]
+ 00b66e0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66dc8 bytes bfa21f39
+ 00b66e0c bytes bfa22039
- 00b66de4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66de4 ["INT_ADD", "register:40f0:8", ["const:b66de4:8", "const:4:8"]]
- 00b66de4 ["CALLIND", null, ["register:0:8"]]
+ 00b66e28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66e28 ["INT_ADD", "register:40f0:8", ["const:b66e28:8", "const:4:8"]]
+ 00b66e28 ["CALLIND", null, ["register:0:8"]]
- 00b66de4 bytes 00013fd6
+ 00b66e28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f2226a7acb82f47bcb3ddd922f71c0"></a>

### [`00b66dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66dfc.md) → [`00b66e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b66e80",
      "incomplete_value": true,
      "site": "00b66e80",
      "value": [
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
    "old": {
      "definition_site": "00b66e3c",
      "incomplete_value": true,
      "site": "00b66e3c",
      "value": [
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
      "definition_site": "00b66e5c",
      "incomplete_value": true,
      "site": "00b66e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66e18",
      "incomplete_value": true,
      "site": "00b66e18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66e64",
      "incomplete_value": false,
      "site": "00b66e78",
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
    "old": {
      "definition_site": "00b66e20",
      "incomplete_value": false,
      "site": "00b66e34",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66e54",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e64",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66e80",
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
      "00b66e54",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e64",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66e80",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66dfc.md#insn-00b66e34) · [`00b66e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66dfc.md#insn-00b66e3c) · [`00b66e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66dfc.md#insn-00b66e10)
- 新版 `00b66e78`（命令位置の公開資料なし） · `00b66e80`（命令位置の公開資料なし） · `00b66e54`（命令位置の公開資料なし）

~~~diff
- 00b66e34 ["INT_ADD", "register:40f0:8", ["const:b66e34:8", "const:4:8"]]
- 00b66e34 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66e78 ["INT_ADD", "register:40f0:8", ["const:b66e78:8", "const:4:8"]]
+ 00b66e78 ["CALL", null, ["callee:00bde090:8"]]
- 00b66e34 bytes 83dc0194
+ 00b66e78 bytes 86dc0194
- 00b66e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b66e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00b66e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66e3c bytes 80f203f9
+ 00b66e80 bytes 801204f9
- 00b66e10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b66e10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66e54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00b66e54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66e10 bytes 81f243f9
+ 00b66e54 bytes 811244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6eefe848b286e29c5bff8d8368f3047"></a>

### [`00b66e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66e6c.md) → [`00b66eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eb0.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b66ecc",
      "incomplete_value": false,
      "site": "00b66ed0",
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
    "old": {
      "definition_site": "00b66e88",
      "incomplete_value": false,
      "site": "00b66e8c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66edc",
      "incomplete_value": true,
      "site": "00b66ee8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66e98",
      "incomplete_value": true,
      "site": "00b66ea4",
      "value": [
        "LOAD",
        "8",
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
      "00b66ecc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66edc",
      "DATA",
      [
        "storage",
        "010a17f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66ecc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66edc",
      "DATA",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66e6c.md#insn-00b66e8c) · [`00b66e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66e6c.md#insn-00b66e88) · [`00b66e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66e6c.md#insn-00b66e94)
- 新版 `00b66ed0`（命令位置の公開資料なし） · `00b66ecc`（命令位置の公開資料なし） · `00b66ed8`（命令位置の公開資料なし）

~~~diff
- 00b66e8c ["INT_ADD", "register:40f0:8", ["const:b66e8c:8", "const:4:8"]]
- 00b66e8c ["CALL", null, ["callee:00bde180:8"]]
+ 00b66ed0 ["INT_ADD", "register:40f0:8", ["const:b66ed0:8", "const:4:8"]]
+ 00b66ed0 ["CALL", null, ["callee:00bde180:8"]]
- 00b66e8c bytes a9dc0194
+ 00b66ed0 bytes acdc0194
- 00b66e88 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b66e88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66e88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66e88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66ecc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b66ecc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66ecc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66ecc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66e88 bytes 00501791
+ 00b66ecc bytes 001c1591
- 00b66e94 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00b66e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66ed8 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00b66ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66e94 bytes 08c11f91
+ 00b66ed8 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d322784bac85cb8565cd435ee723046"></a>

### [`00b66ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ea8.md) → [`00b66eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66f2c",
      "incomplete_value": true,
      "site": "00b66f2c",
      "value": [
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
    "old": {
      "definition_site": "00b66ee8",
      "incomplete_value": true,
      "site": "00b66ee8",
      "value": [
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
      "definition_site": "00b66f08",
      "incomplete_value": true,
      "site": "00b66f08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ec4",
      "incomplete_value": true,
      "site": "00b66ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66ec4"
      ],
      [
        "FALL_THROUGH",
        "00b66f08"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66f08",
      "incomplete_value": true,
      "site": "00b66f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ec4",
      "incomplete_value": true,
      "site": "00b66ee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66f00",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f10",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66f2c",
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
      "00b66f00",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f10",
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      "00b66f2c",
      "WRITE",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ea8.md#insn-00b66ee8) · [`00b66ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ea8.md#insn-00b66ebc) · [`00b66ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ea8.md#insn-00b66ec8)
- 新版 `00b66f2c`（命令位置の公開資料なし） · `00b66f00`（命令位置の公開資料なし） · `00b66f0c`（命令位置の公開資料なし）

~~~diff
- 00b66ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b66ee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00b66f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66ee8 bytes 80f203f9
+ 00b66f2c bytes 801204f9
- 00b66ebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b66ebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66f00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00b66f00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66ebc bytes 81f243f9
+ 00b66f00 bytes 811244f9
- 00b66ec8 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b66f0c ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66ec8 bytes 03baffd0
+ 00b66f0c bytes 03bafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9234f42fb2c91c5eefc89afead761c95"></a>

### [`00b66f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f18.md) → [`00b66f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66f5c.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66f78",
      "incomplete_value": false,
      "site": "00b66f7c",
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
    "old": {
      "definition_site": "00b66f34",
      "incomplete_value": false,
      "site": "00b66f38",
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
      "00b66f78",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b66f88",
      "DATA",
      [
        "storage",
        "010a1808",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66f78",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b66f88",
      "DATA",
      [
        "storage",
        "010a1848",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f18.md#insn-00b66f38) · [`00b66f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f18.md#insn-00b66f34) · [`00b66f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f18.md#insn-00b66f40)
- 新版 `00b66f7c`（命令位置の公開資料なし） · `00b66f78`（命令位置の公開資料なし） · `00b66f84`（命令位置の公開資料なし）

~~~diff
- 00b66f38 ["INT_ADD", "register:40f0:8", ["const:b66f38:8", "const:4:8"]]
- 00b66f38 ["CALL", null, ["callee:00bde180:8"]]
+ 00b66f7c ["INT_ADD", "register:40f0:8", ["const:b66f7c:8", "const:4:8"]]
+ 00b66f7c ["CALL", null, ["callee:00bde180:8"]]
- 00b66f38 bytes 7edc0194
+ 00b66f7c bytes 81dc0194
- 00b66f34 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b66f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66f78 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b66f78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66f78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66f78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66f34 bytes 00fc1991
+ 00b66f78 bytes 00c81791
- 00b66f40 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00b66f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66f84 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00b66f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66f40 bytes 08212091
+ 00b66f84 bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c29afc3f15883b3075a69ff66372245"></a>

### [`00b66f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f54.md) → [`00b66f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66f98.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b66fc4",
      "incomplete_value": true,
      "site": "00b66fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66f80",
      "incomplete_value": true,
      "site": "00b66f80",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66fac",
      "incomplete_value": true,
      "site": "00b66fac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66f68",
      "incomplete_value": true,
      "site": "00b66f68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66fb8",
      "incomplete_value": false,
      "site": "00b66fbc",
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
            "const:ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66f74",
      "incomplete_value": false,
      "site": "00b66f78",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66fa8",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66fb8",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b66fc4",
      "WRITE",
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
      "00b66fa8",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66fb8",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b66fc4",
      "WRITE",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f54.md#insn-00b66f78) · [`00b66f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f54.md#insn-00b66f80) · [`00b66f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f54.md#insn-00b66f64)
- 新版 `00b66fbc`（命令位置の公開資料なし） · `00b66fc4`（命令位置の公開資料なし） · `00b66fa8`（命令位置の公開資料なし）

~~~diff
- 00b66f78 ["INT_ADD", "register:40f0:8", ["const:b66f78:8", "const:4:8"]]
- 00b66f78 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66fbc ["INT_ADD", "register:40f0:8", ["const:b66fbc:8", "const:4:8"]]
+ 00b66fbc ["CALL", null, ["callee:00bde090:8"]]
- 00b66f78 bytes 32dc0194
+ 00b66fbc bytes 35dc0194
- 00b66f80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b66f80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66fc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b66fc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66f80 bytes 600a04f9
+ 00b66fc4 bytes 602a04f9
- 00b66f64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b66f64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66fa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b66fa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66f64 bytes 680a44f9
+ 00b66fa8 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b2442f81b793cfe2cb0119a5d8f045"></a>

### [`00b66f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f94.md) → [`00b66fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66fd8.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b67004",
      "incomplete_value": true,
      "site": "00b67004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fc0",
      "incomplete_value": true,
      "site": "00b66fc0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66fec",
      "incomplete_value": true,
      "site": "00b66fec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fa8",
      "incomplete_value": true,
      "site": "00b66fa8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66ff4",
      "incomplete_value": false,
      "site": "00b66ffc",
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
            "const:ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fb0",
      "incomplete_value": false,
      "site": "00b66fb8",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66fe8",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ff4",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b67004",
      "WRITE",
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
      "00b66fe8",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ff4",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b67004",
      "WRITE",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f94.md#insn-00b66fb8) · [`00b66fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f94.md#insn-00b66fc0) · [`00b66fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f94.md#insn-00b66fa4)
- 新版 `00b66ffc`（命令位置の公開資料なし） · `00b67004`（命令位置の公開資料なし） · `00b66fe8`（命令位置の公開資料なし）

~~~diff
- 00b66fb8 ["INT_ADD", "register:40f0:8", ["const:b66fb8:8", "const:4:8"]]
- 00b66fb8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b66ffc ["INT_ADD", "register:40f0:8", ["const:b66ffc:8", "const:4:8"]]
+ 00b66ffc ["CALL", null, ["callee:00bde090:8"]]
- 00b66fb8 bytes 22dc0194
+ 00b66ffc bytes 25dc0194
- 00b66fc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b66fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b67004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66fc0 bytes 600a04f9
+ 00b67004 bytes 602a04f9
- 00b66fa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b66fa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b66fe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66fa4 bytes 680a44f9
+ 00b66fe8 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e04d6e23194541127aa4788e009eef2"></a>

### [`00b66fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66fd4.md) → [`00b67018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67018.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b67048",
      "incomplete_value": true,
      "site": "00b67048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67004",
      "incomplete_value": true,
      "site": "00b67004",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6702c",
      "incomplete_value": true,
      "site": "00b6702c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fe8",
      "incomplete_value": true,
      "site": "00b66fe8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67038",
      "incomplete_value": false,
      "site": "00b67040",
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
            "const:ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ff4",
      "incomplete_value": false,
      "site": "00b66ffc",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b67028",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67038",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b67048",
      "WRITE",
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
      "00b67028",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67038",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b67048",
      "WRITE",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66fd4.md#insn-00b66ffc) · [`00b67004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66fd4.md#insn-00b67004) · [`00b66fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66fd4.md#insn-00b66fe4)
- 新版 `00b67040`（命令位置の公開資料なし） · `00b67048`（命令位置の公開資料なし） · `00b67028`（命令位置の公開資料なし）

~~~diff
- 00b66ffc ["INT_ADD", "register:40f0:8", ["const:b66ffc:8", "const:4:8"]]
- 00b66ffc ["CALL", null, ["callee:00bde090:8"]]
+ 00b67040 ["INT_ADD", "register:40f0:8", ["const:b67040:8", "const:4:8"]]
+ 00b67040 ["CALL", null, ["callee:00bde090:8"]]
- 00b66ffc bytes 11dc0194
+ 00b67040 bytes 14dc0194
- 00b67004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b67004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b67048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67004 bytes 600a04f9
+ 00b67048 bytes 602a04f9
- 00b66fe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b66fe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b67028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66fe4 bytes 680a44f9
+ 00b67028 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

