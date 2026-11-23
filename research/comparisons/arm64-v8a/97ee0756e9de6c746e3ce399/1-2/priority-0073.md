# v15.7.3 → v15.7.4 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-b3df94f6391f595a925320126c8bf2ad"></a>

### [`00b67018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md) → [`00b6705c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6708c",
      "incomplete_value": true,
      "site": "00b6708c",
      "value": [
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
      "definition_site": "00b67070",
      "incomplete_value": true,
      "site": "00b67070",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67078",
      "incomplete_value": false,
      "site": "00b67084",
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
      "definition_site": "00b67034",
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
      "00b6706c",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67078",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b6708c",
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
      "00b6706c",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67078",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b6708c",
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

- 旧版 [`00b67040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md#insn-00b67040) · [`00b67048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md#insn-00b67048) · [`00b67028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md#insn-00b67028)
- 新版 `00b67084`（命令位置の公開資料なし） · `00b6708c`（命令位置の公開資料なし） · `00b6706c`（命令位置の公開資料なし）

~~~diff
- 00b67040 ["INT_ADD", "register:40f0:8", ["const:b67040:8", "const:4:8"]]
- 00b67040 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67084 ["INT_ADD", "register:40f0:8", ["const:b67084:8", "const:4:8"]]
+ 00b67084 ["CALL", null, ["callee:00bde090:8"]]
- 00b67040 bytes 00dc0194
+ 00b67084 bytes 03dc0194
- 00b67048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b67048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6708c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b6708c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67048 bytes 600a04f9
+ 00b6708c bytes 602a04f9
- 00b67028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b67028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6706c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b6706c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67028 bytes 680a44f9
+ 00b6706c bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a859cf13463775ca52a79295a0cb7110"></a>

### [`00b67068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md) → [`00b670ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b670ac.md) _ZN8firebase4auth8timeunit15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67104",
      "incomplete_value": true,
      "site": "00b67104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b670c0",
      "incomplete_value": true,
      "site": "00b670c0",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b670e0",
      "incomplete_value": true,
      "site": "00b670ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:850:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6709c",
      "incomplete_value": true,
      "site": "00b670a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b670c0",
      "READ",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b670e0",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67104",
      "WRITE",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b670c0",
      "READ",
      [
        "storage",
        "010a1858",
        null,
        "undefined1"
      ]
    ],
    [
      "00b670e0",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67104",
      "WRITE",
      [
        "storage",
        "010a1858",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6707c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md#insn-00b6707c) · [`00b670a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md#insn-00b670a8) · [`00b670c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md#insn-00b670c0)
- 新版 `00b670c0`（命令位置の公開資料なし） · `00b670ec`（命令位置の公開資料なし） · `00b67104`（命令位置の公開資料なし）

~~~diff
- 00b6707c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:818:8"]]
- 00b6707c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6707c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b670c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00b670c0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b670c0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6707c bytes a8626039
+ 00b670c0 bytes a8626139
- 00b670a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b670a8 ["INT_ADD", "register:40f0:8", ["const:b670a8:8", "const:4:8"]]
- 00b670a8 ["CALLIND", null, ["register:0:8"]]
+ 00b670ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b670ec ["INT_ADD", "register:40f0:8", ["const:b670ec:8", "const:4:8"]]
+ 00b670ec ["CALLIND", null, ["register:0:8"]]
- 00b670a8 bytes 00013fd6
+ 00b670ec bytes 00013fd6
- 00b670c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b670c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
- 00b670c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67104 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67104 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:858:8"]]
+ 00b67104 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b670c0 bytes a0622039
+ 00b67104 bytes a0622139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97957e17f353fd484ec87d917a3b9558"></a>

### [`00b670d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b670d4.md) → [`00b67118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67118.md) _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67154",
      "incomplete_value": true,
      "site": "00b67154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67110",
      "incomplete_value": true,
      "site": "00b67110",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67174",
      "incomplete_value": true,
      "site": "00b67174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67130",
      "incomplete_value": true,
      "site": "00b67130",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67164",
      "incomplete_value": true,
      "site": "00b67170",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:850:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67120",
      "incomplete_value": true,
      "site": "00b6712c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:810:8"
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
      "00b6712c",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67138",
      "READ",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67154",
      "WRITE",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6712c",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67138",
      "READ",
      [
        "storage",
        "010a1858",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67154",
      "WRITE",
      [
        "storage",
        "010a1858",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b670e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b670d4.md#insn-00b670e8) · [`00b67110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b670d4.md#insn-00b67110) · [`00b6712c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b670d4.md#insn-00b6712c)
- 新版 `00b6712c`（命令位置の公開資料なし） · `00b67154`（命令位置の公開資料なし） · `00b67170`（命令位置の公開資料なし）

~~~diff
- 00b670e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b670e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6712c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b6712c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b670e8 bytes 810a44f9
+ 00b6712c bytes 812a44f9
- 00b67110 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67110 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67110 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
- 00b67110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67154 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67154 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67154 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:858:8"]]
+ 00b67154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67110 bytes bf622039
+ 00b67154 bytes bf622139
- 00b6712c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6712c ["INT_ADD", "register:40f0:8", ["const:b6712c:8", "const:4:8"]]
- 00b6712c ["CALLIND", null, ["register:0:8"]]
+ 00b67170 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67170 ["INT_ADD", "register:40f0:8", ["const:b67170:8", "const:4:8"]]
+ 00b67170 ["CALLIND", null, ["register:0:8"]]
- 00b6712c bytes 00013fd6
+ 00b67170 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e4b4bc1bd12fd929a887362fed0ae6"></a>

### [`00b67144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md) → [`00b67188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b671c8",
      "incomplete_value": true,
      "site": "00b671c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67184",
      "incomplete_value": true,
      "site": "00b67184",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b671a4",
      "incomplete_value": true,
      "site": "00b671a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67160",
      "incomplete_value": true,
      "site": "00b67160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67160"
      ],
      [
        "FALL_THROUGH",
        "00b671a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b671a4",
      "incomplete_value": true,
      "site": "00b671c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67160",
      "incomplete_value": true,
      "site": "00b67184",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6719c",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b671ac",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b671c8",
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
      "00b6719c",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b671ac",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b671c8",
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

- 旧版 [`00b67184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md#insn-00b67184) · [`00b67158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md#insn-00b67158) · [`00b67168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md#insn-00b67168)
- 新版 `00b671c8`（命令位置の公開資料なし） · `00b6719c`（命令位置の公開資料なし） · `00b671ac`（命令位置の公開資料なし）

~~~diff
- 00b67184 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b67184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b671c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b671c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67184 bytes 800a04f9
+ 00b671c8 bytes 802a04f9
- 00b67158 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b67158 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6719c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b6719c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67158 bytes 810a44f9
+ 00b6719c bytes 812a44f9
- 00b67168 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00b67168 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b67168 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b67168 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b671ac ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00b671ac ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b671ac ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b671ac ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b67168 bytes 63800091
+ 00b671ac bytes 63ac0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-346f79e64799f2a011752d384d59851c"></a>

### [`00b671b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md) → [`00b671f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b671f8.md) _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67214",
      "incomplete_value": false,
      "site": "00b67218",
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
      "definition_site": "00b671d0",
      "incomplete_value": false,
      "site": "00b671d4",
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
      "00b67214",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67224",
      "DATA",
      [
        "storage",
        "010a1820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67214",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67224",
      "DATA",
      [
        "storage",
        "010a1860",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b671d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md#insn-00b671d4) · [`00b671d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md#insn-00b671d0) · [`00b671dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md#insn-00b671dc)
- 新版 `00b67218`（命令位置の公開資料なし） · `00b67214`（命令位置の公開資料なし） · `00b67220`（命令位置の公開資料なし）

~~~diff
- 00b671d4 ["INT_ADD", "register:40f0:8", ["const:b671d4:8", "const:4:8"]]
- 00b671d4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b67218 ["INT_ADD", "register:40f0:8", ["const:b67218:8", "const:4:8"]]
+ 00b67218 ["CALL", null, ["callee:00bde180:8"]]
- 00b671d4 bytes d7db0194
+ 00b67218 bytes dadb0194
- 00b671d0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b671d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b671d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b671d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67214 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b67214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b671d0 bytes 00501791
+ 00b67214 bytes 001c1591
- 00b671dc ["COPY", "tmp:0:8", ["const:820:8"]]
- 00b671dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b671dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b671dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67220 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00b67220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b671dc bytes 08812091
+ 00b67220 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f268ac41992d7a155c2fda021bd9c362"></a>

### [`00b671f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md) → [`00b67234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b67274",
      "incomplete_value": true,
      "site": "00b67274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67230",
      "incomplete_value": true,
      "site": "00b67230",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67250",
      "incomplete_value": true,
      "site": "00b67250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6720c",
      "incomplete_value": true,
      "site": "00b6720c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67258",
      "incomplete_value": false,
      "site": "00b6726c",
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
      "definition_site": "00b67214",
      "incomplete_value": false,
      "site": "00b67228",
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
      "00b67248",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67258",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ],
    [
      "00b67274",
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
      "00b67248",
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67258",
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      "00b67274",
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

- 旧版 [`00b67228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md#insn-00b67228) · [`00b67230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md#insn-00b67230) · [`00b67204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md#insn-00b67204)
- 新版 `00b6726c`（命令位置の公開資料なし） · `00b67274`（命令位置の公開資料なし） · `00b67248`（命令位置の公開資料なし）

~~~diff
- 00b67228 ["INT_ADD", "register:40f0:8", ["const:b67228:8", "const:4:8"]]
- 00b67228 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6726c ["INT_ADD", "register:40f0:8", ["const:b6726c:8", "const:4:8"]]
+ 00b6726c ["CALL", null, ["callee:00bde090:8"]]
- 00b67228 bytes 86db0194
+ 00b6726c bytes 89db0194
- 00b67230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b67230 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67274 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b67274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67230 bytes 800a04f9
+ 00b67274 bytes 802a04f9
- 00b67204 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b67204 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67248 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b67248 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67204 bytes 810a44f9
+ 00b67248 bytes 812a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c61a3863f0e66db841812cffd5e0080"></a>

### [`00b67260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md) → [`00b672a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672a4.md) _ZN8firebase4auth8timeunit10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b672c0",
      "incomplete_value": false,
      "site": "00b672c4",
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
      "definition_site": "00b6727c",
      "incomplete_value": false,
      "site": "00b67280",
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
      "definition_site": "00b672d0",
      "incomplete_value": true,
      "site": "00b672dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6728c",
      "incomplete_value": true,
      "site": "00b67298",
      "value": [
        "LOAD",
        "8",
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
      "00b672c0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b672d0",
      "DATA",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b672c0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b672d0",
      "DATA",
      [
        "storage",
        "010a1868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b67280) · [`00b6727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b6727c) · [`00b67288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b67288)
- 新版 `00b672c4`（命令位置の公開資料なし） · `00b672c0`（命令位置の公開資料なし） · `00b672cc`（命令位置の公開資料なし）

~~~diff
- 00b67280 ["INT_ADD", "register:40f0:8", ["const:b67280:8", "const:4:8"]]
- 00b67280 ["CALL", null, ["callee:00bde180:8"]]
+ 00b672c4 ["INT_ADD", "register:40f0:8", ["const:b672c4:8", "const:4:8"]]
+ 00b672c4 ["CALL", null, ["callee:00bde180:8"]]
- 00b67280 bytes acdb0194
+ 00b672c4 bytes afdb0194
- 00b6727c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6727c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6727c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6727c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b672c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b672c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b672c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b672c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6727c bytes 00fc1991
+ 00b672c0 bytes 00c81791
- 00b67288 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00b67288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b672cc ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00b672cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b672cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b672cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67288 bytes 08a12091
+ 00b672cc bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a27a52f87dd410fefdb3ab6c3573da"></a>

### [`00b6729c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6729c.md) → [`00b672e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b6730c",
      "incomplete_value": true,
      "site": "00b6730c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672c8",
      "incomplete_value": true,
      "site": "00b672c8",
      "value": [
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
      "definition_site": "00b672f4",
      "incomplete_value": true,
      "site": "00b672f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672b0",
      "incomplete_value": true,
      "site": "00b672b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b672b0"
      ],
      [
        "FALL_THROUGH",
        "00b672f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b672f4",
      "incomplete_value": true,
      "site": "00b6730c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672b0",
      "incomplete_value": true,
      "site": "00b672c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b672f0",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6730c",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b672f0",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6730c",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b672c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6729c.md#insn-00b672c8) · [`00b672ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6729c.md#insn-00b672ac) · [`00b672c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6729c.md#insn-00b672c0)
- 新版 `00b6730c`（命令位置の公開資料なし） · `00b672f0`（命令位置の公開資料なし） · `00b67304`（命令位置の公開資料なし）

~~~diff
- 00b672c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b672c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6730c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b6730c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b672c8 bytes 601a04f9
+ 00b6730c bytes 603a04f9
- 00b672ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b672ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b672f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b672f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b672ac bytes 681a44f9
+ 00b672f0 bytes 683a44f9
- 00b672c0 ["INT_ADD", "register:40f0:8", ["const:b672c0:8", "const:4:8"]]
- 00b672c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67304 ["INT_ADD", "register:40f0:8", ["const:b67304:8", "const:4:8"]]
+ 00b67304 ["CALL", null, ["callee:00bde090:8"]]
- 00b672c0 bytes 60db0194
+ 00b67304 bytes 63db0194
~~~


<a id="compare-ea380dc9986c066ae7af094143cfad2a"></a>

### [`00b672dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md) → [`00b67320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b6734c",
      "incomplete_value": true,
      "site": "00b6734c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67308",
      "incomplete_value": true,
      "site": "00b67308",
      "value": [
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
      "definition_site": "00b67334",
      "incomplete_value": true,
      "site": "00b67334",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672f0",
      "incomplete_value": true,
      "site": "00b672f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b672f0"
      ],
      [
        "FALL_THROUGH",
        "00b67334"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67334",
      "incomplete_value": true,
      "site": "00b6734c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672f0",
      "incomplete_value": true,
      "site": "00b67308",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67330",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6734c",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67330",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6734c",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md#insn-00b67308) · [`00b672ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md#insn-00b672ec) · [`00b67300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md#insn-00b67300)
- 新版 `00b6734c`（命令位置の公開資料なし） · `00b67330`（命令位置の公開資料なし） · `00b67344`（命令位置の公開資料なし）

~~~diff
- 00b67308 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b67308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6734c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b6734c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67308 bytes 601a04f9
+ 00b6734c bytes 603a04f9
- 00b672ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b672ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b67330 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b672ec bytes 681a44f9
+ 00b67330 bytes 683a44f9
- 00b67300 ["INT_ADD", "register:40f0:8", ["const:b67300:8", "const:4:8"]]
- 00b67300 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67344 ["INT_ADD", "register:40f0:8", ["const:b67344:8", "const:4:8"]]
+ 00b67344 ["CALL", null, ["callee:00bde090:8"]]
- 00b67300 bytes 50db0194
+ 00b67344 bytes 53db0194
~~~


<a id="compare-f70a836ec53c33d0544d86423e5425e8"></a>

### [`00b6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md) → [`00b67360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b67390",
      "incomplete_value": true,
      "site": "00b67390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6734c",
      "incomplete_value": true,
      "site": "00b6734c",
      "value": [
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
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67374",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67330",
      "incomplete_value": true,
      "site": "00b67330",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67330"
      ],
      [
        "FALL_THROUGH",
        "00b67374"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67390",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67330",
      "incomplete_value": true,
      "site": "00b6734c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67370",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67390",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67370",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67390",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6734c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b6734c) · [`00b6732c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b6732c) · [`00b67344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b67344)
- 新版 `00b67390`（命令位置の公開資料なし） · `00b67370`（命令位置の公開資料なし） · `00b67388`（命令位置の公開資料なし）

~~~diff
- 00b6734c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b6734c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67390 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b67390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6734c bytes 601a04f9
+ 00b67390 bytes 603a04f9
- 00b6732c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b6732c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b67370 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6732c bytes 681a44f9
+ 00b67370 bytes 683a44f9
- 00b67344 ["INT_ADD", "register:40f0:8", ["const:b67344:8", "const:4:8"]]
- 00b67344 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67388 ["INT_ADD", "register:40f0:8", ["const:b67388:8", "const:4:8"]]
+ 00b67388 ["CALL", null, ["callee:00bde090:8"]]
- 00b67344 bytes 3fdb0194
+ 00b67388 bytes 42db0194
~~~


<a id="compare-2683574956bb869cec276fd87dc841ba"></a>

### [`00b67360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md) → [`00b673a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b673d4",
      "incomplete_value": true,
      "site": "00b673d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67390",
      "incomplete_value": true,
      "site": "00b67390",
      "value": [
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
      "definition_site": "00b673b8",
      "incomplete_value": true,
      "site": "00b673b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67374",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67374"
      ],
      [
        "FALL_THROUGH",
        "00b673b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b673b8",
      "incomplete_value": true,
      "site": "00b673d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67390",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b673b4",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b673d4",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b673b4",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b673d4",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md#insn-00b67390) · [`00b67370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md#insn-00b67370) · [`00b67388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md#insn-00b67388)
- 新版 `00b673d4`（命令位置の公開資料なし） · `00b673b4`（命令位置の公開資料なし） · `00b673cc`（命令位置の公開資料なし）

~~~diff
- 00b67390 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b67390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b673d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b673d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67390 bytes 601a04f9
+ 00b673d4 bytes 603a04f9
- 00b67370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b67370 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b673b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00b673b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67370 bytes 681a44f9
+ 00b673b4 bytes 683a44f9
- 00b67388 ["INT_ADD", "register:40f0:8", ["const:b67388:8", "const:4:8"]]
- 00b67388 ["CALL", null, ["callee:00bde090:8"]]
+ 00b673cc ["INT_ADD", "register:40f0:8", ["const:b673cc:8", "const:4:8"]]
+ 00b673cc ["CALL", null, ["callee:00bde090:8"]]
- 00b67388 bytes 2edb0194
+ 00b673cc bytes 31db0194
~~~


<a id="compare-1ae8d27e239c43bd4c173140269cb286"></a>

### [`00b673b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md) → [`00b673f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6744c",
      "incomplete_value": true,
      "site": "00b6744c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67408",
      "incomplete_value": true,
      "site": "00b67408",
      "value": [
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
      "definition_site": "00b67428",
      "incomplete_value": true,
      "site": "00b67434",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b673e4",
      "incomplete_value": true,
      "site": "00b673f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b67408",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67428",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6744c",
      "WRITE",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67408",
      "READ",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67428",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6744c",
      "WRITE",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b673c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b673c4) · [`00b673f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b673f0) · [`00b67408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b67408)
- 新版 `00b67408`（命令位置の公開資料なし） · `00b67434`（命令位置の公開資料なし） · `00b6744c`（命令位置の公開資料なし）

~~~diff
- 00b673c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
- 00b673c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b673c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67408 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:878:8"]]
+ 00b67408 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67408 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b673c4 bytes a8e26039
+ 00b67408 bytes a8e26139
- 00b673f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b673f0 ["INT_ADD", "register:40f0:8", ["const:b673f0:8", "const:4:8"]]
- 00b673f0 ["CALLIND", null, ["register:0:8"]]
+ 00b67434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67434 ["INT_ADD", "register:40f0:8", ["const:b67434:8", "const:4:8"]]
+ 00b67434 ["CALLIND", null, ["register:0:8"]]
- 00b673f0 bytes 00013fd6
+ 00b67434 bytes 00013fd6
- 00b67408 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67408 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
- 00b67408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6744c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6744c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:878:8"]]
+ 00b6744c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67408 bytes a0e22039
+ 00b6744c bytes a0e22139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cc93c4c8c88070aa9660ea57ce04359"></a>

### [`00b6741c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md) → [`00b67460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6749c",
      "incomplete_value": true,
      "site": "00b6749c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67458",
      "incomplete_value": true,
      "site": "00b67458",
      "value": [
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b674bc",
      "incomplete_value": true,
      "site": "00b674bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67478",
      "incomplete_value": true,
      "site": "00b67478",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67478",
      "incomplete_value": true,
      "site": "00b67478",
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
      "definition_site": "00b67434",
      "incomplete_value": true,
      "site": "00b67434",
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
      "00b67474",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67480",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6749c",
      "WRITE",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67474",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67480",
      "READ",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6749c",
      "WRITE",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67430) · [`00b67458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67458) · [`00b67474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67474)
- 新版 `00b67474`（命令位置の公開資料なし） · `00b6749c`（命令位置の公開資料なし） · `00b674b8`（命令位置の公開資料なし）

~~~diff
- 00b67430 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b67430 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67474 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00b67474 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67430 bytes 811a44f9
+ 00b67474 bytes 813a44f9
- 00b67458 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67458 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67458 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
- 00b67458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6749c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6749c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6749c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:878:8"]]
+ 00b6749c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67458 bytes bfe22039
+ 00b6749c bytes bfe22139
- 00b67474 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67474 ["INT_ADD", "register:40f0:8", ["const:b67474:8", "const:4:8"]]
- 00b67474 ["CALLIND", null, ["register:0:8"]]
+ 00b674b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b674b8 ["INT_ADD", "register:40f0:8", ["const:b674b8:8", "const:4:8"]]
+ 00b674b8 ["CALLIND", null, ["register:0:8"]]
- 00b67474 bytes 00013fd6
+ 00b674b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e714c0d8c3fe71ebb048c040641735"></a>

### [`00b6748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md) → [`00b674d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67510",
      "incomplete_value": true,
      "site": "00b67510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674cc",
      "incomplete_value": true,
      "site": "00b674cc",
      "value": [
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
      "definition_site": "00b674ec",
      "incomplete_value": true,
      "site": "00b674ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674a8",
      "incomplete_value": true,
      "site": "00b674a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b674a8"
      ],
      [
        "FALL_THROUGH",
        "00b674ec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b674ec",
      "incomplete_value": true,
      "site": "00b67510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674a8",
      "incomplete_value": true,
      "site": "00b674cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b674e4",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67510",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67524",
      "PARAM",
      [
        "storage",
        "00c12498",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b674e4",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67510",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67524",
      "PARAM",
      [
        "storage",
        "00c124e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b674cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674cc) · [`00b674a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674a0) · [`00b674c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674c4)
- 新版 `00b67510`（命令位置の公開資料なし） · `00b674e4`（命令位置の公開資料なし） · `00b67508`（命令位置の公開資料なし）

~~~diff
- 00b674cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b674cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00b67510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b674cc bytes 801a04f9
+ 00b67510 bytes 803a04f9
- 00b674a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b674a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b674e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00b674e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b674a0 bytes 811a44f9
+ 00b674e4 bytes 813a44f9
- 00b674c4 ["INT_ADD", "register:40f0:8", ["const:b674c4:8", "const:4:8"]]
- 00b674c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67508 ["INT_ADD", "register:40f0:8", ["const:b67508:8", "const:4:8"]]
+ 00b67508 ["CALL", null, ["callee:00bde090:8"]]
- 00b674c4 bytes dfda0194
+ 00b67508 bytes e2da0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-654284767e9dc0398c61fe1420fb2098"></a>

### [`00b674fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md) → [`00b67540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6755c",
      "incomplete_value": false,
      "site": "00b67560",
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
      "definition_site": "00b67518",
      "incomplete_value": false,
      "site": "00b6751c",
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
      "definition_site": "00b6756c",
      "incomplete_value": true,
      "site": "00b67578",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67528",
      "incomplete_value": true,
      "site": "00b67534",
      "value": [
        "LOAD",
        "8",
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
      "00b6755c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6756c",
      "DATA",
      [
        "storage",
        "010a1840",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6755c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6756c",
      "DATA",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b6751c) · [`00b67518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b67518) · [`00b67524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b67524)
- 新版 `00b67560`（命令位置の公開資料なし） · `00b6755c`（命令位置の公開資料なし） · `00b67568`（命令位置の公開資料なし）

~~~diff
- 00b6751c ["INT_ADD", "register:40f0:8", ["const:b6751c:8", "const:4:8"]]
- 00b6751c ["CALL", null, ["callee:00bde180:8"]]
+ 00b67560 ["INT_ADD", "register:40f0:8", ["const:b67560:8", "const:4:8"]]
+ 00b67560 ["CALL", null, ["callee:00bde180:8"]]
- 00b6751c bytes 05db0194
+ 00b67560 bytes 08db0194
- 00b67518 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b67518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6755c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6755c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6755c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6755c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67518 bytes 00501791
+ 00b6755c bytes 001c1591
- 00b67524 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00b67524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67568 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00b67568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67524 bytes 08012191
+ 00b67568 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754ae8e74e1451fd90729b13cfb09279"></a>

### [`00b67538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md) → [`00b6757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b675bc",
      "incomplete_value": true,
      "site": "00b675bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67578",
      "incomplete_value": true,
      "site": "00b67578",
      "value": [
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
      "definition_site": "00b67598",
      "incomplete_value": true,
      "site": "00b67598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67554",
      "incomplete_value": true,
      "site": "00b67554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67554"
      ],
      [
        "FALL_THROUGH",
        "00b67598"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67598",
      "incomplete_value": true,
      "site": "00b675bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67554",
      "incomplete_value": true,
      "site": "00b67578",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67590",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b675bc",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b675d4",
      "PARAM",
      [
        "storage",
        "010a1880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67590",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b675bc",
      "WRITE",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b675d4",
      "PARAM",
      [
        "storage",
        "010a18c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b67578) · [`00b6754c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b6754c) · [`00b67570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b67570)
- 新版 `00b675bc`（命令位置の公開資料なし） · `00b67590`（命令位置の公開資料なし） · `00b675b4`（命令位置の公開資料なし）

~~~diff
- 00b67578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b67578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b675bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00b675bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67578 bytes 801a04f9
+ 00b675bc bytes 803a04f9
- 00b6754c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b6754c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67590 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00b67590 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6754c bytes 811a44f9
+ 00b67590 bytes 813a44f9
- 00b67570 ["INT_ADD", "register:40f0:8", ["const:b67570:8", "const:4:8"]]
- 00b67570 ["CALL", null, ["callee:00bde090:8"]]
+ 00b675b4 ["INT_ADD", "register:40f0:8", ["const:b675b4:8", "const:4:8"]]
+ 00b675b4 ["CALL", null, ["callee:00bde090:8"]]
- 00b67570 bytes b4da0194
+ 00b675b4 bytes b7da0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed8f8aa11679964f24113f7675ea476c"></a>

### [`00b675a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md) → [`00b675ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67608",
      "incomplete_value": false,
      "site": "00b6760c",
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
      "definition_site": "00b675c4",
      "incomplete_value": false,
      "site": "00b675c8",
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
      "definition_site": "00b67618",
      "incomplete_value": true,
      "site": "00b67624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b675d4",
      "incomplete_value": true,
      "site": "00b675e0",
      "value": [
        "LOAD",
        "8",
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
      "00b67608",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67618",
      "DATA",
      [
        "storage",
        "010a1880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67608",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67618",
      "DATA",
      [
        "storage",
        "010a18c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b675c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675c8) · [`00b675c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675c4) · [`00b675d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675d0)
- 新版 `00b6760c`（命令位置の公開資料なし） · `00b67608`（命令位置の公開資料なし） · `00b67614`（命令位置の公開資料なし）

~~~diff
- 00b675c8 ["INT_ADD", "register:40f0:8", ["const:b675c8:8", "const:4:8"]]
- 00b675c8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6760c ["INT_ADD", "register:40f0:8", ["const:b6760c:8", "const:4:8"]]
+ 00b6760c ["CALL", null, ["callee:00bde180:8"]]
- 00b675c8 bytes dada0194
+ 00b6760c bytes ddda0194
- 00b675c4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b675c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b675c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b675c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67608 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b67608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b675c4 bytes 00fc1991
+ 00b67608 bytes 00c81791
- 00b675d0 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00b675d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b675d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b675d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67614 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00b67614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b675d0 bytes 08012291
+ 00b67614 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54dfbfbc265998f1cac0e27d6e714be1"></a>

### [`00b675e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md) → [`00b67628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b67654",
      "incomplete_value": true,
      "site": "00b67654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67610",
      "incomplete_value": true,
      "site": "00b67610",
      "value": [
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
      "definition_site": "00b6763c",
      "incomplete_value": true,
      "site": "00b6763c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675f8",
      "incomplete_value": true,
      "site": "00b675f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67648",
      "incomplete_value": false,
      "site": "00b6764c",
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
    "old": {
      "definition_site": "00b67604",
      "incomplete_value": false,
      "site": "00b67608",
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
            "const:5f9:8"
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
      "00b67638",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67648",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67654",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67638",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67648",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67654",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b67608) · [`00b67610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b67610) · [`00b675f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b675f4)
- 新版 `00b6764c`（命令位置の公開資料なし） · `00b67654`（命令位置の公開資料なし） · `00b67638`（命令位置の公開資料なし）

~~~diff
- 00b67608 ["INT_ADD", "register:40f0:8", ["const:b67608:8", "const:4:8"]]
- 00b67608 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6764c ["INT_ADD", "register:40f0:8", ["const:b6764c:8", "const:4:8"]]
+ 00b6764c ["CALL", null, ["callee:00bde090:8"]]
- 00b67608 bytes 8eda0194
+ 00b6764c bytes 91da0194
- 00b67610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b67610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b67654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67610 bytes 604604f9
+ 00b67654 bytes 606604f9
- 00b675f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b675f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b67638 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b675f4 bytes 684644f9
+ 00b67638 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1c201fd8f3fa85f75e58f05fc034ff"></a>

### [`00b67624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md) → [`00b67668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b67694",
      "incomplete_value": true,
      "site": "00b67694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67650",
      "incomplete_value": true,
      "site": "00b67650",
      "value": [
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
      "definition_site": "00b6767c",
      "incomplete_value": true,
      "site": "00b6767c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67638",
      "incomplete_value": true,
      "site": "00b67638",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67684",
      "incomplete_value": false,
      "site": "00b6768c",
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
    "old": {
      "definition_site": "00b67640",
      "incomplete_value": false,
      "site": "00b67648",
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
            "const:5f9:8"
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
      "00b67678",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67684",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67694",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67678",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67684",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67694",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67648) · [`00b67650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67650) · [`00b67634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67634)
- 新版 `00b6768c`（命令位置の公開資料なし） · `00b67694`（命令位置の公開資料なし） · `00b67678`（命令位置の公開資料なし）

~~~diff
- 00b67648 ["INT_ADD", "register:40f0:8", ["const:b67648:8", "const:4:8"]]
- 00b67648 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6768c ["INT_ADD", "register:40f0:8", ["const:b6768c:8", "const:4:8"]]
+ 00b6768c ["CALL", null, ["callee:00bde090:8"]]
- 00b67648 bytes 7eda0194
+ 00b6768c bytes 81da0194
- 00b67650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b67650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b67694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67650 bytes 604604f9
+ 00b67694 bytes 606604f9
- 00b67634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b67634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b67678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67634 bytes 684644f9
+ 00b67678 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6faf1208fe1987cc69b2914d1f427eb"></a>

### [`00b67664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md) → [`00b676a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b676d8",
      "incomplete_value": true,
      "site": "00b676d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67694",
      "incomplete_value": true,
      "site": "00b67694",
      "value": [
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
      "definition_site": "00b676bc",
      "incomplete_value": true,
      "site": "00b676bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67678",
      "incomplete_value": true,
      "site": "00b67678",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b676c8",
      "incomplete_value": false,
      "site": "00b676d0",
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
    "old": {
      "definition_site": "00b67684",
      "incomplete_value": false,
      "site": "00b6768c",
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
            "const:5f9:8"
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
      "00b676b8",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b676c8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b676d8",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b676b8",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b676c8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b676d8",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6768c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b6768c) · [`00b67694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b67694) · [`00b67674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b67674)
- 新版 `00b676d0`（命令位置の公開資料なし） · `00b676d8`（命令位置の公開資料なし） · `00b676b8`（命令位置の公開資料なし）

~~~diff
- 00b6768c ["INT_ADD", "register:40f0:8", ["const:b6768c:8", "const:4:8"]]
- 00b6768c ["CALL", null, ["callee:00bde090:8"]]
+ 00b676d0 ["INT_ADD", "register:40f0:8", ["const:b676d0:8", "const:4:8"]]
+ 00b676d0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6768c bytes 6dda0194
+ 00b676d0 bytes 70da0194
- 00b67694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b67694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b676d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b676d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67694 bytes 604604f9
+ 00b676d8 bytes 606604f9
- 00b67674 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b67674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b676b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b676b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67674 bytes 684644f9
+ 00b676b8 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0697b96e9531c8423c8e5d75fc374fe9"></a>

### [`00b676a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md) → [`00b676ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6771c",
      "incomplete_value": true,
      "site": "00b6771c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676d8",
      "incomplete_value": true,
      "site": "00b676d8",
      "value": [
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
      "definition_site": "00b67700",
      "incomplete_value": true,
      "site": "00b67700",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676bc",
      "incomplete_value": true,
      "site": "00b676bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67708",
      "incomplete_value": false,
      "site": "00b67714",
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
    "old": {
      "definition_site": "00b676c4",
      "incomplete_value": false,
      "site": "00b676d0",
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
            "const:5f9:8"
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
      "00b676fc",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67708",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b6771c",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b676fc",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67708",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b6771c",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b676d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676d0) · [`00b676d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676d8) · [`00b676b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676b8)
- 新版 `00b67714`（命令位置の公開資料なし） · `00b6771c`（命令位置の公開資料なし） · `00b676fc`（命令位置の公開資料なし）

~~~diff
- 00b676d0 ["INT_ADD", "register:40f0:8", ["const:b676d0:8", "const:4:8"]]
- 00b676d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67714 ["INT_ADD", "register:40f0:8", ["const:b67714:8", "const:4:8"]]
+ 00b67714 ["CALL", null, ["callee:00bde090:8"]]
- 00b676d0 bytes 5cda0194
+ 00b67714 bytes 5fda0194
- 00b676d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b676d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6771c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b6771c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b676d8 bytes 604604f9
+ 00b6771c bytes 606604f9
- 00b676b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b676b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b676fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b676fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b676b8 bytes 684644f9
+ 00b676fc bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bafe5c4ea3b490724c4b44df35bec811"></a>

### [`00b676f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md) → [`00b6773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67794",
      "incomplete_value": true,
      "site": "00b67794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67750",
      "incomplete_value": true,
      "site": "00b67750",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67770",
      "incomplete_value": true,
      "site": "00b6777c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b6772c",
      "incomplete_value": true,
      "site": "00b67738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:888:8"
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
      "00b67750",
      "READ",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67770",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67794",
      "WRITE",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67750",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67770",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67794",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6770c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b6770c) · [`00b67738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b67738) · [`00b67750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b67750)
- 新版 `00b67750`（命令位置の公開資料なし） · `00b6777c`（命令位置の公開資料なし） · `00b67794`（命令位置の公開資料なし）

~~~diff
- 00b6770c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:890:8"]]
- 00b6770c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6770c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67750 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b67750 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67750 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6770c bytes a8426239
+ 00b67750 bytes a8426339
- 00b67738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67738 ["INT_ADD", "register:40f0:8", ["const:b67738:8", "const:4:8"]]
- 00b67738 ["CALLIND", null, ["register:0:8"]]
+ 00b6777c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6777c ["INT_ADD", "register:40f0:8", ["const:b6777c:8", "const:4:8"]]
+ 00b6777c ["CALLIND", null, ["register:0:8"]]
- 00b67738 bytes 00013fd6
+ 00b6777c bytes 00013fd6
- 00b67750 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67750 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
- 00b67750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67794 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67794 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b67794 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67750 bytes a0422239
+ 00b67794 bytes a0422339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc4f9dd76bda569814edd02d3ce0ea7"></a>

### [`00b67764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md) → [`00b677a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b677e4",
      "incomplete_value": true,
      "site": "00b677e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677a0",
      "incomplete_value": true,
      "site": "00b677a0",
      "value": [
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
      "definition_site": "00b67804",
      "incomplete_value": true,
      "site": "00b67804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677c0",
      "incomplete_value": true,
      "site": "00b677c0",
      "value": [
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
      "definition_site": "00b677c0",
      "incomplete_value": true,
      "site": "00b677c0",
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
      "definition_site": "00b6777c",
      "incomplete_value": true,
      "site": "00b6777c",
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
      "00b677bc",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b677c8",
      "READ",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b677e4",
      "WRITE",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b677bc",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b677c8",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b677e4",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b67778) · [`00b677a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b677a0) · [`00b677bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b677bc)
- 新版 `00b677bc`（命令位置の公開資料なし） · `00b677e4`（命令位置の公開資料なし） · `00b67800`（命令位置の公開資料なし）

~~~diff
- 00b67778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b67778 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b677bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b677bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67778 bytes 814644f9
+ 00b677bc bytes 816644f9
- 00b677a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b677a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b677a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
- 00b677a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b677e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b677e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b677e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b677e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b677a0 bytes bf422239
+ 00b677e4 bytes bf422339
- 00b677bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b677bc ["INT_ADD", "register:40f0:8", ["const:b677bc:8", "const:4:8"]]
- 00b677bc ["CALLIND", null, ["register:0:8"]]
+ 00b67800 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67800 ["INT_ADD", "register:40f0:8", ["const:b67800:8", "const:4:8"]]
+ 00b67800 ["CALLIND", null, ["register:0:8"]]
- 00b677bc bytes 00013fd6
+ 00b67800 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1e5986fb4cc0972f595e64c9146b62"></a>

### [`00b677d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md) → [`00b67818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67858",
      "incomplete_value": true,
      "site": "00b67858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67814",
      "incomplete_value": true,
      "site": "00b67814",
      "value": [
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
      "definition_site": "00b67834",
      "incomplete_value": true,
      "site": "00b67834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677f0",
      "incomplete_value": true,
      "site": "00b677f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6783c",
      "incomplete_value": false,
      "site": "00b67850",
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
    "old": {
      "definition_site": "00b677f8",
      "incomplete_value": false,
      "site": "00b6780c",
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
            "const:5f9:8"
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
      "00b6782c",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6783c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67858",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6782c",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6783c",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67858",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b6780c) · [`00b67814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b67814) · [`00b677e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b677e8)
- 新版 `00b67850`（命令位置の公開資料なし） · `00b67858`（命令位置の公開資料なし） · `00b6782c`（命令位置の公開資料なし）

~~~diff
- 00b6780c ["INT_ADD", "register:40f0:8", ["const:b6780c:8", "const:4:8"]]
- 00b6780c ["CALL", null, ["callee:00bde090:8"]]
+ 00b67850 ["INT_ADD", "register:40f0:8", ["const:b67850:8", "const:4:8"]]
+ 00b67850 ["CALL", null, ["callee:00bde090:8"]]
- 00b6780c bytes 0dda0194
+ 00b67850 bytes 10da0194
- 00b67814 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b67814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b67858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67814 bytes 804604f9
+ 00b67858 bytes 806604f9
- 00b677e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b677e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6782c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b6782c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b677e8 bytes 814644f9
+ 00b6782c bytes 816644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3657a97be0d758522965f909c2d0a6"></a>

### [`00b67844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md) → [`00b67888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b678a4",
      "incomplete_value": false,
      "site": "00b678a8",
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
      "definition_site": "00b67860",
      "incomplete_value": false,
      "site": "00b67864",
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
      "definition_site": "00b678b4",
      "incomplete_value": true,
      "site": "00b678c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67870",
      "incomplete_value": true,
      "site": "00b6787c",
      "value": [
        "LOAD",
        "8",
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
      "00b678a4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b678b4",
      "DATA",
      [
        "storage",
        "010a1898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b678a4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b678b4",
      "DATA",
      [
        "storage",
        "010a18d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b67864) · [`00b67860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b67860) · [`00b6786c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b6786c)
- 新版 `00b678a8`（命令位置の公開資料なし） · `00b678a4`（命令位置の公開資料なし） · `00b678b0`（命令位置の公開資料なし）

~~~diff
- 00b67864 ["INT_ADD", "register:40f0:8", ["const:b67864:8", "const:4:8"]]
- 00b67864 ["CALL", null, ["callee:00bde180:8"]]
+ 00b678a8 ["INT_ADD", "register:40f0:8", ["const:b678a8:8", "const:4:8"]]
+ 00b678a8 ["CALL", null, ["callee:00bde180:8"]]
- 00b67864 bytes 33da0194
+ 00b678a8 bytes 36da0194
- 00b67860 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b67860 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67860 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67860 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b678a4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b678a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b678a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b678a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67860 bytes 00501791
+ 00b678a4 bytes 001c1591
- 00b6786c ["COPY", "tmp:0:8", ["const:898:8"]]
- 00b6786c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6786c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6786c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b678b0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00b678b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b678b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b678b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6786c bytes 08612291
+ 00b678b0 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d0398528288b7076cc7dd2378499d15"></a>

### [`00b67880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md) → [`00b678c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67904",
      "incomplete_value": true,
      "site": "00b67904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b678c0",
      "incomplete_value": true,
      "site": "00b678c0",
      "value": [
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
      "definition_site": "00b678e0",
      "incomplete_value": true,
      "site": "00b678e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6789c",
      "incomplete_value": true,
      "site": "00b6789c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b678e8",
      "incomplete_value": false,
      "site": "00b678fc",
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
    "old": {
      "definition_site": "00b678a4",
      "incomplete_value": false,
      "site": "00b678b8",
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
            "const:5f9:8"
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
      "00b678d8",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b678e8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67904",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b678d8",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b678e8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67904",
      "WRITE",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b678b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b678b8) · [`00b678c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b678c0) · [`00b67894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b67894)
- 新版 `00b678fc`（命令位置の公開資料なし） · `00b67904`（命令位置の公開資料なし） · `00b678d8`（命令位置の公開資料なし）

~~~diff
- 00b678b8 ["INT_ADD", "register:40f0:8", ["const:b678b8:8", "const:4:8"]]
- 00b678b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b678fc ["INT_ADD", "register:40f0:8", ["const:b678fc:8", "const:4:8"]]
+ 00b678fc ["CALL", null, ["callee:00bde090:8"]]
- 00b678b8 bytes e2d90194
+ 00b678fc bytes e5d90194
- 00b678c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b678c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67904 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b67904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b678c0 bytes 804604f9
+ 00b67904 bytes 806604f9
- 00b67894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b67894 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b678d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b678d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67894 bytes 814644f9
+ 00b678d8 bytes 816644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4208b2364d64e9cb224bffdd12be5570"></a>

### [`00b678f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md) → [`00b67934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67950",
      "incomplete_value": false,
      "site": "00b67954",
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
      "definition_site": "00b6790c",
      "incomplete_value": false,
      "site": "00b67910",
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
      "definition_site": "00b67960",
      "incomplete_value": true,
      "site": "00b6796c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6791c",
      "incomplete_value": true,
      "site": "00b67928",
      "value": [
        "LOAD",
        "8",
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
      "00b67950",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67960",
      "DATA",
      [
        "storage",
        "010a18b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67950",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67960",
      "DATA",
      [
        "storage",
        "010a18f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b67910) · [`00b6790c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b6790c) · [`00b67918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b67918)
- 新版 `00b67954`（命令位置の公開資料なし） · `00b67950`（命令位置の公開資料なし） · `00b6795c`（命令位置の公開資料なし）

~~~diff
- 00b67910 ["INT_ADD", "register:40f0:8", ["const:b67910:8", "const:4:8"]]
- 00b67910 ["CALL", null, ["callee:00bde180:8"]]
+ 00b67954 ["INT_ADD", "register:40f0:8", ["const:b67954:8", "const:4:8"]]
+ 00b67954 ["CALL", null, ["callee:00bde180:8"]]
- 00b67910 bytes 08da0194
+ 00b67954 bytes 0bda0194
- 00b6790c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6790c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6790c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6790c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67950 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b67950 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67950 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67950 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6790c bytes 00fc1991
+ 00b67950 bytes 00c81791
- 00b67918 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 00b67918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6795c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00b6795c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6795c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6795c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67918 bytes 08c12291
+ 00b6795c bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3aa0ac6bed755aa1e4045fd8071cd63"></a>

### [`00b6792c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md) → [`00b67970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b6799c",
      "incomplete_value": true,
      "site": "00b6799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67958",
      "incomplete_value": true,
      "site": "00b67958",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67984",
      "incomplete_value": true,
      "site": "00b67984",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67940",
      "incomplete_value": true,
      "site": "00b67940",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67990",
      "incomplete_value": false,
      "site": "00b67994",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6794c",
      "incomplete_value": false,
      "site": "00b67950",
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
            "const:74a:8"
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
      "00b67980",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67990",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b6799c",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67980",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67990",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b6799c",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b67950) · [`00b67958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b67958) · [`00b6793c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b6793c)
- 新版 `00b67994`（命令位置の公開資料なし） · `00b6799c`（命令位置の公開資料なし） · `00b67980`（命令位置の公開資料なし）

~~~diff
- 00b67950 ["INT_ADD", "register:40f0:8", ["const:b67950:8", "const:4:8"]]
- 00b67950 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67994 ["INT_ADD", "register:40f0:8", ["const:b67994:8", "const:4:8"]]
+ 00b67994 ["CALL", null, ["callee:00bde090:8"]]
- 00b67950 bytes bcd90194
+ 00b67994 bytes bfd90194
- 00b67958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b67958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6799c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b6799c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67958 bytes 605e04f9
+ 00b6799c bytes 607e04f9
- 00b6793c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b6793c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67980 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b67980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6793c bytes 685e44f9
+ 00b67980 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f6dcd30a71df920fb113bdd973c886"></a>

### [`00b6796c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md) → [`00b679b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b679dc",
      "incomplete_value": true,
      "site": "00b679dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67998",
      "incomplete_value": true,
      "site": "00b67998",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b679c4",
      "incomplete_value": true,
      "site": "00b679c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67980",
      "incomplete_value": true,
      "site": "00b67980",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b679cc",
      "incomplete_value": false,
      "site": "00b679d4",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67988",
      "incomplete_value": false,
      "site": "00b67990",
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
            "const:74a:8"
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
      "00b679c0",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b679cc",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b679dc",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b679c0",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b679cc",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b679dc",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b67990) · [`00b67998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b67998) · [`00b6797c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b6797c)
- 新版 `00b679d4`（命令位置の公開資料なし） · `00b679dc`（命令位置の公開資料なし） · `00b679c0`（命令位置の公開資料なし）

~~~diff
- 00b67990 ["INT_ADD", "register:40f0:8", ["const:b67990:8", "const:4:8"]]
- 00b67990 ["CALL", null, ["callee:00bde090:8"]]
+ 00b679d4 ["INT_ADD", "register:40f0:8", ["const:b679d4:8", "const:4:8"]]
+ 00b679d4 ["CALL", null, ["callee:00bde090:8"]]
- 00b67990 bytes acd90194
+ 00b679d4 bytes afd90194
- 00b67998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b67998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b679dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b679dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67998 bytes 605e04f9
+ 00b679dc bytes 607e04f9
- 00b6797c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b6797c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b679c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b679c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6797c bytes 685e44f9
+ 00b679c0 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-216e4174214c4a79c82c42b892d6a7f5"></a>

### [`00b679ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md) → [`00b679f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b67a20",
      "incomplete_value": true,
      "site": "00b67a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679dc",
      "incomplete_value": true,
      "site": "00b679dc",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67a04",
      "incomplete_value": true,
      "site": "00b67a04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679c0",
      "incomplete_value": true,
      "site": "00b679c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67a10",
      "incomplete_value": false,
      "site": "00b67a18",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679cc",
      "incomplete_value": false,
      "site": "00b679d4",
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
            "const:74a:8"
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
      "00b67a00",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a10",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b67a20",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67a00",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a10",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b67a20",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b679d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679d4) · [`00b679dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679dc) · [`00b679bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679bc)
- 新版 `00b67a18`（命令位置の公開資料なし） · `00b67a20`（命令位置の公開資料なし） · `00b67a00`（命令位置の公開資料なし）

~~~diff
- 00b679d4 ["INT_ADD", "register:40f0:8", ["const:b679d4:8", "const:4:8"]]
- 00b679d4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67a18 ["INT_ADD", "register:40f0:8", ["const:b67a18:8", "const:4:8"]]
+ 00b67a18 ["CALL", null, ["callee:00bde090:8"]]
- 00b679d4 bytes 9bd90194
+ 00b67a18 bytes 9ed90194
- 00b679dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b679dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b67a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b679dc bytes 605e04f9
+ 00b67a20 bytes 607e04f9
- 00b679bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b679bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b67a00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b679bc bytes 685e44f9
+ 00b67a00 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9c6cc1ef5b7610f263719bca8a15b8"></a>

### [`00b679f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md) → [`00b67a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a34.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67a64",
      "incomplete_value": true,
      "site": "00b67a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a20",
      "incomplete_value": true,
      "site": "00b67a20",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67a48",
      "incomplete_value": true,
      "site": "00b67a48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a04",
      "incomplete_value": true,
      "site": "00b67a04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67a50",
      "incomplete_value": false,
      "site": "00b67a5c",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a0c",
      "incomplete_value": false,
      "site": "00b67a18",
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
            "const:74a:8"
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
      "00b67a44",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a50",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b67a64",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67a44",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a50",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b67a64",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a18) · [`00b67a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a20) · [`00b67a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a00)
- 新版 `00b67a5c`（命令位置の公開資料なし） · `00b67a64`（命令位置の公開資料なし） · `00b67a44`（命令位置の公開資料なし）

~~~diff
- 00b67a18 ["INT_ADD", "register:40f0:8", ["const:b67a18:8", "const:4:8"]]
- 00b67a18 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67a5c ["INT_ADD", "register:40f0:8", ["const:b67a5c:8", "const:4:8"]]
+ 00b67a5c ["CALL", null, ["callee:00bde090:8"]]
- 00b67a18 bytes 8ad90194
+ 00b67a5c bytes 8dd90194
- 00b67a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b67a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b67a64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67a20 bytes 605e04f9
+ 00b67a64 bytes 607e04f9
- 00b67a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00b67a00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00b67a44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67a00 bytes 685e44f9
+ 00b67a44 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe90bb56141dada3a4766de07db0b76a"></a>

### [`00b67a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md) → [`00b67a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67a84.md) _ZN8firebase4auth21oauthprovider_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67adc",
      "incomplete_value": true,
      "site": "00b67adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a98",
      "incomplete_value": true,
      "site": "00b67a98",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67ab8",
      "incomplete_value": true,
      "site": "00b67ac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a74",
      "incomplete_value": true,
      "site": "00b67a80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
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
      "00b67a98",
      "READ",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67ab8",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67adc",
      "WRITE",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67a98",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67ab8",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67adc",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a54) · [`00b67a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a80) · [`00b67a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a98)
- 新版 `00b67a98`（命令位置の公開資料なし） · `00b67ac4`（命令位置の公開資料なし） · `00b67adc`（命令位置の公開資料なし）

~~~diff
- 00b67a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8c0:8"]]
- 00b67a54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b67a54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67a98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:900:8"]]
+ 00b67a98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67a98 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b67a54 bytes a8026339
+ 00b67a98 bytes a8026439
- 00b67a80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67a80 ["INT_ADD", "register:40f0:8", ["const:b67a80:8", "const:4:8"]]
- 00b67a80 ["CALLIND", null, ["register:0:8"]]
+ 00b67ac4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67ac4 ["INT_ADD", "register:40f0:8", ["const:b67ac4:8", "const:4:8"]]
+ 00b67ac4 ["CALLIND", null, ["register:0:8"]]
- 00b67a80 bytes 00013fd6
+ 00b67ac4 bytes 00013fd6
- 00b67a98 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67a98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8c0:8"]]
- 00b67a98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67adc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67adc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:900:8"]]
+ 00b67adc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67a98 bytes a0022339
+ 00b67adc bytes a0022439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9484a90c4a1715381d47debc06f711"></a>

### [`00b67aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md) → [`00b67af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67af0.md) _ZN8firebase4auth21oauthprovider_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b67b2c",
      "incomplete_value": true,
      "site": "00b67b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ae8",
      "incomplete_value": true,
      "site": "00b67ae8",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67b4c",
      "incomplete_value": true,
      "site": "00b67b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b08",
      "incomplete_value": true,
      "site": "00b67b08",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67b08",
      "incomplete_value": true,
      "site": "00b67b08",
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
      "definition_site": "00b67ac4",
      "incomplete_value": true,
      "site": "00b67ac4",
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
      "00b67b04",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b10",
      "READ",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67b2c",
      "WRITE",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67b04",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b10",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67b2c",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67ac0) · [`00b67ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67ae8) · [`00b67b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67b04)
- 新版 `00b67b04`（命令位置の公開資料なし） · `00b67b2c`（命令位置の公開資料なし） · `00b67b48`（命令位置の公開資料なし）

~~~diff
- 00b67ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00b67ac0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67b04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00b67b04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67ac0 bytes 815e44f9
+ 00b67b04 bytes 817e44f9
- 00b67ae8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67ae8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67ae8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8c0:8"]]
- 00b67ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67b2c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67b2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67b2c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
+ 00b67b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67ae8 bytes bf022339
+ 00b67b2c bytes bf022439
- 00b67b04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67b04 ["INT_ADD", "register:40f0:8", ["const:b67b04:8", "const:4:8"]]
- 00b67b04 ["CALLIND", null, ["register:0:8"]]
+ 00b67b48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67b48 ["INT_ADD", "register:40f0:8", ["const:b67b48:8", "const:4:8"]]
+ 00b67b48 ["CALLIND", null, ["register:0:8"]]
- 00b67b04 bytes 00013fd6
+ 00b67b48 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6954caa7b16e127d49dbf5267d8ed8fe"></a>

### [`00b67b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md) → [`00b67b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67b60.md) _ZN8firebase4auth21oauthprovider_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67ba0",
      "incomplete_value": true,
      "site": "00b67ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b5c",
      "incomplete_value": true,
      "site": "00b67b5c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67b7c",
      "incomplete_value": true,
      "site": "00b67b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b38",
      "incomplete_value": true,
      "site": "00b67b38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67b84",
      "incomplete_value": false,
      "site": "00b67b98",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b40",
      "incomplete_value": false,
      "site": "00b67b54",
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
            "const:74a:8"
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
      "00b67b74",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b84",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b67ba0",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67b74",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b84",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b67ba0",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b54) · [`00b67b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b5c) · [`00b67b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b30)
- 新版 `00b67b98`（命令位置の公開資料なし） · `00b67ba0`（命令位置の公開資料なし） · `00b67b74`（命令位置の公開資料なし）

~~~diff
- 00b67b54 ["INT_ADD", "register:40f0:8", ["const:b67b54:8", "const:4:8"]]
- 00b67b54 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67b98 ["INT_ADD", "register:40f0:8", ["const:b67b98:8", "const:4:8"]]
+ 00b67b98 ["CALL", null, ["callee:00bde090:8"]]
- 00b67b54 bytes 3bd90194
+ 00b67b98 bytes 3ed90194
- 00b67b5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00b67b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00b67ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67b5c bytes 805e04f9
+ 00b67ba0 bytes 807e04f9
- 00b67b30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00b67b30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00b67b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67b30 bytes 815e44f9
+ 00b67b74 bytes 817e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7950afab3b4c143868950688795d61a"></a>

### [`00b67b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md) → [`00b67bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67bd0.md) _ZN8firebase4auth21oauthprovider_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67bec",
      "incomplete_value": false,
      "site": "00b67bf0",
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
      "definition_site": "00b67ba8",
      "incomplete_value": false,
      "site": "00b67bac",
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
      "definition_site": "00b67bfc",
      "incomplete_value": true,
      "site": "00b67c08",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67bb8",
      "incomplete_value": true,
      "site": "00b67bc4",
      "value": [
        "LOAD",
        "8",
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
      "00b67bec",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67bfc",
      "DATA",
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
      "00b67bec",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67bfc",
      "DATA",
      [
        "storage",
        "010a1908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67bac) · [`00b67ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67ba8) · [`00b67bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67bb4)
- 新版 `00b67bf0`（命令位置の公開資料なし） · `00b67bec`（命令位置の公開資料なし） · `00b67bf8`（命令位置の公開資料なし）

~~~diff
- 00b67bac ["INT_ADD", "register:40f0:8", ["const:b67bac:8", "const:4:8"]]
- 00b67bac ["CALL", null, ["callee:00bde180:8"]]
+ 00b67bf0 ["INT_ADD", "register:40f0:8", ["const:b67bf0:8", "const:4:8"]]
+ 00b67bf0 ["CALL", null, ["callee:00bde180:8"]]
- 00b67bac bytes 61d90194
+ 00b67bf0 bytes 64d90194
- 00b67ba8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b67ba8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ba8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ba8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67bec ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b67bec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67bec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67bec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67ba8 bytes 00501791
+ 00b67bec bytes 001c1591
- 00b67bb4 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00b67bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67bf8 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00b67bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67bb4 bytes 08212391
+ 00b67bf8 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f9a774706e86fa34b72db8d60c29fa2"></a>

### [`00b67bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md) → [`00b67c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c0c.md) _ZN8firebase4auth21oauthprovider_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67c4c",
      "incomplete_value": true,
      "site": "00b67c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c08",
      "incomplete_value": true,
      "site": "00b67c08",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67c28",
      "incomplete_value": true,
      "site": "00b67c28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67be4",
      "incomplete_value": true,
      "site": "00b67be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67c30",
      "incomplete_value": false,
      "site": "00b67c44",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67bec",
      "incomplete_value": false,
      "site": "00b67c00",
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
            "const:74a:8"
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
      "00b67c20",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c30",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ],
    [
      "00b67c4c",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67c20",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c30",
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      "00b67c4c",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67c00) · [`00b67c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67c08) · [`00b67bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67bdc)
- 新版 `00b67c44`（命令位置の公開資料なし） · `00b67c4c`（命令位置の公開資料なし） · `00b67c20`（命令位置の公開資料なし）

~~~diff
- 00b67c00 ["INT_ADD", "register:40f0:8", ["const:b67c00:8", "const:4:8"]]
- 00b67c00 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67c44 ["INT_ADD", "register:40f0:8", ["const:b67c44:8", "const:4:8"]]
+ 00b67c44 ["CALL", null, ["callee:00bde090:8"]]
- 00b67c00 bytes 10d90194
+ 00b67c44 bytes 13d90194
- 00b67c08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00b67c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67c4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00b67c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67c08 bytes 805e04f9
+ 00b67c4c bytes 807e04f9
- 00b67bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00b67bdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00b67c20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67bdc bytes 815e44f9
+ 00b67c20 bytes 817e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a9c5e690e5d3cba0e03681647239f4a"></a>

### [`00b67c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md) → [`00b67c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67c7c.md) _ZN8firebase4auth21oauthprovider_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67c98",
      "incomplete_value": false,
      "site": "00b67c9c",
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
      "definition_site": "00b67c54",
      "incomplete_value": false,
      "site": "00b67c58",
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
      "definition_site": "00b67ca8",
      "incomplete_value": true,
      "site": "00b67cb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67c64",
      "incomplete_value": true,
      "site": "00b67c70",
      "value": [
        "LOAD",
        "8",
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
      "00b67c98",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67ca8",
      "DATA",
      [
        "storage",
        "010a18e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67c98",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67ca8",
      "DATA",
      [
        "storage",
        "010a1920",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c58) · [`00b67c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c54) · [`00b67c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c60)
- 新版 `00b67c9c`（命令位置の公開資料なし） · `00b67c98`（命令位置の公開資料なし） · `00b67ca4`（命令位置の公開資料なし）

~~~diff
- 00b67c58 ["INT_ADD", "register:40f0:8", ["const:b67c58:8", "const:4:8"]]
- 00b67c58 ["CALL", null, ["callee:00bde180:8"]]
+ 00b67c9c ["INT_ADD", "register:40f0:8", ["const:b67c9c:8", "const:4:8"]]
+ 00b67c9c ["CALL", null, ["callee:00bde180:8"]]
- 00b67c58 bytes 36d90194
+ 00b67c9c bytes 39d90194
- 00b67c54 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b67c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67c98 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b67c98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67c98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67c98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67c54 bytes 00fc1991
+ 00b67c98 bytes 00c81791
- 00b67c60 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00b67c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67ca4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00b67ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67c60 bytes 08812391
+ 00b67ca4 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b2c7f2f79e40a32486ff19ac46320db"></a>

### [`00b67c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md) → [`00b67cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cb8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b67ce4",
      "incomplete_value": true,
      "site": "00b67ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ca0",
      "incomplete_value": true,
      "site": "00b67ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67ccc",
      "incomplete_value": true,
      "site": "00b67ccc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c88",
      "incomplete_value": true,
      "site": "00b67c88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67c88"
      ],
      [
        "FALL_THROUGH",
        "00b67ccc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67ccc",
      "incomplete_value": true,
      "site": "00b67ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c88",
      "incomplete_value": true,
      "site": "00b67ca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67cc8",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67ce4",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67cc8",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67ce4",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67ca0) · [`00b67c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67c84) · [`00b67c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67c98)
- 新版 `00b67ce4`（命令位置の公開資料なし） · `00b67cc8`（命令位置の公開資料なし） · `00b67cdc`（命令位置の公開資料なし）

~~~diff
- 00b67ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67ca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ce4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67ce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ca0 bytes 607604f9
+ 00b67ce4 bytes 609604f9
- 00b67c84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67c84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67cc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67cc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67c84 bytes 687644f9
+ 00b67cc8 bytes 689644f9
- 00b67c98 ["INT_ADD", "register:40f0:8", ["const:b67c98:8", "const:4:8"]]
- 00b67c98 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67cdc ["INT_ADD", "register:40f0:8", ["const:b67cdc:8", "const:4:8"]]
+ 00b67cdc ["CALL", null, ["callee:00bde090:8"]]
- 00b67c98 bytes ead80194
+ 00b67cdc bytes edd80194
~~~


<a id="compare-7688751d37465675bb1c19e2eb588d55"></a>

### [`00b67cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md) → [`00b67cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67cf8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b67d24",
      "incomplete_value": true,
      "site": "00b67d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ce0",
      "incomplete_value": true,
      "site": "00b67ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67d0c",
      "incomplete_value": true,
      "site": "00b67d0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67cc8",
      "incomplete_value": true,
      "site": "00b67cc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67cc8"
      ],
      [
        "FALL_THROUGH",
        "00b67d0c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67d0c",
      "incomplete_value": true,
      "site": "00b67d24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67cc8",
      "incomplete_value": true,
      "site": "00b67ce0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67d08",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d24",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67d08",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d24",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67ce0) · [`00b67cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67cc4) · [`00b67cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67cd8)
- 新版 `00b67d24`（命令位置の公開資料なし） · `00b67d08`（命令位置の公開資料なし） · `00b67d1c`（命令位置の公開資料なし）

~~~diff
- 00b67ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ce0 bytes 607604f9
+ 00b67d24 bytes 609604f9
- 00b67cc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67d08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67cc4 bytes 687644f9
+ 00b67d08 bytes 689644f9
- 00b67cd8 ["INT_ADD", "register:40f0:8", ["const:b67cd8:8", "const:4:8"]]
- 00b67cd8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67d1c ["INT_ADD", "register:40f0:8", ["const:b67d1c:8", "const:4:8"]]
+ 00b67d1c ["CALL", null, ["callee:00bde090:8"]]
- 00b67cd8 bytes dad80194
+ 00b67d1c bytes ddd80194
~~~


<a id="compare-ddca92f35d3a2ab04545df6fc02a79e3"></a>

### [`00b67cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md) → [`00b67d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d38.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b67d68",
      "incomplete_value": true,
      "site": "00b67d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d24",
      "incomplete_value": true,
      "site": "00b67d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67d4c",
      "incomplete_value": true,
      "site": "00b67d4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d08",
      "incomplete_value": true,
      "site": "00b67d08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67d08"
      ],
      [
        "FALL_THROUGH",
        "00b67d4c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67d4c",
      "incomplete_value": true,
      "site": "00b67d68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d08",
      "incomplete_value": true,
      "site": "00b67d24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67d48",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d68",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67d48",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d68",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d24) · [`00b67d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d04) · [`00b67d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d1c)
- 新版 `00b67d68`（命令位置の公開資料なし） · `00b67d48`（命令位置の公開資料なし） · `00b67d60`（命令位置の公開資料なし）

~~~diff
- 00b67d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67d24 bytes 607604f9
+ 00b67d68 bytes 609604f9
- 00b67d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67d04 bytes 687644f9
+ 00b67d48 bytes 689644f9
- 00b67d1c ["INT_ADD", "register:40f0:8", ["const:b67d1c:8", "const:4:8"]]
- 00b67d1c ["CALL", null, ["callee:00bde090:8"]]
+ 00b67d60 ["INT_ADD", "register:40f0:8", ["const:b67d60:8", "const:4:8"]]
+ 00b67d60 ["CALL", null, ["callee:00bde090:8"]]
- 00b67d1c bytes c9d80194
+ 00b67d60 bytes ccd80194
~~~


<a id="compare-4e0971703d3a28558de0b7711b66ecac"></a>

### [`00b67d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md) → [`00b67d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67d7c.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67dac",
      "incomplete_value": true,
      "site": "00b67dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d68",
      "incomplete_value": true,
      "site": "00b67d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67d90",
      "incomplete_value": true,
      "site": "00b67d90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67d4c"
      ],
      [
        "FALL_THROUGH",
        "00b67d90"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67d90",
      "incomplete_value": true,
      "site": "00b67dac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "site": "00b67d68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67d8c",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67dac",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67d8c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67dac",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d68) · [`00b67d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d48) · [`00b67d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d60)
- 新版 `00b67dac`（命令位置の公開資料なし） · `00b67d8c`（命令位置の公開資料なし） · `00b67da4`（命令位置の公開資料なし）

~~~diff
- 00b67d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67dac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67dac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67d68 bytes 607604f9
+ 00b67dac bytes 609604f9
- 00b67d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00b67d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:928:8"]]
+ 00b67d8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67d48 bytes 687644f9
+ 00b67d8c bytes 689644f9
- 00b67d60 ["INT_ADD", "register:40f0:8", ["const:b67d60:8", "const:4:8"]]
- 00b67d60 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67da4 ["INT_ADD", "register:40f0:8", ["const:b67da4:8", "const:4:8"]]
+ 00b67da4 ["CALL", null, ["callee:00bde090:8"]]
- 00b67d60 bytes b8d80194
+ 00b67da4 bytes bbd80194
~~~


<a id="compare-660ff242afa65eab2fc6f0e180a66800"></a>

### [`00b67d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md) → [`00b67dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67dcc.md) _ZN8firebase4auth31oauthprovider_credentialbuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67e24",
      "incomplete_value": true,
      "site": "00b67e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67de0",
      "incomplete_value": true,
      "site": "00b67de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "definition_site": "00b67e00",
      "incomplete_value": true,
      "site": "00b67e0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67dbc",
      "incomplete_value": true,
      "site": "00b67dc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
      "00b67de0",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e00",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e24",
      "WRITE",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67de0",
      "READ",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e00",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e24",
      "WRITE",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67d9c) · [`00b67dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67dc8) · [`00b67de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67de0)
- 新版 `00b67de0`（命令位置の公開資料なし） · `00b67e0c`（命令位置の公開資料なし） · `00b67e24`（命令位置の公開資料なし）

~~~diff
- 00b67d9c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
- 00b67d9c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b67d9c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67de0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:930:8"]]
+ 00b67de0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67de0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b67d9c bytes a8c26339
+ 00b67de0 bytes a8c26439
- 00b67dc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67dc8 ["INT_ADD", "register:40f0:8", ["const:b67dc8:8", "const:4:8"]]
- 00b67dc8 ["CALLIND", null, ["register:0:8"]]
+ 00b67e0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67e0c ["INT_ADD", "register:40f0:8", ["const:b67e0c:8", "const:4:8"]]
+ 00b67e0c ["CALLIND", null, ["register:0:8"]]
- 00b67dc8 bytes 00013fd6
+ 00b67e0c bytes 00013fd6
- 00b67de0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67de0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f0:8"]]
- 00b67de0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67e24 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67e24 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:930:8"]]
+ 00b67e24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67de0 bytes a0c22339
+ 00b67e24 bytes a0c22439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86194d20a357f8b4ed3d9c109b314eb"></a>

### [`00b67df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md) → [`00b67e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67e38.md) _ZN8firebase4auth31oauthprovider_credentialbuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b67e74",
      "incomplete_value": true,
      "site": "00b67e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e30",
      "incomplete_value": true,
      "site": "00b67e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "definition_site": "00b67e94",
      "incomplete_value": true,
      "site": "00b67e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e50",
      "incomplete_value": true,
      "site": "00b67e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67e50",
      "incomplete_value": true,
      "site": "00b67e50",
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
      "definition_site": "00b67e0c",
      "incomplete_value": true,
      "site": "00b67e0c",
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
      "00b67e4c",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e58",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e74",
      "WRITE",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67e4c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e58",
      "READ",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e74",
      "WRITE",
      [
        "storage",
        "010a1930",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e08) · [`00b67e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e30) · [`00b67e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e4c)
- 新版 `00b67e4c`（命令位置の公開資料なし） · `00b67e74`（命令位置の公開資料なし） · `00b67e90`（命令位置の公開資料なし）

~~~diff
- 00b67e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00b67e08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67e4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00b67e4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67e08 bytes 817644f9
+ 00b67e4c bytes 819644f9
- 00b67e30 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67e30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67e30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f0:8"]]
- 00b67e30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67e74 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67e74 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67e74 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:930:8"]]
+ 00b67e74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67e30 bytes bfc22339
+ 00b67e74 bytes bfc22439
- 00b67e4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67e4c ["INT_ADD", "register:40f0:8", ["const:b67e4c:8", "const:4:8"]]
- 00b67e4c ["CALLIND", null, ["register:0:8"]]
+ 00b67e90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67e90 ["INT_ADD", "register:40f0:8", ["const:b67e90:8", "const:4:8"]]
+ 00b67e90 ["CALLIND", null, ["register:0:8"]]
- 00b67e4c bytes 00013fd6
+ 00b67e90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0e26ade0d3bbd039c71064ec0f33eab"></a>

### [`00b67e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md) → [`00b67ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67ea8.md) _ZN8firebase4auth31oauthprovider_credentialbuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67ee8",
      "incomplete_value": true,
      "site": "00b67ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ea4",
      "incomplete_value": true,
      "site": "00b67ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67ec4",
      "incomplete_value": true,
      "site": "00b67ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e80",
      "incomplete_value": true,
      "site": "00b67e80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67e80"
      ],
      [
        "FALL_THROUGH",
        "00b67ec4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67ec4",
      "incomplete_value": true,
      "site": "00b67ee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e80",
      "incomplete_value": true,
      "site": "00b67ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67ebc",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67ee8",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67efc",
      "PARAM",
      [
        "storage",
        "00c125e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b67ebc",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67ee8",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67efc",
      "PARAM",
      [
        "storage",
        "00c12638",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67ea4) · [`00b67e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67e78) · [`00b67e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67e9c)
- 新版 `00b67ee8`（命令位置の公開資料なし） · `00b67ebc`（命令位置の公開資料なし） · `00b67ee0`（命令位置の公開資料なし）

~~~diff
- 00b67ea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00b67ea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00b67ee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ea4 bytes 807604f9
+ 00b67ee8 bytes 809604f9
- 00b67e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00b67e78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67ebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00b67ebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67e78 bytes 817644f9
+ 00b67ebc bytes 819644f9
- 00b67e9c ["INT_ADD", "register:40f0:8", ["const:b67e9c:8", "const:4:8"]]
- 00b67e9c ["CALL", null, ["callee:00bde090:8"]]
+ 00b67ee0 ["INT_ADD", "register:40f0:8", ["const:b67ee0:8", "const:4:8"]]
+ 00b67ee0 ["CALL", null, ["callee:00bde090:8"]]
- 00b67e9c bytes 69d80194
+ 00b67ee0 bytes 6cd80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-101f6d6eb385d443f4096071ce2037d5"></a>

### [`00b67ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md) → [`00b67f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f18.md) _ZN8firebase4auth31oauthprovider_credentialbuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67f34",
      "incomplete_value": false,
      "site": "00b67f38",
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
      "definition_site": "00b67ef0",
      "incomplete_value": false,
      "site": "00b67ef4",
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
      "definition_site": "00b67f44",
      "incomplete_value": true,
      "site": "00b67f50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67f00",
      "incomplete_value": true,
      "site": "00b67f0c",
      "value": [
        "LOAD",
        "8",
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
      "00b67f34",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67f44",
      "DATA",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67f34",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67f44",
      "DATA",
      [
        "storage",
        "010a1938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67ef4) · [`00b67ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67ef0) · [`00b67efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67efc)
- 新版 `00b67f38`（命令位置の公開資料なし） · `00b67f34`（命令位置の公開資料なし） · `00b67f40`（命令位置の公開資料なし）

~~~diff
- 00b67ef4 ["INT_ADD", "register:40f0:8", ["const:b67ef4:8", "const:4:8"]]
- 00b67ef4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b67f38 ["INT_ADD", "register:40f0:8", ["const:b67f38:8", "const:4:8"]]
+ 00b67f38 ["CALL", null, ["callee:00bde180:8"]]
- 00b67ef4 bytes 8fd80194
+ 00b67f38 bytes 92d80194
- 00b67ef0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b67ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67f34 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b67f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67ef0 bytes 00501791
+ 00b67f34 bytes 001c1591
- 00b67efc ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00b67efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67f40 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00b67f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67efc bytes 08e12391
+ 00b67f40 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c85295c7781fd85ff933f81011db711"></a>

### [`00b67f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md) → [`00b67f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67f54.md) _ZN8firebase4auth31oauthprovider_credentialbuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67f94",
      "incomplete_value": true,
      "site": "00b67f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f50",
      "incomplete_value": true,
      "site": "00b67f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00b67f70",
      "incomplete_value": true,
      "site": "00b67f70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f2c",
      "incomplete_value": true,
      "site": "00b67f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b67f2c"
      ],
      [
        "FALL_THROUGH",
        "00b67f70"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67f70",
      "incomplete_value": true,
      "site": "00b67f94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f2c",
      "incomplete_value": true,
      "site": "00b67f50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b67f68",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67f94",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67fac",
      "PARAM",
      [
        "storage",
        "010a1918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67f68",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67f94",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67fac",
      "PARAM",
      [
        "storage",
        "010a1958",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f50) · [`00b67f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f24) · [`00b67f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f48)
- 新版 `00b67f94`（命令位置の公開資料なし） · `00b67f68`（命令位置の公開資料なし） · `00b67f8c`（命令位置の公開資料なし）

~~~diff
- 00b67f50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00b67f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00b67f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67f50 bytes 807604f9
+ 00b67f94 bytes 809604f9
- 00b67f24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00b67f24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:928:8"]]
+ 00b67f68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67f24 bytes 817644f9
+ 00b67f68 bytes 819644f9
- 00b67f48 ["INT_ADD", "register:40f0:8", ["const:b67f48:8", "const:4:8"]]
- 00b67f48 ["CALL", null, ["callee:00bde090:8"]]
+ 00b67f8c ["INT_ADD", "register:40f0:8", ["const:b67f8c:8", "const:4:8"]]
+ 00b67f8c ["CALL", null, ["callee:00bde090:8"]]
- 00b67f48 bytes 3ed80194
+ 00b67f8c bytes 41d80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908ed252225e012a8e834615a6e45520"></a>

### [`00b67f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md) → [`00b67fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67fc4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67fe0",
      "incomplete_value": false,
      "site": "00b67fe4",
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
      "definition_site": "00b67f9c",
      "incomplete_value": false,
      "site": "00b67fa0",
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
      "definition_site": "00b67ff0",
      "incomplete_value": true,
      "site": "00b67ffc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67fac",
      "incomplete_value": true,
      "site": "00b67fb8",
      "value": [
        "LOAD",
        "8",
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
      "00b67fe0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67ff0",
      "DATA",
      [
        "storage",
        "010a1918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67fe0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67ff0",
      "DATA",
      [
        "storage",
        "010a1958",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67fa0) · [`00b67f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67f9c) · [`00b67fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67fa8)
- 新版 `00b67fe4`（命令位置の公開資料なし） · `00b67fe0`（命令位置の公開資料なし） · `00b67fec`（命令位置の公開資料なし）

~~~diff
- 00b67fa0 ["INT_ADD", "register:40f0:8", ["const:b67fa0:8", "const:4:8"]]
- 00b67fa0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b67fe4 ["INT_ADD", "register:40f0:8", ["const:b67fe4:8", "const:4:8"]]
+ 00b67fe4 ["CALL", null, ["callee:00bde180:8"]]
- 00b67fa0 bytes 64d80194
+ 00b67fe4 bytes 67d80194
- 00b67f9c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b67f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67fe0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b67fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67f9c bytes 00fc1991
+ 00b67fe0 bytes 00c81791
- 00b67fa8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00b67fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67fec ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00b67fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67fa8 bytes 08612491
+ 00b67fec bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08463bda04b6b130a7f5efbabf470562"></a>

### [`00b67fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md) → [`00b68000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68000.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b6802c",
      "incomplete_value": true,
      "site": "00b6802c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fe8",
      "incomplete_value": true,
      "site": "00b67fe8",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b68014",
      "incomplete_value": true,
      "site": "00b68014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fd0",
      "incomplete_value": true,
      "site": "00b67fd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68020",
      "incomplete_value": false,
      "site": "00b68024",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fdc",
      "incomplete_value": false,
      "site": "00b67fe0",
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
            "const:fd8:8"
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
      "00b68010",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68020",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b6802c",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68010",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68020",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b6802c",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fe0) · [`00b67fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fe8) · [`00b67fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fcc)
- 新版 `00b68024`（命令位置の公開資料なし） · `00b6802c`（命令位置の公開資料なし） · `00b68010`（命令位置の公開資料なし）

~~~diff
- 00b67fe0 ["INT_ADD", "register:40f0:8", ["const:b67fe0:8", "const:4:8"]]
- 00b67fe0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68024 ["INT_ADD", "register:40f0:8", ["const:b68024:8", "const:4:8"]]
+ 00b68024 ["CALL", null, ["callee:00bde090:8"]]
- 00b67fe0 bytes 18d80194
+ 00b68024 bytes 1bd80194
- 00b67fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b67fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6802c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b6802c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67fe8 bytes 609204f9
+ 00b6802c bytes 60b204f9
- 00b67fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b67fcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b68010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67fcc bytes 689244f9
+ 00b68010 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83977e1d3219aaa5d92f8dd1cc12c0b5"></a>

### [`00b67ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md) → [`00b68040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68040.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6806c",
      "incomplete_value": true,
      "site": "00b6806c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68028",
      "incomplete_value": true,
      "site": "00b68028",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b68054",
      "incomplete_value": true,
      "site": "00b68054",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68010",
      "incomplete_value": true,
      "site": "00b68010",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6805c",
      "incomplete_value": false,
      "site": "00b68064",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68018",
      "incomplete_value": false,
      "site": "00b68020",
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
            "const:fd8:8"
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
      "00b68050",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6805c",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b6806c",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68050",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6805c",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b6806c",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b68020) · [`00b68028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b68028) · [`00b6800c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b6800c)
- 新版 `00b68064`（命令位置の公開資料なし） · `00b6806c`（命令位置の公開資料なし） · `00b68050`（命令位置の公開資料なし）

~~~diff
- 00b68020 ["INT_ADD", "register:40f0:8", ["const:b68020:8", "const:4:8"]]
- 00b68020 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68064 ["INT_ADD", "register:40f0:8", ["const:b68064:8", "const:4:8"]]
+ 00b68064 ["CALL", null, ["callee:00bde090:8"]]
- 00b68020 bytes 08d80194
+ 00b68064 bytes 0bd80194
- 00b68028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b68028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6806c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b6806c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68028 bytes 609204f9
+ 00b6806c bytes 60b204f9
- 00b6800c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b6800c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b68050 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6800c bytes 689244f9
+ 00b68050 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8acb4e012d28b1a397c29b593ee1fc05"></a>

### [`00b6803c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md) → [`00b68080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68080.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b680b0",
      "incomplete_value": true,
      "site": "00b680b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6806c",
      "incomplete_value": true,
      "site": "00b6806c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b68094",
      "incomplete_value": true,
      "site": "00b68094",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68050",
      "incomplete_value": true,
      "site": "00b68050",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b680a0",
      "incomplete_value": false,
      "site": "00b680a8",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6805c",
      "incomplete_value": false,
      "site": "00b68064",
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
            "const:fd8:8"
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
      "00b68090",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b680a0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b680b0",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68090",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b680a0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b680b0",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b68064) · [`00b6806c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b6806c) · [`00b6804c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b6804c)
- 新版 `00b680a8`（命令位置の公開資料なし） · `00b680b0`（命令位置の公開資料なし） · `00b68090`（命令位置の公開資料なし）

~~~diff
- 00b68064 ["INT_ADD", "register:40f0:8", ["const:b68064:8", "const:4:8"]]
- 00b68064 ["CALL", null, ["callee:00bde090:8"]]
+ 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
+ 00b680a8 ["CALL", null, ["callee:00bde090:8"]]
- 00b68064 bytes f7d70194
+ 00b680a8 bytes fad70194
- 00b6806c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b6806c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b680b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b680b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6806c bytes 609204f9
+ 00b680b0 bytes 60b204f9
- 00b6804c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b6804c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b68090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6804c bytes 689244f9
+ 00b68090 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e900668119b1d3a796cf5cbed50dccc"></a>

### [`00b68080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md) → [`00b680c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b680c4.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b680f4",
      "incomplete_value": true,
      "site": "00b680f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b680b0",
      "incomplete_value": true,
      "site": "00b680b0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b680d8",
      "incomplete_value": true,
      "site": "00b680d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68094",
      "incomplete_value": true,
      "site": "00b68094",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b680e0",
      "incomplete_value": false,
      "site": "00b680ec",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6809c",
      "incomplete_value": false,
      "site": "00b680a8",
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
            "const:fd8:8"
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
      "00b680d4",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b680e0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b680f4",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b680d4",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b680e0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b680f4",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b680a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b680a8) · [`00b680b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b680b0) · [`00b68090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b68090)
- 新版 `00b680ec`（命令位置の公開資料なし） · `00b680f4`（命令位置の公開資料なし） · `00b680d4`（命令位置の公開資料なし）

~~~diff
- 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
- 00b680a8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b680ec ["INT_ADD", "register:40f0:8", ["const:b680ec:8", "const:4:8"]]
+ 00b680ec ["CALL", null, ["callee:00bde090:8"]]
- 00b680a8 bytes e6d70194
+ 00b680ec bytes e9d70194
- 00b680b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b680b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b680f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b680f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b680b0 bytes 609204f9
+ 00b680f4 bytes 60b204f9
- 00b68090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b68090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b680d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b680d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68090 bytes 689244f9
+ 00b680d4 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63f449c8c1cc25017b53fba935dd6c8e"></a>

### [`00b680d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md) → [`00b68114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68114.md) _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6816c",
      "incomplete_value": true,
      "site": "00b6816c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68128",
      "incomplete_value": true,
      "site": "00b68128",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68148",
      "incomplete_value": true,
      "site": "00b68154",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68104",
      "incomplete_value": true,
      "site": "00b68110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
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
      "00b68128",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68148",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6816c",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68128",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68148",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6816c",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b680e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b680e4) · [`00b68110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b68110) · [`00b68128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b68128)
- 新版 `00b68128`（命令位置の公開資料なし） · `00b68154`（命令位置の公開資料なし） · `00b6816c`（命令位置の公開資料なし）

~~~diff
- 00b680e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:928:8"]]
- 00b680e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b680e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b68128 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
+ 00b68128 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b68128 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b680e4 bytes a8a26439
+ 00b68128 bytes a8a26539
- 00b68110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68110 ["INT_ADD", "register:40f0:8", ["const:b68110:8", "const:4:8"]]
- 00b68110 ["CALLIND", null, ["register:0:8"]]
+ 00b68154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68154 ["INT_ADD", "register:40f0:8", ["const:b68154:8", "const:4:8"]]
+ 00b68154 ["CALLIND", null, ["register:0:8"]]
- 00b68110 bytes 00013fd6
+ 00b68154 bytes 00013fd6
- 00b68128 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68128 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
- 00b68128 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6816c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6816c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:968:8"]]
+ 00b6816c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68128 bytes a0a22439
+ 00b6816c bytes a0a22539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3660f661446b152635f0cde1b794b0c2"></a>

### [`00b6813c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md) → [`00b68180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68180.md) _ZN8firebase4auth8auth_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b681bc",
      "incomplete_value": true,
      "site": "00b681bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68178",
      "incomplete_value": true,
      "site": "00b68178",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b681dc",
      "incomplete_value": true,
      "site": "00b681dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68198",
      "incomplete_value": true,
      "site": "00b68198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "definition_site": "00b68198",
      "incomplete_value": true,
      "site": "00b68198",
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
      "definition_site": "00b68154",
      "incomplete_value": true,
      "site": "00b68154",
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
      "00b68194",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681a0",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b681bc",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68194",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681a0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ],
    [
      "00b681bc",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68150) · [`00b68178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68178) · [`00b68194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68194)
- 新版 `00b68194`（命令位置の公開資料なし） · `00b681bc`（命令位置の公開資料なし） · `00b681d8`（命令位置の公開資料なし）

~~~diff
- 00b68150 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b68150 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68194 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b68194 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68150 bytes 819244f9
+ 00b68194 bytes 81b244f9
- 00b68178 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68178 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68178 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
- 00b68178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b681bc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b681bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b681bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
+ 00b681bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68178 bytes bfa22439
+ 00b681bc bytes bfa22539
- 00b68194 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68194 ["INT_ADD", "register:40f0:8", ["const:b68194:8", "const:4:8"]]
- 00b68194 ["CALLIND", null, ["register:0:8"]]
+ 00b681d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b681d8 ["INT_ADD", "register:40f0:8", ["const:b681d8:8", "const:4:8"]]
+ 00b681d8 ["CALLIND", null, ["register:0:8"]]
- 00b68194 bytes 00013fd6
+ 00b681d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c1cb6c3703b688ca46fee56513d0cf8"></a>

### [`00b681ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md) → [`00b681f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b681f0.md) _ZN8firebase4auth8auth_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68230",
      "incomplete_value": true,
      "site": "00b68230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681ec",
      "incomplete_value": true,
      "site": "00b681ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "definition_site": "00b6820c",
      "incomplete_value": true,
      "site": "00b6820c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681c8",
      "incomplete_value": true,
      "site": "00b681c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68214",
      "incomplete_value": false,
      "site": "00b68228",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681d0",
      "incomplete_value": false,
      "site": "00b681e4",
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
            "const:fd8:8"
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
      "00b68204",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68214",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b68230",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68204",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68214",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b68230",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b681e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681e4) · [`00b681ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681ec) · [`00b681c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681c0)
- 新版 `00b68228`（命令位置の公開資料なし） · `00b68230`（命令位置の公開資料なし） · `00b68204`（命令位置の公開資料なし）

~~~diff
- 00b681e4 ["INT_ADD", "register:40f0:8", ["const:b681e4:8", "const:4:8"]]
- 00b681e4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68228 ["INT_ADD", "register:40f0:8", ["const:b68228:8", "const:4:8"]]
+ 00b68228 ["CALL", null, ["callee:00bde090:8"]]
- 00b681e4 bytes 97d70194
+ 00b68228 bytes 9ad70194
- 00b681ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b681ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b68230 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b681ec bytes 809204f9
+ 00b68230 bytes 80b204f9
- 00b681c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b681c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68204 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b68204 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b681c0 bytes 819244f9
+ 00b68204 bytes 81b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfde1cd2ad52aad0daba36c703b1f62d"></a>

### [`00b6821c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md) → [`00b68260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68260.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6827c",
      "incomplete_value": false,
      "site": "00b68280",
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
      "definition_site": "00b68238",
      "incomplete_value": false,
      "site": "00b6823c",
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
      "definition_site": "00b6828c",
      "incomplete_value": true,
      "site": "00b68298",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68248",
      "incomplete_value": true,
      "site": "00b68254",
      "value": [
        "LOAD",
        "8",
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
      "00b6827c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6828c",
      "DATA",
      [
        "storage",
        "010a1930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6827c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6828c",
      "DATA",
      [
        "storage",
        "010a1970",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6823c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b6823c) · [`00b68238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b68238) · [`00b68244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b68244)
- 新版 `00b68280`（命令位置の公開資料なし） · `00b6827c`（命令位置の公開資料なし） · `00b68288`（命令位置の公開資料なし）

~~~diff
- 00b6823c ["INT_ADD", "register:40f0:8", ["const:b6823c:8", "const:4:8"]]
- 00b6823c ["CALL", null, ["callee:00bde180:8"]]
+ 00b68280 ["INT_ADD", "register:40f0:8", ["const:b68280:8", "const:4:8"]]
+ 00b68280 ["CALL", null, ["callee:00bde180:8"]]
- 00b6823c bytes bdd70194
+ 00b68280 bytes c0d70194
- 00b68238 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b68238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6827c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6827c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6827c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6827c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68238 bytes 00501791
+ 00b6827c bytes 001c1591
- 00b68244 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00b68244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68288 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00b68288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68244 bytes 08c12491
+ 00b68288 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6cb7c2fc516d78016dee3314937d49"></a>

### [`00b68258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md) → [`00b6829c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6829c.md) _ZN8firebase4auth8auth_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b682dc",
      "incomplete_value": true,
      "site": "00b682dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68298",
      "incomplete_value": true,
      "site": "00b68298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "definition_site": "00b682b8",
      "incomplete_value": true,
      "site": "00b682b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68274",
      "incomplete_value": true,
      "site": "00b68274",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b682c0",
      "incomplete_value": false,
      "site": "00b682d4",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6827c",
      "incomplete_value": false,
      "site": "00b68290",
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
            "const:fd8:8"
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
      "00b682b0",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b682c0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b682dc",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b682b0",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b682c0",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b682dc",
      "WRITE",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b68290) · [`00b68298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b68298) · [`00b6826c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b6826c)
- 新版 `00b682d4`（命令位置の公開資料なし） · `00b682dc`（命令位置の公開資料なし） · `00b682b0`（命令位置の公開資料なし）

~~~diff
- 00b68290 ["INT_ADD", "register:40f0:8", ["const:b68290:8", "const:4:8"]]
- 00b68290 ["CALL", null, ["callee:00bde090:8"]]
+ 00b682d4 ["INT_ADD", "register:40f0:8", ["const:b682d4:8", "const:4:8"]]
+ 00b682d4 ["CALL", null, ["callee:00bde090:8"]]
- 00b68290 bytes 6cd70194
+ 00b682d4 bytes 6fd70194
- 00b68298 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b68298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b682dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b682dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68298 bytes 809204f9
+ 00b682dc bytes 80b204f9
- 00b6826c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b6826c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b682b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b682b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6826c bytes 819244f9
+ 00b682b0 bytes 81b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a1c6d3fd661382b49812e92f621756"></a>

### [`00b682c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md) → [`00b6830c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6830c.md) _ZN8firebase4auth8auth_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b68328",
      "incomplete_value": false,
      "site": "00b6832c",
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
      "definition_site": "00b682e4",
      "incomplete_value": false,
      "site": "00b682e8",
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
      "definition_site": "00b68338",
      "incomplete_value": true,
      "site": "00b68344",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b682f4",
      "incomplete_value": true,
      "site": "00b68300",
      "value": [
        "LOAD",
        "8",
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
      "00b68328",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b68338",
      "DATA",
      [
        "storage",
        "010a1938",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68328",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b68338",
      "DATA",
      [
        "storage",
        "010a1978",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b682e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682e8) · [`00b682e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682e4) · [`00b682f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682f0)
- 新版 `00b6832c`（命令位置の公開資料なし） · `00b68328`（命令位置の公開資料なし） · `00b68334`（命令位置の公開資料なし）

~~~diff
- 00b682e8 ["INT_ADD", "register:40f0:8", ["const:b682e8:8", "const:4:8"]]
- 00b682e8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6832c ["INT_ADD", "register:40f0:8", ["const:b6832c:8", "const:4:8"]]
+ 00b6832c ["CALL", null, ["callee:00bde180:8"]]
- 00b682e8 bytes 92d70194
+ 00b6832c bytes 95d70194
- 00b682e4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b682e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b682e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b682e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68328 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b68328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b682e4 bytes 00fc1991
+ 00b68328 bytes 00c81791
- 00b682f0 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00b682f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b682f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b682f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68334 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00b68334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b682f0 bytes 08e12491
+ 00b68334 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d76acebc117ab511b7eaf42f984f08b1"></a>

### [`00b68304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md) → [`00b68348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68348.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b68374",
      "incomplete_value": true,
      "site": "00b68374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68330",
      "incomplete_value": true,
      "site": "00b68330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b6835c",
      "incomplete_value": true,
      "site": "00b6835c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68318",
      "incomplete_value": true,
      "site": "00b68318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68368",
      "incomplete_value": false,
      "site": "00b6836c",
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
    "old": {
      "definition_site": "00b68324",
      "incomplete_value": false,
      "site": "00b68328",
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
            "const:96e:8"
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
      "00b68358",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68368",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68374",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68358",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68368",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68374",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68328) · [`00b68330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68330) · [`00b68314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68314)
- 新版 `00b6836c`（命令位置の公開資料なし） · `00b68374`（命令位置の公開資料なし） · `00b68358`（命令位置の公開資料なし）

~~~diff
- 00b68328 ["INT_ADD", "register:40f0:8", ["const:b68328:8", "const:4:8"]]
- 00b68328 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6836c ["INT_ADD", "register:40f0:8", ["const:b6836c:8", "const:4:8"]]
+ 00b6836c ["CALL", null, ["callee:00bde090:8"]]
- 00b68328 bytes 46d70194
+ 00b6836c bytes 49d70194
- 00b68330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b68330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68374 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b68374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68330 bytes 60a204f9
+ 00b68374 bytes 60c204f9
- 00b68314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b68314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68358 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b68358 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68314 bytes 68a244f9
+ 00b68358 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c50a6f668c5f6663a3ee89b05a047cb9"></a>

### [`00b68344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md) → [`00b68388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68388.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b683b4",
      "incomplete_value": true,
      "site": "00b683b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68370",
      "incomplete_value": true,
      "site": "00b68370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b6839c",
      "incomplete_value": true,
      "site": "00b6839c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68358",
      "incomplete_value": true,
      "site": "00b68358",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b683a4",
      "incomplete_value": false,
      "site": "00b683ac",
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
    "old": {
      "definition_site": "00b68360",
      "incomplete_value": false,
      "site": "00b68368",
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
            "const:96e:8"
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
      "00b68398",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683a4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b683b4",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68398",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683a4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b683b4",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68368) · [`00b68370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68370) · [`00b68354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68354)
- 新版 `00b683ac`（命令位置の公開資料なし） · `00b683b4`（命令位置の公開資料なし） · `00b68398`（命令位置の公開資料なし）

~~~diff
- 00b68368 ["INT_ADD", "register:40f0:8", ["const:b68368:8", "const:4:8"]]
- 00b68368 ["CALL", null, ["callee:00bde090:8"]]
+ 00b683ac ["INT_ADD", "register:40f0:8", ["const:b683ac:8", "const:4:8"]]
+ 00b683ac ["CALL", null, ["callee:00bde090:8"]]
- 00b68368 bytes 36d70194
+ 00b683ac bytes 39d70194
- 00b68370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b68370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b683b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b683b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68370 bytes 60a204f9
+ 00b683b4 bytes 60c204f9
- 00b68354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b68354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68398 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b68398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68354 bytes 68a244f9
+ 00b68398 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1d2483fa41a99599668e4ea8016f33"></a>

### [`00b68384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md) → [`00b683c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b683c8.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b683f8",
      "incomplete_value": true,
      "site": "00b683f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683b4",
      "incomplete_value": true,
      "site": "00b683b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b683dc",
      "incomplete_value": true,
      "site": "00b683dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68398",
      "incomplete_value": true,
      "site": "00b68398",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b683e8",
      "incomplete_value": false,
      "site": "00b683f0",
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
    "old": {
      "definition_site": "00b683a4",
      "incomplete_value": false,
      "site": "00b683ac",
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
            "const:96e:8"
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
      "00b683d8",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683e8",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b683f8",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b683d8",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683e8",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b683f8",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b683ac) · [`00b683b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b683b4) · [`00b68394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b68394)
- 新版 `00b683f0`（命令位置の公開資料なし） · `00b683f8`（命令位置の公開資料なし） · `00b683d8`（命令位置の公開資料なし）

~~~diff
- 00b683ac ["INT_ADD", "register:40f0:8", ["const:b683ac:8", "const:4:8"]]
- 00b683ac ["CALL", null, ["callee:00bde090:8"]]
+ 00b683f0 ["INT_ADD", "register:40f0:8", ["const:b683f0:8", "const:4:8"]]
+ 00b683f0 ["CALL", null, ["callee:00bde090:8"]]
- 00b683ac bytes 25d70194
+ 00b683f0 bytes 28d70194
- 00b683b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b683b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b683f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b683f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b683b4 bytes 60a204f9
+ 00b683f8 bytes 60c204f9
- 00b68394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b68394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b683d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b683d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68394 bytes 68a244f9
+ 00b683d8 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0877b7d66a0331a83b4cce02f149d76b"></a>

### [`00b683c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md) → [`00b6840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6840c.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6843c",
      "incomplete_value": true,
      "site": "00b6843c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683f8",
      "incomplete_value": true,
      "site": "00b683f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b68420",
      "incomplete_value": true,
      "site": "00b68420",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683dc",
      "incomplete_value": true,
      "site": "00b683dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68428",
      "incomplete_value": false,
      "site": "00b68434",
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
    "old": {
      "definition_site": "00b683e4",
      "incomplete_value": false,
      "site": "00b683f0",
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
            "const:96e:8"
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
      "00b6841c",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68428",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6843c",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6841c",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68428",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6843c",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683f0) · [`00b683f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683f8) · [`00b683d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683d8)
- 新版 `00b68434`（命令位置の公開資料なし） · `00b6843c`（命令位置の公開資料なし） · `00b6841c`（命令位置の公開資料なし）

~~~diff
- 00b683f0 ["INT_ADD", "register:40f0:8", ["const:b683f0:8", "const:4:8"]]
- 00b683f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68434 ["INT_ADD", "register:40f0:8", ["const:b68434:8", "const:4:8"]]
+ 00b68434 ["CALL", null, ["callee:00bde090:8"]]
- 00b683f0 bytes 14d70194
+ 00b68434 bytes 17d70194
- 00b683f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b683f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6843c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b6843c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b683f8 bytes 60a204f9
+ 00b6843c bytes 60c204f9
- 00b683d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
- 00b683d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6841c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b6841c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b683d8 bytes 68a244f9
+ 00b6841c bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a88470a5e6e7273cc94792aacc48e1f0"></a>

### [`00b68418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md) → [`00b6845c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6845c.md) _ZN8firebase4auth8user_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b684b4",
      "incomplete_value": true,
      "site": "00b684b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68470",
      "incomplete_value": true,
      "site": "00b68470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "00b68490",
      "incomplete_value": true,
      "site": "00b6849c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6844c",
      "incomplete_value": true,
      "site": "00b68458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
      "00b68470",
      "READ",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68490",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684b4",
      "WRITE",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68470",
      "READ",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68490",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684b4",
      "WRITE",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6842c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b6842c) · [`00b68458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b68458) · [`00b68470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b68470)
- 新版 `00b68470`（命令位置の公開資料なし） · `00b6849c`（命令位置の公開資料なし） · `00b684b4`（命令位置の公開資料なし）

~~~diff
- 00b6842c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:948:8"]]
- 00b6842c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6842c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b68470 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:988:8"]]
+ 00b68470 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b68470 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6842c bytes a8226539
+ 00b68470 bytes a8226639
- 00b68458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68458 ["INT_ADD", "register:40f0:8", ["const:b68458:8", "const:4:8"]]
- 00b68458 ["CALLIND", null, ["register:0:8"]]
+ 00b6849c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6849c ["INT_ADD", "register:40f0:8", ["const:b6849c:8", "const:4:8"]]
+ 00b6849c ["CALLIND", null, ["register:0:8"]]
- 00b68458 bytes 00013fd6
+ 00b6849c bytes 00013fd6
- 00b68470 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68470 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:948:8"]]
- 00b68470 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b684b4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b684b4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:988:8"]]
+ 00b684b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68470 bytes a0222539
+ 00b684b4 bytes a0222639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f552b299f0fbfea222e5b0c95fe1b8f"></a>

### [`00b68484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md) → [`00b684c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b684c8.md) _ZN8firebase4auth8user_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b68504",
      "incomplete_value": true,
      "site": "00b68504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b684c0",
      "incomplete_value": true,
      "site": "00b684c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "00b68524",
      "incomplete_value": true,
      "site": "00b68524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b684e0",
      "incomplete_value": true,
      "site": "00b684e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b684e0",
      "incomplete_value": true,
      "site": "00b684e0",
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
      "definition_site": "00b6849c",
      "incomplete_value": true,
      "site": "00b6849c",
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
      "00b684dc",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684e8",
      "READ",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68504",
      "WRITE",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b684dc",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684e8",
      "READ",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68504",
      "WRITE",
      [
        "storage",
        "010a1988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b68498) · [`00b684c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b684c0) · [`00b684dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b684dc)
- 新版 `00b684dc`（命令位置の公開資料なし） · `00b68504`（命令位置の公開資料なし） · `00b68520`（命令位置の公開資料なし）

~~~diff
- 00b68498 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00b68498 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b684dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b684dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68498 bytes 81a244f9
+ 00b684dc bytes 81c244f9
- 00b684c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b684c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b684c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:948:8"]]
- 00b684c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b68504 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b68504 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b68504 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
+ 00b68504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b684c0 bytes bf222539
+ 00b68504 bytes bf222639
- 00b684dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b684dc ["INT_ADD", "register:40f0:8", ["const:b684dc:8", "const:4:8"]]
- 00b684dc ["CALLIND", null, ["register:0:8"]]
+ 00b68520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68520 ["INT_ADD", "register:40f0:8", ["const:b68520:8", "const:4:8"]]
+ 00b68520 ["CALLIND", null, ["register:0:8"]]
- 00b684dc bytes 00013fd6
+ 00b68520 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-717bf129db5a1ec1f00f844d6058bd5e"></a>

### [`00b684f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md) → [`00b68538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68538.md) _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68578",
      "incomplete_value": true,
      "site": "00b68578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68534",
      "incomplete_value": true,
      "site": "00b68534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b68554",
      "incomplete_value": true,
      "site": "00b68554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68510",
      "incomplete_value": true,
      "site": "00b68510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6855c",
      "incomplete_value": false,
      "site": "00b68570",
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
    "old": {
      "definition_site": "00b68518",
      "incomplete_value": false,
      "site": "00b6852c",
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
            "const:96e:8"
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
      "00b6854c",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6855c",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68578",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6854c",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6855c",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68578",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6852c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b6852c) · [`00b68534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b68534) · [`00b68508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b68508)
- 新版 `00b68570`（命令位置の公開資料なし） · `00b68578`（命令位置の公開資料なし） · `00b6854c`（命令位置の公開資料なし）

~~~diff
- 00b6852c ["INT_ADD", "register:40f0:8", ["const:b6852c:8", "const:4:8"]]
- 00b6852c ["CALL", null, ["callee:00bde090:8"]]
+ 00b68570 ["INT_ADD", "register:40f0:8", ["const:b68570:8", "const:4:8"]]
+ 00b68570 ["CALL", null, ["callee:00bde090:8"]]
- 00b6852c bytes c5d60194
+ 00b68570 bytes c8d60194
- 00b68534 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00b68534 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b68578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68534 bytes 80a204f9
+ 00b68578 bytes 80c204f9
- 00b68508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00b68508 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6854c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b6854c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68508 bytes 81a244f9
+ 00b6854c bytes 81c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2e992a48735be7dc9fcf2f1143a484"></a>

### [`00b68564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md) → [`00b685a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685a8.md) _ZN8firebase4auth8user_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b685c4",
      "incomplete_value": false,
      "site": "00b685c8",
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
      "definition_site": "00b68580",
      "incomplete_value": false,
      "site": "00b68584",
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
      "definition_site": "00b685d4",
      "incomplete_value": true,
      "site": "00b685e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68590",
      "incomplete_value": true,
      "site": "00b6859c",
      "value": [
        "LOAD",
        "8",
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
      "00b685c4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b685d4",
      "DATA",
      [
        "storage",
        "010a1950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b685c4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b685d4",
      "DATA",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b68584) · [`00b68580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b68580) · [`00b6858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b6858c)
- 新版 `00b685c8`（命令位置の公開資料なし） · `00b685c4`（命令位置の公開資料なし） · `00b685d0`（命令位置の公開資料なし）

~~~diff
- 00b68584 ["INT_ADD", "register:40f0:8", ["const:b68584:8", "const:4:8"]]
- 00b68584 ["CALL", null, ["callee:00bde180:8"]]
+ 00b685c8 ["INT_ADD", "register:40f0:8", ["const:b685c8:8", "const:4:8"]]
+ 00b685c8 ["CALL", null, ["callee:00bde180:8"]]
- 00b68584 bytes ebd60194
+ 00b685c8 bytes eed60194
- 00b68580 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b68580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b685c4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b685c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b685c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b685c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68580 bytes 00501791
+ 00b685c4 bytes 001c1591
- 00b6858c ["COPY", "tmp:0:8", ["const:950:8"]]
- 00b6858c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6858c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6858c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b685d0 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00b685d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b685d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b685d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6858c bytes 08412591
+ 00b685d0 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb61f7def1b75ceb719f5085616179d"></a>

### [`00b685a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md) → [`00b685e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b685e4.md) _ZN8firebase4auth8user_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68624",
      "incomplete_value": true,
      "site": "00b68624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685e0",
      "incomplete_value": true,
      "site": "00b685e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "00b68600",
      "incomplete_value": true,
      "site": "00b68600",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685bc",
      "incomplete_value": true,
      "site": "00b685bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68608",
      "incomplete_value": false,
      "site": "00b6861c",
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
    "old": {
      "definition_site": "00b685c4",
      "incomplete_value": false,
      "site": "00b685d8",
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
            "const:96e:8"
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
      "00b685f8",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68608",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68624",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b685f8",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68608",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68624",
      "WRITE",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b685d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685d8) · [`00b685e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685e0) · [`00b685b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685b4)
- 新版 `00b6861c`（命令位置の公開資料なし） · `00b68624`（命令位置の公開資料なし） · `00b685f8`（命令位置の公開資料なし）

~~~diff
- 00b685d8 ["INT_ADD", "register:40f0:8", ["const:b685d8:8", "const:4:8"]]
- 00b685d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6861c ["INT_ADD", "register:40f0:8", ["const:b6861c:8", "const:4:8"]]
+ 00b6861c ["CALL", null, ["callee:00bde090:8"]]
- 00b685d8 bytes 9ad60194
+ 00b6861c bytes 9dd60194
- 00b685e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00b685e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b68624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b685e0 bytes 80a204f9
+ 00b68624 bytes 80c204f9
- 00b685b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00b685b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b685f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b685f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b685b4 bytes 81a244f9
+ 00b685f8 bytes 81c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ac7d4faa3033706d8ede2a41a72cb09"></a>

### [`00b68610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md) → [`00b68654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68654.md) _ZN8firebase4auth8user_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b68670",
      "incomplete_value": false,
      "site": "00b68674",
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
      "definition_site": "00b6862c",
      "incomplete_value": false,
      "site": "00b68630",
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
      "definition_site": "00b68680",
      "incomplete_value": true,
      "site": "00b6868c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6863c",
      "incomplete_value": true,
      "site": "00b68648",
      "value": [
        "LOAD",
        "8",
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
      "00b68670",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b68680",
      "DATA",
      [
        "storage",
        "010a1960",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68670",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b68680",
      "DATA",
      [
        "storage",
        "010a19a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b68630) · [`00b6862c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b6862c) · [`00b68638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b68638)
- 新版 `00b68674`（命令位置の公開資料なし） · `00b68670`（命令位置の公開資料なし） · `00b6867c`（命令位置の公開資料なし）

~~~diff
- 00b68630 ["INT_ADD", "register:40f0:8", ["const:b68630:8", "const:4:8"]]
- 00b68630 ["CALL", null, ["callee:00bde180:8"]]
+ 00b68674 ["INT_ADD", "register:40f0:8", ["const:b68674:8", "const:4:8"]]
+ 00b68674 ["CALL", null, ["callee:00bde180:8"]]
- 00b68630 bytes c0d60194
+ 00b68674 bytes c3d60194
- 00b6862c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6862c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6862c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6862c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68670 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b68670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6862c bytes 00fc1991
+ 00b68670 bytes 00c81791
- 00b68638 ["COPY", "tmp:0:8", ["const:960:8"]]
- 00b68638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6867c ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00b6867c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6867c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6867c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68638 bytes 08812591
+ 00b6867c bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69ef51a7859032966ef8c1da2382177"></a>

### [`00b6864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md) → [`00b68690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68690.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b686bc",
      "incomplete_value": true,
      "site": "00b686bc",
      "value": [
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
    "old": {
      "definition_site": "00b68678",
      "incomplete_value": true,
      "site": "00b68678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b686a4",
      "incomplete_value": true,
      "site": "00b686a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68660",
      "incomplete_value": true,
      "site": "00b68660",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b686b0",
      "incomplete_value": false,
      "site": "00b686b4",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6866c",
      "incomplete_value": false,
      "site": "00b68670",
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
      "00b686a0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686b0",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b686bc",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b686a0",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686b0",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b686bc",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b68670) · [`00b68678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b68678) · [`00b6865c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b6865c)
- 新版 `00b686b4`（命令位置の公開資料なし） · `00b686bc`（命令位置の公開資料なし） · `00b686a0`（命令位置の公開資料なし）

~~~diff
- 00b68670 ["INT_ADD", "register:40f0:8", ["const:b68670:8", "const:4:8"]]
- 00b68670 ["CALL", null, ["callee:00bde090:8"]]
+ 00b686b4 ["INT_ADD", "register:40f0:8", ["const:b686b4:8", "const:4:8"]]
+ 00b686b4 ["CALL", null, ["callee:00bde090:8"]]
- 00b68670 bytes 74d60194
+ 00b686b4 bytes 77d60194
- 00b68678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b68678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b686bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b686bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68678 bytes 60b604f9
+ 00b686bc bytes 60d604f9
- 00b6865c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b6865c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b686a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b686a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6865c bytes 68b644f9
+ 00b686a0 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d6b50a1405a2fe703f16f5e4d7d288"></a>

### [`00b6868c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md) → [`00b686d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b686d0.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b686fc",
      "incomplete_value": true,
      "site": "00b686fc",
      "value": [
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
    "old": {
      "definition_site": "00b686b8",
      "incomplete_value": true,
      "site": "00b686b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b686e4",
      "incomplete_value": true,
      "site": "00b686e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686a0",
      "incomplete_value": true,
      "site": "00b686a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b686ec",
      "incomplete_value": false,
      "site": "00b686f4",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686a8",
      "incomplete_value": false,
      "site": "00b686b0",
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
      "00b686e0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686ec",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b686fc",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b686e0",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686ec",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b686fc",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b686b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b686b0) · [`00b686b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b686b8) · [`00b6869c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b6869c)
- 新版 `00b686f4`（命令位置の公開資料なし） · `00b686fc`（命令位置の公開資料なし） · `00b686e0`（命令位置の公開資料なし）

~~~diff
- 00b686b0 ["INT_ADD", "register:40f0:8", ["const:b686b0:8", "const:4:8"]]
- 00b686b0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b686f4 ["INT_ADD", "register:40f0:8", ["const:b686f4:8", "const:4:8"]]
+ 00b686f4 ["CALL", null, ["callee:00bde090:8"]]
- 00b686b0 bytes 64d60194
+ 00b686f4 bytes 67d60194
- 00b686b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b686b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b686fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b686fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b686b8 bytes 60b604f9
+ 00b686fc bytes 60d604f9
- 00b6869c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b6869c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b686e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b686e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6869c bytes 68b644f9
+ 00b686e0 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1df9daf0049e80feb15d83ffbf4247f"></a>

### [`00b686cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md) → [`00b68710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68710.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b68740",
      "incomplete_value": true,
      "site": "00b68740",
      "value": [
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
    "old": {
      "definition_site": "00b686fc",
      "incomplete_value": true,
      "site": "00b686fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b68724",
      "incomplete_value": true,
      "site": "00b68724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686e0",
      "incomplete_value": true,
      "site": "00b686e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68730",
      "incomplete_value": false,
      "site": "00b68738",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686ec",
      "incomplete_value": false,
      "site": "00b686f4",
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
      "00b68720",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68730",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68740",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68720",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68730",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b68740",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b686f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686f4) · [`00b686fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686fc) · [`00b686dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686dc)
- 新版 `00b68738`（命令位置の公開資料なし） · `00b68740`（命令位置の公開資料なし） · `00b68720`（命令位置の公開資料なし）

~~~diff
- 00b686f4 ["INT_ADD", "register:40f0:8", ["const:b686f4:8", "const:4:8"]]
- 00b686f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68738 ["INT_ADD", "register:40f0:8", ["const:b68738:8", "const:4:8"]]
+ 00b68738 ["CALL", null, ["callee:00bde090:8"]]
- 00b686f4 bytes 53d60194
+ 00b68738 bytes 56d60194
- 00b686fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b686fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b68740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b686fc bytes 60b604f9
+ 00b68740 bytes 60d604f9
- 00b686dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b686dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b68720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b686dc bytes 68b644f9
+ 00b68720 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2708d149be57239b09ecce057c6f9cb1"></a>

### [`00b68710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md) → [`00b68754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68754.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68784",
      "incomplete_value": true,
      "site": "00b68784",
      "value": [
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
    "old": {
      "definition_site": "00b68740",
      "incomplete_value": true,
      "site": "00b68740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b68768",
      "incomplete_value": true,
      "site": "00b68768",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68724",
      "incomplete_value": true,
      "site": "00b68724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68770",
      "incomplete_value": false,
      "site": "00b6877c",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6872c",
      "incomplete_value": false,
      "site": "00b68738",
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
      "00b68764",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68770",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68784",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68764",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68770",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b68784",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68738) · [`00b68740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68740) · [`00b68720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68720)
- 新版 `00b6877c`（命令位置の公開資料なし） · `00b68784`（命令位置の公開資料なし） · `00b68764`（命令位置の公開資料なし）

~~~diff
- 00b68738 ["INT_ADD", "register:40f0:8", ["const:b68738:8", "const:4:8"]]
- 00b68738 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6877c ["INT_ADD", "register:40f0:8", ["const:b6877c:8", "const:4:8"]]
+ 00b6877c ["CALL", null, ["callee:00bde090:8"]]
- 00b68738 bytes 42d60194
+ 00b6877c bytes 45d60194
- 00b68740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b68740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68784 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b68784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68740 bytes 60b604f9
+ 00b68784 bytes 60d604f9
- 00b68720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00b68720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68764 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b68764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68720 bytes 68b644f9
+ 00b68764 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db0df58a999a7182f386e25a1e98ab30"></a>

### [`00b68760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md) → [`00b687a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b687a4.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b687fc",
      "incomplete_value": true,
      "site": "00b687fc",
      "value": [
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
    "old": {
      "definition_site": "00b687b8",
      "incomplete_value": true,
      "site": "00b687b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "00b687d8",
      "incomplete_value": true,
      "site": "00b687e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b68794",
      "incomplete_value": true,
      "site": "00b687a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:968:8"
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
      "00b687b8",
      "READ",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b687d8",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687fc",
      "WRITE",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b687b8",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b687d8",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687fc",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b68774) · [`00b687a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b687a0) · [`00b687b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b687b8)
- 新版 `00b687b8`（命令位置の公開資料なし） · `00b687e4`（命令位置の公開資料なし） · `00b687fc`（命令位置の公開資料なし）

~~~diff
- 00b68774 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
- 00b68774 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b68774 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b687b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00b687b8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b687b8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b68774 bytes a8c26539
+ 00b687b8 bytes a8c26639
- 00b687a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b687a0 ["INT_ADD", "register:40f0:8", ["const:b687a0:8", "const:4:8"]]
- 00b687a0 ["CALLIND", null, ["register:0:8"]]
+ 00b687e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b687e4 ["INT_ADD", "register:40f0:8", ["const:b687e4:8", "const:4:8"]]
+ 00b687e4 ["CALLIND", null, ["register:0:8"]]
- 00b687a0 bytes 00013fd6
+ 00b687e4 bytes 00013fd6
- 00b687b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b687b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
- 00b687b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b687fc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b687fc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
+ 00b687fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b687b8 bytes a0c22539
+ 00b687fc bytes a0c22639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfe1fcbf119248414cdecee30e2bd047"></a>

### [`00b687cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md) → [`00b68810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68810.md) _ZN8firebase4auth8jniphone12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6884c",
      "incomplete_value": true,
      "site": "00b6884c",
      "value": [
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
    "old": {
      "definition_site": "00b68808",
      "incomplete_value": true,
      "site": "00b68808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "00b6886c",
      "incomplete_value": true,
      "site": "00b6886c",
      "value": [
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
    "old": {
      "definition_site": "00b68828",
      "incomplete_value": true,
      "site": "00b68828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b68828",
      "incomplete_value": true,
      "site": "00b68828",
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
      "definition_site": "00b687e4",
      "incomplete_value": true,
      "site": "00b687e4",
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
      "00b68824",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68830",
      "READ",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6884c",
      "WRITE",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68824",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68830",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6884c",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b687e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b687e0) · [`00b68808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b68808) · [`00b68824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b68824)
- 新版 `00b68824`（命令位置の公開資料なし） · `00b6884c`（命令位置の公開資料なし） · `00b68868`（命令位置の公開資料なし）

~~~diff
- 00b687e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b687e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68824 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b68824 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b687e0 bytes 81b644f9
+ 00b68824 bytes 81d644f9
- 00b68808 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68808 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68808 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:970:8"]]
- 00b68808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6884c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6884c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6884c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
+ 00b6884c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68808 bytes bfc22539
+ 00b6884c bytes bfc22639
- 00b68824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68824 ["INT_ADD", "register:40f0:8", ["const:b68824:8", "const:4:8"]]
- 00b68824 ["CALLIND", null, ["register:0:8"]]
+ 00b68868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68868 ["INT_ADD", "register:40f0:8", ["const:b68868:8", "const:4:8"]]
+ 00b68868 ["CALLIND", null, ["register:0:8"]]
- 00b68824 bytes 00013fd6
+ 00b68868 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ff4df801a06bfac8f270e09a8b739d"></a>

### [`00b6883c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md) → [`00b68880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68880.md) _ZN8firebase4auth8jniphone14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b688c0",
      "incomplete_value": true,
      "site": "00b688c0",
      "value": [
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
    "old": {
      "definition_site": "00b6887c",
      "incomplete_value": true,
      "site": "00b6887c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b6889c",
      "incomplete_value": true,
      "site": "00b6889c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68858",
      "incomplete_value": true,
      "site": "00b68858",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b688a4",
      "incomplete_value": false,
      "site": "00b688b8",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68860",
      "incomplete_value": false,
      "site": "00b68874",
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
      "00b68894",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b688a4",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b688c0",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68894",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b688a4",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b688c0",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b68874) · [`00b6887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b6887c) · [`00b68850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b68850)
- 新版 `00b688b8`（命令位置の公開資料なし） · `00b688c0`（命令位置の公開資料なし） · `00b68894`（命令位置の公開資料なし）

~~~diff
- 00b68874 ["INT_ADD", "register:40f0:8", ["const:b68874:8", "const:4:8"]]
- 00b68874 ["CALL", null, ["callee:00bde090:8"]]
+ 00b688b8 ["INT_ADD", "register:40f0:8", ["const:b688b8:8", "const:4:8"]]
+ 00b688b8 ["CALL", null, ["callee:00bde090:8"]]
- 00b68874 bytes f3d50194
+ 00b688b8 bytes f6d50194
- 00b6887c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b6887c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b688c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b688c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6887c bytes 80b604f9
+ 00b688c0 bytes 80d604f9
- 00b68850 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b68850 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b68894 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68850 bytes 81b644f9
+ 00b68894 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51dee7290e9bfda66122085a1a1855a8"></a>

### [`00b688ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md) → [`00b688f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b688f0.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6890c",
      "incomplete_value": false,
      "site": "00b68910",
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
      "definition_site": "00b688c8",
      "incomplete_value": false,
      "site": "00b688cc",
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
      "definition_site": "00b6891c",
      "incomplete_value": true,
      "site": "00b68928",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b688d8",
      "incomplete_value": true,
      "site": "00b688e4",
      "value": [
        "LOAD",
        "8",
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
      "00b6890c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6891c",
      "DATA",
      [
        "storage",
        "010a1978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6890c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6891c",
      "DATA",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b688cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688cc) · [`00b688c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688c8) · [`00b688d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688d4)
- 新版 `00b68910`（命令位置の公開資料なし） · `00b6890c`（命令位置の公開資料なし） · `00b68918`（命令位置の公開資料なし）

~~~diff
- 00b688cc ["INT_ADD", "register:40f0:8", ["const:b688cc:8", "const:4:8"]]
- 00b688cc ["CALL", null, ["callee:00bde180:8"]]
+ 00b68910 ["INT_ADD", "register:40f0:8", ["const:b68910:8", "const:4:8"]]
+ 00b68910 ["CALL", null, ["callee:00bde180:8"]]
- 00b688cc bytes 19d60194
+ 00b68910 bytes 1cd60194
- 00b688c8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b688c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b688c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b688c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6890c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6890c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6890c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6890c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b688c8 bytes 00501791
+ 00b6890c bytes 001c1591
- 00b688d4 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00b688d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b688d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b688d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68918 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00b68918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b688d4 bytes 08e12591
+ 00b68918 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75cf87d273ebc95c03a328844ea9cbb"></a>

### [`00b688e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md) → [`00b6892c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6892c.md) _ZN8firebase4auth8jniphone13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6896c",
      "incomplete_value": true,
      "site": "00b6896c",
      "value": [
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
    "old": {
      "definition_site": "00b68928",
      "incomplete_value": true,
      "site": "00b68928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b68948",
      "incomplete_value": true,
      "site": "00b68948",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68904",
      "incomplete_value": true,
      "site": "00b68904",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68950",
      "incomplete_value": false,
      "site": "00b68964",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6890c",
      "incomplete_value": false,
      "site": "00b68920",
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
      "00b68940",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68950",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b6896c",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68940",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68950",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b6896c",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b68920) · [`00b68928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b68928) · [`00b688fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b688fc)
- 新版 `00b68964`（命令位置の公開資料なし） · `00b6896c`（命令位置の公開資料なし） · `00b68940`（命令位置の公開資料なし）

~~~diff
- 00b68920 ["INT_ADD", "register:40f0:8", ["const:b68920:8", "const:4:8"]]
- 00b68920 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68964 ["INT_ADD", "register:40f0:8", ["const:b68964:8", "const:4:8"]]
+ 00b68964 ["CALL", null, ["callee:00bde090:8"]]
- 00b68920 bytes c8d50194
+ 00b68964 bytes cbd50194
- 00b68928 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b68928 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6896c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b6896c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68928 bytes 80b604f9
+ 00b6896c bytes 80d604f9
- 00b688fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b688fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b68940 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b688fc bytes 81b644f9
+ 00b68940 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f09afeb7d825570c77b5433f00d74c0"></a>

### [`00b68958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md) → [`00b6899c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b6899c.md) _ZN8firebase4auth8jniphone10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b689b8",
      "incomplete_value": false,
      "site": "00b689bc",
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
      "definition_site": "00b68974",
      "incomplete_value": false,
      "site": "00b68978",
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
      "definition_site": "00b689c8",
      "incomplete_value": true,
      "site": "00b689d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b68984",
      "incomplete_value": true,
      "site": "00b68990",
      "value": [
        "LOAD",
        "8",
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
      "00b689b8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b689c8",
      "DATA",
      [
        "storage",
        "010a1988",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b689b8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b689c8",
      "DATA",
      [
        "storage",
        "010a19c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68978) · [`00b68974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68974) · [`00b68980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68980)
- 新版 `00b689bc`（命令位置の公開資料なし） · `00b689b8`（命令位置の公開資料なし） · `00b689c4`（命令位置の公開資料なし）

~~~diff
- 00b68978 ["INT_ADD", "register:40f0:8", ["const:b68978:8", "const:4:8"]]
- 00b68978 ["CALL", null, ["callee:00bde180:8"]]
+ 00b689bc ["INT_ADD", "register:40f0:8", ["const:b689bc:8", "const:4:8"]]
+ 00b689bc ["CALL", null, ["callee:00bde180:8"]]
- 00b68978 bytes eed50194
+ 00b689bc bytes f1d50194
- 00b68974 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b68974 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68974 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68974 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b689b8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b689b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b689b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b689b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68974 bytes 00fc1991
+ 00b689b8 bytes 00c81791
- 00b68980 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00b68980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b689c4 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00b689c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b689c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b689c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68980 bytes 08212691
+ 00b689c4 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dbfa7b9a1e2ade0736f2d87fac13de6"></a>

### [`00b68994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md) → [`00b689d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b689d8.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b68a04",
      "incomplete_value": true,
      "site": "00b68a04",
      "value": [
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
    "old": {
      "definition_site": "00b689c0",
      "incomplete_value": true,
      "site": "00b689c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00b689ec",
      "incomplete_value": true,
      "site": "00b689ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689a8",
      "incomplete_value": true,
      "site": "00b689a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b689f8",
      "incomplete_value": false,
      "site": "00b689fc",
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
    "old": {
      "definition_site": "00b689b4",
      "incomplete_value": false,
      "site": "00b689b8",
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
            "const:1f3:8"
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
      "00b689e8",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689f8",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a04",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b689e8",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689f8",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68a04",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b689b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689b8) · [`00b689c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689c0) · [`00b689a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689a4)
- 新版 `00b689fc`（命令位置の公開資料なし） · `00b68a04`（命令位置の公開資料なし） · `00b689e8`（命令位置の公開資料なし）

~~~diff
- 00b689b8 ["INT_ADD", "register:40f0:8", ["const:b689b8:8", "const:4:8"]]
- 00b689b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b689fc ["INT_ADD", "register:40f0:8", ["const:b689fc:8", "const:4:8"]]
+ 00b689fc ["CALL", null, ["callee:00bde090:8"]]
- 00b689b8 bytes a2d50194
+ 00b689fc bytes a5d50194
- 00b689c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b689c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68a04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b689c0 bytes 60ca04f9
+ 00b68a04 bytes 60ea04f9
- 00b689a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b689a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b689e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b689e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b689a4 bytes 68ca44f9
+ 00b689e8 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b234e7b7d5f5d719c34c7aa3876487"></a>

### [`00b689d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md) → [`00b68a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a18.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b68a44",
      "incomplete_value": true,
      "site": "00b68a44",
      "value": [
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
    "old": {
      "definition_site": "00b68a00",
      "incomplete_value": true,
      "site": "00b68a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00b68a2c",
      "incomplete_value": true,
      "site": "00b68a2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689e8",
      "incomplete_value": true,
      "site": "00b689e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68a34",
      "incomplete_value": false,
      "site": "00b68a3c",
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
    "old": {
      "definition_site": "00b689f0",
      "incomplete_value": false,
      "site": "00b689f8",
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
            "const:1f3:8"
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
      "00b68a28",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a34",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a44",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68a28",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a34",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68a44",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b689f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b689f8) · [`00b68a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b68a00) · [`00b689e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b689e4)
- 新版 `00b68a3c`（命令位置の公開資料なし） · `00b68a44`（命令位置の公開資料なし） · `00b68a28`（命令位置の公開資料なし）

~~~diff
- 00b689f8 ["INT_ADD", "register:40f0:8", ["const:b689f8:8", "const:4:8"]]
- 00b689f8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68a3c ["INT_ADD", "register:40f0:8", ["const:b68a3c:8", "const:4:8"]]
+ 00b68a3c ["CALL", null, ["callee:00bde090:8"]]
- 00b689f8 bytes 92d50194
+ 00b68a3c bytes 95d50194
- 00b68a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b68a00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a00 bytes 60ca04f9
+ 00b68a44 bytes 60ea04f9
- 00b689e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b689e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68a28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68a28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b689e4 bytes 68ca44f9
+ 00b68a28 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103dc43666429039e2c2e59730995974"></a>

### [`00b68a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md) → [`00b68a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a58.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
    "old": {
      "definition_site": "00b68a44",
      "incomplete_value": true,
      "site": "00b68a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:990:8"
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
    "old": {
      "definition_site": "00b68a28",
      "incomplete_value": true,
      "site": "00b68a28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b68a34",
      "incomplete_value": false,
      "site": "00b68a3c",
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
            "const:1f3:8"
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
      "00b68a68",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a78",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a88",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68a68",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a78",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68a88",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a3c) · [`00b68a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a44) · [`00b68a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a24)
- 新版 `00b68a80`（命令位置の公開資料なし） · `00b68a88`（命令位置の公開資料なし） · `00b68a68`（命令位置の公開資料なし）

~~~diff
- 00b68a3c ["INT_ADD", "register:40f0:8", ["const:b68a3c:8", "const:4:8"]]
- 00b68a3c ["CALL", null, ["callee:00bde090:8"]]
+ 00b68a80 ["INT_ADD", "register:40f0:8", ["const:b68a80:8", "const:4:8"]]
+ 00b68a80 ["CALL", null, ["callee:00bde090:8"]]
- 00b68a3c bytes 81d50194
+ 00b68a80 bytes 84d50194
- 00b68a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b68a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a44 bytes 60ca04f9
+ 00b68a88 bytes 60ea04f9
- 00b68a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b68a24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68a68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68a24 bytes 68ca44f9
+ 00b68a68 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a2f0aadbb8058a54e15d130736a1abf"></a>

### [`00b68a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md) → [`00b68a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68a9c.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobject

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
            "const:990:8"
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
    "old": {
      "definition_site": "00b68a74",
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
            "const:1f3:8"
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
      "00b68aac",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68ab8",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68acc",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68aac",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68ab8",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68acc",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a80) · [`00b68a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a88) · [`00b68a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a68)
- 新版 `00b68ac4`（命令位置の公開資料なし） · `00b68acc`（命令位置の公開資料なし） · `00b68aac`（命令位置の公開資料なし）

~~~diff
- 00b68a80 ["INT_ADD", "register:40f0:8", ["const:b68a80:8", "const:4:8"]]
- 00b68a80 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68ac4 ["INT_ADD", "register:40f0:8", ["const:b68ac4:8", "const:4:8"]]
+ 00b68ac4 ["CALL", null, ["callee:00bde090:8"]]
- 00b68a80 bytes 70d50194
+ 00b68ac4 bytes 73d50194
- 00b68a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b68a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68acc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68acc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68a88 bytes 60ca04f9
+ 00b68acc bytes 60ea04f9
- 00b68a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b68a68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68aac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00b68aac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68a68 bytes 68ca44f9
+ 00b68aac bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84b1db43504414a3d5141629fb1d2dc"></a>

### [`00b68aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md) → [`00b68aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00b68b00",
      "incomplete_value": true,
      "site": "00b68b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:998:8"
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
    "old": {
      "definition_site": "00b68adc",
      "incomplete_value": true,
      "site": "00b68ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:990:8"
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
      "00b68b00",
      "READ",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b20",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b44",
      "WRITE",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68b00",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b20",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b44",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68abc) · [`00b68ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68ae8) · [`00b68b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68b00)
- 新版 `00b68b00`（命令位置の公開資料なし） · `00b68b2c`（命令位置の公開資料なし） · `00b68b44`（命令位置の公開資料なし）

~~~diff
- 00b68abc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:998:8"]]
- 00b68abc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b68abc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b68b00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d8:8"]]
+ 00b68b00 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b68b00 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b68abc bytes a8626639
+ 00b68b00 bytes a8626739
- 00b68ae8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68ae8 ["INT_ADD", "register:40f0:8", ["const:b68ae8:8", "const:4:8"]]
- 00b68ae8 ["CALLIND", null, ["register:0:8"]]
+ 00b68b2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68b2c ["INT_ADD", "register:40f0:8", ["const:b68b2c:8", "const:4:8"]]
+ 00b68b2c ["CALLIND", null, ["register:0:8"]]
- 00b68ae8 bytes 00013fd6
+ 00b68b2c bytes 00013fd6
- 00b68b00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68b00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:998:8"]]
- 00b68b00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68b44 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b68b44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d8:8"]]
+ 00b68b44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68b00 bytes a0622639
+ 00b68b44 bytes a0622739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c10747940be1944865fab0fb6e5606d"></a>

### [`00b68b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md) → [`00b68b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68b58.md) _ZN8firebase4auth15phonecredential12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b68b94",
      "incomplete_value": true,
      "site": "00b68b94",
      "value": [
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
    "old": {
      "definition_site": "00b68b50",
      "incomplete_value": true,
      "site": "00b68b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "definition_site": "00b68bb4",
      "incomplete_value": true,
      "site": "00b68bb4",
      "value": [
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
    "old": {
      "definition_site": "00b68b70",
      "incomplete_value": true,
      "site": "00b68b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00b68b70",
      "incomplete_value": true,
      "site": "00b68b70",
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
      "definition_site": "00b68b2c",
      "incomplete_value": true,
      "site": "00b68b2c",
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
      "00b68b6c",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b78",
      "READ",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b94",
      "WRITE",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68b6c",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b78",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b94",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b28) · [`00b68b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b50) · [`00b68b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b6c)
- 新版 `00b68b6c`（命令位置の公開資料なし） · `00b68b94`（命令位置の公開資料なし） · `00b68bb0`（命令位置の公開資料なし）

~~~diff
- 00b68b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
- 00b68b28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00b68b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68b28 bytes 81ca44f9
+ 00b68b6c bytes 81ea44f9
- 00b68b50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68b50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68b50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:998:8"]]
- 00b68b50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b68b94 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b68b94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b68b94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d8:8"]]
+ 00b68b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68b50 bytes bf622639
+ 00b68b94 bytes bf622739
- 00b68b6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68b6c ["INT_ADD", "register:40f0:8", ["const:b68b6c:8", "const:4:8"]]
- 00b68b6c ["CALLIND", null, ["register:0:8"]]
+ 00b68bb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68bb0 ["INT_ADD", "register:40f0:8", ["const:b68bb0:8", "const:4:8"]]
+ 00b68bb0 ["CALLIND", null, ["register:0:8"]]
- 00b68b6c bytes 00013fd6
+ 00b68bb0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a7343408bb80a509f306f32ed2ed77"></a>

### [`00b68b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md) → [`00b68bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68bc8.md) _ZN8firebase4auth15phonecredential14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68c08",
      "incomplete_value": true,
      "site": "00b68c08",
      "value": [
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
    "old": {
      "definition_site": "00b68bc4",
      "incomplete_value": true,
      "site": "00b68bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00b68be4",
      "incomplete_value": true,
      "site": "00b68be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ba0",
      "incomplete_value": true,
      "site": "00b68ba0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b68bec",
      "incomplete_value": false,
      "site": "00b68c00",
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
    "old": {
      "definition_site": "00b68ba8",
      "incomplete_value": false,
      "site": "00b68bbc",
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
            "const:1f3:8"
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
      "00b68bdc",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68bec",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68c08",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68bdc",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68bec",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68c08",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68bbc) · [`00b68bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68bc4) · [`00b68b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68b98)
- 新版 `00b68c00`（命令位置の公開資料なし） · `00b68c08`（命令位置の公開資料なし） · `00b68bdc`（命令位置の公開資料なし）

~~~diff
- 00b68bbc ["INT_ADD", "register:40f0:8", ["const:b68bbc:8", "const:4:8"]]
- 00b68bbc ["CALL", null, ["callee:00bde090:8"]]
+ 00b68c00 ["INT_ADD", "register:40f0:8", ["const:b68c00:8", "const:4:8"]]
+ 00b68c00 ["CALL", null, ["callee:00bde090:8"]]
- 00b68bbc bytes 21d50194
+ 00b68c00 bytes 24d50194
- 00b68bc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
- 00b68bc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68c08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00b68c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68bc4 bytes 80ca04f9
+ 00b68c08 bytes 80ea04f9
- 00b68b98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
- 00b68b98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00b68bdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68b98 bytes 81ca44f9
+ 00b68bdc bytes 81ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9804148b0ce7e2c6fab58ca3f66c242c"></a>

### [`00b68bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md) → [`00b68c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c38.md) _ZN8firebase4auth15phonecredential11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00b68c10",
      "incomplete_value": false,
      "site": "00b68c14",
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
    "old": {
      "definition_site": "00b68c20",
      "incomplete_value": true,
      "site": "00b68c2c",
      "value": [
        "LOAD",
        "8",
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
      "00b68c54",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b68c64",
      "DATA",
      [
        "storage",
        "010a19a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68c54",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b68c64",
      "DATA",
      [
        "storage",
        "010a19e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c14) · [`00b68c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c10) · [`00b68c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c1c)
- 新版 `00b68c58`（命令位置の公開資料なし） · `00b68c54`（命令位置の公開資料なし） · `00b68c60`（命令位置の公開資料なし）

~~~diff
- 00b68c14 ["INT_ADD", "register:40f0:8", ["const:b68c14:8", "const:4:8"]]
- 00b68c14 ["CALL", null, ["callee:00bde180:8"]]
+ 00b68c58 ["INT_ADD", "register:40f0:8", ["const:b68c58:8", "const:4:8"]]
+ 00b68c58 ["CALL", null, ["callee:00bde180:8"]]
- 00b68c14 bytes 47d50194
+ 00b68c58 bytes 4ad50194
- 00b68c10 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b68c10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68c10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68c10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68c54 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b68c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68c10 bytes 00501791
+ 00b68c54 bytes 001c1591
- 00b68c1c ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00b68c1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68c1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68c1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68c60 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00b68c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68c1c bytes 08812691
+ 00b68c60 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d451244a4f29527d705f250f3940ab5"></a>

### [`00b68c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md) → [`00b68c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68c74.md) _ZN8firebase4auth15phonecredential13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00b68c70",
      "incomplete_value": true,
      "site": "00b68c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:990:8"
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
    "old": {
      "definition_site": "00b68c4c",
      "incomplete_value": true,
      "site": "00b68c4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b68c54",
      "incomplete_value": false,
      "site": "00b68c68",
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
            "const:1f3:8"
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
      "00b68c88",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68c98",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68cb4",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68c88",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68c98",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ],
    [
      "00b68cb4",
      "WRITE",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c68) · [`00b68c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c70) · [`00b68c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c44)
- 新版 `00b68cac`（命令位置の公開資料なし） · `00b68cb4`（命令位置の公開資料なし） · `00b68c88`（命令位置の公開資料なし）

~~~diff
- 00b68c68 ["INT_ADD", "register:40f0:8", ["const:b68c68:8", "const:4:8"]]
- 00b68c68 ["CALL", null, ["callee:00bde090:8"]]
+ 00b68cac ["INT_ADD", "register:40f0:8", ["const:b68cac:8", "const:4:8"]]
+ 00b68cac ["CALL", null, ["callee:00bde090:8"]]
- 00b68c68 bytes f6d40194
+ 00b68cac bytes f9d40194
- 00b68c70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
- 00b68c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00b68cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68c70 bytes 80ca04f9
+ 00b68cb4 bytes 80ea04f9
- 00b68c44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
- 00b68c44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00b68c88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68c44 bytes 81ca44f9
+ 00b68c88 bytes 81ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0bf6890afb7c06bc4f96741e3b49cb0"></a>

### [`00b68ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md) → [`00b68ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68ce4.md) _ZN8firebase4auth15phonecredential10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00b68cbc",
      "incomplete_value": false,
      "site": "00b68cc0",
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
    "old": {
      "definition_site": "00b68ccc",
      "incomplete_value": true,
      "site": "00b68cd8",
      "value": [
        "LOAD",
        "8",
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
      "00b68d00",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b68d10",
      "DATA",
      [
        "storage",
        "010a19a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68d00",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b68d10",
      "DATA",
      [
        "storage",
        "010a19e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cc0) · [`00b68cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cbc) · [`00b68cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cc8)
- 新版 `00b68d04`（命令位置の公開資料なし） · `00b68d00`（命令位置の公開資料なし） · `00b68d0c`（命令位置の公開資料なし）

~~~diff
- 00b68cc0 ["INT_ADD", "register:40f0:8", ["const:b68cc0:8", "const:4:8"]]
- 00b68cc0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b68d04 ["INT_ADD", "register:40f0:8", ["const:b68d04:8", "const:4:8"]]
+ 00b68d04 ["CALL", null, ["callee:00bde180:8"]]
- 00b68cc0 bytes 1cd50194
+ 00b68d04 bytes 1fd50194
- 00b68cbc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b68cbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68cbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68cbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68d00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b68d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68cbc bytes 00fc1991
+ 00b68d00 bytes 00c81791
- 00b68cc8 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00b68cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68d0c ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00b68d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68cc8 bytes 08a12691
+ 00b68d0c bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-663401eb7bb17a046eeff2ee5a9cabee"></a>

### [`00b68cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md) → [`00b68d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68d20.md) _ZN8firebase4auth24CacheCredentialMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c60.md) · 呼出先 4件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cb0.md) · 呼出先 4件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 80.78% / 新版 80.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 59件, `store_condition` 1件, `store_destination` 18件

アドレスに依存する影響 `branch_value` 16件, `call_argument_candidate` 1件, `store_condition` 16件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b68d60",
      "incomplete_value": true,
      "site": "00b68d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68d1c",
      "incomplete_value": true,
      "site": "00b68d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00b68dd8",
      "incomplete_value": true,
      "site": "00b68dd8",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68d94",
      "incomplete_value": true,
      "site": "00b68d94",
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
            "const:970:8"
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
      "definition_site": "00b68e14",
      "incomplete_value": true,
      "site": "00b68e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68dd0",
      "incomplete_value": true,
      "site": "00b68dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00b68d38",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68d48",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68d60",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68d38",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68d48",
      "PARAM",
      [
        "storage",
        "002a20b6",
        null,
        "string"
      ]
    ],
    [
      "00b68d60",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68d1c) · [`00b68d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68d94) · [`00b68dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68dd0)
- 新版 `00b68d60`（命令位置の公開資料なし） · `00b68dd8`（命令位置の公開資料なし） · `00b68e14`（命令位置の公開資料なし）

~~~diff
- 00b68d1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
- 00b68d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68d60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9a8:8"]]
+ 00b68d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68d1c bytes a0b604f9
+ 00b68d60 bytes a0d604f9
- 00b68d94 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b68d94 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:970:8"]]
- 00b68d94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68dd8 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b68dd8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:9b0:8"]]
+ 00b68dd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68d94 bytes c8c22539
+ 00b68dd8 bytes c8c22639
- 00b68dd0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:700:8"]]
- 00b68dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68e14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:740:8"]]
+ 00b68e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68dd0 bytes a08203f9
+ 00b68e14 bytes a0a203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7228836ac8819df6b99cf05bb019d5fa"></a>

### [`00b69348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69348.md) → [`00b6938c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b6938c.md) _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c70.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cc0.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 44.31% / 新版 44.31%

CFGの説明率　旧版 33.02% / 新版 33.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 31件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `branch_value` 5件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69384"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b693a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b693d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b693a0",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b693a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b693a8"
      ]
    ],
    [
      "00b693b0",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b693a0",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b693a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b693ec"
      ]
    ],
    [
      "00b693b0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69348.md#insn-00b69384) · [`00b693a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69348.md#insn-00b693a4) · [`00b693c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69348.md#insn-00b693c8)

~~~diff
- 00b69384 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b69384 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b69384 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
- 00b69384 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b69384 bytes bfa22439
- 00b693a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b693a4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b693a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b693a4 bytes 9f9204f9
- 00b693c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6c0:8"]]
- 00b693c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b693c8 bytes 086143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e151bb6a7ac082a722ce97dd92ec799"></a>

### [`00b69880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md) → [`00b698c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b698c4.md) _ZN8firebase4auth10CredentialD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00be0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0db0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 2件 [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00be0e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e00.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

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
    "old": {
      "definition_site": "00b698a8",
      "incomplete_value": false,
      "site": "00b698ac",
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
            "const:e4c:8"
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
      "00b698ec",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b698ec",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b698ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b698ac) · [`00b69898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b69898) · [`00b698a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b698a8)
- 新版 `00b698f0`（命令位置の公開資料なし） · `00b698dc`（命令位置の公開資料なし） · `00b698ec`（命令位置の公開資料なし）

~~~diff
- 00b698ac ["INT_ADD", "register:40f0:8", ["const:b698ac:8", "const:4:8"]]
- 00b698ac ["CALL", null, ["callee:00bde180:8"]]
+ 00b698f0 ["INT_ADD", "register:40f0:8", ["const:b698f0:8", "const:4:8"]]
+ 00b698f0 ["CALL", null, ["callee:00bde180:8"]]
- 00b698ac bytes 21d20194
+ 00b698f0 bytes 24d20194
- 00b69898 ["INT_ADD", "register:40f0:8", ["const:b69898:8", "const:4:8"]]
- 00b69898 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b698dc ["INT_ADD", "register:40f0:8", ["const:b698dc:8", "const:4:8"]]
+ 00b698dc ["CALL", null, ["callee:00bde3e0:8"]]
- 00b69898 bytes bed20194
+ 00b698dc bytes c1d20194
- 00b698a8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b698a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b698a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b698a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b698ec ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b698ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b698ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b698ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b698a8 bytes 00303991
+ 00b698ec bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7543340e71910e230a6034747102b6c"></a>

### [`00b69954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md) → [`00b69998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69998.md) _ZN8firebase4auth10CredentialaSERKS1_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) · 呼出先 4件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 1件 [`00be0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d60.md) · 呼出先 4件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b699d0",
      "incomplete_value": false,
      "site": "00b699d4",
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
    "old": {
      "definition_site": "00b6998c",
      "incomplete_value": false,
      "site": "00b69990",
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
            "const:e4c:8"
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
      "00b699d0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b699d0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b69990) · [`00b6997c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b6997c) · [`00b6998c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b6998c)
- 新版 `00b699d4`（命令位置の公開資料なし） · `00b699c0`（命令位置の公開資料なし） · `00b699d0`（命令位置の公開資料なし）

~~~diff
- 00b69990 ["INT_ADD", "register:40f0:8", ["const:b69990:8", "const:4:8"]]
- 00b69990 ["CALL", null, ["callee:00bde180:8"]]
+ 00b699d4 ["INT_ADD", "register:40f0:8", ["const:b699d4:8", "const:4:8"]]
+ 00b699d4 ["CALL", null, ["callee:00bde180:8"]]
- 00b69990 bytes e8d10194
+ 00b699d4 bytes ebd10194
- 00b6997c ["INT_ADD", "register:40f0:8", ["const:b6997c:8", "const:4:8"]]
- 00b6997c ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b699c0 ["INT_ADD", "register:40f0:8", ["const:b699c0:8", "const:4:8"]]
+ 00b699c0 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6997c bytes 85d20194
+ 00b699c0 bytes 88d20194
- 00b6998c ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6998c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6998c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6998c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b699d0 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b699d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b699d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b699d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6998c bytes 00303991
+ 00b699d0 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f33e00fb1e10050c5440c8a4a5cbb5"></a>

### [`00b69a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md) → [`00b69a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69a68.md) _ZNK8firebase4auth10Credential8providerEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

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
    "old": {
      "definition_site": "00b69a4c",
      "incomplete_value": false,
      "site": "00b69a50",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b69a68",
      "incomplete_value": true,
      "site": "00b69a70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:710:8"
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
      "00b69a90",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69aac",
      "READ",
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
      "00b69a90",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b69aac",
      "READ",
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

- 旧版 [`00b69a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a50) · [`00b69a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a70) · [`00b69a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a3c)
- 新版 `00b69a94`（命令位置の公開資料なし） · `00b69ab4`（命令位置の公開資料なし） · `00b69a80`（命令位置の公開資料なし）

~~~diff
- 00b69a50 ["INT_ADD", "register:40f0:8", ["const:b69a50:8", "const:4:8"]]
- 00b69a50 ["CALL", null, ["callee:00bde180:8"]]
+ 00b69a94 ["INT_ADD", "register:40f0:8", ["const:b69a94:8", "const:4:8"]]
+ 00b69a94 ["CALL", null, ["callee:00bde180:8"]]
- 00b69a50 bytes b8d10194
+ 00b69a94 bytes bbd10194
- 00b69a70 ["INT_ADD", "register:40f0:8", ["const:b69a70:8", "const:4:8"]]
- 00b69a70 ["CALL", null, ["callee:0047495c:8"]]
+ 00b69ab4 ["INT_ADD", "register:40f0:8", ["const:b69ab4:8", "const:4:8"]]
+ 00b69ab4 ["CALL", null, ["callee:0047495c:8"]]
- 00b69a70 bytes bb2be497
+ 00b69ab4 bytes aa2be497
- 00b69a3c ["INT_ADD", "register:40f0:8", ["const:b69a3c:8", "const:4:8"]]
- 00b69a3c ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b69a80 ["INT_ADD", "register:40f0:8", ["const:b69a80:8", "const:4:8"]]
+ 00b69a80 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b69a3c bytes 55d20194
+ 00b69a80 bytes 58d20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2955873da4de311df1306652e8de9ba8"></a>

### [`00b69ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md) → [`00b69afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b69b10",
      "incomplete_value": false,
      "site": "00b69b14",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b69b54",
      "incomplete_value": true,
      "site": "00b69b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b69b58",
      "incomplete_value": true,
      "site": "00b69b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:730:8"
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
      "00b69b38",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69b3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b69c84"
      ]
    ],
    [
      "00b69b54",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b69b38",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69b3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b69cc8"
      ]
    ],
    [
      "00b69b54",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69b14) · [`00b69b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69b58) · [`00b69b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69b6c)
- 新版 `00b69b58`（命令位置の公開資料なし） · `00b69b9c`（命令位置の公開資料なし） · `00b69bb0`（命令位置の公開資料なし）

~~~diff
- 00b69b14 ["INT_ADD", "register:40f0:8", ["const:b69b14:8", "const:4:8"]]
- 00b69b14 ["CALL", null, ["callee:00bde180:8"]]
+ 00b69b58 ["INT_ADD", "register:40f0:8", ["const:b69b58:8", "const:4:8"]]
+ 00b69b58 ["CALL", null, ["callee:00bde180:8"]]
- 00b69b14 bytes 87d10194
+ 00b69b58 bytes 8ad10194
- 00b69b58 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
- 00b69b58 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b69b9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:770:8"]]
+ 00b69b9c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b69b58 bytes 229943f9
+ 00b69b9c bytes 22b943f9
- 00b69b6c ["INT_ADD", "register:40f0:8", ["const:b69b6c:8", "const:4:8"]]
- 00b69b6c ["CALL", null, ["callee:00bddd40:8"]]
+ 00b69bb0 ["INT_ADD", "register:40f0:8", ["const:b69bb0:8", "const:4:8"]]
+ 00b69bb0 ["CALL", null, ["callee:00bddd40:8"]]
- 00b69b6c bytes 61d00194
+ 00b69bb0 bytes 64d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743223e2b2bd59bf8efb63c3f69cc012"></a>

### [`00b69dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md) → [`00b69e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69e40.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)

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
    "old": {
      "definition_site": "00b69e2c",
      "incomplete_value": false,
      "site": "00b69e30",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b69e44",
      "incomplete_value": true,
      "site": "00b69e4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a0:8"
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
      "00b69e70",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69e88",
      "READ",
      [
        "storage",
        "010a19a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69e70",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b69e88",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e30) · [`00b69e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e4c) · [`00b69e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e1c)
- 新版 `00b69e74`（命令位置の公開資料なし） · `00b69e90`（命令位置の公開資料なし） · `00b69e60`（命令位置の公開資料なし）

~~~diff
- 00b69e30 ["INT_ADD", "register:40f0:8", ["const:b69e30:8", "const:4:8"]]
- 00b69e30 ["CALL", null, ["callee:00bde180:8"]]
+ 00b69e74 ["INT_ADD", "register:40f0:8", ["const:b69e74:8", "const:4:8"]]
+ 00b69e74 ["CALL", null, ["callee:00bde180:8"]]
- 00b69e30 bytes c0d00194
+ 00b69e74 bytes c3d00194
- 00b69e4c ["INT_ADD", "register:40f0:8", ["const:b69e4c:8", "const:4:8"]]
- 00b69e4c ["CALL", null, ["callee:0047495c:8"]]
+ 00b69e90 ["INT_ADD", "register:40f0:8", ["const:b69e90:8", "const:4:8"]]
+ 00b69e90 ["CALL", null, ["callee:0047495c:8"]]
- 00b69e4c bytes c42ae497
+ 00b69e90 bytes b32ae497
- 00b69e1c ["INT_ADD", "register:40f0:8", ["const:b69e1c:8", "const:4:8"]]
- 00b69e1c ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b69e60 ["INT_ADD", "register:40f0:8", ["const:b69e60:8", "const:4:8"]]
+ 00b69e60 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b69e1c bytes 5dd10194
+ 00b69e60 bytes 60d10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455be0433b12ac4154a73a87cf34747f"></a>

### [`00b69e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md) → [`00b69ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69ec8.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d50.md) · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 1件 [`00be0da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0da0.md) · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

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
    "old": {
      "definition_site": "00b69eb0",
      "incomplete_value": false,
      "site": "00b69eb4",
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
            "const:e4c:8"
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
      "00b69ef4",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b69ef4",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69eb4) · [`00b69ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69ea0) · [`00b69eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69eb0)
- 新版 `00b69ef8`（命令位置の公開資料なし） · `00b69ee4`（命令位置の公開資料なし） · `00b69ef4`（命令位置の公開資料なし）

~~~diff
- 00b69eb4 ["INT_ADD", "register:40f0:8", ["const:b69eb4:8", "const:4:8"]]
- 00b69eb4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b69ef8 ["INT_ADD", "register:40f0:8", ["const:b69ef8:8", "const:4:8"]]
+ 00b69ef8 ["CALL", null, ["callee:00bde180:8"]]
- 00b69eb4 bytes 9fd00194
+ 00b69ef8 bytes a2d00194
- 00b69ea0 ["INT_ADD", "register:40f0:8", ["const:b69ea0:8", "const:4:8"]]
- 00b69ea0 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b69ee4 ["INT_ADD", "register:40f0:8", ["const:b69ee4:8", "const:4:8"]]
+ 00b69ee4 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b69ea0 bytes 3cd10194
+ 00b69ee4 bytes 3fd10194
- 00b69eb0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b69eb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b69eb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b69eb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b69ef4 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b69ef4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b69ef4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b69ef4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b69eb0 bytes 00303991
+ 00b69ef4 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b1cd212f6f07df8e2ed1078c2e19d38"></a>

### [`00b69f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md) → [`00b69f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69f58.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b69f50",
      "incomplete_value": false,
      "site": "00b69f54",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b69f7c",
      "incomplete_value": true,
      "site": "00b69f90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b69f80",
      "incomplete_value": true,
      "site": "00b69f90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b69f78",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69f94",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69fc0",
      "READ",
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
      "00b69f78",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69f94",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b69fc0",
      "READ",
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

- 旧版 [`00b69f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69f54) · [`00b69f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69f90) · [`00b69fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69fd4)
- 新版 `00b69f98`（命令位置の公開資料なし） · `00b69fd4`（命令位置の公開資料なし） · `00b6a018`（命令位置の公開資料なし）

~~~diff
- 00b69f54 ["INT_ADD", "register:40f0:8", ["const:b69f54:8", "const:4:8"]]
- 00b69f54 ["CALL", null, ["callee:00bde180:8"]]
+ 00b69f98 ["INT_ADD", "register:40f0:8", ["const:b69f98:8", "const:4:8"]]
+ 00b69f98 ["CALL", null, ["callee:00bde180:8"]]
- 00b69f54 bytes 77d00194
+ 00b69f98 bytes 7ad00194
- 00b69f90 ["INT_ADD", "register:40f0:8", ["const:b69f90:8", "const:4:8"]]
- 00b69f90 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b69fd4 ["INT_ADD", "register:40f0:8", ["const:b69fd4:8", "const:4:8"]]
+ 00b69fd4 ["CALL", null, ["callee:00bddd40:8"]]
- 00b69f90 bytes 58cf0194
+ 00b69fd4 bytes 5bcf0194
- 00b69fd4 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b69fd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b69fd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b69fd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6a018 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6a018 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a018 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a018 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b69fd4 bytes 00303991
+ 00b6a018 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1dcdeb53aa3a28b47070d8bd6bfab5b"></a>

### [`00b6a060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md) → [`00b6a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a0a4.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a09c",
      "incomplete_value": false,
      "site": "00b6a0a0",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b6a0c8",
      "incomplete_value": true,
      "site": "00b6a0dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a0cc",
      "incomplete_value": true,
      "site": "00b6a0dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6a0c4",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a0c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a16c"
      ]
    ],
    [
      "00b6a0e0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a0c4",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a0c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a1b0"
      ]
    ],
    [
      "00b6a0e0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md#insn-00b6a0a0) · [`00b6a0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md#insn-00b6a0dc) · [`00b6a120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md#insn-00b6a120)
- 新版 `00b6a0e4`（命令位置の公開資料なし） · `00b6a120`（命令位置の公開資料なし） · `00b6a164`（命令位置の公開資料なし）

~~~diff
- 00b6a0a0 ["INT_ADD", "register:40f0:8", ["const:b6a0a0:8", "const:4:8"]]
- 00b6a0a0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a0e4 ["INT_ADD", "register:40f0:8", ["const:b6a0e4:8", "const:4:8"]]
+ 00b6a0e4 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a0a0 bytes 24d00194
+ 00b6a0e4 bytes 27d00194
- 00b6a0dc ["INT_ADD", "register:40f0:8", ["const:b6a0dc:8", "const:4:8"]]
- 00b6a0dc ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a120 ["INT_ADD", "register:40f0:8", ["const:b6a120:8", "const:4:8"]]
+ 00b6a120 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a0dc bytes 05cf0194
+ 00b6a120 bytes 08cf0194
- 00b6a120 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6a120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6a120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6a120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6a164 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6a164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6a120 bytes 00303991
+ 00b6a164 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3d60b52abcac2b498e6a445aa7712ce"></a>

### [`00b6a1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md) → [`00b6a1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a1f0.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb30.md) · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00bddb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb80.md) · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a1e8",
      "incomplete_value": false,
      "site": "00b6a1ec",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b6a24c",
      "incomplete_value": false,
      "site": "00b6a250",
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
            "const:1c7:8"
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
      "definition_site": "00b6a2bc",
      "incomplete_value": true,
      "site": "00b6a2d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6a278",
      "incomplete_value": true,
      "site": "00b6a28c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6a208",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a22c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6a290",
      "PARAM",
      [
        "storage",
        "002a71c7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a208",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a22c",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b6a290",
      "PARAM",
      [
        "storage",
        "002a7261",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a1ec) · [`00b6a250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a250) · [`00b6a28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a28c)
- 新版 `00b6a230`（命令位置の公開資料なし） · `00b6a294`（命令位置の公開資料なし） · `00b6a2d0`（命令位置の公開資料なし）

~~~diff
- 00b6a1ec ["INT_ADD", "register:40f0:8", ["const:b6a1ec:8", "const:4:8"]]
- 00b6a1ec ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a230 ["INT_ADD", "register:40f0:8", ["const:b6a230:8", "const:4:8"]]
+ 00b6a230 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a1ec bytes d1cf0194
+ 00b6a230 bytes d4cf0194
- 00b6a250 ["INT_ADD", "register:40f0:8", ["const:b6a250:8", "const:4:8"]]
- 00b6a250 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b6a294 ["INT_ADD", "register:40f0:8", ["const:b6a294:8", "const:4:8"]]
+ 00b6a294 ["CALL", null, ["callee:00bdde40:8"]]
- 00b6a250 bytes e8ce0194
+ 00b6a294 bytes ebce0194
- 00b6a28c ["INT_ADD", "register:40f0:8", ["const:b6a28c:8", "const:4:8"]]
- 00b6a28c ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a2d0 ["INT_ADD", "register:40f0:8", ["const:b6a2d0:8", "const:4:8"]]
+ 00b6a2d0 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a28c bytes 99ce0194
+ 00b6a2d0 bytes 9cce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d140558dac167d5be6d779808b2325"></a>

### [`00b6a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md) → [`00b6a394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a394.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a38c",
      "incomplete_value": false,
      "site": "00b6a390",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b6a3b8",
      "incomplete_value": true,
      "site": "00b6a3cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b6a3bc",
      "incomplete_value": true,
      "site": "00b6a3cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6a3b4",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a3b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a45c"
      ]
    ],
    [
      "00b6a3d0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a3b4",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a3b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a4a0"
      ]
    ],
    [
      "00b6a3d0",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a390) · [`00b6a3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a3cc) · [`00b6a410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a410)
- 新版 `00b6a3d4`（命令位置の公開資料なし） · `00b6a410`（命令位置の公開資料なし） · `00b6a454`（命令位置の公開資料なし）

~~~diff
- 00b6a390 ["INT_ADD", "register:40f0:8", ["const:b6a390:8", "const:4:8"]]
- 00b6a390 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a3d4 ["INT_ADD", "register:40f0:8", ["const:b6a3d4:8", "const:4:8"]]
+ 00b6a3d4 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a390 bytes 68cf0194
+ 00b6a3d4 bytes 6bcf0194
- 00b6a3cc ["INT_ADD", "register:40f0:8", ["const:b6a3cc:8", "const:4:8"]]
- 00b6a3cc ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a410 ["INT_ADD", "register:40f0:8", ["const:b6a410:8", "const:4:8"]]
+ 00b6a410 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a3cc bytes 49ce0194
+ 00b6a410 bytes 4cce0194
- 00b6a410 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6a410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6a410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6a410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6a454 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6a454 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a454 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6a454 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6a410 bytes 00303991
+ 00b6a454 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae0f6c2c28ad0f312f38c1cff0a2908f"></a>

### [`00b6a49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md) → [`00b6a4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a4e0.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a4e0",
      "incomplete_value": false,
      "site": "00b6a4e4",
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
            "const:e4c:8"
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
    "old": {
      "definition_site": "00b6a524",
      "incomplete_value": true,
      "site": "00b6a53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b6a528",
      "incomplete_value": true,
      "site": "00b6a53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
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
      "00b6a508",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a524",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6a568",
      "READ",
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
      "00b6a508",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a524",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b6a568",
      "READ",
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

- 旧版 [`00b6a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a4e4) · [`00b6a528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a528) · [`00b6a53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a53c)
- 新版 `00b6a528`（命令位置の公開資料なし） · `00b6a56c`（命令位置の公開資料なし） · `00b6a580`（命令位置の公開資料なし）

~~~diff
- 00b6a4e4 ["INT_ADD", "register:40f0:8", ["const:b6a4e4:8", "const:4:8"]]
- 00b6a4e4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a528 ["INT_ADD", "register:40f0:8", ["const:b6a528:8", "const:4:8"]]
+ 00b6a528 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a4e4 bytes 13cf0194
+ 00b6a528 bytes 16cf0194
- 00b6a528 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d0:8"]]
- 00b6a528 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6a56c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:810:8"]]
+ 00b6a56c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6a528 bytes 22e943f9
+ 00b6a56c bytes 220944f9
- 00b6a53c ["INT_ADD", "register:40f0:8", ["const:b6a53c:8", "const:4:8"]]
- 00b6a53c ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a580 ["INT_ADD", "register:40f0:8", ["const:b6a580:8", "const:4:8"]]
+ 00b6a580 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a53c bytes edcd0194
+ 00b6a580 bytes f0cd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

