# v15.7.3 → v15.7.4 · 最優先の変更候補 (63)

[一覧の目次](README.md)

<a id="compare-d1479be9b5aeb17779b5f41ef48e1a47"></a>

### [`00ae8484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md) → [`00ae84c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae84f4",
      "incomplete_value": true,
      "site": "00ae84f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84b0",
      "incomplete_value": true,
      "site": "00ae84b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00ae84dc",
      "incomplete_value": true,
      "site": "00ae84dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8498",
      "incomplete_value": true,
      "site": "00ae8498",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae84e4",
      "incomplete_value": false,
      "site": "00ae84ec",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84a0",
      "incomplete_value": false,
      "site": "00ae84a8",
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
            "const:4e6:8"
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
      "00ae84d8",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84e4",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae84f4",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae84d8",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84e4",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae84f4",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae84a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md#insn-00ae84a8) · [`00ae84b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md#insn-00ae84b0) · [`00ae8494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md#insn-00ae8494)
- 新版 `00ae84ec`（命令位置の公開資料なし） · `00ae84f4`（命令位置の公開資料なし） · `00ae84d8`（命令位置の公開資料なし）

~~~diff
- 00ae84a8 ["INT_ADD", "register:40f0:8", ["const:ae84a8:8", "const:4:8"]]
- 00ae84a8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
+ 00ae84ec ["CALL", null, ["callee:00bde090:8"]]
- 00ae84a8 bytes e6d60394
+ 00ae84ec bytes e9d60394
- 00ae84b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae84b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae84f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae84f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae84b0 bytes 600603f9
+ 00ae84f4 bytes 602603f9
- 00ae8494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae8494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae84d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae84d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8494 bytes 680643f9
+ 00ae84d8 bytes 682643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7907881d238f7230f7ae06fb7ed88ae9"></a>

### [`00ae84c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md) → [`00ae8508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae8538",
      "incomplete_value": true,
      "site": "00ae8538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84f4",
      "incomplete_value": true,
      "site": "00ae84f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae851c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84d8",
      "incomplete_value": true,
      "site": "00ae84d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8528",
      "incomplete_value": false,
      "site": "00ae8530",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84e4",
      "incomplete_value": false,
      "site": "00ae84ec",
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
            "const:4e6:8"
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
      "00ae8518",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8528",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae8538",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8518",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8528",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae8538",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae84ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md#insn-00ae84ec) · [`00ae84f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md#insn-00ae84f4) · [`00ae84d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md#insn-00ae84d4)
- 新版 `00ae8530`（命令位置の公開資料なし） · `00ae8538`（命令位置の公開資料なし） · `00ae8518`（命令位置の公開資料なし）

~~~diff
- 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
- 00ae84ec ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8530 ["INT_ADD", "register:40f0:8", ["const:ae8530:8", "const:4:8"]]
+ 00ae8530 ["CALL", null, ["callee:00bde090:8"]]
- 00ae84ec bytes d5d60394
+ 00ae8530 bytes d8d60394
- 00ae84f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae84f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae8538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae84f4 bytes 600603f9
+ 00ae8538 bytes 602603f9
- 00ae84d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae84d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae8518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae84d4 bytes 680643f9
+ 00ae8518 bytes 682643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8fb4ce597f434f68df274ebd1c23e5f"></a>

### [`00ae8508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md) → [`00ae854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae857c",
      "incomplete_value": true,
      "site": "00ae857c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8538",
      "incomplete_value": true,
      "site": "00ae8538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00ae8560",
      "incomplete_value": true,
      "site": "00ae8560",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae851c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae851c"
      ],
      [
        "FALL_THROUGH",
        "00ae8560"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8560",
      "incomplete_value": true,
      "site": "00ae857c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae8538",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae855c",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8568",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae857c",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae855c",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8568",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae857c",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md#insn-00ae8538) · [`00ae8518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md#insn-00ae8518) · [`00ae8524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md#insn-00ae8524)
- 新版 `00ae857c`（命令位置の公開資料なし） · `00ae855c`（命令位置の公開資料なし） · `00ae8568`（命令位置の公開資料なし）

~~~diff
- 00ae8538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae8538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae857c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae857c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8538 bytes 600603f9
+ 00ae857c bytes 602603f9
- 00ae8518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae8518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae855c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae855c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8518 bytes 680643f9
+ 00ae855c bytes 682643f9
- 00ae8524 ["COPY", "tmp:0:8", ["const:4e6:8"]]
- 00ae8524 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8524 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8524 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae8568 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00ae8568 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae8568 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae8568 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae8524 bytes 63981391
+ 00ae8568 bytes 63641191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56bcad39c0c7cfd2756be73756f07e34"></a>

### [`00ae8558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md) → [`00ae859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae859c.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae8624",
      "incomplete_value": true,
      "site": "00ae8624",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae85e0",
      "incomplete_value": true,
      "site": "00ae85e0",
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
            "const:610:8"
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
      "definition_site": "00ae85d0",
      "incomplete_value": true,
      "site": "00ae85dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:648:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae858c",
      "incomplete_value": true,
      "site": "00ae8598",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:608:8"
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
      "00ae85b0",
      "READ",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae85d0",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8624",
      "WRITE",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae85b0",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae85d0",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8624",
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md#insn-00ae8598) · [`00ae85e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md#insn-00ae85e0) · [`00ae856c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md#insn-00ae856c)
- 新版 `00ae85dc`（命令位置の公開資料なし） · `00ae8624`（命令位置の公開資料なし） · `00ae85b0`（命令位置の公開資料なし）

~~~diff
- 00ae8598 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8598 ["INT_ADD", "register:40f0:8", ["const:ae8598:8", "const:4:8"]]
- 00ae8598 ["CALLIND", null, ["register:0:8"]]
+ 00ae85dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae85dc ["INT_ADD", "register:40f0:8", ["const:ae85dc:8", "const:4:8"]]
+ 00ae85dc ["CALLIND", null, ["register:0:8"]]
- 00ae8598 bytes 00013fd6
+ 00ae85dc bytes 00013fd6
- 00ae85e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae85e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:610:8"]]
- 00ae85e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae8624 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae8624 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:650:8"]]
+ 00ae8624 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae85e0 bytes a0421839
+ 00ae8624 bytes a0421939
- 00ae856c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
- 00ae856c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae856c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae85b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
+ 00ae85b0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae85b0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae856c bytes a8425839
+ 00ae85b0 bytes a8425939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03027d3a70070bc5d90ba13c5ed94e17"></a>

### [`00ae85f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md) → [`00ae8638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8674",
      "incomplete_value": true,
      "site": "00ae8674",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8630",
      "incomplete_value": true,
      "site": "00ae8630",
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
            "const:610:8"
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
      "definition_site": "00ae86c4",
      "incomplete_value": true,
      "site": "00ae86c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8680",
      "incomplete_value": true,
      "site": "00ae8680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00ae8650",
      "incomplete_value": true,
      "site": "00ae8650",
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
      "definition_site": "00ae860c",
      "incomplete_value": true,
      "site": "00ae860c",
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
      "00ae864c",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8658",
      "READ",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8674",
      "WRITE",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae864c",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8658",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8674",
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md#insn-00ae8630) · [`00ae8680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md#insn-00ae8680) · [`00ae8608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md#insn-00ae8608)
- 新版 `00ae8674`（命令位置の公開資料なし） · `00ae86c4`（命令位置の公開資料なし） · `00ae864c`（命令位置の公開資料なし）

~~~diff
- 00ae8630 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae8630 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae8630 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:610:8"]]
- 00ae8630 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae8674 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae8674 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae8674 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:650:8"]]
+ 00ae8674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae8630 bytes bf421839
+ 00ae8674 bytes bf421939
- 00ae8680 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae8680 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae8680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae86c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae86c4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae86c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae8680 bytes 9f0603f9
+ 00ae86c4 bytes 9f2603f9
- 00ae8608 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae8608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae864c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae864c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8608 bytes 810643f9
+ 00ae864c bytes 812643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d716ab33b1d0da46040d28e1666aaad8"></a>

### [`00ae8694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md) → [`00ae86d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8718",
      "incomplete_value": true,
      "site": "00ae8718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae86d4",
      "incomplete_value": true,
      "site": "00ae86d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00ae86f4",
      "incomplete_value": true,
      "site": "00ae86f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae86b0",
      "incomplete_value": true,
      "site": "00ae86b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae86b0"
      ],
      [
        "FALL_THROUGH",
        "00ae86f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae86f4",
      "incomplete_value": true,
      "site": "00ae8718",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae86b0",
      "incomplete_value": true,
      "site": "00ae86d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae86ec",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae86fc",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae8718",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae86ec",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae86fc",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae8718",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae86d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md#insn-00ae86d4) · [`00ae86a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md#insn-00ae86a8) · [`00ae86b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md#insn-00ae86b8)
- 新版 `00ae8718`（命令位置の公開資料なし） · `00ae86ec`（命令位置の公開資料なし） · `00ae86fc`（命令位置の公開資料なし）

~~~diff
- 00ae86d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae86d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae8718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae86d4 bytes 800603f9
+ 00ae8718 bytes 802603f9
- 00ae86a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae86a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae86ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae86ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae86a8 bytes 810643f9
+ 00ae86ec bytes 812643f9
- 00ae86b8 ["COPY", "tmp:0:8", ["const:4e6:8"]]
- 00ae86b8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae86b8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae86b8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae86fc ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00ae86fc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae86fc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae86fc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae86b8 bytes 63981391
+ 00ae86fc bytes 63641191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8501bd35c7c8d051f2732f044be12123"></a>

### [`00ae8740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md) → [`00ae8784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae87c4",
      "incomplete_value": true,
      "site": "00ae87c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8780",
      "incomplete_value": true,
      "site": "00ae8780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00ae8798",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae87a8",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae87c4",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8798",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae87a8",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae87c4",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md#insn-00ae8780) · [`00ae8754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md#insn-00ae8754) · [`00ae8764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md#insn-00ae8764)
- 新版 `00ae87c4`（命令位置の公開資料なし） · `00ae8798`（命令位置の公開資料なし） · `00ae87a8`（命令位置の公開資料なし）

~~~diff
- 00ae8780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae8780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae87c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae87c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8780 bytes 800603f9
+ 00ae87c4 bytes 802603f9
- 00ae8754 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00ae8754 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00ae8798 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8754 bytes 810643f9
+ 00ae8798 bytes 812643f9
- 00ae8764 ["COPY", "tmp:0:8", ["const:4e6:8"]]
- 00ae8764 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8764 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8764 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae87a8 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00ae87a8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae87a8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae87a8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae8764 bytes 63981391
+ 00ae87a8 bytes 63641191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d46349fd896c3b76774fda238eed9a"></a>

### [`00ae87ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md) → [`00ae8830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8830.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae885c",
      "incomplete_value": true,
      "site": "00ae885c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8818",
      "incomplete_value": true,
      "site": "00ae8818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae8844",
      "incomplete_value": true,
      "site": "00ae8844",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8800",
      "incomplete_value": true,
      "site": "00ae8800",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae8800"
      ],
      [
        "FALL_THROUGH",
        "00ae8844"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8844",
      "incomplete_value": true,
      "site": "00ae885c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8800",
      "incomplete_value": true,
      "site": "00ae8818",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8840",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae885c",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8840",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae885c",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md#insn-00ae8818) · [`00ae87fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md#insn-00ae87fc) · [`00ae8810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md#insn-00ae8810)
- 新版 `00ae885c`（命令位置の公開資料なし） · `00ae8840`（命令位置の公開資料なし） · `00ae8854`（命令位置の公開資料なし）

~~~diff
- 00ae8818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae8818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae885c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae885c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8818 bytes 601a03f9
+ 00ae885c bytes 603a03f9
- 00ae87fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae87fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae8840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae87fc bytes 681a43f9
+ 00ae8840 bytes 683a43f9
- 00ae8810 ["INT_ADD", "register:40f0:8", ["const:ae8810:8", "const:4:8"]]
- 00ae8810 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8854 ["INT_ADD", "register:40f0:8", ["const:ae8854:8", "const:4:8"]]
+ 00ae8854 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8810 bytes 0cd60394
+ 00ae8854 bytes 0fd60394
~~~


<a id="compare-0c9072ad99fa4b2fef9ceb562b88244b"></a>

### [`00ae882c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md) → [`00ae8870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00ae889c",
      "incomplete_value": true,
      "site": "00ae889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8858",
      "incomplete_value": true,
      "site": "00ae8858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae8884",
      "incomplete_value": true,
      "site": "00ae8884",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8840",
      "incomplete_value": true,
      "site": "00ae8840",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae8840"
      ],
      [
        "FALL_THROUGH",
        "00ae8884"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8884",
      "incomplete_value": true,
      "site": "00ae889c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8840",
      "incomplete_value": true,
      "site": "00ae8858",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8880",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae889c",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8880",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae889c",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md#insn-00ae8858) · [`00ae883c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md#insn-00ae883c) · [`00ae8850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md#insn-00ae8850)
- 新版 `00ae889c`（命令位置の公開資料なし） · `00ae8880`（命令位置の公開資料なし） · `00ae8894`（命令位置の公開資料なし）

~~~diff
- 00ae8858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae8858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae889c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae889c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8858 bytes 601a03f9
+ 00ae889c bytes 603a03f9
- 00ae883c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae883c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae8880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae883c bytes 681a43f9
+ 00ae8880 bytes 683a43f9
- 00ae8850 ["INT_ADD", "register:40f0:8", ["const:ae8850:8", "const:4:8"]]
- 00ae8850 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8894 ["INT_ADD", "register:40f0:8", ["const:ae8894:8", "const:4:8"]]
+ 00ae8894 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8850 bytes fcd50394
+ 00ae8894 bytes ffd50394
~~~


<a id="compare-f0b08bd0ce96488ac536e9fd84c4baa3"></a>

### [`00ae886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md) → [`00ae88b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88b0.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae88e0",
      "incomplete_value": true,
      "site": "00ae88e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae889c",
      "incomplete_value": true,
      "site": "00ae889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "00ae88c0",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae88e0",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae88c0",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae88e0",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae889c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md#insn-00ae889c) · [`00ae887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md#insn-00ae887c) · [`00ae8894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md#insn-00ae8894)
- 新版 `00ae88e0`（命令位置の公開資料なし） · `00ae88c0`（命令位置の公開資料なし） · `00ae88d8`（命令位置の公開資料なし）

~~~diff
- 00ae889c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae889c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae88e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae88e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae889c bytes 601a03f9
+ 00ae88e0 bytes 603a03f9
- 00ae887c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae887c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae88c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae88c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae887c bytes 681a43f9
+ 00ae88c0 bytes 683a43f9
- 00ae8894 ["INT_ADD", "register:40f0:8", ["const:ae8894:8", "const:4:8"]]
- 00ae8894 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae88d8 ["INT_ADD", "register:40f0:8", ["const:ae88d8:8", "const:4:8"]]
+ 00ae88d8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8894 bytes ebd50394
+ 00ae88d8 bytes eed50394
~~~


<a id="compare-6f1696e8a4f386884c2d71bbe0758838"></a>

### [`00ae88b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md) → [`00ae88f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8924",
      "incomplete_value": true,
      "site": "00ae8924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae88e0",
      "incomplete_value": true,
      "site": "00ae88e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae8908",
      "incomplete_value": true,
      "site": "00ae8908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae88c4",
      "incomplete_value": true,
      "site": "00ae88c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae88c4"
      ],
      [
        "FALL_THROUGH",
        "00ae8908"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8908",
      "incomplete_value": true,
      "site": "00ae8924",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae88c4",
      "incomplete_value": true,
      "site": "00ae88e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8904",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8924",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8904",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8924",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae88e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md#insn-00ae88e0) · [`00ae88c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md#insn-00ae88c0) · [`00ae88d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md#insn-00ae88d8)
- 新版 `00ae8924`（命令位置の公開資料なし） · `00ae8904`（命令位置の公開資料なし） · `00ae891c`（命令位置の公開資料なし）

~~~diff
- 00ae88e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae88e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae8924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae88e0 bytes 601a03f9
+ 00ae8924 bytes 603a03f9
- 00ae88c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
- 00ae88c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00ae8904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae88c0 bytes 681a43f9
+ 00ae8904 bytes 683a43f9
- 00ae88d8 ["INT_ADD", "register:40f0:8", ["const:ae88d8:8", "const:4:8"]]
- 00ae88d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae891c ["INT_ADD", "register:40f0:8", ["const:ae891c:8", "const:4:8"]]
+ 00ae891c ["CALL", null, ["callee:00bde090:8"]]
- 00ae88d8 bytes dad50394
+ 00ae891c bytes ddd50394
~~~


<a id="compare-3ab30b23915d23860ed8f965513f5d66"></a>

### [`00ae8900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8900.md) → [`00ae8944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8944.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae89cc",
      "incomplete_value": true,
      "site": "00ae89cc",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8988",
      "incomplete_value": true,
      "site": "00ae8988",
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
            "const:638:8"
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
      "00ae8958",
      "READ",
      [
        "storage",
        "010a0638",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8978",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae89cc",
      "WRITE",
      [
        "storage",
        "010a0638",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae8958",
      "READ",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8978",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae89cc",
      "WRITE",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8900.md#insn-00ae8988) · [`00ae8914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8900.md#insn-00ae8914) · [`00ae8934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8900.md#insn-00ae8934)
- 新版 `00ae89cc`（命令位置の公開資料なし） · `00ae8958`（命令位置の公開資料なし） · `00ae8978`（命令位置の公開資料なし）

~~~diff
- 00ae8988 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae8988 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:638:8"]]
- 00ae8988 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae89cc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae89cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:678:8"]]
+ 00ae89cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae8988 bytes a0e21839
+ 00ae89cc bytes a0e21939
- 00ae8914 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:638:8"]]
- 00ae8914 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae8914 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae8958 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
+ 00ae8958 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8958 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae8914 bytes a8e25839
+ 00ae8958 bytes a8e25939
- 00ae8934 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:630:8"]]
- 00ae8934 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8978 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:670:8"]]
+ 00ae8978 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8934 bytes 211943f9
+ 00ae8978 bytes 213943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8d28e8d4044e07c18b957e3252aaec"></a>

### [`00ae899c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae899c.md) → [`00ae89e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae8a1c",
      "incomplete_value": true,
      "site": "00ae8a1c",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae89d8",
      "incomplete_value": true,
      "site": "00ae89d8",
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
            "const:638:8"
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
      "definition_site": "00ae8a6c",
      "incomplete_value": true,
      "site": "00ae8a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a28",
      "incomplete_value": true,
      "site": "00ae8a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae89f8",
      "incomplete_value": true,
      "site": "00ae89f8",
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
      "definition_site": "00ae89b4",
      "incomplete_value": true,
      "site": "00ae89b4",
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
      "00ae89f4",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8a00",
      "READ",
      [
        "storage",
        "010a0638",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8a1c",
      "WRITE",
      [
        "storage",
        "010a0638",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae89f4",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8a00",
      "READ",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8a1c",
      "WRITE",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae89d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae899c.md#insn-00ae89d8) · [`00ae8a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae899c.md#insn-00ae8a24) · [`00ae8a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae899c.md#insn-00ae8a28)
- 新版 `00ae8a1c`（命令位置の公開資料なし） · `00ae8a68`（命令位置の公開資料なし） · `00ae8a6c`（命令位置の公開資料なし）

~~~diff
- 00ae89d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae89d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae89d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:638:8"]]
- 00ae89d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae8a1c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae8a1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae8a1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:678:8"]]
+ 00ae8a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae89d8 bytes bfe21839
+ 00ae8a1c bytes bfe21939
- 00ae8a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8a24 ["INT_ADD", "register:40f0:8", ["const:ae8a24:8", "const:4:8"]]
- 00ae8a24 ["CALLIND", null, ["register:0:8"]]
+ 00ae8a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae8a68 ["INT_ADD", "register:40f0:8", ["const:ae8a68:8", "const:4:8"]]
+ 00ae8a68 ["CALLIND", null, ["register:0:8"]]
- 00ae8a24 bytes 00013fd6
+ 00ae8a68 bytes 00013fd6
- 00ae8a28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
- 00ae8a28 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae8a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae8a6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00ae8a6c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae8a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae8a28 bytes 9f1a03f9
+ 00ae8a6c bytes 9f3a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f61943f34cf5332f423704a758f3cf7"></a>

### [`00ae8a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8a3c.md) → [`00ae8a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8ac0",
      "incomplete_value": true,
      "site": "00ae8ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a7c",
      "incomplete_value": true,
      "site": "00ae8a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae8a9c",
      "incomplete_value": true,
      "site": "00ae8a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a58",
      "incomplete_value": true,
      "site": "00ae8a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae8a58"
      ],
      [
        "FALL_THROUGH",
        "00ae8a9c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8a9c",
      "incomplete_value": true,
      "site": "00ae8ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a58",
      "incomplete_value": true,
      "site": "00ae8a7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8a94",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ac0",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ad4",
      "PARAM",
      [
        "storage",
        "00c10098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae8a94",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ac0",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ad4",
      "PARAM",
      [
        "storage",
        "00c100e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8a3c.md#insn-00ae8a7c) · [`00ae8a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8a3c.md#insn-00ae8a50) · [`00ae8a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8a3c.md#insn-00ae8a74)
- 新版 `00ae8ac0`（命令位置の公開資料なし） · `00ae8a94`（命令位置の公開資料なし） · `00ae8ab8`（命令位置の公開資料なし）

~~~diff
- 00ae8a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
- 00ae8a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00ae8ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8a7c bytes 801a03f9
+ 00ae8ac0 bytes 803a03f9
- 00ae8a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
- 00ae8a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00ae8a94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8a50 bytes 811a43f9
+ 00ae8a94 bytes 813a43f9
- 00ae8a74 ["INT_ADD", "register:40f0:8", ["const:ae8a74:8", "const:4:8"]]
- 00ae8a74 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8ab8 ["INT_ADD", "register:40f0:8", ["const:ae8ab8:8", "const:4:8"]]
+ 00ae8ab8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8a74 bytes 73d50394
+ 00ae8ab8 bytes 76d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba45e896acda623ad03dd9e464f87a6"></a>

### [`00ae8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8aac.md) → [`00ae8af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8af0.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae8b0c",
      "incomplete_value": false,
      "site": "00ae8b10",
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
      "definition_site": "00ae8ac8",
      "incomplete_value": false,
      "site": "00ae8acc",
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
      "definition_site": "00ae8b1c",
      "incomplete_value": true,
      "site": "00ae8b28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8ad8",
      "incomplete_value": true,
      "site": "00ae8ae4",
      "value": [
        "LOAD",
        "8",
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
      "00ae8b0c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae8b1c",
      "DATA",
      [
        "storage",
        "010a0640",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae8b0c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae8b1c",
      "DATA",
      [
        "storage",
        "010a0680",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8aac.md#insn-00ae8acc) · [`00ae8ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8aac.md#insn-00ae8ac8) · [`00ae8ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8aac.md#insn-00ae8ad4)
- 新版 `00ae8b10`（命令位置の公開資料なし） · `00ae8b0c`（命令位置の公開資料なし） · `00ae8b18`（命令位置の公開資料なし）

~~~diff
- 00ae8acc ["INT_ADD", "register:40f0:8", ["const:ae8acc:8", "const:4:8"]]
- 00ae8acc ["CALL", null, ["callee:00bde180:8"]]
+ 00ae8b10 ["INT_ADD", "register:40f0:8", ["const:ae8b10:8", "const:4:8"]]
+ 00ae8b10 ["CALL", null, ["callee:00bde180:8"]]
- 00ae8acc bytes 99d50394
+ 00ae8b10 bytes 9cd50394
- 00ae8ac8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae8ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8b0c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae8b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8ac8 bytes 00501791
+ 00ae8b0c bytes 001c1591
- 00ae8ad4 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00ae8ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8b18 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00ae8b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8ad4 bytes 08011991
+ 00ae8b18 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba1a88daacd42a6da985660219821b5"></a>

### [`00ae8ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md) → [`00ae8b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8b6c",
      "incomplete_value": true,
      "site": "00ae8b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8b28",
      "incomplete_value": true,
      "site": "00ae8b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00ae8b48",
      "incomplete_value": true,
      "site": "00ae8b48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8b04",
      "incomplete_value": true,
      "site": "00ae8b04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae8b04"
      ],
      [
        "FALL_THROUGH",
        "00ae8b48"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8b48",
      "incomplete_value": true,
      "site": "00ae8b6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8b04",
      "incomplete_value": true,
      "site": "00ae8b28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8b40",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8b6c",
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8b84",
      "PARAM",
      [
        "storage",
        "010a0650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae8b40",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8b6c",
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8b84",
      "PARAM",
      [
        "storage",
        "010a0690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md#insn-00ae8b28) · [`00ae8afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md#insn-00ae8afc) · [`00ae8b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md#insn-00ae8b20)
- 新版 `00ae8b6c`（命令位置の公開資料なし） · `00ae8b40`（命令位置の公開資料なし） · `00ae8b64`（命令位置の公開資料なし）

~~~diff
- 00ae8b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
- 00ae8b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00ae8b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8b28 bytes 801a03f9
+ 00ae8b6c bytes 803a03f9
- 00ae8afc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
- 00ae8afc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00ae8b40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8afc bytes 811a43f9
+ 00ae8b40 bytes 813a43f9
- 00ae8b20 ["INT_ADD", "register:40f0:8", ["const:ae8b20:8", "const:4:8"]]
- 00ae8b20 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8b64 ["INT_ADD", "register:40f0:8", ["const:ae8b64:8", "const:4:8"]]
+ 00ae8b64 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8b20 bytes 48d50394
+ 00ae8b64 bytes 4bd50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd903b84a0e3dcbfbd1a32f610583d9"></a>

### [`00ae8b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b58.md) → [`00ae8b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b9c.md) _ZN8firebase4util15character_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae8bb8",
      "incomplete_value": false,
      "site": "00ae8bbc",
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
      "definition_site": "00ae8b74",
      "incomplete_value": false,
      "site": "00ae8b78",
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
      "00ae8bb8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae8bc8",
      "DATA",
      [
        "storage",
        "010a0650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae8bb8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae8bc8",
      "DATA",
      [
        "storage",
        "010a0690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b58.md#insn-00ae8b78) · [`00ae8b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b58.md#insn-00ae8b74) · [`00ae8b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b58.md#insn-00ae8b80)
- 新版 `00ae8bbc`（命令位置の公開資料なし） · `00ae8bb8`（命令位置の公開資料なし） · `00ae8bc4`（命令位置の公開資料なし）

~~~diff
- 00ae8b78 ["INT_ADD", "register:40f0:8", ["const:ae8b78:8", "const:4:8"]]
- 00ae8b78 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae8bbc ["INT_ADD", "register:40f0:8", ["const:ae8bbc:8", "const:4:8"]]
+ 00ae8bbc ["CALL", null, ["callee:00bde180:8"]]
- 00ae8b78 bytes 6ed50394
+ 00ae8bbc bytes 71d50394
- 00ae8b74 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae8b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8bb8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae8bb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8bb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8bb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8b74 bytes 00fc1991
+ 00ae8bb8 bytes 00c81791
- 00ae8b80 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00ae8b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8bc4 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00ae8bc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8bc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8bc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8b80 bytes 08411991
+ 00ae8bc4 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea5e624464a17c62c9f868c43b17207b"></a>

### [`00ae8b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md) → [`00ae8bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae8c04",
      "incomplete_value": true,
      "site": "00ae8c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bc0",
      "incomplete_value": true,
      "site": "00ae8bc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8bec",
      "incomplete_value": true,
      "site": "00ae8bec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8ba8",
      "incomplete_value": true,
      "site": "00ae8ba8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8bf8",
      "incomplete_value": false,
      "site": "00ae8bfc",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bb4",
      "incomplete_value": false,
      "site": "00ae8bb8",
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
            "const:67b:8"
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
      "00ae8be8",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8bf8",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8c04",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8be8",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8bf8",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8c04",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md#insn-00ae8bb8) · [`00ae8bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md#insn-00ae8bc0) · [`00ae8ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md#insn-00ae8ba4)
- 新版 `00ae8bfc`（命令位置の公開資料なし） · `00ae8c04`（命令位置の公開資料なし） · `00ae8be8`（命令位置の公開資料なし）

~~~diff
- 00ae8bb8 ["INT_ADD", "register:40f0:8", ["const:ae8bb8:8", "const:4:8"]]
- 00ae8bb8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8bfc ["INT_ADD", "register:40f0:8", ["const:ae8bfc:8", "const:4:8"]]
+ 00ae8bfc ["CALL", null, ["callee:00bde090:8"]]
- 00ae8bb8 bytes 22d50394
+ 00ae8bfc bytes 25d50394
- 00ae8bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8c04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8bc0 bytes 602e03f9
+ 00ae8c04 bytes 604e03f9
- 00ae8ba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8ba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8be8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8be8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8ba4 bytes 682e43f9
+ 00ae8be8 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1becf42cfeb4dccb95d4c60b9417d86"></a>

### [`00ae8bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md) → [`00ae8c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c18.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae8c44",
      "incomplete_value": true,
      "site": "00ae8c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c00",
      "incomplete_value": true,
      "site": "00ae8c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8c2c",
      "incomplete_value": true,
      "site": "00ae8c2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8be8",
      "incomplete_value": true,
      "site": "00ae8be8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8c34",
      "incomplete_value": true,
      "site": "00ae8c3c",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bf0",
      "incomplete_value": true,
      "site": "00ae8bf8",
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
            "const:67b:8"
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
      "00ae8c28",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c34",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8c44",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8c28",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c34",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8c44",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md#insn-00ae8bf8) · [`00ae8c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md#insn-00ae8c00) · [`00ae8be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md#insn-00ae8be4)
- 新版 `00ae8c3c`（命令位置の公開資料なし） · `00ae8c44`（命令位置の公開資料なし） · `00ae8c28`（命令位置の公開資料なし）

~~~diff
- 00ae8bf8 ["INT_ADD", "register:40f0:8", ["const:ae8bf8:8", "const:4:8"]]
- 00ae8bf8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8c3c ["INT_ADD", "register:40f0:8", ["const:ae8c3c:8", "const:4:8"]]
+ 00ae8c3c ["CALL", null, ["callee:00bde090:8"]]
- 00ae8bf8 bytes 12d50394
+ 00ae8c3c bytes 15d50394
- 00ae8c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8c00 bytes 602e03f9
+ 00ae8c44 bytes 604e03f9
- 00ae8be4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8be4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8c28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8c28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8be4 bytes 682e43f9
+ 00ae8c28 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52eea7499d4aaa4cdcd0d9386abb1624"></a>

### [`00ae8c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c14.md) → [`00ae8c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c58.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8c88",
      "incomplete_value": true,
      "site": "00ae8c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c44",
      "incomplete_value": true,
      "site": "00ae8c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8c78",
      "incomplete_value": false,
      "site": "00ae8c80",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c34",
      "incomplete_value": false,
      "site": "00ae8c3c",
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
            "const:67b:8"
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
      "00ae8c68",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c78",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8c88",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8c68",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c78",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8c88",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c14.md#insn-00ae8c3c) · [`00ae8c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c14.md#insn-00ae8c44) · [`00ae8c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c14.md#insn-00ae8c24)
- 新版 `00ae8c80`（命令位置の公開資料なし） · `00ae8c88`（命令位置の公開資料なし） · `00ae8c68`（命令位置の公開資料なし）

~~~diff
- 00ae8c3c ["INT_ADD", "register:40f0:8", ["const:ae8c3c:8", "const:4:8"]]
- 00ae8c3c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8c80 ["INT_ADD", "register:40f0:8", ["const:ae8c80:8", "const:4:8"]]
+ 00ae8c80 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8c3c bytes 01d50394
+ 00ae8c80 bytes 04d50394
- 00ae8c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8c44 bytes 602e03f9
+ 00ae8c88 bytes 604e03f9
- 00ae8c24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8c24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8c24 bytes 682e43f9
+ 00ae8c68 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0b2c857d2880b3b968fbe7dc1d9e86e"></a>

### [`00ae8c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md) → [`00ae8c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8ccc",
      "incomplete_value": true,
      "site": "00ae8ccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c88",
      "incomplete_value": true,
      "site": "00ae8c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8cb0",
      "incomplete_value": true,
      "site": "00ae8cb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c6c",
      "incomplete_value": true,
      "site": "00ae8c6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8cb8",
      "incomplete_value": false,
      "site": "00ae8cc4",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c74",
      "incomplete_value": false,
      "site": "00ae8c80",
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
            "const:67b:8"
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
      "00ae8cac",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8cb8",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8ccc",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8cac",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8cb8",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8ccc",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md#insn-00ae8c80) · [`00ae8c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md#insn-00ae8c88) · [`00ae8c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md#insn-00ae8c68)
- 新版 `00ae8cc4`（命令位置の公開資料なし） · `00ae8ccc`（命令位置の公開資料なし） · `00ae8cac`（命令位置の公開資料なし）

~~~diff
- 00ae8c80 ["INT_ADD", "register:40f0:8", ["const:ae8c80:8", "const:4:8"]]
- 00ae8c80 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8cc4 ["INT_ADD", "register:40f0:8", ["const:ae8cc4:8", "const:4:8"]]
+ 00ae8cc4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8c80 bytes f0d40394
+ 00ae8cc4 bytes f3d40394
- 00ae8c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8c88 bytes 602e03f9
+ 00ae8ccc bytes 604e03f9
- 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00ae8c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00ae8cac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8c68 bytes 682e43f9
+ 00ae8cac bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cfb59660468f75c62b0b157604e8b22"></a>

### [`00ae8c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c9c.md) → [`00ae8ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ce0.md) _ZN8firebase4util11class_class8GetClassEv

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
      "definition_site": "00ae8ce4",
      "incomplete_value": true,
      "site": "00ae8ce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8ca0",
      "incomplete_value": true,
      "site": "00ae8ca4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:658:8"
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
      "00ae8ce4",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8ce4",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c9c.md#insn-00ae8ca0)
- 新版 `00ae8ce4`（命令位置の公開資料なし）

~~~diff
- 00ae8ca0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:658:8"]]
- 00ae8ca0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
+ 00ae8ce4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8ca0 bytes 002d43f9
+ 00ae8ce4 bytes 004d43f9
~~~


<a id="compare-e31720930a18abf3bfceb06ed298f83a"></a>

### [`00ae8ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md) → [`00ae8cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8cec.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae8d74",
      "incomplete_value": true,
      "site": "00ae8d74",
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
      "definition_site": "00ae8d30",
      "incomplete_value": true,
      "site": "00ae8d30",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8d20",
      "incomplete_value": true,
      "site": "00ae8d2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8cdc",
      "incomplete_value": true,
      "site": "00ae8ce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:658:8"
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
      "00ae8d00",
      "READ",
      [
        "storage",
        "010a0660",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8d20",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8d74",
      "WRITE",
      [
        "storage",
        "010a0660",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae8d00",
      "READ",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8d20",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8d74",
      "WRITE",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md#insn-00ae8ce8) · [`00ae8d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md#insn-00ae8d30) · [`00ae8cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md#insn-00ae8cbc)
- 新版 `00ae8d2c`（命令位置の公開資料なし） · `00ae8d74`（命令位置の公開資料なし） · `00ae8d00`（命令位置の公開資料なし）

~~~diff
- 00ae8ce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8ce8 ["INT_ADD", "register:40f0:8", ["const:ae8ce8:8", "const:4:8"]]
- 00ae8ce8 ["CALLIND", null, ["register:0:8"]]
+ 00ae8d2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae8d2c ["INT_ADD", "register:40f0:8", ["const:ae8d2c:8", "const:4:8"]]
+ 00ae8d2c ["CALLIND", null, ["register:0:8"]]
- 00ae8ce8 bytes 00013fd6
+ 00ae8d2c bytes 00013fd6
- 00ae8d30 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae8d30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:660:8"]]
- 00ae8d30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae8d74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae8d74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a0:8"]]
+ 00ae8d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae8d30 bytes a0821939
+ 00ae8d74 bytes a0821a39
- 00ae8cbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:660:8"]]
- 00ae8cbc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae8cbc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae8d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
+ 00ae8d00 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8d00 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae8cbc bytes a8825939
+ 00ae8d00 bytes a8825a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072a72a69126c467b1ed3db1d76c325a"></a>

### [`00ae8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8d44.md) → [`00ae8d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8d88.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8dc4",
      "incomplete_value": true,
      "site": "00ae8dc4",
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
      "definition_site": "00ae8d80",
      "incomplete_value": true,
      "site": "00ae8d80",
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
      "definition_site": "00ae8e14",
      "incomplete_value": true,
      "site": "00ae8e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8dd0",
      "incomplete_value": true,
      "site": "00ae8dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8e04",
      "incomplete_value": true,
      "site": "00ae8e10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8dc0",
      "incomplete_value": true,
      "site": "00ae8dcc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:658:8"
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
      "00ae8d9c",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8da8",
      "READ",
      [
        "storage",
        "010a0660",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8dc4",
      "WRITE",
      [
        "storage",
        "010a0660",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae8d9c",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8da8",
      "READ",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8dc4",
      "WRITE",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8d44.md#insn-00ae8d80) · [`00ae8dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8d44.md#insn-00ae8dcc) · [`00ae8dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8d44.md#insn-00ae8dd0)
- 新版 `00ae8dc4`（命令位置の公開資料なし） · `00ae8e10`（命令位置の公開資料なし） · `00ae8e14`（命令位置の公開資料なし）

~~~diff
- 00ae8d80 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae8d80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae8d80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:660:8"]]
- 00ae8d80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae8dc4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae8dc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae8dc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a0:8"]]
+ 00ae8dc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae8d80 bytes bf821939
+ 00ae8dc4 bytes bf821a39
- 00ae8dcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8dcc ["INT_ADD", "register:40f0:8", ["const:ae8dcc:8", "const:4:8"]]
- 00ae8dcc ["CALLIND", null, ["register:0:8"]]
+ 00ae8e10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae8e10 ["INT_ADD", "register:40f0:8", ["const:ae8e10:8", "const:4:8"]]
+ 00ae8e10 ["CALLIND", null, ["register:0:8"]]
- 00ae8dcc bytes 00013fd6
+ 00ae8e10 bytes 00013fd6
- 00ae8dd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00ae8dd0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae8dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae8e14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00ae8e14 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae8e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae8dd0 bytes 9f2e03f9
+ 00ae8e14 bytes 9f4e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0866a67e52c8bbbafb472f7dc1de07b"></a>

### [`00ae8de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md) → [`00ae8e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8e68",
      "incomplete_value": true,
      "site": "00ae8e68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e24",
      "incomplete_value": true,
      "site": "00ae8e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8e44",
      "incomplete_value": true,
      "site": "00ae8e44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e00",
      "incomplete_value": true,
      "site": "00ae8e00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8e4c",
      "incomplete_value": true,
      "site": "00ae8e60",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e08",
      "incomplete_value": true,
      "site": "00ae8e1c",
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
            "const:67b:8"
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
      "00ae8e3c",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8e4c",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8e68",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8e3c",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8e4c",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8e68",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md#insn-00ae8e1c) · [`00ae8e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md#insn-00ae8e24) · [`00ae8df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md#insn-00ae8df8)
- 新版 `00ae8e60`（命令位置の公開資料なし） · `00ae8e68`（命令位置の公開資料なし） · `00ae8e3c`（命令位置の公開資料なし）

~~~diff
- 00ae8e1c ["INT_ADD", "register:40f0:8", ["const:ae8e1c:8", "const:4:8"]]
- 00ae8e1c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8e60 ["INT_ADD", "register:40f0:8", ["const:ae8e60:8", "const:4:8"]]
+ 00ae8e60 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8e1c bytes 89d40394
+ 00ae8e60 bytes 8cd40394
- 00ae8e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00ae8e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8e68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00ae8e68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8e24 bytes 802e03f9
+ 00ae8e68 bytes 804e03f9
- 00ae8df8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00ae8df8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00ae8e3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8df8 bytes 812e43f9
+ 00ae8e3c bytes 814e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8e7c5d10b9e87e0c5712b5c9e37c13"></a>

### [`00ae8e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md) → [`00ae8ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8f14",
      "incomplete_value": true,
      "site": "00ae8f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8ed0",
      "incomplete_value": true,
      "site": "00ae8ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "00ae8ef0",
      "incomplete_value": true,
      "site": "00ae8ef0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8eac",
      "incomplete_value": true,
      "site": "00ae8eac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae8eac"
      ],
      [
        "FALL_THROUGH",
        "00ae8ef0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8ef0",
      "incomplete_value": true,
      "site": "00ae8f14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8eac",
      "incomplete_value": true,
      "site": "00ae8ed0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae8ee8",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ef8",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8f14",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8ee8",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8ef8",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8f14",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md#insn-00ae8ed0) · [`00ae8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md#insn-00ae8ea4) · [`00ae8eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md#insn-00ae8eb4)
- 新版 `00ae8f14`（命令位置の公開資料なし） · `00ae8ee8`（命令位置の公開資料なし） · `00ae8ef8`（命令位置の公開資料なし）

~~~diff
- 00ae8ed0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00ae8ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00ae8f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8ed0 bytes 802e03f9
+ 00ae8f14 bytes 804e03f9
- 00ae8ea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00ae8ea4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00ae8ee8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8ea4 bytes 812e43f9
+ 00ae8ee8 bytes 814e43f9
- 00ae8eb4 ["COPY", "tmp:0:8", ["const:67b:8"]]
- 00ae8eb4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8eb4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8eb4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae8ef8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00ae8ef8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae8ef8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae8ef8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae8eb4 bytes 63ec1991
+ 00ae8ef8 bytes 63b81791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ef5fde9bdda3b32853b85c7f2aad23"></a>

### [`00ae8f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f00.md) → [`00ae8f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f44.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae8f60",
      "incomplete_value": false,
      "site": "00ae8f64",
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
      "definition_site": "00ae8f1c",
      "incomplete_value": false,
      "site": "00ae8f20",
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
      "definition_site": "00ae8f70",
      "incomplete_value": true,
      "site": "00ae8f7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8f2c",
      "incomplete_value": true,
      "site": "00ae8f38",
      "value": [
        "LOAD",
        "8",
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
      "00ae8f60",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae8f70",
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
      "00ae8f60",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae8f70",
      "DATA",
      [
        "storage",
        "010a06b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f00.md#insn-00ae8f20) · [`00ae8f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f00.md#insn-00ae8f1c) · [`00ae8f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f00.md#insn-00ae8f28)
- 新版 `00ae8f64`（命令位置の公開資料なし） · `00ae8f60`（命令位置の公開資料なし） · `00ae8f6c`（命令位置の公開資料なし）

~~~diff
- 00ae8f20 ["INT_ADD", "register:40f0:8", ["const:ae8f20:8", "const:4:8"]]
- 00ae8f20 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae8f64 ["INT_ADD", "register:40f0:8", ["const:ae8f64:8", "const:4:8"]]
+ 00ae8f64 ["CALL", null, ["callee:00bde180:8"]]
- 00ae8f20 bytes 84d40394
+ 00ae8f64 bytes 87d40394
- 00ae8f1c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae8f1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8f1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8f1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8f60 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae8f60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8f60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8f60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8f1c bytes 00fc1991
+ 00ae8f60 bytes 00c81791
- 00ae8f28 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00ae8f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8f6c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00ae8f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8f28 bytes 08e11991
+ 00ae8f6c bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6782fddd85d56b99597170c964738d1"></a>

### [`00ae8f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f3c.md) → [`00ae8f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00ae8fac",
      "incomplete_value": true,
      "site": "00ae8fac",
      "value": [
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
      "definition_site": "00ae8f68",
      "incomplete_value": true,
      "site": "00ae8f68",
      "value": [
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
      "definition_site": "00ae8f94",
      "incomplete_value": true,
      "site": "00ae8f94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f50",
      "incomplete_value": true,
      "site": "00ae8f50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8fa0",
      "incomplete_value": false,
      "site": "00ae8fa4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f5c",
      "incomplete_value": false,
      "site": "00ae8f60",
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
            "const:e51:8"
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
      "00ae8f90",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8fa0",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae8fac",
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
      "00ae8f90",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8fa0",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae8fac",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f3c.md#insn-00ae8f60) · [`00ae8f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f3c.md#insn-00ae8f68) · [`00ae8f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f3c.md#insn-00ae8f4c)
- 新版 `00ae8fa4`（命令位置の公開資料なし） · `00ae8fac`（命令位置の公開資料なし） · `00ae8f90`（命令位置の公開資料なし）

~~~diff
- 00ae8f60 ["INT_ADD", "register:40f0:8", ["const:ae8f60:8", "const:4:8"]]
- 00ae8f60 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8fa4 ["INT_ADD", "register:40f0:8", ["const:ae8fa4:8", "const:4:8"]]
+ 00ae8fa4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8f60 bytes 38d40394
+ 00ae8fa4 bytes 3bd40394
- 00ae8f68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8fac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae8fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8f68 bytes 604203f9
+ 00ae8fac bytes 606203f9
- 00ae8f4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8f4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8f90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae8f90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8f4c bytes 684243f9
+ 00ae8f90 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb55a7950556351fb26428e9579ebaab"></a>

### [`00ae8f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md) → [`00ae8fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00ae8fec",
      "incomplete_value": true,
      "site": "00ae8fec",
      "value": [
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
      "definition_site": "00ae8fa8",
      "incomplete_value": true,
      "site": "00ae8fa8",
      "value": [
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
      "definition_site": "00ae8fd4",
      "incomplete_value": true,
      "site": "00ae8fd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f90",
      "incomplete_value": true,
      "site": "00ae8f90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae8fdc",
      "incomplete_value": false,
      "site": "00ae8fe4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f98",
      "incomplete_value": false,
      "site": "00ae8fa0",
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
            "const:e51:8"
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
      "00ae8fd0",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8fdc",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae8fec",
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
      "00ae8fd0",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8fdc",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae8fec",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md#insn-00ae8fa0) · [`00ae8fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md#insn-00ae8fa8) · [`00ae8f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md#insn-00ae8f8c)
- 新版 `00ae8fe4`（命令位置の公開資料なし） · `00ae8fec`（命令位置の公開資料なし） · `00ae8fd0`（命令位置の公開資料なし）

~~~diff
- 00ae8fa0 ["INT_ADD", "register:40f0:8", ["const:ae8fa0:8", "const:4:8"]]
- 00ae8fa0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8fe4 ["INT_ADD", "register:40f0:8", ["const:ae8fe4:8", "const:4:8"]]
+ 00ae8fe4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8fa0 bytes 28d40394
+ 00ae8fe4 bytes 2bd40394
- 00ae8fa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8fa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8fec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae8fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8fa8 bytes 604203f9
+ 00ae8fec bytes 606203f9
- 00ae8f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8f8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8fd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae8fd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8f8c bytes 684243f9
+ 00ae8fd0 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84783820ba03d538e071c6db51d50956"></a>

### [`00ae8fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8fbc.md) → [`00ae9000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9000.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9030",
      "incomplete_value": true,
      "site": "00ae9030",
      "value": [
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
      "definition_site": "00ae8fec",
      "incomplete_value": true,
      "site": "00ae8fec",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9010",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9020",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae9030",
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
      "00ae9010",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9020",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae9030",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8fbc.md#insn-00ae8fec) · [`00ae8fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8fbc.md#insn-00ae8fcc) · [`00ae8fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8fbc.md#insn-00ae8fdc)
- 新版 `00ae9030`（命令位置の公開資料なし） · `00ae9010`（命令位置の公開資料なし） · `00ae9020`（命令位置の公開資料なし）

~~~diff
- 00ae8fec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae9030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8fec bytes 604203f9
+ 00ae9030 bytes 606203f9
- 00ae8fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae8fcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae9010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8fcc bytes 684243f9
+ 00ae9010 bytes 686243f9
- 00ae8fdc ["COPY", "tmp:0:8", ["const:e51:8"]]
- 00ae8fdc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8fdc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae8fdc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae9020 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00ae9020 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae9020 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae9020 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae8fdc bytes 63443991
+ 00ae9020 bytes 63703b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59abc23ff8a6ef1d9f80b4706743ee66"></a>

### [`00ae9000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md) → [`00ae9044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9074",
      "incomplete_value": true,
      "site": "00ae9074",
      "value": [
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
      "definition_site": "00ae9030",
      "incomplete_value": true,
      "site": "00ae9030",
      "value": [
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
      "definition_site": "00ae9058",
      "incomplete_value": true,
      "site": "00ae9058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9014",
      "incomplete_value": true,
      "site": "00ae9014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9060",
      "incomplete_value": false,
      "site": "00ae906c",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae901c",
      "incomplete_value": false,
      "site": "00ae9028",
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
            "const:e51:8"
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
      "00ae9054",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9060",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae9074",
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
      "00ae9054",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9060",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae9074",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md#insn-00ae9028) · [`00ae9030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md#insn-00ae9030) · [`00ae9010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md#insn-00ae9010)
- 新版 `00ae906c`（命令位置の公開資料なし） · `00ae9074`（命令位置の公開資料なし） · `00ae9054`（命令位置の公開資料なし）

~~~diff
- 00ae9028 ["INT_ADD", "register:40f0:8", ["const:ae9028:8", "const:4:8"]]
- 00ae9028 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae906c ["INT_ADD", "register:40f0:8", ["const:ae906c:8", "const:4:8"]]
+ 00ae906c ["CALL", null, ["callee:00bde090:8"]]
- 00ae9028 bytes 06d40394
+ 00ae906c bytes 09d40394
- 00ae9030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae9074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9030 bytes 604203f9
+ 00ae9074 bytes 606203f9
- 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00ae9010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00ae9054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9010 bytes 684243f9
+ 00ae9054 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcfcd082692e51dd6f3f9b74a4704eaa"></a>

### [`00ae9050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9050.md) → [`00ae9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae911c",
      "incomplete_value": true,
      "site": "00ae911c",
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
      "definition_site": "00ae90d8",
      "incomplete_value": true,
      "site": "00ae90d8",
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
      "definition_site": "00ae90c8",
      "incomplete_value": true,
      "site": "00ae90d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9084",
      "incomplete_value": true,
      "site": "00ae9090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ae90a8",
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae90c8",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae911c",
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
      "00ae90a8",
      "READ",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae90c8",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae911c",
      "WRITE",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9050.md#insn-00ae9090) · [`00ae90d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9050.md#insn-00ae90d8) · [`00ae9064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9050.md#insn-00ae9064)
- 新版 `00ae90d4`（命令位置の公開資料なし） · `00ae911c`（命令位置の公開資料なし） · `00ae90a8`（命令位置の公開資料なし）

~~~diff
- 00ae9090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9090 ["INT_ADD", "register:40f0:8", ["const:ae9090:8", "const:4:8"]]
- 00ae9090 ["CALLIND", null, ["register:0:8"]]
+ 00ae90d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae90d4 ["INT_ADD", "register:40f0:8", ["const:ae90d4:8", "const:4:8"]]
+ 00ae90d4 ["CALLIND", null, ["register:0:8"]]
- 00ae9090 bytes 00013fd6
+ 00ae90d4 bytes 00013fd6
- 00ae90d8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae90d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
- 00ae90d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae911c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae911c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
+ 00ae911c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae90d8 bytes a0221a39
+ 00ae911c bytes a0221b39
- 00ae9064 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
- 00ae9064 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae9064 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae90a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00ae90a8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae90a8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae9064 bytes a8225a39
+ 00ae90a8 bytes a8225b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e962ae86fccc72b446903ca3d8c4e1"></a>

### [`00ae90ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md) → [`00ae9130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae916c",
      "incomplete_value": true,
      "site": "00ae916c",
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
      "definition_site": "00ae9128",
      "incomplete_value": true,
      "site": "00ae9128",
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
      "definition_site": "00ae91bc",
      "incomplete_value": true,
      "site": "00ae91bc",
      "value": [
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
      "definition_site": "00ae9178",
      "incomplete_value": true,
      "site": "00ae9178",
      "value": [
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
      "definition_site": "00ae9148",
      "incomplete_value": true,
      "site": "00ae9148",
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
      "definition_site": "00ae9104",
      "incomplete_value": true,
      "site": "00ae9104",
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
      "00ae9144",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9150",
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae916c",
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
      "00ae9144",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9150",
      "READ",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae916c",
      "WRITE",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md#insn-00ae9128) · [`00ae9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md#insn-00ae9174) · [`00ae9178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md#insn-00ae9178)
- 新版 `00ae916c`（命令位置の公開資料なし） · `00ae91b8`（命令位置の公開資料なし） · `00ae91bc`（命令位置の公開資料なし）

~~~diff
- 00ae9128 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9128 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9128 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
- 00ae9128 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae916c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae916c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae916c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
+ 00ae916c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9128 bytes bf221a39
+ 00ae916c bytes bf221b39
- 00ae9174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9174 ["INT_ADD", "register:40f0:8", ["const:ae9174:8", "const:4:8"]]
- 00ae9174 ["CALLIND", null, ["register:0:8"]]
+ 00ae91b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae91b8 ["INT_ADD", "register:40f0:8", ["const:ae91b8:8", "const:4:8"]]
+ 00ae91b8 ["CALLIND", null, ["register:0:8"]]
- 00ae9174 bytes 00013fd6
+ 00ae91b8 bytes 00013fd6
- 00ae9178 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae9178 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae9178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae91bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00ae91bc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae91bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae9178 bytes 9f4203f9
+ 00ae91bc bytes 9f6203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b16687d9b0740e23ee9fc45f72b95e1"></a>

### [`00ae918c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md) → [`00ae91d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9210",
      "incomplete_value": true,
      "site": "00ae9210",
      "value": [
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
      "definition_site": "00ae91cc",
      "incomplete_value": true,
      "site": "00ae91cc",
      "value": [
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
      "definition_site": "00ae91ec",
      "incomplete_value": true,
      "site": "00ae91ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae91a8",
      "incomplete_value": true,
      "site": "00ae91a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae91f4",
      "incomplete_value": false,
      "site": "00ae9208",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae91b0",
      "incomplete_value": false,
      "site": "00ae91c4",
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
            "const:e51:8"
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
      "00ae91e4",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae91f4",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae9210",
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
      "00ae91e4",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae91f4",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae9210",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md#insn-00ae91c4) · [`00ae91cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md#insn-00ae91cc) · [`00ae91a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md#insn-00ae91a0)
- 新版 `00ae9208`（命令位置の公開資料なし） · `00ae9210`（命令位置の公開資料なし） · `00ae91e4`（命令位置の公開資料なし）

~~~diff
- 00ae91c4 ["INT_ADD", "register:40f0:8", ["const:ae91c4:8", "const:4:8"]]
- 00ae91c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9208 ["INT_ADD", "register:40f0:8", ["const:ae9208:8", "const:4:8"]]
+ 00ae9208 ["CALL", null, ["callee:00bde090:8"]]
- 00ae91c4 bytes 9fd30394
+ 00ae9208 bytes a2d30394
- 00ae91cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae91cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00ae9210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae91cc bytes 804203f9
+ 00ae9210 bytes 806203f9
- 00ae91a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae91a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae91e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00ae91e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae91a0 bytes 814243f9
+ 00ae91e4 bytes 816243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dabfd646780d7c424ac039eff7b6ade"></a>

### [`00ae91fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md) → [`00ae9240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae925c",
      "incomplete_value": false,
      "site": "00ae9260",
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
      "definition_site": "00ae9218",
      "incomplete_value": false,
      "site": "00ae921c",
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
      "definition_site": "00ae926c",
      "incomplete_value": true,
      "site": "00ae9278",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9228",
      "incomplete_value": true,
      "site": "00ae9234",
      "value": [
        "LOAD",
        "8",
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
      "00ae925c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae926c",
      "DATA",
      [
        "storage",
        "010a0690",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae925c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae926c",
      "DATA",
      [
        "storage",
        "010a06d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae921c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md#insn-00ae921c) · [`00ae9218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md#insn-00ae9218) · [`00ae9224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md#insn-00ae9224)
- 新版 `00ae9260`（命令位置の公開資料なし） · `00ae925c`（命令位置の公開資料なし） · `00ae9268`（命令位置の公開資料なし）

~~~diff
- 00ae921c ["INT_ADD", "register:40f0:8", ["const:ae921c:8", "const:4:8"]]
- 00ae921c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae9260 ["INT_ADD", "register:40f0:8", ["const:ae9260:8", "const:4:8"]]
+ 00ae9260 ["CALL", null, ["callee:00bde180:8"]]
- 00ae921c bytes c5d30394
+ 00ae9260 bytes c8d30394
- 00ae9218 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae9218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae925c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae925c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae925c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae925c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9218 bytes 00501791
+ 00ae925c bytes 001c1591
- 00ae9224 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00ae9224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9268 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00ae9268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9224 bytes 08411a91
+ 00ae9268 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99968edcc948f04ea994b0a757dfc158"></a>

### [`00ae9238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md) → [`00ae927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae92bc",
      "incomplete_value": true,
      "site": "00ae92bc",
      "value": [
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
      "definition_site": "00ae9278",
      "incomplete_value": true,
      "site": "00ae9278",
      "value": [
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
      "definition_site": "00ae9298",
      "incomplete_value": true,
      "site": "00ae9298",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9254",
      "incomplete_value": true,
      "site": "00ae9254",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae92a0",
      "incomplete_value": false,
      "site": "00ae92b4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae925c",
      "incomplete_value": false,
      "site": "00ae9270",
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
            "const:e51:8"
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
      "00ae9290",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae92a0",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae92bc",
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
      "00ae9290",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae92a0",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00ae92bc",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md#insn-00ae9270) · [`00ae9278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md#insn-00ae9278) · [`00ae924c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md#insn-00ae924c)
- 新版 `00ae92b4`（命令位置の公開資料なし） · `00ae92bc`（命令位置の公開資料なし） · `00ae9290`（命令位置の公開資料なし）

~~~diff
- 00ae9270 ["INT_ADD", "register:40f0:8", ["const:ae9270:8", "const:4:8"]]
- 00ae9270 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae92b4 ["INT_ADD", "register:40f0:8", ["const:ae92b4:8", "const:4:8"]]
+ 00ae92b4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9270 bytes 74d30394
+ 00ae92b4 bytes 77d30394
- 00ae9278 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae9278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae92bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00ae92bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9278 bytes 804203f9
+ 00ae92bc bytes 806203f9
- 00ae924c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00ae924c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00ae9290 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae924c bytes 814243f9
+ 00ae9290 bytes 816243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e07ccfcac97a040f523b5cefce59289"></a>

### [`00ae92a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md) → [`00ae92ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae92ec.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae9308",
      "incomplete_value": false,
      "site": "00ae930c",
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
      "definition_site": "00ae92c4",
      "incomplete_value": false,
      "site": "00ae92c8",
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
      "definition_site": "00ae9318",
      "incomplete_value": true,
      "site": "00ae9324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae92d4",
      "incomplete_value": true,
      "site": "00ae92e0",
      "value": [
        "LOAD",
        "8",
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
      "00ae9308",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae9318",
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
      "00ae9308",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae9318",
      "DATA",
      [
        "storage",
        "010a06e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae92c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md#insn-00ae92c8) · [`00ae92c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md#insn-00ae92c4) · [`00ae92d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md#insn-00ae92d0)
- 新版 `00ae930c`（命令位置の公開資料なし） · `00ae9308`（命令位置の公開資料なし） · `00ae9314`（命令位置の公開資料なし）

~~~diff
- 00ae92c8 ["INT_ADD", "register:40f0:8", ["const:ae92c8:8", "const:4:8"]]
- 00ae92c8 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae930c ["INT_ADD", "register:40f0:8", ["const:ae930c:8", "const:4:8"]]
+ 00ae930c ["CALL", null, ["callee:00bde180:8"]]
- 00ae92c8 bytes 9ad30394
+ 00ae930c bytes 9dd30394
- 00ae92c4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae92c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae92c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae92c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9308 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae9308 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9308 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9308 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae92c4 bytes 00fc1991
+ 00ae9308 bytes 00c81791
- 00ae92d0 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00ae92d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae92d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae92d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9314 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00ae9314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae92d0 bytes 08811a91
+ 00ae9314 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee1d5fc1ba035b50380d06ab2341b69"></a>

### [`00ae92e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md) → [`00ae9328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

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
      "definition_site": "00ae9354",
      "incomplete_value": true,
      "site": "00ae9354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9310",
      "incomplete_value": true,
      "site": "00ae9310",
      "value": [
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
      "definition_site": "00ae933c",
      "incomplete_value": true,
      "site": "00ae933c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae92f8",
      "incomplete_value": true,
      "site": "00ae92f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9348",
      "incomplete_value": false,
      "site": "00ae934c",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9304",
      "incomplete_value": false,
      "site": "00ae9308",
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
            "const:d54:8"
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
      "00ae9338",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9348",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9354",
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
      "00ae9338",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9348",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae9354",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md#insn-00ae9308) · [`00ae9310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md#insn-00ae9310) · [`00ae92f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md#insn-00ae92f4)
- 新版 `00ae934c`（命令位置の公開資料なし） · `00ae9354`（命令位置の公開資料なし） · `00ae9338`（命令位置の公開資料なし）

~~~diff
- 00ae9308 ["INT_ADD", "register:40f0:8", ["const:ae9308:8", "const:4:8"]]
- 00ae9308 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae934c ["INT_ADD", "register:40f0:8", ["const:ae934c:8", "const:4:8"]]
+ 00ae934c ["CALL", null, ["callee:00bde090:8"]]
- 00ae9308 bytes 4ed30394
+ 00ae934c bytes 51d30394
- 00ae9310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae9310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae9354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9310 bytes 605603f9
+ 00ae9354 bytes 607603f9
- 00ae92f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae92f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae9338 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae92f4 bytes 685643f9
+ 00ae9338 bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf48935f3506aade826a5fb82555fb2"></a>

### [`00ae9324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md) → [`00ae9368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae9394",
      "incomplete_value": true,
      "site": "00ae9394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9350",
      "incomplete_value": true,
      "site": "00ae9350",
      "value": [
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
      "definition_site": "00ae937c",
      "incomplete_value": true,
      "site": "00ae937c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9338",
      "incomplete_value": true,
      "site": "00ae9338",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9384",
      "incomplete_value": false,
      "site": "00ae938c",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9340",
      "incomplete_value": false,
      "site": "00ae9348",
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
            "const:d54:8"
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
      "00ae9378",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9384",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9394",
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
      "00ae9378",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9384",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae9394",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md#insn-00ae9348) · [`00ae9350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md#insn-00ae9350) · [`00ae9334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md#insn-00ae9334)
- 新版 `00ae938c`（命令位置の公開資料なし） · `00ae9394`（命令位置の公開資料なし） · `00ae9378`（命令位置の公開資料なし）

~~~diff
- 00ae9348 ["INT_ADD", "register:40f0:8", ["const:ae9348:8", "const:4:8"]]
- 00ae9348 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
+ 00ae938c ["CALL", null, ["callee:00bde090:8"]]
- 00ae9348 bytes 3ed30394
+ 00ae938c bytes 41d30394
- 00ae9350 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae9350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae9394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9350 bytes 605603f9
+ 00ae9394 bytes 607603f9
- 00ae9334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae9334 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae9378 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9334 bytes 685643f9
+ 00ae9378 bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-209bcfafb26e425410fb5a80c2b8e977"></a>

### [`00ae9364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md) → [`00ae93a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae93d8",
      "incomplete_value": true,
      "site": "00ae93d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9394",
      "incomplete_value": true,
      "site": "00ae9394",
      "value": [
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
      "definition_site": "00ae93bc",
      "incomplete_value": true,
      "site": "00ae93bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9378",
      "incomplete_value": true,
      "site": "00ae9378",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae93c8",
      "incomplete_value": false,
      "site": "00ae93d0",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9384",
      "incomplete_value": false,
      "site": "00ae938c",
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
            "const:d54:8"
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
      "00ae93b8",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae93c8",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae93d8",
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
      "00ae93b8",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae93c8",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae93d8",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae938c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md#insn-00ae938c) · [`00ae9394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md#insn-00ae9394) · [`00ae9374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md#insn-00ae9374)
- 新版 `00ae93d0`（命令位置の公開資料なし） · `00ae93d8`（命令位置の公開資料なし） · `00ae93b8`（命令位置の公開資料なし）

~~~diff
- 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
- 00ae938c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
+ 00ae93d0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae938c bytes 2dd30394
+ 00ae93d0 bytes 30d30394
- 00ae9394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae9394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae93d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae93d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9394 bytes 605603f9
+ 00ae93d8 bytes 607603f9
- 00ae9374 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae9374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae93b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9374 bytes 685643f9
+ 00ae93b8 bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e185bd611d63cc4f3a303e4c701b07"></a>

### [`00ae93a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md) → [`00ae93ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae941c",
      "incomplete_value": true,
      "site": "00ae941c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93d8",
      "incomplete_value": true,
      "site": "00ae93d8",
      "value": [
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
      "definition_site": "00ae9400",
      "incomplete_value": true,
      "site": "00ae9400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93bc",
      "incomplete_value": true,
      "site": "00ae93bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9408",
      "incomplete_value": false,
      "site": "00ae9414",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93c4",
      "incomplete_value": false,
      "site": "00ae93d0",
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
            "const:d54:8"
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
      "00ae93fc",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9408",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae941c",
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
      "00ae93fc",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9408",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae941c",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae93d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md#insn-00ae93d0) · [`00ae93d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md#insn-00ae93d8) · [`00ae93b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md#insn-00ae93b8)
- 新版 `00ae9414`（命令位置の公開資料なし） · `00ae941c`（命令位置の公開資料なし） · `00ae93fc`（命令位置の公開資料なし）

~~~diff
- 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
- 00ae93d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9414 ["INT_ADD", "register:40f0:8", ["const:ae9414:8", "const:4:8"]]
+ 00ae9414 ["CALL", null, ["callee:00bde090:8"]]
- 00ae93d0 bytes 1cd30394
+ 00ae9414 bytes 1fd30394
- 00ae93d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae93d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae941c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae941c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae93d8 bytes 605603f9
+ 00ae941c bytes 607603f9
- 00ae93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00ae93b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae93fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00ae93fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae93b8 bytes 685643f9
+ 00ae93fc bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ee7bb8d2c4d425c6ab57a2c4364bba8"></a>

### [`00ae93f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md) → [`00ae943c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae94c4",
      "incomplete_value": true,
      "site": "00ae94c4",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9480",
      "incomplete_value": true,
      "site": "00ae9480",
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
      "definition_site": "00ae9470",
      "incomplete_value": true,
      "site": "00ae947c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae942c",
      "incomplete_value": true,
      "site": "00ae9438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ae9450",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9470",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94c4",
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
      "00ae9450",
      "READ",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9470",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94c4",
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md#insn-00ae9438) · [`00ae9480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md#insn-00ae9480) · [`00ae940c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md#insn-00ae940c)
- 新版 `00ae947c`（命令位置の公開資料なし） · `00ae94c4`（命令位置の公開資料なし） · `00ae9450`（命令位置の公開資料なし）

~~~diff
- 00ae9438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9438 ["INT_ADD", "register:40f0:8", ["const:ae9438:8", "const:4:8"]]
- 00ae9438 ["CALLIND", null, ["register:0:8"]]
+ 00ae947c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae947c ["INT_ADD", "register:40f0:8", ["const:ae947c:8", "const:4:8"]]
+ 00ae947c ["CALLIND", null, ["register:0:8"]]
- 00ae9438 bytes 00013fd6
+ 00ae947c bytes 00013fd6
- 00ae9480 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9480 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6b0:8"]]
- 00ae9480 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae94c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae94c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6f0:8"]]
+ 00ae94c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9480 bytes a0c21a39
+ 00ae94c4 bytes a0c21b39
- 00ae940c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
- 00ae940c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae940c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae9450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
+ 00ae9450 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9450 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae940c bytes a8c25a39
+ 00ae9450 bytes a8c25b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0dd1ac111f04e09c306303a9533d35c"></a>

### [`00ae9494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md) → [`00ae94d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9514",
      "incomplete_value": true,
      "site": "00ae9514",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae94d0",
      "incomplete_value": true,
      "site": "00ae94d0",
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
      "definition_site": "00ae9564",
      "incomplete_value": true,
      "site": "00ae9564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9520",
      "incomplete_value": true,
      "site": "00ae9520",
      "value": [
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
      "definition_site": "00ae94f0",
      "incomplete_value": true,
      "site": "00ae94f0",
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
      "definition_site": "00ae94ac",
      "incomplete_value": true,
      "site": "00ae94ac",
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
      "00ae94ec",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94f8",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9514",
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
      "00ae94ec",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94f8",
      "READ",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9514",
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae94d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md#insn-00ae94d0) · [`00ae9520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md#insn-00ae9520) · [`00ae94a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md#insn-00ae94a8)
- 新版 `00ae9514`（命令位置の公開資料なし） · `00ae9564`（命令位置の公開資料なし） · `00ae94ec`（命令位置の公開資料なし）

~~~diff
- 00ae94d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae94d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae94d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6b0:8"]]
- 00ae94d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae9514 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae9514 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae9514 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
+ 00ae9514 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae94d0 bytes bfc21a39
+ 00ae9514 bytes bfc21b39
- 00ae9520 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae9520 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae9520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae9564 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae9564 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae9564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae9520 bytes 9f5603f9
+ 00ae9564 bytes 9f7603f9
- 00ae94a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae94a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae94ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae94ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae94a8 bytes 815643f9
+ 00ae94ec bytes 817643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e57f2749555f211fa710c3c232ef04"></a>

### [`00ae9534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9534.md) → [`00ae9578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae95b8",
      "incomplete_value": true,
      "site": "00ae95b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9574",
      "incomplete_value": true,
      "site": "00ae9574",
      "value": [
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
      "definition_site": "00ae9594",
      "incomplete_value": true,
      "site": "00ae9594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9550",
      "incomplete_value": true,
      "site": "00ae9550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae959c",
      "incomplete_value": false,
      "site": "00ae95b0",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9558",
      "incomplete_value": false,
      "site": "00ae956c",
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
            "const:d54:8"
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
      "00ae958c",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae959c",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae95b8",
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
      "00ae958c",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae959c",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae95b8",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae956c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9534.md#insn-00ae956c) · [`00ae9574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9534.md#insn-00ae9574) · [`00ae9548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9534.md#insn-00ae9548)
- 新版 `00ae95b0`（命令位置の公開資料なし） · `00ae95b8`（命令位置の公開資料なし） · `00ae958c`（命令位置の公開資料なし）

~~~diff
- 00ae956c ["INT_ADD", "register:40f0:8", ["const:ae956c:8", "const:4:8"]]
- 00ae956c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae95b0 ["INT_ADD", "register:40f0:8", ["const:ae95b0:8", "const:4:8"]]
+ 00ae95b0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae956c bytes b5d20394
+ 00ae95b0 bytes b8d20394
- 00ae9574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae9574 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae95b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae95b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9574 bytes 805603f9
+ 00ae95b8 bytes 807603f9
- 00ae9548 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae9548 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae958c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae958c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9548 bytes 815643f9
+ 00ae958c bytes 817643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba0ca0c725636c766d22ce4b0573191"></a>

### [`00ae95a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95a4.md) → [`00ae95e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde670.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6c0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00ae9604",
      "incomplete_value": false,
      "site": "00ae9608",
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
      "definition_site": "00ae95c0",
      "incomplete_value": false,
      "site": "00ae95c4",
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
      "definition_site": "00ae9614",
      "incomplete_value": true,
      "site": "00ae9620",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae95d0",
      "incomplete_value": true,
      "site": "00ae95dc",
      "value": [
        "LOAD",
        "8",
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
      "00ae9604",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae9614",
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
      "00ae9604",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae9614",
      "DATA",
      [
        "storage",
        "010a06f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae95c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95a4.md#insn-00ae95c4) · [`00ae95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95a4.md#insn-00ae95c0) · [`00ae95cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95a4.md#insn-00ae95cc)
- 新版 `00ae9608`（命令位置の公開資料なし） · `00ae9604`（命令位置の公開資料なし） · `00ae9610`（命令位置の公開資料なし）

~~~diff
- 00ae95c4 ["INT_ADD", "register:40f0:8", ["const:ae95c4:8", "const:4:8"]]
- 00ae95c4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae9608 ["INT_ADD", "register:40f0:8", ["const:ae9608:8", "const:4:8"]]
+ 00ae9608 ["CALL", null, ["callee:00bde180:8"]]
- 00ae95c4 bytes dbd20394
+ 00ae9608 bytes ded20394
- 00ae95c0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae95c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae95c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae95c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9604 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae9604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae95c0 bytes 00501791
+ 00ae9604 bytes 001c1591
- 00ae95cc ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00ae95cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae95cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae95cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9610 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00ae9610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae95cc bytes 08e11a91
+ 00ae9610 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3018a8def46ebcd4cdebf916f5e7cead"></a>

### [`00ae95e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95e0.md) → [`00ae9624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9664",
      "incomplete_value": true,
      "site": "00ae9664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9620",
      "incomplete_value": true,
      "site": "00ae9620",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae9638",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9648",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9664",
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
      "00ae9638",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9648",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00ae9664",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95e0.md#insn-00ae9620) · [`00ae95f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95e0.md#insn-00ae95f4) · [`00ae9604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95e0.md#insn-00ae9604)
- 新版 `00ae9664`（命令位置の公開資料なし） · `00ae9638`（命令位置の公開資料なし） · `00ae9648`（命令位置の公開資料なし）

~~~diff
- 00ae9620 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae9620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae9664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9620 bytes 805603f9
+ 00ae9664 bytes 807603f9
- 00ae95f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00ae95f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00ae9638 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae95f4 bytes 815643f9
+ 00ae9638 bytes 817643f9
- 00ae9604 ["COPY", "tmp:0:8", ["const:d54:8"]]
- 00ae9604 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae9604 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae9604 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae9648 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00ae9648 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae9648 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae9648 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae9604 bytes 63503591
+ 00ae9648 bytes 637c3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d9baab04b679ea09474900f968ab2f"></a>

### [`00ae9650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9650.md) → [`00ae9694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae96b0",
      "incomplete_value": false,
      "site": "00ae96b4",
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
      "definition_site": "00ae966c",
      "incomplete_value": false,
      "site": "00ae9670",
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
      "definition_site": "00ae96c0",
      "incomplete_value": true,
      "site": "00ae96cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae967c",
      "incomplete_value": true,
      "site": "00ae9688",
      "value": [
        "LOAD",
        "8",
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
      "00ae96b0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae96c0",
      "DATA",
      [
        "storage",
        "010a06d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae96b0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae96c0",
      "DATA",
      [
        "storage",
        "010a0710",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9650.md#insn-00ae9670) · [`00ae966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9650.md#insn-00ae966c) · [`00ae9678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9650.md#insn-00ae9678)
- 新版 `00ae96b4`（命令位置の公開資料なし） · `00ae96b0`（命令位置の公開資料なし） · `00ae96bc`（命令位置の公開資料なし）

~~~diff
- 00ae9670 ["INT_ADD", "register:40f0:8", ["const:ae9670:8", "const:4:8"]]
- 00ae9670 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae96b4 ["INT_ADD", "register:40f0:8", ["const:ae96b4:8", "const:4:8"]]
+ 00ae96b4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae9670 bytes b0d20394
+ 00ae96b4 bytes b3d20394
- 00ae966c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae966c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae966c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae966c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae96b0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae96b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae96b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae96b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae966c bytes 00fc1991
+ 00ae96b0 bytes 00c81791
- 00ae9678 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00ae9678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae96bc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00ae96bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae96bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae96bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9678 bytes 08411b91
+ 00ae96bc bytes 08411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a7d105c49fc37639ef1dc19aaa3cdc"></a>

### [`00ae968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae968c.md) → [`00ae96d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00ae96fc",
      "incomplete_value": true,
      "site": "00ae96fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96b8",
      "incomplete_value": true,
      "site": "00ae96b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae96e4",
      "incomplete_value": true,
      "site": "00ae96e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96a0",
      "incomplete_value": true,
      "site": "00ae96a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae96f0",
      "incomplete_value": false,
      "site": "00ae96f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96ac",
      "incomplete_value": false,
      "site": "00ae96b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "00ae96e0",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae96f0",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae96fc",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae96e0",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae96f0",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae96fc",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae96b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae968c.md#insn-00ae96b0) · [`00ae96b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae968c.md#insn-00ae96b8) · [`00ae969c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae968c.md#insn-00ae969c)
- 新版 `00ae96f4`（命令位置の公開資料なし） · `00ae96fc`（命令位置の公開資料なし） · `00ae96e0`（命令位置の公開資料なし）

~~~diff
- 00ae96b0 ["INT_ADD", "register:40f0:8", ["const:ae96b0:8", "const:4:8"]]
- 00ae96b0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae96f4 ["INT_ADD", "register:40f0:8", ["const:ae96f4:8", "const:4:8"]]
+ 00ae96f4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae96b0 bytes 64d20394
+ 00ae96f4 bytes 67d20394
- 00ae96b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae96b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae96fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae96fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae96b8 bytes 606e03f9
+ 00ae96fc bytes 608e03f9
- 00ae969c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae969c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae96e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae96e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae969c bytes 686e43f9
+ 00ae96e0 bytes 688e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e681d334ce2fd19445ba9e99bd8f90"></a>

### [`00ae96cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae96cc.md) → [`00ae9710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae973c",
      "incomplete_value": true,
      "site": "00ae973c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96f8",
      "incomplete_value": true,
      "site": "00ae96f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae9724",
      "incomplete_value": true,
      "site": "00ae9724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96e0",
      "incomplete_value": true,
      "site": "00ae96e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae972c",
      "incomplete_value": false,
      "site": "00ae9734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96e8",
      "incomplete_value": false,
      "site": "00ae96f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "00ae9720",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae972c",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae973c",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9720",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae972c",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae973c",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae96f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae96cc.md#insn-00ae96f0) · [`00ae96f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae96cc.md#insn-00ae96f8) · [`00ae96dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae96cc.md#insn-00ae96dc)
- 新版 `00ae9734`（命令位置の公開資料なし） · `00ae973c`（命令位置の公開資料なし） · `00ae9720`（命令位置の公開資料なし）

~~~diff
- 00ae96f0 ["INT_ADD", "register:40f0:8", ["const:ae96f0:8", "const:4:8"]]
- 00ae96f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9734 ["INT_ADD", "register:40f0:8", ["const:ae9734:8", "const:4:8"]]
+ 00ae9734 ["CALL", null, ["callee:00bde090:8"]]
- 00ae96f0 bytes 54d20394
+ 00ae9734 bytes 57d20394
- 00ae96f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae96f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae973c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae973c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae96f8 bytes 606e03f9
+ 00ae973c bytes 608e03f9
- 00ae96dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae96dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae9720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae96dc bytes 686e43f9
+ 00ae9720 bytes 688e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024784daff30bffa2c49b16dcf2d4015"></a>

### [`00ae970c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae970c.md) → [`00ae9750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae9780",
      "incomplete_value": true,
      "site": "00ae9780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae973c",
      "incomplete_value": true,
      "site": "00ae973c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae9764",
      "incomplete_value": true,
      "site": "00ae9764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9720",
      "incomplete_value": true,
      "site": "00ae9720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9770",
      "incomplete_value": false,
      "site": "00ae9778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae972c",
      "incomplete_value": false,
      "site": "00ae9734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "00ae9760",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9770",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae9780",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9760",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9770",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae9780",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae970c.md#insn-00ae9734) · [`00ae973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae970c.md#insn-00ae973c) · [`00ae971c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae970c.md#insn-00ae971c)
- 新版 `00ae9778`（命令位置の公開資料なし） · `00ae9780`（命令位置の公開資料なし） · `00ae9760`（命令位置の公開資料なし）

~~~diff
- 00ae9734 ["INT_ADD", "register:40f0:8", ["const:ae9734:8", "const:4:8"]]
- 00ae9734 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9778 ["INT_ADD", "register:40f0:8", ["const:ae9778:8", "const:4:8"]]
+ 00ae9778 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9734 bytes 43d20394
+ 00ae9778 bytes 46d20394
- 00ae973c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae973c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae9780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae973c bytes 606e03f9
+ 00ae9780 bytes 608e03f9
- 00ae971c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae971c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae9760 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae971c bytes 686e43f9
+ 00ae9760 bytes 688e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee640d77d64f8af5b4bc69b2b4681308"></a>

### [`00ae9750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9750.md) → [`00ae9794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae97c4",
      "incomplete_value": true,
      "site": "00ae97c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9780",
      "incomplete_value": true,
      "site": "00ae9780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae97a8",
      "incomplete_value": true,
      "site": "00ae97a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9764",
      "incomplete_value": true,
      "site": "00ae9764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae97b0",
      "incomplete_value": false,
      "site": "00ae97bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae976c",
      "incomplete_value": false,
      "site": "00ae9778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "00ae97a4",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae97b0",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae97c4",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae97a4",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae97b0",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae97c4",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9750.md#insn-00ae9778) · [`00ae9780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9750.md#insn-00ae9780) · [`00ae9760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9750.md#insn-00ae9760)
- 新版 `00ae97bc`（命令位置の公開資料なし） · `00ae97c4`（命令位置の公開資料なし） · `00ae97a4`（命令位置の公開資料なし）

~~~diff
- 00ae9778 ["INT_ADD", "register:40f0:8", ["const:ae9778:8", "const:4:8"]]
- 00ae9778 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae97bc ["INT_ADD", "register:40f0:8", ["const:ae97bc:8", "const:4:8"]]
+ 00ae97bc ["CALL", null, ["callee:00bde090:8"]]
- 00ae9778 bytes 32d20394
+ 00ae97bc bytes 35d20394
- 00ae9780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae9780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae97c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae97c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9780 bytes 606e03f9
+ 00ae97c4 bytes 608e03f9
- 00ae9760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00ae9760 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae97a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00ae97a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9760 bytes 686e43f9
+ 00ae97a4 bytes 688e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f67d6a9ccbc6a0320166e40e7eef09c"></a>

### [`00ae97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae97a0.md) → [`00ae97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae986c",
      "incomplete_value": true,
      "site": "00ae986c",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9828",
      "incomplete_value": true,
      "site": "00ae9828",
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
            "const:6e0:8"
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
      "definition_site": "00ae9818",
      "incomplete_value": true,
      "site": "00ae9824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:718:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97d4",
      "incomplete_value": true,
      "site": "00ae97e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d8:8"
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
      "00ae97f8",
      "READ",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9818",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae986c",
      "WRITE",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae97f8",
      "READ",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9818",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae986c",
      "WRITE",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae97e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae97a0.md#insn-00ae97e0) · [`00ae9828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae97a0.md#insn-00ae9828) · [`00ae97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae97a0.md#insn-00ae97b4)
- 新版 `00ae9824`（命令位置の公開資料なし） · `00ae986c`（命令位置の公開資料なし） · `00ae97f8`（命令位置の公開資料なし）

~~~diff
- 00ae97e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae97e0 ["INT_ADD", "register:40f0:8", ["const:ae97e0:8", "const:4:8"]]
- 00ae97e0 ["CALLIND", null, ["register:0:8"]]
+ 00ae9824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9824 ["INT_ADD", "register:40f0:8", ["const:ae9824:8", "const:4:8"]]
+ 00ae9824 ["CALLIND", null, ["register:0:8"]]
- 00ae97e0 bytes 00013fd6
+ 00ae9824 bytes 00013fd6
- 00ae9828 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9828 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e0:8"]]
- 00ae9828 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae986c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae986c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:720:8"]]
+ 00ae986c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9828 bytes a0821b39
+ 00ae986c bytes a0821c39
- 00ae97b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e0:8"]]
- 00ae97b4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae97b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae97f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:720:8"]]
+ 00ae97f8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae97f8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae97b4 bytes a8825b39
+ 00ae97f8 bytes a8825c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-448e18ec85336931afd025e61abb8bd9"></a>

### [`00ae983c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae983c.md) → [`00ae9880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

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
      "definition_site": "00ae98bc",
      "incomplete_value": true,
      "site": "00ae98bc",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9878",
      "incomplete_value": true,
      "site": "00ae9878",
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
            "const:6e0:8"
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
      "definition_site": "00ae990c",
      "incomplete_value": true,
      "site": "00ae990c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae98c8",
      "incomplete_value": true,
      "site": "00ae98c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae9898",
      "incomplete_value": true,
      "site": "00ae9898",
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
      "definition_site": "00ae9854",
      "incomplete_value": true,
      "site": "00ae9854",
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
      "00ae9894",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae98a0",
      "READ",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae98bc",
      "WRITE",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9894",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae98a0",
      "READ",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae98bc",
      "WRITE",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae983c.md#insn-00ae9878) · [`00ae98c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae983c.md#insn-00ae98c4) · [`00ae98c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae983c.md#insn-00ae98c8)
- 新版 `00ae98bc`（命令位置の公開資料なし） · `00ae9908`（命令位置の公開資料なし） · `00ae990c`（命令位置の公開資料なし）

~~~diff
- 00ae9878 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9878 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9878 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6e0:8"]]
- 00ae9878 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae98bc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae98bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae98bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:720:8"]]
+ 00ae98bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9878 bytes bf821b39
+ 00ae98bc bytes bf821c39
- 00ae98c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae98c4 ["INT_ADD", "register:40f0:8", ["const:ae98c4:8", "const:4:8"]]
- 00ae98c4 ["CALLIND", null, ["register:0:8"]]
+ 00ae9908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9908 ["INT_ADD", "register:40f0:8", ["const:ae9908:8", "const:4:8"]]
+ 00ae9908 ["CALLIND", null, ["register:0:8"]]
- 00ae98c4 bytes 00013fd6
+ 00ae9908 bytes 00013fd6
- 00ae98c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00ae98c8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae98c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae990c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00ae990c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae990c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae98c8 bytes 9f6e03f9
+ 00ae990c bytes 9f8e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496ac5d46f54015b561199fd40d2eb07"></a>

### [`00ae98dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae98dc.md) → [`00ae9920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9960",
      "incomplete_value": true,
      "site": "00ae9960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae991c",
      "incomplete_value": true,
      "site": "00ae991c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae993c",
      "incomplete_value": true,
      "site": "00ae993c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae98f8",
      "incomplete_value": true,
      "site": "00ae98f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9944",
      "incomplete_value": false,
      "site": "00ae9958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9900",
      "incomplete_value": false,
      "site": "00ae9914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "00ae9934",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9944",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae9960",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9934",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9944",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae9960",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae98dc.md#insn-00ae9914) · [`00ae991c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae98dc.md#insn-00ae991c) · [`00ae98f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae98dc.md#insn-00ae98f0)
- 新版 `00ae9958`（命令位置の公開資料なし） · `00ae9960`（命令位置の公開資料なし） · `00ae9934`（命令位置の公開資料なし）

~~~diff
- 00ae9914 ["INT_ADD", "register:40f0:8", ["const:ae9914:8", "const:4:8"]]
- 00ae9914 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9958 ["INT_ADD", "register:40f0:8", ["const:ae9958:8", "const:4:8"]]
+ 00ae9958 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9914 bytes cbd10394
+ 00ae9958 bytes ced10394
- 00ae991c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00ae991c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00ae9960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae991c bytes 806e03f9
+ 00ae9960 bytes 808e03f9
- 00ae98f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00ae98f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00ae9934 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae98f0 bytes 816e43f9
+ 00ae9934 bytes 818e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb107fa610e9f75f11d36dc98da90ab8"></a>

### [`00ae994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae994c.md) → [`00ae9990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae99ac",
      "incomplete_value": false,
      "site": "00ae99b0",
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
      "definition_site": "00ae9968",
      "incomplete_value": false,
      "site": "00ae996c",
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
      "definition_site": "00ae99bc",
      "incomplete_value": true,
      "site": "00ae99c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9978",
      "incomplete_value": true,
      "site": "00ae9984",
      "value": [
        "LOAD",
        "8",
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
      "00ae99ac",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae99bc",
      "DATA",
      [
        "storage",
        "010a06e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae99ac",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae99bc",
      "DATA",
      [
        "storage",
        "010a0728",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae994c.md#insn-00ae996c) · [`00ae9968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae994c.md#insn-00ae9968) · [`00ae9974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae994c.md#insn-00ae9974)
- 新版 `00ae99b0`（命令位置の公開資料なし） · `00ae99ac`（命令位置の公開資料なし） · `00ae99b8`（命令位置の公開資料なし）

~~~diff
- 00ae996c ["INT_ADD", "register:40f0:8", ["const:ae996c:8", "const:4:8"]]
- 00ae996c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae99b0 ["INT_ADD", "register:40f0:8", ["const:ae99b0:8", "const:4:8"]]
+ 00ae99b0 ["CALL", null, ["callee:00bde180:8"]]
- 00ae996c bytes f1d10394
+ 00ae99b0 bytes f4d10394
- 00ae9968 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae9968 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9968 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9968 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae99ac ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae99ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae99ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae99ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9968 bytes 00501791
+ 00ae99ac bytes 001c1591
- 00ae9974 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00ae9974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae99b8 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00ae99b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae99b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae99b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9974 bytes 08a11b91
+ 00ae99b8 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-738a932c0184176377947b2790686046"></a>

### [`00ae9988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9988.md) → [`00ae99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9a0c",
      "incomplete_value": true,
      "site": "00ae9a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae99c8",
      "incomplete_value": true,
      "site": "00ae99c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00ae99e8",
      "incomplete_value": true,
      "site": "00ae99e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae99a4",
      "incomplete_value": true,
      "site": "00ae99a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae99a4"
      ],
      [
        "FALL_THROUGH",
        "00ae99e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae99e8",
      "incomplete_value": true,
      "site": "00ae9a0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae99a4",
      "incomplete_value": true,
      "site": "00ae99c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae99e0",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae99f0",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae9a0c",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae99e0",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae99f0",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae9a0c",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae99c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9988.md#insn-00ae99c8) · [`00ae999c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9988.md#insn-00ae999c) · [`00ae99ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9988.md#insn-00ae99ac)
- 新版 `00ae9a0c`（命令位置の公開資料なし） · `00ae99e0`（命令位置の公開資料なし） · `00ae99f0`（命令位置の公開資料なし）

~~~diff
- 00ae99c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00ae99c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00ae9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae99c8 bytes 806e03f9
+ 00ae9a0c bytes 808e03f9
- 00ae999c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00ae999c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae99e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00ae99e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae999c bytes 816e43f9
+ 00ae99e0 bytes 818e43f9
- 00ae99ac ["COPY", "tmp:0:8", ["const:248:8"]]
- 00ae99ac ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae99ac ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae99ac ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae99f0 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00ae99f0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae99f0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae99f0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae99ac bytes 63200991
+ 00ae99f0 bytes 63ec0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ed8c6d5623c26c569a80510a5d0e76"></a>

### [`00ae99f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae99f8.md) → [`00ae9a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae9a58",
      "incomplete_value": false,
      "site": "00ae9a5c",
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
      "definition_site": "00ae9a14",
      "incomplete_value": false,
      "site": "00ae9a18",
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
      "definition_site": "00ae9a68",
      "incomplete_value": true,
      "site": "00ae9a74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9a24",
      "incomplete_value": true,
      "site": "00ae9a30",
      "value": [
        "LOAD",
        "8",
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
      "00ae9a58",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae9a68",
      "DATA",
      [
        "storage",
        "010a0708",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae9a58",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae9a68",
      "DATA",
      [
        "storage",
        "010a0748",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae99f8.md#insn-00ae9a18) · [`00ae9a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae99f8.md#insn-00ae9a14) · [`00ae9a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae99f8.md#insn-00ae9a20)
- 新版 `00ae9a5c`（命令位置の公開資料なし） · `00ae9a58`（命令位置の公開資料なし） · `00ae9a64`（命令位置の公開資料なし）

~~~diff
- 00ae9a18 ["INT_ADD", "register:40f0:8", ["const:ae9a18:8", "const:4:8"]]
- 00ae9a18 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae9a5c ["INT_ADD", "register:40f0:8", ["const:ae9a5c:8", "const:4:8"]]
+ 00ae9a5c ["CALL", null, ["callee:00bde180:8"]]
- 00ae9a18 bytes c6d10394
+ 00ae9a5c bytes c9d10394
- 00ae9a14 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae9a14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9a14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9a14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a58 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae9a58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9a14 bytes 00fc1991
+ 00ae9a58 bytes 00c81791
- 00ae9a20 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00ae9a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a64 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00ae9a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9a20 bytes 08211c91
+ 00ae9a64 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46efa635eeacb7f2dee03dc58552846a"></a>

### [`00ae9a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a34.md) → [`00ae9a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

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
      "definition_site": "00ae9aa4",
      "incomplete_value": true,
      "site": "00ae9aa4",
      "value": [
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
            "const:710:8"
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
      "definition_site": "00ae9a8c",
      "incomplete_value": true,
      "site": "00ae9a8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9a98",
      "incomplete_value": false,
      "site": "00ae9a9c",
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
    "old": {
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
      "00ae9a88",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9a98",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9aa4",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9a88",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9a98",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9aa4",
      "WRITE",
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

- 旧版 [`00ae9a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a34.md#insn-00ae9a58) · [`00ae9a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a34.md#insn-00ae9a60) · [`00ae9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a34.md#insn-00ae9a44)
- 新版 `00ae9a9c`（命令位置の公開資料なし） · `00ae9aa4`（命令位置の公開資料なし） · `00ae9a88`（命令位置の公開資料なし）

~~~diff
- 00ae9a58 ["INT_ADD", "register:40f0:8", ["const:ae9a58:8", "const:4:8"]]
- 00ae9a58 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9a9c ["INT_ADD", "register:40f0:8", ["const:ae9a9c:8", "const:4:8"]]
+ 00ae9a9c ["CALL", null, ["callee:00bde090:8"]]
- 00ae9a58 bytes 7ad10394
+ 00ae9a9c bytes 7dd10394
- 00ae9a60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9aa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9aa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9a60 bytes 608a03f9
+ 00ae9aa4 bytes 60aa03f9
- 00ae9a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9a44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9a88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9a44 bytes 688a43f9
+ 00ae9a88 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-026b9b5825222853511f023cff760d29"></a>

### [`00ae9a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a74.md) → [`00ae9ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae9ae4",
      "incomplete_value": true,
      "site": "00ae9ae4",
      "value": [
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
    "old": {
      "definition_site": "00ae9aa0",
      "incomplete_value": true,
      "site": "00ae9aa0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9acc",
      "incomplete_value": true,
      "site": "00ae9acc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a88",
      "incomplete_value": true,
      "site": "00ae9a88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9ad4",
      "incomplete_value": false,
      "site": "00ae9adc",
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
    "old": {
      "definition_site": "00ae9a90",
      "incomplete_value": false,
      "site": "00ae9a98",
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
      "00ae9ac8",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ad4",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9ae4",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9ac8",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ad4",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9ae4",
      "WRITE",
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

- 旧版 [`00ae9a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a74.md#insn-00ae9a98) · [`00ae9aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a74.md#insn-00ae9aa0) · [`00ae9a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9a74.md#insn-00ae9a84)
- 新版 `00ae9adc`（命令位置の公開資料なし） · `00ae9ae4`（命令位置の公開資料なし） · `00ae9ac8`（命令位置の公開資料なし）

~~~diff
- 00ae9a98 ["INT_ADD", "register:40f0:8", ["const:ae9a98:8", "const:4:8"]]
- 00ae9a98 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9adc ["INT_ADD", "register:40f0:8", ["const:ae9adc:8", "const:4:8"]]
+ 00ae9adc ["CALL", null, ["callee:00bde090:8"]]
- 00ae9a98 bytes 6ad10394
+ 00ae9adc bytes 6dd10394
- 00ae9aa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9aa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9ae4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9aa0 bytes 608a03f9
+ 00ae9ae4 bytes 60aa03f9
- 00ae9a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9a84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9ac8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9ac8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9a84 bytes 688a43f9
+ 00ae9ac8 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09e2d3676164eed78a8f3fd344e6dcce"></a>

### [`00ae9ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ab4.md) → [`00ae9af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9af8.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ae4",
      "incomplete_value": true,
      "site": "00ae9ae4",
      "value": [
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
      "definition_site": "00ae9ac8",
      "incomplete_value": true,
      "site": "00ae9ac8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9b18",
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
            "const:5fe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ad4",
      "incomplete_value": false,
      "site": "00ae9adc",
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
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b18",
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
  ],
  "added": [
    [
      "00ae9b08",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b18",
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
        "010a0750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ab4.md#insn-00ae9adc) · [`00ae9ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ab4.md#insn-00ae9ae4) · [`00ae9ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ab4.md#insn-00ae9ac4)
- 新版 `00ae9b20`（命令位置の公開資料なし） · `00ae9b28`（命令位置の公開資料なし） · `00ae9b08`（命令位置の公開資料なし）

~~~diff
- 00ae9adc ["INT_ADD", "register:40f0:8", ["const:ae9adc:8", "const:4:8"]]
- 00ae9adc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9b20 ["INT_ADD", "register:40f0:8", ["const:ae9b20:8", "const:4:8"]]
+ 00ae9b20 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9adc bytes 59d10394
+ 00ae9b20 bytes 5cd10394
- 00ae9ae4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9ae4 bytes 608a03f9
+ 00ae9b28 bytes 60aa03f9
- 00ae9ac4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9ac4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9ac4 bytes 688a43f9
+ 00ae9b08 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a0507a467b817a4f03e59695f4324e"></a>

### [`00ae9af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9af8.md) → [`00ae9b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9b6c",
      "incomplete_value": true,
      "site": "00ae9b6c",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9b50",
      "incomplete_value": true,
      "site": "00ae9b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9b58",
      "incomplete_value": false,
      "site": "00ae9b64",
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
    "old": {
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
      "00ae9b4c",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b58",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9b6c",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9b4c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9b58",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9b6c",
      "WRITE",
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

- 旧版 [`00ae9b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9af8.md#insn-00ae9b20) · [`00ae9b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9af8.md#insn-00ae9b28) · [`00ae9b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9af8.md#insn-00ae9b08)
- 新版 `00ae9b64`（命令位置の公開資料なし） · `00ae9b6c`（命令位置の公開資料なし） · `00ae9b4c`（命令位置の公開資料なし）

~~~diff
- 00ae9b20 ["INT_ADD", "register:40f0:8", ["const:ae9b20:8", "const:4:8"]]
- 00ae9b20 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9b64 ["INT_ADD", "register:40f0:8", ["const:ae9b64:8", "const:4:8"]]
+ 00ae9b64 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9b20 bytes 48d10394
+ 00ae9b64 bytes 4bd10394
- 00ae9b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9b28 bytes 608a03f9
+ 00ae9b6c bytes 60aa03f9
- 00ae9b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00ae9b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00ae9b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9b08 bytes 688a43f9
+ 00ae9b4c bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74d2d0382c1e4322fc98a1c5eb9d7de"></a>

### [`00ae9b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9b48.md) → [`00ae9b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae9c14",
      "incomplete_value": true,
      "site": "00ae9c14",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9bc0",
      "incomplete_value": true,
      "site": "00ae9bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ae9ba0",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9bc0",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c14",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9ba0",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9bc0",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c14",
      "WRITE",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9b48.md#insn-00ae9b88) · [`00ae9bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9b48.md#insn-00ae9bd0) · [`00ae9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9b48.md#insn-00ae9b5c)
- 新版 `00ae9bcc`（命令位置の公開資料なし） · `00ae9c14`（命令位置の公開資料なし） · `00ae9ba0`（命令位置の公開資料なし）

~~~diff
- 00ae9b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9b88 ["INT_ADD", "register:40f0:8", ["const:ae9b88:8", "const:4:8"]]
- 00ae9b88 ["CALLIND", null, ["register:0:8"]]
+ 00ae9bcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9bcc ["INT_ADD", "register:40f0:8", ["const:ae9bcc:8", "const:4:8"]]
+ 00ae9bcc ["CALLIND", null, ["register:0:8"]]
- 00ae9b88 bytes 00013fd6
+ 00ae9bcc bytes 00013fd6
- 00ae9bd0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9bd0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:718:8"]]
- 00ae9bd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9c14 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9c14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:758:8"]]
+ 00ae9c14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9bd0 bytes a0621c39
+ 00ae9c14 bytes a0621d39
- 00ae9b5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:718:8"]]
- 00ae9b5c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae9b5c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae9ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:758:8"]]
+ 00ae9ba0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9ba0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae9b5c bytes a8625c39
+ 00ae9ba0 bytes a8625d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab02b76b85cc689529ed6059cb414b98"></a>

### [`00ae9be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9be4.md) → [`00ae9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae9c64",
      "incomplete_value": true,
      "site": "00ae9c64",
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
    "old": {
      "definition_site": "00ae9c20",
      "incomplete_value": true,
      "site": "00ae9c20",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9cb4",
      "incomplete_value": true,
      "site": "00ae9cb4",
      "value": [
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
    "old": {
      "definition_site": "00ae9c70",
      "incomplete_value": true,
      "site": "00ae9c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00ae9c40",
      "incomplete_value": true,
      "site": "00ae9c40",
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
      "definition_site": "00ae9bfc",
      "incomplete_value": true,
      "site": "00ae9bfc",
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
      "00ae9c3c",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c48",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9c64",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9c3c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9c48",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9c64",
      "WRITE",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9be4.md#insn-00ae9c20) · [`00ae9c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9be4.md#insn-00ae9c6c) · [`00ae9c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9be4.md#insn-00ae9c70)
- 新版 `00ae9c64`（命令位置の公開資料なし） · `00ae9cb0`（命令位置の公開資料なし） · `00ae9cb4`（命令位置の公開資料なし）

~~~diff
- 00ae9c20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9c20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9c20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:718:8"]]
- 00ae9c20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae9c64 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae9c64 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae9c64 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:758:8"]]
+ 00ae9c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9c20 bytes bf621c39
+ 00ae9c64 bytes bf621d39
- 00ae9c6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9c6c ["INT_ADD", "register:40f0:8", ["const:ae9c6c:8", "const:4:8"]]
- 00ae9c6c ["CALLIND", null, ["register:0:8"]]
+ 00ae9cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9cb0 ["INT_ADD", "register:40f0:8", ["const:ae9cb0:8", "const:4:8"]]
+ 00ae9cb0 ["CALLIND", null, ["register:0:8"]]
- 00ae9c6c bytes 00013fd6
+ 00ae9cb0 bytes 00013fd6
- 00ae9c70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00ae9c70 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae9c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae9cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00ae9cb4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae9cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae9c70 bytes 9f8a03f9
+ 00ae9cb4 bytes 9faa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fefb271dfda919313b9c9bcaa74ca88"></a>

### [`00ae9c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md) → [`00ae9cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9d08",
      "incomplete_value": true,
      "site": "00ae9d08",
      "value": [
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
    "old": {
      "definition_site": "00ae9cc4",
      "incomplete_value": true,
      "site": "00ae9cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00ae9ce4",
      "incomplete_value": true,
      "site": "00ae9ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ca0",
      "incomplete_value": true,
      "site": "00ae9ca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9cec",
      "incomplete_value": false,
      "site": "00ae9d00",
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
    "old": {
      "definition_site": "00ae9ca8",
      "incomplete_value": false,
      "site": "00ae9cbc",
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
      "00ae9cdc",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9cec",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9d08",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9cdc",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9cec",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9d08",
      "WRITE",
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

- 旧版 [`00ae9cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md#insn-00ae9cbc) · [`00ae9cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md#insn-00ae9cc4) · [`00ae9c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md#insn-00ae9c98)
- 新版 `00ae9d00`（命令位置の公開資料なし） · `00ae9d08`（命令位置の公開資料なし） · `00ae9cdc`（命令位置の公開資料なし）

~~~diff
- 00ae9cbc ["INT_ADD", "register:40f0:8", ["const:ae9cbc:8", "const:4:8"]]
- 00ae9cbc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9d00 ["INT_ADD", "register:40f0:8", ["const:ae9d00:8", "const:4:8"]]
+ 00ae9d00 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9cbc bytes e1d00394
+ 00ae9d00 bytes e4d00394
- 00ae9cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00ae9cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9d08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00ae9d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9cc4 bytes 808a03f9
+ 00ae9d08 bytes 80aa03f9
- 00ae9c98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00ae9c98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9cdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00ae9cdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9c98 bytes 818a43f9
+ 00ae9cdc bytes 81aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6de4af2e05218b9bdb7c95f34587d57b"></a>

### [`00ae9cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9cf4.md) → [`00ae9d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d38.md) _ZN8firebase4util4date11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae9d54",
      "incomplete_value": false,
      "site": "00ae9d58",
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
      "definition_site": "00ae9d10",
      "incomplete_value": false,
      "site": "00ae9d14",
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
      "definition_site": "00ae9d64",
      "incomplete_value": true,
      "site": "00ae9d70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9d20",
      "incomplete_value": true,
      "site": "00ae9d2c",
      "value": [
        "LOAD",
        "8",
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
      "00ae9d54",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae9d64",
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
      "00ae9d54",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae9d64",
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

- 旧版 [`00ae9d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9cf4.md#insn-00ae9d14) · [`00ae9d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9cf4.md#insn-00ae9d10) · [`00ae9d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9cf4.md#insn-00ae9d1c)
- 新版 `00ae9d58`（命令位置の公開資料なし） · `00ae9d54`（命令位置の公開資料なし） · `00ae9d60`（命令位置の公開資料なし）

~~~diff
- 00ae9d14 ["INT_ADD", "register:40f0:8", ["const:ae9d14:8", "const:4:8"]]
- 00ae9d14 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae9d58 ["INT_ADD", "register:40f0:8", ["const:ae9d58:8", "const:4:8"]]
+ 00ae9d58 ["CALL", null, ["callee:00bde180:8"]]
- 00ae9d14 bytes 07d10394
+ 00ae9d58 bytes 0ad10394
- 00ae9d10 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae9d10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9d10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9d10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9d54 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae9d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9d10 bytes 00501791
+ 00ae9d54 bytes 001c1591
- 00ae9d1c ["COPY", "tmp:0:8", ["const:720:8"]]
- 00ae9d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9d60 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00ae9d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9d1c bytes 08811c91
+ 00ae9d60 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a715c5af61cfa746d7b02a38d3fc4883"></a>

### [`00ae9d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9d30.md) → [`00ae9d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9db4",
      "incomplete_value": true,
      "site": "00ae9db4",
      "value": [
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
    "old": {
      "definition_site": "00ae9d70",
      "incomplete_value": true,
      "site": "00ae9d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00ae9d90",
      "incomplete_value": true,
      "site": "00ae9d90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d4c",
      "incomplete_value": true,
      "site": "00ae9d4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae9d98",
      "incomplete_value": false,
      "site": "00ae9dac",
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
    "old": {
      "definition_site": "00ae9d54",
      "incomplete_value": false,
      "site": "00ae9d68",
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
      "00ae9d88",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9d98",
      "PARAM",
      [
        "storage",
        "0029868b",
        null,
        "string"
      ]
    ],
    [
      "00ae9db4",
      "WRITE",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9d88",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9d98",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00ae9db4",
      "WRITE",
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

- 旧版 [`00ae9d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9d30.md#insn-00ae9d68) · [`00ae9d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9d30.md#insn-00ae9d70) · [`00ae9d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9d30.md#insn-00ae9d44)
- 新版 `00ae9dac`（命令位置の公開資料なし） · `00ae9db4`（命令位置の公開資料なし） · `00ae9d88`（命令位置の公開資料なし）

~~~diff
- 00ae9d68 ["INT_ADD", "register:40f0:8", ["const:ae9d68:8", "const:4:8"]]
- 00ae9d68 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9dac ["INT_ADD", "register:40f0:8", ["const:ae9dac:8", "const:4:8"]]
+ 00ae9dac ["CALL", null, ["callee:00bde090:8"]]
- 00ae9d68 bytes b6d00394
+ 00ae9dac bytes b9d00394
- 00ae9d70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00ae9d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9db4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00ae9db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9d70 bytes 808a03f9
+ 00ae9db4 bytes 80aa03f9
- 00ae9d44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00ae9d44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00ae9d88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9d44 bytes 818a43f9
+ 00ae9d88 bytes 81aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9fb9a5c5acdf1cf9119450b2a35cba5"></a>

### [`00ae9da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9da0.md) → [`00ae9de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae9e00",
      "incomplete_value": false,
      "site": "00ae9e04",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00ae9e10",
      "incomplete_value": true,
      "site": "00ae9e1c",
      "value": [
        "LOAD",
        "8",
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
      "00ae9e00",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae9e10",
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
      "00ae9e00",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae9e10",
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

- 旧版 [`00ae9dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9da0.md#insn-00ae9dc0) · [`00ae9dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9da0.md#insn-00ae9dbc) · [`00ae9dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9da0.md#insn-00ae9dc8)
- 新版 `00ae9e04`（命令位置の公開資料なし） · `00ae9e00`（命令位置の公開資料なし） · `00ae9e0c`（命令位置の公開資料なし）

~~~diff
- 00ae9dc0 ["INT_ADD", "register:40f0:8", ["const:ae9dc0:8", "const:4:8"]]
- 00ae9dc0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae9e04 ["INT_ADD", "register:40f0:8", ["const:ae9e04:8", "const:4:8"]]
+ 00ae9e04 ["CALL", null, ["callee:00bde180:8"]]
- 00ae9dc0 bytes dcd00394
+ 00ae9e04 bytes dfd00394
- 00ae9dbc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae9dbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9dbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9dbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9e00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae9e00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9e00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9e00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9dbc bytes 00fc1991
+ 00ae9e00 bytes 00c81791
- 00ae9dc8 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00ae9dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9e0c ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00ae9e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9dc8 bytes 08e11c91
+ 00ae9e0c bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95aaebf95a60b80b5af7df88fb8c87f1"></a>

### [`00ae9ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ddc.md) → [`00ae9e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00ae9e4c",
      "incomplete_value": true,
      "site": "00ae9e4c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9e34",
      "incomplete_value": true,
      "site": "00ae9e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9e40",
      "incomplete_value": false,
      "site": "00ae9e44",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ae9e30",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e40",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9e4c",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9e30",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e40",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00ae9e4c",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ddc.md#insn-00ae9e00) · [`00ae9e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ddc.md#insn-00ae9e08) · [`00ae9dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ddc.md#insn-00ae9dec)
- 新版 `00ae9e44`（命令位置の公開資料なし） · `00ae9e4c`（命令位置の公開資料なし） · `00ae9e30`（命令位置の公開資料なし）

~~~diff
- 00ae9e00 ["INT_ADD", "register:40f0:8", ["const:ae9e00:8", "const:4:8"]]
- 00ae9e00 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9e44 ["INT_ADD", "register:40f0:8", ["const:ae9e44:8", "const:4:8"]]
+ 00ae9e44 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9e00 bytes 90d00394
+ 00ae9e44 bytes 93d00394
- 00ae9e08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9e4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e08 bytes 60a203f9
+ 00ae9e4c bytes 60c203f9
- 00ae9dec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9dec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9e30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9e30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9dec bytes 68a243f9
+ 00ae9e30 bytes 68c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16314810dce191cd70eaeb5b2c2b6721"></a>

### [`00ae9e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e1c.md) → [`00ae9e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00ae9e8c",
      "incomplete_value": true,
      "site": "00ae9e8c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9e74",
      "incomplete_value": true,
      "site": "00ae9e74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9e7c",
      "incomplete_value": false,
      "site": "00ae9e84",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ae9e70",
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
      "00ae9e8c",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9e70",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9e7c",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00ae9e8c",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e1c.md#insn-00ae9e40) · [`00ae9e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e1c.md#insn-00ae9e48) · [`00ae9e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e1c.md#insn-00ae9e2c)
- 新版 `00ae9e84`（命令位置の公開資料なし） · `00ae9e8c`（命令位置の公開資料なし） · `00ae9e70`（命令位置の公開資料なし）

~~~diff
- 00ae9e40 ["INT_ADD", "register:40f0:8", ["const:ae9e40:8", "const:4:8"]]
- 00ae9e40 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9e84 ["INT_ADD", "register:40f0:8", ["const:ae9e84:8", "const:4:8"]]
+ 00ae9e84 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9e40 bytes 80d00394
+ 00ae9e84 bytes 83d00394
- 00ae9e48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e48 bytes 60a203f9
+ 00ae9e8c bytes 60c203f9
- 00ae9e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9e2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9e70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9e70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9e2c bytes 68a243f9
+ 00ae9e70 bytes 68c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d489013a879a8f52dc697504513d8827"></a>

### [`00ae9e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e5c.md) → [`00ae9ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ea0.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e8c",
      "incomplete_value": true,
      "site": "00ae9e8c",
      "value": [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9ec0",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e7c",
      "incomplete_value": false,
      "site": "00ae9e84",
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
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ec0",
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
  ],
  "added": [
    [
      "00ae9eb0",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ec0",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00ae9ed0",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e5c.md#insn-00ae9e84) · [`00ae9e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e5c.md#insn-00ae9e8c) · [`00ae9e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9e5c.md#insn-00ae9e6c)
- 新版 `00ae9ec8`（命令位置の公開資料なし） · `00ae9ed0`（命令位置の公開資料なし） · `00ae9eb0`（命令位置の公開資料なし）

~~~diff
- 00ae9e84 ["INT_ADD", "register:40f0:8", ["const:ae9e84:8", "const:4:8"]]
- 00ae9e84 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9ec8 ["INT_ADD", "register:40f0:8", ["const:ae9ec8:8", "const:4:8"]]
+ 00ae9ec8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae9e84 bytes 6fd00394
+ 00ae9ec8 bytes 72d00394
- 00ae9e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e8c bytes 60a203f9
+ 00ae9ed0 bytes 60c203f9
- 00ae9e6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9e6c bytes 68a243f9
+ 00ae9eb0 bytes 68c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da20a312a5cae3b47e1ec52770a1dee5"></a>

### [`00ae9ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ea0.md) → [`00ae9ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9f14",
      "incomplete_value": true,
      "site": "00ae9f14",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9ef8",
      "incomplete_value": true,
      "site": "00ae9ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9f00",
      "incomplete_value": false,
      "site": "00ae9f0c",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ae9ef4",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9f00",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00ae9f14",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9ef4",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9f00",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00ae9f14",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ea0.md#insn-00ae9ec8) · [`00ae9ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ea0.md#insn-00ae9ed0) · [`00ae9eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ea0.md#insn-00ae9eb0)
- 新版 `00ae9f0c`（命令位置の公開資料なし） · `00ae9f14`（命令位置の公開資料なし） · `00ae9ef4`（命令位置の公開資料なし）

~~~diff
- 00ae9ec8 ["INT_ADD", "register:40f0:8", ["const:ae9ec8:8", "const:4:8"]]
- 00ae9ec8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae9f0c ["INT_ADD", "register:40f0:8", ["const:ae9f0c:8", "const:4:8"]]
+ 00ae9f0c ["CALL", null, ["callee:00bde090:8"]]
- 00ae9ec8 bytes 5ed00394
+ 00ae9f0c bytes 61d00394
- 00ae9ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9ed0 bytes 60a203f9
+ 00ae9f14 bytes 60c203f9
- 00ae9eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00ae9eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00ae9ef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9eb0 bytes 68a243f9
+ 00ae9ef4 bytes 68c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d21ead9a0637e59fa5cd9503eb8c39ec"></a>

### [`00ae9ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ef0.md) → [`00ae9f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9f34.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae9fbc",
      "incomplete_value": true,
      "site": "00ae9fbc",
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
      "definition_site": "00ae9f78",
      "incomplete_value": true,
      "site": "00ae9f78",
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
      "definition_site": "00ae9f68",
      "incomplete_value": true,
      "site": "00ae9f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00ae9f48",
      "READ",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9f68",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9fbc",
      "WRITE",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9f48",
      "READ",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9f68",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9fbc",
      "WRITE",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ef0.md#insn-00ae9f30) · [`00ae9f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ef0.md#insn-00ae9f78) · [`00ae9f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9ef0.md#insn-00ae9f04)
- 新版 `00ae9f74`（命令位置の公開資料なし） · `00ae9fbc`（命令位置の公開資料なし） · `00ae9f48`（命令位置の公開資料なし）

~~~diff
- 00ae9f30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9f30 ["INT_ADD", "register:40f0:8", ["const:ae9f30:8", "const:4:8"]]
- 00ae9f30 ["CALLIND", null, ["register:0:8"]]
+ 00ae9f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9f74 ["INT_ADD", "register:40f0:8", ["const:ae9f74:8", "const:4:8"]]
+ 00ae9f74 ["CALLIND", null, ["register:0:8"]]
- 00ae9f30 bytes 00013fd6
+ 00ae9f74 bytes 00013fd6
- 00ae9f78 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9f78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
- 00ae9f78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9fbc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9fbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
+ 00ae9fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9f78 bytes a0221d39
+ 00ae9fbc bytes a0221e39
- 00ae9f04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:748:8"]]
- 00ae9f04 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae9f04 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae9f48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00ae9f48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9f48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae9f04 bytes a8225d39
+ 00ae9f48 bytes a8225e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194c87371daf661dafe5e91c55302a21"></a>

### [`00ae9f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9f8c.md) → [`00ae9fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aea00c",
      "incomplete_value": true,
      "site": "00aea00c",
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
      "definition_site": "00ae9fc8",
      "incomplete_value": true,
      "site": "00ae9fc8",
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
      "definition_site": "00aea05c",
      "incomplete_value": true,
      "site": "00aea05c",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9fe8",
      "incomplete_value": true,
      "site": "00ae9fe8",
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
      "definition_site": "00ae9fa4",
      "incomplete_value": true,
      "site": "00ae9fa4",
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
      "00ae9fe4",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ff0",
      "READ",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea00c",
      "WRITE",
      [
        "storage",
        "010a0748",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9fe4",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9ff0",
      "READ",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea00c",
      "WRITE",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9f8c.md#insn-00ae9fc8) · [`00aea014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9f8c.md#insn-00aea014) · [`00aea018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9f8c.md#insn-00aea018)
- 新版 `00aea00c`（命令位置の公開資料なし） · `00aea058`（命令位置の公開資料なし） · `00aea05c`（命令位置の公開資料なし）

~~~diff
- 00ae9fc8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9fc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9fc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
- 00ae9fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aea00c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aea00c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aea00c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
+ 00aea00c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9fc8 bytes bf221d39
+ 00aea00c bytes bf221e39
- 00aea014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea014 ["INT_ADD", "register:40f0:8", ["const:aea014:8", "const:4:8"]]
- 00aea014 ["CALLIND", null, ["register:0:8"]]
+ 00aea058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea058 ["INT_ADD", "register:40f0:8", ["const:aea058:8", "const:4:8"]]
+ 00aea058 ["CALLIND", null, ["register:0:8"]]
- 00aea014 bytes 00013fd6
+ 00aea058 bytes 00013fd6
- 00aea018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00aea018 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aea05c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00aea05c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aea05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea018 bytes 9fa203f9
+ 00aea05c bytes 9fc203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1161d93074c0a0b25d7fbbc5590effc3"></a>

### [`00aea02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea02c.md) → [`00aea070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea0b0",
      "incomplete_value": true,
      "site": "00aea0b0",
      "value": [
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
      "definition_site": "00aea06c",
      "incomplete_value": true,
      "site": "00aea06c",
      "value": [
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
      "definition_site": "00aea08c",
      "incomplete_value": true,
      "site": "00aea08c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea048",
      "incomplete_value": true,
      "site": "00aea048",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00aea094",
      "incomplete_value": false,
      "site": "00aea0a8",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea050",
      "incomplete_value": false,
      "site": "00aea064",
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
      "00aea084",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea094",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00aea0b0",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea084",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea094",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00aea0b0",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea02c.md#insn-00aea064) · [`00aea06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea02c.md#insn-00aea06c) · [`00aea040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea02c.md#insn-00aea040)
- 新版 `00aea0a8`（命令位置の公開資料なし） · `00aea0b0`（命令位置の公開資料なし） · `00aea084`（命令位置の公開資料なし）

~~~diff
- 00aea064 ["INT_ADD", "register:40f0:8", ["const:aea064:8", "const:4:8"]]
- 00aea064 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea0a8 ["INT_ADD", "register:40f0:8", ["const:aea0a8:8", "const:4:8"]]
+ 00aea0a8 ["CALL", null, ["callee:00bde090:8"]]
- 00aea064 bytes f7cf0394
+ 00aea0a8 bytes facf0394
- 00aea06c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00aea06c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea0b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00aea0b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea06c bytes 80a203f9
+ 00aea0b0 bytes 80c203f9
- 00aea040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00aea040 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00aea084 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea040 bytes 81a243f9
+ 00aea084 bytes 81c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f122ffebd7e87ff4040d7af35af3b39e"></a>

### [`00aea09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea09c.md) → [`00aea0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3c0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde410.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aea0fc",
      "incomplete_value": false,
      "site": "00aea100",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea10c",
      "incomplete_value": true,
      "site": "00aea118",
      "value": [
        "LOAD",
        "8",
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
      "00aea0fc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea10c",
      "DATA",
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
      "00aea0fc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea10c",
      "DATA",
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

- 旧版 [`00aea0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea09c.md#insn-00aea0bc) · [`00aea0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea09c.md#insn-00aea0b8) · [`00aea0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea09c.md#insn-00aea0c4)
- 新版 `00aea100`（命令位置の公開資料なし） · `00aea0fc`（命令位置の公開資料なし） · `00aea108`（命令位置の公開資料なし）

~~~diff
- 00aea0bc ["INT_ADD", "register:40f0:8", ["const:aea0bc:8", "const:4:8"]]
- 00aea0bc ["CALL", null, ["callee:00bde180:8"]]
+ 00aea100 ["INT_ADD", "register:40f0:8", ["const:aea100:8", "const:4:8"]]
+ 00aea100 ["CALL", null, ["callee:00bde180:8"]]
- 00aea0bc bytes 1dd00394
+ 00aea100 bytes 20d00394
- 00aea0b8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aea0b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea0b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea0b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea0fc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aea0fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea0fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea0fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea0b8 bytes 00501791
+ 00aea0fc bytes 001c1591
- 00aea0c4 ["COPY", "tmp:0:8", ["const:750:8"]]
- 00aea0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea108 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00aea108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea0c4 bytes 08411d91
+ 00aea108 bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03876186a9f97b35f52efb6dd9a09acf"></a>

### [`00aea0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea0d8.md) → [`00aea11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea15c",
      "incomplete_value": true,
      "site": "00aea15c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea138",
      "incomplete_value": true,
      "site": "00aea138",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea140",
      "incomplete_value": false,
      "site": "00aea154",
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
            "const:c5:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea130",
      "READ",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea140",
      "PARAM",
      [
        "storage",
        "002a702b",
        null,
        "string"
      ]
    ],
    [
      "00aea15c",
      "WRITE",
      [
        "storage",
        "010a0740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea130",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea140",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00aea15c",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea0d8.md#insn-00aea110) · [`00aea118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea0d8.md#insn-00aea118) · [`00aea0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea0d8.md#insn-00aea0ec)
- 新版 `00aea154`（命令位置の公開資料なし） · `00aea15c`（命令位置の公開資料なし） · `00aea130`（命令位置の公開資料なし）

~~~diff
- 00aea110 ["INT_ADD", "register:40f0:8", ["const:aea110:8", "const:4:8"]]
- 00aea110 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea154 ["INT_ADD", "register:40f0:8", ["const:aea154:8", "const:4:8"]]
+ 00aea154 ["CALL", null, ["callee:00bde090:8"]]
- 00aea110 bytes cccf0394
+ 00aea154 bytes cfcf0394
- 00aea118 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00aea118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea15c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00aea15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea118 bytes 80a203f9
+ 00aea15c bytes 80c203f9
- 00aea0ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00aea0ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00aea130 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea0ec bytes 81a243f9
+ 00aea130 bytes 81c243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c2a16a516a836b6e9ad6aec6aa2c026"></a>

### [`00aea148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea148.md) → [`00aea18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aea1a8",
      "incomplete_value": false,
      "site": "00aea1ac",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea1b8",
      "incomplete_value": true,
      "site": "00aea1c4",
      "value": [
        "LOAD",
        "8",
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
      "00aea1a8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea1b8",
      "DATA",
      [
        "storage",
        "010a0760",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea1a8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea1b8",
      "DATA",
      [
        "storage",
        "010a07a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea148.md#insn-00aea168) · [`00aea164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea148.md#insn-00aea164) · [`00aea170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea148.md#insn-00aea170)
- 新版 `00aea1ac`（命令位置の公開資料なし） · `00aea1a8`（命令位置の公開資料なし） · `00aea1b4`（命令位置の公開資料なし）

~~~diff
- 00aea168 ["INT_ADD", "register:40f0:8", ["const:aea168:8", "const:4:8"]]
- 00aea168 ["CALL", null, ["callee:00bde180:8"]]
+ 00aea1ac ["INT_ADD", "register:40f0:8", ["const:aea1ac:8", "const:4:8"]]
+ 00aea1ac ["CALL", null, ["callee:00bde180:8"]]
- 00aea168 bytes f2cf0394
+ 00aea1ac bytes f5cf0394
- 00aea164 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aea164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea1a8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aea1a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea1a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea1a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea164 bytes 00fc1991
+ 00aea1a8 bytes 00c81791
- 00aea170 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00aea170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea1b4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00aea1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea170 bytes 08811d91
+ 00aea1b4 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47e1fb77525943095969b32e0b64acc6"></a>

### [`00aea184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md) → [`00aea1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00aea1f4",
      "incomplete_value": true,
      "site": "00aea1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
            "const:768:8"
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
      "definition_site": "00aea1dc",
      "incomplete_value": true,
      "site": "00aea1dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea198"
      ],
      [
        "FALL_THROUGH",
        "00aea1dc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea1dc",
      "incomplete_value": true,
      "site": "00aea1f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea1d8",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1f4",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea1d8",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea1f4",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md#insn-00aea1b0) · [`00aea194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md#insn-00aea194) · [`00aea1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea184.md#insn-00aea1a8)
- 新版 `00aea1f4`（命令位置の公開資料なし） · `00aea1d8`（命令位置の公開資料なし） · `00aea1ec`（命令位置の公開資料なし）

~~~diff
- 00aea1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea1f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea1b0 bytes 60b603f9
+ 00aea1f4 bytes 60d603f9
- 00aea194 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea194 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea1d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea1d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea194 bytes 68b643f9
+ 00aea1d8 bytes 68d643f9
- 00aea1a8 ["INT_ADD", "register:40f0:8", ["const:aea1a8:8", "const:4:8"]]
- 00aea1a8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea1ec ["INT_ADD", "register:40f0:8", ["const:aea1ec:8", "const:4:8"]]
+ 00aea1ec ["CALL", null, ["callee:00bde090:8"]]
- 00aea1a8 bytes a6cf0394
+ 00aea1ec bytes a9cf0394
~~~


<a id="compare-0ec2c88f7831274f9ba286b774a456c1"></a>

### [`00aea1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md) → [`00aea208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea21c",
      "incomplete_value": true,
      "site": "00aea21c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea1d8"
      ],
      [
        "FALL_THROUGH",
        "00aea21c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea21c",
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
      "00aea218",
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
  ],
  "added": [
    [
      "00aea218",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea234",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md#insn-00aea1f0) · [`00aea1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md#insn-00aea1d4) · [`00aea1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea1c4.md#insn-00aea1e8)
- 新版 `00aea234`（命令位置の公開資料なし） · `00aea218`（命令位置の公開資料なし） · `00aea22c`（命令位置の公開資料なし）

~~~diff
- 00aea1f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea1f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea1f0 bytes 60b603f9
+ 00aea234 bytes 60d603f9
- 00aea1d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea1d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea218 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea218 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea1d4 bytes 68b643f9
+ 00aea218 bytes 68d643f9
- 00aea1e8 ["INT_ADD", "register:40f0:8", ["const:aea1e8:8", "const:4:8"]]
- 00aea1e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea22c ["INT_ADD", "register:40f0:8", ["const:aea22c:8", "const:4:8"]]
+ 00aea22c ["CALL", null, ["callee:00bde090:8"]]
- 00aea1e8 bytes 96cf0394
+ 00aea22c bytes 99cf0394
~~~


<a id="compare-90813a36e2bdaeaa9cff5cf7cb14bb56"></a>

### [`00aea204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea204.md) → [`00aea248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea218"
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
  ],
  "added": [
    [
      "00aea258",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea278",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea204.md#insn-00aea234) · [`00aea214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea204.md#insn-00aea214) · [`00aea22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea204.md#insn-00aea22c)
- 新版 `00aea278`（命令位置の公開資料なし） · `00aea258`（命令位置の公開資料なし） · `00aea270`（命令位置の公開資料なし）

~~~diff
- 00aea234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea234 bytes 60b603f9
+ 00aea278 bytes 60d603f9
- 00aea214 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea214 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea214 bytes 68b643f9
+ 00aea258 bytes 68d643f9
- 00aea22c ["INT_ADD", "register:40f0:8", ["const:aea22c:8", "const:4:8"]]
- 00aea22c ["CALL", null, ["callee:00bde090:8"]]
+ 00aea270 ["INT_ADD", "register:40f0:8", ["const:aea270:8", "const:4:8"]]
+ 00aea270 ["CALL", null, ["callee:00bde090:8"]]
- 00aea22c bytes 85cf0394
+ 00aea270 bytes 88cf0394
~~~


<a id="compare-267608a6ff8b6ebe7cd6e5a9fd737ad2"></a>

### [`00aea248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea248.md) → [`00aea28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea2bc",
      "incomplete_value": true,
      "site": "00aea2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea2a0",
      "incomplete_value": true,
      "site": "00aea2a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea25c"
      ],
      [
        "FALL_THROUGH",
        "00aea2a0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea2a0",
      "incomplete_value": true,
      "site": "00aea2bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea29c",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea2bc",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea29c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea2bc",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea248.md#insn-00aea278) · [`00aea258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea248.md#insn-00aea258) · [`00aea270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea248.md#insn-00aea270)
- 新版 `00aea2bc`（命令位置の公開資料なし） · `00aea29c`（命令位置の公開資料なし） · `00aea2b4`（命令位置の公開資料なし）

~~~diff
- 00aea278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea2bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea278 bytes 60b603f9
+ 00aea2bc bytes 60d603f9
- 00aea258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00aea258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea29c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00aea29c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea258 bytes 68b643f9
+ 00aea29c bytes 68d643f9
- 00aea270 ["INT_ADD", "register:40f0:8", ["const:aea270:8", "const:4:8"]]
- 00aea270 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea2b4 ["INT_ADD", "register:40f0:8", ["const:aea2b4:8", "const:4:8"]]
+ 00aea2b4 ["CALL", null, ["callee:00bde090:8"]]
- 00aea270 bytes 74cf0394
+ 00aea2b4 bytes 77cf0394
~~~


<a id="compare-3646d3dde5f95dac37f390f14266d9f7"></a>

### [`00aea298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md) → [`00aea2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aea364",
      "incomplete_value": true,
      "site": "00aea364",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea310",
      "incomplete_value": true,
      "site": "00aea31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00aea2f0",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea310",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea364",
      "WRITE",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea2f0",
      "READ",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea310",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea364",
      "WRITE",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md#insn-00aea2d8) · [`00aea320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md#insn-00aea320) · [`00aea2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md#insn-00aea2ac)
- 新版 `00aea31c`（命令位置の公開資料なし） · `00aea364`（命令位置の公開資料なし） · `00aea2f0`（命令位置の公開資料なし）

~~~diff
- 00aea2d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea2d8 ["INT_ADD", "register:40f0:8", ["const:aea2d8:8", "const:4:8"]]
- 00aea2d8 ["CALLIND", null, ["register:0:8"]]
+ 00aea31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea31c ["INT_ADD", "register:40f0:8", ["const:aea31c:8", "const:4:8"]]
+ 00aea31c ["CALLIND", null, ["register:0:8"]]
- 00aea2d8 bytes 00013fd6
+ 00aea31c bytes 00013fd6
- 00aea320 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea320 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:770:8"]]
- 00aea320 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aea364 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aea364 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7b0:8"]]
+ 00aea364 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea320 bytes a0c21d39
+ 00aea364 bytes a0c21e39
- 00aea2ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:770:8"]]
- 00aea2ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aea2ac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aea2f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b0:8"]]
+ 00aea2f0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aea2f0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aea2ac bytes a8c25d39
+ 00aea2f0 bytes a8c25e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-437ee76c93675550f8d351ab842bcd5f"></a>

### [`00aea334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea334.md) → [`00aea378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aea3b4",
      "incomplete_value": true,
      "site": "00aea3b4",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea404",
      "incomplete_value": true,
      "site": "00aea404",
      "value": [
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
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea390",
      "incomplete_value": true,
      "site": "00aea390",
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
      "00aea38c",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea398",
      "READ",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea3b4",
      "WRITE",
      [
        "storage",
        "010a0770",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea38c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea398",
      "READ",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea3b4",
      "WRITE",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea334.md#insn-00aea370) · [`00aea3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea334.md#insn-00aea3bc) · [`00aea3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea334.md#insn-00aea3c0)
- 新版 `00aea3b4`（命令位置の公開資料なし） · `00aea400`（命令位置の公開資料なし） · `00aea404`（命令位置の公開資料なし）

~~~diff
- 00aea370 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea370 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea370 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:770:8"]]
- 00aea370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aea3b4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aea3b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aea3b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7b0:8"]]
+ 00aea3b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea370 bytes bfc21d39
+ 00aea3b4 bytes bfc21e39
- 00aea3bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea3bc ["INT_ADD", "register:40f0:8", ["const:aea3bc:8", "const:4:8"]]
- 00aea3bc ["CALLIND", null, ["register:0:8"]]
+ 00aea400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea400 ["INT_ADD", "register:40f0:8", ["const:aea400:8", "const:4:8"]]
+ 00aea400 ["CALLIND", null, ["register:0:8"]]
- 00aea3bc bytes 00013fd6
+ 00aea400 bytes 00013fd6
- 00aea3c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
- 00aea3c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea3c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aea404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00aea404 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aea404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea3c0 bytes 9fb603f9
+ 00aea404 bytes 9fd603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c1503893b32b674f82817b2cdacc19"></a>

### [`00aea3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea3d4.md) → [`00aea418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea458",
      "incomplete_value": true,
      "site": "00aea458",
      "value": [
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
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea434",
      "incomplete_value": true,
      "site": "00aea434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea3f0"
      ],
      [
        "FALL_THROUGH",
        "00aea434"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea434",
      "incomplete_value": true,
      "site": "00aea458",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea42c",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea458",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea46c",
      "PARAM",
      [
        "storage",
        "00c10248",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aea42c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea458",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea46c",
      "PARAM",
      [
        "storage",
        "00c10298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea3d4.md#insn-00aea414) · [`00aea3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea3d4.md#insn-00aea3e8) · [`00aea40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea3d4.md#insn-00aea40c)
- 新版 `00aea458`（命令位置の公開資料なし） · `00aea42c`（命令位置の公開資料なし） · `00aea450`（命令位置の公開資料なし）

~~~diff
- 00aea414 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
- 00aea414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea458 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00aea458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea414 bytes 80b603f9
+ 00aea458 bytes 80d603f9
- 00aea3e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
- 00aea3e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea42c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00aea42c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea3e8 bytes 81b643f9
+ 00aea42c bytes 81d643f9
- 00aea40c ["INT_ADD", "register:40f0:8", ["const:aea40c:8", "const:4:8"]]
- 00aea40c ["CALL", null, ["callee:00bde090:8"]]
+ 00aea450 ["INT_ADD", "register:40f0:8", ["const:aea450:8", "const:4:8"]]
+ 00aea450 ["CALL", null, ["callee:00bde090:8"]]
- 00aea40c bytes 0dcf0394
+ 00aea450 bytes 10cf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f1d0a7c6e80e562273ecc2677990a2"></a>

### [`00aea444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea444.md) → [`00aea488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aea4a4",
      "incomplete_value": false,
      "site": "00aea4a8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea4b4",
      "incomplete_value": true,
      "site": "00aea4c0",
      "value": [
        "LOAD",
        "8",
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
      "00aea4a4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea4b4",
      "DATA",
      [
        "storage",
        "010a0778",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea4a4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea4b4",
      "DATA",
      [
        "storage",
        "010a07b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea444.md#insn-00aea464) · [`00aea460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea444.md#insn-00aea460) · [`00aea46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea444.md#insn-00aea46c)
- 新版 `00aea4a8`（命令位置の公開資料なし） · `00aea4a4`（命令位置の公開資料なし） · `00aea4b0`（命令位置の公開資料なし）

~~~diff
- 00aea464 ["INT_ADD", "register:40f0:8", ["const:aea464:8", "const:4:8"]]
- 00aea464 ["CALL", null, ["callee:00bde180:8"]]
+ 00aea4a8 ["INT_ADD", "register:40f0:8", ["const:aea4a8:8", "const:4:8"]]
+ 00aea4a8 ["CALL", null, ["callee:00bde180:8"]]
- 00aea464 bytes 33cf0394
+ 00aea4a8 bytes 36cf0394
- 00aea460 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aea460 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea460 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea460 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea4a4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aea4a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea4a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea4a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea460 bytes 00501791
+ 00aea4a4 bytes 001c1591
- 00aea46c ["COPY", "tmp:0:8", ["const:778:8"]]
- 00aea46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea4b0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00aea4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea46c bytes 08e11d91
+ 00aea4b0 bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-832b4217914b9f7c7fb9ffb6faf4be94"></a>

### [`00aea480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea480.md) → [`00aea4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea504",
      "incomplete_value": true,
      "site": "00aea504",
      "value": [
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
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea4e0",
      "incomplete_value": true,
      "site": "00aea4e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aea49c"
      ],
      [
        "FALL_THROUGH",
        "00aea4e0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aea4e0",
      "incomplete_value": true,
      "site": "00aea504",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea4d8",
      "READ",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea504",
      "WRITE",
      [
        "storage",
        "010a0768",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea51c",
      "PARAM",
      [
        "storage",
        "010a0788",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea4d8",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea504",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea51c",
      "PARAM",
      [
        "storage",
        "010a07c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea480.md#insn-00aea4c0) · [`00aea494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea480.md#insn-00aea494) · [`00aea4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea480.md#insn-00aea4b8)
- 新版 `00aea504`（命令位置の公開資料なし） · `00aea4d8`（命令位置の公開資料なし） · `00aea4fc`（命令位置の公開資料なし）

~~~diff
- 00aea4c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
- 00aea4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea504 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00aea504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea4c0 bytes 80b603f9
+ 00aea504 bytes 80d603f9
- 00aea494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:768:8"]]
- 00aea494 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea4d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00aea4d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea494 bytes 81b643f9
+ 00aea4d8 bytes 81d643f9
- 00aea4b8 ["INT_ADD", "register:40f0:8", ["const:aea4b8:8", "const:4:8"]]
- 00aea4b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea4fc ["INT_ADD", "register:40f0:8", ["const:aea4fc:8", "const:4:8"]]
+ 00aea4fc ["CALL", null, ["callee:00bde090:8"]]
- 00aea4b8 bytes e2ce0394
+ 00aea4fc bytes e5ce0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d8b2893dc73cb952f015c5a5b6c8e9e"></a>

### [`00aea4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea4f0.md) → [`00aea534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aea550",
      "incomplete_value": false,
      "site": "00aea554",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea560",
      "incomplete_value": true,
      "site": "00aea56c",
      "value": [
        "LOAD",
        "8",
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
      "00aea550",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea560",
      "DATA",
      [
        "storage",
        "010a0788",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea550",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea560",
      "DATA",
      [
        "storage",
        "010a07c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea4f0.md#insn-00aea510) · [`00aea50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea4f0.md#insn-00aea50c) · [`00aea518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea4f0.md#insn-00aea518)
- 新版 `00aea554`（命令位置の公開資料なし） · `00aea550`（命令位置の公開資料なし） · `00aea55c`（命令位置の公開資料なし）

~~~diff
- 00aea510 ["INT_ADD", "register:40f0:8", ["const:aea510:8", "const:4:8"]]
- 00aea510 ["CALL", null, ["callee:00bde180:8"]]
+ 00aea554 ["INT_ADD", "register:40f0:8", ["const:aea554:8", "const:4:8"]]
+ 00aea554 ["CALL", null, ["callee:00bde180:8"]]
- 00aea510 bytes 08cf0394
+ 00aea554 bytes 0bcf0394
- 00aea50c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aea50c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea50c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea50c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea550 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aea550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea50c bytes 00fc1991
+ 00aea550 bytes 00c81791
- 00aea518 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00aea518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea55c ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00aea55c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea55c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea55c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea518 bytes 08211e91
+ 00aea55c bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-595bbdd3f5e5e0a300973f832f450d1f"></a>

### [`00aea52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea52c.md) → [`00aea570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea570.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

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
      "definition_site": "00aea59c",
      "incomplete_value": true,
      "site": "00aea59c",
      "value": [
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
            "const:790:8"
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
      "definition_site": "00aea584",
      "incomplete_value": true,
      "site": "00aea584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea590",
      "incomplete_value": false,
      "site": "00aea594",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea580",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea590",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea59c",
      "WRITE",
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
      "00aea580",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea590",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea59c",
      "WRITE",
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

- 旧版 [`00aea550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea52c.md#insn-00aea550) · [`00aea558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea52c.md#insn-00aea558) · [`00aea53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea52c.md#insn-00aea53c)
- 新版 `00aea594`（命令位置の公開資料なし） · `00aea59c`（命令位置の公開資料なし） · `00aea580`（命令位置の公開資料なし）

~~~diff
- 00aea550 ["INT_ADD", "register:40f0:8", ["const:aea550:8", "const:4:8"]]
- 00aea550 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea594 ["INT_ADD", "register:40f0:8", ["const:aea594:8", "const:4:8"]]
+ 00aea594 ["CALL", null, ["callee:00bde090:8"]]
- 00aea550 bytes bcce0394
+ 00aea594 bytes bfce0394
- 00aea558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea558 bytes 60ca03f9
+ 00aea59c bytes 60ea03f9
- 00aea53c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea53c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea53c bytes 68ca43f9
+ 00aea580 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62833f2267e8f472f884e741e13a3d48"></a>

### [`00aea56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea56c.md) → [`00aea5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5b0.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea5c4",
      "incomplete_value": true,
      "site": "00aea5c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea5c0",
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
  ],
  "added": [
    [
      "00aea5c0",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea5cc",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea5dc",
      "WRITE",
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

- 旧版 [`00aea590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea56c.md#insn-00aea590) · [`00aea598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea56c.md#insn-00aea598) · [`00aea57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea56c.md#insn-00aea57c)
- 新版 `00aea5d4`（命令位置の公開資料なし） · `00aea5dc`（命令位置の公開資料なし） · `00aea5c0`（命令位置の公開資料なし）

~~~diff
- 00aea590 ["INT_ADD", "register:40f0:8", ["const:aea590:8", "const:4:8"]]
- 00aea590 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea5d4 ["INT_ADD", "register:40f0:8", ["const:aea5d4:8", "const:4:8"]]
+ 00aea5d4 ["CALL", null, ["callee:00bde090:8"]]
- 00aea590 bytes acce0394
+ 00aea5d4 bytes afce0394
- 00aea598 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea598 bytes 60ca03f9
+ 00aea5dc bytes 60ea03f9
- 00aea57c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea5c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea57c bytes 68ca43f9
+ 00aea5c0 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9329bd22462b87aac369695264058b61"></a>

### [`00aea5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5ac.md) → [`00aea5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea610",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea610",
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
  ],
  "added": [
    [
      "00aea600",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea610",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea620",
      "WRITE",
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

- 旧版 [`00aea5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5ac.md#insn-00aea5d4) · [`00aea5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5ac.md#insn-00aea5dc) · [`00aea5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5ac.md#insn-00aea5bc)
- 新版 `00aea618`（命令位置の公開資料なし） · `00aea620`（命令位置の公開資料なし） · `00aea600`（命令位置の公開資料なし）

~~~diff
- 00aea5d4 ["INT_ADD", "register:40f0:8", ["const:aea5d4:8", "const:4:8"]]
- 00aea5d4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea618 ["INT_ADD", "register:40f0:8", ["const:aea618:8", "const:4:8"]]
+ 00aea618 ["CALL", null, ["callee:00bde090:8"]]
- 00aea5d4 bytes 9bce0394
+ 00aea618 bytes 9ece0394
- 00aea5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea5dc bytes 60ca03f9
+ 00aea620 bytes 60ea03f9
- 00aea5bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea5bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea600 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea5bc bytes 68ca43f9
+ 00aea600 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a54eed9b2599211cd3dd97637188f50e"></a>

### [`00aea5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5f0.md) → [`00aea634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea634.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea664",
      "incomplete_value": true,
      "site": "00aea664",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea648",
      "incomplete_value": true,
      "site": "00aea648",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea650",
      "incomplete_value": false,
      "site": "00aea65c",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea644",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea650",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea664",
      "WRITE",
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
      "00aea644",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea650",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea664",
      "WRITE",
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

- 旧版 [`00aea618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5f0.md#insn-00aea618) · [`00aea620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5f0.md#insn-00aea620) · [`00aea600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea5f0.md#insn-00aea600)
- 新版 `00aea65c`（命令位置の公開資料なし） · `00aea664`（命令位置の公開資料なし） · `00aea644`（命令位置の公開資料なし）

~~~diff
- 00aea618 ["INT_ADD", "register:40f0:8", ["const:aea618:8", "const:4:8"]]
- 00aea618 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea65c ["INT_ADD", "register:40f0:8", ["const:aea65c:8", "const:4:8"]]
+ 00aea65c ["CALL", null, ["callee:00bde090:8"]]
- 00aea618 bytes 8ace0394
+ 00aea65c bytes 8dce0394
- 00aea620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea620 bytes 60ca03f9
+ 00aea664 bytes 60ea03f9
- 00aea600 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:790:8"]]
- 00aea600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00aea644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea600 bytes 68ca43f9
+ 00aea644 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77b4ab035bc622a3f769f835a45852b5"></a>

### [`00aea640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea640.md) → [`00aea684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea684.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aea70c",
      "incomplete_value": true,
      "site": "00aea70c",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea6b8",
      "incomplete_value": true,
      "site": "00aea6c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00aea698",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea6b8",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea70c",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea698",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea6b8",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea70c",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea640.md#insn-00aea680) · [`00aea6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea640.md#insn-00aea6c8) · [`00aea654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea640.md#insn-00aea654)
- 新版 `00aea6c4`（命令位置の公開資料なし） · `00aea70c`（命令位置の公開資料なし） · `00aea698`（命令位置の公開資料なし）

~~~diff
- 00aea680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea680 ["INT_ADD", "register:40f0:8", ["const:aea680:8", "const:4:8"]]
- 00aea680 ["CALLIND", null, ["register:0:8"]]
+ 00aea6c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea6c4 ["INT_ADD", "register:40f0:8", ["const:aea6c4:8", "const:4:8"]]
+ 00aea6c4 ["CALLIND", null, ["register:0:8"]]
- 00aea680 bytes 00013fd6
+ 00aea6c4 bytes 00013fd6
- 00aea6c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea6c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:798:8"]]
- 00aea6c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aea70c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aea70c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
+ 00aea70c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea6c8 bytes a0621e39
+ 00aea70c bytes a0621f39
- 00aea654 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:798:8"]]
- 00aea654 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aea654 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aea698 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
+ 00aea698 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aea698 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aea654 bytes a8625e39
+ 00aea698 bytes a8625f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ff6caafff791b3f437f642a47dc486"></a>

### [`00aea6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea6dc.md) → [`00aea720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aea75c",
      "incomplete_value": true,
      "site": "00aea75c",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aea7ac",
      "incomplete_value": true,
      "site": "00aea7ac",
      "value": [
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
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea738",
      "incomplete_value": true,
      "site": "00aea738",
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
      "00aea734",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea740",
      "READ",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea75c",
      "WRITE",
      [
        "storage",
        "010a0798",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aea734",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea740",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aea75c",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea6dc.md#insn-00aea718) · [`00aea764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea6dc.md#insn-00aea764) · [`00aea768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea6dc.md#insn-00aea768)
- 新版 `00aea75c`（命令位置の公開資料なし） · `00aea7a8`（命令位置の公開資料なし） · `00aea7ac`（命令位置の公開資料なし）

~~~diff
- 00aea718 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea718 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea718 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:798:8"]]
- 00aea718 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aea75c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aea75c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aea75c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d8:8"]]
+ 00aea75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea718 bytes bf621e39
+ 00aea75c bytes bf621f39
- 00aea764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea764 ["INT_ADD", "register:40f0:8", ["const:aea764:8", "const:4:8"]]
- 00aea764 ["CALLIND", null, ["register:0:8"]]
+ 00aea7a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aea7a8 ["INT_ADD", "register:40f0:8", ["const:aea7a8:8", "const:4:8"]]
+ 00aea7a8 ["CALLIND", null, ["register:0:8"]]
- 00aea764 bytes 00013fd6
+ 00aea7a8 bytes 00013fd6
- 00aea768 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
- 00aea768 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aea7ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00aea7ac ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aea7ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea768 bytes 9fca03f9
+ 00aea7ac bytes 9fea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134938d52c54e3465de28731eb1accf2"></a>

### [`00aea77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea77c.md) → [`00aea7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea7c0.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea800",
      "incomplete_value": true,
      "site": "00aea800",
      "value": [
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea7dc",
      "incomplete_value": true,
      "site": "00aea7dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea7e4",
      "incomplete_value": false,
      "site": "00aea7f8",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea7d4",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea7e4",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea800",
      "WRITE",
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
      "00aea7d4",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea7e4",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea800",
      "WRITE",
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

- 旧版 [`00aea7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea77c.md#insn-00aea7b4) · [`00aea7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea77c.md#insn-00aea7bc) · [`00aea790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea77c.md#insn-00aea790)
- 新版 `00aea7f8`（命令位置の公開資料なし） · `00aea800`（命令位置の公開資料なし） · `00aea7d4`（命令位置の公開資料なし）

~~~diff
- 00aea7b4 ["INT_ADD", "register:40f0:8", ["const:aea7b4:8", "const:4:8"]]
- 00aea7b4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea7f8 ["INT_ADD", "register:40f0:8", ["const:aea7f8:8", "const:4:8"]]
+ 00aea7f8 ["CALL", null, ["callee:00bde090:8"]]
- 00aea7b4 bytes 23ce0394
+ 00aea7f8 bytes 26ce0394
- 00aea7bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
- 00aea7bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea800 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00aea800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea7bc bytes 80ca03f9
+ 00aea800 bytes 80ea03f9
- 00aea790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
- 00aea790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea7d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00aea7d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea790 bytes 81ca43f9
+ 00aea7d4 bytes 81ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe1b17b888440380cce8301e002c96b"></a>

### [`00aea7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea7ec.md) → [`00aea830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde640.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde690.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aea84c",
      "incomplete_value": false,
      "site": "00aea850",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea85c",
      "incomplete_value": true,
      "site": "00aea868",
      "value": [
        "LOAD",
        "8",
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
      "00aea84c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aea85c",
      "DATA",
      [
        "storage",
        "010a07a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea84c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aea85c",
      "DATA",
      [
        "storage",
        "010a07e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea7ec.md#insn-00aea80c) · [`00aea808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea7ec.md#insn-00aea808) · [`00aea814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea7ec.md#insn-00aea814)
- 新版 `00aea850`（命令位置の公開資料なし） · `00aea84c`（命令位置の公開資料なし） · `00aea858`（命令位置の公開資料なし）

~~~diff
- 00aea80c ["INT_ADD", "register:40f0:8", ["const:aea80c:8", "const:4:8"]]
- 00aea80c ["CALL", null, ["callee:00bde180:8"]]
+ 00aea850 ["INT_ADD", "register:40f0:8", ["const:aea850:8", "const:4:8"]]
+ 00aea850 ["CALL", null, ["callee:00bde180:8"]]
- 00aea80c bytes 49ce0394
+ 00aea850 bytes 4cce0394
- 00aea808 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aea808 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea808 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea808 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea84c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aea84c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea84c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea84c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea808 bytes 00501791
+ 00aea84c bytes 001c1591
- 00aea814 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00aea814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea858 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00aea858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea814 bytes 08811e91
+ 00aea858 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde6a177af26b2f9c95013bdcdd546b6"></a>

### [`00aea828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea828.md) → [`00aea86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea86c.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aea8ac",
      "incomplete_value": true,
      "site": "00aea8ac",
      "value": [
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea888",
      "incomplete_value": true,
      "site": "00aea888",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea890",
      "incomplete_value": false,
      "site": "00aea8a4",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea880",
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea890",
      "PARAM",
      [
        "storage",
        "002a60d8",
        null,
        "string"
      ]
    ],
    [
      "00aea8ac",
      "WRITE",
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
      "00aea880",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea890",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00aea8ac",
      "WRITE",
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

- 旧版 [`00aea860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea828.md#insn-00aea860) · [`00aea868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea828.md#insn-00aea868) · [`00aea83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea828.md#insn-00aea83c)
- 新版 `00aea8a4`（命令位置の公開資料なし） · `00aea8ac`（命令位置の公開資料なし） · `00aea880`（命令位置の公開資料なし）

~~~diff
- 00aea860 ["INT_ADD", "register:40f0:8", ["const:aea860:8", "const:4:8"]]
- 00aea860 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea8a4 ["INT_ADD", "register:40f0:8", ["const:aea8a4:8", "const:4:8"]]
+ 00aea8a4 ["CALL", null, ["callee:00bde090:8"]]
- 00aea860 bytes f8cd0394
+ 00aea8a4 bytes fbcd0394
- 00aea868 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
- 00aea868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea8ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00aea8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea868 bytes 80ca03f9
+ 00aea8ac bytes 80ea03f9
- 00aea83c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:790:8"]]
- 00aea83c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea880 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
+ 00aea880 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea83c bytes 81ca43f9
+ 00aea880 bytes 81ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5626a7c5946d36e6938e77327553c64c"></a>

### [`00aea898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md) → [`00aea8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea8dc.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aea8f8",
      "incomplete_value": false,
      "site": "00aea8fc",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aea908",
      "incomplete_value": true,
      "site": "00aea914",
      "value": [
        "LOAD",
        "8",
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
      "00aea8f8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aea908",
      "DATA",
      [
        "storage",
        "010a07e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aea8f8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aea908",
      "DATA",
      [
        "storage",
        "010a0820",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md#insn-00aea8b8) · [`00aea8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md#insn-00aea8b4) · [`00aea8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md#insn-00aea8c0)
- 新版 `00aea8fc`（命令位置の公開資料なし） · `00aea8f8`（命令位置の公開資料なし） · `00aea904`（命令位置の公開資料なし）

~~~diff
- 00aea8b8 ["INT_ADD", "register:40f0:8", ["const:aea8b8:8", "const:4:8"]]
- 00aea8b8 ["CALL", null, ["callee:00bde180:8"]]
+ 00aea8fc ["INT_ADD", "register:40f0:8", ["const:aea8fc:8", "const:4:8"]]
+ 00aea8fc ["CALL", null, ["callee:00bde180:8"]]
- 00aea8b8 bytes 1ece0394
+ 00aea8fc bytes 21ce0394
- 00aea8b4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aea8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aea8f8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aea8f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea8f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aea8f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea8b4 bytes 00fc1991
+ 00aea8f8 bytes 00c81791
- 00aea8c0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00aea8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aea8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aea8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aea904 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00aea904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aea904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aea8c0 bytes 08811f91
+ 00aea904 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf019058e88a3bf366ba3a501939d73d"></a>

### [`00aea8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea8d4.md) → [`00aea918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea918.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aea944",
      "incomplete_value": true,
      "site": "00aea944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:828:8"
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
            "const:7e8:8"
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
      "definition_site": "00aea92c",
      "incomplete_value": true,
      "site": "00aea92c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea938",
      "incomplete_value": false,
      "site": "00aea93c",
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
    "old": {
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
      "00aea928",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea938",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aea944",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea928",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea938",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aea944",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea8d4.md#insn-00aea8f8) · [`00aea900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea8d4.md#insn-00aea900) · [`00aea8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea8d4.md#insn-00aea8e4)
- 新版 `00aea93c`（命令位置の公開資料なし） · `00aea944`（命令位置の公開資料なし） · `00aea928`（命令位置の公開資料なし）

~~~diff
- 00aea8f8 ["INT_ADD", "register:40f0:8", ["const:aea8f8:8", "const:4:8"]]
- 00aea8f8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea93c ["INT_ADD", "register:40f0:8", ["const:aea93c:8", "const:4:8"]]
+ 00aea93c ["CALL", null, ["callee:00bde090:8"]]
- 00aea8f8 bytes d2cd0394
+ 00aea93c bytes d5cd0394
- 00aea900 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea900 bytes 60f603f9
+ 00aea944 bytes 601604f9
- 00aea8e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea8e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea928 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea928 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea8e4 bytes 68f643f9
+ 00aea928 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a2f9dd0550dafff93c337de7cfc2174"></a>

### [`00aea914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea914.md) → [`00aea958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea958.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aea96c",
      "incomplete_value": true,
      "site": "00aea96c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:654:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00aea968",
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
  ],
  "added": [
    [
      "00aea968",
      "READ",
      [
        "storage",
        "010a0828",
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
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea914.md#insn-00aea938) · [`00aea940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea914.md#insn-00aea940) · [`00aea924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea914.md#insn-00aea924)
- 新版 `00aea97c`（命令位置の公開資料なし） · `00aea984`（命令位置の公開資料なし） · `00aea968`（命令位置の公開資料なし）

~~~diff
- 00aea938 ["INT_ADD", "register:40f0:8", ["const:aea938:8", "const:4:8"]]
- 00aea938 ["CALL", null, ["callee:00bde090:8"]]
+ 00aea97c ["INT_ADD", "register:40f0:8", ["const:aea97c:8", "const:4:8"]]
+ 00aea97c ["CALL", null, ["callee:00bde090:8"]]
- 00aea938 bytes c2cd0394
+ 00aea97c bytes c5cd0394
- 00aea940 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea940 bytes 60f603f9
+ 00aea984 bytes 601604f9
- 00aea924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea924 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea968 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea924 bytes 68f643f9
+ 00aea968 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f585bdf03ce80d64d0d320571de89d10"></a>

### [`00aea954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea954.md) → [`00aea998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea998.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea9b8",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "old": {
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
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9b8",
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
  ],
  "added": [
    [
      "00aea9a8",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9b8",
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
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea954.md#insn-00aea97c) · [`00aea984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea954.md#insn-00aea984) · [`00aea964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea954.md#insn-00aea964)
- 新版 `00aea9c0`（命令位置の公開資料なし） · `00aea9c8`（命令位置の公開資料なし） · `00aea9a8`（命令位置の公開資料なし）

~~~diff
- 00aea97c ["INT_ADD", "register:40f0:8", ["const:aea97c:8", "const:4:8"]]
- 00aea97c ["CALL", null, ["callee:00bde090:8"]]
+ 00aea9c0 ["INT_ADD", "register:40f0:8", ["const:aea9c0:8", "const:4:8"]]
+ 00aea9c0 ["CALL", null, ["callee:00bde090:8"]]
- 00aea97c bytes b1cd0394
+ 00aea9c0 bytes b4cd0394
- 00aea984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aea9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea984 bytes 60f603f9
+ 00aea9c8 bytes 601604f9
- 00aea964 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea9a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea9a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea964 bytes 68f643f9
+ 00aea9a8 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

