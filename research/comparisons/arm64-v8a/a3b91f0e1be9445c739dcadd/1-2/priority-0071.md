# v15.7.3 → v15.7.4 · 最優先の変更候補 (71)

[一覧の目次](README.md)

<a id="compare-d6f45e528e6b771c2a1f01772455f114"></a>

### [`00b61a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md) → [`00b61ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b61af0",
      "incomplete_value": true,
      "site": "00b61af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61aac",
      "incomplete_value": true,
      "site": "00b61aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61ad8",
      "incomplete_value": true,
      "site": "00b61ad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61a94",
      "incomplete_value": true,
      "site": "00b61a94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61ae4",
      "incomplete_value": true,
      "site": "00b61ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61aa0",
      "incomplete_value": true,
      "site": "00b61aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:534:8"
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
      "00b61ad4",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ae4",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61af0",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61ad4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ae4",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61af0",
      "WRITE",
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

- 旧版 [`00b61aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md#insn-00b61aa4) · [`00b61aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md#insn-00b61aac) · [`00b61a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md#insn-00b61a90)
- 新版 [`00b61ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61ae8) · [`00b61af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61af0) · [`00b61ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61ad4)

~~~diff
- 00b61aa4 ["INT_ADD", "register:40f0:8", ["const:b61aa4:8", "const:4:8"]]
- 00b61aa4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61ae8 ["INT_ADD", "register:40f0:8", ["const:b61ae8:8", "const:4:8"]]
+ 00b61ae8 ["CALL", null, ["callee:00bde090:8"]]
- 00b61aa4 bytes 67f10194
+ 00b61ae8 bytes 6af10194
- 00b61aac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61aac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61af0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61aac bytes 60d202f9
+ 00b61af0 bytes 60f202f9
- 00b61a90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61a90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61ad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61ad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61a90 bytes 68d242f9
+ 00b61ad4 bytes 68f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96eb27bb1ac0e68f8f762b0d6eb0c2c2"></a>

### [`00b61ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md) → [`00b61b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b04.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b61b30",
      "incomplete_value": true,
      "site": "00b61b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61aec",
      "incomplete_value": true,
      "site": "00b61aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61b18",
      "incomplete_value": true,
      "site": "00b61b18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ad4",
      "incomplete_value": true,
      "site": "00b61ad4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61b20",
      "incomplete_value": false,
      "site": "00b61b28",
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
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61adc",
      "incomplete_value": false,
      "site": "00b61ae4",
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
            "const:534:8"
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
      "00b61b14",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b20",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61b30",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61b14",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b20",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61b30",
      "WRITE",
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

- 旧版 [`00b61ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61ae4) · [`00b61aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61aec) · [`00b61ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61ad0)
- 新版 [`00b61b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b04.md#insn-00b61b28) · [`00b61b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b04.md#insn-00b61b30) · [`00b61b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b04.md#insn-00b61b14)

~~~diff
- 00b61ae4 ["INT_ADD", "register:40f0:8", ["const:b61ae4:8", "const:4:8"]]
- 00b61ae4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61b28 ["INT_ADD", "register:40f0:8", ["const:b61b28:8", "const:4:8"]]
+ 00b61b28 ["CALL", null, ["callee:00bde090:8"]]
- 00b61ae4 bytes 57f10194
+ 00b61b28 bytes 5af10194
- 00b61aec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61b30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61aec bytes 60d202f9
+ 00b61b30 bytes 60f202f9
- 00b61ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61ad0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61ad0 bytes 68d242f9
+ 00b61b14 bytes 68f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cabcd33507b50d5b84f0bd0761be1c5"></a>

### [`00b61b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md) → [`00b61b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b61b74",
      "incomplete_value": true,
      "site": "00b61b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b30",
      "incomplete_value": true,
      "site": "00b61b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61b58",
      "incomplete_value": true,
      "site": "00b61b58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b14",
      "incomplete_value": true,
      "site": "00b61b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61b64",
      "incomplete_value": false,
      "site": "00b61b6c",
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
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b20",
      "incomplete_value": false,
      "site": "00b61b28",
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
            "const:534:8"
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
      "00b61b54",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b64",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61b74",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61b54",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b64",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61b74",
      "WRITE",
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

- 旧版 [`00b61b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md#insn-00b61b28) · [`00b61b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md#insn-00b61b30) · [`00b61b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md#insn-00b61b10)
- 新版 [`00b61b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b6c) · [`00b61b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b74) · [`00b61b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b54)

~~~diff
- 00b61b28 ["INT_ADD", "register:40f0:8", ["const:b61b28:8", "const:4:8"]]
- 00b61b28 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61b6c ["INT_ADD", "register:40f0:8", ["const:b61b6c:8", "const:4:8"]]
+ 00b61b6c ["CALL", null, ["callee:00bde090:8"]]
- 00b61b28 bytes 46f10194
+ 00b61b6c bytes 49f10194
- 00b61b30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61b30 bytes 60d202f9
+ 00b61b74 bytes 60f202f9
- 00b61b10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61b10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61b10 bytes 68d242f9
+ 00b61b54 bytes 68f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d3a4e6273a23e01d74c61034ba21e9b"></a>

### [`00b61b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md) → [`00b61b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61bb8",
      "incomplete_value": true,
      "site": "00b61bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b74",
      "incomplete_value": true,
      "site": "00b61b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61b9c",
      "incomplete_value": true,
      "site": "00b61b9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b58",
      "incomplete_value": true,
      "site": "00b61b58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61ba4",
      "incomplete_value": true,
      "site": "00b61bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b60",
      "incomplete_value": true,
      "site": "00b61b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:534:8"
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
      "00b61b98",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ba4",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61bb8",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61b98",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ba4",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61bb8",
      "WRITE",
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

- 旧版 [`00b61b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md#insn-00b61b6c) · [`00b61b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md#insn-00b61b74) · [`00b61b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md#insn-00b61b54)
- 新版 [`00b61bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61bb0) · [`00b61bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61bb8) · [`00b61b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61b98)

~~~diff
- 00b61b6c ["INT_ADD", "register:40f0:8", ["const:b61b6c:8", "const:4:8"]]
- 00b61b6c ["CALL", null, ["callee:00bde090:8"]]
+ 00b61bb0 ["INT_ADD", "register:40f0:8", ["const:b61bb0:8", "const:4:8"]]
+ 00b61bb0 ["CALL", null, ["callee:00bde090:8"]]
- 00b61b6c bytes 35f10194
+ 00b61bb0 bytes 38f10194
- 00b61b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61b74 bytes 60d202f9
+ 00b61bb8 bytes 60f202f9
- 00b61b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
+ 00b61b98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61b54 bytes 68d242f9
+ 00b61b98 bytes 68f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0d2adcf42f9741bcb51f808202ca90c"></a>

### [`00b61b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b88.md) → [`00b61bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bcc.md) _ZN8firebase4auth15email_exception8GetClassEv

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
      "definition_site": "00b61bd0",
      "incomplete_value": true,
      "site": "00b61bd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b8c",
      "incomplete_value": true,
      "site": "00b61b90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5a0:8"
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
      "00b61bd0",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61bd0",
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

- 旧版 [`00b61b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b88.md#insn-00b61b8c)
- 新版 [`00b61bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bcc.md#insn-00b61bd0)

~~~diff
- 00b61b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a0:8"]]
- 00b61b8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61bd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
+ 00b61bd0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61b8c bytes 00d142f9
+ 00b61bd0 bytes 00f142f9
~~~


<a id="compare-e96cc22e1f8102c0bc3f675596df1e70"></a>

### [`00b61b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md) → [`00b61bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md) _ZN8firebase4auth15email_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b61c30",
      "incomplete_value": true,
      "site": "00b61c30",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61bec",
      "incomplete_value": true,
      "site": "00b61bec",
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
            "const:5a8:8"
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
      "definition_site": "00b61c0c",
      "incomplete_value": true,
      "site": "00b61c18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61bc8",
      "incomplete_value": true,
      "site": "00b61bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a0:8"
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
      "00b61bec",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61c0c",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c30",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61bec",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61c0c",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c30",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61ba8) · [`00b61bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61bd4) · [`00b61bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61bec)
- 新版 [`00b61bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61bec) · [`00b61c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61c18) · [`00b61c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61c30)

~~~diff
- 00b61ba8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
- 00b61ba8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61ba8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61bec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5e8:8"]]
+ 00b61bec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61bec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61ba8 bytes a8a25639
+ 00b61bec bytes a8a25739
- 00b61bd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61bd4 ["INT_ADD", "register:40f0:8", ["const:b61bd4:8", "const:4:8"]]
- 00b61bd4 ["CALLIND", null, ["register:0:8"]]
+ 00b61c18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61c18 ["INT_ADD", "register:40f0:8", ["const:b61c18:8", "const:4:8"]]
+ 00b61c18 ["CALLIND", null, ["register:0:8"]]
- 00b61bd4 bytes 00013fd6
+ 00b61c18 bytes 00013fd6
- 00b61bec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61bec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
- 00b61bec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b61c30 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b61c30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5e8:8"]]
+ 00b61c30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61bec bytes a0a21639
+ 00b61c30 bytes a0a21739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1470074803b48d49c826d28a2d331c"></a>

### [`00b61c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c00.md) → [`00b61c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md) _ZN8firebase4auth15email_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b61c80",
      "incomplete_value": true,
      "site": "00b61c80",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c3c",
      "incomplete_value": true,
      "site": "00b61c3c",
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
            "const:5a8:8"
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
      "definition_site": "00b61ca0",
      "incomplete_value": true,
      "site": "00b61ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c5c",
      "incomplete_value": true,
      "site": "00b61c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61c5c",
      "incomplete_value": true,
      "site": "00b61c5c",
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
      "definition_site": "00b61c18",
      "incomplete_value": true,
      "site": "00b61c18",
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
      "00b61c58",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c64",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61c80",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61c58",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c64",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61c80",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c00.md#insn-00b61c14) · [`00b61c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c00.md#insn-00b61c3c) · [`00b61c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c00.md#insn-00b61c58)
- 新版 [`00b61c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c58) · [`00b61c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c80) · [`00b61c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c9c)

~~~diff
- 00b61c14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61c14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61c58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b61c58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61c14 bytes 81d242f9
+ 00b61c58 bytes 81f242f9
- 00b61c3c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61c3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61c3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
- 00b61c3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b61c80 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b61c80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b61c80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5e8:8"]]
+ 00b61c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61c3c bytes bfa21639
+ 00b61c80 bytes bfa21739
- 00b61c58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61c58 ["INT_ADD", "register:40f0:8", ["const:b61c58:8", "const:4:8"]]
- 00b61c58 ["CALLIND", null, ["register:0:8"]]
+ 00b61c9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61c9c ["INT_ADD", "register:40f0:8", ["const:b61c9c:8", "const:4:8"]]
+ 00b61c9c ["CALLIND", null, ["register:0:8"]]
- 00b61c58 bytes 00013fd6
+ 00b61c9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0fdb2d05c08c4a0116ac5957022894"></a>

### [`00b61c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md) → [`00b61cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md) _ZN8firebase4auth15email_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61cf4",
      "incomplete_value": true,
      "site": "00b61cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61cb0",
      "incomplete_value": true,
      "site": "00b61cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61cd0",
      "incomplete_value": true,
      "site": "00b61cd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c8c",
      "incomplete_value": true,
      "site": "00b61c8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61cd8",
      "incomplete_value": false,
      "site": "00b61cec",
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
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c94",
      "incomplete_value": false,
      "site": "00b61ca8",
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
            "const:534:8"
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
      "00b61cc8",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61cd8",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61cf4",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61cc8",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61cd8",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61cf4",
      "WRITE",
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

- 旧版 [`00b61ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md#insn-00b61ca8) · [`00b61cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md#insn-00b61cb0) · [`00b61c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md#insn-00b61c84)
- 新版 [`00b61cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cec) · [`00b61cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cf4) · [`00b61cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cc8)

~~~diff
- 00b61ca8 ["INT_ADD", "register:40f0:8", ["const:b61ca8:8", "const:4:8"]]
- 00b61ca8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61cec ["INT_ADD", "register:40f0:8", ["const:b61cec:8", "const:4:8"]]
+ 00b61cec ["CALL", null, ["callee:00bde090:8"]]
- 00b61ca8 bytes e6f00194
+ 00b61cec bytes e9f00194
- 00b61cb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61cf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b61cf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61cb0 bytes 80d202f9
+ 00b61cf4 bytes 80f202f9
- 00b61c84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61c84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61cc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b61cc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61c84 bytes 81d242f9
+ 00b61cc8 bytes 81f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf8726e79f1584a8e7a666a78fac7547"></a>

### [`00b61ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md) → [`00b61d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d24.md) _ZN8firebase4auth15email_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b61d40",
      "incomplete_value": true,
      "site": "00b61d44",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61cfc",
      "incomplete_value": true,
      "site": "00b61d00",
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
      "definition_site": "00b61d50",
      "incomplete_value": true,
      "site": "00b61d5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61d0c",
      "incomplete_value": true,
      "site": "00b61d18",
      "value": [
        "LOAD",
        "8",
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
      "00b61d40",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b61d50",
      "DATA",
      [
        "storage",
        "010a15b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61d40",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b61d50",
      "DATA",
      [
        "storage",
        "010a15f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md#insn-00b61d00) · [`00b61cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md#insn-00b61cfc) · [`00b61d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md#insn-00b61d08)
- 新版 [`00b61d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d24.md#insn-00b61d44) · [`00b61d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d24.md#insn-00b61d40) · [`00b61d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d24.md#insn-00b61d4c)

~~~diff
- 00b61d00 ["INT_ADD", "register:40f0:8", ["const:b61d00:8", "const:4:8"]]
- 00b61d00 ["CALL", null, ["callee:00bde180:8"]]
+ 00b61d44 ["INT_ADD", "register:40f0:8", ["const:b61d44:8", "const:4:8"]]
+ 00b61d44 ["CALL", null, ["callee:00bde180:8"]]
- 00b61d00 bytes 0cf10194
+ 00b61d44 bytes 0ff10194
- 00b61cfc ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b61cfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61cfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61cfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61d40 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b61d40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61d40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61d40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61cfc bytes 00501791
+ 00b61d40 bytes 001c1591
- 00b61d08 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00b61d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61d4c ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00b61d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61d08 bytes 08c11691
+ 00b61d4c bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ffb850ae920123ae5fbad6c505cb591"></a>

### [`00b61d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md) → [`00b61d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md) _ZN8firebase4auth15email_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61da0",
      "incomplete_value": true,
      "site": "00b61da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61d5c",
      "incomplete_value": true,
      "site": "00b61d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00b61d7c",
      "incomplete_value": true,
      "site": "00b61d7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61d38",
      "incomplete_value": true,
      "site": "00b61d38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61d84",
      "incomplete_value": false,
      "site": "00b61d98",
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
            "const:4a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61d40",
      "incomplete_value": false,
      "site": "00b61d54",
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
            "const:534:8"
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
      "00b61d74",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61d84",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61da0",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61d74",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61d84",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61da0",
      "WRITE",
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

- 旧版 [`00b61d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md#insn-00b61d54) · [`00b61d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md#insn-00b61d5c) · [`00b61d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md#insn-00b61d30)
- 新版 [`00b61d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61d98) · [`00b61da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61da0) · [`00b61d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61d74)

~~~diff
- 00b61d54 ["INT_ADD", "register:40f0:8", ["const:b61d54:8", "const:4:8"]]
- 00b61d54 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61d98 ["INT_ADD", "register:40f0:8", ["const:b61d98:8", "const:4:8"]]
+ 00b61d98 ["CALL", null, ["callee:00bde090:8"]]
- 00b61d54 bytes bbf00194
+ 00b61d98 bytes bef00194
- 00b61d5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61da0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b61da0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61d5c bytes 80d202f9
+ 00b61da0 bytes 80f202f9
- 00b61d30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61d30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61d74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b61d74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61d30 bytes 81d242f9
+ 00b61d74 bytes 81f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05fcea9c7666dc7b11ec2e6cf2a5bf11"></a>

### [`00b61d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d8c.md) → [`00b61dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61dd0.md) _ZN8firebase4auth15email_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b61dfc",
      "incomplete_value": true,
      "site": "00b61e08",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61db8",
      "incomplete_value": true,
      "site": "00b61dc4",
      "value": [
        "LOAD",
        "8",
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
      "00b61dec",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61dfc",
      "DATA",
      [
        "storage",
        "010a15b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61dec",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b61dfc",
      "DATA",
      [
        "storage",
        "010a15f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d8c.md#insn-00b61da8) · [`00b61dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d8c.md#insn-00b61dac) · [`00b61db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d8c.md#insn-00b61db4)
- 新版 [`00b61dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61dd0.md#insn-00b61dec) · [`00b61df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61dd0.md#insn-00b61df0) · [`00b61df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61dd0.md#insn-00b61df8)

~~~diff
- 00b61da8 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b61da8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61da8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61da8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61dec ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b61dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61da8 bytes 00fc1991
+ 00b61dec bytes 00c81791
- 00b61dac ["INT_ADD", "register:40f0:8", ["const:b61dac:8", "const:4:8"]]
- 00b61dac ["CALL", null, ["callee:00bde180:8"]]
+ 00b61df0 ["INT_ADD", "register:40f0:8", ["const:b61df0:8", "const:4:8"]]
+ 00b61df0 ["CALL", null, ["callee:00bde180:8"]]
- 00b61dac bytes e1f00194
+ 00b61df0 bytes e4f00194
- 00b61db4 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00b61db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61df8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00b61df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61db4 bytes 08e11691
+ 00b61df8 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a6150e27ebc596d9700327e5f1df3d4"></a>

### [`00b61dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md) → [`00b61e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b61e38",
      "incomplete_value": true,
      "site": "00b61e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61df4",
      "incomplete_value": true,
      "site": "00b61df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b61e20",
      "incomplete_value": true,
      "site": "00b61e20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ddc",
      "incomplete_value": true,
      "site": "00b61ddc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61e2c",
      "incomplete_value": false,
      "site": "00b61e30",
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
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61de8",
      "incomplete_value": false,
      "site": "00b61dec",
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
            "const:8c:8"
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
      "00b61e1c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e2c",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61e38",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61e1c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e2c",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b61e38",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61dec) · [`00b61df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61df4) · [`00b61dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61dd8)
- 新版 [`00b61e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e30) · [`00b61e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e38) · [`00b61e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e1c)

~~~diff
- 00b61dec ["INT_ADD", "register:40f0:8", ["const:b61dec:8", "const:4:8"]]
- 00b61dec ["CALL", null, ["callee:00bde090:8"]]
+ 00b61e30 ["INT_ADD", "register:40f0:8", ["const:b61e30:8", "const:4:8"]]
+ 00b61e30 ["CALL", null, ["callee:00bde090:8"]]
- 00b61dec bytes 95f00194
+ 00b61e30 bytes 98f00194
- 00b61df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61df4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61df4 bytes 60e202f9
+ 00b61e38 bytes 600203f9
- 00b61dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61e1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61dd8 bytes 68e242f9
+ 00b61e1c bytes 680243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a5cda661ed9bf07e36cdae4591a415"></a>

### [`00b61e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md) → [`00b61e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b61e78",
      "incomplete_value": true,
      "site": "00b61e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e34",
      "incomplete_value": true,
      "site": "00b61e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b61e60",
      "incomplete_value": true,
      "site": "00b61e60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e1c",
      "incomplete_value": true,
      "site": "00b61e1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61e68",
      "incomplete_value": false,
      "site": "00b61e70",
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
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e24",
      "incomplete_value": false,
      "site": "00b61e2c",
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
            "const:8c:8"
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
      "00b61e5c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e68",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61e78",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61e5c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e68",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b61e78",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e2c) · [`00b61e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e34) · [`00b61e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e18)
- 新版 [`00b61e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e70) · [`00b61e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e78) · [`00b61e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e5c)

~~~diff
- 00b61e2c ["INT_ADD", "register:40f0:8", ["const:b61e2c:8", "const:4:8"]]
- 00b61e2c ["CALL", null, ["callee:00bde090:8"]]
+ 00b61e70 ["INT_ADD", "register:40f0:8", ["const:b61e70:8", "const:4:8"]]
+ 00b61e70 ["CALL", null, ["callee:00bde090:8"]]
- 00b61e2c bytes 85f00194
+ 00b61e70 bytes 88f00194
- 00b61e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61e34 bytes 60e202f9
+ 00b61e78 bytes 600203f9
- 00b61e18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61e18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61e5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61e18 bytes 68e242f9
+ 00b61e5c bytes 680243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aee34e60d80bcb6905f32d66c7edd9a8"></a>

### [`00b61e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md) → [`00b61e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e8c.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b61ebc",
      "incomplete_value": true,
      "site": "00b61ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e78",
      "incomplete_value": true,
      "site": "00b61e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b61ea0",
      "incomplete_value": true,
      "site": "00b61ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e5c",
      "incomplete_value": true,
      "site": "00b61e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61eac",
      "incomplete_value": false,
      "site": "00b61eb4",
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
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e68",
      "incomplete_value": false,
      "site": "00b61e70",
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
            "const:8c:8"
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
      "00b61e9c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61eac",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61ebc",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61e9c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61eac",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b61ebc",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md#insn-00b61e70) · [`00b61e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md#insn-00b61e78) · [`00b61e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md#insn-00b61e58)
- 新版 [`00b61eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e8c.md#insn-00b61eb4) · [`00b61ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e8c.md#insn-00b61ebc) · [`00b61e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e8c.md#insn-00b61e9c)

~~~diff
- 00b61e70 ["INT_ADD", "register:40f0:8", ["const:b61e70:8", "const:4:8"]]
- 00b61e70 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61eb4 ["INT_ADD", "register:40f0:8", ["const:b61eb4:8", "const:4:8"]]
+ 00b61eb4 ["CALL", null, ["callee:00bde090:8"]]
- 00b61e70 bytes 74f00194
+ 00b61eb4 bytes 77f00194
- 00b61e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61ebc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61e78 bytes 60e202f9
+ 00b61ebc bytes 600203f9
- 00b61e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61e58 bytes 68e242f9
+ 00b61e9c bytes 680243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-322b5d0461ae95078032d3b5f5841b68"></a>

### [`00b61e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md) → [`00b61ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61f00",
      "incomplete_value": true,
      "site": "00b61f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ebc",
      "incomplete_value": true,
      "site": "00b61ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b61ee4",
      "incomplete_value": true,
      "site": "00b61ee4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ea0",
      "incomplete_value": true,
      "site": "00b61ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61eec",
      "incomplete_value": false,
      "site": "00b61ef8",
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
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ea8",
      "incomplete_value": false,
      "site": "00b61eb4",
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
            "const:8c:8"
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
      "00b61ee0",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61eec",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61f00",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61ee0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61eec",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b61f00",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61eb4) · [`00b61ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61ebc) · [`00b61e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61e9c)
- 新版 [`00b61ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61ef8) · [`00b61f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61f00) · [`00b61ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61ee0)

~~~diff
- 00b61eb4 ["INT_ADD", "register:40f0:8", ["const:b61eb4:8", "const:4:8"]]
- 00b61eb4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61ef8 ["INT_ADD", "register:40f0:8", ["const:b61ef8:8", "const:4:8"]]
+ 00b61ef8 ["CALL", null, ["callee:00bde090:8"]]
- 00b61eb4 bytes 63f00194
+ 00b61ef8 bytes 66f00194
- 00b61ebc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61f00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61f00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61ebc bytes 60e202f9
+ 00b61f00 bytes 600203f9
- 00b61e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61ee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b61ee0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61e9c bytes 68e242f9
+ 00b61ee0 bytes 680243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11521505d708501e86c811b4a23b1485"></a>

### [`00b61edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md) → [`00b61f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md) _ZN8firebase4auth23weak_password_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b61f78",
      "incomplete_value": true,
      "site": "00b61f78",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61f34",
      "incomplete_value": true,
      "site": "00b61f34",
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
            "const:5c8:8"
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
      "definition_site": "00b61f54",
      "incomplete_value": true,
      "site": "00b61f60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:600:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61f10",
      "incomplete_value": true,
      "site": "00b61f1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
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
      "00b61f34",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f54",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f78",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61f34",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f54",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f78",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61ef0) · [`00b61f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61f1c) · [`00b61f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61f34)
- 新版 [`00b61f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f34) · [`00b61f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f60) · [`00b61f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f78)

~~~diff
- 00b61ef0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
- 00b61ef0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61ef0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61f34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:608:8"]]
+ 00b61f34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61f34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61ef0 bytes a8225739
+ 00b61f34 bytes a8225839
- 00b61f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61f1c ["INT_ADD", "register:40f0:8", ["const:b61f1c:8", "const:4:8"]]
- 00b61f1c ["CALLIND", null, ["register:0:8"]]
+ 00b61f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61f60 ["INT_ADD", "register:40f0:8", ["const:b61f60:8", "const:4:8"]]
+ 00b61f60 ["CALLIND", null, ["register:0:8"]]
- 00b61f1c bytes 00013fd6
+ 00b61f60 bytes 00013fd6
- 00b61f34 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61f34 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
- 00b61f34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b61f78 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b61f78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:608:8"]]
+ 00b61f78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61f34 bytes a0221739
+ 00b61f78 bytes a0221839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec70e5f5b810669971468e271f6ffae6"></a>

### [`00b61f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md) → [`00b61f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md) _ZN8firebase4auth23weak_password_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b61fc8",
      "incomplete_value": true,
      "site": "00b61fc8",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61f84",
      "incomplete_value": true,
      "site": "00b61f84",
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
            "const:5c8:8"
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
      "definition_site": "00b61fe8",
      "incomplete_value": true,
      "site": "00b61fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61fa4",
      "incomplete_value": true,
      "site": "00b61fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b61fa4",
      "incomplete_value": true,
      "site": "00b61fa4",
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
      "definition_site": "00b61f60",
      "incomplete_value": true,
      "site": "00b61f60",
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
      "00b61fa0",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61fac",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61fc8",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61fa0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61fac",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61fc8",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md#insn-00b61f5c) · [`00b61f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md#insn-00b61f84) · [`00b61fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md#insn-00b61fa0)
- 新版 [`00b61fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fa0) · [`00b61fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fc8) · [`00b61fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fe4)

~~~diff
- 00b61f5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b61f5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61fa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
+ 00b61fa0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61f5c bytes 81e242f9
+ 00b61fa0 bytes 810243f9
- 00b61f84 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61f84 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61f84 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
- 00b61f84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b61fc8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b61fc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b61fc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
+ 00b61fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61f84 bytes bf221739
+ 00b61fc8 bytes bf221839
- 00b61fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61fa0 ["INT_ADD", "register:40f0:8", ["const:b61fa0:8", "const:4:8"]]
- 00b61fa0 ["CALLIND", null, ["register:0:8"]]
+ 00b61fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61fe4 ["INT_ADD", "register:40f0:8", ["const:b61fe4:8", "const:4:8"]]
+ 00b61fe4 ["CALLIND", null, ["register:0:8"]]
- 00b61fa0 bytes 00013fd6
+ 00b61fe4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6308ca977ad78ecefcdfed4cdfa0bda0"></a>

### [`00b61fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md) → [`00b61ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md) _ZN8firebase4auth23weak_password_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6203c",
      "incomplete_value": true,
      "site": "00b6203c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61ff8",
      "incomplete_value": true,
      "site": "00b61ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b62018",
      "incomplete_value": true,
      "site": "00b62018",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61fd4",
      "incomplete_value": true,
      "site": "00b61fd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62020",
      "incomplete_value": false,
      "site": "00b62034",
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
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61fdc",
      "incomplete_value": false,
      "site": "00b61ff0",
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
            "const:8c:8"
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
      "00b62010",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62020",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b6203c",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62010",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62020",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b6203c",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61ff0) · [`00b61ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61ff8) · [`00b61fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61fcc)
- 新版 [`00b62034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b62034) · [`00b6203c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b6203c) · [`00b62010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b62010)

~~~diff
- 00b61ff0 ["INT_ADD", "register:40f0:8", ["const:b61ff0:8", "const:4:8"]]
- 00b61ff0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62034 ["INT_ADD", "register:40f0:8", ["const:b62034:8", "const:4:8"]]
+ 00b62034 ["CALL", null, ["callee:00bde090:8"]]
- 00b61ff0 bytes 14f00194
+ 00b62034 bytes 17f00194
- 00b61ff8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b61ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6203c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
+ 00b6203c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61ff8 bytes 80e202f9
+ 00b6203c bytes 800203f9
- 00b61fcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b61fcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
+ 00b62010 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61fcc bytes 81e242f9
+ 00b62010 bytes 810243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b3b8e534e24068c47c18eb8203bcc5e"></a>

### [`00b62028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md) → [`00b6206c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md) _ZN8firebase4auth23weak_password_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62088",
      "incomplete_value": false,
      "site": "00b6208c",
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
      "definition_site": "00b62044",
      "incomplete_value": false,
      "site": "00b62048",
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
      "definition_site": "00b62098",
      "incomplete_value": true,
      "site": "00b620a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62054",
      "incomplete_value": true,
      "site": "00b62060",
      "value": [
        "LOAD",
        "8",
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
      "00b62088",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62098",
      "DATA",
      [
        "storage",
        "010a15d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62088",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62098",
      "DATA",
      [
        "storage",
        "010a1610",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62048) · [`00b62044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62044) · [`00b62050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62050)
- 新版 [`00b6208c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b6208c) · [`00b62088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b62088) · [`00b62094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b62094)

~~~diff
- 00b62048 ["INT_ADD", "register:40f0:8", ["const:b62048:8", "const:4:8"]]
- 00b62048 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6208c ["INT_ADD", "register:40f0:8", ["const:b6208c:8", "const:4:8"]]
+ 00b6208c ["CALL", null, ["callee:00bde180:8"]]
- 00b62048 bytes 3af00194
+ 00b6208c bytes 3df00194
- 00b62044 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b62044 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62044 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62044 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62088 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b62088 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62088 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62088 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62044 bytes 00501791
+ 00b62088 bytes 001c1591
- 00b62050 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00b62050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62094 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 00b62094 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62094 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62094 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62050 bytes 08411791
+ 00b62094 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccfb8df0e564dc3ee9f59eb7488166f"></a>

### [`00b62064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62064.md) → [`00b620a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md) _ZN8firebase4auth23weak_password_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b620e8",
      "incomplete_value": true,
      "site": "00b620e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b620a4",
      "incomplete_value": true,
      "site": "00b620a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "definition_site": "00b620c4",
      "incomplete_value": true,
      "site": "00b620c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62080",
      "incomplete_value": true,
      "site": "00b62080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b620cc",
      "incomplete_value": true,
      "site": "00b620e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:117:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62088",
      "incomplete_value": true,
      "site": "00b6209c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:8c:8"
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
      "00b620bc",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b620cc",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b620e8",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b620bc",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b620cc",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00b620e8",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6209c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62064.md#insn-00b6209c) · [`00b620a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62064.md#insn-00b620a4) · [`00b62078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62064.md#insn-00b62078)
- 新版 [`00b620e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620e0) · [`00b620e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620e8) · [`00b620bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620bc)

~~~diff
- 00b6209c ["INT_ADD", "register:40f0:8", ["const:b6209c:8", "const:4:8"]]
- 00b6209c ["CALL", null, ["callee:00bde090:8"]]
+ 00b620e0 ["INT_ADD", "register:40f0:8", ["const:b620e0:8", "const:4:8"]]
+ 00b620e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6209c bytes e9ef0194
+ 00b620e0 bytes ecef0194
- 00b620a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b620a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b620e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
+ 00b620e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b620a4 bytes 80e202f9
+ 00b620e8 bytes 800203f9
- 00b62078 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b62078 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b620bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
+ 00b620bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62078 bytes 81e242f9
+ 00b620bc bytes 810243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e671d29c53ad1727fb0b5ad1139befab"></a>

### [`00b620d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b620d4.md) → [`00b62118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62118.md) _ZN8firebase4auth23weak_password_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b62134",
      "incomplete_value": true,
      "site": "00b62138",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b620f0",
      "incomplete_value": true,
      "site": "00b620f4",
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
      "definition_site": "00b62144",
      "incomplete_value": true,
      "site": "00b62150",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62100",
      "incomplete_value": true,
      "site": "00b6210c",
      "value": [
        "LOAD",
        "8",
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
      "00b62134",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b62144",
      "DATA",
      [
        "storage",
        "010a15d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62134",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b62144",
      "DATA",
      [
        "storage",
        "010a1618",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b620f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b620d4.md#insn-00b620f4) · [`00b620f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b620d4.md#insn-00b620f0) · [`00b620fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b620d4.md#insn-00b620fc)
- 新版 [`00b62138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62118.md#insn-00b62138) · [`00b62134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62118.md#insn-00b62134) · [`00b62140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62118.md#insn-00b62140)

~~~diff
- 00b620f4 ["INT_ADD", "register:40f0:8", ["const:b620f4:8", "const:4:8"]]
- 00b620f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b62138 ["INT_ADD", "register:40f0:8", ["const:b62138:8", "const:4:8"]]
+ 00b62138 ["CALL", null, ["callee:00bde180:8"]]
- 00b620f4 bytes 0ff00194
+ 00b62138 bytes 12f00194
- 00b620f0 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b620f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b620f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b620f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62134 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b62134 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62134 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62134 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b620f0 bytes 00fc1991
+ 00b62134 bytes 00c81791
- 00b620fc ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00b620fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b620fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b620fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62140 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00b62140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b620fc bytes 08611791
+ 00b62140 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1cd152f64afcb484367555e35c2e41"></a>

### [`00b62110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62110.md) → [`00b62154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "definition_site": "00b62180",
      "incomplete_value": true,
      "site": "00b62180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6213c",
      "incomplete_value": true,
      "site": "00b6213c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b62168",
      "incomplete_value": true,
      "site": "00b62168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62124",
      "incomplete_value": true,
      "site": "00b62124",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62124"
      ],
      [
        "FALL_THROUGH",
        "00b62168"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62168",
      "incomplete_value": true,
      "site": "00b62180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62124",
      "incomplete_value": true,
      "site": "00b6213c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62164",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62174",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62180",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62164",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62174",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b62180",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62110.md#insn-00b6213c) · [`00b62120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62110.md#insn-00b62120) · [`00b62130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62110.md#insn-00b62130)
- 新版 [`00b62180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62180) · [`00b62164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62164) · [`00b62174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62174)

~~~diff
- 00b6213c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b6213c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6213c bytes 60f202f9
+ 00b62180 bytes 601203f9
- 00b62120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b62120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62120 bytes 68f242f9
+ 00b62164 bytes 681243f9
- 00b62130 ["COPY", "tmp:0:8", ["const:f1d:8"]]
- 00b62130 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b62130 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b62130 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b62174 ["COPY", "tmp:0:8", ["const:fb7:8"]]
+ 00b62174 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62174 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62174 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b62130 bytes 63743c91
+ 00b62174 bytes 63dc3e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8c8092de4e946112933474486bdeae"></a>

### [`00b62150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md) → [`00b62194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

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
      "definition_site": "00b621c0",
      "incomplete_value": true,
      "site": "00b621c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6217c",
      "incomplete_value": true,
      "site": "00b6217c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b621a8",
      "incomplete_value": true,
      "site": "00b621a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62164",
      "incomplete_value": true,
      "site": "00b62164",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b621b0",
      "incomplete_value": false,
      "site": "00b621b8",
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
            "const:fb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6216c",
      "incomplete_value": false,
      "site": "00b62174",
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
            "const:f1d:8"
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
      "00b621a4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621b0",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b621c0",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b621a4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621b0",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b621c0",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md#insn-00b62174) · [`00b6217c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md#insn-00b6217c) · [`00b62160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md#insn-00b62160)
- 新版 [`00b621b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b621b8) · [`00b621c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b621c0) · [`00b621a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b621a4)

~~~diff
- 00b62174 ["INT_ADD", "register:40f0:8", ["const:b62174:8", "const:4:8"]]
- 00b62174 ["CALL", null, ["callee:00bde090:8"]]
+ 00b621b8 ["INT_ADD", "register:40f0:8", ["const:b621b8:8", "const:4:8"]]
+ 00b621b8 ["CALL", null, ["callee:00bde090:8"]]
- 00b62174 bytes b3ef0194
+ 00b621b8 bytes b6ef0194
- 00b6217c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b6217c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b621c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b621c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6217c bytes 60f202f9
+ 00b621c0 bytes 601203f9
- 00b62160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b62160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b621a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b621a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62160 bytes 68f242f9
+ 00b621a4 bytes 681243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57428a6f5bbe9ae3631f7619f5e82b6"></a>

### [`00b62190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62190.md) → [`00b621d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62204",
      "incomplete_value": true,
      "site": "00b62204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621c0",
      "incomplete_value": true,
      "site": "00b621c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b621e8",
      "incomplete_value": true,
      "site": "00b621e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621a4",
      "incomplete_value": true,
      "site": "00b621a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b621f4",
      "incomplete_value": false,
      "site": "00b621fc",
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
            "const:fb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621b0",
      "incomplete_value": false,
      "site": "00b621b8",
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
            "const:f1d:8"
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
      "00b621e4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621f4",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62204",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b621e4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621f4",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b62204",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b621b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62190.md#insn-00b621b8) · [`00b621c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62190.md#insn-00b621c0) · [`00b621a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62190.md#insn-00b621a0)
- 新版 [`00b621fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b621fc) · [`00b62204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b62204) · [`00b621e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b621e4)

~~~diff
- 00b621b8 ["INT_ADD", "register:40f0:8", ["const:b621b8:8", "const:4:8"]]
- 00b621b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b621fc ["INT_ADD", "register:40f0:8", ["const:b621fc:8", "const:4:8"]]
+ 00b621fc ["CALL", null, ["callee:00bde090:8"]]
- 00b621b8 bytes a2ef0194
+ 00b621fc bytes a5ef0194
- 00b621c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b621c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62204 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b621c0 bytes 60f202f9
+ 00b62204 bytes 601203f9
- 00b621a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b621a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b621e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b621e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b621a0 bytes 68f242f9
+ 00b621e4 bytes 681243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d03b067e1d952fa38c5d5a5ff42cb64"></a>

### [`00b621d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md) → [`00b62218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62248",
      "incomplete_value": true,
      "site": "00b62248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62204",
      "incomplete_value": true,
      "site": "00b62204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b6222c",
      "incomplete_value": true,
      "site": "00b6222c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621e8",
      "incomplete_value": true,
      "site": "00b621e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62234",
      "incomplete_value": false,
      "site": "00b62240",
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
            "const:fb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621f0",
      "incomplete_value": false,
      "site": "00b621fc",
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
            "const:f1d:8"
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
      "00b62228",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62234",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62248",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62228",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62234",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b62248",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b621fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md#insn-00b621fc) · [`00b62204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md#insn-00b62204) · [`00b621e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md#insn-00b621e4)
- 新版 [`00b62240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62240) · [`00b62248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62248) · [`00b62228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62228)

~~~diff
- 00b621fc ["INT_ADD", "register:40f0:8", ["const:b621fc:8", "const:4:8"]]
- 00b621fc ["CALL", null, ["callee:00bde090:8"]]
+ 00b62240 ["INT_ADD", "register:40f0:8", ["const:b62240:8", "const:4:8"]]
+ 00b62240 ["CALL", null, ["callee:00bde090:8"]]
- 00b621fc bytes 91ef0194
+ 00b62240 bytes 94ef0194
- 00b62204 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b62204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62204 bytes 60f202f9
+ 00b62248 bytes 601203f9
- 00b621e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b621e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62228 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b621e4 bytes 68f242f9
+ 00b62228 bytes 681243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-005383ca8170cb157bc676686192dcf9"></a>

### [`00b62224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md) → [`00b62268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62268.md) _ZN8firebase4auth29invalid_credentials_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b622c0",
      "incomplete_value": true,
      "site": "00b622c0",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6227c",
      "incomplete_value": true,
      "site": "00b6227c",
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
            "const:5e8:8"
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
      "00b6227c",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6229c",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b622c0",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6227c",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6229c",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b622c0",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md#insn-00b62238) · [`00b6227c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md#insn-00b6227c) · [`00b62258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md#insn-00b62258)
- 新版 [`00b6227c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62268.md#insn-00b6227c) · [`00b622c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62268.md#insn-00b622c0) · [`00b6229c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62268.md#insn-00b6229c)

~~~diff
- 00b62238 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5e8:8"]]
- 00b62238 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62238 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6227c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:628:8"]]
+ 00b6227c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6227c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62238 bytes a8a25739
+ 00b6227c bytes a8a25839
- 00b6227c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6227c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5e8:8"]]
- 00b6227c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b622c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b622c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:628:8"]]
+ 00b622c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6227c bytes a0a21739
+ 00b622c0 bytes a0a21839
- 00b62258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e0:8"]]
- 00b62258 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6229c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:620:8"]]
+ 00b6229c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62258 bytes 21f142f9
+ 00b6229c bytes 211143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598ff8f392736a4bb4ea271ebeefdc4d"></a>

### [`00b62290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62290.md) → [`00b622d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b622d4.md) _ZN8firebase4auth29invalid_credentials_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62310",
      "incomplete_value": true,
      "site": "00b62310",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b622cc",
      "incomplete_value": true,
      "site": "00b622cc",
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
            "const:5e8:8"
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
      "definition_site": "00b62330",
      "incomplete_value": true,
      "site": "00b62330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b622ec",
      "incomplete_value": true,
      "site": "00b622ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b62320",
      "incomplete_value": true,
      "site": "00b6232c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b622dc",
      "incomplete_value": true,
      "site": "00b622e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5e0:8"
              ]
            ]
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
      "00b622e8",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b622f4",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62310",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b622e8",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b622f4",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62310",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b622a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62290.md#insn-00b622a4) · [`00b622cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62290.md#insn-00b622cc) · [`00b622e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62290.md#insn-00b622e8)
- 新版 [`00b622e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b622d4.md#insn-00b622e8) · [`00b62310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b622d4.md#insn-00b62310) · [`00b6232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b622d4.md#insn-00b6232c)

~~~diff
- 00b622a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b622a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b622e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b622e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b622a4 bytes 81f242f9
+ 00b622e8 bytes 811243f9
- 00b622cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b622cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b622cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5e8:8"]]
- 00b622cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b62310 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b62310 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b62310 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:628:8"]]
+ 00b62310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b622cc bytes bfa21739
+ 00b62310 bytes bfa21839
- 00b622e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b622e8 ["INT_ADD", "register:40f0:8", ["const:b622e8:8", "const:4:8"]]
- 00b622e8 ["CALLIND", null, ["register:0:8"]]
+ 00b6232c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6232c ["INT_ADD", "register:40f0:8", ["const:b6232c:8", "const:4:8"]]
+ 00b6232c ["CALLIND", null, ["register:0:8"]]
- 00b622e8 bytes 00013fd6
+ 00b6232c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb37fb3e32701cde8ad4e508518d426"></a>

### [`00b62300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md) → [`00b62344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md) _ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b62384",
      "incomplete_value": true,
      "site": "00b62384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62340",
      "incomplete_value": true,
      "site": "00b62340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b62360",
      "incomplete_value": true,
      "site": "00b62360",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6231c",
      "incomplete_value": true,
      "site": "00b6231c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6231c"
      ],
      [
        "FALL_THROUGH",
        "00b62360"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62360",
      "incomplete_value": true,
      "site": "00b62384",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6231c",
      "incomplete_value": true,
      "site": "00b62340",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62358",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62368",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62384",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62358",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62368",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b62384",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62340) · [`00b62314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62314) · [`00b62324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62324)
- 新版 [`00b62384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b62384) · [`00b62358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b62358) · [`00b62368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b62368)

~~~diff
- 00b62340 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b62340 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62340 bytes 80f202f9
+ 00b62384 bytes 801203f9
- 00b62314 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b62314 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62358 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62358 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62314 bytes 81f242f9
+ 00b62358 bytes 811243f9
- 00b62324 ["COPY", "tmp:0:8", ["const:f1d:8"]]
- 00b62324 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b62324 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b62324 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b62368 ["COPY", "tmp:0:8", ["const:fb7:8"]]
+ 00b62368 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62368 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62368 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b62324 bytes 63743c91
+ 00b62368 bytes 63dc3e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e81f748b7ff1888fa331a4b692c614"></a>

### [`00b62370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62370.md) → [`00b623b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md) _ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b623d0",
      "incomplete_value": false,
      "site": "00b623d4",
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
      "definition_site": "00b6238c",
      "incomplete_value": false,
      "site": "00b62390",
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
      "definition_site": "00b623e0",
      "incomplete_value": true,
      "site": "00b623ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6239c",
      "incomplete_value": true,
      "site": "00b623a8",
      "value": [
        "LOAD",
        "8",
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
      "00b623d0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b623e0",
      "DATA",
      [
        "storage",
        "010a15f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b623d0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b623e0",
      "DATA",
      [
        "storage",
        "010a1630",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62370.md#insn-00b62390) · [`00b6238c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62370.md#insn-00b6238c) · [`00b62398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62370.md#insn-00b62398)
- 新版 [`00b623d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623d4) · [`00b623d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623d0) · [`00b623dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623dc)

~~~diff
- 00b62390 ["INT_ADD", "register:40f0:8", ["const:b62390:8", "const:4:8"]]
- 00b62390 ["CALL", null, ["callee:00bde180:8"]]
+ 00b623d4 ["INT_ADD", "register:40f0:8", ["const:b623d4:8", "const:4:8"]]
+ 00b623d4 ["CALL", null, ["callee:00bde180:8"]]
- 00b62390 bytes 68ef0194
+ 00b623d4 bytes 6bef0194
- 00b6238c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6238c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6238c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6238c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b623d0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b623d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b623d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b623d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6238c bytes 00501791
+ 00b623d0 bytes 001c1591
- 00b62398 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00b62398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b623dc ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00b623dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b623dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b623dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62398 bytes 08c11791
+ 00b623dc bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cebe6348b8c97934c3de802591642ae4"></a>

### [`00b623ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md) → [`00b623f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md) _ZN8firebase4auth29invalid_credentials_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62430",
      "incomplete_value": true,
      "site": "00b62430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b623ec",
      "incomplete_value": true,
      "site": "00b623ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "00b6240c",
      "incomplete_value": true,
      "site": "00b6240c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b623c8",
      "incomplete_value": true,
      "site": "00b623c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b623c8"
      ],
      [
        "FALL_THROUGH",
        "00b6240c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6240c",
      "incomplete_value": true,
      "site": "00b62430",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b623c8",
      "incomplete_value": true,
      "site": "00b623ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62404",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62414",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62430",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62404",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62414",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00b62430",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b623ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md#insn-00b623ec) · [`00b623c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md#insn-00b623c0) · [`00b623d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md#insn-00b623d0)
- 新版 [`00b62430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b62430) · [`00b62404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b62404) · [`00b62414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b62414)

~~~diff
- 00b623ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b623ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62430 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b623ec bytes 80f202f9
+ 00b62430 bytes 801203f9
- 00b623c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b623c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62404 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b623c0 bytes 81f242f9
+ 00b62404 bytes 811243f9
- 00b623d0 ["COPY", "tmp:0:8", ["const:f1d:8"]]
- 00b623d0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b623d0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b623d0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b62414 ["COPY", "tmp:0:8", ["const:fb7:8"]]
+ 00b62414 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62414 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b62414 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b623d0 bytes 63743c91
+ 00b62414 bytes 63dc3e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac2f39482a3d3dc2c37ecb3837e3fd2b"></a>

### [`00b6241c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md) → [`00b62460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62460.md) _ZN8firebase4auth29invalid_credentials_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6247c",
      "incomplete_value": false,
      "site": "00b62480",
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
      "definition_site": "00b62438",
      "incomplete_value": false,
      "site": "00b6243c",
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
      "00b6247c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6248c",
      "DATA",
      [
        "storage",
        "010a15f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6247c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6248c",
      "DATA",
      [
        "storage",
        "010a1638",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6243c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md#insn-00b6243c) · [`00b62438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md#insn-00b62438) · [`00b62444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md#insn-00b62444)
- 新版 [`00b62480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62460.md#insn-00b62480) · [`00b6247c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62460.md#insn-00b6247c) · [`00b62488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62460.md#insn-00b62488)

~~~diff
- 00b6243c ["INT_ADD", "register:40f0:8", ["const:b6243c:8", "const:4:8"]]
- 00b6243c ["CALL", null, ["callee:00bde180:8"]]
+ 00b62480 ["INT_ADD", "register:40f0:8", ["const:b62480:8", "const:4:8"]]
+ 00b62480 ["CALL", null, ["callee:00bde180:8"]]
- 00b6243c bytes 3def0194
+ 00b62480 bytes 40ef0194
- 00b62438 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b62438 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62438 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62438 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6247c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6247c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6247c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6247c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62438 bytes 00fc1991
+ 00b6247c bytes 00c81791
- 00b62444 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00b62444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62488 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 00b62488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62444 bytes 08e11791
+ 00b62488 bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-370fbbb84b8f1bfce0046f085da818ce"></a>

### [`00b62458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md) → [`00b6249c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b624c8",
      "incomplete_value": true,
      "site": "00b624c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62484",
      "incomplete_value": true,
      "site": "00b62484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b624b0",
      "incomplete_value": true,
      "site": "00b624b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6246c",
      "incomplete_value": true,
      "site": "00b6246c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b624bc",
      "incomplete_value": false,
      "site": "00b624c0",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62478",
      "incomplete_value": false,
      "site": "00b6247c",
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
            "const:56c:8"
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
      "00b624ac",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b624bc",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b624c8",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b624ac",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b624bc",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b624c8",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b6247c) · [`00b62484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b62484) · [`00b62468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b62468)
- 新版 [`00b624c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624c0) · [`00b624c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624c8) · [`00b624ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624ac)

~~~diff
- 00b6247c ["INT_ADD", "register:40f0:8", ["const:b6247c:8", "const:4:8"]]
- 00b6247c ["CALL", null, ["callee:00bde090:8"]]
+ 00b624c0 ["INT_ADD", "register:40f0:8", ["const:b624c0:8", "const:4:8"]]
+ 00b624c0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6247c bytes f1ee0194
+ 00b624c0 bytes f4ee0194
- 00b62484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b62484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b624c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b624c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62484 bytes 600203f9
+ 00b624c8 bytes 602203f9
- 00b62468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b62468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b624ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b624ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62468 bytes 680243f9
+ 00b624ac bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e7ebcd5ee64377fc65f344fd7cc665"></a>

### [`00b62498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md) → [`00b624dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b62508",
      "incomplete_value": true,
      "site": "00b62508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624c4",
      "incomplete_value": true,
      "site": "00b624c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b624f0",
      "incomplete_value": true,
      "site": "00b624f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624ac",
      "incomplete_value": true,
      "site": "00b624ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b624f8",
      "incomplete_value": false,
      "site": "00b62500",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624b4",
      "incomplete_value": false,
      "site": "00b624bc",
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
            "const:56c:8"
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
      "00b624ec",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b624f8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b62508",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b624ec",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b624f8",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b62508",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b624bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md#insn-00b624bc) · [`00b624c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md#insn-00b624c4) · [`00b624a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md#insn-00b624a8)
- 新版 [`00b62500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b62500) · [`00b62508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b62508) · [`00b624ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b624ec)

~~~diff
- 00b624bc ["INT_ADD", "register:40f0:8", ["const:b624bc:8", "const:4:8"]]
- 00b624bc ["CALL", null, ["callee:00bde090:8"]]
+ 00b62500 ["INT_ADD", "register:40f0:8", ["const:b62500:8", "const:4:8"]]
+ 00b62500 ["CALL", null, ["callee:00bde090:8"]]
- 00b624bc bytes e1ee0194
+ 00b62500 bytes e4ee0194
- 00b624c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b624c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62508 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b624c4 bytes 600203f9
+ 00b62508 bytes 602203f9
- 00b624a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b624a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b624ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b624ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b624a8 bytes 680243f9
+ 00b624ec bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1f99c6a9c3102384363d7df00add251"></a>

### [`00b624d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b624d8.md) → [`00b6251c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6251c.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6254c",
      "incomplete_value": true,
      "site": "00b6254c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62508",
      "incomplete_value": true,
      "site": "00b62508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b62530",
      "incomplete_value": true,
      "site": "00b62530",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624ec",
      "incomplete_value": true,
      "site": "00b624ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6253c",
      "incomplete_value": false,
      "site": "00b62544",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624f8",
      "incomplete_value": false,
      "site": "00b62500",
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
            "const:56c:8"
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
      "00b6252c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6253c",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b6254c",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6252c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6253c",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b6254c",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b624d8.md#insn-00b62500) · [`00b62508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b624d8.md#insn-00b62508) · [`00b624e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b624d8.md#insn-00b624e8)
- 新版 [`00b62544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6251c.md#insn-00b62544) · [`00b6254c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6251c.md#insn-00b6254c) · [`00b6252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6251c.md#insn-00b6252c)

~~~diff
- 00b62500 ["INT_ADD", "register:40f0:8", ["const:b62500:8", "const:4:8"]]
- 00b62500 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62544 ["INT_ADD", "register:40f0:8", ["const:b62544:8", "const:4:8"]]
+ 00b62544 ["CALL", null, ["callee:00bde090:8"]]
- 00b62500 bytes d0ee0194
+ 00b62544 bytes d3ee0194
- 00b62508 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b62508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6254c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b6254c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62508 bytes 600203f9
+ 00b6254c bytes 602203f9
- 00b624e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b624e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6252c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b6252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b624e8 bytes 680243f9
+ 00b6252c bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7136cacc9cb748c7fa383d4ef42638"></a>

### [`00b6251c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md) → [`00b62560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62590",
      "incomplete_value": true,
      "site": "00b62590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6254c",
      "incomplete_value": true,
      "site": "00b6254c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b6257c",
      "incomplete_value": false,
      "site": "00b62588",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62538",
      "incomplete_value": false,
      "site": "00b62544",
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
            "const:56c:8"
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
      "00b62570",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6257c",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b62590",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62570",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6257c",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b62590",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md#insn-00b62544) · [`00b6254c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md#insn-00b6254c) · [`00b6252c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md#insn-00b6252c)
- 新版 [`00b62588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62588) · [`00b62590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62590) · [`00b62570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62570)

~~~diff
- 00b62544 ["INT_ADD", "register:40f0:8", ["const:b62544:8", "const:4:8"]]
- 00b62544 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62588 ["INT_ADD", "register:40f0:8", ["const:b62588:8", "const:4:8"]]
+ 00b62588 ["CALL", null, ["callee:00bde090:8"]]
- 00b62544 bytes bfee0194
+ 00b62588 bytes c2ee0194
- 00b6254c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b6254c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6254c bytes 600203f9
+ 00b62590 bytes 602203f9
- 00b6252c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b6252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62570 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6252c bytes 680243f9
+ 00b62570 bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e586dfa744baf4954ac86dff361e5944"></a>

### [`00b6256c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md) → [`00b625b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md) _ZN8firebase4auth22invalid_user_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62608",
      "incomplete_value": true,
      "site": "00b62608",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b625c4",
      "incomplete_value": true,
      "site": "00b625c4",
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
            "const:608:8"
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
      "definition_site": "00b625e4",
      "incomplete_value": true,
      "site": "00b625f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:640:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b625a0",
      "incomplete_value": true,
      "site": "00b625ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:600:8"
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
      "00b625c4",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b625e4",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62608",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b625c4",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b625e4",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62608",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md#insn-00b62580) · [`00b625ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md#insn-00b625ac) · [`00b625c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md#insn-00b625c4)
- 新版 [`00b625c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b625c4) · [`00b625f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b625f0) · [`00b62608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b62608)

~~~diff
- 00b62580 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:608:8"]]
- 00b62580 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62580 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b625c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
+ 00b625c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b625c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62580 bytes a8225839
+ 00b625c4 bytes a8225939
- 00b625ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b625ac ["INT_ADD", "register:40f0:8", ["const:b625ac:8", "const:4:8"]]
- 00b625ac ["CALLIND", null, ["register:0:8"]]
+ 00b625f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b625f0 ["INT_ADD", "register:40f0:8", ["const:b625f0:8", "const:4:8"]]
+ 00b625f0 ["CALLIND", null, ["register:0:8"]]
- 00b625ac bytes 00013fd6
+ 00b625f0 bytes 00013fd6
- 00b625c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b625c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:608:8"]]
- 00b625c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62608 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62608 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
+ 00b62608 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b625c4 bytes a0221839
+ 00b62608 bytes a0221939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de2087de2769e99bcef046772f1e92f0"></a>

### [`00b625d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md) → [`00b6261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md) _ZN8firebase4auth22invalid_user_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b62658",
      "incomplete_value": true,
      "site": "00b62658",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62614",
      "incomplete_value": true,
      "site": "00b62614",
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
            "const:608:8"
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
      "definition_site": "00b62678",
      "incomplete_value": true,
      "site": "00b62678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62634",
      "incomplete_value": true,
      "site": "00b62634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b62634",
      "incomplete_value": true,
      "site": "00b62634",
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
      "definition_site": "00b625f0",
      "incomplete_value": true,
      "site": "00b625f0",
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
      "00b62630",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6263c",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62658",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62630",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6263c",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62658",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b625ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md#insn-00b625ec) · [`00b62614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md#insn-00b62614) · [`00b62630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md#insn-00b62630)
- 新版 [`00b62630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62630) · [`00b62658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62658) · [`00b62674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62674)

~~~diff
- 00b625ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b625ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62630 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b625ec bytes 810243f9
+ 00b62630 bytes 812243f9
- 00b62614 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62614 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62614 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
- 00b62614 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b62658 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b62658 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b62658 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
+ 00b62658 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62614 bytes bf221839
+ 00b62658 bytes bf221939
- 00b62630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62630 ["INT_ADD", "register:40f0:8", ["const:b62630:8", "const:4:8"]]
- 00b62630 ["CALLIND", null, ["register:0:8"]]
+ 00b62674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62674 ["INT_ADD", "register:40f0:8", ["const:b62674:8", "const:4:8"]]
+ 00b62674 ["CALLIND", null, ["register:0:8"]]
- 00b62630 bytes 00013fd6
+ 00b62674 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad0c26762f49940a83330353f5133b5"></a>

### [`00b62648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62648.md) → [`00b6268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md) _ZN8firebase4auth22invalid_user_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b626cc",
      "incomplete_value": true,
      "site": "00b626cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62688",
      "incomplete_value": true,
      "site": "00b62688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b626a8",
      "incomplete_value": true,
      "site": "00b626a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62664",
      "incomplete_value": true,
      "site": "00b62664",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b626b0",
      "incomplete_value": false,
      "site": "00b626c4",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6266c",
      "incomplete_value": false,
      "site": "00b62680",
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
            "const:56c:8"
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
      "00b626a0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b626b0",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b626cc",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b626a0",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b626b0",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b626cc",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62648.md#insn-00b62680) · [`00b62688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62648.md#insn-00b62688) · [`00b6265c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62648.md#insn-00b6265c)
- 新版 [`00b626c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b626c4) · [`00b626cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b626cc) · [`00b626a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b626a0)

~~~diff
- 00b62680 ["INT_ADD", "register:40f0:8", ["const:b62680:8", "const:4:8"]]
- 00b62680 ["CALL", null, ["callee:00bde090:8"]]
+ 00b626c4 ["INT_ADD", "register:40f0:8", ["const:b626c4:8", "const:4:8"]]
+ 00b626c4 ["CALL", null, ["callee:00bde090:8"]]
- 00b62680 bytes 70ee0194
+ 00b626c4 bytes 73ee0194
- 00b62688 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b62688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b626cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b626cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62688 bytes 800203f9
+ 00b626cc bytes 802203f9
- 00b6265c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b6265c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b626a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b626a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6265c bytes 810243f9
+ 00b626a0 bytes 812243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2221b5e161a55541599d5a06e801d7cd"></a>

### [`00b626b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md) → [`00b626fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md) _ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62718",
      "incomplete_value": false,
      "site": "00b6271c",
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
      "definition_site": "00b626d4",
      "incomplete_value": false,
      "site": "00b626d8",
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
      "definition_site": "00b62728",
      "incomplete_value": true,
      "site": "00b62734",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b626e4",
      "incomplete_value": true,
      "site": "00b626f0",
      "value": [
        "LOAD",
        "8",
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
      "00b62718",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62728",
      "DATA",
      [
        "storage",
        "010a1610",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62718",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62728",
      "DATA",
      [
        "storage",
        "010a1650",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b626d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626d8) · [`00b626d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626d4) · [`00b626e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626e0)
- 新版 [`00b6271c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b6271c) · [`00b62718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b62718) · [`00b62724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b62724)

~~~diff
- 00b626d8 ["INT_ADD", "register:40f0:8", ["const:b626d8:8", "const:4:8"]]
- 00b626d8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6271c ["INT_ADD", "register:40f0:8", ["const:b6271c:8", "const:4:8"]]
+ 00b6271c ["CALL", null, ["callee:00bde180:8"]]
- 00b626d8 bytes 96ee0194
+ 00b6271c bytes 99ee0194
- 00b626d4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b626d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b626d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b626d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62718 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b62718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b626d4 bytes 00501791
+ 00b62718 bytes 001c1591
- 00b626e0 ["COPY", "tmp:0:8", ["const:610:8"]]
- 00b626e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b626e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b626e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62724 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00b62724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b626e0 bytes 08411891
+ 00b62724 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa82a7e0ce3730d658bca2608e6780ff"></a>

### [`00b626f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md) → [`00b62738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md) _ZN8firebase4auth22invalid_user_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62778",
      "incomplete_value": true,
      "site": "00b62778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62734",
      "incomplete_value": true,
      "site": "00b62734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b62754",
      "incomplete_value": true,
      "site": "00b62754",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62710",
      "incomplete_value": true,
      "site": "00b62710",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6275c",
      "incomplete_value": false,
      "site": "00b62770",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62718",
      "incomplete_value": false,
      "site": "00b6272c",
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
            "const:56c:8"
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
      "00b6274c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6275c",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b62778",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6274c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6275c",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b62778",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6272c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md#insn-00b6272c) · [`00b62734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md#insn-00b62734) · [`00b62708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md#insn-00b62708)
- 新版 [`00b62770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b62770) · [`00b62778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b62778) · [`00b6274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b6274c)

~~~diff
- 00b6272c ["INT_ADD", "register:40f0:8", ["const:b6272c:8", "const:4:8"]]
- 00b6272c ["CALL", null, ["callee:00bde090:8"]]
+ 00b62770 ["INT_ADD", "register:40f0:8", ["const:b62770:8", "const:4:8"]]
+ 00b62770 ["CALL", null, ["callee:00bde090:8"]]
- 00b6272c bytes 45ee0194
+ 00b62770 bytes 48ee0194
- 00b62734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b62734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62734 bytes 800203f9
+ 00b62778 bytes 802203f9
- 00b62708 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b62708 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6274c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b6274c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62708 bytes 810243f9
+ 00b6274c bytes 812243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3594d17e920fde2a04ba880f9efeabb5"></a>

### [`00b62764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62764.md) → [`00b627a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627a8.md) _ZN8firebase4auth22invalid_user_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b627c4",
      "incomplete_value": false,
      "site": "00b627c8",
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
      "definition_site": "00b62780",
      "incomplete_value": false,
      "site": "00b62784",
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
      "definition_site": "00b627d4",
      "incomplete_value": true,
      "site": "00b627e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62790",
      "incomplete_value": true,
      "site": "00b6279c",
      "value": [
        "LOAD",
        "8",
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
      "00b627c4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b627d4",
      "DATA",
      [
        "storage",
        "010a1618",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b627c4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b627d4",
      "DATA",
      [
        "storage",
        "010a1658",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62764.md#insn-00b62784) · [`00b62780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62764.md#insn-00b62780) · [`00b6278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62764.md#insn-00b6278c)
- 新版 [`00b627c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627a8.md#insn-00b627c8) · [`00b627c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627a8.md#insn-00b627c4) · [`00b627d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627a8.md#insn-00b627d0)

~~~diff
- 00b62784 ["INT_ADD", "register:40f0:8", ["const:b62784:8", "const:4:8"]]
- 00b62784 ["CALL", null, ["callee:00bde180:8"]]
+ 00b627c8 ["INT_ADD", "register:40f0:8", ["const:b627c8:8", "const:4:8"]]
+ 00b627c8 ["CALL", null, ["callee:00bde180:8"]]
- 00b62784 bytes 6bee0194
+ 00b627c8 bytes 6eee0194
- 00b62780 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b62780 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62780 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62780 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b627c4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b627c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b627c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b627c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62780 bytes 00fc1991
+ 00b627c4 bytes 00c81791
- 00b6278c ["COPY", "tmp:0:8", ["const:618:8"]]
- 00b6278c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6278c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6278c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b627d0 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00b627d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b627d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b627d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6278c bytes 08611891
+ 00b627d0 bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5b8023f4b4a9dc16870fb9d93928601"></a>

### [`00b627a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md) → [`00b627e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b62810",
      "incomplete_value": true,
      "site": "00b62810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b627cc",
      "incomplete_value": true,
      "site": "00b627cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b627f8",
      "incomplete_value": true,
      "site": "00b627f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b627b4",
      "incomplete_value": true,
      "site": "00b627b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b627b4"
      ],
      [
        "FALL_THROUGH",
        "00b627f8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b627f8",
      "incomplete_value": true,
      "site": "00b62810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b627b4",
      "incomplete_value": true,
      "site": "00b627cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b627f4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62810",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b627f4",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62810",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b627cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md#insn-00b627cc) · [`00b627b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md#insn-00b627b0) · [`00b627c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md#insn-00b627c4)
- 新版 [`00b62810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b62810) · [`00b627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b627f4) · [`00b62808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b62808)

~~~diff
- 00b627cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b627cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b627cc bytes 601203f9
+ 00b62810 bytes 603203f9
- 00b627b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b627b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b627f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b627f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b627b0 bytes 681243f9
+ 00b627f4 bytes 683243f9
- 00b627c4 ["INT_ADD", "register:40f0:8", ["const:b627c4:8", "const:4:8"]]
- 00b627c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62808 ["INT_ADD", "register:40f0:8", ["const:b62808:8", "const:4:8"]]
+ 00b62808 ["CALL", null, ["callee:00bde090:8"]]
- 00b627c4 bytes 1fee0194
+ 00b62808 bytes 22ee0194
~~~


<a id="compare-f9d1962e33443539fed887a5b5e69800"></a>

### [`00b627e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md) → [`00b62824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b62850",
      "incomplete_value": true,
      "site": "00b62850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6280c",
      "incomplete_value": true,
      "site": "00b6280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b62838",
      "incomplete_value": true,
      "site": "00b62838",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b627f4",
      "incomplete_value": true,
      "site": "00b627f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b627f4"
      ],
      [
        "FALL_THROUGH",
        "00b62838"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62838",
      "incomplete_value": true,
      "site": "00b62850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b627f4",
      "incomplete_value": true,
      "site": "00b6280c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62834",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62850",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62834",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62850",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md#insn-00b6280c) · [`00b627f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md#insn-00b627f0) · [`00b62804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md#insn-00b62804)
- 新版 [`00b62850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62850) · [`00b62834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62834) · [`00b62848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62848)

~~~diff
- 00b6280c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b6280c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6280c bytes 601203f9
+ 00b62850 bytes 603203f9
- 00b627f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b627f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b627f0 bytes 681243f9
+ 00b62834 bytes 683243f9
- 00b62804 ["INT_ADD", "register:40f0:8", ["const:b62804:8", "const:4:8"]]
- 00b62804 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62848 ["INT_ADD", "register:40f0:8", ["const:b62848:8", "const:4:8"]]
+ 00b62848 ["CALL", null, ["callee:00bde090:8"]]
- 00b62804 bytes 0fee0194
+ 00b62848 bytes 12ee0194
~~~


<a id="compare-c19123d0484d2d26af9a1b48a28c4a22"></a>

### [`00b62820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md) → [`00b62864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62894",
      "incomplete_value": true,
      "site": "00b62894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62850",
      "incomplete_value": true,
      "site": "00b62850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62834",
      "incomplete_value": true,
      "site": "00b62834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62834"
      ],
      [
        "FALL_THROUGH",
        "00b62878"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62894",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62834",
      "incomplete_value": true,
      "site": "00b62850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62874",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62894",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62874",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62894",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62850) · [`00b62830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62830) · [`00b62848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62848)
- 新版 [`00b62894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b62894) · [`00b62874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b62874) · [`00b6288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b6288c)

~~~diff
- 00b62850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62894 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62850 bytes 601203f9
+ 00b62894 bytes 603203f9
- 00b62830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62830 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62830 bytes 681243f9
+ 00b62874 bytes 683243f9
- 00b62848 ["INT_ADD", "register:40f0:8", ["const:b62848:8", "const:4:8"]]
- 00b62848 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6288c ["INT_ADD", "register:40f0:8", ["const:b6288c:8", "const:4:8"]]
+ 00b6288c ["CALL", null, ["callee:00bde090:8"]]
- 00b62848 bytes feed0194
+ 00b6288c bytes 01ee0194
~~~


<a id="compare-fd764d6cb6a61911d8e8bd444e103640"></a>

### [`00b62864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md) → [`00b628a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b628d8",
      "incomplete_value": true,
      "site": "00b628d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62894",
      "incomplete_value": true,
      "site": "00b62894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b628bc",
      "incomplete_value": true,
      "site": "00b628bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62878"
      ],
      [
        "FALL_THROUGH",
        "00b628bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b628bc",
      "incomplete_value": true,
      "site": "00b628d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62894",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b628b8",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b628d8",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b628b8",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b628d8",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md#insn-00b62894) · [`00b62874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md#insn-00b62874) · [`00b6288c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md#insn-00b6288c)
- 新版 [`00b628d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628d8) · [`00b628b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628b8) · [`00b628d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628d0)

~~~diff
- 00b62894 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b628d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b628d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62894 bytes 601203f9
+ 00b628d8 bytes 603203f9
- 00b62874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b628b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b628b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62874 bytes 681243f9
+ 00b628b8 bytes 683243f9
- 00b6288c ["INT_ADD", "register:40f0:8", ["const:b6288c:8", "const:4:8"]]
- 00b6288c ["CALL", null, ["callee:00bde090:8"]]
+ 00b628d0 ["INT_ADD", "register:40f0:8", ["const:b628d0:8", "const:4:8"]]
+ 00b628d0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6288c bytes eded0194
+ 00b628d0 bytes f0ed0194
~~~


<a id="compare-5344677a67572b7262e496f823b8a6eb"></a>

### [`00b628b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md) → [`00b628f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md) _ZN8firebase4auth31recent_login_required_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62950",
      "incomplete_value": true,
      "site": "00b62950",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6290c",
      "incomplete_value": true,
      "site": "00b6290c",
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
            "const:628:8"
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
      "definition_site": "00b6292c",
      "incomplete_value": true,
      "site": "00b62938",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b628e8",
      "incomplete_value": true,
      "site": "00b628f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
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
      "00b6290c",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6292c",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62950",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6290c",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6292c",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62950",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b628c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b628c8) · [`00b628f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b628f4) · [`00b6290c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b6290c)
- 新版 [`00b6290c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b6290c) · [`00b62938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b62938) · [`00b62950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b62950)

~~~diff
- 00b628c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:628:8"]]
- 00b628c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b628c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6290c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:668:8"]]
+ 00b6290c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6290c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b628c8 bytes a8a25839
+ 00b6290c bytes a8a25939
- 00b628f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b628f4 ["INT_ADD", "register:40f0:8", ["const:b628f4:8", "const:4:8"]]
- 00b628f4 ["CALLIND", null, ["register:0:8"]]
+ 00b62938 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62938 ["INT_ADD", "register:40f0:8", ["const:b62938:8", "const:4:8"]]
+ 00b62938 ["CALLIND", null, ["register:0:8"]]
- 00b628f4 bytes 00013fd6
+ 00b62938 bytes 00013fd6
- 00b6290c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6290c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:628:8"]]
- 00b6290c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62950 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62950 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:668:8"]]
+ 00b62950 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6290c bytes a0a21839
+ 00b62950 bytes a0a21939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b2fe91537ef8788ce790e6335aae71"></a>

### [`00b62920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62920.md) → [`00b62964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md) _ZN8firebase4auth31recent_login_required_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b629a0",
      "incomplete_value": true,
      "site": "00b629a0",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6295c",
      "incomplete_value": true,
      "site": "00b6295c",
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
            "const:628:8"
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
      "definition_site": "00b629c0",
      "incomplete_value": true,
      "site": "00b629c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6297c",
      "incomplete_value": true,
      "site": "00b6297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b6297c",
      "incomplete_value": true,
      "site": "00b6297c",
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
      "definition_site": "00b62938",
      "incomplete_value": true,
      "site": "00b62938",
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
      "00b62978",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62984",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b629a0",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62978",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62984",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b629a0",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62920.md#insn-00b62934) · [`00b6295c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62920.md#insn-00b6295c) · [`00b62978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62920.md#insn-00b62978)
- 新版 [`00b62978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b62978) · [`00b629a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b629a0) · [`00b629bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b629bc)

~~~diff
- 00b62934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b62934 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62978 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b62978 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62934 bytes 811243f9
+ 00b62978 bytes 813243f9
- 00b6295c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6295c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6295c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:628:8"]]
- 00b6295c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b629a0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b629a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b629a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:668:8"]]
+ 00b629a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6295c bytes bfa21839
+ 00b629a0 bytes bfa21939
- 00b62978 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62978 ["INT_ADD", "register:40f0:8", ["const:b62978:8", "const:4:8"]]
- 00b62978 ["CALLIND", null, ["register:0:8"]]
+ 00b629bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b629bc ["INT_ADD", "register:40f0:8", ["const:b629bc:8", "const:4:8"]]
+ 00b629bc ["CALLIND", null, ["register:0:8"]]
- 00b62978 bytes 00013fd6
+ 00b629bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf4bd7a8219f35cb592c4832f6bf306"></a>

### [`00b62990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md) → [`00b629d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md) _ZN8firebase4auth31recent_login_required_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b62a14",
      "incomplete_value": true,
      "site": "00b62a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629d0",
      "incomplete_value": true,
      "site": "00b629d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b629f0",
      "incomplete_value": true,
      "site": "00b629f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629ac",
      "incomplete_value": true,
      "site": "00b629ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b629ac"
      ],
      [
        "FALL_THROUGH",
        "00b629f0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b629f0",
      "incomplete_value": true,
      "site": "00b62a14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629ac",
      "incomplete_value": true,
      "site": "00b629d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b629e8",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a14",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a2c",
      "PARAM",
      [
        "storage",
        "010a1630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b629e8",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a14",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a2c",
      "PARAM",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b629d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629d0) · [`00b629a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629a4) · [`00b629c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629c8)
- 新版 [`00b62a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b62a14) · [`00b629e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b629e8) · [`00b62a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b62a0c)

~~~diff
- 00b629d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b629d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b62a14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b629d0 bytes 801203f9
+ 00b62a14 bytes 803203f9
- 00b629a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b629a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b629e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b629e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b629a4 bytes 811243f9
+ 00b629e8 bytes 813243f9
- 00b629c8 ["INT_ADD", "register:40f0:8", ["const:b629c8:8", "const:4:8"]]
- 00b629c8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62a0c ["INT_ADD", "register:40f0:8", ["const:b62a0c:8", "const:4:8"]]
+ 00b62a0c ["CALL", null, ["callee:00bde090:8"]]
- 00b629c8 bytes 9eed0194
+ 00b62a0c bytes a1ed0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6068b0a9df564ccabf71103a13e128fd"></a>

### [`00b62a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md) → [`00b62a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md) _ZN8firebase4auth31recent_login_required_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62a60",
      "incomplete_value": false,
      "site": "00b62a64",
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
      "definition_site": "00b62a1c",
      "incomplete_value": false,
      "site": "00b62a20",
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
      "definition_site": "00b62a70",
      "incomplete_value": true,
      "site": "00b62a7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62a2c",
      "incomplete_value": true,
      "site": "00b62a38",
      "value": [
        "LOAD",
        "8",
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
      "00b62a60",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62a70",
      "DATA",
      [
        "storage",
        "010a1630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62a60",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62a70",
      "DATA",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a20) · [`00b62a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a1c) · [`00b62a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a28)
- 新版 [`00b62a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a64) · [`00b62a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a60) · [`00b62a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a6c)

~~~diff
- 00b62a20 ["INT_ADD", "register:40f0:8", ["const:b62a20:8", "const:4:8"]]
- 00b62a20 ["CALL", null, ["callee:00bde180:8"]]
+ 00b62a64 ["INT_ADD", "register:40f0:8", ["const:b62a64:8", "const:4:8"]]
+ 00b62a64 ["CALL", null, ["callee:00bde180:8"]]
- 00b62a20 bytes c4ed0194
+ 00b62a64 bytes c7ed0194
- 00b62a1c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b62a1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62a60 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b62a60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62a60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62a60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62a1c bytes 00501791
+ 00b62a60 bytes 001c1591
- 00b62a28 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00b62a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62a6c ["COPY", "tmp:0:8", ["const:670:8"]]
+ 00b62a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62a28 bytes 08c11891
+ 00b62a6c bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd52e78f0e80b7128f8f4a355444822b"></a>

### [`00b62a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md) → [`00b62a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md) _ZN8firebase4auth31recent_login_required_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62ac0",
      "incomplete_value": true,
      "site": "00b62ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a7c",
      "incomplete_value": true,
      "site": "00b62a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b62a9c",
      "incomplete_value": true,
      "site": "00b62a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a58",
      "incomplete_value": true,
      "site": "00b62a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62a58"
      ],
      [
        "FALL_THROUGH",
        "00b62a9c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62a9c",
      "incomplete_value": true,
      "site": "00b62ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a58",
      "incomplete_value": true,
      "site": "00b62a7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62a94",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ac0",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ad8",
      "PARAM",
      [
        "storage",
        "010a1638",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62a94",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ac0",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ad8",
      "PARAM",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a7c) · [`00b62a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a50) · [`00b62a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a74)
- 新版 [`00b62ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62ac0) · [`00b62a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62a94) · [`00b62ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62ab8)

~~~diff
- 00b62a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b62a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b62ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62a7c bytes 801203f9
+ 00b62ac0 bytes 803203f9
- 00b62a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b62a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b62a94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62a50 bytes 811243f9
+ 00b62a94 bytes 813243f9
- 00b62a74 ["INT_ADD", "register:40f0:8", ["const:b62a74:8", "const:4:8"]]
- 00b62a74 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62ab8 ["INT_ADD", "register:40f0:8", ["const:b62ab8:8", "const:4:8"]]
+ 00b62ab8 ["CALL", null, ["callee:00bde090:8"]]
- 00b62a74 bytes 73ed0194
+ 00b62ab8 bytes 76ed0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c20c2c01b7e94ed1f808efd9195060d8"></a>

### [`00b62aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md) → [`00b62af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md) _ZN8firebase4auth31recent_login_required_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b62b0c",
      "incomplete_value": false,
      "site": "00b62b10",
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
      "definition_site": "00b62ac8",
      "incomplete_value": false,
      "site": "00b62acc",
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
      "definition_site": "00b62b1c",
      "incomplete_value": true,
      "site": "00b62b28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62ad8",
      "incomplete_value": true,
      "site": "00b62ae4",
      "value": [
        "LOAD",
        "8",
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
      "00b62b0c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b62b1c",
      "DATA",
      [
        "storage",
        "010a1638",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62b0c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b62b1c",
      "DATA",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62acc) · [`00b62ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62ac8) · [`00b62ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62ad4)
- 新版 [`00b62b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b10) · [`00b62b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b0c) · [`00b62b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b18)

~~~diff
- 00b62acc ["INT_ADD", "register:40f0:8", ["const:b62acc:8", "const:4:8"]]
- 00b62acc ["CALL", null, ["callee:00bde180:8"]]
+ 00b62b10 ["INT_ADD", "register:40f0:8", ["const:b62b10:8", "const:4:8"]]
+ 00b62b10 ["CALL", null, ["callee:00bde180:8"]]
- 00b62acc bytes 99ed0194
+ 00b62b10 bytes 9ced0194
- 00b62ac8 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b62ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62b0c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b62b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62ac8 bytes 00fc1991
+ 00b62b0c bytes 00c81791
- 00b62ad4 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00b62ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62b18 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00b62b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62ad4 bytes 08e11891
+ 00b62b18 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c29afcf656bf2b09934a84ff2816c7e9"></a>

### [`00b62ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md) → [`00b62b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

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
      "definition_site": "00b62b58",
      "incomplete_value": true,
      "site": "00b62b58",
      "value": [
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
    "old": {
      "definition_site": "00b62b14",
      "incomplete_value": true,
      "site": "00b62b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62b40",
      "incomplete_value": true,
      "site": "00b62b40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62afc",
      "incomplete_value": true,
      "site": "00b62afc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62b4c",
      "incomplete_value": false,
      "site": "00b62b50",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b08",
      "incomplete_value": false,
      "site": "00b62b0c",
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
            "const:4d0:8"
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
      "00b62b3c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b4c",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62b58",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62b3c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b4c",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62b58",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62b0c) · [`00b62b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62b14) · [`00b62af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62af8)
- 新版 [`00b62b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b50) · [`00b62b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b58) · [`00b62b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b3c)

~~~diff
- 00b62b0c ["INT_ADD", "register:40f0:8", ["const:b62b0c:8", "const:4:8"]]
- 00b62b0c ["CALL", null, ["callee:00bde090:8"]]
+ 00b62b50 ["INT_ADD", "register:40f0:8", ["const:b62b50:8", "const:4:8"]]
+ 00b62b50 ["CALL", null, ["callee:00bde090:8"]]
- 00b62b0c bytes 4ded0194
+ 00b62b50 bytes 50ed0194
- 00b62b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62b58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b14 bytes 602203f9
+ 00b62b58 bytes 604203f9
- 00b62af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62af8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62b3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62af8 bytes 682243f9
+ 00b62b3c bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6b3dd289575d194fda360e957ff7fd4"></a>

### [`00b62b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md) → [`00b62b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

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
      "definition_site": "00b62b98",
      "incomplete_value": true,
      "site": "00b62b98",
      "value": [
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
    "old": {
      "definition_site": "00b62b54",
      "incomplete_value": true,
      "site": "00b62b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62b80",
      "incomplete_value": true,
      "site": "00b62b80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b3c",
      "incomplete_value": true,
      "site": "00b62b3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62b88",
      "incomplete_value": false,
      "site": "00b62b90",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b44",
      "incomplete_value": false,
      "site": "00b62b4c",
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
            "const:4d0:8"
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
      "00b62b7c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b88",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62b98",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62b7c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b88",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62b98",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b4c) · [`00b62b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b54) · [`00b62b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b38)
- 新版 [`00b62b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b90) · [`00b62b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b98) · [`00b62b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b7c)

~~~diff
- 00b62b4c ["INT_ADD", "register:40f0:8", ["const:b62b4c:8", "const:4:8"]]
- 00b62b4c ["CALL", null, ["callee:00bde090:8"]]
+ 00b62b90 ["INT_ADD", "register:40f0:8", ["const:b62b90:8", "const:4:8"]]
+ 00b62b90 ["CALL", null, ["callee:00bde090:8"]]
- 00b62b4c bytes 3ded0194
+ 00b62b90 bytes 40ed0194
- 00b62b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b54 bytes 602203f9
+ 00b62b98 bytes 604203f9
- 00b62b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62b38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62b7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62b38 bytes 682243f9
+ 00b62b7c bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54dbaa6fceb963d591985c4d67dde93f"></a>

### [`00b62b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md) → [`00b62bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62bdc",
      "incomplete_value": true,
      "site": "00b62bdc",
      "value": [
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
    "old": {
      "definition_site": "00b62b98",
      "incomplete_value": true,
      "site": "00b62b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62bc0",
      "incomplete_value": true,
      "site": "00b62bc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b7c",
      "incomplete_value": true,
      "site": "00b62b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62bcc",
      "incomplete_value": false,
      "site": "00b62bd4",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b88",
      "incomplete_value": false,
      "site": "00b62b90",
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
            "const:4d0:8"
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
      "00b62bbc",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62bcc",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62bdc",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62bbc",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62bcc",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62bdc",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b90) · [`00b62b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b98) · [`00b62b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b78)
- 新版 [`00b62bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bd4) · [`00b62bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bdc) · [`00b62bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bbc)

~~~diff
- 00b62b90 ["INT_ADD", "register:40f0:8", ["const:b62b90:8", "const:4:8"]]
- 00b62b90 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62bd4 ["INT_ADD", "register:40f0:8", ["const:b62bd4:8", "const:4:8"]]
+ 00b62bd4 ["CALL", null, ["callee:00bde090:8"]]
- 00b62b90 bytes 2ced0194
+ 00b62bd4 bytes 2fed0194
- 00b62b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62bdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b98 bytes 602203f9
+ 00b62bdc bytes 604203f9
- 00b62b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62b78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62b78 bytes 682243f9
+ 00b62bbc bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35bcc2bc3db8da9393778397029e6bce"></a>

### [`00b62bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md) → [`00b62bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62c20",
      "incomplete_value": true,
      "site": "00b62c20",
      "value": [
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
    "old": {
      "definition_site": "00b62bdc",
      "incomplete_value": true,
      "site": "00b62bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62c04",
      "incomplete_value": true,
      "site": "00b62c04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62bc0",
      "incomplete_value": true,
      "site": "00b62bc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62c0c",
      "incomplete_value": false,
      "site": "00b62c18",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62bc8",
      "incomplete_value": false,
      "site": "00b62bd4",
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
            "const:4d0:8"
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
      "00b62c00",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c0c",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62c20",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62c00",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c0c",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62c20",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bd4) · [`00b62bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bdc) · [`00b62bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bbc)
- 新版 [`00b62c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c18) · [`00b62c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c20) · [`00b62c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c00)

~~~diff
- 00b62bd4 ["INT_ADD", "register:40f0:8", ["const:b62bd4:8", "const:4:8"]]
- 00b62bd4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62c18 ["INT_ADD", "register:40f0:8", ["const:b62c18:8", "const:4:8"]]
+ 00b62c18 ["CALL", null, ["callee:00bde090:8"]]
- 00b62bd4 bytes 1bed0194
+ 00b62c18 bytes 1eed0194
- 00b62bdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62c20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62bdc bytes 602203f9
+ 00b62c20 bytes 604203f9
- 00b62bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b62c00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62bbc bytes 682243f9
+ 00b62c00 bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88c61efa1eb7b44996d9379d77df3a8b"></a>

### [`00b62bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md) → [`00b62c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md) _ZN8firebase4auth24user_collision_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62c98",
      "incomplete_value": true,
      "site": "00b62c98",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62c54",
      "incomplete_value": true,
      "site": "00b62c54",
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
            "const:648:8"
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
      "definition_site": "00b62c74",
      "incomplete_value": true,
      "site": "00b62c80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:680:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62c30",
      "incomplete_value": true,
      "site": "00b62c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:640:8"
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
      "00b62c54",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62c74",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c98",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62c54",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62c74",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c98",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c10) · [`00b62c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c3c) · [`00b62c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c54)
- 新版 [`00b62c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md#insn-00b62c54) · [`00b62c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md#insn-00b62c80) · [`00b62c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md#insn-00b62c98)

~~~diff
- 00b62c10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
- 00b62c10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62c10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b62c54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
+ 00b62c54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b62c54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62c10 bytes a8225939
+ 00b62c54 bytes a8225a39
- 00b62c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62c3c ["INT_ADD", "register:40f0:8", ["const:b62c3c:8", "const:4:8"]]
- 00b62c3c ["CALLIND", null, ["register:0:8"]]
+ 00b62c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62c80 ["INT_ADD", "register:40f0:8", ["const:b62c80:8", "const:4:8"]]
+ 00b62c80 ["CALLIND", null, ["register:0:8"]]
- 00b62c3c bytes 00013fd6
+ 00b62c80 bytes 00013fd6
- 00b62c54 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62c54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
- 00b62c54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62c98 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62c98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
+ 00b62c98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62c54 bytes a0221939
+ 00b62c98 bytes a0221a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-064a83e94ce77cdc01b0a32175933e13"></a>

### [`00b62c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md) → [`00b62cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md) _ZN8firebase4auth24user_collision_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b62ce8",
      "incomplete_value": true,
      "site": "00b62ce8",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ca4",
      "incomplete_value": true,
      "site": "00b62ca4",
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
            "const:648:8"
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
      "definition_site": "00b62d08",
      "incomplete_value": true,
      "site": "00b62d08",
      "value": [
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
    "old": {
      "definition_site": "00b62cc4",
      "incomplete_value": true,
      "site": "00b62cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62cc4",
      "incomplete_value": true,
      "site": "00b62cc4",
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
      "definition_site": "00b62c80",
      "incomplete_value": true,
      "site": "00b62c80",
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
      "00b62cc0",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ccc",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62ce8",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62cc0",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ccc",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62ce8",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62c7c) · [`00b62ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62ca4) · [`00b62cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62cc0)
- 新版 [`00b62cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62cc0) · [`00b62ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62ce8) · [`00b62d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62d04)

~~~diff
- 00b62c7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62c7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62cc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b62cc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62c7c bytes 812243f9
+ 00b62cc0 bytes 814243f9
- 00b62ca4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62ca4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62ca4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
- 00b62ca4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b62ce8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b62ce8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b62ce8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
+ 00b62ce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62ca4 bytes bf221939
+ 00b62ce8 bytes bf221a39
- 00b62cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62cc0 ["INT_ADD", "register:40f0:8", ["const:b62cc0:8", "const:4:8"]]
- 00b62cc0 ["CALLIND", null, ["register:0:8"]]
+ 00b62d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62d04 ["INT_ADD", "register:40f0:8", ["const:b62d04:8", "const:4:8"]]
+ 00b62d04 ["CALLIND", null, ["register:0:8"]]
- 00b62cc0 bytes 00013fd6
+ 00b62d04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fb1951b26fae2d971d066624b0a5d82"></a>

### [`00b62cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md) → [`00b62d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md) _ZN8firebase4auth24user_collision_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62d5c",
      "incomplete_value": true,
      "site": "00b62d5c",
      "value": [
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
    "old": {
      "definition_site": "00b62d18",
      "incomplete_value": true,
      "site": "00b62d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62d38",
      "incomplete_value": true,
      "site": "00b62d38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62cf4",
      "incomplete_value": true,
      "site": "00b62cf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62d40",
      "incomplete_value": false,
      "site": "00b62d54",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62cfc",
      "incomplete_value": false,
      "site": "00b62d10",
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
            "const:4d0:8"
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
      "00b62d30",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62d40",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62d5c",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62d30",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62d40",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62d5c",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62d10) · [`00b62d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62d18) · [`00b62cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62cec)
- 新版 [`00b62d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d54) · [`00b62d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d5c) · [`00b62d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d30)

~~~diff
- 00b62d10 ["INT_ADD", "register:40f0:8", ["const:b62d10:8", "const:4:8"]]
- 00b62d10 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62d54 ["INT_ADD", "register:40f0:8", ["const:b62d54:8", "const:4:8"]]
+ 00b62d54 ["CALL", null, ["callee:00bde090:8"]]
- 00b62d10 bytes ccec0194
+ 00b62d54 bytes cfec0194
- 00b62d18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62d5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b62d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62d18 bytes 802203f9
+ 00b62d5c bytes 804203f9
- 00b62cec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62cec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62d30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b62d30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62cec bytes 812243f9
+ 00b62d30 bytes 814243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89276a4853af4a3a730e27a1571899d4"></a>

### [`00b62d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md) → [`00b62d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md) _ZN8firebase4auth24user_collision_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62da8",
      "incomplete_value": false,
      "site": "00b62dac",
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
      "definition_site": "00b62d64",
      "incomplete_value": false,
      "site": "00b62d68",
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
      "definition_site": "00b62db8",
      "incomplete_value": true,
      "site": "00b62dc4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62d74",
      "incomplete_value": true,
      "site": "00b62d80",
      "value": [
        "LOAD",
        "8",
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
      "00b62da8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62db8",
      "DATA",
      [
        "storage",
        "010a1650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62da8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62db8",
      "DATA",
      [
        "storage",
        "010a1690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d68) · [`00b62d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d64) · [`00b62d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d70)
- 新版 [`00b62dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62dac) · [`00b62da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62da8) · [`00b62db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62db4)

~~~diff
- 00b62d68 ["INT_ADD", "register:40f0:8", ["const:b62d68:8", "const:4:8"]]
- 00b62d68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b62dac ["INT_ADD", "register:40f0:8", ["const:b62dac:8", "const:4:8"]]
+ 00b62dac ["CALL", null, ["callee:00bde180:8"]]
- 00b62d68 bytes f2ec0194
+ 00b62dac bytes f5ec0194
- 00b62d64 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b62d64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62d64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62d64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62da8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b62da8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62da8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62da8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62d64 bytes 00501791
+ 00b62da8 bytes 001c1591
- 00b62d70 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00b62d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62db4 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00b62db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62d70 bytes 08411991
+ 00b62db4 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3b385aecfb737f24a09ced5280c28d"></a>

### [`00b62d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md) → [`00b62dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md) _ZN8firebase4auth24user_collision_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62e08",
      "incomplete_value": true,
      "site": "00b62e08",
      "value": [
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
    "old": {
      "definition_site": "00b62dc4",
      "incomplete_value": true,
      "site": "00b62dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b62de4",
      "incomplete_value": true,
      "site": "00b62de4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62da0",
      "incomplete_value": true,
      "site": "00b62da0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b62dec",
      "incomplete_value": false,
      "site": "00b62e00",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62da8",
      "incomplete_value": false,
      "site": "00b62dbc",
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
            "const:4d0:8"
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
      "00b62ddc",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62dec",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62e08",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62ddc",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62dec",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62e08",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62dbc) · [`00b62dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62dc4) · [`00b62d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62d98)
- 新版 [`00b62e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62e00) · [`00b62e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62e08) · [`00b62ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62ddc)

~~~diff
- 00b62dbc ["INT_ADD", "register:40f0:8", ["const:b62dbc:8", "const:4:8"]]
- 00b62dbc ["CALL", null, ["callee:00bde090:8"]]
+ 00b62e00 ["INT_ADD", "register:40f0:8", ["const:b62e00:8", "const:4:8"]]
+ 00b62e00 ["CALL", null, ["callee:00bde090:8"]]
- 00b62dbc bytes a1ec0194
+ 00b62e00 bytes a4ec0194
- 00b62dc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b62e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62dc4 bytes 802203f9
+ 00b62e08 bytes 804203f9
- 00b62d98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62d98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62ddc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b62ddc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62d98 bytes 812243f9
+ 00b62ddc bytes 814243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10704aff17fe9a59a792c0e93c81b544"></a>

### [`00b62df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md) → [`00b62e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md) _ZN8firebase4auth24user_collision_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b62e54",
      "incomplete_value": false,
      "site": "00b62e58",
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
      "definition_site": "00b62e10",
      "incomplete_value": false,
      "site": "00b62e14",
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
      "definition_site": "00b62e64",
      "incomplete_value": true,
      "site": "00b62e70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62e20",
      "incomplete_value": true,
      "site": "00b62e2c",
      "value": [
        "LOAD",
        "8",
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
      "00b62e54",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b62e64",
      "DATA",
      [
        "storage",
        "010a1658",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62e54",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b62e64",
      "DATA",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e14) · [`00b62e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e10) · [`00b62e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e1c)
- 新版 [`00b62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e58) · [`00b62e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e54) · [`00b62e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e60)

~~~diff
- 00b62e14 ["INT_ADD", "register:40f0:8", ["const:b62e14:8", "const:4:8"]]
- 00b62e14 ["CALL", null, ["callee:00bde180:8"]]
+ 00b62e58 ["INT_ADD", "register:40f0:8", ["const:b62e58:8", "const:4:8"]]
+ 00b62e58 ["CALL", null, ["callee:00bde180:8"]]
- 00b62e14 bytes c7ec0194
+ 00b62e58 bytes caec0194
- 00b62e10 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b62e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62e54 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b62e54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62e54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62e54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62e10 bytes 00fc1991
+ 00b62e54 bytes 00c81791
- 00b62e1c ["COPY", "tmp:0:8", ["const:658:8"]]
- 00b62e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62e60 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00b62e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62e1c bytes 08611991
+ 00b62e60 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2fa68139bb6dbeadc139c289aad539"></a>

### [`00b62e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md) → [`00b62e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b62ea0",
      "incomplete_value": true,
      "site": "00b62ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e5c",
      "incomplete_value": true,
      "site": "00b62e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b62e88",
      "incomplete_value": true,
      "site": "00b62e88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e44",
      "incomplete_value": true,
      "site": "00b62e44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62e44"
      ],
      [
        "FALL_THROUGH",
        "00b62e88"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62e88",
      "incomplete_value": true,
      "site": "00b62ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e44",
      "incomplete_value": true,
      "site": "00b62e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62e84",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ea0",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62e84",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ea0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e5c) · [`00b62e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e40) · [`00b62e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e54)
- 新版 [`00b62ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62ea0) · [`00b62e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62e84) · [`00b62e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62e98)

~~~diff
- 00b62e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62e5c bytes 603203f9
+ 00b62ea0 bytes 605203f9
- 00b62e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62e40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62e84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62e84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62e40 bytes 683243f9
+ 00b62e84 bytes 685243f9
- 00b62e54 ["INT_ADD", "register:40f0:8", ["const:b62e54:8", "const:4:8"]]
- 00b62e54 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62e98 ["INT_ADD", "register:40f0:8", ["const:b62e98:8", "const:4:8"]]
+ 00b62e98 ["CALL", null, ["callee:00bde090:8"]]
- 00b62e54 bytes 7bec0194
+ 00b62e98 bytes 7eec0194
~~~


<a id="compare-2b2e84812fdef6316a43464c57e3a7ad"></a>

### [`00b62e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md) → [`00b62eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b62ee0",
      "incomplete_value": true,
      "site": "00b62ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e9c",
      "incomplete_value": true,
      "site": "00b62e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b62ec8",
      "incomplete_value": true,
      "site": "00b62ec8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e84",
      "incomplete_value": true,
      "site": "00b62e84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62e84"
      ],
      [
        "FALL_THROUGH",
        "00b62ec8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62ec8",
      "incomplete_value": true,
      "site": "00b62ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e84",
      "incomplete_value": true,
      "site": "00b62e9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62ec4",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ee0",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62ec4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ee0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e9c) · [`00b62e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e80) · [`00b62e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e94)
- 新版 [`00b62ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62ee0) · [`00b62ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62ec4) · [`00b62ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62ed8)

~~~diff
- 00b62e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62ee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62e9c bytes 603203f9
+ 00b62ee0 bytes 605203f9
- 00b62e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62ec4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62e80 bytes 683243f9
+ 00b62ec4 bytes 685243f9
- 00b62e94 ["INT_ADD", "register:40f0:8", ["const:b62e94:8", "const:4:8"]]
- 00b62e94 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62ed8 ["INT_ADD", "register:40f0:8", ["const:b62ed8:8", "const:4:8"]]
+ 00b62ed8 ["CALL", null, ["callee:00bde090:8"]]
- 00b62e94 bytes 6bec0194
+ 00b62ed8 bytes 6eec0194
~~~


<a id="compare-f647dfbf5fa0e014a988acfbf2247add"></a>

### [`00b62eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md) → [`00b62ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62f24",
      "incomplete_value": true,
      "site": "00b62f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ee0",
      "incomplete_value": true,
      "site": "00b62ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ec4",
      "incomplete_value": true,
      "site": "00b62ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62ec4"
      ],
      [
        "FALL_THROUGH",
        "00b62f08"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ec4",
      "incomplete_value": true,
      "site": "00b62ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62f04",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f24",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62f04",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f24",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ee0) · [`00b62ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ec0) · [`00b62ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ed8)
- 新版 [`00b62f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f24) · [`00b62f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f04) · [`00b62f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f1c)

~~~diff
- 00b62ee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62f24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62ee0 bytes 603203f9
+ 00b62f24 bytes 605203f9
- 00b62ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62ec0 bytes 683243f9
+ 00b62f04 bytes 685243f9
- 00b62ed8 ["INT_ADD", "register:40f0:8", ["const:b62ed8:8", "const:4:8"]]
- 00b62ed8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b62f1c ["INT_ADD", "register:40f0:8", ["const:b62f1c:8", "const:4:8"]]
+ 00b62f1c ["CALL", null, ["callee:00bde090:8"]]
- 00b62ed8 bytes 5aec0194
+ 00b62f1c bytes 5dec0194
~~~


<a id="compare-cc41f219692e8308f36ea0dd0aba309b"></a>

### [`00b62ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md) → [`00b62f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62f68",
      "incomplete_value": true,
      "site": "00b62f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f24",
      "incomplete_value": true,
      "site": "00b62f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b62f4c",
      "incomplete_value": true,
      "site": "00b62f4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b62f08"
      ],
      [
        "FALL_THROUGH",
        "00b62f4c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62f4c",
      "incomplete_value": true,
      "site": "00b62f68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62f48",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f68",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62f48",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f68",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f24) · [`00b62f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f04) · [`00b62f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f1c)
- 新版 [`00b62f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f68) · [`00b62f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f48) · [`00b62f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f60)

~~~diff
- 00b62f24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62f68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62f24 bytes 603203f9
+ 00b62f68 bytes 605203f9
- 00b62f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b62f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62f04 bytes 683243f9
+ 00b62f48 bytes 685243f9
- 00b62f1c ["INT_ADD", "register:40f0:8", ["const:b62f1c:8", "const:4:8"]]
- 00b62f1c ["CALL", null, ["callee:00bde090:8"]]
+ 00b62f60 ["INT_ADD", "register:40f0:8", ["const:b62f60:8", "const:4:8"]]
+ 00b62f60 ["CALL", null, ["callee:00bde090:8"]]
- 00b62f1c bytes 49ec0194
+ 00b62f60 bytes 4cec0194
~~~


<a id="compare-1de96ba2608d1f32ed8637f7d492b0ab"></a>

### [`00b62f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md) → [`00b62f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md) _ZN8firebase4auth21android_web_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62fe0",
      "incomplete_value": true,
      "site": "00b62fe0",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f9c",
      "incomplete_value": true,
      "site": "00b62f9c",
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
            "const:668:8"
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
      "definition_site": "00b62fbc",
      "incomplete_value": true,
      "site": "00b62fc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f78",
      "incomplete_value": true,
      "site": "00b62f84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:660:8"
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
      "00b62f9c",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62fbc",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62fe0",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62f9c",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62fbc",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62fe0",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f58) · [`00b62f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f84) · [`00b62f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f9c)
- 新版 [`00b62f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62f9c) · [`00b62fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62fc8) · [`00b62fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62fe0)

~~~diff
- 00b62f58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:668:8"]]
- 00b62f58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62f58 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b62f9c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b62f9c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b62f9c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62f58 bytes a8a25939
+ 00b62f9c bytes a8a25a39
- 00b62f84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62f84 ["INT_ADD", "register:40f0:8", ["const:b62f84:8", "const:4:8"]]
- 00b62f84 ["CALLIND", null, ["register:0:8"]]
+ 00b62fc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62fc8 ["INT_ADD", "register:40f0:8", ["const:b62fc8:8", "const:4:8"]]
+ 00b62fc8 ["CALLIND", null, ["register:0:8"]]
- 00b62f84 bytes 00013fd6
+ 00b62fc8 bytes 00013fd6
- 00b62f9c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62f9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:668:8"]]
- 00b62f9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62fe0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62fe0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b62fe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62f9c bytes a0a21939
+ 00b62fe0 bytes a0a21a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d7f142d8274bb6822c03e74433014e"></a>

### [`00b62fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md) → [`00b62ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md) _ZN8firebase4auth21android_web_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b63030",
      "incomplete_value": true,
      "site": "00b63030",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62fec",
      "incomplete_value": true,
      "site": "00b62fec",
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
            "const:668:8"
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
      "definition_site": "00b63050",
      "incomplete_value": true,
      "site": "00b63050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6300c",
      "incomplete_value": true,
      "site": "00b6300c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b6300c",
      "incomplete_value": true,
      "site": "00b6300c",
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
      "definition_site": "00b62fc8",
      "incomplete_value": true,
      "site": "00b62fc8",
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
      "00b63008",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63014",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63030",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63008",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63014",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63030",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b62fc4) · [`00b62fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b62fec) · [`00b63008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b63008)
- 新版 [`00b63008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b63008) · [`00b63030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b63030) · [`00b6304c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b6304c)

~~~diff
- 00b62fc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b62fc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63008 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b63008 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62fc4 bytes 813243f9
+ 00b63008 bytes 815243f9
- 00b62fec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62fec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62fec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:668:8"]]
- 00b62fec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b63030 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b63030 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b63030 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b63030 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62fec bytes bfa21939
+ 00b63030 bytes bfa21a39
- 00b63008 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63008 ["INT_ADD", "register:40f0:8", ["const:b63008:8", "const:4:8"]]
- 00b63008 ["CALLIND", null, ["register:0:8"]]
+ 00b6304c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6304c ["INT_ADD", "register:40f0:8", ["const:b6304c:8", "const:4:8"]]
+ 00b6304c ["CALLIND", null, ["register:0:8"]]
- 00b63008 bytes 00013fd6
+ 00b6304c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2602dbc30bad3dc77257a39f83521ced"></a>

### [`00b63020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md) → [`00b63064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md) _ZN8firebase4auth21android_web_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b630a4",
      "incomplete_value": true,
      "site": "00b630a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63060",
      "incomplete_value": true,
      "site": "00b63060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b63080",
      "incomplete_value": true,
      "site": "00b63080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6303c",
      "incomplete_value": true,
      "site": "00b6303c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6303c"
      ],
      [
        "FALL_THROUGH",
        "00b63080"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63080",
      "incomplete_value": true,
      "site": "00b630a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6303c",
      "incomplete_value": true,
      "site": "00b63060",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63078",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b630a4",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b630bc",
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
      "00b63078",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b630a4",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b630bc",
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

- 旧版 [`00b63060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63060) · [`00b63034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63034) · [`00b63058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63058)
- 新版 [`00b630a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b630a4) · [`00b63078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b63078) · [`00b6309c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b6309c)

~~~diff
- 00b63060 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b63060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b630a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b630a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63060 bytes 803203f9
+ 00b630a4 bytes 805203f9
- 00b63034 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b63034 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63078 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b63078 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63034 bytes 813243f9
+ 00b63078 bytes 815243f9
- 00b63058 ["INT_ADD", "register:40f0:8", ["const:b63058:8", "const:4:8"]]
- 00b63058 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6309c ["INT_ADD", "register:40f0:8", ["const:b6309c:8", "const:4:8"]]
+ 00b6309c ["CALL", null, ["callee:00bde090:8"]]
- 00b63058 bytes faeb0194
+ 00b6309c bytes fdeb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a939295b1621a514ad41f11062859f7"></a>

### [`00b63090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md) → [`00b630d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md) _ZN8firebase4auth21android_web_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b630f0",
      "incomplete_value": false,
      "site": "00b630f4",
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
      "definition_site": "00b630ac",
      "incomplete_value": false,
      "site": "00b630b0",
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
      "definition_site": "00b63100",
      "incomplete_value": true,
      "site": "00b6310c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b630bc",
      "incomplete_value": true,
      "site": "00b630c8",
      "value": [
        "LOAD",
        "8",
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
      "00b630f0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63100",
      "DATA",
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
      "00b630f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63100",
      "DATA",
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

- 旧版 [`00b630b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630b0) · [`00b630ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630ac) · [`00b630b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630b8)
- 新版 [`00b630f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630f4) · [`00b630f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630f0) · [`00b630fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630fc)

~~~diff
- 00b630b0 ["INT_ADD", "register:40f0:8", ["const:b630b0:8", "const:4:8"]]
- 00b630b0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b630f4 ["INT_ADD", "register:40f0:8", ["const:b630f4:8", "const:4:8"]]
+ 00b630f4 ["CALL", null, ["callee:00bde180:8"]]
- 00b630b0 bytes 20ec0194
+ 00b630f4 bytes 23ec0194
- 00b630ac ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b630ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b630ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b630ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b630f0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b630f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b630f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b630f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b630ac bytes 00501791
+ 00b630f0 bytes 001c1591
- 00b630b8 ["COPY", "tmp:0:8", ["const:670:8"]]
- 00b630b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b630b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b630b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b630fc ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00b630fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b630fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b630fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b630b8 bytes 08c11991
+ 00b630fc bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-298ecf93cc6aca56e7aa1583782135f9"></a>

### [`00b630cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md) → [`00b63110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md) _ZN8firebase4auth21android_web_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63150",
      "incomplete_value": true,
      "site": "00b63150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6310c",
      "incomplete_value": true,
      "site": "00b6310c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b6312c",
      "incomplete_value": true,
      "site": "00b6312c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b630e8",
      "incomplete_value": true,
      "site": "00b630e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b630e8"
      ],
      [
        "FALL_THROUGH",
        "00b6312c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6312c",
      "incomplete_value": true,
      "site": "00b63150",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b630e8",
      "incomplete_value": true,
      "site": "00b6310c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63124",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63150",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63168",
      "PARAM",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63124",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63150",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63168",
      "PARAM",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6310c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b6310c) · [`00b630e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b630e0) · [`00b63104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b63104)
- 新版 [`00b63150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b63150) · [`00b63124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b63124) · [`00b63148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b63148)

~~~diff
- 00b6310c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b6310c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63150 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b63150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6310c bytes 803203f9
+ 00b63150 bytes 805203f9
- 00b630e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b630e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63124 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b63124 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b630e0 bytes 813243f9
+ 00b63124 bytes 815243f9
- 00b63104 ["INT_ADD", "register:40f0:8", ["const:b63104:8", "const:4:8"]]
- 00b63104 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63148 ["INT_ADD", "register:40f0:8", ["const:b63148:8", "const:4:8"]]
+ 00b63148 ["CALL", null, ["callee:00bde090:8"]]
- 00b63104 bytes cfeb0194
+ 00b63148 bytes d2eb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22c31b379c70f0f1474ff258b35964b6"></a>

### [`00b6313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md) → [`00b63180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md) _ZN8firebase4auth21android_web_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6319c",
      "incomplete_value": false,
      "site": "00b631a0",
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
      "definition_site": "00b63158",
      "incomplete_value": false,
      "site": "00b6315c",
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
      "definition_site": "00b631ac",
      "incomplete_value": true,
      "site": "00b631b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63168",
      "incomplete_value": true,
      "site": "00b63174",
      "value": [
        "LOAD",
        "8",
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
      "00b6319c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b631ac",
      "DATA",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6319c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b631ac",
      "DATA",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6315c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b6315c) · [`00b63158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b63158) · [`00b63164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b63164)
- 新版 [`00b631a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b631a0) · [`00b6319c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b6319c) · [`00b631a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b631a8)

~~~diff
- 00b6315c ["INT_ADD", "register:40f0:8", ["const:b6315c:8", "const:4:8"]]
- 00b6315c ["CALL", null, ["callee:00bde180:8"]]
+ 00b631a0 ["INT_ADD", "register:40f0:8", ["const:b631a0:8", "const:4:8"]]
+ 00b631a0 ["CALL", null, ["callee:00bde180:8"]]
- 00b6315c bytes f5eb0194
+ 00b631a0 bytes f8eb0194
- 00b63158 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b63158 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63158 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63158 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6319c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6319c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6319c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6319c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63158 bytes 00fc1991
+ 00b6319c bytes 00c81791
- 00b63164 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00b63164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b631a8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00b631a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b631a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b631a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63164 bytes 08e11991
+ 00b631a8 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b112c1e59ab545022e94be4ccb74d4"></a>

### [`00b63178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md) → [`00b631bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b631e8",
      "incomplete_value": true,
      "site": "00b631e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631a4",
      "incomplete_value": true,
      "site": "00b631a4",
      "value": [
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
      "definition_site": "00b631d0",
      "incomplete_value": true,
      "site": "00b631d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6318c",
      "incomplete_value": true,
      "site": "00b6318c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6318c"
      ],
      [
        "FALL_THROUGH",
        "00b631d0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b631d0",
      "incomplete_value": true,
      "site": "00b631e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6318c",
      "incomplete_value": true,
      "site": "00b631a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b631cc",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b631e8",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b631cc",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b631e8",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b631a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b631a4) · [`00b63188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b63188) · [`00b6319c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b6319c)
- 新版 [`00b631e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631e8) · [`00b631cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631cc) · [`00b631e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631e0)

~~~diff
- 00b631a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b631a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b631e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b631e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b631a4 bytes 604203f9
+ 00b631e8 bytes 606203f9
- 00b63188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b63188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b631cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b631cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63188 bytes 684243f9
+ 00b631cc bytes 686243f9
- 00b6319c ["INT_ADD", "register:40f0:8", ["const:b6319c:8", "const:4:8"]]
- 00b6319c ["CALL", null, ["callee:00bde090:8"]]
+ 00b631e0 ["INT_ADD", "register:40f0:8", ["const:b631e0:8", "const:4:8"]]
+ 00b631e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6319c bytes a9eb0194
+ 00b631e0 bytes aceb0194
~~~


<a id="compare-0d22568d9c4eafb04fa419362e161d04"></a>

### [`00b631b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md) → [`00b631fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b63228",
      "incomplete_value": true,
      "site": "00b63228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631e4",
      "incomplete_value": true,
      "site": "00b631e4",
      "value": [
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
      "definition_site": "00b63210",
      "incomplete_value": true,
      "site": "00b63210",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631cc",
      "incomplete_value": true,
      "site": "00b631cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b631cc"
      ],
      [
        "FALL_THROUGH",
        "00b63210"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63210",
      "incomplete_value": true,
      "site": "00b63228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631cc",
      "incomplete_value": true,
      "site": "00b631e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6320c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63228",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6320c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63228",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b631e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631e4) · [`00b631c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631c8) · [`00b631dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631dc)
- 新版 [`00b63228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b63228) · [`00b6320c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b6320c) · [`00b63220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b63220)

~~~diff
- 00b631e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b631e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b631e4 bytes 604203f9
+ 00b63228 bytes 606203f9
- 00b631c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b631c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6320c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b6320c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b631c8 bytes 684243f9
+ 00b6320c bytes 686243f9
- 00b631dc ["INT_ADD", "register:40f0:8", ["const:b631dc:8", "const:4:8"]]
- 00b631dc ["CALL", null, ["callee:00bde090:8"]]
+ 00b63220 ["INT_ADD", "register:40f0:8", ["const:b63220:8", "const:4:8"]]
+ 00b63220 ["CALL", null, ["callee:00bde090:8"]]
- 00b631dc bytes 99eb0194
+ 00b63220 bytes 9ceb0194
~~~


<a id="compare-848a886e06787522665f0f92cf2ae1b7"></a>

### [`00b631f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md) → [`00b6323c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6326c",
      "incomplete_value": true,
      "site": "00b6326c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63228",
      "incomplete_value": true,
      "site": "00b63228",
      "value": [
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
      "definition_site": "00b63250",
      "incomplete_value": true,
      "site": "00b63250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6320c",
      "incomplete_value": true,
      "site": "00b6320c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6320c"
      ],
      [
        "FALL_THROUGH",
        "00b63250"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63250",
      "incomplete_value": true,
      "site": "00b6326c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6320c",
      "incomplete_value": true,
      "site": "00b63228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6324c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6326c",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6324c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6326c",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63228) · [`00b63208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63208) · [`00b63220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63220)
- 新版 [`00b6326c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b6326c) · [`00b6324c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b6324c) · [`00b63264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b63264)

~~~diff
- 00b63228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b63228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6326c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b6326c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63228 bytes 604203f9
+ 00b6326c bytes 606203f9
- 00b63208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b63208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6324c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b6324c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63208 bytes 684243f9
+ 00b6324c bytes 686243f9
- 00b63220 ["INT_ADD", "register:40f0:8", ["const:b63220:8", "const:4:8"]]
- 00b63220 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63264 ["INT_ADD", "register:40f0:8", ["const:b63264:8", "const:4:8"]]
+ 00b63264 ["CALL", null, ["callee:00bde090:8"]]
- 00b63220 bytes 88eb0194
+ 00b63264 bytes 8beb0194
~~~


<a id="compare-d952c38eb194a226629e8a705642f87e"></a>

### [`00b6323c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md) → [`00b63280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b632b0",
      "incomplete_value": true,
      "site": "00b632b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6326c",
      "incomplete_value": true,
      "site": "00b6326c",
      "value": [
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
      "definition_site": "00b63294",
      "incomplete_value": true,
      "site": "00b63294",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63250",
      "incomplete_value": true,
      "site": "00b63250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63250"
      ],
      [
        "FALL_THROUGH",
        "00b63294"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63294",
      "incomplete_value": true,
      "site": "00b632b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63250",
      "incomplete_value": true,
      "site": "00b6326c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63290",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b632b0",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63290",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b632b0",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6326c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b6326c) · [`00b6324c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b6324c) · [`00b63264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b63264)
- 新版 [`00b632b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b632b0) · [`00b63290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b63290) · [`00b632a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b632a8)

~~~diff
- 00b6326c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b6326c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b632b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b632b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6326c bytes 604203f9
+ 00b632b0 bytes 606203f9
- 00b6324c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b6324c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63290 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6324c bytes 684243f9
+ 00b63290 bytes 686243f9
- 00b63264 ["INT_ADD", "register:40f0:8", ["const:b63264:8", "const:4:8"]]
- 00b63264 ["CALL", null, ["callee:00bde090:8"]]
+ 00b632a8 ["INT_ADD", "register:40f0:8", ["const:b632a8:8", "const:4:8"]]
+ 00b632a8 ["CALL", null, ["callee:00bde090:8"]]
- 00b63264 bytes 77eb0194
+ 00b632a8 bytes 7aeb0194
~~~


<a id="compare-399203e46b8cb92d1b07cdc1fd0023b8"></a>

### [`00b6328c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md) → [`00b632d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md) _ZN8firebase4auth23firebase_auth_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b63328",
      "incomplete_value": true,
      "site": "00b63328",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b632e4",
      "incomplete_value": true,
      "site": "00b632e4",
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
            "const:688:8"
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
      "definition_site": "00b63304",
      "incomplete_value": true,
      "site": "00b63310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b632c0",
      "incomplete_value": true,
      "site": "00b632cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b632e4",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63304",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63328",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b632e4",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63304",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63328",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b632a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632a0) · [`00b632cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632cc) · [`00b632e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632e4)
- 新版 [`00b632e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b632e4) · [`00b63310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b63310) · [`00b63328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b63328)

~~~diff
- 00b632a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
- 00b632a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b632a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b632e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b632e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b632e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b632a0 bytes a8225a39
+ 00b632e4 bytes a8225b39
- 00b632cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b632cc ["INT_ADD", "register:40f0:8", ["const:b632cc:8", "const:4:8"]]
- 00b632cc ["CALLIND", null, ["register:0:8"]]
+ 00b63310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63310 ["INT_ADD", "register:40f0:8", ["const:b63310:8", "const:4:8"]]
+ 00b63310 ["CALLIND", null, ["register:0:8"]]
- 00b632cc bytes 00013fd6
+ 00b63310 bytes 00013fd6
- 00b632e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b632e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
- 00b632e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b63328 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b63328 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b63328 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b632e4 bytes a0221a39
+ 00b63328 bytes a0221b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db8a16f3cb01aa485f806c253924b4f"></a>

### [`00b632f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md) → [`00b6333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md) _ZN8firebase4auth23firebase_auth_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b63378",
      "incomplete_value": true,
      "site": "00b63378",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63334",
      "incomplete_value": true,
      "site": "00b63334",
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
            "const:688:8"
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
      "definition_site": "00b63398",
      "incomplete_value": true,
      "site": "00b63398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63354",
      "incomplete_value": true,
      "site": "00b63354",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63354",
      "incomplete_value": true,
      "site": "00b63354",
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
      "definition_site": "00b63310",
      "incomplete_value": true,
      "site": "00b63310",
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
      "00b63350",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6335c",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63378",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63350",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6335c",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63378",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6330c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b6330c) · [`00b63334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b63334) · [`00b63350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b63350)
- 新版 [`00b63350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63350) · [`00b63378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63378) · [`00b63394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63394)

~~~diff
- 00b6330c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b6330c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63350 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6330c bytes 814243f9
+ 00b63350 bytes 816243f9
- 00b63334 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b63334 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b63334 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
- 00b63334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b63378 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b63378 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b63378 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b63378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b63334 bytes bf221a39
+ 00b63378 bytes bf221b39
- 00b63350 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63350 ["INT_ADD", "register:40f0:8", ["const:b63350:8", "const:4:8"]]
- 00b63350 ["CALLIND", null, ["register:0:8"]]
+ 00b63394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63394 ["INT_ADD", "register:40f0:8", ["const:b63394:8", "const:4:8"]]
+ 00b63394 ["CALLIND", null, ["register:0:8"]]
- 00b63350 bytes 00013fd6
+ 00b63394 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7595640ac8dd24e8aef624f7f51ceb2e"></a>

### [`00b63368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md) → [`00b633ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md) _ZN8firebase4auth23firebase_auth_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b633ec",
      "incomplete_value": true,
      "site": "00b633ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b633a8",
      "incomplete_value": true,
      "site": "00b633a8",
      "value": [
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
      "definition_site": "00b633c8",
      "incomplete_value": true,
      "site": "00b633c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63384",
      "incomplete_value": true,
      "site": "00b63384",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63384"
      ],
      [
        "FALL_THROUGH",
        "00b633c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b633c8",
      "incomplete_value": true,
      "site": "00b633ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63384",
      "incomplete_value": true,
      "site": "00b633a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b633c0",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b633ec",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63400",
      "PARAM",
      [
        "storage",
        "00c11e90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b633c0",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b633ec",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63400",
      "PARAM",
      [
        "storage",
        "00c11ee0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b633a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b633a8) · [`00b6337c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b6337c) · [`00b633a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b633a0)
- 新版 [`00b633ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633ec) · [`00b633c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633c0) · [`00b633e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633e4)

~~~diff
- 00b633a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b633a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b633ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b633ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b633a8 bytes 804203f9
+ 00b633ec bytes 806203f9
- 00b6337c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b6337c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b633c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b633c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6337c bytes 814243f9
+ 00b633c0 bytes 816243f9
- 00b633a0 ["INT_ADD", "register:40f0:8", ["const:b633a0:8", "const:4:8"]]
- 00b633a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b633e4 ["INT_ADD", "register:40f0:8", ["const:b633e4:8", "const:4:8"]]
+ 00b633e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b633a0 bytes 28eb0194
+ 00b633e4 bytes 2beb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7625a2344951e91338b23640f6de6022"></a>

### [`00b633d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md) → [`00b6341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6341c.md) _ZN8firebase4auth23firebase_auth_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b63438",
      "incomplete_value": false,
      "site": "00b6343c",
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
      "definition_site": "00b633f4",
      "incomplete_value": false,
      "site": "00b633f8",
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
      "definition_site": "00b63448",
      "incomplete_value": true,
      "site": "00b63454",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63404",
      "incomplete_value": true,
      "site": "00b63410",
      "value": [
        "LOAD",
        "8",
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
      "00b63438",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63448",
      "DATA",
      [
        "storage",
        "010a1690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63438",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63448",
      "DATA",
      [
        "storage",
        "010a16d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b633f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b633f8) · [`00b633f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b633f4) · [`00b63400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b63400)
- 新版 [`00b6343c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6341c.md#insn-00b6343c) · [`00b63438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6341c.md#insn-00b63438) · [`00b63444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6341c.md#insn-00b63444)

~~~diff
- 00b633f8 ["INT_ADD", "register:40f0:8", ["const:b633f8:8", "const:4:8"]]
- 00b633f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6343c ["INT_ADD", "register:40f0:8", ["const:b6343c:8", "const:4:8"]]
+ 00b6343c ["CALL", null, ["callee:00bde180:8"]]
- 00b633f8 bytes 4eeb0194
+ 00b6343c bytes 51eb0194
- 00b633f4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b633f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b633f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b633f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63438 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b63438 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63438 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63438 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b633f4 bytes 00501791
+ 00b63438 bytes 001c1591
- 00b63400 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00b63400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63444 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00b63444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63400 bytes 08411a91
+ 00b63444 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5585e7c85a7adf06ef615222d47e870a"></a>

### [`00b63414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md) → [`00b63458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md) _ZN8firebase4auth23firebase_auth_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63498",
      "incomplete_value": true,
      "site": "00b63498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63454",
      "incomplete_value": true,
      "site": "00b63454",
      "value": [
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
      "definition_site": "00b63474",
      "incomplete_value": true,
      "site": "00b63474",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63430",
      "incomplete_value": true,
      "site": "00b63430",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63430"
      ],
      [
        "FALL_THROUGH",
        "00b63474"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63474",
      "incomplete_value": true,
      "site": "00b63498",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63430",
      "incomplete_value": true,
      "site": "00b63454",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6346c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63498",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b634b0",
      "PARAM",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6346c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63498",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b634b0",
      "PARAM",
      [
        "storage",
        "010a16d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b63454) · [`00b63428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b63428) · [`00b6344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b6344c)
- 新版 [`00b63498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b63498) · [`00b6346c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b6346c) · [`00b63490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b63490)

~~~diff
- 00b63454 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b63454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63498 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63498 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63454 bytes 804203f9
+ 00b63498 bytes 806203f9
- 00b63428 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b63428 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6346c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b6346c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63428 bytes 814243f9
+ 00b6346c bytes 816243f9
- 00b6344c ["INT_ADD", "register:40f0:8", ["const:b6344c:8", "const:4:8"]]
- 00b6344c ["CALL", null, ["callee:00bde090:8"]]
+ 00b63490 ["INT_ADD", "register:40f0:8", ["const:b63490:8", "const:4:8"]]
+ 00b63490 ["CALL", null, ["callee:00bde090:8"]]
- 00b6344c bytes fdea0194
+ 00b63490 bytes 00eb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56e599b6c8412d9ce4f55f17342f1369"></a>

### [`00b63484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md) → [`00b634c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md) _ZN8firebase4auth23firebase_auth_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b634e4",
      "incomplete_value": false,
      "site": "00b634e8",
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
      "definition_site": "00b634a0",
      "incomplete_value": false,
      "site": "00b634a4",
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
      "definition_site": "00b634f4",
      "incomplete_value": true,
      "site": "00b63500",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b634b0",
      "incomplete_value": true,
      "site": "00b634bc",
      "value": [
        "LOAD",
        "8",
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
      "00b634e4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b634f4",
      "DATA",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b634e4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b634f4",
      "DATA",
      [
        "storage",
        "010a16d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b634a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634a4) · [`00b634a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634a0) · [`00b634ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634ac)
- 新版 [`00b634e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634e8) · [`00b634e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634e4) · [`00b634f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634f0)

~~~diff
- 00b634a4 ["INT_ADD", "register:40f0:8", ["const:b634a4:8", "const:4:8"]]
- 00b634a4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b634e8 ["INT_ADD", "register:40f0:8", ["const:b634e8:8", "const:4:8"]]
+ 00b634e8 ["CALL", null, ["callee:00bde180:8"]]
- 00b634a4 bytes 23eb0194
+ 00b634e8 bytes 26eb0194
- 00b634a0 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b634a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b634a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b634a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b634e4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b634e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b634e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b634e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b634a0 bytes 00fc1991
+ 00b634e4 bytes 00c81791
- 00b634ac ["COPY", "tmp:0:8", ["const:698:8"]]
- 00b634ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b634ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b634ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b634f0 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00b634f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b634f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b634f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b634ac bytes 08611a91
+ 00b634f0 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4296141312ba73e9bb2e57fe0cf95725"></a>

### [`00b634c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md) → [`00b63504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b63530",
      "incomplete_value": true,
      "site": "00b63530",
      "value": [
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
    "old": {
      "definition_site": "00b634ec",
      "incomplete_value": true,
      "site": "00b634ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b63518",
      "incomplete_value": true,
      "site": "00b63518",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b634d4",
      "incomplete_value": true,
      "site": "00b634d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b634d4"
      ],
      [
        "FALL_THROUGH",
        "00b63518"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63518",
      "incomplete_value": true,
      "site": "00b63530",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b634d4",
      "incomplete_value": true,
      "site": "00b634ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63514",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63530",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63514",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63530",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b634ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634ec) · [`00b634d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634d0) · [`00b634e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634e4)
- 新版 [`00b63530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63530) · [`00b63514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63514) · [`00b63528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63528)

~~~diff
- 00b634ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b634ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b634ec bytes 605203f9
+ 00b63530 bytes 607203f9
- 00b634d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b634d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63514 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b634d0 bytes 685243f9
+ 00b63514 bytes 687243f9
- 00b634e4 ["INT_ADD", "register:40f0:8", ["const:b634e4:8", "const:4:8"]]
- 00b634e4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63528 ["INT_ADD", "register:40f0:8", ["const:b63528:8", "const:4:8"]]
+ 00b63528 ["CALL", null, ["callee:00bde090:8"]]
- 00b634e4 bytes d7ea0194
+ 00b63528 bytes daea0194
~~~


<a id="compare-bab54e2d23aab7dc7467524a95811bfa"></a>

### [`00b63500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md) → [`00b63544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b63570",
      "incomplete_value": true,
      "site": "00b63570",
      "value": [
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
    "old": {
      "definition_site": "00b6352c",
      "incomplete_value": true,
      "site": "00b6352c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b63558",
      "incomplete_value": true,
      "site": "00b63558",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63514",
      "incomplete_value": true,
      "site": "00b63514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63514"
      ],
      [
        "FALL_THROUGH",
        "00b63558"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63558",
      "incomplete_value": true,
      "site": "00b63570",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63514",
      "incomplete_value": true,
      "site": "00b6352c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63554",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63570",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63554",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63570",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6352c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b6352c) · [`00b63510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b63510) · [`00b63524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b63524)
- 新版 [`00b63570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63570) · [`00b63554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63554) · [`00b63568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63568)

~~~diff
- 00b6352c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b6352c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6352c bytes 605203f9
+ 00b63570 bytes 607203f9
- 00b63510 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b63510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63554 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63510 bytes 685243f9
+ 00b63554 bytes 687243f9
- 00b63524 ["INT_ADD", "register:40f0:8", ["const:b63524:8", "const:4:8"]]
- 00b63524 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63568 ["INT_ADD", "register:40f0:8", ["const:b63568:8", "const:4:8"]]
+ 00b63568 ["CALL", null, ["callee:00bde090:8"]]
- 00b63524 bytes c7ea0194
+ 00b63568 bytes caea0194
~~~


<a id="compare-90f78ad00e06d1907a34968b3828f9c6"></a>

### [`00b63540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md) → [`00b63584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b635b4",
      "incomplete_value": true,
      "site": "00b635b4",
      "value": [
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
    "old": {
      "definition_site": "00b63570",
      "incomplete_value": true,
      "site": "00b63570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b63598",
      "incomplete_value": true,
      "site": "00b63598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63554",
      "incomplete_value": true,
      "site": "00b63554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63554"
      ],
      [
        "FALL_THROUGH",
        "00b63598"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63598",
      "incomplete_value": true,
      "site": "00b635b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63554",
      "incomplete_value": true,
      "site": "00b63570",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63594",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635b4",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63594",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635b4",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63570) · [`00b63550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63550) · [`00b63568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63568)
- 新版 [`00b635b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b635b4) · [`00b63594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b63594) · [`00b635ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b635ac)

~~~diff
- 00b63570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b63570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b635b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b635b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63570 bytes 605203f9
+ 00b635b4 bytes 607203f9
- 00b63550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b63550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63550 bytes 685243f9
+ 00b63594 bytes 687243f9
- 00b63568 ["INT_ADD", "register:40f0:8", ["const:b63568:8", "const:4:8"]]
- 00b63568 ["CALL", null, ["callee:00bde090:8"]]
+ 00b635ac ["INT_ADD", "register:40f0:8", ["const:b635ac:8", "const:4:8"]]
+ 00b635ac ["CALL", null, ["callee:00bde090:8"]]
- 00b63568 bytes b6ea0194
+ 00b635ac bytes b9ea0194
~~~


<a id="compare-075efbb72b60daef9bf901e5908525b4"></a>

### [`00b63584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md) → [`00b635c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b635f8",
      "incomplete_value": true,
      "site": "00b635f8",
      "value": [
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
    "old": {
      "definition_site": "00b635b4",
      "incomplete_value": true,
      "site": "00b635b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b635dc",
      "incomplete_value": true,
      "site": "00b635dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63598",
      "incomplete_value": true,
      "site": "00b63598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63598"
      ],
      [
        "FALL_THROUGH",
        "00b635dc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b635dc",
      "incomplete_value": true,
      "site": "00b635f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63598",
      "incomplete_value": true,
      "site": "00b635b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b635d8",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635f8",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b635d8",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635f8",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b635b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b635b4) · [`00b63594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b63594) · [`00b635ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b635ac)
- 新版 [`00b635f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635f8) · [`00b635d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635d8) · [`00b635f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635f0)

~~~diff
- 00b635b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b635b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b635f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b635f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b635b4 bytes 605203f9
+ 00b635f8 bytes 607203f9
- 00b63594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b63594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b635d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b635d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63594 bytes 685243f9
+ 00b635d8 bytes 687243f9
- 00b635ac ["INT_ADD", "register:40f0:8", ["const:b635ac:8", "const:4:8"]]
- 00b635ac ["CALL", null, ["callee:00bde090:8"]]
+ 00b635f0 ["INT_ADD", "register:40f0:8", ["const:b635f0:8", "const:4:8"]]
+ 00b635f0 ["CALL", null, ["callee:00bde090:8"]]
- 00b635ac bytes a5ea0194
+ 00b635f0 bytes a8ea0194
~~~


<a id="compare-a5983b58a8e80615d663245ce401e013"></a>

### [`00b635d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md) → [`00b63618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md) _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b63670",
      "incomplete_value": true,
      "site": "00b63670",
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
    "old": {
      "definition_site": "00b6362c",
      "incomplete_value": true,
      "site": "00b6362c",
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
            "const:6a8:8"
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
      "definition_site": "00b6364c",
      "incomplete_value": true,
      "site": "00b63658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b63608",
      "incomplete_value": true,
      "site": "00b63614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a0:8"
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
      "00b6362c",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6364c",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63670",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6362c",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6364c",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63670",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b635e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b635e8) · [`00b63614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b63614) · [`00b6362c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b6362c)
- 新版 [`00b6362c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b6362c) · [`00b63658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b63658) · [`00b63670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b63670)

~~~diff
- 00b635e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a8:8"]]
- 00b635e8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b635e8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6362c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e8:8"]]
+ 00b6362c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6362c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b635e8 bytes a8a25a39
+ 00b6362c bytes a8a25b39
- 00b63614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63614 ["INT_ADD", "register:40f0:8", ["const:b63614:8", "const:4:8"]]
- 00b63614 ["CALLIND", null, ["register:0:8"]]
+ 00b63658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63658 ["INT_ADD", "register:40f0:8", ["const:b63658:8", "const:4:8"]]
+ 00b63658 ["CALLIND", null, ["register:0:8"]]
- 00b63614 bytes 00013fd6
+ 00b63658 bytes 00013fd6
- 00b6362c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6362c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a8:8"]]
- 00b6362c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b63670 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b63670 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e8:8"]]
+ 00b63670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6362c bytes a0a21a39
+ 00b63670 bytes a0a21b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b89c16fce71e3c319728242a95bca03"></a>

### [`00b63640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md) → [`00b63684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md) _ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b636c0",
      "incomplete_value": true,
      "site": "00b636c0",
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
    "old": {
      "definition_site": "00b6367c",
      "incomplete_value": true,
      "site": "00b6367c",
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
            "const:6a8:8"
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
      "definition_site": "00b636e0",
      "incomplete_value": true,
      "site": "00b636e0",
      "value": [
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
    "old": {
      "definition_site": "00b6369c",
      "incomplete_value": true,
      "site": "00b6369c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b6369c",
      "incomplete_value": true,
      "site": "00b6369c",
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
      "definition_site": "00b63658",
      "incomplete_value": true,
      "site": "00b63658",
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
      "00b63698",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b636a4",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b636c0",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63698",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b636a4",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b636c0",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b63654) · [`00b6367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b6367c) · [`00b63698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b63698)
- 新版 [`00b63698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b63698) · [`00b636c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b636c0) · [`00b636dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b636dc)

~~~diff
- 00b63654 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b63654 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
+ 00b63698 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63654 bytes 815243f9
+ 00b63698 bytes 817243f9
- 00b6367c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6367c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6367c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a8:8"]]
- 00b6367c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b636c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b636c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b636c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6e8:8"]]
+ 00b636c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6367c bytes bfa21a39
+ 00b636c0 bytes bfa21b39
- 00b63698 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63698 ["INT_ADD", "register:40f0:8", ["const:b63698:8", "const:4:8"]]
- 00b63698 ["CALLIND", null, ["register:0:8"]]
+ 00b636dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b636dc ["INT_ADD", "register:40f0:8", ["const:b636dc:8", "const:4:8"]]
+ 00b636dc ["CALLIND", null, ["register:0:8"]]
- 00b63698 bytes 00013fd6
+ 00b636dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07c3363391ed21da37d26ce396467b8"></a>

### [`00b636b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md) → [`00b636f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md) _ZN8firebase4auth26firebase_network_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b63734",
      "incomplete_value": true,
      "site": "00b63734",
      "value": [
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
    "old": {
      "definition_site": "00b636f0",
      "incomplete_value": true,
      "site": "00b636f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b63710",
      "incomplete_value": true,
      "site": "00b63710",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636cc",
      "incomplete_value": true,
      "site": "00b636cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b636cc"
      ],
      [
        "FALL_THROUGH",
        "00b63710"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b63710",
      "incomplete_value": true,
      "site": "00b63734",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636cc",
      "incomplete_value": true,
      "site": "00b636f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63708",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63734",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6374c",
      "PARAM",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63708",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63734",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6374c",
      "PARAM",
      [
        "storage",
        "010a16f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b636f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636f0) · [`00b636c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636c4) · [`00b636e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636e8)
- 新版 [`00b63734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b63734) · [`00b63708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b63708) · [`00b6372c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b6372c)

~~~diff
- 00b636f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b636f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
+ 00b63734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b636f0 bytes 805203f9
+ 00b63734 bytes 807203f9
- 00b636c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b636c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63708 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
+ 00b63708 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b636c4 bytes 815243f9
+ 00b63708 bytes 817243f9
- 00b636e8 ["INT_ADD", "register:40f0:8", ["const:b636e8:8", "const:4:8"]]
- 00b636e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6372c ["INT_ADD", "register:40f0:8", ["const:b6372c:8", "const:4:8"]]
+ 00b6372c ["CALL", null, ["callee:00bde090:8"]]
- 00b636e8 bytes 56ea0194
+ 00b6372c bytes 59ea0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ffed48549d01f740c6a8b43c8ddfc11"></a>

### [`00b63720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md) → [`00b63764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md) _ZN8firebase4auth26firebase_network_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b63780",
      "incomplete_value": false,
      "site": "00b63784",
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
      "definition_site": "00b6373c",
      "incomplete_value": false,
      "site": "00b63740",
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
      "definition_site": "00b63790",
      "incomplete_value": true,
      "site": "00b6379c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6374c",
      "incomplete_value": true,
      "site": "00b63758",
      "value": [
        "LOAD",
        "8",
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
      "00b63780",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63790",
      "DATA",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63780",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63790",
      "DATA",
      [
        "storage",
        "010a16f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b63740) · [`00b6373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b6373c) · [`00b63748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b63748)
- 新版 [`00b63784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b63784) · [`00b63780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b63780) · [`00b6378c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b6378c)

~~~diff
- 00b63740 ["INT_ADD", "register:40f0:8", ["const:b63740:8", "const:4:8"]]
- 00b63740 ["CALL", null, ["callee:00bde180:8"]]
+ 00b63784 ["INT_ADD", "register:40f0:8", ["const:b63784:8", "const:4:8"]]
+ 00b63784 ["CALL", null, ["callee:00bde180:8"]]
- 00b63740 bytes 7cea0194
+ 00b63784 bytes 7fea0194
- 00b6373c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6373c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6373c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6373c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63780 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b63780 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63780 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63780 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6373c bytes 00501791
+ 00b63780 bytes 001c1591
- 00b63748 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00b63748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6378c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00b6378c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6378c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6378c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63748 bytes 08c11a91
+ 00b6378c bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63eeb4e70140c639d44a1e3e1e07c244"></a>

### [`00b6375c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md) → [`00b637a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md) _ZN8firebase4auth26firebase_network_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b637e0",
      "incomplete_value": true,
      "site": "00b637e0",
      "value": [
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
    "old": {
      "definition_site": "00b6379c",
      "incomplete_value": true,
      "site": "00b6379c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b637bc",
      "incomplete_value": true,
      "site": "00b637bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63778",
      "incomplete_value": true,
      "site": "00b63778",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b63778"
      ],
      [
        "FALL_THROUGH",
        "00b637bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b637bc",
      "incomplete_value": true,
      "site": "00b637e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63778",
      "incomplete_value": true,
      "site": "00b6379c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b637b4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b637e0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b637f8",
      "PARAM",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b637b4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b637e0",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b637f8",
      "PARAM",
      [
        "storage",
        "010a16f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6379c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b6379c) · [`00b63770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b63770) · [`00b63794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b63794)
- 新版 [`00b637e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637e0) · [`00b637b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637b4) · [`00b637d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637d8)

~~~diff
- 00b6379c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b6379c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b637e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
+ 00b637e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6379c bytes 805203f9
+ 00b637e0 bytes 807203f9
- 00b63770 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b63770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b637b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
+ 00b637b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63770 bytes 815243f9
+ 00b637b4 bytes 817243f9
- 00b63794 ["INT_ADD", "register:40f0:8", ["const:b63794:8", "const:4:8"]]
- 00b63794 ["CALL", null, ["callee:00bde090:8"]]
+ 00b637d8 ["INT_ADD", "register:40f0:8", ["const:b637d8:8", "const:4:8"]]
+ 00b637d8 ["CALL", null, ["callee:00bde090:8"]]
- 00b63794 bytes 2bea0194
+ 00b637d8 bytes 2eea0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17315dfa4c63bf72c704201e2771450b"></a>

### [`00b637cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md) → [`00b63810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md) _ZN8firebase4auth26firebase_network_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6382c",
      "incomplete_value": false,
      "site": "00b63830",
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
      "definition_site": "00b637e8",
      "incomplete_value": false,
      "site": "00b637ec",
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
      "definition_site": "00b6383c",
      "incomplete_value": true,
      "site": "00b63848",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b637f8",
      "incomplete_value": true,
      "site": "00b63804",
      "value": [
        "LOAD",
        "8",
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
      "00b6382c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6383c",
      "DATA",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6382c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6383c",
      "DATA",
      [
        "storage",
        "010a16f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b637ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637ec) · [`00b637e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637e8) · [`00b637f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637f4)
- 新版 [`00b63830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b63830) · [`00b6382c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b6382c) · [`00b63838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b63838)

~~~diff
- 00b637ec ["INT_ADD", "register:40f0:8", ["const:b637ec:8", "const:4:8"]]
- 00b637ec ["CALL", null, ["callee:00bde180:8"]]
+ 00b63830 ["INT_ADD", "register:40f0:8", ["const:b63830:8", "const:4:8"]]
+ 00b63830 ["CALL", null, ["callee:00bde180:8"]]
- 00b637ec bytes 51ea0194
+ 00b63830 bytes 54ea0194
- 00b637e8 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b637e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b637e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b637e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6382c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6382c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6382c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6382c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b637e8 bytes 00fc1991
+ 00b6382c bytes 00c81791
- 00b637f4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00b637f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b637f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b637f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63838 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00b63838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b637f4 bytes 08e11a91
+ 00b63838 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b9b40493279447c7ee35290e6d9c59"></a>

### [`00b63808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md) → [`00b6384c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b63878",
      "incomplete_value": true,
      "site": "00b63878",
      "value": [
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
    "old": {
      "definition_site": "00b63834",
      "incomplete_value": true,
      "site": "00b63834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b63860",
      "incomplete_value": true,
      "site": "00b63860",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6381c",
      "incomplete_value": true,
      "site": "00b6381c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6386c",
      "incomplete_value": false,
      "site": "00b63870",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63828",
      "incomplete_value": false,
      "site": "00b6382c",
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
            "const:120:8"
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
      "00b6385c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6386c",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63878",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6385c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6386c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b63878",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6382c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b6382c) · [`00b63834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b63834) · [`00b63818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b63818)
- 新版 [`00b63870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b63870) · [`00b63878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b63878) · [`00b6385c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b6385c)

~~~diff
- 00b6382c ["INT_ADD", "register:40f0:8", ["const:b6382c:8", "const:4:8"]]
- 00b6382c ["CALL", null, ["callee:00bde090:8"]]
+ 00b63870 ["INT_ADD", "register:40f0:8", ["const:b63870:8", "const:4:8"]]
+ 00b63870 ["CALL", null, ["callee:00bde090:8"]]
- 00b6382c bytes 05ea0194
+ 00b63870 bytes 08ea0194
- 00b63834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b63878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63834 bytes 606203f9
+ 00b63878 bytes 608203f9
- 00b63818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6385c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b6385c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63818 bytes 686243f9
+ 00b6385c bytes 688243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0119b71c0bca574a916238a5f5fcf7d"></a>

### [`00b63848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md) → [`00b6388c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b638b8",
      "incomplete_value": true,
      "site": "00b638b8",
      "value": [
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
    "old": {
      "definition_site": "00b63874",
      "incomplete_value": true,
      "site": "00b63874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b638a0",
      "incomplete_value": true,
      "site": "00b638a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6385c",
      "incomplete_value": true,
      "site": "00b6385c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b638a8",
      "incomplete_value": false,
      "site": "00b638b0",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63864",
      "incomplete_value": false,
      "site": "00b6386c",
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
            "const:120:8"
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
      "00b6389c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638a8",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b638b8",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6389c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638a8",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b638b8",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b6386c) · [`00b63874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b63874) · [`00b63858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b63858)
- 新版 [`00b638b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b638b0) · [`00b638b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b638b8) · [`00b6389c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b6389c)

~~~diff
- 00b6386c ["INT_ADD", "register:40f0:8", ["const:b6386c:8", "const:4:8"]]
- 00b6386c ["CALL", null, ["callee:00bde090:8"]]
+ 00b638b0 ["INT_ADD", "register:40f0:8", ["const:b638b0:8", "const:4:8"]]
+ 00b638b0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6386c bytes f5e90194
+ 00b638b0 bytes f8e90194
- 00b63874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b638b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b638b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63874 bytes 606203f9
+ 00b638b8 bytes 608203f9
- 00b63858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6389c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b6389c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63858 bytes 686243f9
+ 00b6389c bytes 688243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5acf6632ece14cf49eb586baf82370bb"></a>

### [`00b63888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63888.md) → [`00b638cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b638fc",
      "incomplete_value": true,
      "site": "00b638fc",
      "value": [
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
    "old": {
      "definition_site": "00b638b8",
      "incomplete_value": true,
      "site": "00b638b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b638e0",
      "incomplete_value": true,
      "site": "00b638e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6389c",
      "incomplete_value": true,
      "site": "00b6389c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b638ec",
      "incomplete_value": false,
      "site": "00b638f4",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638a8",
      "incomplete_value": false,
      "site": "00b638b0",
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
            "const:120:8"
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
      "00b638dc",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638ec",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b638fc",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b638dc",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638ec",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b638fc",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63888.md#insn-00b638b0) · [`00b638b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63888.md#insn-00b638b8) · [`00b63898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63888.md#insn-00b63898)
- 新版 [`00b638f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638f4) · [`00b638fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638fc) · [`00b638dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638dc)

~~~diff
- 00b638b0 ["INT_ADD", "register:40f0:8", ["const:b638b0:8", "const:4:8"]]
- 00b638b0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b638f4 ["INT_ADD", "register:40f0:8", ["const:b638f4:8", "const:4:8"]]
+ 00b638f4 ["CALL", null, ["callee:00bde090:8"]]
- 00b638b0 bytes e4e90194
+ 00b638f4 bytes e7e90194
- 00b638b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b638b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b638fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b638fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b638b8 bytes 606203f9
+ 00b638fc bytes 608203f9
- 00b63898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b638dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b638dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63898 bytes 686243f9
+ 00b638dc bytes 688243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef319d69f6cc30c38c5ead1aee19e60d"></a>

### [`00b638cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b638cc.md) → [`00b63910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63940",
      "incomplete_value": true,
      "site": "00b63940",
      "value": [
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
    "old": {
      "definition_site": "00b638fc",
      "incomplete_value": true,
      "site": "00b638fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b63924",
      "incomplete_value": true,
      "site": "00b63924",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638e0",
      "incomplete_value": true,
      "site": "00b638e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6392c",
      "incomplete_value": false,
      "site": "00b63938",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638e8",
      "incomplete_value": false,
      "site": "00b638f4",
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
            "const:120:8"
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
      "00b63920",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6392c",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63940",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63920",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6392c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b63940",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b638cc.md#insn-00b638f4) · [`00b638fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b638cc.md#insn-00b638fc) · [`00b638dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b638cc.md#insn-00b638dc)
- 新版 [`00b63938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b63938) · [`00b63940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b63940) · [`00b63920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b63920)

~~~diff
- 00b638f4 ["INT_ADD", "register:40f0:8", ["const:b638f4:8", "const:4:8"]]
- 00b638f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63938 ["INT_ADD", "register:40f0:8", ["const:b63938:8", "const:4:8"]]
+ 00b63938 ["CALL", null, ["callee:00bde090:8"]]
- 00b638f4 bytes d3e90194
+ 00b63938 bytes d6e90194
- 00b638fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b638fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63940 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b63940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b638fc bytes 606203f9
+ 00b63940 bytes 608203f9
- 00b638dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b638dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63920 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b63920 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b638dc bytes 686243f9
+ 00b63920 bytes 688243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91cdc5e896d3ee312766d210c23a9e6"></a>

### [`00b6391c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6391c.md) → [`00b63960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md) _ZN8firebase4auth27too_many_requests_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b639b8",
      "incomplete_value": true,
      "site": "00b639b8",
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
    "old": {
      "definition_site": "00b63974",
      "incomplete_value": true,
      "site": "00b63974",
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
            "const:6c8:8"
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
      "definition_site": "00b63994",
      "incomplete_value": true,
      "site": "00b639a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b63950",
      "incomplete_value": true,
      "site": "00b6395c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
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
      "00b63974",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63994",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639b8",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63974",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63994",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639b8",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6391c.md#insn-00b63930) · [`00b6395c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6391c.md#insn-00b6395c) · [`00b63974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6391c.md#insn-00b63974)
- 新版 [`00b63974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b63974) · [`00b639a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b639a0) · [`00b639b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b639b8)

~~~diff
- 00b63930 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
- 00b63930 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b63930 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b63974 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:708:8"]]
+ 00b63974 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b63974 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b63930 bytes a8225b39
+ 00b63974 bytes a8225c39
- 00b6395c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6395c ["INT_ADD", "register:40f0:8", ["const:b6395c:8", "const:4:8"]]
- 00b6395c ["CALLIND", null, ["register:0:8"]]
+ 00b639a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b639a0 ["INT_ADD", "register:40f0:8", ["const:b639a0:8", "const:4:8"]]
+ 00b639a0 ["CALLIND", null, ["register:0:8"]]
- 00b6395c bytes 00013fd6
+ 00b639a0 bytes 00013fd6
- 00b63974 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63974 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
- 00b63974 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b639b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b639b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:708:8"]]
+ 00b639b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63974 bytes a0221b39
+ 00b639b8 bytes a0221c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9162d25252472c56ff4b84e2643b70d9"></a>

### [`00b63988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63988.md) → [`00b639cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md) _ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b63a08",
      "incomplete_value": true,
      "site": "00b63a08",
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
    "old": {
      "definition_site": "00b639c4",
      "incomplete_value": true,
      "site": "00b639c4",
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
            "const:6c8:8"
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
      "definition_site": "00b63a28",
      "incomplete_value": true,
      "site": "00b63a28",
      "value": [
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
    "old": {
      "definition_site": "00b639e4",
      "incomplete_value": true,
      "site": "00b639e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b639e4",
      "incomplete_value": true,
      "site": "00b639e4",
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
      "definition_site": "00b639a0",
      "incomplete_value": true,
      "site": "00b639a0",
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
      "00b639e0",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639ec",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63a08",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b639e0",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639ec",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63a08",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6399c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63988.md#insn-00b6399c) · [`00b639c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63988.md#insn-00b639c4) · [`00b639e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63988.md#insn-00b639e0)
- 新版 [`00b639e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b639e0) · [`00b63a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b63a08) · [`00b63a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b63a24)

~~~diff
- 00b6399c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b6399c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b639e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
+ 00b639e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6399c bytes 816243f9
+ 00b639e0 bytes 818243f9
- 00b639c4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b639c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b639c4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
- 00b639c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b63a08 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b63a08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b63a08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:708:8"]]
+ 00b63a08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b639c4 bytes bf221b39
+ 00b63a08 bytes bf221c39
- 00b639e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b639e0 ["INT_ADD", "register:40f0:8", ["const:b639e0:8", "const:4:8"]]
- 00b639e0 ["CALLIND", null, ["register:0:8"]]
+ 00b63a24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63a24 ["INT_ADD", "register:40f0:8", ["const:b63a24:8", "const:4:8"]]
+ 00b63a24 ["CALLIND", null, ["register:0:8"]]
- 00b639e0 bytes 00013fd6
+ 00b63a24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4ca91885223129b31c5e0875edf4d21"></a>

### [`00b639f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b639f8.md) → [`00b63a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md) _ZN8firebase4auth27too_many_requests_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63a7c",
      "incomplete_value": true,
      "site": "00b63a7c",
      "value": [
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
    "old": {
      "definition_site": "00b63a38",
      "incomplete_value": true,
      "site": "00b63a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b63a58",
      "incomplete_value": true,
      "site": "00b63a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a14",
      "incomplete_value": true,
      "site": "00b63a14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b63a60",
      "incomplete_value": false,
      "site": "00b63a74",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a1c",
      "incomplete_value": false,
      "site": "00b63a30",
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
            "const:120:8"
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
      "00b63a50",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63a60",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63a7c",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63a50",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63a60",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b63a7c",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b639f8.md#insn-00b63a30) · [`00b63a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b639f8.md#insn-00b63a38) · [`00b63a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b639f8.md#insn-00b63a0c)
- 新版 [`00b63a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a74) · [`00b63a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a7c) · [`00b63a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a50)

~~~diff
- 00b63a30 ["INT_ADD", "register:40f0:8", ["const:b63a30:8", "const:4:8"]]
- 00b63a30 ["CALL", null, ["callee:00bde090:8"]]
+ 00b63a74 ["INT_ADD", "register:40f0:8", ["const:b63a74:8", "const:4:8"]]
+ 00b63a74 ["CALL", null, ["callee:00bde090:8"]]
- 00b63a30 bytes 84e90194
+ 00b63a74 bytes 87e90194
- 00b63a38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
+ 00b63a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63a38 bytes 806203f9
+ 00b63a7c bytes 808203f9
- 00b63a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63a0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
+ 00b63a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63a0c bytes 816243f9
+ 00b63a50 bytes 818243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c792454d53dc876ff32178f01ce96a3"></a>

### [`00b63a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63a68.md) → [`00b63aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md) _ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b63ac8",
      "incomplete_value": false,
      "site": "00b63acc",
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
      "definition_site": "00b63a84",
      "incomplete_value": false,
      "site": "00b63a88",
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
      "definition_site": "00b63ad8",
      "incomplete_value": true,
      "site": "00b63ae4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63a94",
      "incomplete_value": true,
      "site": "00b63aa0",
      "value": [
        "LOAD",
        "8",
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
      "00b63ac8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63ad8",
      "DATA",
      [
        "storage",
        "010a16d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63ac8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63ad8",
      "DATA",
      [
        "storage",
        "010a1710",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63a68.md#insn-00b63a88) · [`00b63a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63a68.md#insn-00b63a84) · [`00b63a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63a68.md#insn-00b63a90)
- 新版 [`00b63acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63acc) · [`00b63ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63ac8) · [`00b63ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63ad4)

~~~diff
- 00b63a88 ["INT_ADD", "register:40f0:8", ["const:b63a88:8", "const:4:8"]]
- 00b63a88 ["CALL", null, ["callee:00bde180:8"]]
+ 00b63acc ["INT_ADD", "register:40f0:8", ["const:b63acc:8", "const:4:8"]]
+ 00b63acc ["CALL", null, ["callee:00bde180:8"]]
- 00b63a88 bytes aae90194
+ 00b63acc bytes ade90194
- 00b63a84 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b63a84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63a84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63a84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63ac8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b63ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63a84 bytes 00501791
+ 00b63ac8 bytes 001c1591
- 00b63a90 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00b63a90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63a90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63a90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63ad4 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00b63ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63a90 bytes 08411b91
+ 00b63ad4 bytes 08411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64502c40eba51515a824aad1e8631e58"></a>

### [`00b63aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63aa4.md) → [`00b63ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md) _ZN8firebase4auth27too_many_requests_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63b28",
      "incomplete_value": true,
      "site": "00b63b28",
      "value": [
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
    "old": {
      "definition_site": "00b63ae4",
      "incomplete_value": true,
      "site": "00b63ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b63b04",
      "incomplete_value": true,
      "site": "00b63b04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ac0",
      "incomplete_value": true,
      "site": "00b63ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b63b0c",
      "incomplete_value": false,
      "site": "00b63b20",
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
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ac8",
      "incomplete_value": false,
      "site": "00b63adc",
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
            "const:120:8"
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
      "00b63afc",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63b0c",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63b28",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63afc",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63b0c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00b63b28",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63aa4.md#insn-00b63adc) · [`00b63ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63aa4.md#insn-00b63ae4) · [`00b63ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63aa4.md#insn-00b63ab8)
- 新版 [`00b63b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63b20) · [`00b63b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63b28) · [`00b63afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63afc)

~~~diff
- 00b63adc ["INT_ADD", "register:40f0:8", ["const:b63adc:8", "const:4:8"]]
- 00b63adc ["CALL", null, ["callee:00bde090:8"]]
+ 00b63b20 ["INT_ADD", "register:40f0:8", ["const:b63b20:8", "const:4:8"]]
+ 00b63b20 ["CALL", null, ["callee:00bde090:8"]]
- 00b63adc bytes 59e90194
+ 00b63b20 bytes 5ce90194
- 00b63ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
+ 00b63b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63ae4 bytes 806203f9
+ 00b63b28 bytes 808203f9
- 00b63ab8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63ab8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63afc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
+ 00b63afc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63ab8 bytes 816243f9
+ 00b63afc bytes 818243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

