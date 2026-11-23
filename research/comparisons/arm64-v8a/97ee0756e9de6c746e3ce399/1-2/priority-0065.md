# v15.7.3 → v15.7.4 · 最優先の変更候補 (65)

[一覧の目次](README.md)

<a id="compare-edbc96c902218b0b5643045a725867dd"></a>

### [`00aece28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md) → [`00aece6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece6c.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

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
            "const:988:8"
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
    "old": {
      "definition_site": "00aece44",
      "incomplete_value": false,
      "site": "00aece50",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aece7c",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece88",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aece9c",
      "WRITE",
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
      "00aece7c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece88",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aece9c",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece50) · [`00aece58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece58) · [`00aece38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece38)
- 新版 `00aece94`（命令位置の公開資料なし） · `00aece9c`（命令位置の公開資料なし） · `00aece7c`（命令位置の公開資料なし）

~~~diff
- 00aece50 ["INT_ADD", "register:40f0:8", ["const:aece50:8", "const:4:8"]]
- 00aece50 ["CALL", null, ["callee:00bde090:8"]]
+ 00aece94 ["INT_ADD", "register:40f0:8", ["const:aece94:8", "const:4:8"]]
+ 00aece94 ["CALL", null, ["callee:00bde090:8"]]
- 00aece50 bytes 7cc40394
+ 00aece94 bytes 7fc40394
- 00aece58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aece58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aece9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aece9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aece58 bytes 60c604f9
+ 00aece9c bytes 60e604f9
- 00aece38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aece38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aece7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aece7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aece38 bytes 68c644f9
+ 00aece7c bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683b938b281012da1a99713b9b9ed155"></a>

### [`00aece78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md) → [`00aecebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecebc.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aecf00",
      "incomplete_value": true,
      "site": "00aecf00",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aeceac",
      "incomplete_value": true,
      "site": "00aeceb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "00aeced0",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecef0",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf44",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeced0",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecef0",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf44",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeceb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aeceb8) · [`00aecf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aecf00) · [`00aece8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aece8c)
- 新版 `00aecefc`（命令位置の公開資料なし） · `00aecf44`（命令位置の公開資料なし） · `00aeced0`（命令位置の公開資料なし）

~~~diff
- 00aeceb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeceb8 ["INT_ADD", "register:40f0:8", ["const:aeceb8:8", "const:4:8"]]
- 00aeceb8 ["CALLIND", null, ["register:0:8"]]
+ 00aecefc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aecefc ["INT_ADD", "register:40f0:8", ["const:aecefc:8", "const:4:8"]]
+ 00aecefc ["CALLIND", null, ["register:0:8"]]
- 00aeceb8 bytes 00013fd6
+ 00aecefc bytes 00013fd6
- 00aecf00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aecf00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:990:8"]]
- 00aecf00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aecf44 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aecf44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d0:8"]]
+ 00aecf44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aecf00 bytes a0422639
+ 00aecf44 bytes a0422739
- 00aece8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
- 00aece8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aece8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeced0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d0:8"]]
+ 00aeced0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeced0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aece8c bytes a8426639
+ 00aeced0 bytes a8426739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4915681a897d34af74bdfaff630c3f"></a>

### [`00aecf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md) → [`00aecf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aecf50",
      "incomplete_value": true,
      "site": "00aecf50",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aecfa0",
      "incomplete_value": true,
      "site": "00aecfa0",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aecf2c",
      "incomplete_value": true,
      "site": "00aecf2c",
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
      "00aecf6c",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf78",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecf94",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aecf6c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf78",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecf94",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecf50) · [`00aecf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecf9c) · [`00aecfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecfa0)
- 新版 `00aecf94`（命令位置の公開資料なし） · `00aecfe0`（命令位置の公開資料なし） · `00aecfe4`（命令位置の公開資料なし）

~~~diff
- 00aecf50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aecf50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aecf50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:990:8"]]
- 00aecf50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aecf94 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aecf94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aecf94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d0:8"]]
+ 00aecf94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aecf50 bytes bf422639
+ 00aecf94 bytes bf422739
- 00aecf9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecf9c ["INT_ADD", "register:40f0:8", ["const:aecf9c:8", "const:4:8"]]
- 00aecf9c ["CALLIND", null, ["register:0:8"]]
+ 00aecfe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aecfe0 ["INT_ADD", "register:40f0:8", ["const:aecfe0:8", "const:4:8"]]
+ 00aecfe0 ["CALLIND", null, ["register:0:8"]]
- 00aecf9c bytes 00013fd6
+ 00aecfe0 bytes 00013fd6
- 00aecfa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aecfa0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aecfa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aecfe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00aecfe4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aecfe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aecfa0 bytes 9fc604f9
+ 00aecfe4 bytes 9fe604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1cf4a8fa4ed193e87dba13e7e0c8b3a"></a>

### [`00aecfb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md) → [`00aecff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecff8.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aecff4",
      "incomplete_value": true,
      "site": "00aecff4",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aecfd0",
      "incomplete_value": true,
      "site": "00aecfd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aecfd8",
      "incomplete_value": false,
      "site": "00aecfec",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed00c",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed01c",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aed038",
      "WRITE",
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
      "00aed00c",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed01c",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aed038",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecfec) · [`00aecff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecff4) · [`00aecfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecfc8)
- 新版 `00aed030`（命令位置の公開資料なし） · `00aed038`（命令位置の公開資料なし） · `00aed00c`（命令位置の公開資料なし）

~~~diff
- 00aecfec ["INT_ADD", "register:40f0:8", ["const:aecfec:8", "const:4:8"]]
- 00aecfec ["CALL", null, ["callee:00bde090:8"]]
+ 00aed030 ["INT_ADD", "register:40f0:8", ["const:aed030:8", "const:4:8"]]
+ 00aed030 ["CALL", null, ["callee:00bde090:8"]]
- 00aecfec bytes 15c40394
+ 00aed030 bytes 18c40394
- 00aecff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aecff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00aed038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecff4 bytes 80c604f9
+ 00aed038 bytes 80e604f9
- 00aecfc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aecfc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed00c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00aed00c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecfc8 bytes 81c644f9
+ 00aed00c bytes 81e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f64d5db4e4dcff9f923c1b33b0dedf0"></a>

### [`00aed024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md) → [`00aed068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed068.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde630.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde680.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
    "old": {
      "definition_site": "00aed040",
      "incomplete_value": false,
      "site": "00aed044",
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
    "old": {
      "definition_site": "00aed050",
      "incomplete_value": true,
      "site": "00aed05c",
      "value": [
        "LOAD",
        "8",
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
      "00aed084",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed094",
      "DATA",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed084",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed094",
      "DATA",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed044) · [`00aed040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed040) · [`00aed04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed04c)
- 新版 `00aed088`（命令位置の公開資料なし） · `00aed084`（命令位置の公開資料なし） · `00aed090`（命令位置の公開資料なし）

~~~diff
- 00aed044 ["INT_ADD", "register:40f0:8", ["const:aed044:8", "const:4:8"]]
- 00aed044 ["CALL", null, ["callee:00bde180:8"]]
+ 00aed088 ["INT_ADD", "register:40f0:8", ["const:aed088:8", "const:4:8"]]
+ 00aed088 ["CALL", null, ["callee:00bde180:8"]]
- 00aed044 bytes 3bc40394
+ 00aed088 bytes 3ec40394
- 00aed040 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aed040 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed040 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed040 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed084 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed040 bytes 00501791
+ 00aed084 bytes 001c1591
- 00aed04c ["COPY", "tmp:0:8", ["const:998:8"]]
- 00aed04c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed04c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed04c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed090 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00aed090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed04c bytes 08612691
+ 00aed090 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-415b67934b863e5fe3d71e998120e8a9"></a>

### [`00aed060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md) → [`00aed0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed0a4.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed0a0",
      "incomplete_value": true,
      "site": "00aed0a0",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aed07c",
      "incomplete_value": true,
      "site": "00aed07c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed084",
      "incomplete_value": false,
      "site": "00aed098",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed0b8",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed0c8",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aed0e4",
      "WRITE",
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
      "00aed0b8",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed0c8",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aed0e4",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed098) · [`00aed0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed0a0) · [`00aed074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed074)
- 新版 `00aed0dc`（命令位置の公開資料なし） · `00aed0e4`（命令位置の公開資料なし） · `00aed0b8`（命令位置の公開資料なし）

~~~diff
- 00aed098 ["INT_ADD", "register:40f0:8", ["const:aed098:8", "const:4:8"]]
- 00aed098 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed0dc ["INT_ADD", "register:40f0:8", ["const:aed0dc:8", "const:4:8"]]
+ 00aed0dc ["CALL", null, ["callee:00bde090:8"]]
- 00aed098 bytes eac30394
+ 00aed0dc bytes edc30394
- 00aed0a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aed0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed0e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00aed0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed0a0 bytes 80c604f9
+ 00aed0e4 bytes 80e604f9
- 00aed074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aed074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed0b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00aed0b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed074 bytes 81c644f9
+ 00aed0b8 bytes 81e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce3e1cc565cf98c34a871a0bdf9ce54"></a>

### [`00aed0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md) → [`00aed114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed114.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed0ec",
      "incomplete_value": false,
      "site": "00aed0f0",
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
    "old": {
      "definition_site": "00aed0fc",
      "incomplete_value": true,
      "site": "00aed108",
      "value": [
        "LOAD",
        "8",
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
      "00aed130",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed140",
      "DATA",
      [
        "storage",
        "010a09a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed130",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed140",
      "DATA",
      [
        "storage",
        "010a09e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0f0) · [`00aed0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0ec) · [`00aed0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0f8)
- 新版 `00aed134`（命令位置の公開資料なし） · `00aed130`（命令位置の公開資料なし） · `00aed13c`（命令位置の公開資料なし）

~~~diff
- 00aed0f0 ["INT_ADD", "register:40f0:8", ["const:aed0f0:8", "const:4:8"]]
- 00aed0f0 ["CALL", null, ["callee:00bde180:8"]]
+ 00aed134 ["INT_ADD", "register:40f0:8", ["const:aed134:8", "const:4:8"]]
+ 00aed134 ["CALL", null, ["callee:00bde180:8"]]
- 00aed0f0 bytes 10c40394
+ 00aed134 bytes 13c40394
- 00aed0ec ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed0ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed0ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed0ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed130 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed0ec bytes 00fc1991
+ 00aed130 bytes 00c81791
- 00aed0f8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00aed0f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed0f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed0f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed13c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00aed13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed0f8 bytes 08812691
+ 00aed13c bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffd856a243b9def87b2e6243def6f051"></a>

### [`00aed10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md) → [`00aed150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed150.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed138",
      "incomplete_value": true,
      "site": "00aed138",
      "value": [
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
    "old": {
      "definition_site": "00aed120",
      "incomplete_value": true,
      "site": "00aed120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00aed120"
      ],
      [
        "FALL_THROUGH",
        "00aed164"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed164",
      "incomplete_value": true,
      "site": "00aed17c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed120",
      "incomplete_value": true,
      "site": "00aed138",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed160",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed17c",
      "WRITE",
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
      "00aed160",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed17c",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed138) · [`00aed11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed11c) · [`00aed130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed130)
- 新版 `00aed17c`（命令位置の公開資料なし） · `00aed160`（命令位置の公開資料なし） · `00aed174`（命令位置の公開資料なし）

~~~diff
- 00aed138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed17c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed17c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed138 bytes 60d604f9
+ 00aed17c bytes 60f604f9
- 00aed11c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed11c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed11c bytes 68d644f9
+ 00aed160 bytes 68f644f9
- 00aed130 ["INT_ADD", "register:40f0:8", ["const:aed130:8", "const:4:8"]]
- 00aed130 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed174 ["INT_ADD", "register:40f0:8", ["const:aed174:8", "const:4:8"]]
+ 00aed174 ["CALL", null, ["callee:00bde090:8"]]
- 00aed130 bytes c4c30394
+ 00aed174 bytes c7c30394
~~~


<a id="compare-f3b9b031cd2c2757dacdb258558aeac3"></a>

### [`00aed14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md) → [`00aed190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed190.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed178",
      "incomplete_value": true,
      "site": "00aed178",
      "value": [
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
    "old": {
      "definition_site": "00aed160",
      "incomplete_value": true,
      "site": "00aed160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00aed160"
      ],
      [
        "FALL_THROUGH",
        "00aed1a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed1a4",
      "incomplete_value": true,
      "site": "00aed1bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed160",
      "incomplete_value": true,
      "site": "00aed178",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed1a0",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1bc",
      "WRITE",
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
      "00aed1a0",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1bc",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed178) · [`00aed15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed15c) · [`00aed170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed170)
- 新版 `00aed1bc`（命令位置の公開資料なし） · `00aed1a0`（命令位置の公開資料なし） · `00aed1b4`（命令位置の公開資料なし）

~~~diff
- 00aed178 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed178 bytes 60d604f9
+ 00aed1bc bytes 60f604f9
- 00aed15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed15c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed1a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed1a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed15c bytes 68d644f9
+ 00aed1a0 bytes 68f644f9
- 00aed170 ["INT_ADD", "register:40f0:8", ["const:aed170:8", "const:4:8"]]
- 00aed170 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed1b4 ["INT_ADD", "register:40f0:8", ["const:aed1b4:8", "const:4:8"]]
+ 00aed1b4 ["CALL", null, ["callee:00bde090:8"]]
- 00aed170 bytes b4c30394
+ 00aed1b4 bytes b7c30394
~~~


<a id="compare-aba62b585b11a15668ee69749791d50b"></a>

### [`00aed18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md) → [`00aed1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed1d0.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aed1a0",
      "incomplete_value": true,
      "site": "00aed1a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00aed1a0"
      ],
      [
        "FALL_THROUGH",
        "00aed1e4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed1e4",
      "incomplete_value": true,
      "site": "00aed200",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed1a0",
      "incomplete_value": true,
      "site": "00aed1bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed1e0",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed200",
      "WRITE",
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
      "00aed1e0",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed200",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed1bc) · [`00aed19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed19c) · [`00aed1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed1b4)
- 新版 `00aed200`（命令位置の公開資料なし） · `00aed1e0`（命令位置の公開資料なし） · `00aed1f8`（命令位置の公開資料なし）

~~~diff
- 00aed1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed1bc bytes 60d604f9
+ 00aed200 bytes 60f604f9
- 00aed19c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed19c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed1e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed19c bytes 68d644f9
+ 00aed1e0 bytes 68f644f9
- 00aed1b4 ["INT_ADD", "register:40f0:8", ["const:aed1b4:8", "const:4:8"]]
- 00aed1b4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed1f8 ["INT_ADD", "register:40f0:8", ["const:aed1f8:8", "const:4:8"]]
+ 00aed1f8 ["CALL", null, ["callee:00bde090:8"]]
- 00aed1b4 bytes a3c30394
+ 00aed1f8 bytes a6c30394
~~~


<a id="compare-5a61de8fb6e41b7bd726c59a5e7fa184"></a>

### [`00aed1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md) → [`00aed214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed214.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

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
    "guard": [
      [
        "FALL_THROUGH",
        "00aed1e4"
      ],
      [
        "FALL_THROUGH",
        "00aed228"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed228",
      "incomplete_value": true,
      "site": "00aed244",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "site": "00aed200",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed224",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed244",
      "WRITE",
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
      "00aed224",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed244",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed200) · [`00aed1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed1e0) · [`00aed1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed1f8)
- 新版 `00aed244`（命令位置の公開資料なし） · `00aed224`（命令位置の公開資料なし） · `00aed23c`（命令位置の公開資料なし）

~~~diff
- 00aed200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed200 bytes 60d604f9
+ 00aed244 bytes 60f604f9
- 00aed1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed1e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00aed224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed1e0 bytes 68d644f9
+ 00aed224 bytes 68f644f9
- 00aed1f8 ["INT_ADD", "register:40f0:8", ["const:aed1f8:8", "const:4:8"]]
- 00aed1f8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed23c ["INT_ADD", "register:40f0:8", ["const:aed23c:8", "const:4:8"]]
+ 00aed23c ["CALL", null, ["callee:00bde090:8"]]
- 00aed1f8 bytes 92c30394
+ 00aed23c bytes 95c30394
~~~


<a id="compare-a5a7644256bd51eecb45d341d0363ce6"></a>

### [`00aed220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md) → [`00aed264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed264.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aed2a8",
      "incomplete_value": true,
      "site": "00aed2a8",
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
    "old": {
      "definition_site": "00aed254",
      "incomplete_value": true,
      "site": "00aed260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00aed278",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed298",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2ec",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed278",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed298",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2ec",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed260) · [`00aed2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed2a8) · [`00aed234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed234)
- 新版 `00aed2a4`（命令位置の公開資料なし） · `00aed2ec`（命令位置の公開資料なし） · `00aed278`（命令位置の公開資料なし）

~~~diff
- 00aed260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed260 ["INT_ADD", "register:40f0:8", ["const:aed260:8", "const:4:8"]]
- 00aed260 ["CALLIND", null, ["register:0:8"]]
+ 00aed2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed2a4 ["INT_ADD", "register:40f0:8", ["const:aed2a4:8", "const:4:8"]]
+ 00aed2a4 ["CALLIND", null, ["register:0:8"]]
- 00aed260 bytes 00013fd6
+ 00aed2a4 bytes 00013fd6
- 00aed2a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed2a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00aed2a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aed2ec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aed2ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f0:8"]]
+ 00aed2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed2a8 bytes a0c22639
+ 00aed2ec bytes a0c22739
- 00aed234 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00aed234 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed234 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed278 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f0:8"]]
+ 00aed278 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed278 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed234 bytes a8c26639
+ 00aed278 bytes a8c26739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ce7726c056e52bef25630cb654457c"></a>

### [`00aed2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md) → [`00aed300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aed2f8",
      "incomplete_value": true,
      "site": "00aed2f8",
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
    "old": {
      "definition_site": "00aed348",
      "incomplete_value": true,
      "site": "00aed348",
      "value": [
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
    "old": {
      "definition_site": "00aed2d4",
      "incomplete_value": true,
      "site": "00aed2d4",
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
      "00aed314",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed320",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed33c",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed314",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed320",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed33c",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed2f8) · [`00aed344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed344) · [`00aed348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed348)
- 新版 `00aed33c`（命令位置の公開資料なし） · `00aed388`（命令位置の公開資料なし） · `00aed38c`（命令位置の公開資料なし）

~~~diff
- 00aed2f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed2f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed2f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
- 00aed2f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aed33c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aed33c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aed33c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9f0:8"]]
+ 00aed33c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed2f8 bytes bfc22639
+ 00aed33c bytes bfc22739
- 00aed344 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed344 ["INT_ADD", "register:40f0:8", ["const:aed344:8", "const:4:8"]]
- 00aed344 ["CALLIND", null, ["register:0:8"]]
+ 00aed388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed388 ["INT_ADD", "register:40f0:8", ["const:aed388:8", "const:4:8"]]
+ 00aed388 ["CALLIND", null, ["register:0:8"]]
- 00aed344 bytes 00013fd6
+ 00aed388 bytes 00013fd6
- 00aed348 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed348 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aed38c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00aed38c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aed38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed348 bytes 9fd604f9
+ 00aed38c bytes 9ff604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66c989943779231227ac85dd7bd30839"></a>

### [`00aed35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md) → [`00aed3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed3a0.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed39c",
      "incomplete_value": true,
      "site": "00aed39c",
      "value": [
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
    "old": {
      "definition_site": "00aed378",
      "incomplete_value": true,
      "site": "00aed378",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00aed378"
      ],
      [
        "FALL_THROUGH",
        "00aed3bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed3bc",
      "incomplete_value": true,
      "site": "00aed3e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed378",
      "incomplete_value": true,
      "site": "00aed39c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed3b4",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed3e0",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed3f4",
      "PARAM",
      [
        "storage",
        "00c10560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aed3b4",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed3e0",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed3f4",
      "PARAM",
      [
        "storage",
        "00c105b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed39c) · [`00aed370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed370) · [`00aed394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed394)
- 新版 `00aed3e0`（命令位置の公開資料なし） · `00aed3b4`（命令位置の公開資料なし） · `00aed3d8`（命令位置の公開資料なし）

~~~diff
- 00aed39c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed39c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed3e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00aed3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed39c bytes 80d604f9
+ 00aed3e0 bytes 80f604f9
- 00aed370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed370 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed3b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00aed3b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed370 bytes 81d644f9
+ 00aed3b4 bytes 81f644f9
- 00aed394 ["INT_ADD", "register:40f0:8", ["const:aed394:8", "const:4:8"]]
- 00aed394 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed3d8 ["INT_ADD", "register:40f0:8", ["const:aed3d8:8", "const:4:8"]]
+ 00aed3d8 ["CALL", null, ["callee:00bde090:8"]]
- 00aed394 bytes 2bc30394
+ 00aed3d8 bytes 2ec30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6817cbed1ebb13af985bc51cdaca59ec"></a>

### [`00aed3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md) → [`00aed410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed410.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aed3e8",
      "incomplete_value": false,
      "site": "00aed3ec",
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
    "old": {
      "definition_site": "00aed3f8",
      "incomplete_value": true,
      "site": "00aed404",
      "value": [
        "LOAD",
        "8",
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
      "00aed42c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed43c",
      "DATA",
      [
        "storage",
        "010a09b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed42c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed43c",
      "DATA",
      [
        "storage",
        "010a09f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3ec) · [`00aed3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3e8) · [`00aed3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3f4)
- 新版 `00aed430`（命令位置の公開資料なし） · `00aed42c`（命令位置の公開資料なし） · `00aed438`（命令位置の公開資料なし）

~~~diff
- 00aed3ec ["INT_ADD", "register:40f0:8", ["const:aed3ec:8", "const:4:8"]]
- 00aed3ec ["CALL", null, ["callee:00bde180:8"]]
+ 00aed430 ["INT_ADD", "register:40f0:8", ["const:aed430:8", "const:4:8"]]
+ 00aed430 ["CALL", null, ["callee:00bde180:8"]]
- 00aed3ec bytes 51c30394
+ 00aed430 bytes 54c30394
- 00aed3e8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aed3e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed3e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed3e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed42c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed3e8 bytes 00501791
+ 00aed42c bytes 001c1591
- 00aed3f4 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00aed3f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed3f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed3f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed438 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00aed438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed3f4 bytes 08e12691
+ 00aed438 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a01e0eea9d1bf253c8c08c3cd9c615aa"></a>

### [`00aed408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md) → [`00aed44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed44c.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed448",
      "incomplete_value": true,
      "site": "00aed448",
      "value": [
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
    "old": {
      "definition_site": "00aed424",
      "incomplete_value": true,
      "site": "00aed424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00aed424"
      ],
      [
        "FALL_THROUGH",
        "00aed468"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aed468",
      "incomplete_value": true,
      "site": "00aed48c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed424",
      "incomplete_value": true,
      "site": "00aed448",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00aed460",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed48c",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed4a4",
      "PARAM",
      [
        "storage",
        "010a09c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed460",
      "READ",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed48c",
      "WRITE",
      [
        "storage",
        "010a09e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed4a4",
      "PARAM",
      [
        "storage",
        "010a0a08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed448) · [`00aed41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed41c) · [`00aed440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed440)
- 新版 `00aed48c`（命令位置の公開資料なし） · `00aed460`（命令位置の公開資料なし） · `00aed484`（命令位置の公開資料なし）

~~~diff
- 00aed448 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed48c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00aed48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed448 bytes 80d604f9
+ 00aed48c bytes 80f604f9
- 00aed41c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed41c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed460 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00aed460 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed41c bytes 81d644f9
+ 00aed460 bytes 81f644f9
- 00aed440 ["INT_ADD", "register:40f0:8", ["const:aed440:8", "const:4:8"]]
- 00aed440 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed484 ["INT_ADD", "register:40f0:8", ["const:aed484:8", "const:4:8"]]
+ 00aed484 ["CALL", null, ["callee:00bde090:8"]]
- 00aed440 bytes 00c30394
+ 00aed484 bytes 03c30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ea82cb0ccc4965863d30a453481824c"></a>

### [`00aed478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md) → [`00aed4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4bc.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed494",
      "incomplete_value": false,
      "site": "00aed498",
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
    "old": {
      "definition_site": "00aed4a4",
      "incomplete_value": true,
      "site": "00aed4b0",
      "value": [
        "LOAD",
        "8",
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
      "00aed4d8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed4e8",
      "DATA",
      [
        "storage",
        "010a09c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed4d8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed4e8",
      "DATA",
      [
        "storage",
        "010a0a08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed498) · [`00aed494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed494) · [`00aed4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed4a0)
- 新版 `00aed4dc`（命令位置の公開資料なし） · `00aed4d8`（命令位置の公開資料なし） · `00aed4e4`（命令位置の公開資料なし）

~~~diff
- 00aed498 ["INT_ADD", "register:40f0:8", ["const:aed498:8", "const:4:8"]]
- 00aed498 ["CALL", null, ["callee:00bde180:8"]]
+ 00aed4dc ["INT_ADD", "register:40f0:8", ["const:aed4dc:8", "const:4:8"]]
+ 00aed4dc ["CALL", null, ["callee:00bde180:8"]]
- 00aed498 bytes 26c30394
+ 00aed4dc bytes 29c30394
- 00aed494 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed494 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed494 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed494 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed4d8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed494 bytes 00fc1991
+ 00aed4d8 bytes 00c81791
- 00aed4a0 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00aed4a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed4a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed4a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed4e4 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00aed4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed4a0 bytes 08212791
+ 00aed4e4 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a68e98aef502ed80550d57c823c765fb"></a>

### [`00aed4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md) → [`00aed4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed4f8.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
    "old": {
      "definition_site": "00aed4e0",
      "incomplete_value": true,
      "site": "00aed4e0",
      "value": [
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
    "old": {
      "definition_site": "00aed4c8",
      "incomplete_value": true,
      "site": "00aed4c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed4d4",
      "incomplete_value": false,
      "site": "00aed4d8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed508",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed518",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed524",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed508",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed518",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed524",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4d8) · [`00aed4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4e0) · [`00aed4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4c4)
- 新版 `00aed51c`（命令位置の公開資料なし） · `00aed524`（命令位置の公開資料なし） · `00aed508`（命令位置の公開資料なし）

~~~diff
- 00aed4d8 ["INT_ADD", "register:40f0:8", ["const:aed4d8:8", "const:4:8"]]
- 00aed4d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed51c ["INT_ADD", "register:40f0:8", ["const:aed51c:8", "const:4:8"]]
+ 00aed51c ["CALL", null, ["callee:00bde090:8"]]
- 00aed4d8 bytes dac20394
+ 00aed51c bytes ddc20394
- 00aed4e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed4e0 bytes 60ea04f9
+ 00aed524 bytes 600a05f9
- 00aed4c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed4c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed508 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed508 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed4c4 bytes 68ea44f9
+ 00aed508 bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e100240267fd2a8f3a130a044e031860"></a>

### [`00aed4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md) → [`00aed538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed538.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed520",
      "incomplete_value": true,
      "site": "00aed520",
      "value": [
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
    "old": {
      "definition_site": "00aed508",
      "incomplete_value": true,
      "site": "00aed508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed510",
      "incomplete_value": false,
      "site": "00aed518",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed548",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed554",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed564",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed548",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed554",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed564",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed518) · [`00aed520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed520) · [`00aed504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed504)
- 新版 `00aed55c`（命令位置の公開資料なし） · `00aed564`（命令位置の公開資料なし） · `00aed548`（命令位置の公開資料なし）

~~~diff
- 00aed518 ["INT_ADD", "register:40f0:8", ["const:aed518:8", "const:4:8"]]
- 00aed518 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed55c ["INT_ADD", "register:40f0:8", ["const:aed55c:8", "const:4:8"]]
+ 00aed55c ["CALL", null, ["callee:00bde090:8"]]
- 00aed518 bytes cac20394
+ 00aed55c bytes cdc20394
- 00aed520 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed520 bytes 60ea04f9
+ 00aed564 bytes 600a05f9
- 00aed504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed504 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed504 bytes 68ea44f9
+ 00aed548 bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f6ca7dd22cc82400a7e773c7856b340"></a>

### [`00aed534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md) → [`00aed578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed578.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aed548",
      "incomplete_value": true,
      "site": "00aed548",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed588",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed598",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed5a8",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed588",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed598",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed5a8",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed55c) · [`00aed564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed564) · [`00aed544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed544)
- 新版 `00aed5a0`（命令位置の公開資料なし） · `00aed5a8`（命令位置の公開資料なし） · `00aed588`（命令位置の公開資料なし）

~~~diff
- 00aed55c ["INT_ADD", "register:40f0:8", ["const:aed55c:8", "const:4:8"]]
- 00aed55c ["CALL", null, ["callee:00bde090:8"]]
+ 00aed5a0 ["INT_ADD", "register:40f0:8", ["const:aed5a0:8", "const:4:8"]]
+ 00aed5a0 ["CALL", null, ["callee:00bde090:8"]]
- 00aed55c bytes b9c20394
+ 00aed5a0 bytes bcc20394
- 00aed564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed564 bytes 60ea04f9
+ 00aed5a8 bytes 600a05f9
- 00aed544 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed588 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed544 bytes 68ea44f9
+ 00aed588 bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ea9de5d2dd31a492bb31c0de0c77009"></a>

### [`00aed578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md) → [`00aed5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed5bc.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed594",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed5cc",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed5d8",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed5ec",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed5cc",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed5d8",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed5ec",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed5a0) · [`00aed5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed5a8) · [`00aed588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed588)
- 新版 `00aed5e4`（命令位置の公開資料なし） · `00aed5ec`（命令位置の公開資料なし） · `00aed5cc`（命令位置の公開資料なし）

~~~diff
- 00aed5a0 ["INT_ADD", "register:40f0:8", ["const:aed5a0:8", "const:4:8"]]
- 00aed5a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed5e4 ["INT_ADD", "register:40f0:8", ["const:aed5e4:8", "const:4:8"]]
+ 00aed5e4 ["CALL", null, ["callee:00bde090:8"]]
- 00aed5a0 bytes a8c20394
+ 00aed5e4 bytes abc20394
- 00aed5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed5a8 bytes 60ea04f9
+ 00aed5ec bytes 600a05f9
- 00aed588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed588 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed5cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00aed5cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed588 bytes 68ea44f9
+ 00aed5cc bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d2c4b55b6ca17f9e644b3625a8d243"></a>

### [`00aed5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md) → [`00aed60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed60c.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aed650",
      "incomplete_value": true,
      "site": "00aed650",
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
    "old": {
      "definition_site": "00aed5fc",
      "incomplete_value": true,
      "site": "00aed608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
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
      "00aed620",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed640",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed694",
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed620",
      "READ",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed640",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed694",
      "WRITE",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed608) · [`00aed650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed650) · [`00aed5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed5dc)
- 新版 `00aed64c`（命令位置の公開資料なし） · `00aed694`（命令位置の公開資料なし） · `00aed620`（命令位置の公開資料なし）

~~~diff
- 00aed608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed608 ["INT_ADD", "register:40f0:8", ["const:aed608:8", "const:4:8"]]
- 00aed608 ["CALLIND", null, ["register:0:8"]]
+ 00aed64c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed64c ["INT_ADD", "register:40f0:8", ["const:aed64c:8", "const:4:8"]]
+ 00aed64c ["CALLIND", null, ["register:0:8"]]
- 00aed608 bytes 00013fd6
+ 00aed64c bytes 00013fd6
- 00aed650 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed650 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d8:8"]]
- 00aed650 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aed694 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aed694 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a18:8"]]
+ 00aed694 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed650 bytes a0622739
+ 00aed694 bytes a0622839
- 00aed5dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d8:8"]]
- 00aed5dc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed5dc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed620 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a18:8"]]
+ 00aed620 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed620 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed5dc bytes a8626739
+ 00aed620 bytes a8626839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1133cfce7864f4f0f03ec0e4cf8cd07e"></a>

### [`00aed664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md) → [`00aed6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed6a8.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aed6a0",
      "incomplete_value": true,
      "site": "00aed6a0",
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
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aed6f0",
      "incomplete_value": true,
      "site": "00aed6f0",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aed67c",
      "incomplete_value": true,
      "site": "00aed67c",
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
      "00aed6bc",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed6c8",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed6e4",
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed6bc",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed6c8",
      "READ",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed6e4",
      "WRITE",
      [
        "storage",
        "010a0a18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6a0) · [`00aed6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6ec) · [`00aed6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6f0)
- 新版 `00aed6e4`（命令位置の公開資料なし） · `00aed730`（命令位置の公開資料なし） · `00aed734`（命令位置の公開資料なし）

~~~diff
- 00aed6a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed6a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed6a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d8:8"]]
- 00aed6a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aed6e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aed6e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aed6e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a18:8"]]
+ 00aed6e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed6a0 bytes bf622739
+ 00aed6e4 bytes bf622839
- 00aed6ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed6ec ["INT_ADD", "register:40f0:8", ["const:aed6ec:8", "const:4:8"]]
- 00aed6ec ["CALLIND", null, ["register:0:8"]]
+ 00aed730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed730 ["INT_ADD", "register:40f0:8", ["const:aed730:8", "const:4:8"]]
+ 00aed730 ["CALLIND", null, ["register:0:8"]]
- 00aed6ec bytes 00013fd6
+ 00aed730 bytes 00013fd6
- 00aed6f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed6f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aed734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
+ 00aed734 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aed734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed6f0 bytes 9fea04f9
+ 00aed734 bytes 9f0a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78ad8b218d5ce009faec497270a1266b"></a>

### [`00aed704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md) → [`00aed748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed748.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed744",
      "incomplete_value": true,
      "site": "00aed744",
      "value": [
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
    "old": {
      "definition_site": "00aed720",
      "incomplete_value": true,
      "site": "00aed720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed728",
      "incomplete_value": false,
      "site": "00aed73c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed75c",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed76c",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed788",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed75c",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed76c",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed788",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed73c) · [`00aed744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed744) · [`00aed718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed718)
- 新版 `00aed780`（命令位置の公開資料なし） · `00aed788`（命令位置の公開資料なし） · `00aed75c`（命令位置の公開資料なし）

~~~diff
- 00aed73c ["INT_ADD", "register:40f0:8", ["const:aed73c:8", "const:4:8"]]
- 00aed73c ["CALL", null, ["callee:00bde090:8"]]
+ 00aed780 ["INT_ADD", "register:40f0:8", ["const:aed780:8", "const:4:8"]]
+ 00aed780 ["CALL", null, ["callee:00bde090:8"]]
- 00aed73c bytes 41c20394
+ 00aed780 bytes 44c20394
- 00aed744 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
+ 00aed788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed744 bytes 80ea04f9
+ 00aed788 bytes 800a05f9
- 00aed718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed718 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed75c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
+ 00aed75c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed718 bytes 81ea44f9
+ 00aed75c bytes 810a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e14b2482f1c9f225ec014ee93c8e7a7"></a>

### [`00aed774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md) → [`00aed7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7b8.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aed790",
      "incomplete_value": false,
      "site": "00aed794",
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
    "old": {
      "definition_site": "00aed7a0",
      "incomplete_value": true,
      "site": "00aed7ac",
      "value": [
        "LOAD",
        "8",
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
      "00aed7d4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed7e4",
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
      "00aed7d4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed7e4",
      "DATA",
      [
        "storage",
        "010a0a20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed794) · [`00aed790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed790) · [`00aed79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed79c)
- 新版 `00aed7d8`（命令位置の公開資料なし） · `00aed7d4`（命令位置の公開資料なし） · `00aed7e0`（命令位置の公開資料なし）

~~~diff
- 00aed794 ["INT_ADD", "register:40f0:8", ["const:aed794:8", "const:4:8"]]
- 00aed794 ["CALL", null, ["callee:00bde180:8"]]
+ 00aed7d8 ["INT_ADD", "register:40f0:8", ["const:aed7d8:8", "const:4:8"]]
+ 00aed7d8 ["CALL", null, ["callee:00bde180:8"]]
- 00aed794 bytes 67c20394
+ 00aed7d8 bytes 6ac20394
- 00aed790 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aed790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed7d4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed7d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed7d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed7d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed790 bytes 00501791
+ 00aed7d4 bytes 001c1591
- 00aed79c ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00aed79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed7e0 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00aed7e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed7e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed79c bytes 08812791
+ 00aed7e0 bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7c56bd6a9ae6e650f28b82cea4ba770"></a>

### [`00aed7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md) → [`00aed7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed7f4.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aed7f0",
      "incomplete_value": true,
      "site": "00aed7f0",
      "value": [
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
    "old": {
      "definition_site": "00aed7cc",
      "incomplete_value": true,
      "site": "00aed7cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed7d4",
      "incomplete_value": false,
      "site": "00aed7e8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed808",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed818",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed834",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed808",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed818",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "00aed834",
      "WRITE",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7e8) · [`00aed7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7f0) · [`00aed7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7c4)
- 新版 `00aed82c`（命令位置の公開資料なし） · `00aed834`（命令位置の公開資料なし） · `00aed808`（命令位置の公開資料なし）

~~~diff
- 00aed7e8 ["INT_ADD", "register:40f0:8", ["const:aed7e8:8", "const:4:8"]]
- 00aed7e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed82c ["INT_ADD", "register:40f0:8", ["const:aed82c:8", "const:4:8"]]
+ 00aed82c ["CALL", null, ["callee:00bde090:8"]]
- 00aed7e8 bytes 16c20394
+ 00aed82c bytes 19c20394
- 00aed7f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
+ 00aed834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed7f0 bytes 80ea04f9
+ 00aed834 bytes 800a05f9
- 00aed7c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed7c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
+ 00aed808 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed7c4 bytes 81ea44f9
+ 00aed808 bytes 810a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e063e818b9b7aa68c4a79b9dd02922a"></a>

### [`00aed820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md) → [`00aed864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed864.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aed83c",
      "incomplete_value": false,
      "site": "00aed840",
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
    "old": {
      "definition_site": "00aed84c",
      "incomplete_value": true,
      "site": "00aed858",
      "value": [
        "LOAD",
        "8",
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
      "00aed880",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed890",
      "DATA",
      [
        "storage",
        "010a09e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed880",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed890",
      "DATA",
      [
        "storage",
        "010a0a28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed840) · [`00aed83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed83c) · [`00aed848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed848)
- 新版 `00aed884`（命令位置の公開資料なし） · `00aed880`（命令位置の公開資料なし） · `00aed88c`（命令位置の公開資料なし）

~~~diff
- 00aed840 ["INT_ADD", "register:40f0:8", ["const:aed840:8", "const:4:8"]]
- 00aed840 ["CALL", null, ["callee:00bde180:8"]]
+ 00aed884 ["INT_ADD", "register:40f0:8", ["const:aed884:8", "const:4:8"]]
+ 00aed884 ["CALL", null, ["callee:00bde180:8"]]
- 00aed840 bytes 3cc20394
+ 00aed884 bytes 3fc20394
- 00aed83c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed83c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed83c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed83c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed880 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed83c bytes 00fc1991
+ 00aed880 bytes 00c81791
- 00aed848 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00aed848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed88c ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00aed88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed848 bytes 08a12791
+ 00aed88c bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a226e21220172ef0dcdd0ddd054566c"></a>

### [`00aed85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md) → [`00aed8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8a0.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
    "old": {
      "definition_site": "00aed888",
      "incomplete_value": true,
      "site": "00aed888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed870",
      "incomplete_value": true,
      "site": "00aed870",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed87c",
      "incomplete_value": false,
      "site": "00aed880",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed8b0",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8c0",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed8cc",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed8b0",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8c0",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aed8cc",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed880) · [`00aed888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed888) · [`00aed86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed86c)
- 新版 `00aed8c4`（命令位置の公開資料なし） · `00aed8cc`（命令位置の公開資料なし） · `00aed8b0`（命令位置の公開資料なし）

~~~diff
- 00aed880 ["INT_ADD", "register:40f0:8", ["const:aed880:8", "const:4:8"]]
- 00aed880 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed8c4 ["INT_ADD", "register:40f0:8", ["const:aed8c4:8", "const:4:8"]]
+ 00aed8c4 ["CALL", null, ["callee:00bde090:8"]]
- 00aed880 bytes f0c10394
+ 00aed8c4 bytes f3c10394
- 00aed888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed888 bytes 60fa04f9
+ 00aed8cc bytes 601a05f9
- 00aed86c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed86c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed8b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed8b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed86c bytes 68fa44f9
+ 00aed8b0 bytes 681a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a8a348f27ed914bb3f56fdb28537b7e"></a>

### [`00aed89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md) → [`00aed8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed8e0.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aed8c8",
      "incomplete_value": true,
      "site": "00aed8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed8b0",
      "incomplete_value": true,
      "site": "00aed8b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aed8b8",
      "incomplete_value": false,
      "site": "00aed8c0",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed8f0",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8fc",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed90c",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed8f0",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8fc",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aed90c",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8c0) · [`00aed8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8c8) · [`00aed8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8ac)
- 新版 `00aed904`（命令位置の公開資料なし） · `00aed90c`（命令位置の公開資料なし） · `00aed8f0`（命令位置の公開資料なし）

~~~diff
- 00aed8c0 ["INT_ADD", "register:40f0:8", ["const:aed8c0:8", "const:4:8"]]
- 00aed8c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed904 ["INT_ADD", "register:40f0:8", ["const:aed904:8", "const:4:8"]]
+ 00aed904 ["CALL", null, ["callee:00bde090:8"]]
- 00aed8c0 bytes e0c10394
+ 00aed904 bytes e3c10394
- 00aed8c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed8c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed8c8 bytes 60fa04f9
+ 00aed90c bytes 601a05f9
- 00aed8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed8ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed8f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed8f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed8ac bytes 68fa44f9
+ 00aed8f0 bytes 681a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89559accbfc9dbbed8b3c1134aa7d93"></a>

### [`00aed8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md) → [`00aed920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed920.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed8f0",
      "incomplete_value": true,
      "site": "00aed8f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed930",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed940",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed950",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed930",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed940",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aed950",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed904) · [`00aed90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed90c) · [`00aed8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed8ec)
- 新版 `00aed948`（命令位置の公開資料なし） · `00aed950`（命令位置の公開資料なし） · `00aed930`（命令位置の公開資料なし）

~~~diff
- 00aed904 ["INT_ADD", "register:40f0:8", ["const:aed904:8", "const:4:8"]]
- 00aed904 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed948 ["INT_ADD", "register:40f0:8", ["const:aed948:8", "const:4:8"]]
+ 00aed948 ["CALL", null, ["callee:00bde090:8"]]
- 00aed904 bytes cfc10394
+ 00aed948 bytes d2c10394
- 00aed90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed90c bytes 60fa04f9
+ 00aed950 bytes 601a05f9
- 00aed8ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed8ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed8ec bytes 68fa44f9
+ 00aed930 bytes 681a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcf7b18765ccf6f9a05170ce5d19e890"></a>

### [`00aed920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md) → [`00aed964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed964.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

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
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aed93c",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed974",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed980",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed994",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed974",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed980",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aed994",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed948) · [`00aed950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed950) · [`00aed930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed930)
- 新版 `00aed98c`（命令位置の公開資料なし） · `00aed994`（命令位置の公開資料なし） · `00aed974`（命令位置の公開資料なし）

~~~diff
- 00aed948 ["INT_ADD", "register:40f0:8", ["const:aed948:8", "const:4:8"]]
- 00aed948 ["CALL", null, ["callee:00bde090:8"]]
+ 00aed98c ["INT_ADD", "register:40f0:8", ["const:aed98c:8", "const:4:8"]]
+ 00aed98c ["CALL", null, ["callee:00bde090:8"]]
- 00aed948 bytes bec10394
+ 00aed98c bytes c1c10394
- 00aed950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed950 bytes 60fa04f9
+ 00aed994 bytes 601a05f9
- 00aed930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00aed974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed930 bytes 68fa44f9
+ 00aed974 bytes 681a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e49fe706bdd5bda1fb13bc9ae66a7e4"></a>

### [`00aed970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md) → [`00aed9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed9b4.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aed9f8",
      "incomplete_value": true,
      "site": "00aed9f8",
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
            "const:9f8:8"
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
    "old": {
      "definition_site": "00aed9a4",
      "incomplete_value": true,
      "site": "00aed9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "00aed9c8",
      "READ",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed9e8",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda3c",
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed9c8",
      "READ",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed9e8",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda3c",
      "WRITE",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed9b0) · [`00aed9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed9f8) · [`00aed984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed984)
- 新版 `00aed9f4`（命令位置の公開資料なし） · `00aeda3c`（命令位置の公開資料なし） · `00aed9c8`（命令位置の公開資料なし）

~~~diff
- 00aed9b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed9b0 ["INT_ADD", "register:40f0:8", ["const:aed9b0:8", "const:4:8"]]
- 00aed9b0 ["CALLIND", null, ["register:0:8"]]
+ 00aed9f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed9f4 ["INT_ADD", "register:40f0:8", ["const:aed9f4:8", "const:4:8"]]
+ 00aed9f4 ["CALLIND", null, ["register:0:8"]]
- 00aed9b0 bytes 00013fd6
+ 00aed9f4 bytes 00013fd6
- 00aed9f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed9f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f8:8"]]
- 00aed9f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeda3c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeda3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a38:8"]]
+ 00aeda3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed9f8 bytes a0e22739
+ 00aeda3c bytes a0e22839
- 00aed984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
- 00aed984 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed984 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed9c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a38:8"]]
+ 00aed9c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed9c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed984 bytes a8e26739
+ 00aed9c8 bytes a8e26839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53fcdfa7d13ca2f9e32c4b691784e964"></a>

### [`00aeda0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md) → [`00aeda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeda50.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aeda48",
      "incomplete_value": true,
      "site": "00aeda48",
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
            "const:9f8:8"
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
    "old": {
      "definition_site": "00aeda98",
      "incomplete_value": true,
      "site": "00aeda98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aeda24",
      "incomplete_value": true,
      "site": "00aeda24",
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
      "00aeda64",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda70",
      "READ",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeda8c",
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeda64",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda70",
      "READ",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeda8c",
      "WRITE",
      [
        "storage",
        "010a0a38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeda48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda48) · [`00aeda94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda94) · [`00aeda98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda98)
- 新版 `00aeda8c`（命令位置の公開資料なし） · `00aedad8`（命令位置の公開資料なし） · `00aedadc`（命令位置の公開資料なし）

~~~diff
- 00aeda48 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeda48 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeda48 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9f8:8"]]
- 00aeda48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeda8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeda8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeda8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a38:8"]]
+ 00aeda8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeda48 bytes bfe22739
+ 00aeda8c bytes bfe22839
- 00aeda94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeda94 ["INT_ADD", "register:40f0:8", ["const:aeda94:8", "const:4:8"]]
- 00aeda94 ["CALLIND", null, ["register:0:8"]]
+ 00aedad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aedad8 ["INT_ADD", "register:40f0:8", ["const:aedad8:8", "const:4:8"]]
+ 00aedad8 ["CALLIND", null, ["register:0:8"]]
- 00aeda94 bytes 00013fd6
+ 00aedad8 bytes 00013fd6
- 00aeda98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aeda98 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeda98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aedadc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
+ 00aedadc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aedadc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeda98 bytes 9ffa04f9
+ 00aedadc bytes 9f1a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52061bc9526a74e20225d69405663b5a"></a>

### [`00aedaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md) → [`00aedaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aedb30",
      "incomplete_value": true,
      "site": "00aedb30",
      "value": [
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
    "old": {
      "definition_site": "00aedaec",
      "incomplete_value": true,
      "site": "00aedaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "definition_site": "00aedb0c",
      "incomplete_value": true,
      "site": "00aedb0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedac8",
      "incomplete_value": true,
      "site": "00aedac8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedb14",
      "incomplete_value": false,
      "site": "00aedb28",
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
    "old": {
      "definition_site": "00aedad0",
      "incomplete_value": false,
      "site": "00aedae4",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedb04",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedb14",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aedb30",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedb04",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedb14",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aedb30",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md#insn-00aedae4) · [`00aedaec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md#insn-00aedaec) · [`00aedac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md#insn-00aedac0)
- 新版 `00aedb28`（命令位置の公開資料なし） · `00aedb30`（命令位置の公開資料なし） · `00aedb04`（命令位置の公開資料なし）

~~~diff
- 00aedae4 ["INT_ADD", "register:40f0:8", ["const:aedae4:8", "const:4:8"]]
- 00aedae4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedb28 ["INT_ADD", "register:40f0:8", ["const:aedb28:8", "const:4:8"]]
+ 00aedb28 ["CALL", null, ["callee:00bde090:8"]]
- 00aedae4 bytes 57c10394
+ 00aedb28 bytes 5ac10394
- 00aedaec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aedaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedb30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
+ 00aedb30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedaec bytes 80fa04f9
+ 00aedb30 bytes 801a05f9
- 00aedac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aedac0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedb04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
+ 00aedb04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedac0 bytes 81fa44f9
+ 00aedb04 bytes 811a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ad32faf11046ec0d8a3d7482777320"></a>

### [`00aedb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md) → [`00aedb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb60.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aedb38",
      "incomplete_value": false,
      "site": "00aedb3c",
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
    "old": {
      "definition_site": "00aedb48",
      "incomplete_value": true,
      "site": "00aedb54",
      "value": [
        "LOAD",
        "8",
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
      "00aedb7c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aedb8c",
      "DATA",
      [
        "storage",
        "010a0a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedb7c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aedb8c",
      "DATA",
      [
        "storage",
        "010a0a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb3c) · [`00aedb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb38) · [`00aedb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb44)
- 新版 `00aedb80`（命令位置の公開資料なし） · `00aedb7c`（命令位置の公開資料なし） · `00aedb88`（命令位置の公開資料なし）

~~~diff
- 00aedb3c ["INT_ADD", "register:40f0:8", ["const:aedb3c:8", "const:4:8"]]
- 00aedb3c ["CALL", null, ["callee:00bde180:8"]]
+ 00aedb80 ["INT_ADD", "register:40f0:8", ["const:aedb80:8", "const:4:8"]]
+ 00aedb80 ["CALL", null, ["callee:00bde180:8"]]
- 00aedb3c bytes 7dc10394
+ 00aedb80 bytes 80c10394
- 00aedb38 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aedb38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedb7c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aedb7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedb7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedb7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedb38 bytes 00501791
+ 00aedb7c bytes 001c1591
- 00aedb44 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00aedb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aedb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aedb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedb88 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00aedb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aedb44 bytes 08012891
+ 00aedb88 bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0918e1bc934f087711d96acae2692adb"></a>

### [`00aedb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md) → [`00aedb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedb9c.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aedb98",
      "incomplete_value": true,
      "site": "00aedb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
    "old": {
      "definition_site": "00aedb74",
      "incomplete_value": true,
      "site": "00aedb74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedb7c",
      "incomplete_value": false,
      "site": "00aedb90",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedbb0",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedbc0",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aedbdc",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedbb0",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedbc0",
      "PARAM",
      [
        "storage",
        "002a8ca4",
        null,
        "string"
      ]
    ],
    [
      "00aedbdc",
      "WRITE",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md#insn-00aedb90) · [`00aedb98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md#insn-00aedb98) · [`00aedb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md#insn-00aedb6c)
- 新版 `00aedbd4`（命令位置の公開資料なし） · `00aedbdc`（命令位置の公開資料なし） · `00aedbb0`（命令位置の公開資料なし）

~~~diff
- 00aedb90 ["INT_ADD", "register:40f0:8", ["const:aedb90:8", "const:4:8"]]
- 00aedb90 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedbd4 ["INT_ADD", "register:40f0:8", ["const:aedbd4:8", "const:4:8"]]
+ 00aedbd4 ["CALL", null, ["callee:00bde090:8"]]
- 00aedb90 bytes 2cc10394
+ 00aedbd4 bytes 2fc10394
- 00aedb98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aedb98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedbdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
+ 00aedbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedb98 bytes 80fa04f9
+ 00aedbdc bytes 801a05f9
- 00aedb6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aedb6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedbb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
+ 00aedbb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedb6c bytes 81fa44f9
+ 00aedbb0 bytes 811a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-957065c961b8e5c86041ab5683787492"></a>

### [`00aedbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md) → [`00aedc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aedbe4",
      "incomplete_value": false,
      "site": "00aedbe8",
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
    "old": {
      "definition_site": "00aedbf4",
      "incomplete_value": true,
      "site": "00aedc00",
      "value": [
        "LOAD",
        "8",
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
      "00aedc28",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aedc38",
      "DATA",
      [
        "storage",
        "010a0a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aedc28",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aedc38",
      "DATA",
      [
        "storage",
        "010a0a58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbe8) · [`00aedbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbe4) · [`00aedbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbf0)
- 新版 `00aedc2c`（命令位置の公開資料なし） · `00aedc28`（命令位置の公開資料なし） · `00aedc34`（命令位置の公開資料なし）

~~~diff
- 00aedbe8 ["INT_ADD", "register:40f0:8", ["const:aedbe8:8", "const:4:8"]]
- 00aedbe8 ["CALL", null, ["callee:00bde180:8"]]
+ 00aedc2c ["INT_ADD", "register:40f0:8", ["const:aedc2c:8", "const:4:8"]]
+ 00aedc2c ["CALL", null, ["callee:00bde180:8"]]
- 00aedbe8 bytes 52c10394
+ 00aedc2c bytes 55c10394
- 00aedbe4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aedbe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedbe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedbe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedc28 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aedc28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedc28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedc28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedbe4 bytes 00fc1991
+ 00aedc28 bytes 00c81791
- 00aedbf0 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 00aedbf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aedbf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aedbf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedc34 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00aedc34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedc34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedc34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aedbf0 bytes 08612891
+ 00aedc34 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57ae221e6ee24ed475c934e1abfc962"></a>

### [`00aedc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md) → [`00aedc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc48.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
    "old": {
      "definition_site": "00aedc30",
      "incomplete_value": true,
      "site": "00aedc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
    "old": {
      "definition_site": "00aedc18",
      "incomplete_value": true,
      "site": "00aedc18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedc24",
      "incomplete_value": false,
      "site": "00aedc28",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedc58",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc68",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedc74",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedc58",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc68",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedc74",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc28) · [`00aedc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc30) · [`00aedc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc14)
- 新版 `00aedc6c`（命令位置の公開資料なし） · `00aedc74`（命令位置の公開資料なし） · `00aedc58`（命令位置の公開資料なし）

~~~diff
- 00aedc28 ["INT_ADD", "register:40f0:8", ["const:aedc28:8", "const:4:8"]]
- 00aedc28 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedc6c ["INT_ADD", "register:40f0:8", ["const:aedc6c:8", "const:4:8"]]
+ 00aedc6c ["CALL", null, ["callee:00bde090:8"]]
- 00aedc28 bytes 06c10394
+ 00aedc6c bytes 09c10394
- 00aedc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedc30 bytes 601205f9
+ 00aedc74 bytes 603205f9
- 00aedc14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedc58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedc58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedc14 bytes 681245f9
+ 00aedc58 bytes 683245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc84c57dff4488a44b073e3b2073b4a"></a>

### [`00aedc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md) → [`00aedc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc88.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aedc70",
      "incomplete_value": true,
      "site": "00aedc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
    "old": {
      "definition_site": "00aedc58",
      "incomplete_value": true,
      "site": "00aedc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedc60",
      "incomplete_value": false,
      "site": "00aedc68",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedc98",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedca4",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedcb4",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedc98",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedca4",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedcb4",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc68) · [`00aedc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc70) · [`00aedc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc54)
- 新版 `00aedcac`（命令位置の公開資料なし） · `00aedcb4`（命令位置の公開資料なし） · `00aedc98`（命令位置の公開資料なし）

~~~diff
- 00aedc68 ["INT_ADD", "register:40f0:8", ["const:aedc68:8", "const:4:8"]]
- 00aedc68 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedcac ["INT_ADD", "register:40f0:8", ["const:aedcac:8", "const:4:8"]]
+ 00aedcac ["CALL", null, ["callee:00bde090:8"]]
- 00aedc68 bytes f6c00394
+ 00aedcac bytes f9c00394
- 00aedc70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedcb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedcb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedc70 bytes 601205f9
+ 00aedcb4 bytes 603205f9
- 00aedc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedc98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedc98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedc54 bytes 681245f9
+ 00aedc98 bytes 683245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af593b477ef08983e11d2bfedd2ac80"></a>

### [`00aedc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md) → [`00aedcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedcc8.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:a20:8"
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
    "old": {
      "definition_site": "00aedc98",
      "incomplete_value": true,
      "site": "00aedc98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedcd8",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedce8",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedcf8",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedcd8",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedce8",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedcf8",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedcac) · [`00aedcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedcb4) · [`00aedc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedc94)
- 新版 `00aedcf0`（命令位置の公開資料なし） · `00aedcf8`（命令位置の公開資料なし） · `00aedcd8`（命令位置の公開資料なし）

~~~diff
- 00aedcac ["INT_ADD", "register:40f0:8", ["const:aedcac:8", "const:4:8"]]
- 00aedcac ["CALL", null, ["callee:00bde090:8"]]
+ 00aedcf0 ["INT_ADD", "register:40f0:8", ["const:aedcf0:8", "const:4:8"]]
+ 00aedcf0 ["CALL", null, ["callee:00bde090:8"]]
- 00aedcac bytes e5c00394
+ 00aedcf0 bytes e8c00394
- 00aedcb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedcb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedcf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedcf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedcb4 bytes 601205f9
+ 00aedcf8 bytes 603205f9
- 00aedc94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedcd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedcd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedc94 bytes 681245f9
+ 00aedcd8 bytes 683245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed3d196d44faf28b9bbd930c1ee7360b"></a>

### [`00aedcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md) → [`00aedd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

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
            "const:a20:8"
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
    "old": {
      "definition_site": "00aedce4",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedd1c",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedd28",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedd3c",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedd1c",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedd28",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedd3c",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcf0) · [`00aedcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcf8) · [`00aedcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcd8)
- 新版 `00aedd34`（命令位置の公開資料なし） · `00aedd3c`（命令位置の公開資料なし） · `00aedd1c`（命令位置の公開資料なし）

~~~diff
- 00aedcf0 ["INT_ADD", "register:40f0:8", ["const:aedcf0:8", "const:4:8"]]
- 00aedcf0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedd34 ["INT_ADD", "register:40f0:8", ["const:aedd34:8", "const:4:8"]]
+ 00aedd34 ["CALL", null, ["callee:00bde090:8"]]
- 00aedcf0 bytes d4c00394
+ 00aedd34 bytes d7c00394
- 00aedcf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedcf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedcf8 bytes 601205f9
+ 00aedd3c bytes 603205f9
- 00aedcd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedcd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedd1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
+ 00aedd1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedcd8 bytes 681245f9
+ 00aedd1c bytes 683245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6230e7fee5ce7636ee54a5e26aabcf"></a>

### [`00aedd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md) → [`00aedd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd5c.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aedda0",
      "incomplete_value": true,
      "site": "00aedda0",
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
            "const:a28:8"
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
    "old": {
      "definition_site": "00aedd4c",
      "incomplete_value": true,
      "site": "00aedd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
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
      "00aedd70",
      "READ",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      "00aedd90",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedde4",
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aedd70",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ],
    [
      "00aedd90",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedde4",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedd58) · [`00aedda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedda0) · [`00aedd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedd2c)
- 新版 `00aedd9c`（命令位置の公開資料なし） · `00aedde4`（命令位置の公開資料なし） · `00aedd70`（命令位置の公開資料なし）

~~~diff
- 00aedd58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aedd58 ["INT_ADD", "register:40f0:8", ["const:aedd58:8", "const:4:8"]]
- 00aedd58 ["CALLIND", null, ["register:0:8"]]
+ 00aedd9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aedd9c ["INT_ADD", "register:40f0:8", ["const:aedd9c:8", "const:4:8"]]
+ 00aedd9c ["CALLIND", null, ["register:0:8"]]
- 00aedd58 bytes 00013fd6
+ 00aedd9c bytes 00013fd6
- 00aedda0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aedda0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a28:8"]]
- 00aedda0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aedde4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aedde4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a68:8"]]
+ 00aedde4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aedda0 bytes a0a22839
+ 00aedde4 bytes a0a22939
- 00aedd2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a28:8"]]
- 00aedd2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aedd2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aedd70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a68:8"]]
+ 00aedd70 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aedd70 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aedd2c bytes a8a26839
+ 00aedd70 bytes a8a26939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2a9ae4a2a45255a1c46828822685ccc"></a>

### [`00aeddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md) → [`00aeddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aeddf8.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aeddf0",
      "incomplete_value": true,
      "site": "00aeddf0",
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
            "const:a28:8"
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
    "old": {
      "definition_site": "00aede40",
      "incomplete_value": true,
      "site": "00aede40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
    "old": {
      "definition_site": "00aeddcc",
      "incomplete_value": true,
      "site": "00aeddcc",
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
      "00aede0c",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aede18",
      "READ",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      "00aede34",
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aede0c",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aede18",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ],
    [
      "00aede34",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aeddf0) · [`00aede3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aede3c) · [`00aede40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aede40)
- 新版 `00aede34`（命令位置の公開資料なし） · `00aede80`（命令位置の公開資料なし） · `00aede84`（命令位置の公開資料なし）

~~~diff
- 00aeddf0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeddf0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeddf0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a28:8"]]
- 00aeddf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aede34 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aede34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aede34 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a68:8"]]
+ 00aede34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeddf0 bytes bfa22839
+ 00aede34 bytes bfa22939
- 00aede3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aede3c ["INT_ADD", "register:40f0:8", ["const:aede3c:8", "const:4:8"]]
- 00aede3c ["CALLIND", null, ["register:0:8"]]
+ 00aede80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aede80 ["INT_ADD", "register:40f0:8", ["const:aede80:8", "const:4:8"]]
+ 00aede80 ["CALLIND", null, ["register:0:8"]]
- 00aede3c bytes 00013fd6
+ 00aede80 bytes 00013fd6
- 00aede40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aede40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aede40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aede84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00aede84 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aede84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aede40 bytes 9f1205f9
+ 00aede84 bytes 9f3205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4716e4ffd82f07f8ce4ada3d876a50"></a>

### [`00aede54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md) → [`00aede98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aede98.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aede94",
      "incomplete_value": true,
      "site": "00aede94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
    "old": {
      "definition_site": "00aede70",
      "incomplete_value": true,
      "site": "00aede70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aede78",
      "incomplete_value": false,
      "site": "00aede8c",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedeac",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedebc",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aeded8",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedeac",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedebc",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aeded8",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aede8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede8c) · [`00aede94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede94) · [`00aede68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede68)
- 新版 `00aeded0`（命令位置の公開資料なし） · `00aeded8`（命令位置の公開資料なし） · `00aedeac`（命令位置の公開資料なし）

~~~diff
- 00aede8c ["INT_ADD", "register:40f0:8", ["const:aede8c:8", "const:4:8"]]
- 00aede8c ["CALL", null, ["callee:00bde090:8"]]
+ 00aeded0 ["INT_ADD", "register:40f0:8", ["const:aeded0:8", "const:4:8"]]
+ 00aeded0 ["CALL", null, ["callee:00bde090:8"]]
- 00aede8c bytes 6dc00394
+ 00aeded0 bytes 70c00394
- 00aede94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aede94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeded8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00aeded8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aede94 bytes 801205f9
+ 00aeded8 bytes 803205f9
- 00aede68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aede68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedeac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00aedeac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aede68 bytes 811245f9
+ 00aedeac bytes 813245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98f84e53448277453bc711feacb475e3"></a>

### [`00aedec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md) → [`00aedf08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aedee0",
      "incomplete_value": false,
      "site": "00aedee4",
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
    "old": {
      "definition_site": "00aedef0",
      "incomplete_value": true,
      "site": "00aedefc",
      "value": [
        "LOAD",
        "8",
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
      "00aedf24",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aedf34",
      "DATA",
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
      "00aedf24",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aedf34",
      "DATA",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedee4) · [`00aedee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedee0) · [`00aedeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedeec)
- 新版 `00aedf28`（命令位置の公開資料なし） · `00aedf24`（命令位置の公開資料なし） · `00aedf30`（命令位置の公開資料なし）

~~~diff
- 00aedee4 ["INT_ADD", "register:40f0:8", ["const:aedee4:8", "const:4:8"]]
- 00aedee4 ["CALL", null, ["callee:00bde180:8"]]
+ 00aedf28 ["INT_ADD", "register:40f0:8", ["const:aedf28:8", "const:4:8"]]
+ 00aedf28 ["CALL", null, ["callee:00bde180:8"]]
- 00aedee4 bytes 93c00394
+ 00aedf28 bytes 96c00394
- 00aedee0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aedee0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedee0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedee0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedf24 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aedf24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedf24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedf24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedee0 bytes 00501791
+ 00aedf24 bytes 001c1591
- 00aedeec ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00aedeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aedeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aedeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedf30 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00aedf30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedf30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedf30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aedeec bytes 08c12891
+ 00aedf30 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1844f5a4d4ee7163cdb549ea62a3cf18"></a>

### [`00aedf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md) → [`00aedf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf44.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aedf40",
      "incomplete_value": true,
      "site": "00aedf40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
    "old": {
      "definition_site": "00aedf1c",
      "incomplete_value": true,
      "site": "00aedf1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedf24",
      "incomplete_value": false,
      "site": "00aedf38",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aedf58",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedf68",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedf84",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedf58",
      "READ",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedf68",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedf84",
      "WRITE",
      [
        "storage",
        "010a0a60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf38) · [`00aedf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf40) · [`00aedf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf14)
- 新版 `00aedf7c`（命令位置の公開資料なし） · `00aedf84`（命令位置の公開資料なし） · `00aedf58`（命令位置の公開資料なし）

~~~diff
- 00aedf38 ["INT_ADD", "register:40f0:8", ["const:aedf38:8", "const:4:8"]]
- 00aedf38 ["CALL", null, ["callee:00bde090:8"]]
+ 00aedf7c ["INT_ADD", "register:40f0:8", ["const:aedf7c:8", "const:4:8"]]
+ 00aedf7c ["CALL", null, ["callee:00bde090:8"]]
- 00aedf38 bytes 42c00394
+ 00aedf7c bytes 45c00394
- 00aedf40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aedf40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedf84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00aedf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedf40 bytes 801205f9
+ 00aedf84 bytes 803205f9
- 00aedf14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aedf14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedf58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00aedf58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedf14 bytes 811245f9
+ 00aedf58 bytes 813245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-635aad5bf821325ab941ae7e651f06ec"></a>

### [`00aedf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md) → [`00aedfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedfb4.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aedf8c",
      "incomplete_value": false,
      "site": "00aedf90",
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
    "old": {
      "definition_site": "00aedf9c",
      "incomplete_value": true,
      "site": "00aedfa8",
      "value": [
        "LOAD",
        "8",
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
      "00aedfd0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aedfe0",
      "DATA",
      [
        "storage",
        "010a0a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aedfd0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aedfe0",
      "DATA",
      [
        "storage",
        "010a0a80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf90) · [`00aedf8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf8c) · [`00aedf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf98)
- 新版 `00aedfd4`（命令位置の公開資料なし） · `00aedfd0`（命令位置の公開資料なし） · `00aedfdc`（命令位置の公開資料なし）

~~~diff
- 00aedf90 ["INT_ADD", "register:40f0:8", ["const:aedf90:8", "const:4:8"]]
- 00aedf90 ["CALL", null, ["callee:00bde180:8"]]
+ 00aedfd4 ["INT_ADD", "register:40f0:8", ["const:aedfd4:8", "const:4:8"]]
+ 00aedfd4 ["CALL", null, ["callee:00bde180:8"]]
- 00aedf90 bytes 68c00394
+ 00aedfd4 bytes 6bc00394
- 00aedf8c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aedf8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedf8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedf8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedfd0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aedfd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedfd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedfd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedf8c bytes 00fc1991
+ 00aedfd0 bytes 00c81791
- 00aedf98 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00aedf98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aedf98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aedf98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedfdc ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00aedfdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedfdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedfdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aedf98 bytes 08012991
+ 00aedfdc bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e3f07bd416bf04def6c7b531e0827c"></a>

### [`00aedfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md) → [`00aedff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
    "old": {
      "definition_site": "00aedfd8",
      "incomplete_value": true,
      "site": "00aedfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
    "old": {
      "definition_site": "00aedfc0",
      "incomplete_value": true,
      "site": "00aedfc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aedfcc",
      "incomplete_value": false,
      "site": "00aedfd0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee000",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee010",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee01c",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee000",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee010",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee01c",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfd0) · [`00aedfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfd8) · [`00aedfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfbc)
- 新版 `00aee014`（命令位置の公開資料なし） · `00aee01c`（命令位置の公開資料なし） · `00aee000`（命令位置の公開資料なし）

~~~diff
- 00aedfd0 ["INT_ADD", "register:40f0:8", ["const:aedfd0:8", "const:4:8"]]
- 00aedfd0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee014 ["INT_ADD", "register:40f0:8", ["const:aee014:8", "const:4:8"]]
+ 00aee014 ["CALL", null, ["callee:00bde090:8"]]
- 00aedfd0 bytes 1cc00394
+ 00aee014 bytes 1fc00394
- 00aedfd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee01c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedfd8 bytes 602605f9
+ 00aee01c bytes 604605f9
- 00aedfbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedfbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee000 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee000 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedfbc bytes 682645f9
+ 00aee000 bytes 684645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7fa74bbd0cd3085976280229c4f5c5"></a>

### [`00aedfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md) → [`00aee030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aee018",
      "incomplete_value": true,
      "site": "00aee018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee000",
      "incomplete_value": true,
      "site": "00aee000",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee008",
      "incomplete_value": false,
      "site": "00aee010",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee040",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee04c",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee05c",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee040",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee04c",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee05c",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aee010) · [`00aee018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aee018) · [`00aedffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aedffc)
- 新版 `00aee054`（命令位置の公開資料なし） · `00aee05c`（命令位置の公開資料なし） · `00aee040`（命令位置の公開資料なし）

~~~diff
- 00aee010 ["INT_ADD", "register:40f0:8", ["const:aee010:8", "const:4:8"]]
- 00aee010 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee054 ["INT_ADD", "register:40f0:8", ["const:aee054:8", "const:4:8"]]
+ 00aee054 ["CALL", null, ["callee:00bde090:8"]]
- 00aee010 bytes 0cc00394
+ 00aee054 bytes 0fc00394
- 00aee018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aee018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee018 bytes 602605f9
+ 00aee05c bytes 604605f9
- 00aedffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedffc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee040 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedffc bytes 682645f9
+ 00aee040 bytes 684645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce23083932ea44e1c0f9337e150e81ab"></a>

### [`00aee02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md) → [`00aee070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee070.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee040",
      "incomplete_value": true,
      "site": "00aee040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee080",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee090",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee0a0",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee080",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee090",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee0a0",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee054) · [`00aee05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee05c) · [`00aee03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee03c)
- 新版 `00aee098`（命令位置の公開資料なし） · `00aee0a0`（命令位置の公開資料なし） · `00aee080`（命令位置の公開資料なし）

~~~diff
- 00aee054 ["INT_ADD", "register:40f0:8", ["const:aee054:8", "const:4:8"]]
- 00aee054 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee098 ["INT_ADD", "register:40f0:8", ["const:aee098:8", "const:4:8"]]
+ 00aee098 ["CALL", null, ["callee:00bde090:8"]]
- 00aee054 bytes fbbf0394
+ 00aee098 bytes febf0394
- 00aee05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aee05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee05c bytes 602605f9
+ 00aee0a0 bytes 604605f9
- 00aee03c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aee03c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee03c bytes 682645f9
+ 00aee080 bytes 684645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b3c64ebc235bb8518d04c9e4432861"></a>

### [`00aee070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md) → [`00aee0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee0b4.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

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
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee08c",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee0c4",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee0d0",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee0e4",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee0c4",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee0d0",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee0e4",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee098) · [`00aee0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee0a0) · [`00aee080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee080)
- 新版 `00aee0dc`（命令位置の公開資料なし） · `00aee0e4`（命令位置の公開資料なし） · `00aee0c4`（命令位置の公開資料なし）

~~~diff
- 00aee098 ["INT_ADD", "register:40f0:8", ["const:aee098:8", "const:4:8"]]
- 00aee098 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee0dc ["INT_ADD", "register:40f0:8", ["const:aee0dc:8", "const:4:8"]]
+ 00aee0dc ["CALL", null, ["callee:00bde090:8"]]
- 00aee098 bytes eabf0394
+ 00aee0dc bytes edbf0394
- 00aee0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aee0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee0a0 bytes 602605f9
+ 00aee0e4 bytes 604605f9
- 00aee080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aee080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00aee0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee080 bytes 682645f9
+ 00aee0c4 bytes 684645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa97a08ebcaf6021062175fe57767ac6"></a>

### [`00aee0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md) → [`00aee104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md) _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aee148",
      "incomplete_value": true,
      "site": "00aee148",
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
            "const:a50:8"
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
    "old": {
      "definition_site": "00aee0f4",
      "incomplete_value": true,
      "site": "00aee100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
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
      "00aee118",
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee138",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee18c",
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aee118",
      "READ",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee138",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee18c",
      "WRITE",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee100) · [`00aee148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee148) · [`00aee0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee0d4)
- 新版 `00aee144`（命令位置の公開資料なし） · `00aee18c`（命令位置の公開資料なし） · `00aee118`（命令位置の公開資料なし）

~~~diff
- 00aee100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee100 ["INT_ADD", "register:40f0:8", ["const:aee100:8", "const:4:8"]]
- 00aee100 ["CALLIND", null, ["register:0:8"]]
+ 00aee144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee144 ["INT_ADD", "register:40f0:8", ["const:aee144:8", "const:4:8"]]
+ 00aee144 ["CALLIND", null, ["register:0:8"]]
- 00aee100 bytes 00013fd6
+ 00aee144 bytes 00013fd6
- 00aee148 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aee148 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a50:8"]]
- 00aee148 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aee18c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aee18c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a90:8"]]
+ 00aee18c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aee148 bytes a0422939
+ 00aee18c bytes a0422a39
- 00aee0d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
- 00aee0d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aee0d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aee118 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a90:8"]]
+ 00aee118 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aee118 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aee0d4 bytes a8426939
+ 00aee118 bytes a8426a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4565e13637e05d42ae207bc3495a1364"></a>

### [`00aee15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md) → [`00aee1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee1a0.md) _ZN8firebase4util6object12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aee198",
      "incomplete_value": true,
      "site": "00aee198",
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
            "const:a50:8"
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
    "old": {
      "definition_site": "00aee1e8",
      "incomplete_value": true,
      "site": "00aee1e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee174",
      "incomplete_value": true,
      "site": "00aee174",
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
      "00aee1b4",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee1c0",
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee1dc",
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aee1b4",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee1c0",
      "READ",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee1dc",
      "WRITE",
      [
        "storage",
        "010a0a90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee198) · [`00aee1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee1e4) · [`00aee1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee1e8)
- 新版 `00aee1dc`（命令位置の公開資料なし） · `00aee228`（命令位置の公開資料なし） · `00aee22c`（命令位置の公開資料なし）

~~~diff
- 00aee198 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee198 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee198 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a50:8"]]
- 00aee198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aee1dc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aee1dc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aee1dc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a90:8"]]
+ 00aee1dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee198 bytes bf422939
+ 00aee1dc bytes bf422a39
- 00aee1e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee1e4 ["INT_ADD", "register:40f0:8", ["const:aee1e4:8", "const:4:8"]]
- 00aee1e4 ["CALLIND", null, ["register:0:8"]]
+ 00aee228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee228 ["INT_ADD", "register:40f0:8", ["const:aee228:8", "const:4:8"]]
+ 00aee228 ["CALLIND", null, ["register:0:8"]]
- 00aee1e4 bytes 00013fd6
+ 00aee228 bytes 00013fd6
- 00aee1e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee1e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee1e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aee22c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
+ 00aee22c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aee22c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee1e8 bytes 9f2605f9
+ 00aee22c bytes 9f4605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80481a15140f1919ecdd24b0913d0cd2"></a>

### [`00aee1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md) → [`00aee240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee240.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aee23c",
      "incomplete_value": true,
      "site": "00aee23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee218",
      "incomplete_value": true,
      "site": "00aee218",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee220",
      "incomplete_value": false,
      "site": "00aee234",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee254",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee264",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee280",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee254",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee264",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee280",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee234) · [`00aee23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee23c) · [`00aee210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee210)
- 新版 `00aee278`（命令位置の公開資料なし） · `00aee280`（命令位置の公開資料なし） · `00aee254`（命令位置の公開資料なし）

~~~diff
- 00aee234 ["INT_ADD", "register:40f0:8", ["const:aee234:8", "const:4:8"]]
- 00aee234 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee278 ["INT_ADD", "register:40f0:8", ["const:aee278:8", "const:4:8"]]
+ 00aee278 ["CALL", null, ["callee:00bde090:8"]]
- 00aee234 bytes 83bf0394
+ 00aee278 bytes 86bf0394
- 00aee23c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee23c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
+ 00aee280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee23c bytes 802605f9
+ 00aee280 bytes 804605f9
- 00aee210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee210 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee254 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
+ 00aee254 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee210 bytes 812645f9
+ 00aee254 bytes 814645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bfc3e56f749570f51050de86c0571e1"></a>

### [`00aee26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md) → [`00aee2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2b0.md) _ZN8firebase4util6object11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aee288",
      "incomplete_value": false,
      "site": "00aee28c",
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
    "old": {
      "definition_site": "00aee298",
      "incomplete_value": true,
      "site": "00aee2a4",
      "value": [
        "LOAD",
        "8",
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
      "00aee2cc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aee2dc",
      "DATA",
      [
        "storage",
        "010a0a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee2cc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aee2dc",
      "DATA",
      [
        "storage",
        "010a0a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee28c) · [`00aee288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee288) · [`00aee294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee294)
- 新版 `00aee2d0`（命令位置の公開資料なし） · `00aee2cc`（命令位置の公開資料なし） · `00aee2d8`（命令位置の公開資料なし）

~~~diff
- 00aee28c ["INT_ADD", "register:40f0:8", ["const:aee28c:8", "const:4:8"]]
- 00aee28c ["CALL", null, ["callee:00bde180:8"]]
+ 00aee2d0 ["INT_ADD", "register:40f0:8", ["const:aee2d0:8", "const:4:8"]]
+ 00aee2d0 ["CALL", null, ["callee:00bde180:8"]]
- 00aee28c bytes a9bf0394
+ 00aee2d0 bytes acbf0394
- 00aee288 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aee288 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aee288 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aee288 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aee2cc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aee2cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee2cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee2cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aee288 bytes 00501791
+ 00aee2cc bytes 001c1591
- 00aee294 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00aee294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee2d8 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00aee2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee294 bytes 08612991
+ 00aee2d8 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-453c9c84ff586cddf503c2d38c79c188"></a>

### [`00aee2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md) → [`00aee2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee2ec.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aee2e8",
      "incomplete_value": true,
      "site": "00aee2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
    "old": {
      "definition_site": "00aee2c4",
      "incomplete_value": true,
      "site": "00aee2c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aee2cc",
      "incomplete_value": false,
      "site": "00aee2e0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee300",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee310",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee32c",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee300",
      "READ",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee310",
      "PARAM",
      [
        "storage",
        "0029ddf7",
        null,
        "string"
      ]
    ],
    [
      "00aee32c",
      "WRITE",
      [
        "storage",
        "010a0a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2e0) · [`00aee2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2e8) · [`00aee2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2bc)
- 新版 `00aee324`（命令位置の公開資料なし） · `00aee32c`（命令位置の公開資料なし） · `00aee300`（命令位置の公開資料なし）

~~~diff
- 00aee2e0 ["INT_ADD", "register:40f0:8", ["const:aee2e0:8", "const:4:8"]]
- 00aee2e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aee324 ["INT_ADD", "register:40f0:8", ["const:aee324:8", "const:4:8"]]
+ 00aee324 ["CALL", null, ["callee:00bde090:8"]]
- 00aee2e0 bytes 58bf0394
+ 00aee324 bytes 5bbf0394
- 00aee2e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee32c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
+ 00aee32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee2e8 bytes 802605f9
+ 00aee32c bytes 804605f9
- 00aee2bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee2bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a88:8"]]
+ 00aee300 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee2bc bytes 812645f9
+ 00aee300 bytes 814645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db49dbb47c82ea7248058e80e454975"></a>

### [`00aee318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md) → [`00aee35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee35c.md) _ZN8firebase4util6object10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aee378",
      "incomplete_value": false,
      "site": "00aee37c",
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
      "definition_site": "00aee334",
      "incomplete_value": false,
      "site": "00aee338",
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
      "definition_site": "00aee388",
      "incomplete_value": true,
      "site": "00aee394",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aee344",
      "incomplete_value": true,
      "site": "00aee350",
      "value": [
        "LOAD",
        "8",
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
      "00aee378",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aee388",
      "DATA",
      [
        "storage",
        "010a0a60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aee378",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aee388",
      "DATA",
      [
        "storage",
        "010a0aa0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee338) · [`00aee334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee334) · [`00aee340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee340)
- 新版 `00aee37c`（命令位置の公開資料なし） · `00aee378`（命令位置の公開資料なし） · `00aee384`（命令位置の公開資料なし）

~~~diff
- 00aee338 ["INT_ADD", "register:40f0:8", ["const:aee338:8", "const:4:8"]]
- 00aee338 ["CALL", null, ["callee:00bde180:8"]]
+ 00aee37c ["INT_ADD", "register:40f0:8", ["const:aee37c:8", "const:4:8"]]
+ 00aee37c ["CALL", null, ["callee:00bde180:8"]]
- 00aee338 bytes 7ebf0394
+ 00aee37c bytes 81bf0394
- 00aee334 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aee334 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aee334 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aee334 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aee378 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aee378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aee334 bytes 00fc1991
+ 00aee378 bytes 00c81791
- 00aee340 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00aee340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee384 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00aee384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee340 bytes 08812991
+ 00aee384 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a989e247ca01ecef547c20f9fd7a38d"></a>

### [`00aee354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) → [`00aee398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde620.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00aee8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bde670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde670.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00aee908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 8件, `store_condition` 2件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee3c4",
      "incomplete_value": false,
      "site": "00aee3c4",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee380",
      "incomplete_value": false,
      "site": "00aee380",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee408",
      "incomplete_value": true,
      "site": "00aee408",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee3c4",
      "incomplete_value": true,
      "site": "00aee3c4",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee460",
      "incomplete_value": true,
      "site": "00aee460",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee41c",
      "incomplete_value": true,
      "site": "00aee41c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee3b8",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee3c4",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee3dc",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee3b8",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee3c4",
      "WRITE",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee3dc",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee380) · [`00aee3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee3c4) · [`00aee3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee3d8)
- 新版 `00aee3c4`（命令位置の公開資料なし） · `00aee408`（命令位置の公開資料なし） · `00aee41c`（命令位置の公開資料なし）

~~~diff
- 00aee380 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:a68:8"]]
- 00aee380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee3c4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:aa8:8"]]
+ 00aee3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee380 bytes e86a0ab9
+ 00aee3c4 bytes e8aa0ab9
- 00aee3c4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:4c8:8"]]
- 00aee3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee408 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:508:8"]]
+ 00aee408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee3c4 bytes c06602f9
+ 00aee408 bytes c08602f9
- 00aee3d8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00aee3d8 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00aee3d8 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00aee3d8 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00aee41c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00aee41c ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00aee41c ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00aee41c ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00aee3d8 bytes 84601391
+ 00aee41c bytes 84601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67643e3c9455093cab9a77f22e3d00b8"></a>

### [`00aee714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md) → [`00aee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee758.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde610.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde660.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.96% / 新版 87.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aee748",
      "incomplete_value": true,
      "site": "00aee748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
    "old": {
      "definition_site": "00aee778",
      "incomplete_value": true,
      "site": "00aee778",
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
            "const:4d0:8"
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
    "old": {
      "definition_site": "00aee7c8",
      "incomplete_value": true,
      "site": "00aee7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "00aee76c",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee784",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee78c",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00aee76c",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee784",
      "READ",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee78c",
      "WRITE",
      [
        "storage",
        "010a0aa8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee748) · [`00aee778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee778) · [`00aee7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee7b0)
- 新版 `00aee78c`（命令位置の公開資料なし） · `00aee7bc`（命令位置の公開資料なし） · `00aee7f4`（命令位置の公開資料なし）

~~~diff
- 00aee748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00aee748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee78c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00aee78c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee748 bytes 886a0ab9
+ 00aee78c bytes 88aa0ab9
- 00aee778 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee778 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee778 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d0:8"]]
- 00aee778 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aee7bc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aee7bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aee7bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
+ 00aee7bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee778 bytes bf421339
+ 00aee7bc bytes bf421439
- 00aee7b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee7b0 ["INT_ADD", "register:40f0:8", ["const:aee7b0:8", "const:4:8"]]
- 00aee7b0 ["CALLIND", null, ["register:0:8"]]
+ 00aee7f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee7f4 ["INT_ADD", "register:40f0:8", ["const:aee7f4:8", "const:4:8"]]
+ 00aee7f4 ["CALLIND", null, ["register:0:8"]]
- 00aee7b0 bytes 00013fd6
+ 00aee7f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c13e739db5b228944e3dd950e9d1e8b"></a>

### [`00aee8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) → [`00aee908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee908.md) FUN_00aee908

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aee354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00aee398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee398.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aee940",
      "incomplete_value": true,
      "site": "00aee940",
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
            "const:a70:8"
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
    "old": {
      "definition_site": "00aee8e8",
      "incomplete_value": true,
      "site": "00aee8ec",
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
    "old": {
      "definition_site": "00aee914",
      "incomplete_value": true,
      "site": "00aee914",
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
      "00aee91c",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee94c",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee984",
      "WRITE",
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
      "00aee91c",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee94c",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee984",
      "WRITE",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee940) · [`00aee8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee8d8) · [`00aee904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee904)
- 新版 `00aee984`（命令位置の公開資料なし） · `00aee91c`（命令位置の公開資料なし） · `00aee948`（命令位置の公開資料なし）

~~~diff
- 00aee940 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
- 00aee940 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aee984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
+ 00aee984 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aee984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee940 bytes bf3a05f9
+ 00aee984 bytes bf5a05f9
- 00aee8d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
- 00aee8d8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee91c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
+ 00aee91c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee8d8 bytes b33a45f9
+ 00aee91c bytes b35a45f9
- 00aee904 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee904 ["INT_ADD", "register:40f0:8", ["const:aee904:8", "const:4:8"]]
- 00aee904 ["CALLIND", null, ["register:0:8"]]
+ 00aee948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee948 ["INT_ADD", "register:40f0:8", ["const:aee948:8", "const:4:8"]]
+ 00aee948 ["CALLIND", null, ["register:0:8"]]
- 00aee904 bytes 00013fd6
+ 00aee948 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a054e8731fbb46ac7a42f1cb3c3b800"></a>

### [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) → [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md) · 呼出先 13件 [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md) · 呼出先 13件 [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.21% / 新版 82.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 132件, `store_destination` 46件

アドレスに依存する影響 `branch_value` 37件, `store_condition` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeea10",
      "incomplete_value": true,
      "site": "00aeea10",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee9cc",
      "incomplete_value": true,
      "site": "00aee9cc",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeea68",
      "incomplete_value": true,
      "site": "00aeea68",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeea24",
      "incomplete_value": true,
      "site": "00aeea24",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee9bc",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9c8",
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9e8",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee9bc",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9c8",
      "WRITE",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9e8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md#insn-00aee984) · [`00aee9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md#insn-00aee9cc) · [`00aee9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md#insn-00aee9e0)
- 新版 `00aee9c8`（命令位置の公開資料なし） · `00aeea10`（命令位置の公開資料なし） · `00aeea24`（命令位置の公開資料なし）

~~~diff
- 00aee984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00aee984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee9c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 00aee9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee984 bytes a87a0ab9
+ 00aee9c8 bytes a8ba0ab9
- 00aee9cc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:530:8"]]
- 00aee9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeea10 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:570:8"]]
+ 00aeea10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee9cc bytes c09a02f9
+ 00aeea10 bytes c0ba02f9
- 00aee9e0 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00aee9e0 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00aee9e0 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00aee9e0 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00aeea24 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00aeea24 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00aeea24 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00aeea24 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00aee9e0 bytes 84001591
+ 00aeea24 bytes 84001691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f12db314ca1c9d0e55537ae3f275327"></a>

### [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) → [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) FUN_00aefa14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) · 呼出先 1件 [`00bde4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4b0.md)
- 新版 呼出元 2件 [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) · 呼出先 1件 [`00bde500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde500.md)

変更の種類 branch_value, call, call_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 7.67% / 新版 7.67%

CFGの説明率　旧版 5.36% / 新版 5.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 101件, `unresolved_call_alignment` 175件, `unresolved_store_alignment` 71件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aefa28",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00aefa30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aefa60"
      ]
    ],
    [
      "00aefa38",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aefa28",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aefa30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aefaa4"
      ]
    ],
    [
      "00aefa38",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefa0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md#insn-00aefa0c) · [`00aefa5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md#insn-00aefa5c)
- 新版 `00aefa5c`（命令位置の公開資料なし）

~~~diff
- 00aefa0c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aefa0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aefa0c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:568:8"]]
- 00aefa0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aefa0c bytes bfa21539
- 00aefa5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00aefa5c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aefa5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aefa5c bytes 9fb202f9
+ 00aefa5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:720:8"]]
+ 00aefa5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aefa5c bytes 089143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38751bdf1ee459adae23b573983ee645"></a>

### [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) → [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) _ZN8firebase4util9TerminateEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) · 呼出先 10件 [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)
- 新版 呼出元 2件 [`00aee990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee990.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) · 呼出先 10件 [`00aefa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aef/00aefa14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00af0c28",
      "incomplete_value": true,
      "site": "00af0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
    "old": {
      "definition_site": "00af0c8c",
      "incomplete_value": true,
      "site": "00af0c8c",
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
            "const:a80:8"
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
    "old": {
      "definition_site": "00af0c48",
      "incomplete_value": true,
      "site": "00af0c48",
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
      "00af0c4c",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c64",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c6c",
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00af0c4c",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c64",
      "READ",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c6c",
      "WRITE",
      [
        "storage",
        "010a0ab8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c1c) · [`00af0c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c28) · [`00af0c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c60)
- 新版 `00af0c60`（命令位置の公開資料なし） · `00af0c6c`（命令位置の公開資料なし） · `00af0ca4`（命令位置の公開資料なし）

~~~diff
- 00af0c1c ["INT_ADD", "register:40f0:8", ["const:af0c1c:8", "const:4:8"]]
- 00af0c1c ["CALL", null, ["callee:00bde180:8"]]
+ 00af0c60 ["INT_ADD", "register:40f0:8", ["const:af0c60:8", "const:4:8"]]
+ 00af0c60 ["CALL", null, ["callee:00bde180:8"]]
- 00af0c1c bytes 45b50394
+ 00af0c60 bytes 48b50394
- 00af0c28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a78:8"]]
- 00af0c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00af0c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
+ 00af0c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00af0c28 bytes 887a0ab9
+ 00af0c6c bytes 88ba0ab9
- 00af0c60 ["INT_ADD", "register:40f0:8", ["const:af0c60:8", "const:4:8"]]
- 00af0c60 ["CALL", null, ["callee:00bde820:8"]]
+ 00af0ca4 ["INT_ADD", "register:40f0:8", ["const:af0ca4:8", "const:4:8"]]
+ 00af0ca4 ["CALL", null, ["callee:00bde820:8"]]
- 00af0c60 bytes dcb60394
+ 00af0ca4 bytes dfb60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f350e07e0c0e89183f9c8942725e725c"></a>

### [`00af0d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md) → [`00af0d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0d50.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4d0.md) · 呼出先 6件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)
- 新版 呼出元 1件 [`00bde520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde520.md) · 呼出先 6件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af0d74",
      "incomplete_value": true,
      "site": "00af0d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0d30",
      "incomplete_value": true,
      "site": "00af0d38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af0dd4",
      "incomplete_value": false,
      "site": "00af0dd8",
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
            "const:d66:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0d90",
      "incomplete_value": false,
      "site": "00af0d94",
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
            "const:cdb:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af0df4",
      "incomplete_value": true,
      "site": "00af0e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0db0",
      "incomplete_value": true,
      "site": "00af0dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af0d74",
      "READ",
      [
        "storage",
        "010a04e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af0dd4",
      "PARAM",
      [
        "storage",
        "002a2cdb",
        null,
        "string"
      ]
    ],
    [
      "00af0df4",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af0d74",
      "READ",
      [
        "storage",
        "010a0520",
        null,
        "undefined8"
      ]
    ],
    [
      "00af0dd4",
      "PARAM",
      [
        "storage",
        "002a2d66",
        null,
        "string"
      ]
    ],
    [
      "00af0df4",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md#insn-00af0d38) · [`00af0d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md#insn-00af0d94) · [`00af0dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md#insn-00af0dcc)
- 新版 `00af0d7c`（命令位置の公開資料なし） · `00af0dd8`（命令位置の公開資料なし） · `00af0e10`（命令位置の公開資料なし）

~~~diff
- 00af0d38 ["INT_ADD", "register:40f0:8", ["const:af0d38:8", "const:4:8"]]
- 00af0d38 ["CALL", null, ["callee:0047495c:8"]]
+ 00af0d7c ["INT_ADD", "register:40f0:8", ["const:af0d7c:8", "const:4:8"]]
+ 00af0d7c ["CALL", null, ["callee:0047495c:8"]]
- 00af0d38 bytes 090fe697
+ 00af0d7c bytes f80ee697
- 00af0d94 ["INT_ADD", "register:40f0:8", ["const:af0d94:8", "const:4:8"]]
- 00af0d94 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00af0dd8 ["INT_ADD", "register:40f0:8", ["const:af0dd8:8", "const:4:8"]]
+ 00af0dd8 ["CALL", null, ["callee:00bde2b0:8"]]
- 00af0d94 bytes 33b50394
+ 00af0dd8 bytes 36b50394
- 00af0dcc ["INT_ADD", "register:40f0:8", ["const:af0dcc:8", "const:4:8"]]
- 00af0dcc ["CALL", null, ["callee:0056681c:8"]]
+ 00af0e10 ["INT_ADD", "register:40f0:8", ["const:af0e10:8", "const:4:8"]]
+ 00af0e10 ["CALL", null, ["callee:0056681c:8"]]
- 00af0dcc bytes 94d6e997
+ 00af0e10 bytes 83d6e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ddfb2e3f7e1e1659fa1e7ff7b1e1f1"></a>

### [`00af11ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af11ac.md) → [`00af11f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af11f0.md) _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde480.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 1件 [`00bde4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4d0.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.17% / 新版 88.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af123c",
      "incomplete_value": true,
      "site": "00af123c",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af11f8",
      "incomplete_value": true,
      "site": "00af11f8",
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
            "const:378:8"
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
    "old": {
      "definition_site": "00af1298",
      "incomplete_value": true,
      "site": "00af1298",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af1328",
      "incomplete_value": true,
      "site": "00af1328",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af12e4",
      "incomplete_value": true,
      "site": "00af12e4",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af120c",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af123c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1250",
      "PARAM",
      [
        "storage",
        "00c0fc60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00af120c",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af123c",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1250",
      "PARAM",
      [
        "storage",
        "00c0fcb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af11f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af11ac.md#insn-00af11f8) · [`00af120c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af11ac.md#insn-00af120c) · [`00af1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af11ac.md#insn-00af1220)
- 新版 `00af123c`（命令位置の公開資料なし） · `00af1250`（命令位置の公開資料なし） · `00af1264`（命令位置の公開資料なし）

~~~diff
- 00af11f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:378:8"]]
- 00af11f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00af123c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3b8:8"]]
+ 00af123c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00af11f8 bytes c0be01f9
+ 00af123c bytes c0de01f9
- 00af120c ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00af120c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00af120c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00af120c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00af1250 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00af1250 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00af1250 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00af1250 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00af120c bytes 42803191
+ 00af1250 bytes 42c03291
- 00af1220 ["INT_ADD", "register:40f0:8", ["const:af1220:8", "const:4:8"]]
- 00af1220 ["CALL", null, ["callee:00bde0b0:8"]]
+ 00af1264 ["INT_ADD", "register:40f0:8", ["const:af1264:8", "const:4:8"]]
+ 00af1264 ["CALL", null, ["callee:00bde0b0:8"]]
- 00af1220 bytes 90b30394
+ 00af1264 bytes 93b30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25ecfaa380b651af032ba66e7d647664"></a>

### [`00af1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md) → [`00af1364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md) _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bde730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bde780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af14a4",
      "incomplete_value": true,
      "site": "00af14b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:368:8"
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
      "00af13cc",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ],
    [
      "00af13d4",
      "READ",
      [
        "storage",
        "010a0a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1430",
      "READ",
      [
        "storage",
        "010a0a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af13cc",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ],
    [
      "00af13d4",
      "READ",
      [
        "storage",
        "010a0ac0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1430",
      "READ",
      [
        "storage",
        "010a0ac0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md#insn-00af14b0) · [`00af135c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md#insn-00af135c) · [`00af1364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md#insn-00af1364)
- 新版 `00af14f4`（命令位置の公開資料なし） · `00af13a0`（命令位置の公開資料なし） · `00af13a8`（命令位置の公開資料なし）

~~~diff
- 00af14b0 ["INT_ADD", "register:40f0:8", ["const:af14b0:8", "const:4:8"]]
- 00af14b0 ["CALL", null, ["callee:00551e14:8"]]
+ 00af14f4 ["INT_ADD", "register:40f0:8", ["const:af14f4:8", "const:4:8"]]
+ 00af14f4 ["CALL", null, ["callee:00551e14:8"]]
- 00af14b0 bytes 5982e997
+ 00af14f4 bytes 4882e997
- 00af135c ["INT_ADD", "register:40f0:8", ["const:af135c:8", "const:4:8"]]
- 00af135c ["CALL", null, ["callee:00bde2b0:8"]]
+ 00af13a0 ["INT_ADD", "register:40f0:8", ["const:af13a0:8", "const:4:8"]]
+ 00af13a0 ["CALL", null, ["callee:00bde2b0:8"]]
- 00af135c bytes c1b30394
+ 00af13a0 bytes c4b30394
- 00af1364 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00af1364 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00af1364 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00af1364 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00af13a8 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00af13a8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00af13a8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00af13a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00af1364 bytes b5222a91
+ 00af13a8 bytes b5222b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94317aaa14a6611e3f846070b2357820"></a>

### [`00af1648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md) → [`00af168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af168c.md) _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde550.md) · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)
- 新版 呼出元 1件 [`00bde5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5a0.md) · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)

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
    "old": {
      "definition_site": "00af166c",
      "incomplete_value": true,
      "site": "00af1678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
    "old": {
      "definition_site": "00af1670",
      "incomplete_value": true,
      "site": "00af1678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af16b0",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af16b4",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af16d0",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af16b0",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00af16b4",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00af16d0",
      "READ",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af1678) · [`00af1664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af1664) · [`00af166c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af166c)
- 新版 `00af16bc`（命令位置の公開資料なし） · `00af16a8`（命令位置の公開資料なし） · `00af16b0`（命令位置の公開資料なし）

~~~diff
- 00af1678 ["INT_ADD", "register:40f0:8", ["const:af1678:8", "const:4:8"]]
- 00af1678 ["CALL", null, ["callee:0056681c:8"]]
+ 00af16bc ["INT_ADD", "register:40f0:8", ["const:af16bc:8", "const:4:8"]]
+ 00af16bc ["CALL", null, ["callee:0056681c:8"]]
- 00af1678 bytes 69d4e997
+ 00af16bc bytes 58d4e997
- 00af1664 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00af1664 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00af1664 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00af1664 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00af16a8 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00af16a8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af16a8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af16a8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00af1664 bytes d6021591
+ 00af16a8 bytes d6021691
- 00af166c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 00af166c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af16b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00af16b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af166c bytes 019942f9
+ 00af16b0 bytes 01b942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563f9b5d83f69e68d9efee97c83882a7"></a>

### [`00af1750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md) → [`00af1794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1794.md) _ZN8firebase4util25StdUnorderedSetToJavaListEP7_JNIEnvRKNSt6__ndk113unordered_setINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af1774",
      "incomplete_value": true,
      "site": "00af1780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
    "old": {
      "definition_site": "00af1778",
      "incomplete_value": true,
      "site": "00af1780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af17b8",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af17bc",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af17d4",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af17b8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00af17bc",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00af17d4",
      "READ",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md#insn-00af1780) · [`00af176c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md#insn-00af176c) · [`00af1774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md#insn-00af1774)
- 新版 `00af17c4`（命令位置の公開資料なし） · `00af17b0`（命令位置の公開資料なし） · `00af17b8`（命令位置の公開資料なし）

~~~diff
- 00af1780 ["INT_ADD", "register:40f0:8", ["const:af1780:8", "const:4:8"]]
- 00af1780 ["CALL", null, ["callee:0056681c:8"]]
+ 00af17c4 ["INT_ADD", "register:40f0:8", ["const:af17c4:8", "const:4:8"]]
+ 00af17c4 ["CALL", null, ["callee:0056681c:8"]]
- 00af1780 bytes 27d4e997
+ 00af17c4 bytes 16d4e997
- 00af176c ["COPY", "tmp:0:8", ["const:540:8"]]
- 00af176c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00af176c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00af176c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00af17b0 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00af17b0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00af17b0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00af17b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00af176c bytes b5021591
+ 00af17b0 bytes b5021691
- 00af1774 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 00af1774 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af17b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00af17b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af1774 bytes 019942f9
+ 00af17b8 bytes 01b942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245e03b3f79228969b666c9406aaaedc"></a>

### [`00af19bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af19bc.md) → [`00af1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1a00.md) _ZN8firebase4util19VariantToJavaObjectEP7_JNIEnvRKNS_7VariantE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde570.md) · 呼出先 7件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) [`00bddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde560.md)
- 新版 呼出元 1件 [`00bde5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5c0.md) · 呼出先 7件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) [`00bddcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcd0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1c0c",
      "incomplete_value": false,
      "site": "00af1c10",
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
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af1bc8",
      "incomplete_value": false,
      "site": "00af1bcc",
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
            "const:614:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1a30",
      "DATA",
      [
        "storage",
        "002f5a4a",
        "switchD_00af19f8::switchdataD_002f5a4a",
        "byte"
      ]
    ],
    [
      "00af1a84",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1a88",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af1a30",
      "DATA",
      [
        "storage",
        "002f5a4a",
        "switchD_00af1a3c::switchdataD_002f5a4a",
        "byte"
      ]
    ],
    [
      "00af1a84",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1a88",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af19bc.md#insn-00af1bcc) · [`00af19e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af19bc.md#insn-00af19e8) · [`00af1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af19bc.md#insn-00af1a00)
- 新版 `00af1c10`（命令位置の公開資料なし） · `00af1a2c`（命令位置の公開資料なし） · `00af1a44`（命令位置の公開資料なし）

~~~diff
- 00af1bcc ["INT_ADD", "register:40f0:8", ["const:af1bcc:8", "const:4:8"]]
- 00af1bcc ["CALL", null, ["callee:00bddf60:8"]]
+ 00af1c10 ["INT_ADD", "register:40f0:8", ["const:af1c10:8", "const:4:8"]]
+ 00af1c10 ["CALL", null, ["callee:00bddf60:8"]]
- 00af1bcc bytes d1b00394
+ 00af1c10 bytes d4b00394
- 00af19e8 ["COPY", "register:4050:8", ["const:af19fc:8"]]
+ 00af1a2c ["COPY", "register:4050:8", ["const:af1a40:8"]]
- 00af19e8 bytes aa000010
+ 00af1a2c bytes aa000010
- 00af1a00 ["INT_ADD", "register:40f0:8", ["const:af1a00:8", "const:4:8"]]
- 00af1a00 ["CALL", null, ["callee:00bddcd0:8"]]
+ 00af1a44 ["INT_ADD", "register:40f0:8", ["const:af1a44:8", "const:4:8"]]
+ 00af1a44 ["CALL", null, ["callee:00bddcd0:8"]]
- 00af1a00 bytes a0b00394
+ 00af1a44 bytes a3b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d8c6ad0f593d150ef33606cfacd44e8"></a>

### [`00af1ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1ee8.md) → [`00af1f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1f2c.md) _ZN8firebase4util15JavaMapToStdMapEP7_JNIEnvPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4lessISA_EEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.34% / 新版 99.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af1f28",
      "incomplete_value": true,
      "site": "00af1f30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1fb8",
      "incomplete_value": true,
      "site": "00af1fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af1f74",
      "incomplete_value": true,
      "site": "00af1f80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2008",
      "incomplete_value": true,
      "site": "00af2018",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af1fc4",
      "incomplete_value": true,
      "site": "00af1fd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
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
      "00af1f6c",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1fb8",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2008",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af1f6c",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1fb8",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2008",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1ee8.md#insn-00af1f30) · [`00af1f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1ee8.md#insn-00af1f74) · [`00af1f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1ee8.md#insn-00af1f80)
- 新版 `00af1f74`（命令位置の公開資料なし） · `00af1fb8`（命令位置の公開資料なし） · `00af1fc4`（命令位置の公開資料なし）

~~~diff
- 00af1f30 ["INT_ADD", "register:40f0:8", ["const:af1f30:8", "const:4:8"]]
- 00af1f30 ["CALL", null, ["callee:0047495c:8"]]
+ 00af1f74 ["INT_ADD", "register:40f0:8", ["const:af1f74:8", "const:4:8"]]
+ 00af1f74 ["CALL", null, ["callee:0047495c:8"]]
- 00af1f30 bytes 8b0ae697
+ 00af1f74 bytes 7a0ae697
- 00af1f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
- 00af1f74 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af1fb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
+ 00af1fb8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af1f74 bytes 02cd44f9
+ 00af1fb8 bytes 02ed44f9
- 00af1f80 ["INT_ADD", "register:40f0:8", ["const:af1f80:8", "const:4:8"]]
- 00af1f80 ["CALL", null, ["callee:0047495c:8"]]
+ 00af1fc4 ["INT_ADD", "register:40f0:8", ["const:af1fc4:8", "const:4:8"]]
+ 00af1fc4 ["CALL", null, ["callee:0047495c:8"]]
- 00af1f80 bytes 770ae697
+ 00af1fc4 bytes 660ae697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55619fc3d7061f4618ed496824005bd3"></a>

### [`00af24c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24c0.md) → [`00af2504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2504.md) FUN_00af2504

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00af24bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24bc.md) [`00af27c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md)
- 新版 呼出元 2件 [`00af2500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2500.md) [`00af2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00af2500",
      "incomplete_value": true,
      "site": "00af2508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2590",
      "incomplete_value": true,
      "site": "00af259c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af254c",
      "incomplete_value": true,
      "site": "00af2558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af25e0",
      "incomplete_value": true,
      "site": "00af25f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af259c",
      "incomplete_value": true,
      "site": "00af25ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
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
      "00af2544",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2590",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af25e0",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af2544",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2590",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af25e0",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24c0.md#insn-00af2508) · [`00af254c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24c0.md#insn-00af254c) · [`00af2558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24c0.md#insn-00af2558)
- 新版 `00af254c`（命令位置の公開資料なし） · `00af2590`（命令位置の公開資料なし） · `00af259c`（命令位置の公開資料なし）

~~~diff
- 00af2508 ["INT_ADD", "register:40f0:8", ["const:af2508:8", "const:4:8"]]
- 00af2508 ["CALL", null, ["callee:0047495c:8"]]
+ 00af254c ["INT_ADD", "register:40f0:8", ["const:af254c:8", "const:4:8"]]
+ 00af254c ["CALL", null, ["callee:0047495c:8"]]
- 00af2508 bytes 1509e697
+ 00af254c bytes 0409e697
- 00af254c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
- 00af254c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af2590 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
+ 00af2590 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af254c bytes 02cd44f9
+ 00af2590 bytes 02ed44f9
- 00af2558 ["INT_ADD", "register:40f0:8", ["const:af2558:8", "const:4:8"]]
- 00af2558 ["CALL", null, ["callee:0047495c:8"]]
+ 00af259c ["INT_ADD", "register:40f0:8", ["const:af259c:8", "const:4:8"]]
+ 00af259c ["CALL", null, ["callee:0047495c:8"]]
- 00af2558 bytes 0109e697
+ 00af259c bytes f008e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7841cdab721527561f819f060580986"></a>

### [`00af27c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md) → [`00af2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2808.md) _ZN8firebase4util19JavaObjectToVariantEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde540.md) · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md)
- 新版 呼出元 1件 [`00bde590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde590.md) · 呼出先 19件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2840",
      "incomplete_value": true,
      "site": "00af2850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af27fc",
      "incomplete_value": true,
      "site": "00af280c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af289c",
      "incomplete_value": true,
      "site": "00af28ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2858",
      "incomplete_value": true,
      "site": "00af2868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2928",
      "incomplete_value": true,
      "site": "00af2938",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af28e4",
      "incomplete_value": true,
      "site": "00af28f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af2840",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af289c",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00af28bc",
      "READ",
      [
        "storage",
        "010a0730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af2840",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00af289c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00af28bc",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md#insn-00af280c) · [`00af2824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md#insn-00af2824) · [`00af2868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md#insn-00af2868)
- 新版 `00af2850`（命令位置の公開資料なし） · `00af2868`（命令位置の公開資料なし） · `00af28ac`（命令位置の公開資料なし）

~~~diff
- 00af280c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af280c ["INT_ADD", "register:40f0:8", ["const:af280c:8", "const:4:8"]]
- 00af280c ["CALLIND", null, ["register:0:8"]]
+ 00af2850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af2850 ["INT_ADD", "register:40f0:8", ["const:af2850:8", "const:4:8"]]
+ 00af2850 ["CALLIND", null, ["register:0:8"]]
- 00af280c bytes 00013fd6
+ 00af2850 bytes 00013fd6
- 00af2824 ["INT_ADD", "register:40f0:8", ["const:af2824:8", "const:4:8"]]
- 00af2824 ["CALL", null, ["callee:00bde0a0:8"]]
+ 00af2868 ["INT_ADD", "register:40f0:8", ["const:af2868:8", "const:4:8"]]
+ 00af2868 ["CALL", null, ["callee:00bde0a0:8"]]
- 00af2824 bytes 0bae0394
+ 00af2868 bytes 0eae0394
- 00af2868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af2868 ["INT_ADD", "register:40f0:8", ["const:af2868:8", "const:4:8"]]
- 00af2868 ["CALLIND", null, ["register:0:8"]]
+ 00af28ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af28ac ["INT_ADD", "register:40f0:8", ["const:af28ac:8", "const:4:8"]]
+ 00af28ac ["CALLIND", null, ["register:0:8"]]
- 00af2868 bytes 00013fd6
+ 00af28ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5cde98e68a55826c367fc3c6e02e41d"></a>

### [`00af2edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md) → [`00af2f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md) _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde600.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde650.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2f60",
      "incomplete_value": true,
      "site": "00af2f68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2f1c",
      "incomplete_value": true,
      "site": "00af2f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2fac",
      "incomplete_value": true,
      "site": "00af2fb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2f68",
      "incomplete_value": true,
      "site": "00af2f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
              ]
            ]
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
      "definition_site": "00af2fd0",
      "incomplete_value": true,
      "site": "00af2fdc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
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
      "definition_site": "00af2f8c",
      "incomplete_value": true,
      "site": "00af2f98",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
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
      "00af2f60",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2fac",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2fd0",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af2f60",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2fac",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2fd0",
      "READ",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md#insn-00af2f24) · [`00af2f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md#insn-00af2f68) · [`00af2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md#insn-00af2f74)
- 新版 `00af2f68`（命令位置の公開資料なし） · `00af2fac`（命令位置の公開資料なし） · `00af2fb8`（命令位置の公開資料なし）

~~~diff
- 00af2f24 ["INT_ADD", "register:40f0:8", ["const:af2f24:8", "const:4:8"]]
- 00af2f24 ["CALL", null, ["callee:0047495c:8"]]
+ 00af2f68 ["INT_ADD", "register:40f0:8", ["const:af2f68:8", "const:4:8"]]
+ 00af2f68 ["CALL", null, ["callee:0047495c:8"]]
- 00af2f24 bytes 8e06e697
+ 00af2f68 bytes 7d06e697
- 00af2f68 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:8c8:8"]]
- 00af2f68 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af2fac ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:908:8"]]
+ 00af2fac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af2f68 bytes 626744f9
+ 00af2fac bytes 628744f9
- 00af2f74 ["INT_ADD", "register:40f0:8", ["const:af2f74:8", "const:4:8"]]
- 00af2f74 ["CALL", null, ["callee:00474b70:8"]]
+ 00af2fb8 ["INT_ADD", "register:40f0:8", ["const:af2fb8:8", "const:4:8"]]
+ 00af2fb8 ["CALL", null, ["callee:00474b70:8"]]
- 00af2f74 bytes ff06e697
+ 00af2fb8 bytes ee06e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bfb3681050052980ee30c5711dead09"></a>

### [`00af3190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3190.md) → [`00af31d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31d4.md) _ZN8firebase4util23VariantVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5f0.md) · 呼出先 3件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde570.md)
- 新版 呼出元 1件 [`00bde640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde640.md) · 呼出先 3件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af31f8",
      "incomplete_value": true,
      "site": "00af3204",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af31b4",
      "incomplete_value": true,
      "site": "00af31c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
      "definition_site": "00af31fc",
      "incomplete_value": true,
      "site": "00af3204",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af31b8",
      "incomplete_value": true,
      "site": "00af31c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af31f8",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31fc",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3218",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af31f8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31fc",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3218",
      "READ",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af31c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3190.md#insn-00af31c0) · [`00af31ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3190.md#insn-00af31ac) · [`00af31b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3190.md#insn-00af31b4)
- 新版 `00af3204`（命令位置の公開資料なし） · `00af31f0`（命令位置の公開資料なし） · `00af31f8`（命令位置の公開資料なし）

~~~diff
- 00af31c0 ["INT_ADD", "register:40f0:8", ["const:af31c0:8", "const:4:8"]]
- 00af31c0 ["CALL", null, ["callee:0056681c:8"]]
+ 00af3204 ["INT_ADD", "register:40f0:8", ["const:af3204:8", "const:4:8"]]
+ 00af3204 ["CALL", null, ["callee:0056681c:8"]]
- 00af31c0 bytes 97cde997
+ 00af3204 bytes 86cde997
- 00af31ac ["COPY", "tmp:0:8", ["const:540:8"]]
- 00af31ac ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00af31ac ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00af31ac ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00af31f0 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00af31f0 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00af31f0 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00af31f0 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00af31ac bytes f7021591
+ 00af31f0 bytes f7021691
- 00af31b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 00af31b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af31f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00af31f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af31b4 bytes 019942f9
+ 00af31f8 bytes 01b942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c22540e3a3f81955f75e7f5cb6b875"></a>

### [`00af3278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md) → [`00af32bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md) _ZN8firebase4util25JavaListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_IS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.15% / 新版 99.15%

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
      "definition_site": "00af32f4",
      "incomplete_value": true,
      "site": "00af32fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af32b0",
      "incomplete_value": true,
      "site": "00af32b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:900:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af33c4",
      "incomplete_value": true,
      "site": "00af33d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3380",
      "incomplete_value": true,
      "site": "00af3390",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
      "00af32f4",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af33c4",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af32f4",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined8"
      ]
    ],
    [
      "00af33c4",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af32b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md#insn-00af32b8) · [`00af3390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md#insn-00af3390) · [`00af32b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md#insn-00af32b0)
- 新版 `00af32fc`（命令位置の公開資料なし） · `00af33d4`（命令位置の公開資料なし） · `00af32f4`（命令位置の公開資料なし）

~~~diff
- 00af32b8 ["INT_ADD", "register:40f0:8", ["const:af32b8:8", "const:4:8"]]
- 00af32b8 ["CALL", null, ["callee:005533e0:8"]]
+ 00af32fc ["INT_ADD", "register:40f0:8", ["const:af32fc:8", "const:4:8"]]
+ 00af32fc ["CALL", null, ["callee:005533e0:8"]]
- 00af32b8 bytes 4a80e997
+ 00af32fc bytes 3980e997
- 00af3390 ["INT_ADD", "register:40f0:8", ["const:af3390:8", "const:4:8"]]
- 00af3390 ["CALL", null, ["callee:0047495c:8"]]
+ 00af33d4 ["INT_ADD", "register:40f0:8", ["const:af33d4:8", "const:4:8"]]
+ 00af33d4 ["CALL", null, ["callee:0047495c:8"]]
- 00af3390 bytes 7305e697
+ 00af33d4 bytes 6205e697
- 00af32b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
- 00af32b0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af32f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
+ 00af32f4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af32b0 bytes 028144f9
+ 00af32f4 bytes 02a144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3b9da8941e94bc5a1bdcd82ab8839bc"></a>

### [`00af3560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md) → [`00af35a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md) _ZN8firebase4util31JavaObjectListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af35e0",
      "incomplete_value": true,
      "site": "00af35e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af359c",
      "incomplete_value": true,
      "site": "00af35a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:900:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af36c8",
      "incomplete_value": true,
      "site": "00af36d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3684",
      "incomplete_value": true,
      "site": "00af3694",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
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
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af371c",
      "incomplete_value": true,
      "site": "00af3728",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
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
      "definition_site": "00af36d8",
      "incomplete_value": true,
      "site": "00af36e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
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
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af35e0",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af36c8",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af371c",
      "READ",
      [
        "storage",
        "010a0a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af35e0",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined8"
      ]
    ],
    [
      "00af36c8",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00af371c",
      "READ",
      [
        "storage",
        "010a0a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af35a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md#insn-00af35a4) · [`00af3694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md#insn-00af3694) · [`00af36d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md#insn-00af36d8)
- 新版 `00af35e8`（命令位置の公開資料なし） · `00af36d8`（命令位置の公開資料なし） · `00af371c`（命令位置の公開資料なし）

~~~diff
- 00af35a4 ["INT_ADD", "register:40f0:8", ["const:af35a4:8", "const:4:8"]]
- 00af35a4 ["CALL", null, ["callee:005533e0:8"]]
+ 00af35e8 ["INT_ADD", "register:40f0:8", ["const:af35e8:8", "const:4:8"]]
+ 00af35e8 ["CALL", null, ["callee:005533e0:8"]]
- 00af35a4 bytes 8f7fe997
+ 00af35e8 bytes 7e7fe997
- 00af3694 ["INT_ADD", "register:40f0:8", ["const:af3694:8", "const:4:8"]]
- 00af3694 ["CALL", null, ["callee:0047495c:8"]]
+ 00af36d8 ["INT_ADD", "register:40f0:8", ["const:af36d8:8", "const:4:8"]]
+ 00af36d8 ["CALL", null, ["callee:0047495c:8"]]
- 00af3694 bytes b204e697
+ 00af36d8 bytes a104e697
- 00af36d8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a58:8"]]
- 00af36d8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af371c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a98:8"]]
+ 00af371c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af36d8 bytes 822f45f9
+ 00af371c bytes 824f45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe1291515acaf837c96162941552adb"></a>

### [`00af3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md) → [`00af38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md) _ZN8firebase4util21JavaListToVariantListEP7_JNIEnvPNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEEP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5d0.md) · 呼出先 8件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)
- 新版 呼出元 1件 [`00bde620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde620.md) · 呼出先 8件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

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
      "definition_site": "00af38e4",
      "incomplete_value": true,
      "site": "00af38ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af38a0",
      "incomplete_value": true,
      "site": "00af38a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:900:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af39ac",
      "incomplete_value": true,
      "site": "00af39bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af3968",
      "incomplete_value": true,
      "site": "00af3978",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
      "00af38e4",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af39ac",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af38e4",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined8"
      ]
    ],
    [
      "00af39ac",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af38a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md#insn-00af38a8) · [`00af3978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md#insn-00af3978) · [`00af38a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md#insn-00af38a0)
- 新版 `00af38ec`（命令位置の公開資料なし） · `00af39bc`（命令位置の公開資料なし） · `00af38e4`（命令位置の公開資料なし）

~~~diff
- 00af38a8 ["INT_ADD", "register:40f0:8", ["const:af38a8:8", "const:4:8"]]
- 00af38a8 ["CALL", null, ["callee:005533e0:8"]]
+ 00af38ec ["INT_ADD", "register:40f0:8", ["const:af38ec:8", "const:4:8"]]
+ 00af38ec ["CALL", null, ["callee:005533e0:8"]]
- 00af38a8 bytes ce7ee997
+ 00af38ec bytes bd7ee997
- 00af3978 ["INT_ADD", "register:40f0:8", ["const:af3978:8", "const:4:8"]]
- 00af3978 ["CALL", null, ["callee:0047495c:8"]]
+ 00af39bc ["INT_ADD", "register:40f0:8", ["const:af39bc:8", "const:4:8"]]
+ 00af39bc ["CALL", null, ["callee:0047495c:8"]]
- 00af3978 bytes f903e697
+ 00af39bc bytes e803e697
- 00af38a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
- 00af38a0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af38e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
+ 00af38e4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af38a0 bytes 028144f9
+ 00af38e4 bytes 02a144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c078bf98f139a204a1edc43566a6b3c5"></a>

### [`00af42dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af42dc.md) → [`00af4320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4320.md) _ZN8firebase4util15IsJBooleanArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00af42f8",
      "incomplete_value": false,
      "site": "00af4304",
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
            "const:d73:8"
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
      "00af433c",
      "PARAM",
      [
        "storage",
        "0029bd73",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af433c",
      "PARAM",
      [
        "storage",
        "0029bd71",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af42dc.md#insn-00af4304) · [`00af42f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af42dc.md#insn-00af42f8) · [`00af4320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af42dc.md#insn-00af4320)
- 新版 `00af4348`（命令位置の公開資料なし） · `00af433c`（命令位置の公開資料なし） · `00af4364`（命令位置の公開資料なし）

~~~diff
- 00af4304 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4304 ["INT_ADD", "register:40f0:8", ["const:af4304:8", "const:4:8"]]
- 00af4304 ["CALLIND", null, ["register:0:8"]]
+ 00af4348 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4348 ["INT_ADD", "register:40f0:8", ["const:af4348:8", "const:4:8"]]
+ 00af4348 ["CALLIND", null, ["register:0:8"]]
- 00af4304 bytes 00013fd6
+ 00af4348 bytes 00013fd6
- 00af42f8 ["COPY", "tmp:0:8", ["const:d73:8"]]
- 00af42f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af42f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af42f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af433c ["COPY", "tmp:0:8", ["const:d71:8"]]
+ 00af433c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af433c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af433c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af42f8 bytes 21cc3591
+ 00af433c bytes 21c43591
- 00af4320 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4320 ["INT_ADD", "register:40f0:8", ["const:af4320:8", "const:4:8"]]
- 00af4320 ["CALLIND", null, ["register:0:8"]]
+ 00af4364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4364 ["INT_ADD", "register:40f0:8", ["const:af4364:8", "const:4:8"]]
+ 00af4364 ["CALLIND", null, ["register:0:8"]]
- 00af4320 bytes 00013fd6
+ 00af4364 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76deb958db852e3c521b09145de2be8"></a>

### [`00af43cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af43cc.md) → [`00af4410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4410.md) _ZN8firebase4util12IsJCharArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00af43e8",
      "incomplete_value": false,
      "site": "00af43f4",
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
            "const:73:8"
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
      "00af442c",
      "PARAM",
      [
        "storage",
        "002a6073",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af442c",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af43f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af43cc.md#insn-00af43f4) · [`00af43e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af43cc.md#insn-00af43e8) · [`00af4410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af43cc.md#insn-00af4410)
- 新版 `00af4438`（命令位置の公開資料なし） · `00af442c`（命令位置の公開資料なし） · `00af4454`（命令位置の公開資料なし）

~~~diff
- 00af43f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af43f4 ["INT_ADD", "register:40f0:8", ["const:af43f4:8", "const:4:8"]]
- 00af43f4 ["CALLIND", null, ["register:0:8"]]
+ 00af4438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4438 ["INT_ADD", "register:40f0:8", ["const:af4438:8", "const:4:8"]]
+ 00af4438 ["CALLIND", null, ["register:0:8"]]
- 00af43f4 bytes 00013fd6
+ 00af4438 bytes 00013fd6
- 00af43e8 ["COPY", "tmp:0:8", ["const:73:8"]]
- 00af43e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af43e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af43e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af442c ["COPY", "tmp:0:8", ["const:10d:8"]]
+ 00af442c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af442c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af442c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af43e8 bytes 21cc0191
+ 00af442c bytes 21340491
- 00af4410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4410 ["INT_ADD", "register:40f0:8", ["const:af4410:8", "const:4:8"]]
- 00af4410 ["CALLIND", null, ["register:0:8"]]
+ 00af4454 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4454 ["INT_ADD", "register:40f0:8", ["const:af4454:8", "const:4:8"]]
+ 00af4454 ["CALLIND", null, ["register:0:8"]]
- 00af4410 bytes 00013fd6
+ 00af4454 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-532b4305ab51485618489875583c7b70"></a>

### [`00af4444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4444.md) → [`00af4488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4488.md) _ZN8firebase4util13IsJShortArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00af4460",
      "incomplete_value": false,
      "site": "00af446c",
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
            "const:ce9:8"
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
      "00af44a4",
      "PARAM",
      [
        "storage",
        "002a3ce9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af44a4",
      "PARAM",
      [
        "storage",
        "002a3d74",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af446c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4444.md#insn-00af446c) · [`00af4460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4444.md#insn-00af4460) · [`00af4488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4444.md#insn-00af4488)
- 新版 `00af44b0`（命令位置の公開資料なし） · `00af44a4`（命令位置の公開資料なし） · `00af44cc`（命令位置の公開資料なし）

~~~diff
- 00af446c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af446c ["INT_ADD", "register:40f0:8", ["const:af446c:8", "const:4:8"]]
- 00af446c ["CALLIND", null, ["register:0:8"]]
+ 00af44b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af44b0 ["INT_ADD", "register:40f0:8", ["const:af44b0:8", "const:4:8"]]
+ 00af44b0 ["CALLIND", null, ["register:0:8"]]
- 00af446c bytes 00013fd6
+ 00af44b0 bytes 00013fd6
- 00af4460 ["COPY", "tmp:0:8", ["const:ce9:8"]]
- 00af4460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af44a4 ["COPY", "tmp:0:8", ["const:d74:8"]]
+ 00af44a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af44a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af44a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4460 bytes 21a43391
+ 00af44a4 bytes 21d03591
- 00af4488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4488 ["INT_ADD", "register:40f0:8", ["const:af4488:8", "const:4:8"]]
- 00af4488 ["CALLIND", null, ["register:0:8"]]
+ 00af44cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af44cc ["INT_ADD", "register:40f0:8", ["const:af44cc:8", "const:4:8"]]
+ 00af44cc ["CALLIND", null, ["register:0:8"]]
- 00af4488 bytes 00013fd6
+ 00af44cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-693a7b1b9935273a2a78be2969b8bfa1"></a>

### [`00af4534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4534.md) → [`00af4578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4578.md) _ZN8firebase4util12IsJLongArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00af4594",
      "incomplete_value": false,
      "site": "00af45a0",
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
            "const:584:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4550",
      "incomplete_value": false,
      "site": "00af455c",
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
            "const:611:8"
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
      "00af4594",
      "PARAM",
      [
        "storage",
        "00298611",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4594",
      "PARAM",
      [
        "storage",
        "00298584",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af455c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4534.md#insn-00af455c) · [`00af4550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4534.md#insn-00af4550) · [`00af4578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4534.md#insn-00af4578)
- 新版 `00af45a0`（命令位置の公開資料なし） · `00af4594`（命令位置の公開資料なし） · `00af45bc`（命令位置の公開資料なし）

~~~diff
- 00af455c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af455c ["INT_ADD", "register:40f0:8", ["const:af455c:8", "const:4:8"]]
- 00af455c ["CALLIND", null, ["register:0:8"]]
+ 00af45a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af45a0 ["INT_ADD", "register:40f0:8", ["const:af45a0:8", "const:4:8"]]
+ 00af45a0 ["CALLIND", null, ["register:0:8"]]
- 00af455c bytes 00013fd6
+ 00af45a0 bytes 00013fd6
- 00af4550 ["COPY", "tmp:0:8", ["const:611:8"]]
- 00af4550 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4550 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4550 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4594 ["COPY", "tmp:0:8", ["const:584:8"]]
+ 00af4594 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4594 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4594 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4550 bytes 21441891
+ 00af4594 bytes 21101691
- 00af4578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4578 ["INT_ADD", "register:40f0:8", ["const:af4578:8", "const:4:8"]]
- 00af4578 ["CALLIND", null, ["register:0:8"]]
+ 00af45bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af45bc ["INT_ADD", "register:40f0:8", ["const:af45bc:8", "const:4:8"]]
+ 00af45bc ["CALLIND", null, ["register:0:8"]]
- 00af4578 bytes 00013fd6
+ 00af45bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b54348ad24afe106b7dcac4f98cb3a7c"></a>

### [`00af45ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af45ac.md) → [`00af45f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af45f0.md) _ZN8firebase4util13IsJFloatArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00af45c8",
      "incomplete_value": false,
      "site": "00af45d4",
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
            "const:74c:8"
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
      "00af460c",
      "PARAM",
      [
        "storage",
        "0029a74c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af460c",
      "PARAM",
      [
        "storage",
        "0029a74a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af45d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af45ac.md#insn-00af45d4) · [`00af45c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af45ac.md#insn-00af45c8) · [`00af45f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af45ac.md#insn-00af45f0)
- 新版 `00af4618`（命令位置の公開資料なし） · `00af460c`（命令位置の公開資料なし） · `00af4634`（命令位置の公開資料なし）

~~~diff
- 00af45d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af45d4 ["INT_ADD", "register:40f0:8", ["const:af45d4:8", "const:4:8"]]
- 00af45d4 ["CALLIND", null, ["register:0:8"]]
+ 00af4618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4618 ["INT_ADD", "register:40f0:8", ["const:af4618:8", "const:4:8"]]
+ 00af4618 ["CALLIND", null, ["register:0:8"]]
- 00af45d4 bytes 00013fd6
+ 00af4618 bytes 00013fd6
- 00af45c8 ["COPY", "tmp:0:8", ["const:74c:8"]]
- 00af45c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af45c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af45c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af460c ["COPY", "tmp:0:8", ["const:74a:8"]]
+ 00af460c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af460c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af460c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af45c8 bytes 21301d91
+ 00af460c bytes 21281d91
- 00af45f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af45f0 ["INT_ADD", "register:40f0:8", ["const:af45f0:8", "const:4:8"]]
- 00af45f0 ["CALLIND", null, ["register:0:8"]]
+ 00af4634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4634 ["INT_ADD", "register:40f0:8", ["const:af4634:8", "const:4:8"]]
+ 00af4634 ["CALLIND", null, ["register:0:8"]]
- 00af45f0 bytes 00013fd6
+ 00af4634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a717e364954d72ad74db7a8fa956cb"></a>

### [`00af4624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4624.md) → [`00af4668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4668.md) _ZN8firebase4util14IsJDoubleArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00af4684",
      "incomplete_value": false,
      "site": "00af4690",
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
            "const:606:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4640",
      "incomplete_value": false,
      "site": "00af464c",
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
            "const:693:8"
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
      "00af4684",
      "PARAM",
      [
        "storage",
        "00299693",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4684",
      "PARAM",
      [
        "storage",
        "00299606",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4624.md#insn-00af464c) · [`00af4640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4624.md#insn-00af4640) · [`00af4668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4624.md#insn-00af4668)
- 新版 `00af4690`（命令位置の公開資料なし） · `00af4684`（命令位置の公開資料なし） · `00af46ac`（命令位置の公開資料なし）

~~~diff
- 00af464c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af464c ["INT_ADD", "register:40f0:8", ["const:af464c:8", "const:4:8"]]
- 00af464c ["CALLIND", null, ["register:0:8"]]
+ 00af4690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4690 ["INT_ADD", "register:40f0:8", ["const:af4690:8", "const:4:8"]]
+ 00af4690 ["CALLIND", null, ["register:0:8"]]
- 00af464c bytes 00013fd6
+ 00af4690 bytes 00013fd6
- 00af4640 ["COPY", "tmp:0:8", ["const:693:8"]]
- 00af4640 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4640 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4640 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4684 ["COPY", "tmp:0:8", ["const:606:8"]]
+ 00af4684 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4684 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4684 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4640 bytes 214c1a91
+ 00af4684 bytes 21181891
- 00af4668 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4668 ["INT_ADD", "register:40f0:8", ["const:af4668:8", "const:4:8"]]
- 00af4668 ["CALLIND", null, ["register:0:8"]]
+ 00af46ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af46ac ["INT_ADD", "register:40f0:8", ["const:af46ac:8", "const:4:8"]]
+ 00af46ac ["CALLIND", null, ["register:0:8"]]
- 00af4668 bytes 00013fd6
+ 00af46ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8184d9a3ddf9891736c3f011e2e99b"></a>

### [`00af53e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af53e4.md) → [`00af5428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5428.md) _ZN8firebase4util15JArrayToVariantEP7_JNIEnvP7_jarray

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde430.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4e0.md) [`00bde500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde500.md) [`00bde510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde510.md)
- 新版 呼出元 1件 [`00bde480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde480.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde530.md) [`00bde550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde550.md) [`00bde560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde560.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.05% / 新版 97.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5458",
      "incomplete_value": true,
      "site": "00af5468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af5414",
      "incomplete_value": true,
      "site": "00af5424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:668:8"
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
      "definition_site": "00af54c8",
      "incomplete_value": false,
      "site": "00af54cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:31a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5484",
      "incomplete_value": false,
      "site": "00af5488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:3a7:8"
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
    "new": {
      "definition_site": "00af54d8",
      "incomplete_value": false,
      "site": "00af54e4",
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
    "old": {
      "definition_site": "00af5494",
      "incomplete_value": false,
      "site": "00af54a0",
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
            "const:d73:8"
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
      "00af5458",
      "READ",
      [
        "storage",
        "010a0668",
        null,
        "undefined8"
      ]
    ],
    [
      "00af54c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af548c"
      ]
    ],
    [
      "00af54c8",
      "PARAM",
      [
        "storage",
        "002953a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af5458",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af54c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af54d0"
      ]
    ],
    [
      "00af54c8",
      "PARAM",
      [
        "storage",
        "0029531a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af53e4.md#insn-00af5424) · [`00af5488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af53e4.md#insn-00af5488) · [`00af54a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af53e4.md#insn-00af54a0)
- 新版 `00af5468`（命令位置の公開資料なし） · `00af54cc`（命令位置の公開資料なし） · `00af54e4`（命令位置の公開資料なし）

~~~diff
- 00af5424 ["INT_ADD", "register:40f0:8", ["const:af5424:8", "const:4:8"]]
- 00af5424 ["CALL", null, ["callee:00474b70:8"]]
+ 00af5468 ["INT_ADD", "register:40f0:8", ["const:af5468:8", "const:4:8"]]
+ 00af5468 ["CALL", null, ["callee:00474b70:8"]]
- 00af5424 bytes d3fde597
+ 00af5468 bytes c2fde597
- 00af5488 ["INT_ADD", "register:40f0:8", ["const:af5488:8", "const:4:8"]]
- 00af5488 ["CALL", null, ["callee:00bde180:8"]]
+ 00af54cc ["INT_ADD", "register:40f0:8", ["const:af54cc:8", "const:4:8"]]
+ 00af54cc ["CALL", null, ["callee:00bde180:8"]]
- 00af5488 bytes 2aa30394
+ 00af54cc bytes 2da30394
- 00af54a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af54a0 ["INT_ADD", "register:40f0:8", ["const:af54a0:8", "const:4:8"]]
- 00af54a0 ["CALLIND", null, ["register:0:8"]]
+ 00af54e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af54e4 ["INT_ADD", "register:40f0:8", ["const:af54e4:8", "const:4:8"]]
+ 00af54e4 ["CALLIND", null, ["register:0:8"]]
- 00af54a0 bytes 00013fd6
+ 00af54e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235ed225893be9bb50d33c0e2b3c3aea"></a>

### [`00af5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) → [`00af5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md) _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde070.md) · 呼出先 6件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)
- 新版 呼出元 1件 [`00bde0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0c0.md) · 呼出先 6件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5e48",
      "incomplete_value": false,
      "site": "00af5e4c",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5e04",
      "incomplete_value": false,
      "site": "00af5e08",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5e58",
      "incomplete_value": true,
      "site": "00af5e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5e14",
      "incomplete_value": true,
      "site": "00af5e2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:350:8"
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
      "definition_site": "00af5e5c",
      "incomplete_value": true,
      "site": "00af5e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5e18",
      "incomplete_value": true,
      "site": "00af5e2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
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
      "00af5d1c",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ],
    [
      "00af5d38",
      "READ",
      [
        "storage",
        "010a0a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00af5e48",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5d1c",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ],
    [
      "00af5d38",
      "READ",
      [
        "storage",
        "010a0ac0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af5e48",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md#insn-00af5e08) · [`00af5e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md#insn-00af5e2c) · [`00af5e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md#insn-00af5e8c)
- 新版 `00af5e4c`（命令位置の公開資料なし） · `00af5e70`（命令位置の公開資料なし） · `00af5ed0`（命令位置の公開資料なし）

~~~diff
- 00af5e08 ["INT_ADD", "register:40f0:8", ["const:af5e08:8", "const:4:8"]]
- 00af5e08 ["CALL", null, ["callee:00bde830:8"]]
+ 00af5e4c ["INT_ADD", "register:40f0:8", ["const:af5e4c:8", "const:4:8"]]
+ 00af5e4c ["CALL", null, ["callee:00bde830:8"]]
- 00af5e08 bytes 76a20394
+ 00af5e4c bytes 79a20394
- 00af5e2c ["INT_ADD", "register:40f0:8", ["const:af5e2c:8", "const:4:8"]]
- 00af5e2c ["CALL", null, ["callee:0056681c:8"]]
+ 00af5e70 ["INT_ADD", "register:40f0:8", ["const:af5e70:8", "const:4:8"]]
+ 00af5e70 ["CALL", null, ["callee:0056681c:8"]]
- 00af5e2c bytes 7cc2e997
+ 00af5e70 bytes 6bc2e997
- 00af5e8c ["INT_ADD", "register:40f0:8", ["const:af5e8c:8", "const:4:8"]]
- 00af5e8c ["CALL", null, ["callee:00bde830:8"]]
+ 00af5ed0 ["INT_ADD", "register:40f0:8", ["const:af5ed0:8", "const:4:8"]]
+ 00af5ed0 ["CALL", null, ["callee:00bde830:8"]]
- 00af5e8c bytes 55a20394
+ 00af5ed0 bytes 58a20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68800ce38337d722ca55b493100acaa1"></a>

### [`00af5ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md) → [`00af5f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md) _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5f30",
      "incomplete_value": false,
      "site": "00af5f50",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5eec",
      "incomplete_value": false,
      "site": "00af5f0c",
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
            "const:a88:8"
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
      "definition_site": "00af5f9c",
      "incomplete_value": false,
      "site": "00af5fa0",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5f58",
      "incomplete_value": false,
      "site": "00af5f5c",
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
            "const:a88:8"
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
      "00af5f30",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ],
    [
      "00af5f9c",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5f30",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ],
    [
      "00af5f9c",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md#insn-00af5f0c) · [`00af5f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md#insn-00af5f50) · [`00af5f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md#insn-00af5f5c)
- 新版 `00af5f50`（命令位置の公開資料なし） · `00af5f94`（命令位置の公開資料なし） · `00af5fa0`（命令位置の公開資料なし）

~~~diff
- 00af5f0c ["INT_ADD", "register:40f0:8", ["const:af5f0c:8", "const:4:8"]]
- 00af5f0c ["CALL", null, ["callee:00bde820:8"]]
+ 00af5f50 ["INT_ADD", "register:40f0:8", ["const:af5f50:8", "const:4:8"]]
+ 00af5f50 ["CALL", null, ["callee:00bde820:8"]]
- 00af5f0c bytes 31a20394
+ 00af5f50 bytes 34a20394
- 00af5f50 ["INT_ADD", "register:40f0:8", ["const:af5f50:8", "const:4:8"]]
- 00af5f50 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af5f94 ["INT_ADD", "register:40f0:8", ["const:af5f94:8", "const:4:8"]]
+ 00af5f94 ["CALL", null, ["callee:00bdb060:8"]]
- 00af5f50 bytes 30940394
+ 00af5f94 bytes 33940394
- 00af5f5c ["INT_ADD", "register:40f0:8", ["const:af5f5c:8", "const:4:8"]]
- 00af5f5c ["CALL", null, ["callee:00bde830:8"]]
+ 00af5fa0 ["INT_ADD", "register:40f0:8", ["const:af5fa0:8", "const:4:8"]]
+ 00af5fa0 ["CALL", null, ["callee:00bde830:8"]]
- 00af5f5c bytes 21a20394
+ 00af5fa0 bytes 24a20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e626ad001a8ed5d4dd1e35e4e2e6bd"></a>

### [`00af6074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md) → [`00af60b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af60b8.md) _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde310.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde360.md)

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
      "definition_site": "00af60d8",
      "incomplete_value": true,
      "site": "00af60e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6094",
      "incomplete_value": true,
      "site": "00af609c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:398:8"
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
      "00af60d8",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af60d8",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af609c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md#insn-00af609c) · [`00af6084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md#insn-00af6084) · [`00af6094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md#insn-00af6094)
- 新版 `00af60e0`（命令位置の公開資料なし） · `00af60c8`（命令位置の公開資料なし） · `00af60d8`（命令位置の公開資料なし）

~~~diff
- 00af609c ["INT_ADD", "register:40f0:8", ["const:af609c:8", "const:4:8"]]
- 00af609c ["CALL", null, ["callee:00551e14:8"]]
+ 00af60e0 ["INT_ADD", "register:40f0:8", ["const:af60e0:8", "const:4:8"]]
+ 00af60e0 ["CALL", null, ["callee:00551e14:8"]]
- 00af609c bytes 5e6fe997
+ 00af60e0 bytes 4d6fe997
- 00af6084 ["INT_ADD", "register:40f0:8", ["const:af6084:8", "const:4:8"]]
- 00af6084 ["CALL", null, ["callee:00bde360:8"]]
+ 00af60c8 ["INT_ADD", "register:40f0:8", ["const:af60c8:8", "const:4:8"]]
+ 00af60c8 ["CALL", null, ["callee:00bde360:8"]]
- 00af6084 bytes a3a00394
+ 00af60c8 bytes a6a00394
- 00af6094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:398:8"]]
- 00af6094 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af60d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
+ 00af60d8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af6094 bytes 02cd41f9
+ 00af60d8 bytes 02ed41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0138abc48b59ce4f288a1e80158f0ab3"></a>

### [`00af6170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6170.md) → [`00af61b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af61b4.md) _ZN8firebase4util17JavaThreadContext9TerminateEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bde500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde500.md) · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af61f0",
      "incomplete_value": true,
      "site": "00af61f0",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af61ac",
      "incomplete_value": true,
      "site": "00af61ac",
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
            "const:380:8"
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
      "definition_site": "00af6240",
      "incomplete_value": true,
      "site": "00af6240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af61fc",
      "incomplete_value": true,
      "site": "00af61fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "definition_site": "00af626c",
      "incomplete_value": true,
      "site": "00af626c",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6228",
      "incomplete_value": true,
      "site": "00af6228",
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
            "const:3b8:8"
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
      "00af61c8",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af61d8",
      "READ",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ],
    [
      "00af61f0",
      "WRITE",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00af61c8",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af61d8",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00af61f0",
      "WRITE",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af61ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6170.md#insn-00af61ac) · [`00af61e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6170.md#insn-00af61e4) · [`00af61f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6170.md#insn-00af61f8)
- 新版 `00af61f0`（命令位置の公開資料なし） · `00af6228`（命令位置の公開資料なし） · `00af623c`（命令位置の公開資料なし）

~~~diff
- 00af61ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00af61ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00af61ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:380:8"]]
- 00af61ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00af61f0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00af61f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00af61f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3c0:8"]]
+ 00af61f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00af61ac bytes bf020e39
+ 00af61f0 bytes bf020f39
- 00af61e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af61e4 ["INT_ADD", "register:40f0:8", ["const:af61e4:8", "const:4:8"]]
- 00af61e4 ["CALLIND", null, ["register:0:8"]]
+ 00af6228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af6228 ["INT_ADD", "register:40f0:8", ["const:af6228:8", "const:4:8"]]
+ 00af6228 ["CALLIND", null, ["register:0:8"]]
- 00af61e4 bytes 00013fd6
+ 00af6228 bytes 00013fd6
- 00af61f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af61f8 ["INT_ADD", "register:40f0:8", ["const:af61f8:8", "const:4:8"]]
- 00af61f8 ["CALLIND", null, ["register:0:8"]]
+ 00af623c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af623c ["INT_ADD", "register:40f0:8", ["const:af623c:8", "const:4:8"]]
+ 00af623c ["CALLIND", null, ["register:0:8"]]
- 00af61f8 bytes 00013fd6
+ 00af623c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d835664b9a0ff067c517a7464fd54c"></a>

### [`00af628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af628c.md) → [`00af62d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af62d0.md) _ZN8firebase4util17JavaThreadContext13SetupInstanceEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af62f8",
      "incomplete_value": true,
      "site": "00af6304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af62b4",
      "incomplete_value": true,
      "site": "00af62c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
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
      "definition_site": "00af62fc",
      "incomplete_value": true,
      "site": "00af6304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af62b8",
      "incomplete_value": true,
      "site": "00af62c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
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
      "00af62f8",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af62fc",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af62f8",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af62fc",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af62c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af628c.md#insn-00af62c0) · [`00af62b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af628c.md#insn-00af62b4) · [`00af62b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af628c.md#insn-00af62b8)
- 新版 `00af6304`（命令位置の公開資料なし） · `00af62f8`（命令位置の公開資料なし） · `00af62fc`（命令位置の公開資料なし）

~~~diff
- 00af62c0 ["INT_ADD", "register:40f0:8", ["const:af62c0:8", "const:4:8"]]
- 00af62c0 ["CALL", null, ["callee:0056681c:8"]]
+ 00af6304 ["INT_ADD", "register:40f0:8", ["const:af6304:8", "const:4:8"]]
+ 00af6304 ["CALL", null, ["callee:0056681c:8"]]
- 00af62c0 bytes 57c1e997
+ 00af6304 bytes 46c1e997
- 00af62b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 00af62b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af62f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b8:8"]]
+ 00af62f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af62b4 bytes 01bd41f9
+ 00af62f8 bytes 01dd41f9
- 00af62b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:388:8"]]
- 00af62b8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af62fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3c8:8"]]
+ 00af62fc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af62b8 bytes 22c541f9
+ 00af62fc bytes 22e541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e16910ced66b31a84783911701ed35a"></a>

### [`00af6324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6324.md) → [`00af6368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6368.md) _ZN8firebase4util17JavaThreadContext15RunOnMainThreadEP7_JNIEnvP8_jobjectPFvPvES6_S8_PS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde490.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)
- 新版 呼出元 1件 [`00bde4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4e0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af63f8",
      "incomplete_value": true,
      "site": "00af640c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af63b4",
      "incomplete_value": true,
      "site": "00af63c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
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
      "definition_site": "00af63fc",
      "incomplete_value": true,
      "site": "00af640c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af63b8",
      "incomplete_value": true,
      "site": "00af63c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "00af6394",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6398",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ],
    [
      "00af63f8",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af6394",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6398",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af63f8",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af63c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6324.md#insn-00af63c8) · [`00af6350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6324.md#insn-00af6350) · [`00af6354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6324.md#insn-00af6354)
- 新版 `00af640c`（命令位置の公開資料なし） · `00af6394`（命令位置の公開資料なし） · `00af6398`（命令位置の公開資料なし）

~~~diff
- 00af63c8 ["INT_ADD", "register:40f0:8", ["const:af63c8:8", "const:4:8"]]
- 00af63c8 ["CALL", null, ["callee:00bde3c0:8"]]
+ 00af640c ["INT_ADD", "register:40f0:8", ["const:af640c:8", "const:4:8"]]
+ 00af640c ["CALL", null, ["callee:00bde3c0:8"]]
- 00af63c8 bytes ea9f0394
+ 00af640c bytes ed9f0394
- 00af6350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 00af6350 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af6394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b8:8"]]
+ 00af6394 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af6350 bytes 01bd41f9
+ 00af6394 bytes 01dd41f9
- 00af6354 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:388:8"]]
- 00af6354 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af6398 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3c8:8"]]
+ 00af6398 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af6354 bytes 22c541f9
+ 00af6398 bytes 22e541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6059fa93cc2ddb8508d1191588e82ec1"></a>

### [`00af6424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6424.md) → [`00af6468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6468.md) _ZN8firebase4util17JavaThreadContext21RunOnBackgroundThreadEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4a0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)
- 新版 呼出元 1件 [`00bde4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4f0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6490",
      "incomplete_value": true,
      "site": "00af649c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af644c",
      "incomplete_value": true,
      "site": "00af6458",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:378:8"
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
      "definition_site": "00af6494",
      "incomplete_value": true,
      "site": "00af649c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6450",
      "incomplete_value": true,
      "site": "00af6458",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:388:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af64f4",
      "incomplete_value": true,
      "site": "00af6504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af64b0",
      "incomplete_value": true,
      "site": "00af64c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
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
      "00af6490",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6494",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ],
    [
      "00af64f4",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af6490",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6494",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af64f4",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6424.md#insn-00af6458) · [`00af64c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6424.md#insn-00af64c0) · [`00af644c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6424.md#insn-00af644c)
- 新版 `00af649c`（命令位置の公開資料なし） · `00af6504`（命令位置の公開資料なし） · `00af6490`（命令位置の公開資料なし）

~~~diff
- 00af6458 ["INT_ADD", "register:40f0:8", ["const:af6458:8", "const:4:8"]]
- 00af6458 ["CALL", null, ["callee:0056681c:8"]]
+ 00af649c ["INT_ADD", "register:40f0:8", ["const:af649c:8", "const:4:8"]]
+ 00af649c ["CALL", null, ["callee:0056681c:8"]]
- 00af6458 bytes f1c0e997
+ 00af649c bytes e0c0e997
- 00af64c0 ["INT_ADD", "register:40f0:8", ["const:af64c0:8", "const:4:8"]]
- 00af64c0 ["CALL", null, ["callee:00bde3c0:8"]]
+ 00af6504 ["INT_ADD", "register:40f0:8", ["const:af6504:8", "const:4:8"]]
+ 00af6504 ["CALL", null, ["callee:00bde3c0:8"]]
- 00af64c0 bytes ac9f0394
+ 00af6504 bytes af9f0394
- 00af644c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 00af644c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af6490 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b8:8"]]
+ 00af6490 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af644c bytes 01bd41f9
+ 00af6490 bytes 01dd41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39e58ef213471c559c43b8bdca8fda18"></a>

### [`00af6524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6524.md) → [`00af6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6568.md) _ZN8firebase4util9FindClassEP7_JNIEnvPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6a0.md) · 呼出先 1件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md)
- 新版 呼出元 1件 [`00bde6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6f0.md) · 呼出先 1件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af65e0",
      "incomplete_value": true,
      "site": "00af65e4",
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
      "definition_site": "00af659c",
      "incomplete_value": true,
      "site": "00af65a0",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af660c",
      "incomplete_value": true,
      "site": "00af6610",
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
      "definition_site": "00af65c8",
      "incomplete_value": true,
      "site": "00af65cc",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af667c",
      "incomplete_value": true,
      "site": "00af6680",
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
      "definition_site": "00af6638",
      "incomplete_value": true,
      "site": "00af663c",
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
      "00af65d4",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6600",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6618",
      "READ",
      [
        "storage",
        "010a0340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af65d4",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6600",
      "READ",
      [
        "storage",
        "010a0ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6618",
      "READ",
      [
        "storage",
        "010a0380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af655c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6524.md#insn-00af655c) · [`00af6588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6524.md#insn-00af6588) · [`00af65e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6524.md#insn-00af65e0)
- 新版 `00af65a0`（命令位置の公開資料なし） · `00af65cc`（命令位置の公開資料なし） · `00af6624`（命令位置の公開資料なし）

~~~diff
- 00af655c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af655c ["INT_ADD", "register:40f0:8", ["const:af655c:8", "const:4:8"]]
- 00af655c ["CALLIND", null, ["register:0:8"]]
+ 00af65a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af65a0 ["INT_ADD", "register:40f0:8", ["const:af65a0:8", "const:4:8"]]
+ 00af65a0 ["CALLIND", null, ["register:0:8"]]
- 00af655c bytes 00013fd6
+ 00af65a0 bytes 00013fd6
- 00af6588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af6588 ["INT_ADD", "register:40f0:8", ["const:af6588:8", "const:4:8"]]
- 00af6588 ["CALLIND", null, ["register:0:8"]]
+ 00af65cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af65cc ["INT_ADD", "register:40f0:8", ["const:af65cc:8", "const:4:8"]]
+ 00af65cc ["CALLIND", null, ["register:0:8"]]
- 00af6588 bytes 00013fd6
+ 00af65cc bytes 00013fd6
- 00af65e0 ["INT_ADD", "register:40f0:8", ["const:af65e0:8", "const:4:8"]]
- 00af65e0 ["CALL", null, ["callee:0047495c:8"]]
+ 00af6624 ["INT_ADD", "register:40f0:8", ["const:af6624:8", "const:4:8"]]
+ 00af6624 ["CALL", null, ["callee:0047495c:8"]]
- 00af65e0 bytes dff8e597
+ 00af6624 bytes cef8e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-035a8126f30a59ea0fb9711d96f99dee"></a>

### [`00af66a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af66a8.md) → [`00af66ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af66ec.md) _ZN8firebase4util16FindClassInFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde460.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4b0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6734",
      "incomplete_value": true,
      "site": "00af6744",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af66f0",
      "incomplete_value": true,
      "site": "00af6700",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6788",
      "incomplete_value": true,
      "site": "00af6794",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6744",
      "incomplete_value": true,
      "site": "00af6750",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7a8:8"
              ]
            ]
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
      "definition_site": "00af6858",
      "incomplete_value": true,
      "site": "00af6864",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6814",
      "incomplete_value": true,
      "site": "00af6820",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af6734",
      "READ",
      [
        "storage",
        "010a04e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6788",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6800",
      "READ",
      [
        "storage",
        "010a0520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af6734",
      "READ",
      [
        "storage",
        "010a0520",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6788",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6800",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af66a8.md#insn-00af6700) · [`00af6744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af66a8.md#insn-00af6744) · [`00af6750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af66a8.md#insn-00af6750)
- 新版 `00af6744`（命令位置の公開資料なし） · `00af6788`（命令位置の公開資料なし） · `00af6794`（命令位置の公開資料なし）

~~~diff
- 00af6700 ["INT_ADD", "register:40f0:8", ["const:af6700:8", "const:4:8"]]
- 00af6700 ["CALL", null, ["callee:0047495c:8"]]
+ 00af6744 ["INT_ADD", "register:40f0:8", ["const:af6744:8", "const:4:8"]]
+ 00af6744 ["CALL", null, ["callee:0047495c:8"]]
- 00af6700 bytes 97f8e597
+ 00af6744 bytes 86f8e597
- 00af6744 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00af6744 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af6788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00af6788 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af6744 bytes 82d643f9
+ 00af6788 bytes 82f643f9
- 00af6750 ["INT_ADD", "register:40f0:8", ["const:af6750:8", "const:4:8"]]
- 00af6750 ["CALL", null, ["callee:0047495c:8"]]
+ 00af6794 ["INT_ADD", "register:40f0:8", ["const:af6794:8", "const:4:8"]]
+ 00af6794 ["CALL", null, ["callee:0047495c:8"]]
- 00af6750 bytes 83f8e597
+ 00af6794 bytes 72f8e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd51bc9bb09d69af33b75896bad1eeb1"></a>

### [`00af6ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6ed8.md) → [`00af6f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6f1c.md) _ZN8firebase4util25GetResourceIdFromActivityEP7_JNIEnvP8_jobjectPKcNS0_12ResourceTypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6f38",
      "incomplete_value": true,
      "site": "00af6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6ef4",
      "incomplete_value": true,
      "site": "00af6f04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6f8c",
      "incomplete_value": true,
      "site": "00af6f98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:538:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6f48",
      "incomplete_value": true,
      "site": "00af6f54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
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
      "definition_site": "00af7010",
      "incomplete_value": true,
      "site": "00af702c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af6fcc",
      "incomplete_value": true,
      "site": "00af6fe8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af6f38",
      "READ",
      [
        "storage",
        "010a0500",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6f8c",
      "READ",
      [
        "storage",
        "010a04f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6fe4",
      "DATA",
      [
        "storage",
        "00c10680",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00af6f38",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6f8c",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6fe4",
      "DATA",
      [
        "storage",
        "00c106d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6ed8.md#insn-00af6f04) · [`00af6f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6ed8.md#insn-00af6f48) · [`00af6f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6ed8.md#insn-00af6f54)
- 新版 `00af6f48`（命令位置の公開資料なし） · `00af6f8c`（命令位置の公開資料なし） · `00af6f98`（命令位置の公開資料なし）

~~~diff
- 00af6f04 ["INT_ADD", "register:40f0:8", ["const:af6f04:8", "const:4:8"]]
- 00af6f04 ["CALL", null, ["callee:0047495c:8"]]
+ 00af6f48 ["INT_ADD", "register:40f0:8", ["const:af6f48:8", "const:4:8"]]
+ 00af6f48 ["CALL", null, ["callee:0047495c:8"]]
- 00af6f04 bytes 96f6e597
+ 00af6f48 bytes 85f6e597
- 00af6f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f8:8"]]
- 00af6f48 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af6f8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:538:8"]]
+ 00af6f8c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af6f48 bytes 027d42f9
+ 00af6f8c bytes 029d42f9
- 00af6f54 ["INT_ADD", "register:40f0:8", ["const:af6f54:8", "const:4:8"]]
- 00af6f54 ["CALL", null, ["callee:0047495c:8"]]
+ 00af6f98 ["INT_ADD", "register:40f0:8", ["const:af6f98:8", "const:4:8"]]
+ 00af6f98 ["CALL", null, ["callee:0047495c:8"]]
- 00af6f54 bytes 82f6e597
+ 00af6f98 bytes 71f6e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b013b98055ec45450d3df5e3cafcf390"></a>

### [`00af7090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7090.md) → [`00af70d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af70d4.md) _ZN8firebase4util29GetResourceStringFromActivityEP7_JNIEnvP8_jobjecti

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

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
      "definition_site": "00af70fc",
      "incomplete_value": false,
      "site": "00af7100",
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
            "const:eac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af70b8",
      "incomplete_value": false,
      "site": "00af70bc",
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
            "const:e21:8"
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
      "definition_site": "00af7108",
      "incomplete_value": true,
      "site": "00af7118",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af70c4",
      "incomplete_value": true,
      "site": "00af70d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
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
      "00af70fc",
      "PARAM",
      [
        "storage",
        "002a4e21",
        null,
        "string"
      ]
    ],
    [
      "00af7108",
      "READ",
      [
        "storage",
        "010a0518",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af70fc",
      "PARAM",
      [
        "storage",
        "002a4eac",
        null,
        "string"
      ]
    ],
    [
      "00af7108",
      "READ",
      [
        "storage",
        "010a0558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af70bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7090.md#insn-00af70bc) · [`00af70d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7090.md#insn-00af70d4) · [`00af7100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7090.md#insn-00af7100)
- 新版 `00af7100`（命令位置の公開資料なし） · `00af7118`（命令位置の公開資料なし） · `00af7144`（命令位置の公開資料なし）

~~~diff
- 00af70bc ["INT_ADD", "register:40f0:8", ["const:af70bc:8", "const:4:8"]]
- 00af70bc ["CALL", null, ["callee:00bde180:8"]]
+ 00af7100 ["INT_ADD", "register:40f0:8", ["const:af7100:8", "const:4:8"]]
+ 00af7100 ["CALL", null, ["callee:00bde180:8"]]
- 00af70bc bytes 1d9c0394
+ 00af7100 bytes 209c0394
- 00af70d4 ["INT_ADD", "register:40f0:8", ["const:af70d4:8", "const:4:8"]]
- 00af70d4 ["CALL", null, ["callee:0047495c:8"]]
+ 00af7118 ["INT_ADD", "register:40f0:8", ["const:af7118:8", "const:4:8"]]
+ 00af7118 ["CALL", null, ["callee:0047495c:8"]]
- 00af70d4 bytes 22f6e597
+ 00af7118 bytes 11f6e597
- 00af7100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af7100 ["INT_ADD", "register:40f0:8", ["const:af7100:8", "const:4:8"]]
- 00af7100 ["CALLIND", null, ["register:0:8"]]
+ 00af7144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af7144 ["INT_ADD", "register:40f0:8", ["const:af7144:8", "const:4:8"]]
+ 00af7144 ["CALLIND", null, ["register:0:8"]]
- 00af7100 bytes 00013fd6
+ 00af7144 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f087b7384f6faa34ddd255b335da7390"></a>

### [`00af73fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md) → [`00af7440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7440.md) _ZN8firebase4util12LogExceptionEP7_JNIEnvNS_8LogLevelEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde010.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md)
- 新版 呼出元 1件 [`00bde060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde060.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af74b8",
      "incomplete_value": true,
      "site": "00af74c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af7474",
      "incomplete_value": true,
      "site": "00af7480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af7560",
      "incomplete_value": true,
      "site": "00af756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af751c",
      "incomplete_value": true,
      "site": "00af7528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af7618",
      "incomplete_value": false,
      "site": "00af7624",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af75d4",
      "incomplete_value": false,
      "site": "00af75e0",
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
            "const:ab4:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af74b8",
      "READ",
      [
        "storage",
        "010a0a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af750c",
      "READ",
      [
        "storage",
        "010a0a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00af7560",
      "READ",
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
      "00af74b8",
      "READ",
      [
        "storage",
        "010a0a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00af750c",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00af7560",
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md#insn-00af7480) · [`00af7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md#insn-00af7528) · [`00af75e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md#insn-00af75e0)
- 新版 `00af74c4`（命令位置の公開資料なし） · `00af756c`（命令位置の公開資料なし） · `00af7624`（命令位置の公開資料なし）

~~~diff
- 00af7480 ["INT_ADD", "register:40f0:8", ["const:af7480:8", "const:4:8"]]
- 00af7480 ["CALL", null, ["callee:0047495c:8"]]
+ 00af74c4 ["INT_ADD", "register:40f0:8", ["const:af74c4:8", "const:4:8"]]
+ 00af74c4 ["CALL", null, ["callee:0047495c:8"]]
- 00af7480 bytes 37f5e597
+ 00af74c4 bytes 26f5e597
- 00af7528 ["INT_ADD", "register:40f0:8", ["const:af7528:8", "const:4:8"]]
- 00af7528 ["CALL", null, ["callee:0047495c:8"]]
+ 00af756c ["INT_ADD", "register:40f0:8", ["const:af756c:8", "const:4:8"]]
+ 00af756c ["CALL", null, ["callee:0047495c:8"]]
- 00af7528 bytes 0df5e597
+ 00af756c bytes fcf4e597
- 00af75e0 ["INT_ADD", "register:40f0:8", ["const:af75e0:8", "const:4:8"]]
- 00af75e0 ["CALL", null, ["callee:00bde2d0:8"]]
+ 00af7624 ["INT_ADD", "register:40f0:8", ["const:af7624:8", "const:4:8"]]
+ 00af7624 ["CALL", null, ["callee:00bde2d0:8"]]
- 00af75e0 bytes 289b0394
+ 00af7624 bytes 2b9b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0f0541a33ccd2b924d6ee84fbd5187"></a>

### [`00af773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af773c.md) → [`00af7780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7780.md) _ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md) · 呼出先 4件 [`00af7728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7728.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bde7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7f0.md)
- 新版 呼出元 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md) · 呼出先 4件 [`00af776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af776c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bde840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af77a8",
      "incomplete_value": true,
      "site": "00af77b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af7764",
      "incomplete_value": true,
      "site": "00af776c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
              ]
            ]
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
      "definition_site": "00af77ac",
      "incomplete_value": true,
      "site": "00af77b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af7768",
      "incomplete_value": true,
      "site": "00af776c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c0:8"
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
      "definition_site": "00af77c0",
      "incomplete_value": true,
      "site": "00af77c4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af777c",
      "incomplete_value": true,
      "site": "00af7780",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "LOAD"
            ]
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
      "00af77a8",
      "READ",
      [
        "storage",
        "00c1b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00af77a8",
      "PARAM",
      [
        "storage",
        "010a0cb8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "00af77ac",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00af77a8",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "00af77a8",
      "PARAM",
      [
        "storage",
        "010a0cf8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "00af77ac",
      "READ",
      [
        "storage",
        "00c1b910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af773c.md#insn-00af776c) · [`00af7780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af773c.md#insn-00af7780) · [`00af7764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af773c.md#insn-00af7764)
- 新版 `00af77b0`（命令位置の公開資料なし） · `00af77c4`（命令位置の公開資料なし） · `00af77a8`（命令位置の公開資料なし）

~~~diff
- 00af776c ["INT_ADD", "register:40f0:8", ["const:af776c:8", "const:4:8"]]
- 00af776c ["CALL", null, ["callee:00bde840:8"]]
+ 00af77b0 ["INT_ADD", "register:40f0:8", ["const:af77b0:8", "const:4:8"]]
+ 00af77b0 ["CALL", null, ["callee:00bde840:8"]]
- 00af776c bytes 219c0394
+ 00af77b0 bytes 249c0394
- 00af7780 ["INT_ADD", "register:40f0:8", ["const:af7780:8", "const:4:8"]]
- 00af7780 ["CALL", null, ["callee:00bdb2f0:8"]]
+ 00af77c4 ["INT_ADD", "register:40f0:8", ["const:af77c4:8", "const:4:8"]]
+ 00af77c4 ["CALL", null, ["callee:00bdb2f0:8"]]
- 00af7780 bytes c88e0394
+ 00af77c4 bytes cb8e0394
- 00af7764 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8e8:8"]]
- 00af7764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af77a8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:938:8"]]
+ 00af77a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00af7764 bytes 007444f9
+ 00af77a8 bytes 009c44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9e9678397431665f2904384f4e6de0"></a>

### [`00af8818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8818.md) → [`00af885c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af885c.md) Java_com_google_firebase_app_internal_cpp_Log_nativeLog

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af88e8",
      "incomplete_value": true,
      "site": "00af88ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af88a4",
      "incomplete_value": true,
      "site": "00af88a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:534:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af88e8",
      "PARAM",
      [
        "storage",
        "00296534",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af88e8",
      "PARAM",
      [
        "storage",
        "002964a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af88a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8818.md#insn-00af88a8) · [`00af8854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8818.md#insn-00af8854) · [`00af8868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8818.md#insn-00af8868)
- 新版 `00af88ec`（命令位置の公開資料なし） · `00af8898`（命令位置の公開資料なし） · `00af88ac`（命令位置の公開資料なし）

~~~diff
- 00af88a8 ["INT_ADD", "register:40f0:8", ["const:af88a8:8", "const:4:8"]]
- 00af88a8 ["CALL", null, ["callee:00bde240:8"]]
+ 00af88ec ["INT_ADD", "register:40f0:8", ["const:af88ec:8", "const:4:8"]]
+ 00af88ec ["CALL", null, ["callee:00bde240:8"]]
- 00af88a8 bytes 52960394
+ 00af88ec bytes 55960394
- 00af8854 ["INT_ADD", "register:40f0:8", ["const:af8854:8", "const:4:8"]]
- 00af8854 ["CALL", null, ["callee:00bde0a0:8"]]
+ 00af8898 ["INT_ADD", "register:40f0:8", ["const:af8898:8", "const:4:8"]]
+ 00af8898 ["CALL", null, ["callee:00bde0a0:8"]]
- 00af8854 bytes ff950394
+ 00af8898 bytes 02960394
- 00af8868 ["INT_ADD", "register:40f0:8", ["const:af8868:8", "const:4:8"]]
- 00af8868 ["CALL", null, ["callee:00bde0a0:8"]]
+ 00af88ac ["INT_ADD", "register:40f0:8", ["const:af88ac:8", "const:4:8"]]
+ 00af88ac ["CALL", null, ["callee:00bde0a0:8"]]
- 00af8868 bytes fa950394
+ 00af88ac bytes fd950394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29230e38d542de395d1697ae91baaf07"></a>

### [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md) → [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md) · 呼出先 20件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bde8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8d0.md) · 呼出先 20件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8f38",
      "incomplete_value": false,
      "site": "00af8f38",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af8ef4",
      "incomplete_value": false,
      "site": "00af8ef4",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8fb8",
      "incomplete_value": true,
      "site": "00af8fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af8f74",
      "incomplete_value": true,
      "site": "00af8f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af8f88",
      "incomplete_value": true,
      "site": "00af8f88",
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
      "definition_site": "00af8f44",
      "incomplete_value": true,
      "site": "00af8f44",
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af8ee4",
      "PARAM",
      [
        "storage",
        "0029cdde",
        null,
        "string"
      ]
    ],
    [
      "00af8f04",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af8f28",
      "PARAM",
      [
        "storage",
        "002a4ec6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af8ee4",
      "PARAM",
      [
        "storage",
        "0029ce69",
        null,
        "string"
      ]
    ],
    [
      "00af8f04",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af8f28",
      "PARAM",
      [
        "storage",
        "002a4f51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md#insn-00af8ea4) · [`00af8ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md#insn-00af8ec8) · [`00af8ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md#insn-00af8ee8)
- 新版 `00af8ee8`（命令位置の公開資料なし） · `00af8f0c`（命令位置の公開資料なし） · `00af8f2c`（命令位置の公開資料なし）

~~~diff
- 00af8ea4 ["INT_ADD", "register:40f0:8", ["const:af8ea4:8", "const:4:8"]]
- 00af8ea4 ["CALL", null, ["callee:00bde180:8"]]
+ 00af8ee8 ["INT_ADD", "register:40f0:8", ["const:af8ee8:8", "const:4:8"]]
+ 00af8ee8 ["CALL", null, ["callee:00bde180:8"]]
- 00af8ea4 bytes a3940394
+ 00af8ee8 bytes a6940394
- 00af8ec8 ["INT_ADD", "register:40f0:8", ["const:af8ec8:8", "const:4:8"]]
- 00af8ec8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00af8f0c ["INT_ADD", "register:40f0:8", ["const:af8f0c:8", "const:4:8"]]
+ 00af8f0c ["CALL", null, ["callee:00bddc20:8"]]
- 00af8ec8 bytes 42930394
+ 00af8f0c bytes 45930394
- 00af8ee8 ["INT_ADD", "register:40f0:8", ["const:af8ee8:8", "const:4:8"]]
- 00af8ee8 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00af8f2c ["INT_ADD", "register:40f0:8", ["const:af8f2c:8", "const:4:8"]]
+ 00af8f2c ["CALL", null, ["callee:00bde9d0:8"]]
- 00af8ee8 bytes a6960394
+ 00af8f2c bytes a9960394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33c1a92cd47d573df04572369f6a49d2"></a>

### [`00af91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md) → [`00af9208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md) _ZN8firebase10app_common13FindAppByNameEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde820.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bde870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde870.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af924c",
      "incomplete_value": true,
      "site": "00af924c",
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
      "definition_site": "00af9208",
      "incomplete_value": true,
      "site": "00af9208",
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
      "definition_site": "00af92e8",
      "incomplete_value": true,
      "site": "00af92ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00af92a4",
      "incomplete_value": true,
      "site": "00af92a8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:40a0:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af923c",
      "incomplete_value": true,
      "site": "00af9240",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af91f8",
      "incomplete_value": true,
      "site": "00af91fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
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
      "00af9238",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9248",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af92e0",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af9238",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9248",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00af92e0",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af91fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md#insn-00af91fc) · [`00af9254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md#insn-00af9254) · [`00af91f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md#insn-00af91f4)
- 新版 `00af9240`（命令位置の公開資料なし） · `00af9298`（命令位置の公開資料なし） · `00af9238`（命令位置の公開資料なし）

~~~diff
- 00af91fc ["INT_ADD", "register:40f0:8", ["const:af91fc:8", "const:4:8"]]
- 00af91fc ["CALL", null, ["callee:00bddc20:8"]]
+ 00af9240 ["INT_ADD", "register:40f0:8", ["const:af9240:8", "const:4:8"]]
+ 00af9240 ["CALL", null, ["callee:00bddc20:8"]]
- 00af91fc bytes 75920394
+ 00af9240 bytes 78920394
- 00af9254 ["INT_ADD", "register:40f0:8", ["const:af9254:8", "const:4:8"]]
- 00af9254 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af9298 ["INT_ADD", "register:40f0:8", ["const:af9298:8", "const:4:8"]]
+ 00af9298 ["CALL", null, ["callee:00bdb040:8"]]
- 00af9254 bytes 67870394
+ 00af9298 bytes 6a870394
- 00af91f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00af91f4 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af9238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00af9238 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00af91f4 bytes 136146f9
+ 00af9238 bytes 138146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

