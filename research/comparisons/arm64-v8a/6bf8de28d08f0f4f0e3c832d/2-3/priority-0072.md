# v16.0.2 → v16.0.3 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-13f6edcfdb44a36171ef0483580954d9"></a>

### [`00b408d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md) → [`00b418c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b418c8.md) _ZN8firebase9analytics22analytics_consent_type15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

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
      "definition_site": "00b41920",
      "incomplete_value": true,
      "site": "00b41920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4092c",
      "incomplete_value": true,
      "site": "00b4092c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "definition_site": "00b418fc",
      "incomplete_value": true,
      "site": "00b41908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40908",
      "incomplete_value": true,
      "site": "00b40914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a0:8"
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
      "00b418dc",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b418fc",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41920",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b418dc",
      "READ",
      [
        "storage",
        "01126468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b418fc",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41920",
      "WRITE",
      [
        "storage",
        "01126468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b40914) · [`00b4092c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b4092c) · [`00b408e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b408e4)
- 新版 [`00b41908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b418c8.md#insn-00b41908) · [`00b41920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b418c8.md#insn-00b41920) · [`00b418d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b418c8.md#insn-00b418d8)

~~~diff
- 00b40914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40914 ["INT_ADD", "register:40f0:8", ["const:b40914:8", "const:4:8"]]
- 00b40914 ["CALLIND", null, ["register:0:8"]]
+ 00b41908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41908 ["INT_ADD", "register:40f0:8", ["const:b41908:8", "const:4:8"]]
+ 00b41908 ["CALLIND", null, ["register:0:8"]]
- 00b40914 bytes 00013fd6
+ 00b41908 bytes 00013fd6
- 00b4092c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4092c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4a8:8"]]
- 00b4092c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b41920 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b41920 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:468:8"]]
+ 00b41920 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4092c bytes a0a21239
+ 00b41920 bytes a0a21139
- 00b408e4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b418d8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b408e4 bytes 352f00b0
+ 00b418d8 bytes 352f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d34e6c9b440fbfde96df64b29e94a33"></a>

### [`00b40940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40940.md) → [`00b41934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41934.md) _ZN8firebase9analytics22analytics_consent_type12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

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
      "definition_site": "00b41970",
      "incomplete_value": true,
      "site": "00b41970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4097c",
      "incomplete_value": true,
      "site": "00b4097c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "definition_site": "00b41990",
      "incomplete_value": true,
      "site": "00b41990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4099c",
      "incomplete_value": true,
      "site": "00b4099c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "definition_site": "00b4194c",
      "incomplete_value": true,
      "site": "00b4194c",
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
      "definition_site": "00b40958",
      "incomplete_value": true,
      "site": "00b40958",
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
      "00b41948",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41954",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41970",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b41948",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41954",
      "READ",
      [
        "storage",
        "01126468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41970",
      "WRITE",
      [
        "storage",
        "01126468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4097c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40940.md#insn-00b4097c) · [`00b4099c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40940.md#insn-00b4099c) · [`00b40950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40940.md#insn-00b40950)
- 新版 [`00b41970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41934.md#insn-00b41970) · [`00b41990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41934.md#insn-00b41990) · [`00b41944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41934.md#insn-00b41944)

~~~diff
- 00b4097c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4097c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4097c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4a8:8"]]
- 00b4097c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b41970 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b41970 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b41970 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:468:8"]]
+ 00b41970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4097c bytes bfa21239
+ 00b41970 bytes bfa21139
- 00b4099c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b4099c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4099c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b41990 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b41990 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b41990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4099c bytes 9f5202f9
+ 00b41990 bytes 9f3202f9
- 00b40950 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b41944 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b40950 bytes 342f00b0
+ 00b41944 bytes 342f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d921e3eb4bdc2af1169944086fd4251f"></a>

### [`00b409b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b409b0.md) → [`00b419a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b419a4.md) _ZN8firebase9analytics22analytics_consent_type14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b419e4",
      "incomplete_value": true,
      "site": "00b419e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b409f0",
      "incomplete_value": true,
      "site": "00b409f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "definition_site": "00b419c0",
      "incomplete_value": true,
      "site": "00b419c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b409cc",
      "incomplete_value": true,
      "site": "00b409cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b409cc"
      ],
      [
        "FALL_THROUGH",
        "00b419c0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b419c0",
      "incomplete_value": true,
      "site": "00b419e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b409cc",
      "incomplete_value": true,
      "site": "00b409f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b419b8",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b419c8",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b419e4",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b419b8",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b419c8",
      "PARAM",
      [
        "storage",
        "002b25c5",
        null,
        "string"
      ]
    ],
    [
      "00b419e4",
      "WRITE",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b409f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b409b0.md#insn-00b409f0) · [`00b409bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b409b0.md#insn-00b409bc) · [`00b409c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b409b0.md#insn-00b409c4)
- 新版 [`00b419e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b419a4.md#insn-00b419e4) · [`00b419b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b419a4.md#insn-00b419b0) · [`00b419b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b419a4.md#insn-00b419b8)

~~~diff
- 00b409f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b409f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b419e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b419e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b409f0 bytes 805202f9
+ 00b419e4 bytes 803202f9
- 00b409bc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b419b0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b409bc bytes 342f00b0
+ 00b419b0 bytes 342f00b0
- 00b409c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b409c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b419b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b419b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b409c4 bytes 815242f9
+ 00b419b8 bytes 813242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab8e28867869ef0e5bcdda2faa63de0e"></a>

### [`00b40a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40a5c.md) → [`00b41a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41a50.md) _ZN8firebase9analytics22analytics_consent_type13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41a90",
      "incomplete_value": true,
      "site": "00b41a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40a9c",
      "incomplete_value": true,
      "site": "00b40a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "definition_site": "00b41a6c",
      "incomplete_value": true,
      "site": "00b41a6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40a78",
      "incomplete_value": true,
      "site": "00b40a78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b40a78"
      ],
      [
        "FALL_THROUGH",
        "00b41a6c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b41a6c",
      "incomplete_value": true,
      "site": "00b41a90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40a78",
      "incomplete_value": true,
      "site": "00b40a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b41a64",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41a74",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b41a90",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41a64",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41a74",
      "PARAM",
      [
        "storage",
        "002b25c5",
        null,
        "string"
      ]
    ],
    [
      "00b41a90",
      "WRITE",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40a5c.md#insn-00b40a9c) · [`00b40a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40a5c.md#insn-00b40a68) · [`00b40a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40a5c.md#insn-00b40a70)
- 新版 [`00b41a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41a50.md#insn-00b41a90) · [`00b41a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41a50.md#insn-00b41a5c) · [`00b41a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41a50.md#insn-00b41a64)

~~~diff
- 00b40a9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b40a9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41a90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b41a90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40a9c bytes 805202f9
+ 00b41a90 bytes 803202f9
- 00b40a68 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b41a5c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b40a68 bytes 342f00b0
+ 00b41a5c bytes 342f00b0
- 00b40a70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b40a70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b41a64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b41a64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40a70 bytes 815242f9
+ 00b41a64 bytes 813242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-842e0abed4bfed35ac809c388de0bd6f"></a>

### [`00b40acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40acc.md) → [`00b41ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41ac0.md) _ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b41aec",
      "incomplete_value": true,
      "site": "00b41af8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b40af8",
      "incomplete_value": true,
      "site": "00b40b04",
      "value": [
        "LOAD",
        "8",
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
      "00b41adc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b41aec",
      "DATA",
      [
        "storage",
        "011254b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41adc",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b41aec",
      "DATA",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40acc.md#insn-00b40ae8) · [`00b40aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40acc.md#insn-00b40aec) · [`00b40af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40acc.md#insn-00b40af0)
- 新版 [`00b41adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41ac0.md#insn-00b41adc) · [`00b41ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41ac0.md#insn-00b41ae0) · [`00b41ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41ac0.md#insn-00b41ae4)

~~~diff
- 00b40ae8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b40ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b41adc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b41adc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41adc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41adc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40ae8 bytes 00341591
+ 00b41adc bytes 00681891
- 00b40aec ["INT_ADD", "register:40f0:8", ["const:b40aec:8", "const:4:8"]]
- 00b40aec ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b41ae0 ["INT_ADD", "register:40f0:8", ["const:b41ae0:8", "const:4:8"]]
+ 00b41ae0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b40aec bytes 79690494
+ 00b41ae0 bytes 70690494
- 00b40af0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b41ae4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b40af0 bytes 282f00b0
+ 00b41ae4 bytes 282f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed898320650625f4f2f1c64b7debac6"></a>

### [`00b40b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b08.md) → [`00b41afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41afc.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41b28",
      "incomplete_value": true,
      "site": "00b41b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b34",
      "incomplete_value": true,
      "site": "00b40b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41b10",
      "incomplete_value": true,
      "site": "00b41b10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b1c",
      "incomplete_value": true,
      "site": "00b40b1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41b1c",
      "incomplete_value": false,
      "site": "00b41b20",
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
            "const:ab3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b28",
      "incomplete_value": false,
      "site": "00b40b2c",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41b0c",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b1c",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41b28",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41b0c",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b1c",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41b28",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b08.md#insn-00b40b2c) · [`00b40b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b08.md#insn-00b40b34) · [`00b40b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b08.md#insn-00b40b14)
- 新版 [`00b41b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41afc.md#insn-00b41b20) · [`00b41b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41afc.md#insn-00b41b28) · [`00b41b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41afc.md#insn-00b41b08)

~~~diff
- 00b40b2c ["INT_ADD", "register:40f0:8", ["const:b40b2c:8", "const:4:8"]]
- 00b40b2c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41b20 ["INT_ADD", "register:40f0:8", ["const:b41b20:8", "const:4:8"]]
+ 00b41b20 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40b2c bytes 2d690494
+ 00b41b20 bytes 24690494
- 00b40b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
- 00b40b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:498:8"]]
+ 00b41b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40b34 bytes 606e02f9
+ 00b41b28 bytes 604e02f9
- 00b40b14 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b41b08 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b40b14 bytes 332f00b0
+ 00b41b08 bytes 332f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d55e66888f105c150d5e2e95a85ce1"></a>

### [`00b40b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b48.md) → [`00b41b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b3c.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41b68",
      "incomplete_value": true,
      "site": "00b41b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b74",
      "incomplete_value": true,
      "site": "00b40b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41b50",
      "incomplete_value": true,
      "site": "00b41b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b5c",
      "incomplete_value": true,
      "site": "00b40b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b40b5c"
      ],
      [
        "FALL_THROUGH",
        "00b41b50"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b41b50",
      "incomplete_value": true,
      "site": "00b41b68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b5c",
      "incomplete_value": true,
      "site": "00b40b74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b41b4c",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b58",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41b68",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41b4c",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b58",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41b68",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b48.md#insn-00b40b74) · [`00b40b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b48.md#insn-00b40b54) · [`00b40b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b48.md#insn-00b40b58)
- 新版 [`00b41b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b3c.md#insn-00b41b68) · [`00b41b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b3c.md#insn-00b41b48) · [`00b41b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b3c.md#insn-00b41b4c)

~~~diff
- 00b40b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
- 00b40b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41b68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:498:8"]]
+ 00b41b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40b74 bytes 606e02f9
+ 00b41b68 bytes 604e02f9
- 00b40b54 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b41b48 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b40b54 bytes 332f00b0
+ 00b41b48 bytes 332f00b0
- 00b40b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
- 00b40b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b41b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:498:8"]]
+ 00b41b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40b58 bytes 686e42f9
+ 00b41b4c bytes 684e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aa1a6cb46ee19070a2a838715726e1f"></a>

### [`00b40b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md) → [`00b41b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b7c.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41bac",
      "incomplete_value": true,
      "site": "00b41bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40bb8",
      "incomplete_value": true,
      "site": "00b40bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41b90",
      "incomplete_value": true,
      "site": "00b41b90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b9c",
      "incomplete_value": true,
      "site": "00b40b9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41b9c",
      "incomplete_value": false,
      "site": "00b41ba4",
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
            "const:ab3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40ba8",
      "incomplete_value": false,
      "site": "00b40bb0",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41b8c",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b9c",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41bac",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41b8c",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b9c",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41bac",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md#insn-00b40bb0) · [`00b40bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md#insn-00b40bb8) · [`00b40b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md#insn-00b40b94)
- 新版 [`00b41ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b7c.md#insn-00b41ba4) · [`00b41bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b7c.md#insn-00b41bac) · [`00b41b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41b7c.md#insn-00b41b88)

~~~diff
- 00b40bb0 ["INT_ADD", "register:40f0:8", ["const:b40bb0:8", "const:4:8"]]
- 00b40bb0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41ba4 ["INT_ADD", "register:40f0:8", ["const:b41ba4:8", "const:4:8"]]
+ 00b41ba4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40bb0 bytes 0c690494
+ 00b41ba4 bytes 03690494
- 00b40bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
- 00b40bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:498:8"]]
+ 00b41bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40bb8 bytes 606e02f9
+ 00b41bac bytes 604e02f9
- 00b40b94 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b41b88 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b40b94 bytes 332f00b0
+ 00b41b88 bytes 332f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6b6b1a99f5fe06b71b7ffc5aa1201c1"></a>

### [`00b40bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md) → [`00b41bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41bc0.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41bf0",
      "incomplete_value": true,
      "site": "00b41bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40bfc",
      "incomplete_value": true,
      "site": "00b40bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41bd4",
      "incomplete_value": true,
      "site": "00b41bd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40be0",
      "incomplete_value": true,
      "site": "00b40be0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41bdc",
      "incomplete_value": false,
      "site": "00b41be8",
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
            "const:ab3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40be8",
      "incomplete_value": false,
      "site": "00b40bf4",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41bd0",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41bdc",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41bf0",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41bd0",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41bdc",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41bf0",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bf4) · [`00b40bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bfc) · [`00b40bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bd8)
- 新版 [`00b41be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41bc0.md#insn-00b41be8) · [`00b41bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41bc0.md#insn-00b41bf0) · [`00b41bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41bc0.md#insn-00b41bcc)

~~~diff
- 00b40bf4 ["INT_ADD", "register:40f0:8", ["const:b40bf4:8", "const:4:8"]]
- 00b40bf4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41be8 ["INT_ADD", "register:40f0:8", ["const:b41be8:8", "const:4:8"]]
+ 00b41be8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40bf4 bytes fb680494
+ 00b41be8 bytes f2680494
- 00b40bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
- 00b40bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41bf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:498:8"]]
+ 00b41bf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40bfc bytes 606e02f9
+ 00b41bf0 bytes 604e02f9
- 00b40bd8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b41bcc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b40bd8 bytes 332f00b0
+ 00b41bcc bytes 332f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96de36ef298c08dc815348e0e2b470f4"></a>

### [`00b40c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md) → [`00b41c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c10.md) _ZN8firebase9analytics24analytics_consent_status15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

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
      "definition_site": "00b41c68",
      "incomplete_value": true,
      "site": "00b41c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c74",
      "incomplete_value": true,
      "site": "00b40c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "definition_site": "00b41c44",
      "incomplete_value": true,
      "site": "00b41c50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c50",
      "incomplete_value": true,
      "site": "00b40c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d8:8"
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
      "00b41c24",
      "READ",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41c44",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41c68",
      "WRITE",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b41c24",
      "READ",
      [
        "storage",
        "011264a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41c44",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41c68",
      "WRITE",
      [
        "storage",
        "011264a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c5c) · [`00b40c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c74) · [`00b40c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c2c)
- 新版 [`00b41c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c10.md#insn-00b41c50) · [`00b41c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c10.md#insn-00b41c68) · [`00b41c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c10.md#insn-00b41c20)

~~~diff
- 00b40c5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40c5c ["INT_ADD", "register:40f0:8", ["const:b40c5c:8", "const:4:8"]]
- 00b40c5c ["CALLIND", null, ["register:0:8"]]
+ 00b41c50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41c50 ["INT_ADD", "register:40f0:8", ["const:b41c50:8", "const:4:8"]]
+ 00b41c50 ["CALLIND", null, ["register:0:8"]]
- 00b40c5c bytes 00013fd6
+ 00b41c50 bytes 00013fd6
- 00b40c74 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b40c74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4e0:8"]]
- 00b40c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b41c68 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b41c68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4a0:8"]]
+ 00b41c68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b40c74 bytes a0821339
+ 00b41c68 bytes a0821239
- 00b40c2c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b41c20 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b40c2c bytes 352f00b0
+ 00b41c20 bytes 352f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc59698053783edbca2ad7f15cfa9fcd"></a>

### [`00b40c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md) → [`00b41c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c7c.md) _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

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
      "definition_site": "00b41cb8",
      "incomplete_value": true,
      "site": "00b41cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40cc4",
      "incomplete_value": true,
      "site": "00b40cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "definition_site": "00b41cd8",
      "incomplete_value": true,
      "site": "00b41cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40ce4",
      "incomplete_value": true,
      "site": "00b40ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41c94",
      "incomplete_value": true,
      "site": "00b41c94",
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
      "definition_site": "00b40ca0",
      "incomplete_value": true,
      "site": "00b40ca0",
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
      "00b41c90",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41c9c",
      "READ",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41cb8",
      "WRITE",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b41c90",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41c9c",
      "READ",
      [
        "storage",
        "011264a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b41cb8",
      "WRITE",
      [
        "storage",
        "011264a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40cc4) · [`00b40ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40ce0) · [`00b40ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40ce4)
- 新版 [`00b41cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c7c.md#insn-00b41cb8) · [`00b41cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c7c.md#insn-00b41cd4) · [`00b41cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41c7c.md#insn-00b41cd8)

~~~diff
- 00b40cc4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b40cc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b40cc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4e0:8"]]
- 00b40cc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b41cb8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b41cb8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b41cb8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4a0:8"]]
+ 00b41cb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b40cc4 bytes bf821339
+ 00b41cb8 bytes bf821239
- 00b40ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40ce0 ["INT_ADD", "register:40f0:8", ["const:b40ce0:8", "const:4:8"]]
- 00b40ce0 ["CALLIND", null, ["register:0:8"]]
+ 00b41cd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41cd4 ["INT_ADD", "register:40f0:8", ["const:b41cd4:8", "const:4:8"]]
+ 00b41cd4 ["CALLIND", null, ["register:0:8"]]
- 00b40ce0 bytes 00013fd6
+ 00b41cd4 bytes 00013fd6
- 00b40ce4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
- 00b40ce4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b40ce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b41cd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:498:8"]]
+ 00b41cd8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b41cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b40ce4 bytes 9f6e02f9
+ 00b41cd8 bytes 9f4e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944457cdf3e98e6e77023f9f31af379b"></a>

### [`00b40cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md) → [`00b41cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41cec.md) _ZN8firebase9analytics24analytics_consent_status14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b41d2c",
      "incomplete_value": true,
      "site": "00b41d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40d38",
      "incomplete_value": true,
      "site": "00b40d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41d08",
      "incomplete_value": true,
      "site": "00b41d08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40d14",
      "incomplete_value": true,
      "site": "00b40d14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41d10",
      "incomplete_value": false,
      "site": "00b41d24",
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
            "const:ab3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40d1c",
      "incomplete_value": false,
      "site": "00b40d30",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41d00",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41d10",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41d2c",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41d00",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41d10",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41d2c",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d30) · [`00b40d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d38) · [`00b40d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d04)
- 新版 [`00b41d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41cec.md#insn-00b41d24) · [`00b41d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41cec.md#insn-00b41d2c) · [`00b41cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41cec.md#insn-00b41cf8)

~~~diff
- 00b40d30 ["INT_ADD", "register:40f0:8", ["const:b40d30:8", "const:4:8"]]
- 00b40d30 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41d24 ["INT_ADD", "register:40f0:8", ["const:b41d24:8", "const:4:8"]]
+ 00b41d24 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40d30 bytes ac680494
+ 00b41d24 bytes a3680494
- 00b40d38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
- 00b40d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:498:8"]]
+ 00b41d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40d38 bytes 806e02f9
+ 00b41d2c bytes 804e02f9
- 00b40d04 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b41cf8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b40d04 bytes 342f00b0
+ 00b41cf8 bytes 342f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3088ed5c2d740381065703cbe2de38e"></a>

### [`00b40d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md) → [`00b41d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d5c.md) _ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b41d78",
      "incomplete_value": false,
      "site": "00b41d7c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40d84",
      "incomplete_value": false,
      "site": "00b40d88",
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
            "const:30b:8"
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
      "definition_site": "00b41d88",
      "incomplete_value": true,
      "site": "00b41d94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b40d94",
      "incomplete_value": true,
      "site": "00b40da0",
      "value": [
        "LOAD",
        "8",
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
      "00b41d78",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b41d88",
      "DATA",
      [
        "storage",
        "011254e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b41d78",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b41d88",
      "DATA",
      [
        "storage",
        "011264a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d88) · [`00b40d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d84) · [`00b40d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d8c)
- 新版 [`00b41d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d5c.md#insn-00b41d7c) · [`00b41d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d5c.md#insn-00b41d78) · [`00b41d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d5c.md#insn-00b41d80)

~~~diff
- 00b40d88 ["INT_ADD", "register:40f0:8", ["const:b40d88:8", "const:4:8"]]
- 00b40d88 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b41d7c ["INT_ADD", "register:40f0:8", ["const:b41d7c:8", "const:4:8"]]
+ 00b41d7c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b40d88 bytes d2680494
+ 00b41d7c bytes c9680494
- 00b40d84 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b40d84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40d84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40d84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b41d78 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b41d78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41d78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41d78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40d84 bytes 002c0c91
+ 00b41d78 bytes 008c1191
- 00b40d8c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b41d80 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b40d8c bytes 282f00b0
+ 00b41d80 bytes 282f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abcfd4b2611cae2a5f86438f1760b9ad"></a>

### [`00b40da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md) → [`00b41d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d98.md) _ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b41dd8",
      "incomplete_value": true,
      "site": "00b41dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40de4",
      "incomplete_value": true,
      "site": "00b40de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "00b41db4",
      "incomplete_value": true,
      "site": "00b41db4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40dc0",
      "incomplete_value": true,
      "site": "00b40dc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41dbc",
      "incomplete_value": false,
      "site": "00b41dd0",
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
            "const:ab3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40dc8",
      "incomplete_value": false,
      "site": "00b40ddc",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41dac",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41dbc",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b41dd8",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41dac",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41dbc",
      "PARAM",
      [
        "storage",
        "002a3ab3",
        null,
        "string"
      ]
    ],
    [
      "00b41dd8",
      "WRITE",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md#insn-00b40ddc) · [`00b40de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md#insn-00b40de4) · [`00b40db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md#insn-00b40db0)
- 新版 [`00b41dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d98.md#insn-00b41dd0) · [`00b41dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d98.md#insn-00b41dd8) · [`00b41da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41d98.md#insn-00b41da4)

~~~diff
- 00b40ddc ["INT_ADD", "register:40f0:8", ["const:b40ddc:8", "const:4:8"]]
- 00b40ddc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41dd0 ["INT_ADD", "register:40f0:8", ["const:b41dd0:8", "const:4:8"]]
+ 00b41dd0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40ddc bytes 81680494
+ 00b41dd0 bytes 78680494
- 00b40de4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
- 00b40de4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b41dd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:498:8"]]
+ 00b41dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40de4 bytes 806e02f9
+ 00b41dd8 bytes 804e02f9
- 00b40db0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b41da4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b40db0 bytes 342f00b0
+ 00b41da4 bytes 342f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0901de584acc463bd61741bed632b25a"></a>

### [`00b40e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md) → [`00b41e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e08.md) _ZN8firebase9analytics24analytics_consent_status10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b41e24",
      "incomplete_value": false,
      "site": "00b41e28",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40e30",
      "incomplete_value": false,
      "site": "00b40e34",
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
            "const:54d:8"
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
      "definition_site": "00b41e34",
      "incomplete_value": true,
      "site": "00b41e40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b40e40",
      "incomplete_value": true,
      "site": "00b40e4c",
      "value": [
        "LOAD",
        "8",
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
      "00b41e24",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b41e34",
      "DATA",
      [
        "storage",
        "011254f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41e24",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b41e34",
      "DATA",
      [
        "storage",
        "011264b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e34) · [`00b40e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e30) · [`00b40e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e38)
- 新版 [`00b41e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e08.md#insn-00b41e28) · [`00b41e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e08.md#insn-00b41e24) · [`00b41e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e08.md#insn-00b41e2c)

~~~diff
- 00b40e34 ["INT_ADD", "register:40f0:8", ["const:b40e34:8", "const:4:8"]]
- 00b40e34 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b41e28 ["INT_ADD", "register:40f0:8", ["const:b41e28:8", "const:4:8"]]
+ 00b41e28 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b40e34 bytes a7680494
+ 00b41e28 bytes 9e680494
- 00b40e30 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b40e30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40e30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40e30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b41e24 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b41e24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41e24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b41e24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40e30 bytes 00341591
+ 00b41e24 bytes 00681891
- 00b40e38 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b41e2c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b40e38 bytes 282f00b0
+ 00b41e2c bytes 282f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-494cc6afe239ae091b26a31d28b1ac1e"></a>

### [`00b40e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e50.md) → [`00b41e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e44.md) _ZN8firebase9analytics10InitializeERKNS_3AppE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa30.md) · 呼出先 13件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad90.md) [`00c5adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5adc0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md)
- 新版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba00.md) · 呼出先 13件 [`00c5bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd60.md) [`00c5bd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd90.md) [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) [`00c5bf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf40.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.01% / 新版 82.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 18件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b41f00",
      "incomplete_value": true,
      "site": "00b41f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40f0c",
      "incomplete_value": true,
      "site": "00b40f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b41f58",
      "incomplete_value": true,
      "site": "00b41f58",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40f64",
      "incomplete_value": true,
      "site": "00b40f64",
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
            "const:4a0:8"
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
      "definition_site": "00b41fb0",
      "incomplete_value": true,
      "site": "00b41fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40fbc",
      "incomplete_value": true,
      "site": "00b40fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41e60",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41e6c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b41e7c",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b41e60",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41e6c",
      "READ",
      [
        "storage",
        "00c9c748",
        null,
        "pointer"
      ]
    ],
    [
      "00b41e7c",
      "READ",
      [
        "storage",
        "00ca56d0",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e50.md#insn-00b40eac) · [`00b40ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e50.md#insn-00b40ec4) · [`00b40f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e50.md#insn-00b40f04)
- 新版 [`00b41ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e44.md#insn-00b41ea0) · [`00b41eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e44.md#insn-00b41eb8) · [`00b41ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41e44.md#insn-00b41ef8)

~~~diff
- 00b40eac ["INT_ADD", "register:40f0:8", ["const:b40eac:8", "const:4:8"]]
- 00b40eac ["CALL", null, ["callee:00c5c080:8"]]
+ 00b41ea0 ["INT_ADD", "register:40f0:8", ["const:b41ea0:8", "const:4:8"]]
+ 00b41ea0 ["CALL", null, ["callee:00c5c080:8"]]
- 00b40eac bytes 81680494
+ 00b41ea0 bytes 78680494
- 00b40ec4 ["INT_ADD", "register:40f0:8", ["const:b40ec4:8", "const:4:8"]]
- 00b40ec4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b41eb8 ["INT_ADD", "register:40f0:8", ["const:b41eb8:8", "const:4:8"]]
+ 00b41eb8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b40ec4 bytes 83680494
+ 00b41eb8 bytes 7a680494
- 00b40f04 ["INT_ADD", "register:40f0:8", ["const:b40f04:8", "const:4:8"]]
- 00b40f04 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b41ef8 ["INT_ADD", "register:40f0:8", ["const:b41ef8:8", "const:4:8"]]
+ 00b41ef8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b40f04 bytes 37680494
+ 00b41ef8 bytes 2e680494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f4e6b0034fbab5c79fd33a21bdefb9"></a>

### [`00b411f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md) → [`00b421e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b421e8.md) _ZN8firebase9analytics9TerminateEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md) · 呼出先 7件 [`00c5ada0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ada0.md) [`00c5add0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5add0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9e0.md) · 呼出先 7件 [`00c5bd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd70.md) [`00c5bda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bda0.md) [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) [`00c5bfa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfa0.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 8件

アドレスに依存する影響 `branch_value` 4件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b42224",
      "incomplete_value": true,
      "site": "00b42224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b41230",
      "incomplete_value": true,
      "site": "00b41230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b42248",
      "incomplete_value": true,
      "site": "00b42248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b41254",
      "incomplete_value": true,
      "site": "00b41254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "definition_site": "00b4226c",
      "incomplete_value": true,
      "site": "00b4226c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b41278",
      "incomplete_value": true,
      "site": "00b41278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "00b421fc",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4220c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b42214",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b421fc",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4220c",
      "READ",
      [
        "storage",
        "00c9c748",
        null,
        "pointer"
      ]
    ],
    [
      "00b42214",
      "READ",
      [
        "storage",
        "00ca56d0",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b41230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b41230) · [`00b41248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b41248) · [`00b41254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b41254)
- 新版 [`00b42224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b421e8.md#insn-00b42224) · [`00b4223c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b421e8.md#insn-00b4223c) · [`00b42248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b421e8.md#insn-00b42248)

~~~diff
- 00b41230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b41230 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b41230 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b42224 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00b42224 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b42224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b41230 bytes 9f8202f9
+ 00b42224 bytes 9f6202f9
- 00b41248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41248 ["INT_ADD", "register:40f0:8", ["const:b41248:8", "const:4:8"]]
- 00b41248 ["CALLIND", null, ["register:0:8"]]
+ 00b4223c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4223c ["INT_ADD", "register:40f0:8", ["const:b4223c:8", "const:4:8"]]
+ 00b4223c ["CALLIND", null, ["register:0:8"]]
- 00b41248 bytes 00013fd6
+ 00b4223c bytes 00013fd6
- 00b41254 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
- 00b41254 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b41254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b42248 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4c8:8"]]
+ 00b42248 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b42248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b41254 bytes bf8602f9
+ 00b42248 bytes bf6602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb07eee6eae52448538584ec5b6ae60b"></a>

### [`00b4136c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md) → [`00b42360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42360.md) _ZN8firebase9analytics29SetAnalyticsCollectionEnabledEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42374",
      "incomplete_value": true,
      "site": "00b42374",
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
      "definition_site": "00b41380",
      "incomplete_value": true,
      "site": "00b41380",
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
      "definition_site": "00b4238c",
      "incomplete_value": true,
      "site": "00b4239c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b41398",
      "incomplete_value": true,
      "site": "00b413a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "definition_site": "00b42390",
      "incomplete_value": true,
      "site": "00b4239c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4139c",
      "incomplete_value": true,
      "site": "00b413a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:440:8"
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
      "00b42370",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4238c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42390",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42370",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4238c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42390",
      "READ",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b413a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b413a8) · [`00b41378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b41378) · [`00b4137c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b4137c)
- 新版 [`00b4239c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42360.md#insn-00b4239c) · [`00b4236c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42360.md#insn-00b4236c) · [`00b42370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42360.md#insn-00b42370)

~~~diff
- 00b413a8 ["INT_ADD", "register:40f0:8", ["const:b413a8:8", "const:4:8"]]
- 00b413a8 ["CALL", null, ["callee:0057504c:8"]]
+ 00b4239c ["INT_ADD", "register:40f0:8", ["const:b4239c:8", "const:4:8"]]
+ 00b4239c ["CALL", null, ["callee:0057504c:8"]]
- 00b413a8 bytes 61cee897
+ 00b4239c bytes 2ccbe897
- 00b41378 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4236c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b41378 bytes 282f0090
+ 00b4236c bytes 282f0090
- 00b4137c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 00b4137c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42370 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 00b42370 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4137c bytes 088142f9
+ 00b42370 bytes 086142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc48f3c488d93fa5359ce4ab78fe94f"></a>

### [`00b413d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md) → [`00b423c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b423c4.md) _ZN8firebase9analytics10SetConsentERKNSt6__ndk13mapINS0_11ConsentTypeENS0_13ConsentStatusENS1_4lessIS3_EENS1_9allocatorINS1_4pairIKS3_S4_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5afb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afb0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5bf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b423e8",
      "incomplete_value": true,
      "site": "00b423e8",
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
      "definition_site": "00b413f4",
      "incomplete_value": true,
      "site": "00b413f4",
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
      "definition_site": "00b424a4",
      "incomplete_value": true,
      "site": "00b424b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b414b0",
      "incomplete_value": true,
      "site": "00b414c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4a0:8"
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
      "definition_site": "00b424a8",
      "incomplete_value": true,
      "site": "00b424b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b414b4",
      "incomplete_value": true,
      "site": "00b414c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "00b423e4",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42468",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00b42490",
      "DATA",
      [
        "storage",
        "0030b5d5",
        "switchD_00b414a4::switchdataD_0030b5d5",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b423e4",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42468",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ],
    [
      "00b42490",
      "DATA",
      [
        "storage",
        "0030b615",
        "switchD_00b42498::switchdataD_0030b615",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b414c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md#insn-00b414c0) · [`00b414d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md#insn-00b414d8) · [`00b414fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md#insn-00b414fc)
- 新版 [`00b424b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b423c4.md#insn-00b424b4) · [`00b424cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b423c4.md#insn-00b424cc) · [`00b424f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b423c4.md#insn-00b424f0)

~~~diff
- 00b414c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b414c0 ["INT_ADD", "register:40f0:8", ["const:b414c0:8", "const:4:8"]]
- 00b414c0 ["CALLIND", null, ["register:0:8"]]
+ 00b424b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b424b4 ["INT_ADD", "register:40f0:8", ["const:b424b4:8", "const:4:8"]]
+ 00b424b4 ["CALLIND", null, ["register:0:8"]]
- 00b414c0 bytes 00013fd6
+ 00b424b4 bytes 00013fd6
- 00b414d8 ["INT_ADD", "register:40f0:8", ["const:b414d8:8", "const:4:8"]]
- 00b414d8 ["CALL", null, ["callee:00c5bf80:8"]]
+ 00b424cc ["INT_ADD", "register:40f0:8", ["const:b424cc:8", "const:4:8"]]
+ 00b424cc ["CALL", null, ["callee:00c5bf80:8"]]
- 00b414d8 bytes b6660494
+ 00b424cc bytes ad660494
- 00b414fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b414fc ["INT_ADD", "register:40f0:8", ["const:b414fc:8", "const:4:8"]]
- 00b414fc ["CALLIND", null, ["register:0:8"]]
+ 00b424f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b424f0 ["INT_ADD", "register:40f0:8", ["const:b424f0:8", "const:4:8"]]
+ 00b424f0 ["CALLIND", null, ["register:0:8"]]
- 00b414fc bytes 00013fd6
+ 00b424f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-505b372273748f756b5068c2f6ba1a77"></a>

### [`00b41fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md) → [`00b42fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42fe0.md) _ZN8firebase9analytics8LogEventEPKcS2_S2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42ffc",
      "incomplete_value": true,
      "site": "00b42ffc",
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
      "definition_site": "00b42008",
      "incomplete_value": true,
      "site": "00b42008",
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
      "definition_site": "00b430d8",
      "incomplete_value": true,
      "site": "00b430f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b420e4",
      "incomplete_value": true,
      "site": "00b420fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b430dc",
      "incomplete_value": true,
      "site": "00b430f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b420e8",
      "incomplete_value": true,
      "site": "00b420fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b42ff8",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b430d8",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b430dc",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42ff8",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b430d8",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b430dc",
      "READ",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b420fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b420fc) · [`00b42118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b42118) · [`00b42000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b42000)
- 新版 [`00b430f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42fe0.md#insn-00b430f0) · [`00b4310c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42fe0.md#insn-00b4310c) · [`00b42ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42fe0.md#insn-00b42ff4)

~~~diff
- 00b420fc ["INT_ADD", "register:40f0:8", ["const:b420fc:8", "const:4:8"]]
- 00b420fc ["CALL", null, ["callee:0057504c:8"]]
+ 00b430f0 ["INT_ADD", "register:40f0:8", ["const:b430f0:8", "const:4:8"]]
+ 00b430f0 ["CALL", null, ["callee:0057504c:8"]]
- 00b420fc bytes 0ccbe897
+ 00b430f0 bytes d7c7e897
- 00b42118 ["INT_ADD", "register:40f0:8", ["const:b42118:8", "const:4:8"]]
- 00b42118 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b4310c ["INT_ADD", "register:40f0:8", ["const:b4310c:8", "const:4:8"]]
+ 00b4310c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b42118 bytes 16630494
+ 00b4310c bytes 0d630494
- 00b42000 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b42ff4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42000 bytes 082f00f0
+ 00b42ff4 bytes 282f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c71c434652e70a8706a87f058d2a97b8"></a>

### [`00b42170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md) → [`00b43164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43164.md) _ZN8firebase9analytics8LogEventEPKcS2_d

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43180",
      "incomplete_value": true,
      "site": "00b43180",
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
      "definition_site": "00b4218c",
      "incomplete_value": true,
      "site": "00b4218c",
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
      "definition_site": "00b43230",
      "incomplete_value": true,
      "site": "00b43248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4223c",
      "incomplete_value": true,
      "site": "00b42254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43234",
      "incomplete_value": true,
      "site": "00b43248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42240",
      "incomplete_value": true,
      "site": "00b42254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
      "00b4317c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43230",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43234",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4317c",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43230",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43234",
      "READ",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md#insn-00b42254) · [`00b42270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md#insn-00b42270) · [`00b42184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md#insn-00b42184)
- 新版 [`00b43248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43164.md#insn-00b43248) · [`00b43264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43164.md#insn-00b43264) · [`00b43178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43164.md#insn-00b43178)

~~~diff
- 00b42254 ["INT_ADD", "register:40f0:8", ["const:b42254:8", "const:4:8"]]
- 00b42254 ["CALL", null, ["callee:0057504c:8"]]
+ 00b43248 ["INT_ADD", "register:40f0:8", ["const:b43248:8", "const:4:8"]]
+ 00b43248 ["CALL", null, ["callee:0057504c:8"]]
- 00b42254 bytes b6cae897
+ 00b43248 bytes 81c7e897
- 00b42270 ["INT_ADD", "register:40f0:8", ["const:b42270:8", "const:4:8"]]
- 00b42270 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b43264 ["INT_ADD", "register:40f0:8", ["const:b43264:8", "const:4:8"]]
+ 00b43264 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b42270 bytes c0620494
+ 00b43264 bytes b7620494
- 00b42184 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43178 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42184 bytes 082f00f0
+ 00b43178 bytes 082f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02422a088169223c489b091dbbafc7d"></a>

### [`00b422c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md) → [`00b432bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b432bc.md) _ZN8firebase9analytics8LogEventEPKcS2_l

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b130.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 1件 [`00c5c100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c100.md) · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b432d8",
      "incomplete_value": true,
      "site": "00b432d8",
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
      "definition_site": "00b422e4",
      "incomplete_value": true,
      "site": "00b422e4",
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
      "definition_site": "00b43388",
      "incomplete_value": true,
      "site": "00b433a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42394",
      "incomplete_value": true,
      "site": "00b423ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4338c",
      "incomplete_value": true,
      "site": "00b433a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42398",
      "incomplete_value": true,
      "site": "00b423ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
      "00b432d4",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43388",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4338c",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b432d4",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43388",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4338c",
      "READ",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b423ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b423ac) · [`00b423c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b423c8) · [`00b422dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b422dc)
- 新版 [`00b433a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b432bc.md#insn-00b433a0) · [`00b433bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b432bc.md#insn-00b433bc) · [`00b432d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b432bc.md#insn-00b432d0)

~~~diff
- 00b423ac ["INT_ADD", "register:40f0:8", ["const:b423ac:8", "const:4:8"]]
- 00b423ac ["CALL", null, ["callee:0057504c:8"]]
+ 00b433a0 ["INT_ADD", "register:40f0:8", ["const:b433a0:8", "const:4:8"]]
+ 00b433a0 ["CALL", null, ["callee:0057504c:8"]]
- 00b423ac bytes 60cae897
+ 00b433a0 bytes 2bc7e897
- 00b423c8 ["INT_ADD", "register:40f0:8", ["const:b423c8:8", "const:4:8"]]
- 00b423c8 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b433bc ["INT_ADD", "register:40f0:8", ["const:b433bc:8", "const:4:8"]]
+ 00b433bc ["CALL", null, ["callee:00c5bd40:8"]]
- 00b423c8 bytes 6a620494
+ 00b433bc bytes 61620494
- 00b422dc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b432d0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b422dc bytes 082f00f0
+ 00b432d0 bytes 082f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae15bc8c566306d52d0cf8536e1fb5b6"></a>

### [`00b42434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md) → [`00b43428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43428.md) _ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa60.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 1件 [`00c5ba30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba30.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43448",
      "incomplete_value": true,
      "site": "00b43448",
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
      "definition_site": "00b42454",
      "incomplete_value": true,
      "site": "00b42454",
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
      "definition_site": "00b43508",
      "incomplete_value": true,
      "site": "00b43520",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42514",
      "incomplete_value": true,
      "site": "00b4252c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4350c",
      "incomplete_value": true,
      "site": "00b43520",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42518",
      "incomplete_value": true,
      "site": "00b4252c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
      "00b43444",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b434dc",
      "PARAM",
      [
        "storage",
        "002be4ec",
        null,
        "string"
      ]
    ],
    [
      "00b43508",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b43444",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b434dc",
      "PARAM",
      [
        "storage",
        "002be5ca",
        null,
        "string"
      ]
    ],
    [
      "00b43508",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b4252c) · [`00b42548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b42548) · [`00b4244c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b4244c)
- 新版 [`00b43520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43428.md#insn-00b43520) · [`00b4353c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43428.md#insn-00b4353c) · [`00b43440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43428.md#insn-00b43440)

~~~diff
- 00b4252c ["INT_ADD", "register:40f0:8", ["const:b4252c:8", "const:4:8"]]
- 00b4252c ["CALL", null, ["callee:0057504c:8"]]
+ 00b43520 ["INT_ADD", "register:40f0:8", ["const:b43520:8", "const:4:8"]]
+ 00b43520 ["CALL", null, ["callee:0057504c:8"]]
- 00b4252c bytes 00cae897
+ 00b43520 bytes cbc6e897
- 00b42548 ["INT_ADD", "register:40f0:8", ["const:b42548:8", "const:4:8"]]
- 00b42548 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b4353c ["INT_ADD", "register:40f0:8", ["const:b4353c:8", "const:4:8"]]
+ 00b4353c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b42548 bytes 0a620494
+ 00b4353c bytes 01620494
- 00b4244c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43440 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4244c bytes 082f00f0
+ 00b43440 bytes 082f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b701be83ed8af657476cfcd0a8895e9d"></a>

### [`00b425a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md) → [`00b4359c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b4359c.md) _ZN8firebase9analytics19LogAppleTransactionEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4360c",
      "incomplete_value": false,
      "site": "00b43620",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42618",
      "incomplete_value": false,
      "site": "00b4262c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4360c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4360c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4262c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md#insn-00b4262c) · [`00b425cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md#insn-00b425cc) · [`00b425d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md#insn-00b425d4)
- 新版 [`00b43620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b4359c.md#insn-00b43620) · [`00b435c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b4359c.md#insn-00b435c0) · [`00b435c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b4359c.md#insn-00b435c8)

~~~diff
- 00b4262c ["INT_ADD", "register:40f0:8", ["const:b4262c:8", "const:4:8"]]
- 00b4262c ["CALL", null, ["callee:00c5be40:8"]]
+ 00b43620 ["INT_ADD", "register:40f0:8", ["const:b43620:8", "const:4:8"]]
+ 00b43620 ["CALL", null, ["callee:00c5be40:8"]]
- 00b4262c bytes 11620494
+ 00b43620 bytes 08620494
- 00b425cc ["INT_ADD", "register:40f0:8", ["const:b425cc:8", "const:4:8"]]
- 00b425cc ["CALL", null, ["callee:00c5bd50:8"]]
+ 00b435c0 ["INT_ADD", "register:40f0:8", ["const:b435c0:8", "const:4:8"]]
+ 00b435c0 ["CALL", null, ["callee:00c5bd50:8"]]
- 00b425cc bytes ed610494
+ 00b435c0 bytes e4610494
- 00b425d4 ["INT_ADD", "register:40f0:8", ["const:b425d4:8", "const:4:8"]]
- 00b425d4 ["CALL", null, ["callee:00c5bd50:8"]]
+ 00b435c8 ["INT_ADD", "register:40f0:8", ["const:b435c8:8", "const:4:8"]]
+ 00b435c8 ["CALL", null, ["callee:00c5bd50:8"]]
- 00b425d4 bytes eb610494
+ 00b435c8 bytes e2610494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb5b9c974c61ef6fc9f6a7b1c23cefd"></a>

### [`00b42860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md) → [`00b43854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43854.md) _ZN8firebase9analytics25SetDefaultEventParametersEPKNS0_9ParameterEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b110.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 1件 [`00c5c0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0e0.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.96% / 新版 91.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43874",
      "incomplete_value": true,
      "site": "00b43874",
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
      "definition_site": "00b42880",
      "incomplete_value": true,
      "site": "00b42880",
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
      "definition_site": "00b43950",
      "incomplete_value": true,
      "site": "00b43960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4295c",
      "incomplete_value": true,
      "site": "00b4296c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43954",
      "incomplete_value": true,
      "site": "00b43960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42960",
      "incomplete_value": true,
      "site": "00b4296c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:490:8"
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
      "00b43870",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43918",
      "PARAM",
      [
        "storage",
        "002b98bf",
        null,
        "string"
      ]
    ],
    [
      "00b4393c",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b43870",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43918",
      "PARAM",
      [
        "storage",
        "002b999d",
        null,
        "string"
      ]
    ],
    [
      "00b4393c",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b4296c) · [`00b429a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b429a4) · [`00b429dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b429dc)
- 新版 [`00b43960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43854.md#insn-00b43960) · [`00b43998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43854.md#insn-00b43998) · [`00b439d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43854.md#insn-00b439d0)

~~~diff
- 00b4296c ["INT_ADD", "register:40f0:8", ["const:b4296c:8", "const:4:8"]]
- 00b4296c ["CALL", null, ["callee:0057504c:8"]]
+ 00b43960 ["INT_ADD", "register:40f0:8", ["const:b43960:8", "const:4:8"]]
+ 00b43960 ["CALL", null, ["callee:0057504c:8"]]
- 00b4296c bytes f0c8e897
+ 00b43960 bytes bbc5e897
- 00b429a4 ["INT_ADD", "register:40f0:8", ["const:b429a4:8", "const:4:8"]]
- 00b429a4 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b43998 ["INT_ADD", "register:40f0:8", ["const:b43998:8", "const:4:8"]]
+ 00b43998 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b429a4 bytes f3600494
+ 00b43998 bytes ea600494
- 00b429dc ["INT_ADD", "register:40f0:8", ["const:b429dc:8", "const:4:8"]]
- 00b429dc ["CALL", null, ["callee:0057504c:8"]]
+ 00b439d0 ["INT_ADD", "register:40f0:8", ["const:b439d0:8", "const:4:8"]]
+ 00b439d0 ["CALL", null, ["callee:0057504c:8"]]
- 00b429dc bytes d4c8e897
+ 00b439d0 bytes 9fc5e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a9515f968add0738ca3f456ed179d53"></a>

### [`00b42aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md) → [`00b43a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43a98.md) _ZN8firebase9analytics15SetUserPropertyEPKcS2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43ab4",
      "incomplete_value": true,
      "site": "00b43ab4",
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
      "definition_site": "00b42ac0",
      "incomplete_value": true,
      "site": "00b42ac0",
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
      "definition_site": "00b43b28",
      "incomplete_value": true,
      "site": "00b43b3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42b34",
      "incomplete_value": true,
      "site": "00b42b48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "definition_site": "00b43b2c",
      "incomplete_value": true,
      "site": "00b43b3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42b38",
      "incomplete_value": true,
      "site": "00b42b48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
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
      "00b43ab0",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43b10",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00b43b28",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b43ab0",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43b10",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ],
    [
      "00b43b28",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md#insn-00b42b48) · [`00b42b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md#insn-00b42b68) · [`00b42ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md#insn-00b42ab8)
- 新版 [`00b43b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43a98.md#insn-00b43b3c) · [`00b43b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43a98.md#insn-00b43b5c) · [`00b43aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43a98.md#insn-00b43aac)

~~~diff
- 00b42b48 ["INT_ADD", "register:40f0:8", ["const:b42b48:8", "const:4:8"]]
- 00b42b48 ["CALL", null, ["callee:0057504c:8"]]
+ 00b43b3c ["INT_ADD", "register:40f0:8", ["const:b43b3c:8", "const:4:8"]]
+ 00b43b3c ["CALL", null, ["callee:0057504c:8"]]
- 00b42b48 bytes 79c8e897
+ 00b43b3c bytes 44c5e897
- 00b42b68 ["INT_ADD", "register:40f0:8", ["const:b42b68:8", "const:4:8"]]
- 00b42b68 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b43b5c ["INT_ADD", "register:40f0:8", ["const:b43b5c:8", "const:4:8"]]
+ 00b43b5c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b42b68 bytes 82600494
+ 00b43b5c bytes 79600494
- 00b42ab8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43aac ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42ab8 bytes 082f00f0
+ 00b43aac bytes 082f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6915bd8fa35d4f00235e32a1cf91748f"></a>

### [`00b42ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md) → [`00b43b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43b9c.md) _ZN8firebase9analytics9SetUserIdEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa50.md) · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba20.md) · 呼出先 5件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43bb4",
      "incomplete_value": true,
      "site": "00b43bb4",
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
      "definition_site": "00b42bc0",
      "incomplete_value": true,
      "site": "00b42bc0",
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
      "definition_site": "00b43c0c",
      "incomplete_value": true,
      "site": "00b43c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c18",
      "incomplete_value": true,
      "site": "00b42c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "definition_site": "00b43c10",
      "incomplete_value": true,
      "site": "00b43c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c1c",
      "incomplete_value": true,
      "site": "00b42c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b43bb0",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43bf4",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00b43c0c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b43bb0",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43bf4",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ],
    [
      "00b43c0c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42c28) · [`00b42c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42c44) · [`00b42bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42bb8)
- 新版 [`00b43c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43b9c.md#insn-00b43c1c) · [`00b43c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43b9c.md#insn-00b43c38) · [`00b43bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43b9c.md#insn-00b43bac)

~~~diff
- 00b42c28 ["INT_ADD", "register:40f0:8", ["const:b42c28:8", "const:4:8"]]
- 00b42c28 ["CALL", null, ["callee:0057504c:8"]]
+ 00b43c1c ["INT_ADD", "register:40f0:8", ["const:b43c1c:8", "const:4:8"]]
+ 00b43c1c ["CALL", null, ["callee:0057504c:8"]]
- 00b42c28 bytes 41c8e897
+ 00b43c1c bytes 0cc5e897
- 00b42c44 ["INT_ADD", "register:40f0:8", ["const:b42c44:8", "const:4:8"]]
- 00b42c44 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b43c38 ["INT_ADD", "register:40f0:8", ["const:b43c38:8", "const:4:8"]]
+ 00b43c38 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b42c44 bytes 4b600494
+ 00b43c38 bytes 42600494
- 00b42bb8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43bac ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42bb8 bytes 082f00f0
+ 00b43bac bytes 082f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-206c6cca4e85b2e00ea79cc4270ad5e8"></a>

### [`00b42c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md) → [`00b43c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43c70.md) _ZN8firebase9analytics25SetSessionTimeoutDurationEl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aa40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa40.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba10.md) · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43c84",
      "incomplete_value": true,
      "site": "00b43c84",
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
      "definition_site": "00b42c90",
      "incomplete_value": true,
      "site": "00b42c90",
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
      "definition_site": "00b43c9c",
      "incomplete_value": true,
      "site": "00b43cac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42ca8",
      "incomplete_value": true,
      "site": "00b42cb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "definition_site": "00b43ca0",
      "incomplete_value": true,
      "site": "00b43cac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:428:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42cac",
      "incomplete_value": true,
      "site": "00b42cb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:468:8"
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
      "00b43c80",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43c9c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43ca0",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b43c80",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43c9c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43ca0",
      "READ",
      [
        "storage",
        "01126428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42cb8) · [`00b42c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42c88) · [`00b42c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42c8c)
- 新版 [`00b43cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43c70.md#insn-00b43cac) · [`00b43c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43c70.md#insn-00b43c7c) · [`00b43c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43c70.md#insn-00b43c80)

~~~diff
- 00b42cb8 ["INT_ADD", "register:40f0:8", ["const:b42cb8:8", "const:4:8"]]
- 00b42cb8 ["CALL", null, ["callee:0057504c:8"]]
+ 00b43cac ["INT_ADD", "register:40f0:8", ["const:b43cac:8", "const:4:8"]]
+ 00b43cac ["CALL", null, ["callee:0057504c:8"]]
- 00b42cb8 bytes 1dc8e897
+ 00b43cac bytes e8c4e897
- 00b42c88 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43c7c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42c88 bytes 082f00f0
+ 00b43c7c bytes 082f00f0
- 00b42c8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 00b42c8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b43c80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 00b43c80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42c8c bytes 088142f9
+ 00b43c80 bytes 086142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68a22b669e14a9c5e7c9cba0c92cce3"></a>

### [`00b42ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md) → [`00b43cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43cd4.md) _ZN8firebase9analytics18ResetAnalyticsDataEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43ce8",
      "incomplete_value": true,
      "site": "00b43ce8",
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
      "definition_site": "00b42cf4",
      "incomplete_value": true,
      "site": "00b42cf4",
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
      "definition_site": "00b43cf8",
      "incomplete_value": true,
      "site": "00b43d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42d04",
      "incomplete_value": true,
      "site": "00b42d10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "definition_site": "00b43cfc",
      "incomplete_value": true,
      "site": "00b43d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42d08",
      "incomplete_value": true,
      "site": "00b42d10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "00b43ce4",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43cf8",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43cfc",
      "READ",
      [
        "storage",
        "01125470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b43ce4",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43cf8",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43cfc",
      "READ",
      [
        "storage",
        "01126430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42d10) · [`00b42cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42cec) · [`00b42cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42cf0)
- 新版 [`00b43d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43cd4.md#insn-00b43d04) · [`00b43ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43cd4.md#insn-00b43ce0) · [`00b43ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43cd4.md#insn-00b43ce4)

~~~diff
- 00b42d10 ["INT_ADD", "register:40f0:8", ["const:b42d10:8", "const:4:8"]]
- 00b42d10 ["CALL", null, ["callee:0057504c:8"]]
+ 00b43d04 ["INT_ADD", "register:40f0:8", ["const:b43d04:8", "const:4:8"]]
+ 00b43d04 ["CALL", null, ["callee:0057504c:8"]]
- 00b42d10 bytes 07c8e897
+ 00b43d04 bytes d2c4e897
- 00b42cec ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b43ce0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b42cec bytes 082f00f0
+ 00b43ce0 bytes 082f00f0
- 00b42cf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 00b42cf0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b43ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 00b43ce4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42cf0 bytes 008142f9
+ 00b43ce4 bytes 006142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f801d746f295b132e0276848f2b07cb4"></a>

### [`00b42d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md) → [`00b43d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43d40.md) _ZN8firebase9analytics22GetAnalyticsInstanceIdEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b43628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43628.md) [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00b4461c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b4461c.md) [`00b45048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45048.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43d70",
      "incomplete_value": true,
      "site": "00b43d70",
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
      "definition_site": "00b42d7c",
      "incomplete_value": true,
      "site": "00b42d7c",
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
      "definition_site": "00b43d98",
      "incomplete_value": true,
      "site": "00b43dac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42da4",
      "incomplete_value": true,
      "site": "00b42db8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43e70",
      "incomplete_value": false,
      "site": "00b43e74",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42e7c",
      "incomplete_value": false,
      "site": "00b42e80",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b43d6c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43d98",
      "READ",
      [
        "storage",
        "00c9b788",
        null,
        "pointer"
      ]
    ],
    [
      "00b43d98",
      "PARAM",
      [
        "storage",
        "00b44054",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b43d6c",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43d98",
      "READ",
      [
        "storage",
        "00c9c758",
        null,
        "pointer"
      ]
    ],
    [
      "00b43d98",
      "PARAM",
      [
        "storage",
        "00b45048",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42db8) · [`00b42e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42e80) · [`00b42eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42eb0)
- 新版 [`00b43dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43d40.md#insn-00b43dac) · [`00b43e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43d40.md#insn-00b43e74) · [`00b43ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43d40.md#insn-00b43ea4)

~~~diff
- 00b42db8 ["INT_ADD", "register:40f0:8", ["const:b42db8:8", "const:4:8"]]
- 00b42db8 ["CALL", null, ["callee:00c5bee0:8"]]
+ 00b43dac ["INT_ADD", "register:40f0:8", ["const:b43dac:8", "const:4:8"]]
+ 00b43dac ["CALL", null, ["callee:00c5bee0:8"]]
- 00b42db8 bytes 56600494
+ 00b43dac bytes 4d600494
- 00b42e80 ["INT_ADD", "register:40f0:8", ["const:b42e80:8", "const:4:8"]]
- 00b42e80 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b43e74 ["INT_ADD", "register:40f0:8", ["const:b43e74:8", "const:4:8"]]
+ 00b43e74 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b42e80 bytes 94600494
+ 00b43e74 bytes 8b600494
- 00b42eb0 ["INT_ADD", "register:40f0:8", ["const:b42eb0:8", "const:4:8"]]
- 00b42eb0 ["CALL", null, ["callee:00c5bfe0:8"]]
+ 00b43ea4 ["INT_ADD", "register:40f0:8", ["const:b43ea4:8", "const:4:8"]]
+ 00b43ea4 ["CALL", null, ["callee:00c5bfe0:8"]]
- 00b42eb0 bytes 58600494
+ 00b43ea4 bytes 4f600494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e35bc6825c519bebad2bf121e167df90"></a>

### [`00b42fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md) → [`00b43f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43f94.md) _ZN8firebase9analytics32GetAnalyticsInstanceIdLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b120.md) · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)
- 新版 呼出元 1件 [`00c5c0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0f0.md) · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43fb0",
      "incomplete_value": true,
      "site": "00b43fb0",
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
      "definition_site": "00b42fbc",
      "incomplete_value": true,
      "site": "00b42fbc",
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
      "definition_site": "00b44004",
      "incomplete_value": false,
      "site": "00b44008",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43010",
      "incomplete_value": false,
      "site": "00b43014",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b42fbc"
      ],
      [
        "FALL_THROUGH",
        "00b43fb0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b43fb0",
      "incomplete_value": true,
      "site": "00b43fe4",
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
      "definition_site": "00b42fbc",
      "incomplete_value": true,
      "site": "00b42ff0",
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
      "00b43fa8",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44004",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b43fa8",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44004",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md#insn-00b43014) · [`00b42fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md#insn-00b42fb0) · [`00b42fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md#insn-00b42fb4)
- 新版 [`00b44008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43f94.md#insn-00b44008) · [`00b43fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43f94.md#insn-00b43fa4) · [`00b43fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43f94.md#insn-00b43fa8)

~~~diff
- 00b43014 ["INT_ADD", "register:40f0:8", ["const:b43014:8", "const:4:8"]]
- 00b43014 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b44008 ["INT_ADD", "register:40f0:8", ["const:b44008:8", "const:4:8"]]
+ 00b44008 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b43014 bytes 2f600494
+ 00b44008 bytes 26600494
- 00b42fb0 ["COPY", "register:4048:8", ["const:1125000:8"]]
+ 00b43fa4 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b42fb0 bytes 092f00f0
+ 00b43fa4 bytes 092f00f0
- 00b42fb4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:500:8"]]
- 00b42fb4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b43fa8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c0:8"]]
+ 00b43fa8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42fb4 bytes 298142f9
+ 00b43fa8 bytes 296142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4ade730e4bfe0cd20b1e19c94c187f3"></a>

### [`00b43114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md) → [`00b44108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44108.md) _ZN8firebase9analytics12GetSessionIdEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b43b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md) [`00b4408c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4408c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00b44b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44b80.md) [`00b45080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45080.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44138",
      "incomplete_value": true,
      "site": "00b44138",
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
      "definition_site": "00b43144",
      "incomplete_value": true,
      "site": "00b43144",
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
      "definition_site": "00b44150",
      "incomplete_value": true,
      "site": "00b44164",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00b4315c",
      "incomplete_value": true,
      "site": "00b43170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:790:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4418c",
      "incomplete_value": true,
      "site": "00b44198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43198",
      "incomplete_value": true,
      "site": "00b431a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
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
      "00b44134",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44150",
      "READ",
      [
        "storage",
        "00c9b790",
        null,
        "pointer"
      ]
    ],
    [
      "00b44150",
      "PARAM",
      [
        "storage",
        "00b4408c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44134",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44150",
      "READ",
      [
        "storage",
        "00c9c760",
        null,
        "pointer"
      ]
    ],
    [
      "00b44150",
      "PARAM",
      [
        "storage",
        "00b45080",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md#insn-00b43170) · [`00b431a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md#insn-00b431a4) · [`00b431ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md#insn-00b431ec)
- 新版 [`00b44164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44108.md#insn-00b44164) · [`00b44198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44108.md#insn-00b44198) · [`00b441e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44108.md#insn-00b441e0)

~~~diff
- 00b43170 ["INT_ADD", "register:40f0:8", ["const:b43170:8", "const:4:8"]]
- 00b43170 ["CALL", null, ["callee:00c5bee0:8"]]
+ 00b44164 ["INT_ADD", "register:40f0:8", ["const:b44164:8", "const:4:8"]]
+ 00b44164 ["CALL", null, ["callee:00c5bee0:8"]]
- 00b43170 bytes 685f0494
+ 00b44164 bytes 5f5f0494
- 00b431a4 ["INT_ADD", "register:40f0:8", ["const:b431a4:8", "const:4:8"]]
- 00b431a4 ["CALL", null, ["callee:00497b94:8"]]
+ 00b44198 ["INT_ADD", "register:40f0:8", ["const:b44198:8", "const:4:8"]]
+ 00b44198 ["CALL", null, ["callee:00497b94:8"]]
- 00b431a4 bytes b451e597
+ 00b44198 bytes 7f4ee597
- 00b431ec ["INT_ADD", "register:40f0:8", ["const:b431ec:8", "const:4:8"]]
- 00b431ec ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b441e0 ["INT_ADD", "register:40f0:8", ["const:b441e0:8", "const:4:8"]]
+ 00b441e0 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b431ec bytes e15e0494
+ 00b441e0 bytes d85e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc8ee273d1de74139807e3890f163606"></a>

### [`00b433dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b433dc.md) → [`00b443d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b443d0.md) _ZN8firebase9analytics22GetSessionIdLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44440",
      "incomplete_value": false,
      "site": "00b44444",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4344c",
      "incomplete_value": false,
      "site": "00b43450",
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
            "const:8c8:8"
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
      "00b443e4",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44440",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b443e4",
      "READ",
      [
        "storage",
        "011264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44440",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b433dc.md#insn-00b43450) · [`00b433ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b433dc.md#insn-00b433ec) · [`00b433f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b433dc.md#insn-00b433f0)
- 新版 [`00b44444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b443d0.md#insn-00b44444) · [`00b443e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b443d0.md#insn-00b443e0) · [`00b443e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b443d0.md#insn-00b443e4)

~~~diff
- 00b43450 ["INT_ADD", "register:40f0:8", ["const:b43450:8", "const:4:8"]]
- 00b43450 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b44444 ["INT_ADD", "register:40f0:8", ["const:b44444:8", "const:4:8"]]
+ 00b44444 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b43450 bytes 205f0494
+ 00b44444 bytes 175f0494
- 00b433ec ["COPY", "register:4048:8", ["const:1125000:8"]]
+ 00b443e0 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b433ec bytes 092f00d0
+ 00b443e0 bytes 092f00d0
- 00b433f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:500:8"]]
- 00b433f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b443e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c0:8"]]
+ 00b443e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b433f0 bytes 298142f9
+ 00b443e4 bytes 296142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4641767625df055987251dad85fa8447"></a>

### [`00b4384c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4384c.md) → [`00b44840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44840.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae30.md) · 呼出先 11件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5be00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be00.md) · 呼出先 11件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b448ac",
      "incomplete_value": false,
      "site": "00b448b0",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b438b8",
      "incomplete_value": false,
      "site": "00b438bc",
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
            "const:88:8"
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
      "00b448ac",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b448ac",
      "PARAM",
      [
        "storage",
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b438bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4384c.md#insn-00b438bc) · [`00b43880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4384c.md#insn-00b43880) · [`00b4388c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4384c.md#insn-00b4388c)
- 新版 [`00b448b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44840.md#insn-00b448b0) · [`00b44874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44840.md#insn-00b44874) · [`00b44880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44840.md#insn-00b44880)

~~~diff
- 00b438bc ["INT_ADD", "register:40f0:8", ["const:b438bc:8", "const:4:8"]]
- 00b438bc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b448b0 ["INT_ADD", "register:40f0:8", ["const:b448b0:8", "const:4:8"]]
+ 00b448b0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b438bc bytes 055e0494
+ 00b448b0 bytes fc5d0494
- 00b43880 ["INT_ADD", "register:40f0:8", ["const:b43880:8", "const:4:8"]]
- 00b43880 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b44874 ["INT_ADD", "register:40f0:8", ["const:b44874:8", "const:4:8"]]
+ 00b44874 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b43880 bytes 945c0494
+ 00b44874 bytes 8b5c0494
- 00b4388c ["INT_ADD", "register:40f0:8", ["const:b4388c:8", "const:4:8"]]
- 00b4388c ["CALL", null, ["callee:00c5bf20:8"]]
+ 00b44880 ["INT_ADD", "register:40f0:8", ["const:b44880:8", "const:4:8"]]
+ 00b44880 ["CALL", null, ["callee:00c5bf20:8"]]
- 00b4388c bytes b15d0494
+ 00b44880 bytes a85d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4957dde40c4b1cb20083f8a925e187c"></a>

### [`00b43b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md) → [`00b44b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44b80.md) FUN_00b44b80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b43114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md) · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)
- 新版 呼出元 1件 [`00b44108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44108.md) · 呼出先 9件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5bd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44c08",
      "incomplete_value": false,
      "site": "00b44c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:782:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43c14",
      "incomplete_value": false,
      "site": "00b43c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "definition_site": "00b44c3c",
      "incomplete_value": false,
      "site": "00b44c50",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43c48",
      "incomplete_value": false,
      "site": "00b43c5c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44be8",
      "PARAM",
      [
        "storage",
        "002a1969",
        null,
        "string"
      ]
    ],
    [
      "00b44c08",
      "PARAM",
      [
        "storage",
        "002aa6b5",
        null,
        "string"
      ]
    ],
    [
      "00b44c3c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b44be8",
      "PARAM",
      [
        "storage",
        "002a19a9",
        null,
        "string"
      ]
    ],
    [
      "00b44c08",
      "PARAM",
      [
        "storage",
        "002aa782",
        null,
        "string"
      ]
    ],
    [
      "00b44c3c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md#insn-00b43c1c) · [`00b43c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md#insn-00b43c5c) · [`00b43bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md#insn-00b43bc8)
- 新版 [`00b44c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44b80.md#insn-00b44c10) · [`00b44c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44b80.md#insn-00b44c50) · [`00b44bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44b80.md#insn-00b44bbc)

~~~diff
- 00b43c1c ["INT_ADD", "register:40f0:8", ["const:b43c1c:8", "const:4:8"]]
- 00b43c1c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b44c10 ["INT_ADD", "register:40f0:8", ["const:b44c10:8", "const:4:8"]]
+ 00b44c10 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b43c1c bytes 555c0494
+ 00b44c10 bytes 4c5c0494
- 00b43c5c ["INT_ADD", "register:40f0:8", ["const:b43c5c:8", "const:4:8"]]
- 00b43c5c ["CALL", null, ["callee:00c5be30:8"]]
+ 00b44c50 ["INT_ADD", "register:40f0:8", ["const:b44c50:8", "const:4:8"]]
+ 00b44c50 ["CALL", null, ["callee:00c5be30:8"]]
- 00b43c5c bytes 815c0494
+ 00b44c50 bytes 785c0494
- 00b43bc8 ["INT_ADD", "register:40f0:8", ["const:b43bc8:8", "const:4:8"]]
- 00b43bc8 ["CALL", null, ["callee:00c5bd50:8"]]
+ 00b44bbc ["INT_ADD", "register:40f0:8", ["const:b44bbc:8", "const:4:8"]]
+ 00b44bbc ["CALL", null, ["callee:00c5bd50:8"]]
- 00b43bc8 bytes 6e5c0494
+ 00b44bbc bytes 655c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2961bb2c9a033e1a2716b14a086f0d"></a>

### [`00b43d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md) → [`00b44cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44cf8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae60.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5be30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be30.md) · 呼出先 10件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44d64",
      "incomplete_value": false,
      "site": "00b44d68",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43d70",
      "incomplete_value": false,
      "site": "00b43d74",
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
            "const:88:8"
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
      "00b44d64",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44d64",
      "PARAM",
      [
        "storage",
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d74) · [`00b43d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d38) · [`00b43d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d44)
- 新版 [`00b44d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44cf8.md#insn-00b44d68) · [`00b44d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44cf8.md#insn-00b44d2c) · [`00b44d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44cf8.md#insn-00b44d38)

~~~diff
- 00b43d74 ["INT_ADD", "register:40f0:8", ["const:b43d74:8", "const:4:8"]]
- 00b43d74 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b44d68 ["INT_ADD", "register:40f0:8", ["const:b44d68:8", "const:4:8"]]
+ 00b44d68 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b43d74 bytes d75c0494
+ 00b44d68 bytes ce5c0494
- 00b43d38 ["INT_ADD", "register:40f0:8", ["const:b43d38:8", "const:4:8"]]
- 00b43d38 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b44d2c ["INT_ADD", "register:40f0:8", ["const:b44d2c:8", "const:4:8"]]
+ 00b44d2c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b43d38 bytes 665b0494
+ 00b44d2c bytes 5d5b0494
- 00b43d44 ["INT_ADD", "register:40f0:8", ["const:b43d44:8", "const:4:8"]]
- 00b43d44 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00b44d38 ["INT_ADD", "register:40f0:8", ["const:b44d38:8", "const:4:8"]]
+ 00b44d38 ["CALL", null, ["callee:00c5bf20:8"]]
- 00b43d44 bytes 835c0494
+ 00b44d38 bytes 7a5c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e694a99ad61d52d27fa106ba2686ab7"></a>

### [`00b43f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md) → [`00b44f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44f40.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) · 呼出先 10件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44fa4",
      "incomplete_value": false,
      "site": "00b44fa8",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43fb0",
      "incomplete_value": false,
      "site": "00b43fb4",
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
            "const:88:8"
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
      "00b44fa4",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44fa4",
      "PARAM",
      [
        "storage",
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43fb4) · [`00b43f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43f78) · [`00b43f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43f84)
- 新版 [`00b44fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44f40.md#insn-00b44fa8) · [`00b44f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44f40.md#insn-00b44f6c) · [`00b44f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44f40.md#insn-00b44f78)

~~~diff
- 00b43fb4 ["INT_ADD", "register:40f0:8", ["const:b43fb4:8", "const:4:8"]]
- 00b43fb4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b44fa8 ["INT_ADD", "register:40f0:8", ["const:b44fa8:8", "const:4:8"]]
+ 00b44fa8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b43fb4 bytes 475c0494
+ 00b44fa8 bytes 3e5c0494
- 00b43f78 ["INT_ADD", "register:40f0:8", ["const:b43f78:8", "const:4:8"]]
- 00b43f78 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b44f6c ["INT_ADD", "register:40f0:8", ["const:b44f6c:8", "const:4:8"]]
+ 00b44f6c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b43f78 bytes d65a0494
+ 00b44f6c bytes cd5a0494
- 00b43f84 ["INT_ADD", "register:40f0:8", ["const:b43f84:8", "const:4:8"]]
- 00b43f84 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00b44f78 ["INT_ADD", "register:40f0:8", ["const:b44f78:8", "const:4:8"]]
+ 00b44f78 ["CALL", null, ["callee:00c5bf20:8"]]
- 00b43f84 bytes f35b0494
+ 00b44f78 bytes ea5b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4816f81d956d8222455e367aa3848341"></a>

### [`00b44098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44098.md) → [`00b4508c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4508c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae50.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5be20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be20.md) · 呼出先 10件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b450f8",
      "incomplete_value": false,
      "site": "00b450fc",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44104",
      "incomplete_value": false,
      "site": "00b44108",
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
            "const:88:8"
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
      "00b450f8",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b450f8",
      "PARAM",
      [
        "storage",
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44098.md#insn-00b44108) · [`00b440cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44098.md#insn-00b440cc) · [`00b440d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44098.md#insn-00b440d8)
- 新版 [`00b450fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4508c.md#insn-00b450fc) · [`00b450c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4508c.md#insn-00b450c0) · [`00b450cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4508c.md#insn-00b450cc)

~~~diff
- 00b44108 ["INT_ADD", "register:40f0:8", ["const:b44108:8", "const:4:8"]]
- 00b44108 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b450fc ["INT_ADD", "register:40f0:8", ["const:b450fc:8", "const:4:8"]]
+ 00b450fc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b44108 bytes f25b0494
+ 00b450fc bytes e95b0494
- 00b440cc ["INT_ADD", "register:40f0:8", ["const:b440cc:8", "const:4:8"]]
- 00b440cc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b450c0 ["INT_ADD", "register:40f0:8", ["const:b450c0:8", "const:4:8"]]
+ 00b450c0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b440cc bytes 815a0494
+ 00b450c0 bytes 785a0494
- 00b440d8 ["INT_ADD", "register:40f0:8", ["const:b440d8:8", "const:4:8"]]
- 00b440d8 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00b450cc ["INT_ADD", "register:40f0:8", ["const:b450cc:8", "const:4:8"]]
+ 00b450cc ["CALL", null, ["callee:00c5bf20:8"]]
- 00b440d8 bytes 9e5b0494
+ 00b450cc bytes 955b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3d0f51e9f6fb97f53157d850b23a115"></a>

### [`00b441ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md) → [`00b451e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451e0.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md) · 呼出先 8件 [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md) · 呼出先 8件 [`00b451b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451b0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 80.33% / 新版 80.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4521c",
      "incomplete_value": true,
      "site": "00b4521c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
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
      "definition_site": "00b44228",
      "incomplete_value": true,
      "site": "00b44228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4526c",
      "incomplete_value": false,
      "site": "00b45278",
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
            "const:4e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44278",
      "incomplete_value": false,
      "site": "00b44284",
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
            "const:521:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b4529c",
      "incomplete_value": true,
      "site": "00b4529c",
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
      "definition_site": "00b442a8",
      "incomplete_value": true,
      "site": "00b442a8",
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
      "00b45210",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b45218",
      "READ",
      [
        "storage",
        "01125518",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b45234",
      "WRITE",
      [
        "storage",
        "01125518",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45210",
      "READ",
      [
        "storage",
        "00c9c778",
        null,
        "pointer"
      ]
    ],
    [
      "00b45218",
      "READ",
      [
        "storage",
        "011264d8",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b45234",
      "WRITE",
      [
        "storage",
        "011264d8",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md#insn-00b44284) · [`00b442a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md#insn-00b442a8) · [`00b4420c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md#insn-00b4420c)
- 新版 [`00b45278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451e0.md#insn-00b45278) · [`00b4529c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451e0.md#insn-00b4529c) · [`00b45200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451e0.md#insn-00b45200)

~~~diff
- 00b44284 ["INT_ADD", "register:40f0:8", ["const:b44284:8", "const:4:8"]]
- 00b44284 ["CALL", null, ["callee:00c5c1f0:8"]]
+ 00b45278 ["INT_ADD", "register:40f0:8", ["const:b45278:8", "const:4:8"]]
+ 00b45278 ["CALL", null, ["callee:00c5c1f0:8"]]
- 00b44284 bytes e75b0494
+ 00b45278 bytes de5b0494
- 00b442a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b442a8 ["INT_ADD", "register:40f0:8", ["const:b442a8:8", "const:4:8"]]
- 00b442a8 ["CALLIND", null, ["register:0:8"]]
+ 00b4529c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4529c ["INT_ADD", "register:40f0:8", ["const:b4529c:8", "const:4:8"]]
+ 00b4529c ["CALLIND", null, ["register:0:8"]]
- 00b442a8 bytes 00013fd6
+ 00b4529c bytes 00013fd6
- 00b4420c ["COPY", "register:40c0:8", ["const:c9b000:8"]]
+ 00b45200 ["COPY", "register:40c0:8", ["const:c9c000:8"]]
- 00b4420c bytes b80a00f0
+ 00b45200 bytes b80a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bda6f32d2357f261735e2cf4c993adf"></a>

### [`00b442e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b442e0.md) → [`00b452d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b452d4.md) _ZN8firebase11GetLogLevelEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c170.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b452dc",
      "incomplete_value": true,
      "site": "00b452e0",
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
      "definition_site": "00b442e8",
      "incomplete_value": true,
      "site": "00b442ec",
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
      "00b452d8",
      "READ",
      [
        "storage",
        "00c9b7a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b452dc",
      "READ",
      [
        "storage",
        "00ca4710",
        "_ZN8firebase11g_log_levelE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b452d8",
      "READ",
      [
        "storage",
        "00c9c770",
        null,
        "pointer"
      ]
    ],
    [
      "00b452dc",
      "READ",
      [
        "storage",
        "00ca56e0",
        "_ZN8firebase11g_log_levelE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b442e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b442e0.md#insn-00b442e0) · [`00b442e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b442e0.md#insn-00b442e4)
- 新版 [`00b452d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b452d4.md#insn-00b452d4) · [`00b452d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b452d4.md#insn-00b452d8)

~~~diff
- 00b442e0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b452d4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b442e0 bytes a80a00f0
+ 00b452d4 bytes a80a00f0
- 00b442e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7a0:8"]]
- 00b442e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b452d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
+ 00b452d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b442e4 bytes 08d143f9
+ 00b452d8 bytes 08b943f9
~~~


<a id="compare-2acda43d7db160696be9276d2262add3"></a>

### [`00b44714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md) → [`00b45708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45708.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b451b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451b0.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45720",
      "incomplete_value": false,
      "site": "00b45724",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4472c",
      "incomplete_value": false,
      "site": "00b44730",
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
            "const:f1e:8"
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
      "definition_site": "00b45744",
      "incomplete_value": true,
      "site": "00b4574c",
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
      "definition_site": "00b44750",
      "incomplete_value": true,
      "site": "00b44758",
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
      "00b45720",
      "PARAM",
      [
        "storage",
        "002abf1e",
        null,
        "string"
      ]
    ],
    [
      "00b4572c",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b45730",
      "READ",
      [
        "storage",
        "01125510",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45720",
      "PARAM",
      [
        "storage",
        "002abfeb",
        null,
        "string"
      ]
    ],
    [
      "00b4572c",
      "READ",
      [
        "storage",
        "00c9c788",
        null,
        "pointer"
      ]
    ],
    [
      "00b45730",
      "READ",
      [
        "storage",
        "011264d0",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md#insn-00b44730) · [`00b4472c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md#insn-00b4472c) · [`00b44734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md#insn-00b44734)
- 新版 [`00b45724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45708.md#insn-00b45724) · [`00b45720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45708.md#insn-00b45720) · [`00b45728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45708.md#insn-00b45728)

~~~diff
- 00b44730 ["INT_ADD", "register:40f0:8", ["const:b44730:8", "const:4:8"]]
- 00b44730 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b45724 ["INT_ADD", "register:40f0:8", ["const:b45724:8", "const:4:8"]]
+ 00b45724 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b44730 bytes 685a0494
+ 00b45724 bytes 5f5a0494
- 00b4472c ["COPY", "tmp:0:8", ["const:f1e:8"]]
- 00b4472c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4472c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4472c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b45720 ["COPY", "tmp:0:8", ["const:feb:8"]]
+ 00b45720 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45720 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45720 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4472c bytes 00783c91
+ 00b45720 bytes 00ac3f91
- 00b44734 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b45728 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b44734 bytes a80a00f0
+ 00b45728 bytes a80a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc72f6ccb733fc16718ccf2656142baa"></a>

### [`00b44994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md) → [`00b45988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45988.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b459b4",
      "incomplete_value": true,
      "site": "00b459b4",
      "value": [
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
      "definition_site": "00b449c0",
      "incomplete_value": true,
      "site": "00b449c0",
      "value": [
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
      "definition_site": "00b4599c",
      "incomplete_value": true,
      "site": "00b4599c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b449a8",
      "incomplete_value": true,
      "site": "00b449a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b459a8",
      "incomplete_value": false,
      "site": "00b459ac",
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
            "const:aa1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b449b4",
      "incomplete_value": false,
      "site": "00b449b8",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45998",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b459a8",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b459b4",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45998",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b459a8",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b459b4",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b449b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md#insn-00b449b8) · [`00b449c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md#insn-00b449c0) · [`00b449a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md#insn-00b449a0)
- 新版 [`00b459ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45988.md#insn-00b459ac) · [`00b459b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45988.md#insn-00b459b4) · [`00b45994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45988.md#insn-00b45994)

~~~diff
- 00b449b8 ["INT_ADD", "register:40f0:8", ["const:b449b8:8", "const:4:8"]]
- 00b449b8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b459ac ["INT_ADD", "register:40f0:8", ["const:b459ac:8", "const:4:8"]]
+ 00b459ac ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b449b8 bytes 8a590494
+ 00b459ac bytes 81590494
- 00b449c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b449c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b459b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b459b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b449c0 bytes 609603f9
+ 00b459b4 bytes 607603f9
- 00b449a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45994 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b449a0 bytes 132f00b0
+ 00b45994 bytes 132f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14d614e7d9dc166d372ce7bc5ebfbcb0"></a>

### [`00b449d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md) → [`00b459c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b459c8.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) · 呼出先 4件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md) [`00c5b400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b400.md) [`00c5b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b640.md)
- 新版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) · 呼出先 4件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md) [`00c5c3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c3d0.md) [`00c5c610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b459e8",
      "incomplete_value": false,
      "site": "00b459fc",
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
            "const:d23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b449f4",
      "incomplete_value": false,
      "site": "00b44a08",
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
            "const:c54:8"
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
      "definition_site": "00b45a34",
      "incomplete_value": false,
      "site": "00b45a40",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44a40",
      "incomplete_value": false,
      "site": "00b44a4c",
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
            "const:5c6:8"
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
      "definition_site": "00b45acc",
      "incomplete_value": false,
      "site": "00b45ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30b000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44ad8",
      "incomplete_value": false,
      "site": "00b44ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30b000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00b459e8",
      "PARAM",
      [
        "storage",
        "002b6c54",
        null,
        "string"
      ]
    ],
    [
      "00b45a34",
      "PARAM",
      [
        "storage",
        "002b25c6",
        null,
        "string"
      ]
    ],
    [
      "00b45a78",
      "PARAM",
      [
        "storage",
        "002a9564",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b459e8",
      "PARAM",
      [
        "storage",
        "002b6d23",
        null,
        "string"
      ]
    ],
    [
      "00b45a34",
      "PARAM",
      [
        "storage",
        "002b2610",
        null,
        "string"
      ]
    ],
    [
      "00b45a78",
      "PARAM",
      [
        "storage",
        "002a9631",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44a08) · [`00b44a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44a4c) · [`00b44ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44ae4)
- 新版 [`00b459fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b459c8.md#insn-00b459fc) · [`00b45a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b459c8.md#insn-00b45a40) · [`00b45ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b459c8.md#insn-00b45ad8)

~~~diff
- 00b44a08 ["INT_ADD", "register:40f0:8", ["const:b44a08:8", "const:4:8"]]
- 00b44a08 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b459fc ["INT_ADD", "register:40f0:8", ["const:b459fc:8", "const:4:8"]]
+ 00b459fc ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b44a08 bytes fe590494
+ 00b459fc bytes f5590494
- 00b44a4c ["INT_ADD", "register:40f0:8", ["const:b44a4c:8", "const:4:8"]]
- 00b44a4c ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b45a40 ["INT_ADD", "register:40f0:8", ["const:b45a40:8", "const:4:8"]]
+ 00b45a40 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b44a4c bytes ed590494
+ 00b45a40 bytes e4590494
- 00b44ae4 ["INT_ADD", "register:40f0:8", ["const:b44ae4:8", "const:4:8"]]
- 00b44ae4 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b45ad8 ["INT_ADD", "register:40f0:8", ["const:b45ad8:8", "const:4:8"]]
+ 00b45ad8 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b44ae4 bytes a3580494
+ 00b45ad8 bytes 9a580494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0015e28134852c56cc124f408b3739a3"></a>

### [`00b44b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md) → [`00b45af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45af8.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b45b24",
      "incomplete_value": true,
      "site": "00b45b24",
      "value": [
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
      "definition_site": "00b44b30",
      "incomplete_value": true,
      "site": "00b44b30",
      "value": [
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
      "definition_site": "00b45b0c",
      "incomplete_value": true,
      "site": "00b45b0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b18",
      "incomplete_value": true,
      "site": "00b44b18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45b14",
      "incomplete_value": false,
      "site": "00b45b1c",
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
            "const:aa1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b20",
      "incomplete_value": false,
      "site": "00b44b28",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45b08",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b14",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b45b24",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45b08",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b14",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b45b24",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b28) · [`00b44b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b30) · [`00b44b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b10)
- 新版 [`00b45b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45af8.md#insn-00b45b1c) · [`00b45b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45af8.md#insn-00b45b24) · [`00b45b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45af8.md#insn-00b45b04)

~~~diff
- 00b44b28 ["INT_ADD", "register:40f0:8", ["const:b44b28:8", "const:4:8"]]
- 00b44b28 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b45b1c ["INT_ADD", "register:40f0:8", ["const:b45b1c:8", "const:4:8"]]
+ 00b45b1c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b44b28 bytes 2e590494
+ 00b45b1c bytes 25590494
- 00b44b30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b44b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45b24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b45b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44b30 bytes 609603f9
+ 00b45b24 bytes 607603f9
- 00b44b10 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45b04 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b44b10 bytes 132f00b0
+ 00b45b04 bytes 132f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b807c9dc37fad2ef54d3f5e68545b813"></a>

### [`00b44b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md) → [`00b45b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b38.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b45b68",
      "incomplete_value": true,
      "site": "00b45b68",
      "value": [
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
      "definition_site": "00b44b74",
      "incomplete_value": true,
      "site": "00b44b74",
      "value": [
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
      "definition_site": "00b45b4c",
      "incomplete_value": true,
      "site": "00b45b4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b58",
      "incomplete_value": true,
      "site": "00b44b58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b44b58"
      ],
      [
        "FALL_THROUGH",
        "00b45b4c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b45b4c",
      "incomplete_value": true,
      "site": "00b45b68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b58",
      "incomplete_value": true,
      "site": "00b44b74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b45b48",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b58",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b45b68",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45b48",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b58",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b45b68",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md#insn-00b44b74) · [`00b44b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md#insn-00b44b50) · [`00b44b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md#insn-00b44b54)
- 新版 [`00b45b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b38.md#insn-00b45b68) · [`00b45b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b38.md#insn-00b45b44) · [`00b45b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b38.md#insn-00b45b48)

~~~diff
- 00b44b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b44b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45b68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b45b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44b74 bytes 609603f9
+ 00b45b68 bytes 607603f9
- 00b44b50 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45b44 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b44b50 bytes 132f00b0
+ 00b45b44 bytes 132f00b0
- 00b44b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b44b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45b48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b45b48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44b54 bytes 689643f9
+ 00b45b48 bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48c2012bbec61aaeecef2e37fb5859f4"></a>

### [`00b44b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md) → [`00b45b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b7c.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b45bac",
      "incomplete_value": true,
      "site": "00b45bac",
      "value": [
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
      "definition_site": "00b44bb8",
      "incomplete_value": true,
      "site": "00b44bb8",
      "value": [
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
      "definition_site": "00b45b90",
      "incomplete_value": true,
      "site": "00b45b90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b9c",
      "incomplete_value": true,
      "site": "00b44b9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b44b9c"
      ],
      [
        "FALL_THROUGH",
        "00b45b90"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b45b90",
      "incomplete_value": true,
      "site": "00b45bac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44b9c",
      "incomplete_value": true,
      "site": "00b44bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b45b8c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b98",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b45bac",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45b8c",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45b98",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b45bac",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md#insn-00b44bb8) · [`00b44b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md#insn-00b44b94) · [`00b44b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md#insn-00b44b98)
- 新版 [`00b45bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b7c.md#insn-00b45bac) · [`00b45b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b7c.md#insn-00b45b88) · [`00b45b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45b7c.md#insn-00b45b8c)

~~~diff
- 00b44bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b44bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b45bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44bb8 bytes 609603f9
+ 00b45bac bytes 607603f9
- 00b44b94 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45b88 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b44b94 bytes 132f00b0
+ 00b45b88 bytes 132f00b0
- 00b44b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b44b98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45b8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b45b8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44b98 bytes 689643f9
+ 00b45b8c bytes 687643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e37295023e701843ed1fb27d5c722f8d"></a>

### [`00b44bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44bd8.md) → [`00b45bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45bcc.md) _ZN8firebase4util12class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b45c54",
      "incomplete_value": true,
      "site": "00b45c54",
      "value": [
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
      "definition_site": "00b44c60",
      "incomplete_value": true,
      "site": "00b44c60",
      "value": [
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
      "definition_site": "00b45c00",
      "incomplete_value": true,
      "site": "00b45c0c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:6e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44c0c",
      "incomplete_value": true,
      "site": "00b44c18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
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
      "00b45be0",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45c00",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45c54",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45be0",
      "READ",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45c00",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45c54",
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44bd8.md#insn-00b44c18) · [`00b44c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44bd8.md#insn-00b44c60) · [`00b44be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44bd8.md#insn-00b44be8)
- 新版 [`00b45c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45bcc.md#insn-00b45c0c) · [`00b45c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45bcc.md#insn-00b45c54) · [`00b45bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45bcc.md#insn-00b45bdc)

~~~diff
- 00b44c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44c18 ["INT_ADD", "register:40f0:8", ["const:b44c18:8", "const:4:8"]]
- 00b44c18 ["CALLIND", null, ["register:0:8"]]
+ 00b45c0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45c0c ["INT_ADD", "register:40f0:8", ["const:b45c0c:8", "const:4:8"]]
+ 00b45c0c ["CALLIND", null, ["register:0:8"]]
- 00b44c18 bytes 00013fd6
+ 00b45c0c bytes 00013fd6
- 00b44c60 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b44c60 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:730:8"]]
- 00b44c60 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b45c54 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b45c54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b45c54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b44c60 bytes a0c21c39
+ 00b45c54 bytes a0c21b39
- 00b44be8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b45bdc ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b44be8 bytes 152f00b0
+ 00b45bdc bytes 152f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9586b4642145f3aff17d38fd797593b"></a>

### [`00b44cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md) → [`00b45cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45cc4.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b45d00",
      "incomplete_value": true,
      "site": "00b45d00",
      "value": [
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
      "definition_site": "00b44d0c",
      "incomplete_value": true,
      "site": "00b44d0c",
      "value": [
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45d50",
      "incomplete_value": true,
      "site": "00b45d50",
      "value": [
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
      "definition_site": "00b44d5c",
      "incomplete_value": true,
      "site": "00b44d5c",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45cdc",
      "incomplete_value": true,
      "site": "00b45cdc",
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
      "definition_site": "00b44ce8",
      "incomplete_value": true,
      "site": "00b44ce8",
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
      "00b45cd8",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45ce4",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45d00",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45cd8",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45ce4",
      "READ",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45d00",
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md#insn-00b44d0c) · [`00b44d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md#insn-00b44d58) · [`00b44d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md#insn-00b44d5c)
- 新版 [`00b45d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45cc4.md#insn-00b45d00) · [`00b45d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45cc4.md#insn-00b45d4c) · [`00b45d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45cc4.md#insn-00b45d50)

~~~diff
- 00b44d0c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b44d0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b44d0c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:730:8"]]
- 00b44d0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b45d00 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b45d00 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b45d00 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b45d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b44d0c bytes bfc21c39
+ 00b45d00 bytes bfc21b39
- 00b44d58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44d58 ["INT_ADD", "register:40f0:8", ["const:b44d58:8", "const:4:8"]]
- 00b44d58 ["CALLIND", null, ["register:0:8"]]
+ 00b45d4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45d4c ["INT_ADD", "register:40f0:8", ["const:b45d4c:8", "const:4:8"]]
+ 00b45d4c ["CALLIND", null, ["register:0:8"]]
- 00b44d58 bytes 00013fd6
+ 00b45d4c bytes 00013fd6
- 00b44d5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b44d5c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b44d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b45d50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b45d50 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b45d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b44d5c bytes 9f9603f9
+ 00b45d50 bytes 9f7603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615badd210d4caed670f403215c0037b"></a>

### [`00b44d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md) → [`00b45d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45d64.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b45da4",
      "incomplete_value": true,
      "site": "00b45da4",
      "value": [
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
      "definition_site": "00b44db0",
      "incomplete_value": true,
      "site": "00b44db0",
      "value": [
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
      "definition_site": "00b45d80",
      "incomplete_value": true,
      "site": "00b45d80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44d8c",
      "incomplete_value": true,
      "site": "00b44d8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45d88",
      "incomplete_value": false,
      "site": "00b45d9c",
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
            "const:aa1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44d94",
      "incomplete_value": false,
      "site": "00b44da8",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45d78",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45d88",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b45da4",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45d78",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45d88",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b45da4",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44da8) · [`00b44db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44db0) · [`00b44d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44d7c)
- 新版 [`00b45d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45d64.md#insn-00b45d9c) · [`00b45da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45d64.md#insn-00b45da4) · [`00b45d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45d64.md#insn-00b45d70)

~~~diff
- 00b44da8 ["INT_ADD", "register:40f0:8", ["const:b44da8:8", "const:4:8"]]
- 00b44da8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b45d9c ["INT_ADD", "register:40f0:8", ["const:b45d9c:8", "const:4:8"]]
+ 00b45d9c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b44da8 bytes 8e580494
+ 00b45d9c bytes 85580494
- 00b44db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b44db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b45da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44db0 bytes 809603f9
+ 00b45da4 bytes 807603f9
- 00b44d7c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b45d70 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b44d7c bytes 142f00b0
+ 00b45d70 bytes 142f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44505445fd0174811136987e2d0f62c2"></a>

### [`00b44de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md) → [`00b45dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45dd4.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) · 呼出先 5件 [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)
- 新版 呼出元 1件 [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md) · 呼出先 5件 [`00b52830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52830.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45e2c",
      "incomplete_value": false,
      "site": "00b45e34",
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
            "const:8be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44e38",
      "incomplete_value": false,
      "site": "00b44e40",
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
            "const:874:8"
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
      "definition_site": "00b45f70",
      "incomplete_value": false,
      "site": "00b45f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:dea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44f7c",
      "incomplete_value": false,
      "site": "00b44f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:d0c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45fa8",
      "incomplete_value": false,
      "site": "00b45fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:166:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44fb4",
      "incomplete_value": false,
      "site": "00b44fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:99:8"
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
      "00b45e2c",
      "PARAM",
      [
        "storage",
        "002c0874",
        null,
        "string"
      ]
    ],
    [
      "00b45f20",
      "PARAM",
      [
        "storage",
        "002b1553",
        null,
        "string"
      ]
    ],
    [
      "00b45f20",
      "PARAM",
      [
        "storage",
        "002bad03",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45e2c",
      "PARAM",
      [
        "storage",
        "002c08be",
        null,
        "string"
      ]
    ],
    [
      "00b45f20",
      "PARAM",
      [
        "storage",
        "002b162a",
        null,
        "string"
      ]
    ],
    [
      "00b45f20",
      "PARAM",
      [
        "storage",
        "002bade1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md#insn-00b44e40) · [`00b44f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md#insn-00b44f80) · [`00b44fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md#insn-00b44fb8)
- 新版 [`00b45e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45dd4.md#insn-00b45e34) · [`00b45f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45dd4.md#insn-00b45f74) · [`00b45fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45dd4.md#insn-00b45fac)

~~~diff
- 00b44e40 ["INT_ADD", "register:40f0:8", ["const:b44e40:8", "const:4:8"]]
- 00b44e40 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b45e34 ["INT_ADD", "register:40f0:8", ["const:b45e34:8", "const:4:8"]]
+ 00b45e34 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b44e40 bytes f0580494
+ 00b45e34 bytes e7580494
- 00b44f80 ["INT_ADD", "register:40f0:8", ["const:b44f80:8", "const:4:8"]]
- 00b44f80 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b45f74 ["INT_ADD", "register:40f0:8", ["const:b45f74:8", "const:4:8"]]
+ 00b45f74 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b44f80 bytes 7c570494
+ 00b45f74 bytes 73570494
- 00b44fb8 ["INT_ADD", "register:40f0:8", ["const:b44fb8:8", "const:4:8"]]
- 00b44fb8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b45fac ["INT_ADD", "register:40f0:8", ["const:b45fac:8", "const:4:8"]]
+ 00b45fac ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b44fb8 bytes 46580494
+ 00b45fac bytes 3d580494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-612f91eacbe1d1acbd1243059e013354"></a>

### [`00b4504c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4504c.md) → [`00b46040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46040.md) _ZN8firebase4util12class_loader11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4605c",
      "incomplete_value": false,
      "site": "00b46060",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45068",
      "incomplete_value": false,
      "site": "00b4506c",
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
            "const:30b:8"
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
      "definition_site": "00b4606c",
      "incomplete_value": true,
      "site": "00b46078",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b45078",
      "incomplete_value": true,
      "site": "00b45084",
      "value": [
        "LOAD",
        "8",
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
      "00b4605c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4606c",
      "DATA",
      [
        "storage",
        "01125738",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4605c",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4606c",
      "DATA",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4506c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4504c.md#insn-00b4506c) · [`00b45068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4504c.md#insn-00b45068) · [`00b45070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4504c.md#insn-00b45070)
- 新版 [`00b46060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46040.md#insn-00b46060) · [`00b4605c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46040.md#insn-00b4605c) · [`00b46064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46040.md#insn-00b46064)

~~~diff
- 00b4506c ["INT_ADD", "register:40f0:8", ["const:b4506c:8", "const:4:8"]]
- 00b4506c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46060 ["INT_ADD", "register:40f0:8", ["const:b46060:8", "const:4:8"]]
+ 00b46060 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4506c bytes 19580494
+ 00b46060 bytes 10580494
- 00b45068 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b45068 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45068 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45068 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4605c ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4605c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4605c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4605c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45068 bytes 002c0c91
+ 00b4605c bytes 008c1191
- 00b45070 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46064 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45070 bytes 082f0090
+ 00b46064 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adc06c6b5f93714af6858c2ec8f72d0a"></a>

### [`00b45088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md) → [`00b4607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4607c.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b460bc",
      "incomplete_value": true,
      "site": "00b460bc",
      "value": [
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
      "definition_site": "00b450c8",
      "incomplete_value": true,
      "site": "00b450c8",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b460a0",
      "incomplete_value": false,
      "site": "00b460b4",
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
            "const:aa1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b450ac",
      "incomplete_value": false,
      "site": "00b450c0",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46090",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b460a0",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b460bc",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46090",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b460a0",
      "PARAM",
      [
        "storage",
        "002b8aa1",
        null,
        "string"
      ]
    ],
    [
      "00b460bc",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b450c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md#insn-00b450c0) · [`00b450c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md#insn-00b450c8) · [`00b45094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md#insn-00b45094)
- 新版 [`00b460b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4607c.md#insn-00b460b4) · [`00b460bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4607c.md#insn-00b460bc) · [`00b46088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4607c.md#insn-00b46088)

~~~diff
- 00b450c0 ["INT_ADD", "register:40f0:8", ["const:b450c0:8", "const:4:8"]]
- 00b450c0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b460b4 ["INT_ADD", "register:40f0:8", ["const:b460b4:8", "const:4:8"]]
+ 00b460b4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b450c0 bytes c8570494
+ 00b460b4 bytes bf570494
- 00b450c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b450c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b460bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b460bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b450c8 bytes 809603f9
+ 00b460bc bytes 807603f9
- 00b45094 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46088 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b45094 bytes 142f0090
+ 00b46088 bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-635a9e4f463766bcc4d5e8892892faa0"></a>

### [`00b450f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md) → [`00b460ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b460ec.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) · 呼出先 5件 [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)
- 新版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) · 呼出先 5件 [`00b52830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52830.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.39% / 新版 88.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46144",
      "incomplete_value": false,
      "site": "00b4614c",
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
            "const:d07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45150",
      "incomplete_value": false,
      "site": "00b45158",
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
            "const:c38:8"
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
      "definition_site": "00b46288",
      "incomplete_value": false,
      "site": "00b4628c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:7c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45294",
      "incomplete_value": false,
      "site": "00b45298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:6f4:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46294",
      "incomplete_value": false,
      "site": "00b462a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30b000:8"
          ],
          [
            "leaf",
            "const:ac5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b452a0",
      "incomplete_value": false,
      "site": "00b452ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30b000:8"
          ],
          [
            "leaf",
            "const:a85:8"
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
      "00b4613c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b452e8"
      ]
    ],
    [
      "00b46144",
      "PARAM",
      [
        "storage",
        "002b6c38",
        null,
        "string"
      ]
    ],
    [
      "00b46238",
      "PARAM",
      [
        "storage",
        "002b1553",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4613c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b462dc"
      ]
    ],
    [
      "00b46144",
      "PARAM",
      [
        "storage",
        "002b6d07",
        null,
        "string"
      ]
    ],
    [
      "00b46238",
      "PARAM",
      [
        "storage",
        "002b162a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md#insn-00b45158) · [`00b45298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md#insn-00b45298) · [`00b452ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md#insn-00b452ac)
- 新版 [`00b4614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b460ec.md#insn-00b4614c) · [`00b4628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b460ec.md#insn-00b4628c) · [`00b462a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b460ec.md#insn-00b462a0)

~~~diff
- 00b45158 ["INT_ADD", "register:40f0:8", ["const:b45158:8", "const:4:8"]]
- 00b45158 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b4614c ["INT_ADD", "register:40f0:8", ["const:b4614c:8", "const:4:8"]]
+ 00b4614c ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b45158 bytes 2a580494
+ 00b4614c bytes 21580494
- 00b45298 ["INT_ADD", "register:40f0:8", ["const:b45298:8", "const:4:8"]]
- 00b45298 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b4628c ["INT_ADD", "register:40f0:8", ["const:b4628c:8", "const:4:8"]]
+ 00b4628c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b45298 bytes b6560494
+ 00b4628c bytes ad560494
- 00b452ac ["INT_ADD", "register:40f0:8", ["const:b452ac:8", "const:4:8"]]
- 00b452ac ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b462a0 ["INT_ADD", "register:40f0:8", ["const:b462a0:8", "const:4:8"]]
+ 00b462a0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b452ac bytes 89570494
+ 00b462a0 bytes 80570494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62af40c8265b5700dbf1734e646d1845"></a>

### [`00b45364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md) → [`00b46358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46358.md) _ZN8firebase4util12class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46374",
      "incomplete_value": false,
      "site": "00b46378",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45380",
      "incomplete_value": false,
      "site": "00b45384",
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
            "const:54d:8"
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
      "definition_site": "00b46384",
      "incomplete_value": true,
      "site": "00b46390",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b45390",
      "incomplete_value": true,
      "site": "00b4539c",
      "value": [
        "LOAD",
        "8",
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
      "00b46374",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b46384",
      "DATA",
      [
        "storage",
        "01125748",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46374",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b46384",
      "DATA",
      [
        "storage",
        "01126708",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b45384) · [`00b45380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b45380) · [`00b45388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b45388)
- 新版 [`00b46378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46358.md#insn-00b46378) · [`00b46374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46358.md#insn-00b46374) · [`00b4637c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46358.md#insn-00b4637c)

~~~diff
- 00b45384 ["INT_ADD", "register:40f0:8", ["const:b45384:8", "const:4:8"]]
- 00b45384 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46378 ["INT_ADD", "register:40f0:8", ["const:b46378:8", "const:4:8"]]
+ 00b46378 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45384 bytes 53570494
+ 00b46378 bytes 4a570494
- 00b45380 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b45380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46374 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b46374 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46374 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46374 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45380 bytes 00341591
+ 00b46374 bytes 00681891
- 00b45388 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4637c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45388 bytes 082f0090
+ 00b4637c bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c57b63f4dff042486839e8f942f3d7"></a>

### [`00b453a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md) → [`00b46394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46394.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b463c0",
      "incomplete_value": true,
      "site": "00b463c0",
      "value": [
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
      "definition_site": "00b453cc",
      "incomplete_value": true,
      "site": "00b453cc",
      "value": [
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
      "definition_site": "00b463a8",
      "incomplete_value": true,
      "site": "00b463a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453b4",
      "incomplete_value": true,
      "site": "00b453b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b463b4",
      "incomplete_value": false,
      "site": "00b463b8",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453c0",
      "incomplete_value": false,
      "site": "00b453c4",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b463a4",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463b4",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b463c0",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b463a4",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463b4",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b463c0",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b453c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453c4) · [`00b453cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453cc) · [`00b453ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453ac)
- 新版 [`00b463b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46394.md#insn-00b463b8) · [`00b463c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46394.md#insn-00b463c0) · [`00b463a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46394.md#insn-00b463a0)

~~~diff
- 00b453c4 ["INT_ADD", "register:40f0:8", ["const:b453c4:8", "const:4:8"]]
- 00b453c4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b463b8 ["INT_ADD", "register:40f0:8", ["const:b463b8:8", "const:4:8"]]
+ 00b463b8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b453c4 bytes 07570494
+ 00b463b8 bytes fe560494
- 00b453cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b453cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b463c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b463c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b453cc bytes 60aa03f9
+ 00b463c0 bytes 608a03f9
- 00b453ac ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b463a0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b453ac bytes 132f0090
+ 00b463a0 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eee83d5fe55a2b3e9c75f25ddecb250"></a>

### [`00b453e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md) → [`00b463d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b463d4.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46400",
      "incomplete_value": true,
      "site": "00b46400",
      "value": [
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
      "definition_site": "00b4540c",
      "incomplete_value": true,
      "site": "00b4540c",
      "value": [
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
      "definition_site": "00b463e8",
      "incomplete_value": true,
      "site": "00b463e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453f4",
      "incomplete_value": true,
      "site": "00b453f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b463f0",
      "incomplete_value": false,
      "site": "00b463f8",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453fc",
      "incomplete_value": false,
      "site": "00b45404",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b463e4",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463f0",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b46400",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b463e4",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463f0",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b46400",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b45404) · [`00b4540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b4540c) · [`00b453ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b453ec)
- 新版 [`00b463f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b463d4.md#insn-00b463f8) · [`00b46400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b463d4.md#insn-00b46400) · [`00b463e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b463d4.md#insn-00b463e0)

~~~diff
- 00b45404 ["INT_ADD", "register:40f0:8", ["const:b45404:8", "const:4:8"]]
- 00b45404 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b463f8 ["INT_ADD", "register:40f0:8", ["const:b463f8:8", "const:4:8"]]
+ 00b463f8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45404 bytes f7560494
+ 00b463f8 bytes ee560494
- 00b4540c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b4540c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b46400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4540c bytes 60aa03f9
+ 00b46400 bytes 608a03f9
- 00b453ec ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b463e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b453ec bytes 132f0090
+ 00b463e0 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fa79f94e511173524f55879aebf5002"></a>

### [`00b45420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md) → [`00b46414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46414.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46444",
      "incomplete_value": true,
      "site": "00b46444",
      "value": [
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
      "definition_site": "00b45450",
      "incomplete_value": true,
      "site": "00b45450",
      "value": [
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
      "definition_site": "00b46428",
      "incomplete_value": true,
      "site": "00b46428",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45434",
      "incomplete_value": true,
      "site": "00b45434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46434",
      "incomplete_value": false,
      "site": "00b4643c",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45440",
      "incomplete_value": false,
      "site": "00b45448",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46424",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46434",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b46444",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46424",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46434",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b46444",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b45448) · [`00b45450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b45450) · [`00b4542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b4542c)
- 新版 [`00b4643c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46414.md#insn-00b4643c) · [`00b46444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46414.md#insn-00b46444) · [`00b46420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46414.md#insn-00b46420)

~~~diff
- 00b45448 ["INT_ADD", "register:40f0:8", ["const:b45448:8", "const:4:8"]]
- 00b45448 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4643c ["INT_ADD", "register:40f0:8", ["const:b4643c:8", "const:4:8"]]
+ 00b4643c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45448 bytes e6560494
+ 00b4643c bytes dd560494
- 00b45450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b45450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46444 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b46444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45450 bytes 60aa03f9
+ 00b46444 bytes 608a03f9
- 00b4542c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46420 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4542c bytes 132f0090
+ 00b46420 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c2b39a4377ad6a2b740cd7748996dc"></a>

### [`00b45464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md) → [`00b46458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46458.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46488",
      "incomplete_value": true,
      "site": "00b46488",
      "value": [
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
      "definition_site": "00b45494",
      "incomplete_value": true,
      "site": "00b45494",
      "value": [
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
      "definition_site": "00b4646c",
      "incomplete_value": true,
      "site": "00b4646c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45478",
      "incomplete_value": true,
      "site": "00b45478",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46474",
      "incomplete_value": false,
      "site": "00b46480",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45480",
      "incomplete_value": false,
      "site": "00b4548c",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46468",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46474",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b46488",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46468",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46474",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b46488",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b4548c) · [`00b45494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b45494) · [`00b45470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b45470)
- 新版 [`00b46480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46458.md#insn-00b46480) · [`00b46488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46458.md#insn-00b46488) · [`00b46464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46458.md#insn-00b46464)

~~~diff
- 00b4548c ["INT_ADD", "register:40f0:8", ["const:b4548c:8", "const:4:8"]]
- 00b4548c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46480 ["INT_ADD", "register:40f0:8", ["const:b46480:8", "const:4:8"]]
+ 00b46480 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4548c bytes d5560494
+ 00b46480 bytes cc560494
- 00b45494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b45494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46488 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b46488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45494 bytes 60aa03f9
+ 00b46488 bytes 608a03f9
- 00b45470 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46464 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45470 bytes 132f0090
+ 00b46464 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95bc9c1bcb118b5cf3294e2ca571c710"></a>

### [`00b454b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md) → [`00b464a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b464a8.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b46530",
      "incomplete_value": true,
      "site": "00b46530",
      "value": [
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
      "definition_site": "00b4553c",
      "incomplete_value": true,
      "site": "00b4553c",
      "value": [
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
    "new": {
      "definition_site": "00b464dc",
      "incomplete_value": true,
      "site": "00b464e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b454e8",
      "incomplete_value": true,
      "site": "00b454f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:750:8"
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
      "00b464bc",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ],
    [
      "00b464dc",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46530",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b464bc",
      "READ",
      [
        "storage",
        "01126718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b464dc",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46530",
      "WRITE",
      [
        "storage",
        "01126718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b454f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md#insn-00b454f4) · [`00b4553c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md#insn-00b4553c) · [`00b454c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md#insn-00b454c4)
- 新版 [`00b464e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b464a8.md#insn-00b464e8) · [`00b46530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b464a8.md#insn-00b46530) · [`00b464b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b464a8.md#insn-00b464b8)

~~~diff
- 00b454f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b454f4 ["INT_ADD", "register:40f0:8", ["const:b454f4:8", "const:4:8"]]
- 00b454f4 ["CALLIND", null, ["register:0:8"]]
+ 00b464e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b464e8 ["INT_ADD", "register:40f0:8", ["const:b464e8:8", "const:4:8"]]
+ 00b464e8 ["CALLIND", null, ["register:0:8"]]
- 00b454f4 bytes 00013fd6
+ 00b464e8 bytes 00013fd6
- 00b4553c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4553c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:758:8"]]
- 00b4553c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b46530 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b46530 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:718:8"]]
+ 00b46530 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4553c bytes a0621d39
+ 00b46530 bytes a0621c39
- 00b454c4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b464b8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b454c4 bytes 152f0090
+ 00b464b8 bytes 152f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3fd57a91dcb610bdc3eea2e3e69e50"></a>

### [`00b45550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45550.md) → [`00b46544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46544.md) _ZN8firebase4util17jniresultcallback12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46580",
      "incomplete_value": true,
      "site": "00b46580",
      "value": [
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
      "definition_site": "00b4558c",
      "incomplete_value": true,
      "site": "00b4558c",
      "value": [
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
      "definition_site": "00b465d0",
      "incomplete_value": true,
      "site": "00b465d0",
      "value": [
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
    "old": {
      "definition_site": "00b455dc",
      "incomplete_value": true,
      "site": "00b455dc",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b465c0",
      "incomplete_value": true,
      "site": "00b465cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b455cc",
      "incomplete_value": true,
      "site": "00b455d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:750:8"
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
      "00b46558",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46564",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46580",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46558",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46564",
      "READ",
      [
        "storage",
        "01126718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46580",
      "WRITE",
      [
        "storage",
        "01126718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4558c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45550.md#insn-00b4558c) · [`00b455d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45550.md#insn-00b455d8) · [`00b455dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45550.md#insn-00b455dc)
- 新版 [`00b46580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46544.md#insn-00b46580) · [`00b465cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46544.md#insn-00b465cc) · [`00b465d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46544.md#insn-00b465d0)

~~~diff
- 00b4558c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4558c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4558c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:758:8"]]
- 00b4558c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46580 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46580 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46580 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:718:8"]]
+ 00b46580 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4558c bytes bf621d39
+ 00b46580 bytes bf621c39
- 00b455d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b455d8 ["INT_ADD", "register:40f0:8", ["const:b455d8:8", "const:4:8"]]
- 00b455d8 ["CALLIND", null, ["register:0:8"]]
+ 00b465cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b465cc ["INT_ADD", "register:40f0:8", ["const:b465cc:8", "const:4:8"]]
+ 00b465cc ["CALLIND", null, ["register:0:8"]]
- 00b455d8 bytes 00013fd6
+ 00b465cc bytes 00013fd6
- 00b455dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b455dc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b455dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b465d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
+ 00b465d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b465d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b455dc bytes 9faa03f9
+ 00b465d0 bytes 9f8a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17df39384cdbcde7e9baa4918bf85722"></a>

### [`00b455f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md) → [`00b465e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b465e4.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b46624",
      "incomplete_value": true,
      "site": "00b46624",
      "value": [
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
    "old": {
      "definition_site": "00b45630",
      "incomplete_value": true,
      "site": "00b45630",
      "value": [
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
      "definition_site": "00b46600",
      "incomplete_value": true,
      "site": "00b46600",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4560c",
      "incomplete_value": true,
      "site": "00b4560c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46608",
      "incomplete_value": false,
      "site": "00b4661c",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45614",
      "incomplete_value": false,
      "site": "00b45628",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b465f8",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46608",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b46624",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b465f8",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46608",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b46624",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b45628) · [`00b45630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b45630) · [`00b455fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b455fc)
- 新版 [`00b4661c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b465e4.md#insn-00b4661c) · [`00b46624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b465e4.md#insn-00b46624) · [`00b465f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b465e4.md#insn-00b465f0)

~~~diff
- 00b45628 ["INT_ADD", "register:40f0:8", ["const:b45628:8", "const:4:8"]]
- 00b45628 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4661c ["INT_ADD", "register:40f0:8", ["const:b4661c:8", "const:4:8"]]
+ 00b4661c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45628 bytes 6e560494
+ 00b4661c bytes 65560494
- 00b45630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b45630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
+ 00b46624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45630 bytes 80aa03f9
+ 00b46624 bytes 808a03f9
- 00b455fc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b465f0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b455fc bytes 142f0090
+ 00b465f0 bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdabdca2426f17f4324eaf46994e2e97"></a>

### [`00b45660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md) → [`00b46654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46654.md) _ZN8firebase4util17jniresultcallback11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46670",
      "incomplete_value": false,
      "site": "00b46674",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4567c",
      "incomplete_value": false,
      "site": "00b45680",
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
            "const:30b:8"
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
      "definition_site": "00b46680",
      "incomplete_value": true,
      "site": "00b4668c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4568c",
      "incomplete_value": true,
      "site": "00b45698",
      "value": [
        "LOAD",
        "8",
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
      "00b46670",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b46680",
      "DATA",
      [
        "storage",
        "01125760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46670",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b46680",
      "DATA",
      [
        "storage",
        "01126720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b45680) · [`00b4567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b4567c) · [`00b45684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b45684)
- 新版 [`00b46674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46654.md#insn-00b46674) · [`00b46670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46654.md#insn-00b46670) · [`00b46678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46654.md#insn-00b46678)

~~~diff
- 00b45680 ["INT_ADD", "register:40f0:8", ["const:b45680:8", "const:4:8"]]
- 00b45680 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46674 ["INT_ADD", "register:40f0:8", ["const:b46674:8", "const:4:8"]]
+ 00b46674 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45680 bytes 94560494
+ 00b46674 bytes 8b560494
- 00b4567c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4567c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4567c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4567c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46670 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b46670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4567c bytes 002c0c91
+ 00b46670 bytes 008c1191
- 00b45684 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46678 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45684 bytes 082f0090
+ 00b46678 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd9f0fcb34442db767680a6503e39953"></a>

### [`00b4569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md) → [`00b46690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46690.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b466d0",
      "incomplete_value": true,
      "site": "00b466d0",
      "value": [
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
    "old": {
      "definition_site": "00b456dc",
      "incomplete_value": true,
      "site": "00b456dc",
      "value": [
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
      "definition_site": "00b466ac",
      "incomplete_value": true,
      "site": "00b466ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b456b8",
      "incomplete_value": true,
      "site": "00b456b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b466b4",
      "incomplete_value": false,
      "site": "00b466c8",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b456c0",
      "incomplete_value": false,
      "site": "00b456d4",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b466a4",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466b4",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b466d0",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b466a4",
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466b4",
      "PARAM",
      [
        "storage",
        "002b0578",
        null,
        "string"
      ]
    ],
    [
      "00b466d0",
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b456d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md#insn-00b456d4) · [`00b456dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md#insn-00b456dc) · [`00b456a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md#insn-00b456a8)
- 新版 [`00b466c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46690.md#insn-00b466c8) · [`00b466d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46690.md#insn-00b466d0) · [`00b4669c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46690.md#insn-00b4669c)

~~~diff
- 00b456d4 ["INT_ADD", "register:40f0:8", ["const:b456d4:8", "const:4:8"]]
- 00b456d4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b466c8 ["INT_ADD", "register:40f0:8", ["const:b466c8:8", "const:4:8"]]
+ 00b466c8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b456d4 bytes 43560494
+ 00b466c8 bytes 3a560494
- 00b456dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b456dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b466d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
+ 00b466d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b456dc bytes 80aa03f9
+ 00b466d0 bytes 808a03f9
- 00b456a8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4669c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b456a8 bytes 142f0090
+ 00b4669c bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e6abe5128b5c3f20d0ad9c3c953b07"></a>

### [`00b45748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45748.md) → [`00b4673c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4673c.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46768",
      "incomplete_value": true,
      "site": "00b46768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45774",
      "incomplete_value": true,
      "site": "00b45774",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4675c",
      "incomplete_value": false,
      "site": "00b46760",
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
            "const:615:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45768",
      "incomplete_value": false,
      "site": "00b4576c",
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
            "const:537:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4674c",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4675c",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b46768",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4674c",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4675c",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b46768",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4576c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45748.md#insn-00b4576c) · [`00b45774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45748.md#insn-00b45774) · [`00b45754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45748.md#insn-00b45754)
- 新版 [`00b46760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4673c.md#insn-00b46760) · [`00b46768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4673c.md#insn-00b46768) · [`00b46748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4673c.md#insn-00b46748)

~~~diff
- 00b4576c ["INT_ADD", "register:40f0:8", ["const:b4576c:8", "const:4:8"]]
- 00b4576c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46760 ["INT_ADD", "register:40f0:8", ["const:b46760:8", "const:4:8"]]
+ 00b46760 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4576c bytes 1d560494
+ 00b46760 bytes 14560494
- 00b45774 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b45774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46768 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00b46768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45774 bytes 60be03f9
+ 00b46768 bytes 609e03f9
- 00b45754 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46748 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45754 bytes 132f0090
+ 00b46748 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8891b0488e3642fdd87b951c7a5c4b22"></a>

### [`00b45788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md) → [`00b4677c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4677c.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b467a8",
      "incomplete_value": true,
      "site": "00b467a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b457b4",
      "incomplete_value": true,
      "site": "00b457b4",
      "value": [
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
      "definition_site": "00b46790",
      "incomplete_value": true,
      "site": "00b46790",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4579c",
      "incomplete_value": true,
      "site": "00b4579c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b4579c"
      ],
      [
        "FALL_THROUGH",
        "00b46790"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b46790",
      "incomplete_value": true,
      "site": "00b467a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4579c",
      "incomplete_value": true,
      "site": "00b457b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4678c",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46798",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b467a8",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4678c",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46798",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b467a8",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b457b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md#insn-00b457b4) · [`00b45794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md#insn-00b45794) · [`00b45798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md#insn-00b45798)
- 新版 [`00b467a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4677c.md#insn-00b467a8) · [`00b46788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4677c.md#insn-00b46788) · [`00b4678c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4677c.md#insn-00b4678c)

~~~diff
- 00b457b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b457b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b467a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00b467a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b457b4 bytes 60be03f9
+ 00b467a8 bytes 609e03f9
- 00b45794 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46788 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45794 bytes 132f0090
+ 00b46788 bytes 132f0090
- 00b45798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b45798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4678c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00b4678c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45798 bytes 68be43f9
+ 00b4678c bytes 689e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef7fde6b4ef6921f6c274fd99f03d01"></a>

### [`00b457c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b457c8.md) → [`00b467bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b467bc.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b467ec",
      "incomplete_value": true,
      "site": "00b467ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b457f8",
      "incomplete_value": true,
      "site": "00b457f8",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b467dc",
      "incomplete_value": false,
      "site": "00b467e4",
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
            "const:615:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b457e8",
      "incomplete_value": false,
      "site": "00b457f0",
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
            "const:537:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b467cc",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b467dc",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b467ec",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b467cc",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b467dc",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b467ec",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b457f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b457c8.md#insn-00b457f0) · [`00b457f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b457c8.md#insn-00b457f8) · [`00b457d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b457c8.md#insn-00b457d4)
- 新版 [`00b467e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b467bc.md#insn-00b467e4) · [`00b467ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b467bc.md#insn-00b467ec) · [`00b467c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b467bc.md#insn-00b467c8)

~~~diff
- 00b457f0 ["INT_ADD", "register:40f0:8", ["const:b457f0:8", "const:4:8"]]
- 00b457f0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b467e4 ["INT_ADD", "register:40f0:8", ["const:b467e4:8", "const:4:8"]]
+ 00b467e4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b457f0 bytes fc550494
+ 00b467e4 bytes f3550494
- 00b457f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b457f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b467ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00b467ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b457f8 bytes 60be03f9
+ 00b467ec bytes 609e03f9
- 00b457d4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b467c8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b457d4 bytes 132f0090
+ 00b467c8 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e15a188b7eef27383a74764411cc91f"></a>

### [`00b4580c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md) → [`00b46800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46800.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46830",
      "incomplete_value": true,
      "site": "00b46830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4583c",
      "incomplete_value": true,
      "site": "00b4583c",
      "value": [
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
      "definition_site": "00b46814",
      "incomplete_value": true,
      "site": "00b46814",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45820",
      "incomplete_value": true,
      "site": "00b45820",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4681c",
      "incomplete_value": false,
      "site": "00b46828",
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
            "const:615:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45828",
      "incomplete_value": false,
      "site": "00b45834",
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
            "const:537:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46810",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4681c",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b46830",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46810",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4681c",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b46830",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md#insn-00b45834) · [`00b4583c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md#insn-00b4583c) · [`00b45818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md#insn-00b45818)
- 新版 [`00b46828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46800.md#insn-00b46828) · [`00b46830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46800.md#insn-00b46830) · [`00b4680c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46800.md#insn-00b4680c)

~~~diff
- 00b45834 ["INT_ADD", "register:40f0:8", ["const:b45834:8", "const:4:8"]]
- 00b45834 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46828 ["INT_ADD", "register:40f0:8", ["const:b46828:8", "const:4:8"]]
+ 00b46828 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45834 bytes eb550494
+ 00b46828 bytes e2550494
- 00b4583c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b4583c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00b46830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4583c bytes 60be03f9
+ 00b46830 bytes 609e03f9
- 00b45818 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4680c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45818 bytes 132f0090
+ 00b4680c bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede1962ef59eb3bda26dc422e2267777"></a>

### [`00b4585c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4585c.md) → [`00b46850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46850.md) _ZN8firebase4util26cppthreaddispatchercontext15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b468d8",
      "incomplete_value": true,
      "site": "00b468d8",
      "value": [
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
      "definition_site": "00b458e4",
      "incomplete_value": true,
      "site": "00b458e4",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46864",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46884",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b468d8",
      "WRITE",
      [
        "storage",
        "01125780",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46864",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46884",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b468d8",
      "WRITE",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b458e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4585c.md#insn-00b458e4) · [`00b4586c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4585c.md#insn-00b4586c) · [`00b45870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4585c.md#insn-00b45870)
- 新版 [`00b468d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46850.md#insn-00b468d8) · [`00b46860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46850.md#insn-00b46860) · [`00b46864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46850.md#insn-00b46864)

~~~diff
- 00b458e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b458e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:780:8"]]
- 00b458e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b468d8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b468d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:740:8"]]
+ 00b468d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b458e4 bytes a0021e39
+ 00b468d8 bytes a0021d39
- 00b4586c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46860 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4586c bytes 152f0090
+ 00b46860 bytes 152f0090
- 00b45870 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:780:8"]]
- 00b45870 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b45870 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46864 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:740:8"]]
+ 00b46864 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46864 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b45870 bytes a8025e39
+ 00b46864 bytes a8025d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-065924b4460af6f71e4b30f63e64fdc5"></a>

### [`00b458f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b458f8.md) → [`00b468ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b468ec.md) _ZN8firebase4util26cppthreaddispatchercontext12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46928",
      "incomplete_value": true,
      "site": "00b46928",
      "value": [
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
      "definition_site": "00b45934",
      "incomplete_value": true,
      "site": "00b45934",
      "value": [
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
      "definition_site": "00b46978",
      "incomplete_value": true,
      "site": "00b46978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45984",
      "incomplete_value": true,
      "site": "00b45984",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46900",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4690c",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46928",
      "WRITE",
      [
        "storage",
        "01125780",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46900",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4690c",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46928",
      "WRITE",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b458f8.md#insn-00b45934) · [`00b45984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b458f8.md#insn-00b45984) · [`00b45908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b458f8.md#insn-00b45908)
- 新版 [`00b46928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b468ec.md#insn-00b46928) · [`00b46978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b468ec.md#insn-00b46978) · [`00b468fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b468ec.md#insn-00b468fc)

~~~diff
- 00b45934 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b45934 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b45934 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:780:8"]]
- 00b45934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46928 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46928 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46928 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:740:8"]]
+ 00b46928 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b45934 bytes bf021e39
+ 00b46928 bytes bf021d39
- 00b45984 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b45984 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b45984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b46978 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00b46978 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b46978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b45984 bytes 9fbe03f9
+ 00b46978 bytes 9f9e03f9
- 00b45908 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b468fc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b45908 bytes 142f0090
+ 00b468fc bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45fc7d83572f1139f77b6a58b47bd561"></a>

### [`00b45998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md) → [`00b4698c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4698c.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b469cc",
      "incomplete_value": true,
      "site": "00b469cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b459d8",
      "incomplete_value": true,
      "site": "00b459d8",
      "value": [
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
      "definition_site": "00b469a8",
      "incomplete_value": true,
      "site": "00b469a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b459b4",
      "incomplete_value": true,
      "site": "00b459b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b469b0",
      "incomplete_value": true,
      "site": "00b469c4",
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
            "const:615:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b459bc",
      "incomplete_value": true,
      "site": "00b459d0",
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
            "const:537:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b469a0",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b469b0",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b469cc",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b469a0",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b469b0",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b469cc",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b459d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md#insn-00b459d0) · [`00b459d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md#insn-00b459d8) · [`00b459a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md#insn-00b459a4)
- 新版 [`00b469c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4698c.md#insn-00b469c4) · [`00b469cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4698c.md#insn-00b469cc) · [`00b46998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b4698c.md#insn-00b46998)

~~~diff
- 00b459d0 ["INT_ADD", "register:40f0:8", ["const:b459d0:8", "const:4:8"]]
- 00b459d0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b469c4 ["INT_ADD", "register:40f0:8", ["const:b469c4:8", "const:4:8"]]
+ 00b469c4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b459d0 bytes 84550494
+ 00b469c4 bytes 7b550494
- 00b459d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b459d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b469cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00b469cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b459d8 bytes 80be03f9
+ 00b469cc bytes 809e03f9
- 00b459a4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46998 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b459a4 bytes 142f0090
+ 00b46998 bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3d5d5e65e4a503c7fa01eca901b446"></a>

### [`00b45a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a08.md) → [`00b469fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b469fc.md) _ZN8firebase4util26cppthreaddispatchercontext11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46a18",
      "incomplete_value": false,
      "site": "00b46a1c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45a24",
      "incomplete_value": false,
      "site": "00b45a28",
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
            "const:30b:8"
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
      "definition_site": "00b46a28",
      "incomplete_value": true,
      "site": "00b46a34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b45a34",
      "incomplete_value": true,
      "site": "00b45a40",
      "value": [
        "LOAD",
        "8",
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
      "00b46a18",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b46a28",
      "DATA",
      [
        "storage",
        "01125788",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46a18",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b46a28",
      "DATA",
      [
        "storage",
        "01126748",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a08.md#insn-00b45a28) · [`00b45a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a08.md#insn-00b45a24) · [`00b45a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a08.md#insn-00b45a2c)
- 新版 [`00b46a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b469fc.md#insn-00b46a1c) · [`00b46a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b469fc.md#insn-00b46a18) · [`00b46a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b469fc.md#insn-00b46a20)

~~~diff
- 00b45a28 ["INT_ADD", "register:40f0:8", ["const:b45a28:8", "const:4:8"]]
- 00b45a28 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46a1c ["INT_ADD", "register:40f0:8", ["const:b46a1c:8", "const:4:8"]]
+ 00b46a1c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45a28 bytes aa550494
+ 00b46a1c bytes a1550494
- 00b45a24 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b45a24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45a24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45a24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46a18 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b46a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45a24 bytes 002c0c91
+ 00b46a18 bytes 008c1191
- 00b45a2c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46a20 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45a2c bytes 082f0090
+ 00b46a20 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bbd6c8272bac45402384649c678dd24"></a>

### [`00b45a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a44.md) → [`00b46a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46a38.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46a78",
      "incomplete_value": true,
      "site": "00b46a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45a84",
      "incomplete_value": true,
      "site": "00b45a84",
      "value": [
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
      "definition_site": "00b46a54",
      "incomplete_value": true,
      "site": "00b46a54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45a60",
      "incomplete_value": true,
      "site": "00b45a60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b45a60"
      ],
      [
        "FALL_THROUGH",
        "00b46a54"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b46a54",
      "incomplete_value": true,
      "site": "00b46a78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45a60",
      "incomplete_value": true,
      "site": "00b45a84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b46a4c",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a5c",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b46a78",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46a4c",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a5c",
      "PARAM",
      [
        "storage",
        "002be615",
        null,
        "string"
      ]
    ],
    [
      "00b46a78",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a44.md#insn-00b45a84) · [`00b45a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a44.md#insn-00b45a50) · [`00b45a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a44.md#insn-00b45a58)
- 新版 [`00b46a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46a38.md#insn-00b46a78) · [`00b46a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46a38.md#insn-00b46a44) · [`00b46a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46a38.md#insn-00b46a4c)

~~~diff
- 00b45a84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b45a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46a78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00b46a78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45a84 bytes 80be03f9
+ 00b46a78 bytes 809e03f9
- 00b45a50 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46a44 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b45a50 bytes 142f0090
+ 00b46a44 bytes 142f0090
- 00b45a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b45a58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46a4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00b46a4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45a58 bytes 81be43f9
+ 00b46a4c bytes 819e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ded208621424df0192b7e00ee31dbc"></a>

### [`00b45ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ab4.md) → [`00b46aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46aa8.md) _ZN8firebase4util26cppthreaddispatchercontext10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46ac4",
      "incomplete_value": false,
      "site": "00b46ac8",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45ad0",
      "incomplete_value": false,
      "site": "00b45ad4",
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
            "const:54d:8"
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
      "00b46ac4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b46ad4",
      "DATA",
      [
        "storage",
        "011257a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46ac4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b46ad4",
      "DATA",
      [
        "storage",
        "01126768",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ab4.md#insn-00b45ad4) · [`00b45ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ab4.md#insn-00b45ad0) · [`00b45ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ab4.md#insn-00b45ad8)
- 新版 [`00b46ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46aa8.md#insn-00b46ac8) · [`00b46ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46aa8.md#insn-00b46ac4) · [`00b46acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46aa8.md#insn-00b46acc)

~~~diff
- 00b45ad4 ["INT_ADD", "register:40f0:8", ["const:b45ad4:8", "const:4:8"]]
- 00b45ad4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46ac8 ["INT_ADD", "register:40f0:8", ["const:b46ac8:8", "const:4:8"]]
+ 00b46ac8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45ad4 bytes 7f550494
+ 00b46ac8 bytes 76550494
- 00b45ad0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b45ad0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45ad0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45ad0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46ac4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b46ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45ad0 bytes 00341591
+ 00b46ac4 bytes 00681891
- 00b45ad8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46acc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45ad8 bytes 082f0090
+ 00b46acc bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e6133124a3f0566fd1d10681502469"></a>

### [`00b45af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45af0.md) → [`00b46ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ae4.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46b10",
      "incomplete_value": true,
      "site": "00b46b10",
      "value": [
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
    "old": {
      "definition_site": "00b45b1c",
      "incomplete_value": true,
      "site": "00b45b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46b04",
      "incomplete_value": false,
      "site": "00b46b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b10",
      "incomplete_value": false,
      "site": "00b45b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:d4f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46af4",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b04",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46b10",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46af4",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b04",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46b10",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45af0.md#insn-00b45b14) · [`00b45b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45af0.md#insn-00b45b1c) · [`00b45afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45af0.md#insn-00b45afc)
- 新版 [`00b46b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ae4.md#insn-00b46b08) · [`00b46b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ae4.md#insn-00b46b10) · [`00b46af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ae4.md#insn-00b46af0)

~~~diff
- 00b45b14 ["INT_ADD", "register:40f0:8", ["const:b45b14:8", "const:4:8"]]
- 00b45b14 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46b08 ["INT_ADD", "register:40f0:8", ["const:b46b08:8", "const:4:8"]]
+ 00b46b08 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45b14 bytes 33550494
+ 00b46b08 bytes 2a550494
- 00b45b1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b0:8"]]
- 00b45b1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46b10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
+ 00b46b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45b1c bytes 60da03f9
+ 00b46b10 bytes 60ba03f9
- 00b45afc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46af0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45afc bytes 132f0090
+ 00b46af0 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-056888a8bf6666c4b9fc525db82c73d2"></a>

### [`00b45b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b30.md) → [`00b46b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b24.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46b50",
      "incomplete_value": true,
      "site": "00b46b50",
      "value": [
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
    "old": {
      "definition_site": "00b45b5c",
      "incomplete_value": true,
      "site": "00b45b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46b38",
      "incomplete_value": true,
      "site": "00b46b38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b44",
      "incomplete_value": true,
      "site": "00b45b44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46b40",
      "incomplete_value": false,
      "site": "00b46b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b4c",
      "incomplete_value": false,
      "site": "00b45b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:d4f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46b34",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b40",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46b50",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46b34",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b40",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46b50",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b30.md#insn-00b45b54) · [`00b45b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b30.md#insn-00b45b5c) · [`00b45b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b30.md#insn-00b45b3c)
- 新版 [`00b46b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b24.md#insn-00b46b48) · [`00b46b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b24.md#insn-00b46b50) · [`00b46b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b24.md#insn-00b46b30)

~~~diff
- 00b45b54 ["INT_ADD", "register:40f0:8", ["const:b45b54:8", "const:4:8"]]
- 00b45b54 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46b48 ["INT_ADD", "register:40f0:8", ["const:b46b48:8", "const:4:8"]]
+ 00b46b48 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45b54 bytes 23550494
+ 00b46b48 bytes 1a550494
- 00b45b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b0:8"]]
- 00b45b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
+ 00b46b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45b5c bytes 60da03f9
+ 00b46b50 bytes 60ba03f9
- 00b45b3c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46b30 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45b3c bytes 132f0090
+ 00b46b30 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e2f1fb6a6d3b5e83d29ca3cc372b60"></a>

### [`00b45b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b70.md) → [`00b46b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b64.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46b94",
      "incomplete_value": true,
      "site": "00b46b94",
      "value": [
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
    "old": {
      "definition_site": "00b45ba0",
      "incomplete_value": true,
      "site": "00b45ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46b84",
      "incomplete_value": true,
      "site": "00b46b8c",
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
            "const:e2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45b90",
      "incomplete_value": true,
      "site": "00b45b98",
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
            "const:d4f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46b74",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b84",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46b94",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46b74",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b84",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46b94",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b70.md#insn-00b45b98) · [`00b45ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b70.md#insn-00b45ba0) · [`00b45b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45b70.md#insn-00b45b7c)
- 新版 [`00b46b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b64.md#insn-00b46b8c) · [`00b46b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b64.md#insn-00b46b94) · [`00b46b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46b64.md#insn-00b46b70)

~~~diff
- 00b45b98 ["INT_ADD", "register:40f0:8", ["const:b45b98:8", "const:4:8"]]
- 00b45b98 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46b8c ["INT_ADD", "register:40f0:8", ["const:b46b8c:8", "const:4:8"]]
+ 00b46b8c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45b98 bytes 12550494
+ 00b46b8c bytes 09550494
- 00b45ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b0:8"]]
- 00b45ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
+ 00b46b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45ba0 bytes 60da03f9
+ 00b46b94 bytes 60ba03f9
- 00b45b7c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46b70 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45b7c bytes 132f0090
+ 00b46b70 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0cca22472d2224ed654ecaad826b66f"></a>

### [`00b45bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45bb4.md) → [`00b46ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ba8.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46bd8",
      "incomplete_value": true,
      "site": "00b46bd8",
      "value": [
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
    "old": {
      "definition_site": "00b45be4",
      "incomplete_value": true,
      "site": "00b45be4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46bbc",
      "incomplete_value": true,
      "site": "00b46bbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45bc8",
      "incomplete_value": true,
      "site": "00b45bc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b45bc8"
      ],
      [
        "FALL_THROUGH",
        "00b46bbc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b46bbc",
      "incomplete_value": true,
      "site": "00b46bd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45bc8",
      "incomplete_value": true,
      "site": "00b45be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b46bb8",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46bc4",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46bd8",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46bb8",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46bc4",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46bd8",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45bb4.md#insn-00b45be4) · [`00b45bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45bb4.md#insn-00b45bc0) · [`00b45bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45bb4.md#insn-00b45bc4)
- 新版 [`00b46bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ba8.md#insn-00b46bd8) · [`00b46bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ba8.md#insn-00b46bb4) · [`00b46bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ba8.md#insn-00b46bb8)

~~~diff
- 00b45be4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b0:8"]]
- 00b45be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46bd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
+ 00b46bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45be4 bytes 60da03f9
+ 00b46bd8 bytes 60ba03f9
- 00b45bc0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46bb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45bc0 bytes 132f0090
+ 00b46bb4 bytes 132f0090
- 00b45bc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b0:8"]]
- 00b45bc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
+ 00b46bb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45bc4 bytes 68da43f9
+ 00b46bb8 bytes 68ba43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e6b7cc85062a702b5f97bc4343a932f"></a>

### [`00b45c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45c04.md) → [`00b46bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46bf8.md) _ZN8firebase4util19cppthreaddispatcher15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b46c80",
      "incomplete_value": true,
      "site": "00b46c80",
      "value": [
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
    "old": {
      "definition_site": "00b45c8c",
      "incomplete_value": true,
      "site": "00b45c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "00b46c0c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46c2c",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c80",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46c0c",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46c2c",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c80",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45c04.md#insn-00b45c8c) · [`00b45c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45c04.md#insn-00b45c14) · [`00b45c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45c04.md#insn-00b45c18)
- 新版 [`00b46c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46bf8.md#insn-00b46c80) · [`00b46c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46bf8.md#insn-00b46c08) · [`00b46c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46bf8.md#insn-00b46c0c)

~~~diff
- 00b45c8c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b45c8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7b8:8"]]
- 00b45c8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b46c80 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b46c80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:778:8"]]
+ 00b46c80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b45c8c bytes a0e21e39
+ 00b46c80 bytes a0e21d39
- 00b45c14 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46c08 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b45c14 bytes 152f0090
+ 00b46c08 bytes 152f0090
- 00b45c18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b8:8"]]
- 00b45c18 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b45c18 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46c0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00b46c0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46c0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b45c18 bytes a8e25e39
+ 00b46c0c bytes a8e25d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ee566caba8398c22d5e511e336d61e5"></a>

### [`00b45ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ca0.md) → [`00b46c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46c94.md) _ZN8firebase4util19cppthreaddispatcher12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46cd0",
      "incomplete_value": true,
      "site": "00b46cd0",
      "value": [
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
    "old": {
      "definition_site": "00b45cdc",
      "incomplete_value": true,
      "site": "00b45cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "definition_site": "00b46d20",
      "incomplete_value": true,
      "site": "00b46d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45d2c",
      "incomplete_value": true,
      "site": "00b45d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46cac",
      "incomplete_value": true,
      "site": "00b46cac",
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
      "definition_site": "00b45cb8",
      "incomplete_value": true,
      "site": "00b45cb8",
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
      "00b46ca8",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb4",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46cd0",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46ca8",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb4",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46cd0",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ca0.md#insn-00b45cdc) · [`00b45d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ca0.md#insn-00b45d28) · [`00b45d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ca0.md#insn-00b45d2c)
- 新版 [`00b46cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46c94.md#insn-00b46cd0) · [`00b46d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46c94.md#insn-00b46d1c) · [`00b46d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46c94.md#insn-00b46d20)

~~~diff
- 00b45cdc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b45cdc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b45cdc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7b8:8"]]
- 00b45cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46cd0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46cd0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46cd0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:778:8"]]
+ 00b46cd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b45cdc bytes bfe21e39
+ 00b46cd0 bytes bfe21d39
- 00b45d28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45d28 ["INT_ADD", "register:40f0:8", ["const:b45d28:8", "const:4:8"]]
- 00b45d28 ["CALLIND", null, ["register:0:8"]]
+ 00b46d1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46d1c ["INT_ADD", "register:40f0:8", ["const:b46d1c:8", "const:4:8"]]
+ 00b46d1c ["CALLIND", null, ["register:0:8"]]
- 00b45d28 bytes 00013fd6
+ 00b46d1c bytes 00013fd6
- 00b45d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b0:8"]]
- 00b45d2c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b45d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b46d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b46d20 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b46d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b45d2c bytes 9fda03f9
+ 00b46d20 bytes 9fba03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c61162df6cd26c27077267548dfeb8be"></a>

### [`00b45d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45d40.md) → [`00b46d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46d34.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46d74",
      "incomplete_value": true,
      "site": "00b46d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45d80",
      "incomplete_value": true,
      "site": "00b45d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "00b46d48",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d58",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46d74",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46d48",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d58",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46d74",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45d40.md#insn-00b45d80) · [`00b45d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45d40.md#insn-00b45d4c) · [`00b45d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45d40.md#insn-00b45d54)
- 新版 [`00b46d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46d34.md#insn-00b46d74) · [`00b46d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46d34.md#insn-00b46d40) · [`00b46d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46d34.md#insn-00b46d48)

~~~diff
- 00b45d80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b0:8"]]
- 00b45d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46d74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b46d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45d80 bytes 80da03f9
+ 00b46d74 bytes 80ba03f9
- 00b45d4c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46d40 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b45d4c bytes 142f0090
+ 00b46d40 bytes 142f0090
- 00b45d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b0:8"]]
- 00b45d54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46d48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b46d48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45d54 bytes 81da43f9
+ 00b46d48 bytes 81ba43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94dc56d981611bb7822d241ede667e06"></a>

### [`00b45db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45db0.md) → [`00b46da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46da4.md) _ZN8firebase4util19cppthreaddispatcher11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46dc0",
      "incomplete_value": true,
      "site": "00b46dc4",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45dcc",
      "incomplete_value": true,
      "site": "00b45dd0",
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
            "const:30b:8"
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
      "00b46dc0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b46dd0",
      "DATA",
      [
        "storage",
        "011257c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46dc0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b46dd0",
      "DATA",
      [
        "storage",
        "01126780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45db0.md#insn-00b45dd0) · [`00b45dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45db0.md#insn-00b45dcc) · [`00b45dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45db0.md#insn-00b45dd4)
- 新版 [`00b46dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46da4.md#insn-00b46dc4) · [`00b46dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46da4.md#insn-00b46dc0) · [`00b46dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46da4.md#insn-00b46dc8)

~~~diff
- 00b45dd0 ["INT_ADD", "register:40f0:8", ["const:b45dd0:8", "const:4:8"]]
- 00b45dd0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46dc4 ["INT_ADD", "register:40f0:8", ["const:b46dc4:8", "const:4:8"]]
+ 00b46dc4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45dd0 bytes c0540494
+ 00b46dc4 bytes b7540494
- 00b45dcc ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b45dcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45dcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45dcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46dc0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b46dc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46dc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46dc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45dcc bytes 002c0c91
+ 00b46dc0 bytes 008c1191
- 00b45dd4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46dc8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45dd4 bytes 082f0090
+ 00b46dc8 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0926cb56f61a516326aa383df7359f37"></a>

### [`00b45dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45dec.md) → [`00b46de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46de0.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46e20",
      "incomplete_value": true,
      "site": "00b46e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45e2c",
      "incomplete_value": true,
      "site": "00b45e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "00b46dfc",
      "incomplete_value": true,
      "site": "00b46dfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45e08",
      "incomplete_value": true,
      "site": "00b45e08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b45e08"
      ],
      [
        "FALL_THROUGH",
        "00b46dfc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b46dfc",
      "incomplete_value": true,
      "site": "00b46e20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45e08",
      "incomplete_value": true,
      "site": "00b45e2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b46df4",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e04",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ],
    [
      "00b46e20",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46df4",
      "READ",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e04",
      "PARAM",
      [
        "storage",
        "002bae2d",
        null,
        "string"
      ]
    ],
    [
      "00b46e20",
      "WRITE",
      [
        "storage",
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45dec.md#insn-00b45e2c) · [`00b45df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45dec.md#insn-00b45df8) · [`00b45e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45dec.md#insn-00b45e00)
- 新版 [`00b46e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46de0.md#insn-00b46e20) · [`00b46dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46de0.md#insn-00b46dec) · [`00b46df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46de0.md#insn-00b46df4)

~~~diff
- 00b45e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b0:8"]]
- 00b45e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46e20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b46e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45e2c bytes 80da03f9
+ 00b46e20 bytes 80ba03f9
- 00b45df8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46dec ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b45df8 bytes 142f0090
+ 00b46dec bytes 142f0090
- 00b45e00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b0:8"]]
- 00b45e00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46df4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b46df4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45e00 bytes 81da43f9
+ 00b46df4 bytes 81ba43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec6191817e7b8b161efcdca2e1cf76a7"></a>

### [`00b45e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e5c.md) → [`00b46e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e50.md) _ZN8firebase4util19cppthreaddispatcher10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b46e6c",
      "incomplete_value": false,
      "site": "00b46e70",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45e78",
      "incomplete_value": false,
      "site": "00b45e7c",
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
            "const:54d:8"
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
      "00b46e6c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b46e7c",
      "DATA",
      [
        "storage",
        "011257d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46e6c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b46e7c",
      "DATA",
      [
        "storage",
        "01126790",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e5c.md#insn-00b45e7c) · [`00b45e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e5c.md#insn-00b45e78) · [`00b45e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e5c.md#insn-00b45e80)
- 新版 [`00b46e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e50.md#insn-00b46e70) · [`00b46e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e50.md#insn-00b46e6c) · [`00b46e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e50.md#insn-00b46e74)

~~~diff
- 00b45e7c ["INT_ADD", "register:40f0:8", ["const:b45e7c:8", "const:4:8"]]
- 00b45e7c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b46e70 ["INT_ADD", "register:40f0:8", ["const:b46e70:8", "const:4:8"]]
+ 00b46e70 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b45e7c bytes 95540494
+ 00b46e70 bytes 8c540494
- 00b45e78 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b45e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b45e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b45e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46e6c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b46e6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46e6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46e6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b45e78 bytes 00341591
+ 00b46e6c bytes 00681891
- 00b45e80 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46e74 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b45e80 bytes 082f0090
+ 00b46e74 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-725035a7a44889c88ee108571d91c88b"></a>

### [`00b45e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e98.md) → [`00b46e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e8c.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46eb8",
      "incomplete_value": true,
      "site": "00b46eb8",
      "value": [
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
    "old": {
      "definition_site": "00b45ec4",
      "incomplete_value": true,
      "site": "00b45ec4",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46eac",
      "incomplete_value": true,
      "site": "00b46eb0",
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
            "const:e41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45eb8",
      "incomplete_value": true,
      "site": "00b45ebc",
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
            "const:d63:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46e9c",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46eac",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b46eb8",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46e9c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46eac",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b46eb8",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e98.md#insn-00b45ebc) · [`00b45ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e98.md#insn-00b45ec4) · [`00b45ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45e98.md#insn-00b45ea4)
- 新版 [`00b46eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e8c.md#insn-00b46eb0) · [`00b46eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e8c.md#insn-00b46eb8) · [`00b46e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46e8c.md#insn-00b46e98)

~~~diff
- 00b45ebc ["INT_ADD", "register:40f0:8", ["const:b45ebc:8", "const:4:8"]]
- 00b45ebc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46eb0 ["INT_ADD", "register:40f0:8", ["const:b46eb0:8", "const:4:8"]]
+ 00b46eb0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45ebc bytes 49540494
+ 00b46eb0 bytes 40540494
- 00b45ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45ec4 bytes 60ee03f9
+ 00b46eb8 bytes 60ce03f9
- 00b45ea4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46e98 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45ea4 bytes 132f0090
+ 00b46e98 bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b548539015c5c681dafbda41bc0c69"></a>

### [`00b45ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ed8.md) → [`00b46ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ecc.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46ef8",
      "incomplete_value": true,
      "site": "00b46ef8",
      "value": [
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
    "old": {
      "definition_site": "00b45f04",
      "incomplete_value": true,
      "site": "00b45f04",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46edc",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ee8",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b46ef8",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46edc",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ee8",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b46ef8",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ed8.md#insn-00b45f04) · [`00b45ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ed8.md#insn-00b45ee4) · [`00b45ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45ed8.md#insn-00b45ee8)
- 新版 [`00b46ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ecc.md#insn-00b46ef8) · [`00b46ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ecc.md#insn-00b46ed8) · [`00b46edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46ecc.md#insn-00b46edc)

~~~diff
- 00b45f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46ef8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46ef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45f04 bytes 60ee03f9
+ 00b46ef8 bytes 60ce03f9
- 00b45ee4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46ed8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45ee4 bytes 132f0090
+ 00b46ed8 bytes 132f0090
- 00b45ee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45ee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46edc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45ee8 bytes 68ee43f9
+ 00b46edc bytes 68ce43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4967490c722cb6d9e0cdef72eddf61"></a>

### [`00b45f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f18.md) → [`00b46f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f0c.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46f3c",
      "incomplete_value": true,
      "site": "00b46f3c",
      "value": [
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
    "old": {
      "definition_site": "00b45f48",
      "incomplete_value": true,
      "site": "00b45f48",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46f1c",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f2c",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b46f3c",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46f1c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f2c",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b46f3c",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f18.md#insn-00b45f48) · [`00b45f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f18.md#insn-00b45f24) · [`00b45f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f18.md#insn-00b45f28)
- 新版 [`00b46f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f0c.md#insn-00b46f3c) · [`00b46f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f0c.md#insn-00b46f18) · [`00b46f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f0c.md#insn-00b46f1c)

~~~diff
- 00b45f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46f3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46f3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45f48 bytes 60ee03f9
+ 00b46f3c bytes 60ce03f9
- 00b45f24 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46f18 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45f24 bytes 132f0090
+ 00b46f18 bytes 132f0090
- 00b45f28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45f28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46f1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46f1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45f28 bytes 68ee43f9
+ 00b46f1c bytes 68ce43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc33084d1dc0bbc34775f1cdcd1f52c2"></a>

### [`00b45f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f5c.md) → [`00b46f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f50.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b46f80",
      "incomplete_value": true,
      "site": "00b46f80",
      "value": [
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
    "old": {
      "definition_site": "00b45f8c",
      "incomplete_value": true,
      "site": "00b45f8c",
      "value": [
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
      "definition_site": "00b46f64",
      "incomplete_value": true,
      "site": "00b46f64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45f70",
      "incomplete_value": true,
      "site": "00b45f70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46f6c",
      "incomplete_value": false,
      "site": "00b46f78",
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
            "const:e41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45f78",
      "incomplete_value": false,
      "site": "00b45f84",
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
            "const:d63:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46f60",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f6c",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b46f80",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46f60",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f6c",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b46f80",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f5c.md#insn-00b45f84) · [`00b45f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f5c.md#insn-00b45f8c) · [`00b45f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f5c.md#insn-00b45f68)
- 新版 [`00b46f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f50.md#insn-00b46f78) · [`00b46f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f50.md#insn-00b46f80) · [`00b46f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46f50.md#insn-00b46f5c)

~~~diff
- 00b45f84 ["INT_ADD", "register:40f0:8", ["const:b45f84:8", "const:4:8"]]
- 00b45f84 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b46f78 ["INT_ADD", "register:40f0:8", ["const:b46f78:8", "const:4:8"]]
+ 00b46f78 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b45f84 bytes 17540494
+ 00b46f78 bytes 0e540494
- 00b45f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
- 00b45f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46f80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b46f80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45f8c bytes 60ee03f9
+ 00b46f80 bytes 60ce03f9
- 00b45f68 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46f5c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b45f68 bytes 132f0090
+ 00b46f5c bytes 132f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a99d0e80491a34bd579dd9efb6f0345"></a>

### [`00b45fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45fac.md) → [`00b46fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46fa0.md) _ZN8firebase4util3log15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b47028",
      "incomplete_value": true,
      "site": "00b47028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46034",
      "incomplete_value": true,
      "site": "00b46034",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46fb4",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46fd4",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47028",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46fb4",
      "READ",
      [
        "storage",
        "011267a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46fd4",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47028",
      "WRITE",
      [
        "storage",
        "011267a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45fac.md#insn-00b46034) · [`00b45fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45fac.md#insn-00b45fbc) · [`00b45fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45fac.md#insn-00b45fc0)
- 新版 [`00b47028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46fa0.md#insn-00b47028) · [`00b46fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46fa0.md#insn-00b46fb0) · [`00b46fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b46fa0.md#insn-00b46fb4)

~~~diff
- 00b46034 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46034 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e0:8"]]
- 00b46034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47028 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47028 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a0:8"]]
+ 00b47028 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46034 bytes a0821f39
+ 00b47028 bytes a0821e39
- 00b45fbc ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46fb0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b45fbc bytes 152f0090
+ 00b46fb0 bytes 152f0090
- 00b45fc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e0:8"]]
- 00b45fc0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b45fc0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46fb4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a0:8"]]
+ 00b46fb4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46fb4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b45fc0 bytes a8825f39
+ 00b46fb4 bytes a8825e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04f28270e359e7dc5aa3b7d5b28f9104"></a>

### [`00b46048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46048.md) → [`00b4703c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4703c.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47078",
      "incomplete_value": true,
      "site": "00b47078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46084",
      "incomplete_value": true,
      "site": "00b46084",
      "value": [
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b470c8",
      "incomplete_value": true,
      "site": "00b470c8",
      "value": [
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
    "old": {
      "definition_site": "00b460d4",
      "incomplete_value": true,
      "site": "00b460d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00b470b8",
      "incomplete_value": true,
      "site": "00b470c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:798:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b460c4",
      "incomplete_value": true,
      "site": "00b460d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
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
      "00b47050",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4705c",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47078",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47050",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4705c",
      "READ",
      [
        "storage",
        "011267a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47078",
      "WRITE",
      [
        "storage",
        "011267a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46048.md#insn-00b46084) · [`00b460d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46048.md#insn-00b460d0) · [`00b460d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46048.md#insn-00b460d4)
- 新版 [`00b47078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4703c.md#insn-00b47078) · [`00b470c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4703c.md#insn-00b470c4) · [`00b470c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4703c.md#insn-00b470c8)

~~~diff
- 00b46084 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e0:8"]]
- 00b46084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47078 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47078 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47078 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a0:8"]]
+ 00b47078 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46084 bytes bf821f39
+ 00b47078 bytes bf821e39
- 00b460d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b460d0 ["INT_ADD", "register:40f0:8", ["const:b460d0:8", "const:4:8"]]
- 00b460d0 ["CALLIND", null, ["register:0:8"]]
+ 00b470c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b470c4 ["INT_ADD", "register:40f0:8", ["const:b470c4:8", "const:4:8"]]
+ 00b470c4 ["CALLIND", null, ["register:0:8"]]
- 00b460d0 bytes 00013fd6
+ 00b470c4 bytes 00013fd6
- 00b460d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00b460d4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b460d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b470c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
+ 00b470c8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b470c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b460d4 bytes 9fee03f9
+ 00b470c8 bytes 9fce03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1796c305f42096ab43c4ab75f4408ebe"></a>

### [`00b460e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b460e8.md) → [`00b470dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b470dc.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4711c",
      "incomplete_value": true,
      "site": "00b4711c",
      "value": [
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
    "old": {
      "definition_site": "00b46128",
      "incomplete_value": true,
      "site": "00b46128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00b470f8",
      "incomplete_value": true,
      "site": "00b470f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46104",
      "incomplete_value": true,
      "site": "00b46104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47100",
      "incomplete_value": false,
      "site": "00b47114",
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
            "const:e41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4610c",
      "incomplete_value": false,
      "site": "00b46120",
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
            "const:d63:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b470f0",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47100",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b4711c",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b470f0",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47100",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b4711c",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b460e8.md#insn-00b46120) · [`00b46128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b460e8.md#insn-00b46128) · [`00b460f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b460e8.md#insn-00b460f4)
- 新版 [`00b47114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b470dc.md#insn-00b47114) · [`00b4711c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b470dc.md#insn-00b4711c) · [`00b470e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b470dc.md#insn-00b470e8)

~~~diff
- 00b46120 ["INT_ADD", "register:40f0:8", ["const:b46120:8", "const:4:8"]]
- 00b46120 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47114 ["INT_ADD", "register:40f0:8", ["const:b47114:8", "const:4:8"]]
+ 00b47114 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46120 bytes b0530494
+ 00b47114 bytes a7530494
- 00b46128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00b46128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4711c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
+ 00b4711c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46128 bytes 80ee03f9
+ 00b4711c bytes 80ce03f9
- 00b460f4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b470e8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b460f4 bytes f42e00f0
+ 00b470e8 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0be93b8a3694aa3198bd57e9289dfd9"></a>

### [`00b46158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46158.md) → [`00b4714c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4714c.md) _ZN8firebase4util3log11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b47168",
      "incomplete_value": false,
      "site": "00b4716c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46174",
      "incomplete_value": false,
      "site": "00b46178",
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
            "const:30b:8"
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
      "00b47168",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b47178",
      "DATA",
      [
        "storage",
        "011257e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47168",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b47178",
      "DATA",
      [
        "storage",
        "011267a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46158.md#insn-00b46178) · [`00b46174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46158.md#insn-00b46174) · [`00b4617c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46158.md#insn-00b4617c)
- 新版 [`00b4716c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4714c.md#insn-00b4716c) · [`00b47168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4714c.md#insn-00b47168) · [`00b47170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4714c.md#insn-00b47170)

~~~diff
- 00b46178 ["INT_ADD", "register:40f0:8", ["const:b46178:8", "const:4:8"]]
- 00b46178 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4716c ["INT_ADD", "register:40f0:8", ["const:b4716c:8", "const:4:8"]]
+ 00b4716c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46178 bytes d6530494
+ 00b4716c bytes cd530494
- 00b46174 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b46174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47168 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b47168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46174 bytes 002c0c91
+ 00b47168 bytes 008c1191
- 00b4617c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47170 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4617c bytes e82e00f0
+ 00b47170 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59c032724eed4d72c860dc67c85ef12"></a>

### [`00b46194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46194.md) → [`00b47188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47188.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b471c8",
      "incomplete_value": true,
      "site": "00b471c8",
      "value": [
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
    "old": {
      "definition_site": "00b461d4",
      "incomplete_value": true,
      "site": "00b461d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00b471a4",
      "incomplete_value": true,
      "site": "00b471a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b461b0",
      "incomplete_value": true,
      "site": "00b461b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b471ac",
      "incomplete_value": false,
      "site": "00b471c0",
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
            "const:e41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b461b8",
      "incomplete_value": false,
      "site": "00b461cc",
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
            "const:d63:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4719c",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b471ac",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ],
    [
      "00b471c8",
      "WRITE",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4719c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b471ac",
      "PARAM",
      [
        "storage",
        "002bbe41",
        null,
        "string"
      ]
    ],
    [
      "00b471c8",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b461cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46194.md#insn-00b461cc) · [`00b461d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46194.md#insn-00b461d4) · [`00b461a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46194.md#insn-00b461a0)
- 新版 [`00b471c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47188.md#insn-00b471c0) · [`00b471c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47188.md#insn-00b471c8) · [`00b47194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47188.md#insn-00b47194)

~~~diff
- 00b461cc ["INT_ADD", "register:40f0:8", ["const:b461cc:8", "const:4:8"]]
- 00b461cc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b471c0 ["INT_ADD", "register:40f0:8", ["const:b471c0:8", "const:4:8"]]
+ 00b471c0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b461cc bytes 85530494
+ 00b471c0 bytes 7c530494
- 00b461d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00b461d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b471c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
+ 00b471c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b461d4 bytes 80ee03f9
+ 00b471c8 bytes 80ce03f9
- 00b461a0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47194 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b461a0 bytes f42e00f0
+ 00b47194 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e0402502da1754ffd869d1a80c9925"></a>

### [`00b46204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46204.md) → [`00b471f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b471f8.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b47214",
      "incomplete_value": false,
      "site": "00b47218",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46220",
      "incomplete_value": false,
      "site": "00b46224",
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
            "const:54d:8"
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
      "definition_site": "00b47224",
      "incomplete_value": true,
      "site": "00b47230",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b46230",
      "incomplete_value": true,
      "site": "00b4623c",
      "value": [
        "LOAD",
        "8",
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
      "00b47214",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b47224",
      "DATA",
      [
        "storage",
        "011257f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47214",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b47224",
      "DATA",
      [
        "storage",
        "011267b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46204.md#insn-00b46224) · [`00b46220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46204.md#insn-00b46220) · [`00b46228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46204.md#insn-00b46228)
- 新版 [`00b47218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b471f8.md#insn-00b47218) · [`00b47214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b471f8.md#insn-00b47214) · [`00b4721c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b471f8.md#insn-00b4721c)

~~~diff
- 00b46224 ["INT_ADD", "register:40f0:8", ["const:b46224:8", "const:4:8"]]
- 00b46224 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b47218 ["INT_ADD", "register:40f0:8", ["const:b47218:8", "const:4:8"]]
+ 00b47218 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46224 bytes ab530494
+ 00b47218 bytes a2530494
- 00b46220 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b46220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47214 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b47214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46220 bytes 00341591
+ 00b47214 bytes 00681891
- 00b46228 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4721c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b46228 bytes e82e00f0
+ 00b4721c bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53d59ceb8b4f263cc387ed25ac70a637"></a>

### [`00b46240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46240.md) → [`00b47234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47234.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b47260",
      "incomplete_value": true,
      "site": "00b47260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4626c",
      "incomplete_value": true,
      "site": "00b4626c",
      "value": [
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
      "definition_site": "00b47248",
      "incomplete_value": true,
      "site": "00b47248",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46254",
      "incomplete_value": true,
      "site": "00b46254",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47254",
      "incomplete_value": false,
      "site": "00b47258",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46260",
      "incomplete_value": false,
      "site": "00b46264",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47244",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47254",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b47260",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47244",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47254",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b47260",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46240.md#insn-00b46264) · [`00b4626c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46240.md#insn-00b4626c) · [`00b4624c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46240.md#insn-00b4624c)
- 新版 [`00b47258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47234.md#insn-00b47258) · [`00b47260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47234.md#insn-00b47260) · [`00b47240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47234.md#insn-00b47240)

~~~diff
- 00b46264 ["INT_ADD", "register:40f0:8", ["const:b46264:8", "const:4:8"]]
- 00b46264 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47258 ["INT_ADD", "register:40f0:8", ["const:b47258:8", "const:4:8"]]
+ 00b47258 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46264 bytes 5f530494
+ 00b47258 bytes 56530494
- 00b4626c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b4626c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47260 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b47260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4626c bytes 60fe03f9
+ 00b47260 bytes 60de03f9
- 00b4624c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47240 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4624c bytes f32e00f0
+ 00b47240 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d996ac378e83ddb24d7856dd8405765f"></a>

### [`00b46280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46280.md) → [`00b47274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47274.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b472a0",
      "incomplete_value": true,
      "site": "00b472a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462ac",
      "incomplete_value": true,
      "site": "00b462ac",
      "value": [
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
      "definition_site": "00b47288",
      "incomplete_value": true,
      "site": "00b47288",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46294",
      "incomplete_value": true,
      "site": "00b46294",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b46294"
      ],
      [
        "FALL_THROUGH",
        "00b47288"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b47288",
      "incomplete_value": true,
      "site": "00b472a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46294",
      "incomplete_value": true,
      "site": "00b462ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b47284",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47290",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b472a0",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47284",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47290",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b472a0",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b462ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46280.md#insn-00b462ac) · [`00b4628c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46280.md#insn-00b4628c) · [`00b46290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46280.md#insn-00b46290)
- 新版 [`00b472a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47274.md#insn-00b472a0) · [`00b47280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47274.md#insn-00b47280) · [`00b47284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47274.md#insn-00b47284)

~~~diff
- 00b462ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b462ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b472a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b472a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b462ac bytes 60fe03f9
+ 00b472a0 bytes 60de03f9
- 00b4628c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47280 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4628c bytes f32e00f0
+ 00b47280 bytes f32e00f0
- 00b46290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b46290 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47284 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b47284 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46290 bytes 68fe43f9
+ 00b47284 bytes 68de43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823b281c7d09c77ef644bcfa67c3edd2"></a>

### [`00b462c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b462c0.md) → [`00b472b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472b4.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b472e4",
      "incomplete_value": true,
      "site": "00b472e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462f0",
      "incomplete_value": true,
      "site": "00b462f0",
      "value": [
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
      "definition_site": "00b472c8",
      "incomplete_value": true,
      "site": "00b472c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462d4",
      "incomplete_value": true,
      "site": "00b462d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b472d4",
      "incomplete_value": false,
      "site": "00b472dc",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462e0",
      "incomplete_value": false,
      "site": "00b462e8",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b472c4",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b472d4",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b472e4",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b472c4",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b472d4",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b472e4",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b462e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b462c0.md#insn-00b462e8) · [`00b462f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b462c0.md#insn-00b462f0) · [`00b462cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b462c0.md#insn-00b462cc)
- 新版 [`00b472dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472b4.md#insn-00b472dc) · [`00b472e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472b4.md#insn-00b472e4) · [`00b472c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472b4.md#insn-00b472c0)

~~~diff
- 00b462e8 ["INT_ADD", "register:40f0:8", ["const:b462e8:8", "const:4:8"]]
- 00b462e8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b472dc ["INT_ADD", "register:40f0:8", ["const:b472dc:8", "const:4:8"]]
+ 00b472dc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b462e8 bytes 3e530494
+ 00b472dc bytes 35530494
- 00b462f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b462f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b472e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b472e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b462f0 bytes 60fe03f9
+ 00b472e4 bytes 60de03f9
- 00b462cc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b472c0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b462cc bytes f32e00f0
+ 00b472c0 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbbe0993580708cfb5cca488d6f7846d"></a>

### [`00b46304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46304.md) → [`00b472f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472f8.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b47328",
      "incomplete_value": true,
      "site": "00b47328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46334",
      "incomplete_value": true,
      "site": "00b46334",
      "value": [
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
      "definition_site": "00b4730c",
      "incomplete_value": true,
      "site": "00b4730c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46318",
      "incomplete_value": true,
      "site": "00b46318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47314",
      "incomplete_value": false,
      "site": "00b47320",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46320",
      "incomplete_value": false,
      "site": "00b4632c",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47308",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47314",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b47328",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47308",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47314",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b47328",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4632c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46304.md#insn-00b4632c) · [`00b46334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46304.md#insn-00b46334) · [`00b46310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46304.md#insn-00b46310)
- 新版 [`00b47320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472f8.md#insn-00b47320) · [`00b47328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472f8.md#insn-00b47328) · [`00b47304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b472f8.md#insn-00b47304)

~~~diff
- 00b4632c ["INT_ADD", "register:40f0:8", ["const:b4632c:8", "const:4:8"]]
- 00b4632c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47320 ["INT_ADD", "register:40f0:8", ["const:b47320:8", "const:4:8"]]
+ 00b47320 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4632c bytes 2d530494
+ 00b47320 bytes 24530494
- 00b46334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b46334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b47328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46334 bytes 60fe03f9
+ 00b47328 bytes 60de03f9
- 00b46310 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47304 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46310 bytes f32e00f0
+ 00b47304 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47caabc2b431d0b8b399f732b86836fe"></a>

### [`00b46354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46354.md) → [`00b47348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47348.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b473d0",
      "incomplete_value": true,
      "site": "00b473d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b463dc",
      "incomplete_value": true,
      "site": "00b463dc",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4737c",
      "incomplete_value": true,
      "site": "00b47388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46388",
      "incomplete_value": true,
      "site": "00b46394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
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
      "00b4735c",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4737c",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b473d0",
      "WRITE",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4735c",
      "READ",
      [
        "storage",
        "011267c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4737c",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b473d0",
      "WRITE",
      [
        "storage",
        "011267c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46354.md#insn-00b46394) · [`00b463dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46354.md#insn-00b463dc) · [`00b46364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46354.md#insn-00b46364)
- 新版 [`00b47388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47348.md#insn-00b47388) · [`00b473d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47348.md#insn-00b473d0) · [`00b47358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47348.md#insn-00b47358)

~~~diff
- 00b46394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46394 ["INT_ADD", "register:40f0:8", ["const:b46394:8", "const:4:8"]]
- 00b46394 ["CALLIND", null, ["register:0:8"]]
+ 00b47388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47388 ["INT_ADD", "register:40f0:8", ["const:b47388:8", "const:4:8"]]
+ 00b47388 ["CALLIND", null, ["register:0:8"]]
- 00b46394 bytes 00013fd6
+ 00b47388 bytes 00013fd6
- 00b463dc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b463dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:800:8"]]
- 00b463dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b473d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b473d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c0:8"]]
+ 00b473d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b463dc bytes a0022039
+ 00b473d0 bytes a0021f39
- 00b46364 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47358 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b46364 bytes f52e00f0
+ 00b47358 bytes f52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2460eca881428c63fc4f9aaaf047aae"></a>

### [`00b463f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b463f0.md) → [`00b473e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b473e4.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b47420",
      "incomplete_value": true,
      "site": "00b47420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4642c",
      "incomplete_value": true,
      "site": "00b4642c",
      "value": [
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
      "definition_site": "00b47470",
      "incomplete_value": true,
      "site": "00b47470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4647c",
      "incomplete_value": true,
      "site": "00b4647c",
      "value": [
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
      "definition_site": "00b473fc",
      "incomplete_value": true,
      "site": "00b473fc",
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
      "definition_site": "00b46408",
      "incomplete_value": true,
      "site": "00b46408",
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
      "00b473f8",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47404",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47420",
      "WRITE",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b473f8",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47404",
      "READ",
      [
        "storage",
        "011267c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47420",
      "WRITE",
      [
        "storage",
        "011267c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4642c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b463f0.md#insn-00b4642c) · [`00b46478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b463f0.md#insn-00b46478) · [`00b4647c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b463f0.md#insn-00b4647c)
- 新版 [`00b47420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b473e4.md#insn-00b47420) · [`00b4746c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b473e4.md#insn-00b4746c) · [`00b47470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b473e4.md#insn-00b47470)

~~~diff
- 00b4642c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4642c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4642c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:800:8"]]
- 00b4642c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47420 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47420 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47420 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c0:8"]]
+ 00b47420 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4642c bytes bf022039
+ 00b47420 bytes bf021f39
- 00b46478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46478 ["INT_ADD", "register:40f0:8", ["const:b46478:8", "const:4:8"]]
- 00b46478 ["CALLIND", null, ["register:0:8"]]
+ 00b4746c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4746c ["INT_ADD", "register:40f0:8", ["const:b4746c:8", "const:4:8"]]
+ 00b4746c ["CALLIND", null, ["register:0:8"]]
- 00b46478 bytes 00013fd6
+ 00b4746c bytes 00013fd6
- 00b4647c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b4647c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4647c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47470 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b47470 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4647c bytes 9ffe03f9
+ 00b47470 bytes 9fde03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43d94efe3f6bdf8aa3aecff973251054"></a>

### [`00b46490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46490.md) → [`00b47484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47484.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b474c4",
      "incomplete_value": true,
      "site": "00b474c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b464d0",
      "incomplete_value": true,
      "site": "00b464d0",
      "value": [
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
      "definition_site": "00b474a0",
      "incomplete_value": true,
      "site": "00b474a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b464ac",
      "incomplete_value": true,
      "site": "00b464ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b474a8",
      "incomplete_value": false,
      "site": "00b474bc",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b464b4",
      "incomplete_value": false,
      "site": "00b464c8",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47498",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474a8",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b474c4",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47498",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474a8",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b474c4",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b464c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46490.md#insn-00b464c8) · [`00b464d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46490.md#insn-00b464d0) · [`00b4649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46490.md#insn-00b4649c)
- 新版 [`00b474bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47484.md#insn-00b474bc) · [`00b474c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47484.md#insn-00b474c4) · [`00b47490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47484.md#insn-00b47490)

~~~diff
- 00b464c8 ["INT_ADD", "register:40f0:8", ["const:b464c8:8", "const:4:8"]]
- 00b464c8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b474bc ["INT_ADD", "register:40f0:8", ["const:b474bc:8", "const:4:8"]]
+ 00b474bc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b464c8 bytes c6520494
+ 00b474bc bytes bd520494
- 00b464d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b464d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b474c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b474c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b464d0 bytes 80fe03f9
+ 00b474c4 bytes 80de03f9
- 00b4649c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47490 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4649c bytes f42e00f0
+ 00b47490 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

