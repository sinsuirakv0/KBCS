# v16.0.2 → v16.0.3 · 最優先の変更候補 (86)

[一覧の目次](README.md)

<a id="compare-9c6c18c19395bff6dd3ffa341e4344a1"></a>

### [`00bddc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md) → [`00bdec8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec8c.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdecbc",
      "incomplete_value": true,
      "site": "00bdecbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcc8",
      "incomplete_value": true,
      "site": "00bddcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdeca0",
      "incomplete_value": true,
      "site": "00bdeca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcac",
      "incomplete_value": true,
      "site": "00bddcac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdeca8",
      "incomplete_value": false,
      "site": "00bdecb4",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcb4",
      "incomplete_value": false,
      "site": "00bddcc0",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdec9c",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdeca8",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bdecbc",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdec9c",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdeca8",
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      "00bdecbc",
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddcc0) · [`00bddcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddcc8) · [`00bddca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddca4)
- 新版 [`00bdecb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec8c.md#insn-00bdecb4) · [`00bdecbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec8c.md#insn-00bdecbc) · [`00bdec98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec8c.md#insn-00bdec98)

~~~diff
- 00bddcc0 ["INT_ADD", "register:40f0:8", ["const:bddcc0:8", "const:4:8"]]
- 00bddcc0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bdecb4 ["INT_ADD", "register:40f0:8", ["const:bdecb4:8", "const:4:8"]]
+ 00bdecb4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bddcc0 bytes c8f40194
+ 00bdecb4 bytes bff40194
- 00bddcc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
- 00bddcc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdecbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ee8:8"]]
+ 00bdecbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddcc8 bytes 609607f9
+ 00bdecbc bytes 607607f9
- 00bddca4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bdec98 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bddca4 bytes 532a00b0
+ 00bdec98 bytes 532a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1c298f82c8d9d45ef8d47f07bfa84b5"></a>

### [`00bddce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md) → [`00bdecdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bded34",
      "incomplete_value": true,
      "site": "00bded34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd40",
      "incomplete_value": true,
      "site": "00bddd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "definition_site": "00bded10",
      "incomplete_value": true,
      "site": "00bded1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd1c",
      "incomplete_value": true,
      "site": "00bddd28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
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
      "00bdecf0",
      "READ",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bded10",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bded34",
      "WRITE",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdecf0",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bded10",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bded34",
      "WRITE",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddd28) · [`00bddd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddd40) · [`00bddcf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddcf8)
- 新版 [`00bded1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md#insn-00bded1c) · [`00bded34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md#insn-00bded34) · [`00bdecec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md#insn-00bdecec)

~~~diff
- 00bddd28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bddd28 ["INT_ADD", "register:40f0:8", ["const:bddd28:8", "const:4:8"]]
- 00bddd28 ["CALLIND", null, ["register:0:8"]]
+ 00bded1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bded1c ["INT_ADD", "register:40f0:8", ["const:bded1c:8", "const:4:8"]]
+ 00bded1c ["CALLIND", null, ["register:0:8"]]
- 00bddd28 bytes 00013fd6
+ 00bded1c bytes 00013fd6
- 00bddd40 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bddd40 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f30:8"]]
- 00bddd40 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bded34 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bded34 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ef0:8"]]
+ 00bded34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bddd40 bytes a0c23c39
+ 00bded34 bytes a0c23b39
- 00bddcf8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bdecec ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bddcf8 bytes 552a00b0
+ 00bdecec bytes 552a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd21f27595b64345cdae6a83e7e1305d"></a>

### [`00bddd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md) → [`00bded48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bded48.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bded84",
      "incomplete_value": true,
      "site": "00bded84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd90",
      "incomplete_value": true,
      "site": "00bddd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "definition_site": "00bdeda4",
      "incomplete_value": true,
      "site": "00bdeda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdddb0",
      "incomplete_value": true,
      "site": "00bdddb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bded60",
      "incomplete_value": true,
      "site": "00bded60",
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
      "definition_site": "00bddd6c",
      "incomplete_value": true,
      "site": "00bddd6c",
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
      "00bded5c",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bded68",
      "READ",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bded84",
      "WRITE",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bded5c",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bded68",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bded84",
      "WRITE",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bddd90) · [`00bdddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bdddac) · [`00bdddb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bdddb0)
- 新版 [`00bded84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bded48.md#insn-00bded84) · [`00bdeda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bded48.md#insn-00bdeda0) · [`00bdeda4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bded48.md#insn-00bdeda4)

~~~diff
- 00bddd90 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bddd90 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bddd90 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f30:8"]]
- 00bddd90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bded84 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bded84 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bded84 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ef0:8"]]
+ 00bded84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bddd90 bytes bfc23c39
+ 00bded84 bytes bfc23b39
- 00bdddac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdddac ["INT_ADD", "register:40f0:8", ["const:bdddac:8", "const:4:8"]]
- 00bdddac ["CALLIND", null, ["register:0:8"]]
+ 00bdeda0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdeda0 ["INT_ADD", "register:40f0:8", ["const:bdeda0:8", "const:4:8"]]
+ 00bdeda0 ["CALLIND", null, ["register:0:8"]]
- 00bdddac bytes 00013fd6
+ 00bdeda0 bytes 00013fd6
- 00bdddb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
- 00bdddb0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdddb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdeda4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
+ 00bdeda4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdeda4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdddb0 bytes 9f9607f9
+ 00bdeda4 bytes 9f7607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9af46344420b71a5bf8188f4c8b4383"></a>

### [`00bdddc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md) → [`00bdedb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdedf8",
      "incomplete_value": true,
      "site": "00bdedf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde04",
      "incomplete_value": true,
      "site": "00bdde04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdedd4",
      "incomplete_value": true,
      "site": "00bdedd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddde0",
      "incomplete_value": true,
      "site": "00bddde0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdeddc",
      "incomplete_value": false,
      "site": "00bdedf0",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddde8",
      "incomplete_value": false,
      "site": "00bdddfc",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdedcc",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdeddc",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bdedf8",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdedcc",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdeddc",
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      "00bdedf8",
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdddfc) · [`00bdde04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdde04) · [`00bdddd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdddd0)
- 新版 [`00bdedf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md#insn-00bdedf0) · [`00bdedf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md#insn-00bdedf8) · [`00bdedc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md#insn-00bdedc4)

~~~diff
- 00bdddfc ["INT_ADD", "register:40f0:8", ["const:bdddfc:8", "const:4:8"]]
- 00bdddfc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bdedf0 ["INT_ADD", "register:40f0:8", ["const:bdedf0:8", "const:4:8"]]
+ 00bdedf0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bdddfc bytes 79f40194
+ 00bdedf0 bytes 70f40194
- 00bdde04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
- 00bdde04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdedf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
+ 00bdedf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdde04 bytes 809607f9
+ 00bdedf8 bytes 807607f9
- 00bdddd0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdedc4 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdddd0 bytes 542a00b0
+ 00bdedc4 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff123ea9c0a70116681843ab0fb6448c"></a>

### [`00bdde34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md) → [`00bdee28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee28.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdee44",
      "incomplete_value": false,
      "site": "00bdee48",
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
      "definition_site": "00bdde50",
      "incomplete_value": false,
      "site": "00bdde54",
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
      "definition_site": "00bdee54",
      "incomplete_value": true,
      "site": "00bdee60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdde60",
      "incomplete_value": true,
      "site": "00bdde6c",
      "value": [
        "LOAD",
        "8",
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
      "00bdee44",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bdee54",
      "DATA",
      [
        "storage",
        "01126f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdee44",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00bdee54",
      "DATA",
      [
        "storage",
        "01127ef8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdde54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde54) · [`00bdde50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde50) · [`00bdde58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde58)
- 新版 [`00bdee48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee28.md#insn-00bdee48) · [`00bdee44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee28.md#insn-00bdee44) · [`00bdee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee28.md#insn-00bdee4c)

~~~diff
- 00bdde54 ["INT_ADD", "register:40f0:8", ["const:bdde54:8", "const:4:8"]]
- 00bdde54 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bdee48 ["INT_ADD", "register:40f0:8", ["const:bdee48:8", "const:4:8"]]
+ 00bdee48 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bdde54 bytes 9ff40194
+ 00bdee48 bytes 96f40194
- 00bdde50 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00bdde50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdde50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdde50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdee44 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00bdee44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdee44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdee44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdde50 bytes 002c0c91
+ 00bdee44 bytes 008c1191
- 00bdde58 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bdee4c ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bdde58 bytes 482a00b0
+ 00bdee4c bytes 482a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff6e94105afb2145030fa6d9fb74e5b"></a>

### [`00bdde70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md) → [`00bdee64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee64.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdeea4",
      "incomplete_value": true,
      "site": "00bdeea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddeb0",
      "incomplete_value": true,
      "site": "00bddeb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdee80",
      "incomplete_value": true,
      "site": "00bdee80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde8c",
      "incomplete_value": true,
      "site": "00bdde8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdee88",
      "incomplete_value": false,
      "site": "00bdee9c",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde94",
      "incomplete_value": false,
      "site": "00bddea8",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdee78",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdee88",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bdeea4",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdee78",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdee88",
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      "00bdeea4",
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md#insn-00bddea8) · [`00bddeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md#insn-00bddeb0) · [`00bdde7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md#insn-00bdde7c)
- 新版 [`00bdee9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee64.md#insn-00bdee9c) · [`00bdeea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee64.md#insn-00bdeea4) · [`00bdee70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee64.md#insn-00bdee70)

~~~diff
- 00bddea8 ["INT_ADD", "register:40f0:8", ["const:bddea8:8", "const:4:8"]]
- 00bddea8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bdee9c ["INT_ADD", "register:40f0:8", ["const:bdee9c:8", "const:4:8"]]
+ 00bdee9c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bddea8 bytes 4ef40194
+ 00bdee9c bytes 45f40194
- 00bddeb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
- 00bddeb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdeea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
+ 00bdeea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddeb0 bytes 809607f9
+ 00bdeea4 bytes 807607f9
- 00bdde7c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdee70 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdde7c bytes 542a00b0
+ 00bdee70 bytes 542a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec6d6ec59a2512a4fb01e8989307c17"></a>

### [`00bddee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md) → [`00bdeed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeed4.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdeef0",
      "incomplete_value": false,
      "site": "00bdeef4",
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
      "definition_site": "00bddefc",
      "incomplete_value": false,
      "site": "00bddf00",
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
      "definition_site": "00bdef00",
      "incomplete_value": true,
      "site": "00bdef0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bddf0c",
      "incomplete_value": true,
      "site": "00bddf18",
      "value": [
        "LOAD",
        "8",
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
      "00bdeef0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bdef00",
      "DATA",
      [
        "storage",
        "01126f58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdeef0",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00bdef00",
      "DATA",
      [
        "storage",
        "01127f18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddf00) · [`00bddefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddefc) · [`00bddf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddf04)
- 新版 [`00bdeef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeed4.md#insn-00bdeef4) · [`00bdeef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeed4.md#insn-00bdeef0) · [`00bdeef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeed4.md#insn-00bdeef8)

~~~diff
- 00bddf00 ["INT_ADD", "register:40f0:8", ["const:bddf00:8", "const:4:8"]]
- 00bddf00 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bdeef4 ["INT_ADD", "register:40f0:8", ["const:bdeef4:8", "const:4:8"]]
+ 00bdeef4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bddf00 bytes 74f40194
+ 00bdeef4 bytes 6bf40194
- 00bddefc ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00bddefc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bddefc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bddefc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdeef0 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00bdeef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdeef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdeef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bddefc bytes 00341591
+ 00bdeef0 bytes 00681891
- 00bddf04 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bdeef8 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bddf04 bytes 482a00b0
+ 00bdeef8 bytes 482a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b8c594ec11562e0c521e3d151b3e67"></a>

### [`00bddf1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md) → [`00bdef10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd20.md) · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5ecf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ecf0.md) · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.05% / 新版 78.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_condition` 1件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bdef54",
      "incomplete_value": true,
      "site": "00bdef54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddf60",
      "incomplete_value": true,
      "site": "00bddf60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bdefac",
      "incomplete_value": true,
      "site": "00bdefac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddfb8",
      "incomplete_value": true,
      "site": "00bddfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bdf004",
      "incomplete_value": true,
      "site": "00bdf004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde010",
      "incomplete_value": true,
      "site": "00bde010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "00bdef28",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdef38",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdef54",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdef28",
      "READ",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdef38",
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      "00bdef54",
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf58) · [`00bddf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf60) · [`00bddf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf84)
- 新版 [`00bdef4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md#insn-00bdef4c) · [`00bdef54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md#insn-00bdef54) · [`00bdef78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md#insn-00bdef78)

~~~diff
- 00bddf58 ["INT_ADD", "register:40f0:8", ["const:bddf58:8", "const:4:8"]]
- 00bddf58 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bdef4c ["INT_ADD", "register:40f0:8", ["const:bdef4c:8", "const:4:8"]]
+ 00bdef4c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bddf58 bytes 22f40194
+ 00bdef4c bytes 19f40194
- 00bddf60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e00:8"]]
- 00bddf60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdef54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc0:8"]]
+ 00bdef54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddf60 bytes a00207f9
+ 00bdef54 bytes a0e206f9
- 00bddf84 ["INT_ADD", "register:40f0:8", ["const:bddf84:8", "const:4:8"]]
- 00bddf84 ["CALL", null, ["callee:00c5bfd0:8"]]
+ 00bdef78 ["INT_ADD", "register:40f0:8", ["const:bdef78:8", "const:4:8"]]
+ 00bdef78 ["CALL", null, ["callee:00c5bfd0:8"]]
- 00bddf84 bytes 1ff40194
+ 00bdef78 bytes 16f40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af84ab670b729cf297d45e6c5dafcbf0"></a>

### [`00bde108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md) → [`00bdf0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf0fc.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd40.md) · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5ed10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed10.md) · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.58% / 新版 85.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bdf138",
      "incomplete_value": true,
      "site": "00bdf138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde144",
      "incomplete_value": true,
      "site": "00bde144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "definition_site": "00bdf158",
      "incomplete_value": true,
      "site": "00bdf158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde164",
      "incomplete_value": true,
      "site": "00bde164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bdf184",
      "incomplete_value": true,
      "site": "00bdf184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde190",
      "incomplete_value": true,
      "site": "00bde190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00bdf110",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdf120",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdf138",
      "WRITE",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdf110",
      "READ",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdf120",
      "READ",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdf138",
      "WRITE",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md#insn-00bde144) · [`00bde160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md#insn-00bde160) · [`00bde164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md#insn-00bde164)
- 新版 [`00bdf138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf0fc.md#insn-00bdf138) · [`00bdf154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf0fc.md#insn-00bdf154) · [`00bdf158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf0fc.md#insn-00bdf158)

~~~diff
- 00bde144 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bde144 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bde144 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e08:8"]]
- 00bde144 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdf138 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdf138 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdf138 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:dc8:8"]]
+ 00bdf138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bde144 bytes bf223839
+ 00bdf138 bytes bf223739
- 00bde160 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bde160 ["INT_ADD", "register:40f0:8", ["const:bde160:8", "const:4:8"]]
- 00bde160 ["CALLIND", null, ["register:0:8"]]
+ 00bdf154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdf154 ["INT_ADD", "register:40f0:8", ["const:bdf154:8", "const:4:8"]]
+ 00bdf154 ["CALLIND", null, ["register:0:8"]]
- 00bde160 bytes 00013fd6
+ 00bdf154 bytes 00013fd6
- 00bde164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bde164 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bde164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdf158 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
+ 00bdf158 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdf158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bde164 bytes 9f0207f9
+ 00bdf158 bytes 9fe206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd2c6f9f3ee38a3fec5c3b0b0915d76"></a>

### [`00bde740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md) → [`00bdf734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf734.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00bdf8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf8a8.md) · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

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
      "definition_site": "00bdf7b8",
      "incomplete_value": false,
      "site": "00bdf7bc",
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
            "const:ffe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde7c4",
      "incomplete_value": false,
      "site": "00bde7c8",
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
            "const:f2f:8"
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
      "definition_site": "00bdf7c4",
      "incomplete_value": true,
      "site": "00bdf7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde7d0",
      "incomplete_value": true,
      "site": "00bde7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
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
      "00bdf7b8",
      "PARAM",
      [
        "storage",
        "002b6f2f",
        null,
        "string"
      ]
    ],
    [
      "00bdf7c4",
      "READ",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf7b8",
      "PARAM",
      [
        "storage",
        "002b6ffe",
        null,
        "string"
      ]
    ],
    [
      "00bdf7c4",
      "READ",
      [
        "storage",
        "01127dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde7c8) · [`00bde7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde7dc) · [`00bde784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde784)
- 新版 [`00bdf7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf734.md#insn-00bdf7bc) · [`00bdf7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf734.md#insn-00bdf7d0) · [`00bdf778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf734.md#insn-00bdf778)

~~~diff
- 00bde7c8 ["INT_ADD", "register:40f0:8", ["const:bde7c8:8", "const:4:8"]]
- 00bde7c8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bdf7bc ["INT_ADD", "register:40f0:8", ["const:bdf7bc:8", "const:4:8"]]
+ 00bdf7bc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bde7c8 bytes 42f20194
+ 00bdf7bc bytes 39f20194
- 00bde7dc ["INT_ADD", "register:40f0:8", ["const:bde7dc:8", "const:4:8"]]
- 00bde7dc ["CALL", null, ["callee:00497b94:8"]]
+ 00bdf7d0 ["INT_ADD", "register:40f0:8", ["const:bdf7d0:8", "const:4:8"]]
+ 00bdf7d0 ["CALL", null, ["callee:00497b94:8"]]
- 00bde7dc bytes 26e4e297
+ 00bdf7d0 bytes f1e0e297
- 00bde784 ["INT_ADD", "register:40f0:8", ["const:bde784:8", "const:4:8"]]
- 00bde784 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bdf778 ["INT_ADD", "register:40f0:8", ["const:bdf778:8", "const:4:8"]]
+ 00bdf778 ["CALL", null, ["callee:00c5c120:8"]]
- 00bde784 bytes 73f20194
+ 00bdf778 bytes 6af20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f214658bbb2c92e2b38b2e5228697c05"></a>

### [`00bdec18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md) → [`00bdfc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfc0c.md) _ZNK8firebase4auth4User13provider_dataEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab80.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5bb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb50.md) · 呼出先 14件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.98% / 新版 98.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be01a8",
      "incomplete_value": true,
      "site": "00be01ac",
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
      "definition_site": "00bdf1b4",
      "incomplete_value": true,
      "site": "00bdf1b8",
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
    "ordinal": 102,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdfc6c",
      "incomplete_value": true,
      "site": "00bdfc7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdec78",
      "incomplete_value": true,
      "site": "00bdec88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "definition_site": "00bdfe58",
      "incomplete_value": true,
      "site": "00bdfe64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdee64",
      "incomplete_value": true,
      "site": "00bdee70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdfc6c",
      "READ",
      [
        "storage",
        "01126e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfcbc",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfcc4",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bdfc6c",
      "READ",
      [
        "storage",
        "01127e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfcbc",
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfcc4",
      "READ",
      [
        "storage",
        "00c9ca68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdec88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md#insn-00bdec88) · [`00bdee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md#insn-00bdee70) · [`00bdef14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md#insn-00bdef14)
- 新版 [`00bdfc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfc0c.md#insn-00bdfc7c) · [`00bdfe64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfc0c.md#insn-00bdfe64) · [`00bdff08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfc0c.md#insn-00bdff08)

~~~diff
- 00bdec88 ["INT_ADD", "register:40f0:8", ["const:bdec88:8", "const:4:8"]]
- 00bdec88 ["CALL", null, ["callee:00497b94:8"]]
+ 00bdfc7c ["INT_ADD", "register:40f0:8", ["const:bdfc7c:8", "const:4:8"]]
+ 00bdfc7c ["CALL", null, ["callee:00497b94:8"]]
- 00bdec88 bytes fbe2e297
+ 00bdfc7c bytes c6dfe297
- 00bdee70 ["INT_ADD", "register:40f0:8", ["const:bdee70:8", "const:4:8"]]
- 00bdee70 ["CALL", null, ["callee:00497b94:8"]]
+ 00bdfe64 ["INT_ADD", "register:40f0:8", ["const:bdfe64:8", "const:4:8"]]
+ 00bdfe64 ["CALL", null, ["callee:00497b94:8"]]
- 00bdee70 bytes 81e2e297
+ 00bdfe64 bytes 4cdfe297
- 00bdef14 ["INT_ADD", "register:40f0:8", ["const:bdef14:8", "const:4:8"]]
- 00bdef14 ["CALL", null, ["callee:00497b94:8"]]
+ 00bdff08 ["INT_ADD", "register:40f0:8", ["const:bdff08:8", "const:4:8"]]
+ 00bdff08 ["CALL", null, ["callee:00497b94:8"]]
- 00bdef14 bytes 58e2e297
+ 00bdff08 bytes 23dfe297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d1d890230fbfee5adbca461b004818"></a>

### [`00bdf324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md) → [`00be0318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0318.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfa0.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df70.md)
- 新版 呼出元 1件 [`00c5ef70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef70.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0428",
      "incomplete_value": false,
      "site": "00be042c",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf434",
      "incomplete_value": false,
      "site": "00bdf438",
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
            "const:61f:8"
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
      "00be0428",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00be0428",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md#insn-00bdf438) · [`00bdf394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md#insn-00bdf394) · [`00bdf3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md#insn-00bdf3b8)
- 新版 [`00be042c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0318.md#insn-00be042c) · [`00be0388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0318.md#insn-00be0388) · [`00be03ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0318.md#insn-00be03ac)

~~~diff
- 00bdf438 ["INT_ADD", "register:40f0:8", ["const:bdf438:8", "const:4:8"]]
- 00bdf438 ["CALL", null, ["callee:00b41350:8"]]
+ 00be042c ["INT_ADD", "register:40f0:8", ["const:be042c:8", "const:4:8"]]
+ 00be042c ["CALL", null, ["callee:00b41350:8"]]
- 00bdf438 bytes c983fd97
+ 00be042c bytes c983fd97
- 00bdf394 ["INT_ADD", "register:40f0:8", ["const:bdf394:8", "const:4:8"]]
- 00bdf394 ["CALL", null, ["callee:00c58f30:8"]]
+ 00be0388 ["INT_ADD", "register:40f0:8", ["const:be0388:8", "const:4:8"]]
+ 00be0388 ["CALL", null, ["callee:00c58f30:8"]]
- 00bdf394 bytes f3e20194
+ 00be0388 bytes eae20194
- 00bdf3b8 ["INT_ADD", "register:40f0:8", ["const:bdf3b8:8", "const:4:8"]]
- 00bdf3b8 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00be03ac ["INT_ADD", "register:40f0:8", ["const:be03ac:8", "const:4:8"]]
+ 00be03ac ["CALL", null, ["callee:00c5ef40:8"]]
- 00bdf3b8 bytes eefa0194
+ 00be03ac bytes e5fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09e0b799a37af5057f66bf9d45024535"></a>

### [`00bdf578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md) → [`00be056c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be056c.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0598",
      "incomplete_value": true,
      "site": "00be05a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf5a4",
      "incomplete_value": true,
      "site": "00bdf5b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ed0:8"
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
      "00be0598",
      "READ",
      [
        "storage",
        "01126ed0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be0598",
      "READ",
      [
        "storage",
        "01127e90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf5b0) · [`00bdf594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf594) · [`00bdf5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf5a0)
- 新版 [`00be05a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be056c.md#insn-00be05a4) · [`00be0588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be056c.md#insn-00be0588) · [`00be0594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be056c.md#insn-00be0594)

~~~diff
- 00bdf5b0 ["INT_ADD", "register:40f0:8", ["const:bdf5b0:8", "const:4:8"]]
- 00bdf5b0 ["CALL", null, ["callee:00497b94:8"]]
+ 00be05a4 ["INT_ADD", "register:40f0:8", ["const:be05a4:8", "const:4:8"]]
+ 00be05a4 ["CALL", null, ["callee:00497b94:8"]]
- 00bdf5b0 bytes b1e0e297
+ 00be05a4 bytes 7cdde297
- 00bdf594 ["INT_ADD", "register:40f0:8", ["const:bdf594:8", "const:4:8"]]
- 00bdf594 ["CALL", null, ["callee:00c5c120:8"]]
+ 00be0588 ["INT_ADD", "register:40f0:8", ["const:be0588:8", "const:4:8"]]
+ 00be0588 ["CALL", null, ["callee:00c5c120:8"]]
- 00bdf594 bytes efee0194
+ 00be0588 bytes e6ee0194
- 00bdf5a0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00be0594 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bdf5a0 bytes 282a00f0
+ 00be0594 bytes 282a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-633f29d6f7bcd9cfe2610f5ee3181bde"></a>

### [`00bdf5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md) → [`00be05f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md) _ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be061c",
      "incomplete_value": true,
      "site": "00be0628",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf628",
      "incomplete_value": true,
      "site": "00bdf634",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ee0:8"
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
      "00be061c",
      "READ",
      [
        "storage",
        "01126ee0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be061c",
      "READ",
      [
        "storage",
        "01127ea0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md#insn-00bdf634) · [`00bdf618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md#insn-00bdf618) · [`00bdf624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md#insn-00bdf624)
- 新版 [`00be0628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md#insn-00be0628) · [`00be060c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md#insn-00be060c) · [`00be0618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md#insn-00be0618)

~~~diff
- 00bdf634 ["INT_ADD", "register:40f0:8", ["const:bdf634:8", "const:4:8"]]
- 00bdf634 ["CALL", null, ["callee:00497b94:8"]]
+ 00be0628 ["INT_ADD", "register:40f0:8", ["const:be0628:8", "const:4:8"]]
+ 00be0628 ["CALL", null, ["callee:00497b94:8"]]
- 00bdf634 bytes 90e0e297
+ 00be0628 bytes 5bdde297
- 00bdf618 ["INT_ADD", "register:40f0:8", ["const:bdf618:8", "const:4:8"]]
- 00bdf618 ["CALL", null, ["callee:00c5c120:8"]]
+ 00be060c ["INT_ADD", "register:40f0:8", ["const:be060c:8", "const:4:8"]]
+ 00be060c ["CALL", null, ["callee:00c5c120:8"]]
- 00bdf618 bytes ceee0194
+ 00be060c bytes c5ee0194
- 00bdf624 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00be0618 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bdf624 bytes 282a00f0
+ 00be0618 bytes 282a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e52e9afb8201636fa7458a2a31c834a"></a>

### [`00bdf788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md) → [`00be077c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be077c.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5ec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be0798",
      "incomplete_value": true,
      "site": "00be079c",
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
      "definition_site": "00bdf7a4",
      "incomplete_value": true,
      "site": "00bdf7a8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be0790",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00be079c",
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be0790",
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      "00be079c",
      "DATA",
      [
        "storage",
        "00c939b0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md#insn-00bdf794) · [`00bdf79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md#insn-00bdf79c) · [`00bdf7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md#insn-00bdf7b0)
- 新版 [`00be0788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be077c.md#insn-00be0788) · [`00be0790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be077c.md#insn-00be0790) · [`00be07a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be077c.md#insn-00be07a4)

~~~diff
- 00bdf794 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be0788 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bdf794 bytes e9050090
+ 00be0788 bytes e9050090
- 00bdf79c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
- 00bdf79c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be0790 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b00:8"]]
+ 00be0790 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf79c bytes 299945f9
+ 00be0790 bytes 298145f9
- 00bdf7b0 ["INT_ADD", "register:40f0:8", ["const:bdf7b0:8", "const:4:8"]]
- 00bdf7b0 ["CALL", null, ["callee:00c5c120:8"]]
+ 00be07a4 ["INT_ADD", "register:40f0:8", ["const:be07a4:8", "const:4:8"]]
+ 00be07a4 ["CALL", null, ["callee:00c5c120:8"]]
- 00bdf7b0 bytes 68ee0194
+ 00be07a4 bytes 5fee0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa5d166a6aad9ec06e176ee6bbb2f020"></a>

### [`00bdfa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md) → [`00be0a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00bd1550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

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
      "definition_site": "00be0a98",
      "incomplete_value": true,
      "site": "00be0aa8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdfaa4",
      "incomplete_value": true,
      "site": "00bdfab4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f38:8"
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
      "definition_site": "00be0d50",
      "incomplete_value": true,
      "site": "00be0d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdfd5c",
      "incomplete_value": true,
      "site": "00bdfd6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be0a94",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00be0a98",
      "READ",
      [
        "storage",
        "01126f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00be0acc",
      "READ",
      [
        "storage",
        "01126f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be0a94",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00be0a98",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "00be0acc",
      "READ",
      [
        "storage",
        "01127f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md#insn-00bdfab4) · [`00bdfd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md#insn-00bdfd6c) · [`00bdfa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md#insn-00bdfa74)
- 新版 [`00be0aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md#insn-00be0aa8) · [`00be0d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md#insn-00be0d60) · [`00be0a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md#insn-00be0a68)

~~~diff
- 00bdfab4 ["INT_ADD", "register:40f0:8", ["const:bdfab4:8", "const:4:8"]]
- 00bdfab4 ["CALL", null, ["callee:00589a54:8"]]
+ 00be0aa8 ["INT_ADD", "register:40f0:8", ["const:be0aa8:8", "const:4:8"]]
+ 00be0aa8 ["CALL", null, ["callee:00589a54:8"]]
- 00bdfab4 bytes 20a7e697
+ 00be0aa8 bytes eba3e697
- 00bdfd6c ["INT_ADD", "register:40f0:8", ["const:bdfd6c:8", "const:4:8"]]
- 00bdfd6c ["CALL", null, ["callee:00c5bfe0:8"]]
+ 00be0d60 ["INT_ADD", "register:40f0:8", ["const:be0d60:8", "const:4:8"]]
+ 00be0d60 ["CALL", null, ["callee:00c5bfe0:8"]]
- 00bdfd6c bytes a9ec0194
+ 00be0d60 bytes a0ec0194
- 00bdfa74 ["INT_ADD", "register:40f0:8", ["const:bdfa74:8", "const:4:8"]]
- 00bdfa74 ["CALL", null, ["callee:00c5bee0:8"]]
+ 00be0a68 ["INT_ADD", "register:40f0:8", ["const:be0a68:8", "const:4:8"]]
+ 00be0a68 ["CALL", null, ["callee:00c5bee0:8"]]
- 00bdfa74 bytes 27ed0194
+ 00be0a68 bytes 1eed0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49475db1f6214776cf7f4078ff50f6ca"></a>

### [`00be0014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md) → [`00be1008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1008.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00be1044",
      "incomplete_value": false,
      "site": "00be1048",
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
            "const:cd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0050",
      "incomplete_value": false,
      "site": "00be0054",
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
            "const:c02:8"
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
      "00be1044",
      "PARAM",
      [
        "storage",
        "002b5c02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00be1044",
      "PARAM",
      [
        "storage",
        "002b5cd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md#insn-00be0054) · [`00be0050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md#insn-00be0050) · [`00be0060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md#insn-00be0060)
- 新版 [`00be1048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1008.md#insn-00be1048) · [`00be1044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1008.md#insn-00be1044) · [`00be1054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1008.md#insn-00be1054)

~~~diff
- 00be0054 ["INT_ADD", "register:40f0:8", ["const:be0054:8", "const:4:8"]]
- 00be0054 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00be1048 ["INT_ADD", "register:40f0:8", ["const:be1048:8", "const:4:8"]]
+ 00be1048 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00be0054 bytes 1fec0194
+ 00be1048 bytes 16ec0194
- 00be0050 ["COPY", "tmp:0:8", ["const:c02:8"]]
- 00be0050 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00be0050 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00be0050 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00be1044 ["COPY", "tmp:0:8", ["const:cd1:8"]]
+ 00be1044 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00be1044 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00be1044 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00be0050 bytes 00083091
+ 00be1044 bytes 00443391
- 00be0060 ["INT_ADD", "register:40f0:8", ["const:be0060:8", "const:4:8"]]
- 00be0060 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be1054 ["INT_ADD", "register:40f0:8", ["const:be1054:8", "const:4:8"]]
+ 00be1054 ["CALL", null, ["callee:00c5bd10:8"]]
- 00be0060 bytes 38eb0194
+ 00be1054 bytes 2feb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495583918c2c8748a3411120f5644fd7"></a>

### [`00be02a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md) → [`00be1294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd01a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md) [`00bd4cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4cd8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bd119c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md) [`00bd5ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5ccc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be1390",
      "incomplete_value": true,
      "site": "00be1390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be039c",
      "incomplete_value": true,
      "site": "00be039c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
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
      "definition_site": "00be132c",
      "incomplete_value": true,
      "site": "00be133c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:e30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0338",
      "incomplete_value": true,
      "site": "00be0348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
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
      "definition_site": "00be13dc",
      "incomplete_value": false,
      "site": "00be13f0",
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
            "const:903:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be03e8",
      "incomplete_value": false,
      "site": "00be03fc",
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
            "const:82c:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be132c",
      "READ",
      [
        "storage",
        "01126e70",
        null,
        "undefined8"
      ]
    ],
    [
      "00be138c",
      "READ",
      [
        "storage",
        "00c9baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00be1390",
      "DATA",
      [
        "storage",
        "00bd4cd8",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00be132c",
      "READ",
      [
        "storage",
        "01127e30",
        null,
        "undefined8"
      ]
    ],
    [
      "00be138c",
      "READ",
      [
        "storage",
        "00c9cac8",
        null,
        "pointer"
      ]
    ],
    [
      "00be1390",
      "DATA",
      [
        "storage",
        "00bd5ccc",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md#insn-00be0348) · [`00be03fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md#insn-00be03fc) · [`00be0424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md#insn-00be0424)
- 新版 [`00be133c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md#insn-00be133c) · [`00be13f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md#insn-00be13f0) · [`00be1418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md#insn-00be1418)

~~~diff
- 00be0348 ["INT_ADD", "register:40f0:8", ["const:be0348:8", "const:4:8"]]
- 00be0348 ["CALL", null, ["callee:00497b94:8"]]
+ 00be133c ["INT_ADD", "register:40f0:8", ["const:be133c:8", "const:4:8"]]
+ 00be133c ["CALL", null, ["callee:00497b94:8"]]
- 00be0348 bytes 4bdde297
+ 00be133c bytes 16dae297
- 00be03fc ["INT_ADD", "register:40f0:8", ["const:be03fc:8", "const:4:8"]]
- 00be03fc ["CALL", null, ["callee:00c5ec80:8"]]
+ 00be13f0 ["INT_ADD", "register:40f0:8", ["const:be13f0:8", "const:4:8"]]
+ 00be13f0 ["CALL", null, ["callee:00c5ec80:8"]]
- 00be03fc bytes 2df60194
+ 00be13f0 bytes 24f60194
- 00be0424 ["INT_ADD", "register:40f0:8", ["const:be0424:8", "const:4:8"]]
- 00be0424 ["CALL", null, ["callee:00c5bfe0:8"]]
+ 00be1418 ["INT_ADD", "register:40f0:8", ["const:be1418:8", "const:4:8"]]
+ 00be1418 ["CALL", null, ["callee:00c5bfe0:8"]]
- 00be0424 bytes fbea0194
+ 00be1418 bytes f2ea0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-771ec16c61259959504484f63682cad1"></a>

### [`00be0aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md) → [`00be1aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1aa0.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00be1adc",
      "incomplete_value": false,
      "site": "00be1ae0",
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
            "const:cd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0ae8",
      "incomplete_value": false,
      "site": "00be0aec",
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
            "const:c02:8"
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
      "00be1adc",
      "PARAM",
      [
        "storage",
        "002b5c02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00be1adc",
      "PARAM",
      [
        "storage",
        "002b5cd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0aec) · [`00be0ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0ae8) · [`00be0af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0af8)
- 新版 [`00be1ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1aa0.md#insn-00be1ae0) · [`00be1adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1aa0.md#insn-00be1adc) · [`00be1aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1aa0.md#insn-00be1aec)

~~~diff
- 00be0aec ["INT_ADD", "register:40f0:8", ["const:be0aec:8", "const:4:8"]]
- 00be0aec ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00be1ae0 ["INT_ADD", "register:40f0:8", ["const:be1ae0:8", "const:4:8"]]
+ 00be1ae0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00be0aec bytes 79e90194
+ 00be1ae0 bytes 70e90194
- 00be0ae8 ["COPY", "tmp:0:8", ["const:c02:8"]]
- 00be0ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00be0ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00be0ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00be1adc ["COPY", "tmp:0:8", ["const:cd1:8"]]
+ 00be1adc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00be1adc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00be1adc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00be0ae8 bytes 00083091
+ 00be1adc bytes 00443391
- 00be0af8 ["INT_ADD", "register:40f0:8", ["const:be0af8:8", "const:4:8"]]
- 00be0af8 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00be1aec ["INT_ADD", "register:40f0:8", ["const:be1aec:8", "const:4:8"]]
+ 00be1aec ["CALL", null, ["callee:00c5bd10:8"]]
- 00be0af8 bytes 92e80194
+ 00be1aec bytes 89e80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29ada1f9212044d0200c0f07db4fdff8"></a>

### [`00be1140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md) → [`00be2134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2134.md) _ZNK8firebase4auth4User8metadataEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0058f8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f8fc.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

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
      "definition_site": "00be2168",
      "incomplete_value": true,
      "site": "00be2174",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be1174",
      "incomplete_value": true,
      "site": "00be1180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
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
      "definition_site": "00be2190",
      "incomplete_value": true,
      "site": "00be219c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be119c",
      "incomplete_value": true,
      "site": "00be11a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "00be2168",
      "READ",
      [
        "storage",
        "01126ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be2190",
      "READ",
      [
        "storage",
        "01126f10",
        null,
        "undefined8"
      ]
    ],
    [
      "00be21a0",
      "READ",
      [
        "storage",
        "01126f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be2168",
      "READ",
      [
        "storage",
        "01127e60",
        null,
        "undefined8"
      ]
    ],
    [
      "00be2190",
      "READ",
      [
        "storage",
        "01127ed0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be21a0",
      "READ",
      [
        "storage",
        "01127ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be1180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be1180) · [`00be11a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be11a8) · [`00be1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be1168)
- 新版 [`00be2174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2134.md#insn-00be2174) · [`00be219c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2134.md#insn-00be219c) · [`00be215c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2134.md#insn-00be215c)

~~~diff
- 00be1180 ["INT_ADD", "register:40f0:8", ["const:be1180:8", "const:4:8"]]
- 00be1180 ["CALL", null, ["callee:00497b94:8"]]
+ 00be2174 ["INT_ADD", "register:40f0:8", ["const:be2174:8", "const:4:8"]]
+ 00be2174 ["CALL", null, ["callee:00497b94:8"]]
- 00be1180 bytes bdd9e297
+ 00be2174 bytes 88d6e297
- 00be11a8 ["INT_ADD", "register:40f0:8", ["const:be11a8:8", "const:4:8"]]
- 00be11a8 ["CALL", null, ["callee:0058f8fc:8"]]
+ 00be219c ["INT_ADD", "register:40f0:8", ["const:be219c:8", "const:4:8"]]
+ 00be219c ["CALL", null, ["callee:0058f8fc:8"]]
- 00be11a8 bytes 0db9e697
+ 00be219c bytes d8b5e697
- 00be1168 ["INT_ADD", "register:40f0:8", ["const:be1168:8", "const:4:8"]]
- 00be1168 ["CALL", null, ["callee:00c5c120:8"]]
+ 00be215c ["INT_ADD", "register:40f0:8", ["const:be215c:8", "const:4:8"]]
+ 00be215c ["CALL", null, ["callee:00c5c120:8"]]
- 00be1168 bytes fae70194
+ 00be215c bytes f1e70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5da5f014e01da14b1a28f22c09965544"></a>

### [`00be12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md) → [`00be22c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be22c0.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5ec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be22dc",
      "incomplete_value": true,
      "site": "00be22e0",
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
      "definition_site": "00be12e8",
      "incomplete_value": true,
      "site": "00be12ec",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be22d4",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00be22e0",
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be22d4",
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      "00be22e0",
      "DATA",
      [
        "storage",
        "00c939b0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be12d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be12d8) · [`00be12e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be12e0) · [`00be12f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be12f4)
- 新版 [`00be22cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be22c0.md#insn-00be22cc) · [`00be22d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be22c0.md#insn-00be22d4) · [`00be22e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be22c0.md#insn-00be22e8)

~~~diff
- 00be12d8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be22cc ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00be12d8 bytes c90500d0
+ 00be22cc bytes c90500d0
- 00be12e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
- 00be12e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be22d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b00:8"]]
+ 00be22d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be12e0 bytes 299945f9
+ 00be22d4 bytes 298145f9
- 00be12f4 ["INT_ADD", "register:40f0:8", ["const:be12f4:8", "const:4:8"]]
- 00be12f4 ["CALL", null, ["callee:00c5c120:8"]]
+ 00be22e8 ["INT_ADD", "register:40f0:8", ["const:be22e8:8", "const:4:8"]]
+ 00be22e8 ["CALL", null, ["callee:00c5c120:8"]]
- 00be12f4 bytes 97e70194
+ 00be22e8 bytes 8ee70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a869a6c83c2a87bbccd2480621e22c7f"></a>

### [`00be1348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md) → [`00be233c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be233c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df60.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ef30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef30.md) · 呼出先 10件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

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
      "definition_site": "00be23a0",
      "incomplete_value": false,
      "site": "00be23a4",
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
      "definition_site": "00be13ac",
      "incomplete_value": false,
      "site": "00be13b0",
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
      "00be23a0",
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
      "00be23a0",
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

- 旧版 [`00be13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be13b0) · [`00be1374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be1374) · [`00be1380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be1380)
- 新版 [`00be23a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be233c.md#insn-00be23a4) · [`00be2368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be233c.md#insn-00be2368) · [`00be2374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be233c.md#insn-00be2374)

~~~diff
- 00be13b0 ["INT_ADD", "register:40f0:8", ["const:be13b0:8", "const:4:8"]]
- 00be13b0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00be23a4 ["INT_ADD", "register:40f0:8", ["const:be23a4:8", "const:4:8"]]
+ 00be23a4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00be13b0 bytes 48e70194
+ 00be23a4 bytes 3fe70194
- 00be1374 ["INT_ADD", "register:40f0:8", ["const:be1374:8", "const:4:8"]]
- 00be1374 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be2368 ["INT_ADD", "register:40f0:8", ["const:be2368:8", "const:4:8"]]
+ 00be2368 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1374 bytes d7e50194
+ 00be2368 bytes cee50194
- 00be1380 ["INT_ADD", "register:40f0:8", ["const:be1380:8", "const:4:8"]]
- 00be1380 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00be2374 ["INT_ADD", "register:40f0:8", ["const:be2374:8", "const:4:8"]]
+ 00be2374 ["CALL", null, ["callee:00c5bf20:8"]]
- 00be1380 bytes f4e60194
+ 00be2374 bytes ebe60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd67772ddafa0873e398785016c1a445"></a>

### [`00be1524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md) → [`00be2518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2518.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df50.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ef20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef20.md) · 呼出先 10件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be2584",
      "incomplete_value": false,
      "site": "00be2588",
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
      "definition_site": "00be1590",
      "incomplete_value": false,
      "site": "00be1594",
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
      "00be2584",
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
      "00be2584",
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

- 旧版 [`00be1594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1594) · [`00be1558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1558) · [`00be1564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1564)
- 新版 [`00be2588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2518.md#insn-00be2588) · [`00be254c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2518.md#insn-00be254c) · [`00be2558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2518.md#insn-00be2558)

~~~diff
- 00be1594 ["INT_ADD", "register:40f0:8", ["const:be1594:8", "const:4:8"]]
- 00be1594 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00be2588 ["INT_ADD", "register:40f0:8", ["const:be2588:8", "const:4:8"]]
+ 00be2588 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00be1594 bytes cfe60194
+ 00be2588 bytes c6e60194
- 00be1558 ["INT_ADD", "register:40f0:8", ["const:be1558:8", "const:4:8"]]
- 00be1558 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be254c ["INT_ADD", "register:40f0:8", ["const:be254c:8", "const:4:8"]]
+ 00be254c ["CALL", null, ["callee:00c5baa0:8"]]
- 00be1558 bytes 5ee50194
+ 00be254c bytes 55e50194
- 00be1564 ["INT_ADD", "register:40f0:8", ["const:be1564:8", "const:4:8"]]
- 00be1564 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00be2558 ["INT_ADD", "register:40f0:8", ["const:be2558:8", "const:4:8"]]
+ 00be2558 ["CALL", null, ["callee:00c5bf20:8"]]
- 00be1564 bytes 7be60194
+ 00be2558 bytes 72e60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6dd61be06978b0b9432d5e2d22f5eae"></a>

### [`00be21c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md) → [`00be31b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be31b4.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5dc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc40.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00c5ec10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec10.md) [`00c5ec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be31d0",
      "incomplete_value": true,
      "site": "00be31d4",
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
      "definition_site": "00be21dc",
      "incomplete_value": true,
      "site": "00be21e0",
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
      "00be31c8",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00be31d4",
      "DATA",
      [
        "storage",
        "00c92a48",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be31c8",
      "READ",
      [
        "storage",
        "00c9ca68",
        null,
        "pointer"
      ]
    ],
    [
      "00be31d4",
      "DATA",
      [
        "storage",
        "00c93a18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be21cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be21cc) · [`00be21d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be21d4) · [`00be2220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be2220)
- 新版 [`00be31c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be31b4.md#insn-00be31c0) · [`00be31c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be31b4.md#insn-00be31c8) · [`00be3214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be31b4.md#insn-00be3214)

~~~diff
- 00be21cc ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be31c0 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00be21cc bytes c90500b0
+ 00be31c0 bytes c90500b0
- 00be21d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a98:8"]]
- 00be21d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be31c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a68:8"]]
+ 00be31c8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be21d4 bytes 294d45f9
+ 00be31c8 bytes 293545f9
- 00be2220 ["INT_ADD", "register:40f0:8", ["const:be2220:8", "const:4:8"]]
- 00be2220 ["CALL", null, ["callee:00c58f50:8"]]
+ 00be3214 ["INT_ADD", "register:40f0:8", ["const:be3214:8", "const:4:8"]]
+ 00be3214 ["CALL", null, ["callee:00c58f50:8"]]
- 00be2220 bytes 58d70194
+ 00be3214 bytes 4fd70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c58360063f35f8ab9b5158a9a989e14"></a>

### [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) → [`00be4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) FUN_00be4144

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3134.md) [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) · 呼出先 4件 [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) [`00be9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9e64.md) [`00bea124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea124.md) [`00bea24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea24c.md)
- 新版 呼出元 2件 [`00be4128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4128.md) [`00be4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) · 呼出先 4件 [`00be4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) [`00beb118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb118.md) [`00beb240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb240.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be44d0",
      "value": [
        "leaf",
        "ram:beae58:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be34dc",
      "value": [
        "leaf",
        "ram:be9e64:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be44e4",
      "value": [
        "leaf",
        "ram:beae58:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be34f0",
      "value": [
        "leaf",
        "ram:be9e64:8"
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
      "00be44d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ],
    [
      "00be44e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ]
  ],
  "added": [
    [
      "00be44d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae58"
      ]
    ],
    [
      "00be44e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be34dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be34dc) · [`00be34f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be34f0) · [`00be350c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be350c)
- 新版 [`00be44d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md#insn-00be44d0) · [`00be44e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md#insn-00be44e4) · [`00be4500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md#insn-00be4500)

~~~diff
- 00be34dc ["INT_ADD", "register:40f0:8", ["const:be34dc:8", "const:4:8"]]
- 00be34dc ["CALL", null, ["ram:be9e64:8"]]
+ 00be44d0 ["INT_ADD", "register:40f0:8", ["const:be44d0:8", "const:4:8"]]
+ 00be44d0 ["CALL", null, ["ram:beae58:8"]]
- 00be34dc bytes 621a0094
+ 00be44d0 bytes 621a0094
- 00be34f0 ["INT_ADD", "register:40f0:8", ["const:be34f0:8", "const:4:8"]]
- 00be34f0 ["CALL", null, ["ram:be9e64:8"]]
+ 00be44e4 ["INT_ADD", "register:40f0:8", ["const:be44e4:8", "const:4:8"]]
+ 00be44e4 ["CALL", null, ["ram:beae58:8"]]
- 00be34f0 bytes 5d1a0094
+ 00be44e4 bytes 5d1a0094
- 00be350c ["INT_ADD", "register:40f0:8", ["const:be350c:8", "const:4:8"]]
- 00be350c ["CALL", null, ["local:b0:8"]]
+ 00be4500 ["INT_ADD", "register:40f0:8", ["const:be4500:8", "const:4:8"]]
+ 00be4500 ["CALL", null, ["local:b0:8"]]
- 00be350c bytes 11ffff97
+ 00be4500 bytes 11ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e069f515fb6b68b898f4ed8afcffdf"></a>

### [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) → [`00be4fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) FUN_00be4fb0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3f9c.md) [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) · 呼出先 4件 [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) [`00beac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beac1c.md) [`00beaedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beaedc.md) [`00beb004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb004.md)
- 新版 呼出元 2件 [`00be4f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4f90.md) [`00be4fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) · 呼出先 4件 [`00be4fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) [`00bebed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebed0.md) [`00bebff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebff8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be5340",
      "value": [
        "leaf",
        "ram:bebc10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be434c",
      "value": [
        "leaf",
        "ram:beac1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be5354",
      "value": [
        "leaf",
        "ram:bebc10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4360",
      "value": [
        "leaf",
        "ram:beac1c:8"
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
      "00be5340",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ],
    [
      "00be5354",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ]
  ],
  "added": [
    [
      "00be5340",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bebc10"
      ]
    ],
    [
      "00be5354",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bebc10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be434c) · [`00be4360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be4360) · [`00be437c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be437c)
- 新版 [`00be5340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md#insn-00be5340) · [`00be5354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md#insn-00be5354) · [`00be5370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md#insn-00be5370)

~~~diff
- 00be434c ["INT_ADD", "register:40f0:8", ["const:be434c:8", "const:4:8"]]
- 00be434c ["CALL", null, ["ram:beac1c:8"]]
+ 00be5340 ["INT_ADD", "register:40f0:8", ["const:be5340:8", "const:4:8"]]
+ 00be5340 ["CALL", null, ["ram:bebc10:8"]]
- 00be434c bytes 341a0094
+ 00be5340 bytes 341a0094
- 00be4360 ["INT_ADD", "register:40f0:8", ["const:be4360:8", "const:4:8"]]
- 00be4360 ["CALL", null, ["ram:beac1c:8"]]
+ 00be5354 ["INT_ADD", "register:40f0:8", ["const:be5354:8", "const:4:8"]]
+ 00be5354 ["CALL", null, ["ram:bebc10:8"]]
- 00be4360 bytes 2f1a0094
+ 00be5354 bytes 2f1a0094
- 00be437c ["INT_ADD", "register:40f0:8", ["const:be437c:8", "const:4:8"]]
- 00be437c ["CALL", null, ["local:b0:8"]]
+ 00be5370 ["INT_ADD", "register:40f0:8", ["const:be5370:8", "const:4:8"]]
+ 00be5370 ["CALL", null, ["local:b0:8"]]
- 00be437c bytes 10ffff97
+ 00be5370 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee233a8e1a3f179ef7c7c52c646199c9"></a>

### [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) → [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) FUN_00be56ec

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be46d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46d8.md) [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) · 呼出先 4件 [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) [`00beb300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb300.md) [`00beb5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb5c0.md) [`00beb6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb6e8.md)
- 新版 呼出元 2件 [`00be56cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56cc.md) [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · 呼出先 4件 [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) [`00bec5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) [`00bec6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec6dc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be5a7c",
      "value": [
        "leaf",
        "ram:bec2f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a88",
      "value": [
        "leaf",
        "ram:beb300:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be5a90",
      "value": [
        "leaf",
        "ram:bec2f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a9c",
      "value": [
        "leaf",
        "ram:beb300:8"
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
      "00be5a7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ],
    [
      "00be5a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ]
  ],
  "added": [
    [
      "00be5a7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec2f4"
      ]
    ],
    [
      "00be5a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec2f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be4a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4a88) · [`00be4a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4a9c) · [`00be4ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4ab8)
- 新版 [`00be5a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md#insn-00be5a7c) · [`00be5a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md#insn-00be5a90) · [`00be5aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md#insn-00be5aac)

~~~diff
- 00be4a88 ["INT_ADD", "register:40f0:8", ["const:be4a88:8", "const:4:8"]]
- 00be4a88 ["CALL", null, ["ram:beb300:8"]]
+ 00be5a7c ["INT_ADD", "register:40f0:8", ["const:be5a7c:8", "const:4:8"]]
+ 00be5a7c ["CALL", null, ["ram:bec2f4:8"]]
- 00be4a88 bytes 1e1a0094
+ 00be5a7c bytes 1e1a0094
- 00be4a9c ["INT_ADD", "register:40f0:8", ["const:be4a9c:8", "const:4:8"]]
- 00be4a9c ["CALL", null, ["ram:beb300:8"]]
+ 00be5a90 ["INT_ADD", "register:40f0:8", ["const:be5a90:8", "const:4:8"]]
+ 00be5a90 ["CALL", null, ["ram:bec2f4:8"]]
- 00be4a9c bytes 191a0094
+ 00be5a90 bytes 191a0094
- 00be4ab8 ["INT_ADD", "register:40f0:8", ["const:be4ab8:8", "const:4:8"]]
- 00be4ab8 ["CALL", null, ["local:b0:8"]]
+ 00be5aac ["INT_ADD", "register:40f0:8", ["const:be5aac:8", "const:4:8"]]
+ 00be5aac ["CALL", null, ["local:b0:8"]]
- 00be4ab8 bytes 10ffff97
+ 00be5aac bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e500fb8287eb0e29a0c9d3ab56d559f"></a>

### [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) → [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) FUN_00be5e28

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be4e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e14.md) [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) · 呼出先 4件 [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) [`00beb9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb9e4.md) [`00bebc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebc84.md) [`00bebdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebdac.md)
- 新版 呼出元 2件 [`00be5e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e08.md) [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) · 呼出先 4件 [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) [`00becc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becc78.md) [`00becda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becda0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be61b8",
      "value": [
        "leaf",
        "ram:bec9d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be51c4",
      "value": [
        "leaf",
        "ram:beb9e4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be61cc",
      "value": [
        "leaf",
        "ram:bec9d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be51d8",
      "value": [
        "leaf",
        "ram:beb9e4:8"
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
      "00be61b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ],
    [
      "00be61cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ]
  ],
  "added": [
    [
      "00be61b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec9d8"
      ]
    ],
    [
      "00be61cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec9d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be51c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51c4) · [`00be51d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51d8) · [`00be51f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51f4)
- 新版 [`00be61b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md#insn-00be61b8) · [`00be61cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md#insn-00be61cc) · [`00be61e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md#insn-00be61e8)

~~~diff
- 00be51c4 ["INT_ADD", "register:40f0:8", ["const:be51c4:8", "const:4:8"]]
- 00be51c4 ["CALL", null, ["ram:beb9e4:8"]]
+ 00be61b8 ["INT_ADD", "register:40f0:8", ["const:be61b8:8", "const:4:8"]]
+ 00be61b8 ["CALL", null, ["ram:bec9d8:8"]]
- 00be51c4 bytes 081a0094
+ 00be61b8 bytes 081a0094
- 00be51d8 ["INT_ADD", "register:40f0:8", ["const:be51d8:8", "const:4:8"]]
- 00be51d8 ["CALL", null, ["ram:beb9e4:8"]]
+ 00be61cc ["INT_ADD", "register:40f0:8", ["const:be61cc:8", "const:4:8"]]
+ 00be61cc ["CALL", null, ["ram:bec9d8:8"]]
- 00be51d8 bytes 031a0094
+ 00be61cc bytes 031a0094
- 00be51f4 ["INT_ADD", "register:40f0:8", ["const:be51f4:8", "const:4:8"]]
- 00be51f4 ["CALL", null, ["local:b0:8"]]
+ 00be61e8 ["INT_ADD", "register:40f0:8", ["const:be61e8:8", "const:4:8"]]
+ 00be61e8 ["CALL", null, ["local:b0:8"]]
- 00be51f4 bytes 10ffff97
+ 00be61e8 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb458ab6b3aebb7691de38e63591cfdb"></a>

### [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) → [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) FUN_00be88b8

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be78a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78a4.md) [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) · 呼出先 4件 [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) [`00bee27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee27c.md) [`00bee51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee51c.md) [`00bee644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee644.md)
- 新版 呼出元 2件 [`00be8898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8898.md) [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) · 呼出先 4件 [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) [`00bef510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef510.md) [`00bef638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be8c48",
      "value": [
        "leaf",
        "ram:bef270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7c54",
      "value": [
        "leaf",
        "ram:bee27c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be8c5c",
      "value": [
        "leaf",
        "ram:bef270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7c68",
      "value": [
        "leaf",
        "ram:bee27c:8"
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
      "00be8c48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ],
    [
      "00be8c5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ]
  ],
  "added": [
    [
      "00be8c48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef270"
      ]
    ],
    [
      "00be8c5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be7c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c54) · [`00be7c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c68) · [`00be7c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c84)
- 新版 [`00be8c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md#insn-00be8c48) · [`00be8c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md#insn-00be8c5c) · [`00be8c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md#insn-00be8c78)

~~~diff
- 00be7c54 ["INT_ADD", "register:40f0:8", ["const:be7c54:8", "const:4:8"]]
- 00be7c54 ["CALL", null, ["ram:bee27c:8"]]
+ 00be8c48 ["INT_ADD", "register:40f0:8", ["const:be8c48:8", "const:4:8"]]
+ 00be8c48 ["CALL", null, ["ram:bef270:8"]]
- 00be7c54 bytes 8a190094
+ 00be8c48 bytes 8a190094
- 00be7c68 ["INT_ADD", "register:40f0:8", ["const:be7c68:8", "const:4:8"]]
- 00be7c68 ["CALL", null, ["ram:bee27c:8"]]
+ 00be8c5c ["INT_ADD", "register:40f0:8", ["const:be8c5c:8", "const:4:8"]]
+ 00be8c5c ["CALL", null, ["ram:bef270:8"]]
- 00be7c68 bytes 85190094
+ 00be8c5c bytes 85190094
- 00be7c84 ["INT_ADD", "register:40f0:8", ["const:be7c84:8", "const:4:8"]]
- 00be7c84 ["CALL", null, ["local:b0:8"]]
+ 00be8c78 ["INT_ADD", "register:40f0:8", ["const:be8c78:8", "const:4:8"]]
+ 00be8c78 ["CALL", null, ["local:b0:8"]]
- 00be7c84 bytes 10ffff97
+ 00be8c78 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed80e6e6744af2dadc85ceb96eaf897b"></a>

### [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) → [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) FUN_00be8fd0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be7fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fbc.md) [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) · 呼出先 4件 [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) [`00bee91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee91c.md) [`00beebbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beebbc.md) [`00beece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beece4.md)
- 新版 呼出元 2件 [`00be8fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fb0.md) [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · 呼出先 4件 [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) [`00befbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befbb0.md) [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be9360",
      "value": [
        "leaf",
        "ram:bef910:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be836c",
      "value": [
        "leaf",
        "ram:bee91c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be9374",
      "value": [
        "leaf",
        "ram:bef910:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be8380",
      "value": [
        "leaf",
        "ram:bee91c:8"
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
      "00be9360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee91c"
      ]
    ],
    [
      "00be9374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee91c"
      ]
    ]
  ],
  "added": [
    [
      "00be9360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef910"
      ]
    ],
    [
      "00be9374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef910"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be836c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be836c) · [`00be8380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be8380) · [`00be839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be839c)
- 新版 [`00be9360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md#insn-00be9360) · [`00be9374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md#insn-00be9374) · [`00be9390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md#insn-00be9390)

~~~diff
- 00be836c ["INT_ADD", "register:40f0:8", ["const:be836c:8", "const:4:8"]]
- 00be836c ["CALL", null, ["ram:bee91c:8"]]
+ 00be9360 ["INT_ADD", "register:40f0:8", ["const:be9360:8", "const:4:8"]]
+ 00be9360 ["CALL", null, ["ram:bef910:8"]]
- 00be836c bytes 6c190094
+ 00be9360 bytes 6c190094
- 00be8380 ["INT_ADD", "register:40f0:8", ["const:be8380:8", "const:4:8"]]
- 00be8380 ["CALL", null, ["ram:bee91c:8"]]
+ 00be9374 ["INT_ADD", "register:40f0:8", ["const:be9374:8", "const:4:8"]]
+ 00be9374 ["CALL", null, ["ram:bef910:8"]]
- 00be8380 bytes 67190094
+ 00be9374 bytes 67190094
- 00be839c ["INT_ADD", "register:40f0:8", ["const:be839c:8", "const:4:8"]]
- 00be839c ["CALL", null, ["local:b0:8"]]
+ 00be9390 ["INT_ADD", "register:40f0:8", ["const:be9390:8", "const:4:8"]]
+ 00be9390 ["CALL", null, ["local:b0:8"]]
- 00be839c bytes 10ffff97
+ 00be9390 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8826eb78b21bcfd14d477105e3c09b2"></a>

### [`00bef9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md) → [`00bf09e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf09e4.md) _ZNSt6__ndk16chrono12system_clock3nowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)
- 新版 呼出元 1件 [`00c59620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59620.md) · 呼出先 3件 [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5a7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a7a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0a50",
      "incomplete_value": false,
      "site": "00bf0a54",
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
            "const:aec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00befa5c",
      "incomplete_value": false,
      "site": "00befa60",
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
            "const:a0e:8"
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
      "00bf0a50",
      "PARAM",
      [
        "storage",
        "002b4a0e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf0a50",
      "PARAM",
      [
        "storage",
        "002b4aec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00befa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa60) · [`00befa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa08) · [`00befa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa50)
- 新版 [`00bf0a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf09e4.md#insn-00bf0a54) · [`00bf09fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf09e4.md#insn-00bf09fc) · [`00bf0a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf09e4.md#insn-00bf0a44)

~~~diff
- 00befa60 ["INT_ADD", "register:40f0:8", ["const:befa60:8", "const:4:8"]]
- 00befa60 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bf0a54 ["INT_ADD", "register:40f0:8", ["const:bf0a54:8", "const:4:8"]]
+ 00bf0a54 ["CALL", null, ["callee:00c591c0:8"]]
- 00befa60 bytes e4a10194
+ 00bf0a54 bytes dba10194
- 00befa08 ["INT_ADD", "register:40f0:8", ["const:befa08:8", "const:4:8"]]
- 00befa08 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bf09fc ["INT_ADD", "register:40f0:8", ["const:bf09fc:8", "const:4:8"]]
+ 00bf09fc ["CALL", null, ["callee:00c5a7a0:8"]]
- 00befa08 bytes 72a70194
+ 00bf09fc bytes 69a70194
- 00befa50 ["INT_ADD", "register:40f0:8", ["const:befa50:8", "const:4:8"]]
- 00befa50 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf0a44 ["INT_ADD", "register:40f0:8", ["const:bf0a44:8", "const:4:8"]]
+ 00bf0a44 ["CALL", null, ["callee:00c59160:8"]]
- 00befa50 bytes d0a10194
+ 00bf0a44 bytes c7a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f84bc13e870928a66d909437b869ffc"></a>

### [`00befaa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md) → [`00bf0a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0a98.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f90.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)
- 新版 呼出元 1件 [`00c58f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f60.md) · 呼出先 3件 [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5a7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a7a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0ae4",
      "incomplete_value": false,
      "site": "00bf0ae8",
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
            "const:20e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00befaf0",
      "incomplete_value": false,
      "site": "00befaf4",
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
            "const:143:8"
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
      "00bf0ae4",
      "PARAM",
      [
        "storage",
        "002a5143",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf0ae4",
      "PARAM",
      [
        "storage",
        "002a520e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00befaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befaf4) · [`00befabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befabc) · [`00befae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befae4)
- 新版 [`00bf0ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0a98.md#insn-00bf0ae8) · [`00bf0ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0a98.md#insn-00bf0ab0) · [`00bf0ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0a98.md#insn-00bf0ad8)

~~~diff
- 00befaf4 ["INT_ADD", "register:40f0:8", ["const:befaf4:8", "const:4:8"]]
- 00befaf4 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bf0ae8 ["INT_ADD", "register:40f0:8", ["const:bf0ae8:8", "const:4:8"]]
+ 00bf0ae8 ["CALL", null, ["callee:00c591c0:8"]]
- 00befaf4 bytes bfa10194
+ 00bf0ae8 bytes b6a10194
- 00befabc ["INT_ADD", "register:40f0:8", ["const:befabc:8", "const:4:8"]]
- 00befabc ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bf0ab0 ["INT_ADD", "register:40f0:8", ["const:bf0ab0:8", "const:4:8"]]
+ 00bf0ab0 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00befabc bytes 45a70194
+ 00bf0ab0 bytes 3ca70194
- 00befae4 ["INT_ADD", "register:40f0:8", ["const:befae4:8", "const:4:8"]]
- 00befae4 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf0ad8 ["INT_ADD", "register:40f0:8", ["const:bf0ad8:8", "const:4:8"]]
+ 00bf0ad8 ["CALL", null, ["callee:00c59160:8"]]
- 00befae4 bytes aba10194
+ 00bf0ad8 bytes a2a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c590e6a652c0aed0ee04744fa3868a6"></a>

### [`00befba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md) → [`00bf0b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b9c.md) _ZNSt16nested_exceptionC2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf0bb8",
      "incomplete_value": true,
      "site": "00bf0bbc",
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
      "definition_site": "00befbc4",
      "incomplete_value": true,
      "site": "00befbc8",
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
      "00bf0bb4",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0bbc",
      "DATA",
      [
        "storage",
        "00c92aa8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00bf0bb4",
      "READ",
      [
        "storage",
        "00c9cb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0bbc",
      "DATA",
      [
        "storage",
        "00c93a78",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00befbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md#insn-00befbb8) · [`00befbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md#insn-00befbc0) · [`00befbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md#insn-00befbcc)
- 新版 [`00bf0bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b9c.md#insn-00bf0bac) · [`00bf0bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b9c.md#insn-00bf0bb4) · [`00bf0bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b9c.md#insn-00bf0bc0)

~~~diff
- 00befbb8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bf0bac ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00befbb8 bytes 68050090
+ 00bf0bac bytes 68050090
- 00befbc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b40:8"]]
- 00befbc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf0bb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00bf0bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00befbc0 bytes 08a145f9
+ 00bf0bb4 bytes 088945f9
- 00befbcc ["INT_ADD", "register:40f0:8", ["const:befbcc:8", "const:4:8"]]
- 00befbcc ["CALL", null, ["callee:00c5efe0:8"]]
+ 00bf0bc0 ["INT_ADD", "register:40f0:8", ["const:bf0bc0:8", "const:4:8"]]
+ 00bf0bc0 ["CALL", null, ["callee:00c5efe0:8"]]
- 00befbcc bytes 11b90194
+ 00bf0bc0 bytes 08b90194
~~~


<a id="compare-8e9474813f9d78025519784d0930db59"></a>

### [`00befcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md) → [`00bf0cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0cb8.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md) · 呼出先 1件 [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md)
- 新版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8c0.md) · 呼出先 1件 [`00bf13d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf13d0",
      "incomplete_value": false,
      "site": "00bf13d4",
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
            "const:31a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf03dc",
      "incomplete_value": false,
      "site": "00bf03e0",
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
            "const:23c:8"
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
      "00bf0ce8",
      "READ",
      [
        "storage",
        "00310368",
        null,
        "undefined4"
      ]
    ],
    [
      "00bf0ce8",
      "READ",
      [
        "storage",
        "00310338",
        null,
        "undefined4"
      ]
    ],
    [
      "00bf0cfc",
      "READ",
      [
        "storage",
        "00310308",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bf0ce8",
      "READ",
      [
        "storage",
        "003103a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00bf0ce8",
      "READ",
      [
        "storage",
        "00310378",
        null,
        "undefined4"
      ]
    ],
    [
      "00bf0cfc",
      "READ",
      [
        "storage",
        "00310348",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf03e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00bf03e0) · [`00befcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00befcdc) · [`00befd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00befd48)
- 新版 [`00bf13d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0cb8.md#insn-00bf13d4) · [`00bf0cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0cb8.md#insn-00bf0cd0) · [`00bf0d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0cb8.md#insn-00bf0d3c)

~~~diff
- 00bf03e0 ["INT_ADD", "register:40f0:8", ["const:bf03e0:8", "const:4:8"]]
- 00bf03e0 ["CALL", null, ["callee:00bf13d8:8"]]
+ 00bf13d4 ["INT_ADD", "register:40f0:8", ["const:bf13d4:8", "const:4:8"]]
+ 00bf13d4 ["CALL", null, ["callee:00bf13d8:8"]]
- 00bf03e0 bytes 01000094
+ 00bf13d4 bytes 01000094
- 00befcdc ["COPY", "tmp:0:8", ["const:308:8"]]
- 00befcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00befcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00befcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bf0cd0 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00bf0cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf0cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf0cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00befcdc bytes 08210c91
+ 00bf0cd0 bytes 08210d91
- 00befd48 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 00befd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00befd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00befd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bf0d3c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00bf0d3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bf0d3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bf0d3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00befd48 bytes 29210f91
+ 00bf0d3c bytes 29211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d80de73d387811b441bf63abea7d7d2"></a>

### [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md) → [`00bf13d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md) FUN_00bf13d8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00befcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md) · 呼出先 4件 [`00bf0438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0438.md) [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00bf0cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0cb8.md) · 呼出先 4件 [`00bf142c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf142c.md) [`00c38dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf140c",
      "incomplete_value": true,
      "site": "00bf1414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0418",
      "incomplete_value": true,
      "site": "00bf0420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
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
      "definition_site": "00bf1410",
      "incomplete_value": true,
      "site": "00bf1414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf041c",
      "incomplete_value": true,
      "site": "00bf0420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b50:8"
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
      "00bf140c",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00bf140c",
      "PARAM",
      [
        "storage",
        "00c96980",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf1410",
      "READ",
      [
        "storage",
        "00c9bb50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf140c",
      "READ",
      [
        "storage",
        "00c9cb18",
        null,
        "pointer"
      ]
    ],
    [
      "00bf140c",
      "PARAM",
      [
        "storage",
        "00c97950",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf1410",
      "READ",
      [
        "storage",
        "00c9cb20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf0420) · [`00bf03fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf03fc) · [`00bf0408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf0408)
- 新版 [`00bf1414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md#insn-00bf1414) · [`00bf13f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md#insn-00bf13f0) · [`00bf13fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md#insn-00bf13fc)

~~~diff
- 00bf0420 ["INT_ADD", "register:40f0:8", ["const:bf0420:8", "const:4:8"]]
- 00bf0420 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00bf1414 ["INT_ADD", "register:40f0:8", ["const:bf1414:8", "const:4:8"]]
+ 00bf1414 ["CALL", null, ["callee:00c58fb0:8"]]
- 00bf0420 bytes f09e0194
+ 00bf1414 bytes e79e0194
- 00bf03fc ["INT_ADD", "register:40f0:8", ["const:bf03fc:8", "const:4:8"]]
- 00bf03fc ["CALL", null, ["callee:00c58f90:8"]]
+ 00bf13f0 ["INT_ADD", "register:40f0:8", ["const:bf13f0:8", "const:4:8"]]
+ 00bf13f0 ["CALL", null, ["callee:00c58f90:8"]]
- 00bf03fc bytes f19e0194
+ 00bf13f0 bytes e89e0194
- 00bf0408 ["INT_ADD", "register:40f0:8", ["const:bf0408:8", "const:4:8"]]
- 00bf0408 ["CALL", null, ["callee:00bf142c:8"]]
+ 00bf13fc ["INT_ADD", "register:40f0:8", ["const:bf13fc:8", "const:4:8"]]
+ 00bf13fc ["CALL", null, ["callee:00bf142c:8"]]
- 00bf0408 bytes 0c000094
+ 00bf13fc bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caf9d708975a9f7a04851b6b1d3cc1e8"></a>

### [`00bf04a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04a4.md) → [`00bf1498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1498.md) _ZNKSt6__ndk112bad_weak_ptr4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf14a0",
      "incomplete_value": false,
      "site": "00bf14a4",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf04ac",
      "incomplete_value": false,
      "site": "00bf04b0",
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
            "const:b7:8"
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
      "00bf14a0",
      "DATA",
      [
        "storage",
        "002bb0b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf14a0",
      "DATA",
      [
        "storage",
        "002bb195",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf04ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04a4.md#insn-00bf04ac)
- 新版 [`00bf14a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1498.md#insn-00bf14a0)

~~~diff
- 00bf04ac ["COPY", "tmp:0:8", ["const:b7:8"]]
- 00bf04ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf04ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf04ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf14a0 ["COPY", "tmp:0:8", ["const:195:8"]]
+ 00bf14a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf14a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf14a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf04ac bytes 00dc0291
+ 00bf14a0 bytes 00540691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0573b64f65a0ff727e50e17c44a0207"></a>

### [`00bf07b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md) → [`00bf17a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17a8.md) _ZSt17__throw_bad_allocv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md) · 呼出先 4件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md)
- 新版 呼出元 1件 [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md) · 呼出先 4件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf17d4",
      "incomplete_value": true,
      "site": "00bf17dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf07e0",
      "incomplete_value": true,
      "site": "00bf07e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:eb8:8"
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
      "definition_site": "00bf17d8",
      "incomplete_value": true,
      "site": "00bf17dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf07e4",
      "incomplete_value": true,
      "site": "00bf07e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:ec0:8"
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
      "00bf17d4",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf17d4",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf17d8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf17d4",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00bf17d4",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf17d8",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07e8) · [`00bf07c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07c8) · [`00bf07d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07d0)
- 新版 [`00bf17dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17a8.md#insn-00bf17dc) · [`00bf17bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17a8.md#insn-00bf17bc) · [`00bf17c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17a8.md#insn-00bf17c4)

~~~diff
- 00bf07e8 ["INT_ADD", "register:40f0:8", ["const:bf07e8:8", "const:4:8"]]
- 00bf07e8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00bf17dc ["INT_ADD", "register:40f0:8", ["const:bf17dc:8", "const:4:8"]]
+ 00bf17dc ["CALL", null, ["callee:00c58fb0:8"]]
- 00bf07e8 bytes fe9d0194
+ 00bf17dc bytes f59d0194
- 00bf07c8 ["INT_ADD", "register:40f0:8", ["const:bf07c8:8", "const:4:8"]]
- 00bf07c8 ["CALL", null, ["callee:00c58f90:8"]]
+ 00bf17bc ["INT_ADD", "register:40f0:8", ["const:bf17bc:8", "const:4:8"]]
+ 00bf17bc ["CALL", null, ["callee:00c58f90:8"]]
- 00bf07c8 bytes fe9d0194
+ 00bf17bc bytes f59d0194
- 00bf07d0 ["INT_ADD", "register:40f0:8", ["const:bf07d0:8", "const:4:8"]]
- 00bf07d0 ["CALL", null, ["callee:00c59ae0:8"]]
+ 00bf17c4 ["INT_ADD", "register:40f0:8", ["const:bf17c4:8", "const:4:8"]]
+ 00bf17c4 ["CALL", null, ["callee:00c59ae0:8"]]
- 00bf07d0 bytes d0a00194
+ 00bf17c4 bytes c7a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c5621b84e1589cea4264814c9db1512"></a>

### [`00bf07ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md) → [`00bf17e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17e0.md) _ZNSt11logic_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e060.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5f030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f030.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf1800",
      "incomplete_value": true,
      "site": "00bf1804",
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
      "definition_site": "00bf080c",
      "incomplete_value": true,
      "site": "00bf0810",
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
      "00bf17fc",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1804",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf17fc",
      "READ",
      [
        "storage",
        "00c9cb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1804",
      "DATA",
      [
        "storage",
        "00c97778",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0800) · [`00bf0808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0808) · [`00bf0828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0828)
- 新版 [`00bf17f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17e0.md#insn-00bf17f4) · [`00bf17fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17e0.md#insn-00bf17fc) · [`00bf181c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf17e0.md#insn-00bf181c)

~~~diff
- 00bf0800 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bf17f4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bf0800 bytes 480500f0
+ 00bf17f4 bytes 480500f0
- 00bf0808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00bf0808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf17fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00bf17fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf0808 bytes 08b145f9
+ 00bf17fc bytes 089945f9
- 00bf0828 ["INT_ADD", "register:40f0:8", ["const:bf0828:8", "const:4:8"]]
- 00bf0828 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf181c ["INT_ADD", "register:40f0:8", ["const:bf181c:8", "const:4:8"]]
+ 00bf181c ["CALL", null, ["callee:00c59080:8"]]
- 00bf0828 bytes 229e0194
+ 00bf181c bytes 199e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d71d294595bb2da0e21e59499a72f9e9"></a>

### [`00bf0880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md) → [`00bf1874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1874.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58000.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c58fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fd0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf1898",
      "incomplete_value": true,
      "site": "00bf189c",
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
      "definition_site": "00bf08a4",
      "incomplete_value": true,
      "site": "00bf08a8",
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
      "00bf1894",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00bf189c",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf1894",
      "READ",
      [
        "storage",
        "00c9cb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bf189c",
      "DATA",
      [
        "storage",
        "00c97778",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf0894) · [`00bf08a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf08a0) · [`00bf08b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf08b0)
- 新版 [`00bf1888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1874.md#insn-00bf1888) · [`00bf1894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1874.md#insn-00bf1894) · [`00bf18a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1874.md#insn-00bf18a4)

~~~diff
- 00bf0894 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bf1888 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bf0894 bytes 480500f0
+ 00bf1888 bytes 480500f0
- 00bf08a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00bf08a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf1894 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00bf1894 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf08a0 bytes 08b145f9
+ 00bf1894 bytes 089945f9
- 00bf08b0 ["INT_ADD", "register:40f0:8", ["const:bf08b0:8", "const:4:8"]]
- 00bf08b0 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf18a4 ["INT_ADD", "register:40f0:8", ["const:bf18a4:8", "const:4:8"]]
+ 00bf18a4 ["CALL", null, ["callee:00c59080:8"]]
- 00bf08b0 bytes 009e0194
+ 00bf18a4 bytes f79d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef369ec26696a14df824cef166817227"></a>

### [`00bf099c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md) → [`00bf1990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1990.md) _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e070.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f040.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf19b0",
      "incomplete_value": true,
      "site": "00bf19b4",
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
      "definition_site": "00bf09bc",
      "incomplete_value": true,
      "site": "00bf09c0",
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
      "00bf19ac",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bf19b4",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf19ac",
      "READ",
      [
        "storage",
        "00c9cb38",
        null,
        "pointer"
      ]
    ],
    [
      "00bf19b4",
      "DATA",
      [
        "storage",
        "00c977a0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf09b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09b0) · [`00bf09b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09b8) · [`00bf09d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09d8)
- 新版 [`00bf19a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1990.md#insn-00bf19a4) · [`00bf19ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1990.md#insn-00bf19ac) · [`00bf19cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1990.md#insn-00bf19cc)

~~~diff
- 00bf09b0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bf19a4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bf09b0 bytes 480500f0
+ 00bf19a4 bytes 480500f0
- 00bf09b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00bf09b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf19ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00bf19ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf09b8 bytes 08b545f9
+ 00bf19ac bytes 089d45f9
- 00bf09d8 ["INT_ADD", "register:40f0:8", ["const:bf09d8:8", "const:4:8"]]
- 00bf09d8 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf19cc ["INT_ADD", "register:40f0:8", ["const:bf19cc:8", "const:4:8"]]
+ 00bf19cc ["CALL", null, ["callee:00c59080:8"]]
- 00bf09d8 bytes b69d0194
+ 00bf19cc bytes ad9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ba431b99875729e3b2a24dd8a525e5"></a>

### [`00bf0a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md) → [`00bf1a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1a24.md) _ZNSt13runtime_errorC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9a0.md) [`00c5e090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e090.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00c5b970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b970.md) [`00c5f060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f060.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf1a48",
      "incomplete_value": true,
      "site": "00bf1a4c",
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
      "definition_site": "00bf0a54",
      "incomplete_value": true,
      "site": "00bf0a58",
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
      "00bf1a44",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1a4c",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf1a44",
      "READ",
      [
        "storage",
        "00c9cb38",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1a4c",
      "DATA",
      [
        "storage",
        "00c977a0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a44) · [`00bf0a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a50) · [`00bf0a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a60)
- 新版 [`00bf1a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1a24.md#insn-00bf1a38) · [`00bf1a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1a24.md#insn-00bf1a44) · [`00bf1a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1a24.md#insn-00bf1a54)

~~~diff
- 00bf0a44 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bf1a38 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bf0a44 bytes 480500f0
+ 00bf1a38 bytes 480500f0
- 00bf0a50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00bf0a50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf1a44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00bf1a44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf0a50 bytes 08b545f9
+ 00bf1a44 bytes 089d45f9
- 00bf0a60 ["INT_ADD", "register:40f0:8", ["const:bf0a60:8", "const:4:8"]]
- 00bf0a60 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf1a54 ["INT_ADD", "register:40f0:8", ["const:bf1a54:8", "const:4:8"]]
+ 00bf1a54 ["CALL", null, ["callee:00c59080:8"]]
- 00bf0a60 bytes 949d0194
+ 00bf1a54 bytes 8b9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3b8b23c2b3a42d9547ccb18fc1d0ed6"></a>

### [`00bf0b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md) → [`00bf1b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b40.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md) · 呼出先 4件 [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e090.md)
- 新版 呼出元 1件 [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md) · 呼出先 4件 [`00c38dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5f060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf1b74",
      "incomplete_value": true,
      "site": "00bf1b7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0b80",
      "incomplete_value": true,
      "site": "00bf0b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b70:8"
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
      "definition_site": "00bf1b78",
      "incomplete_value": true,
      "site": "00bf1b7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0b84",
      "incomplete_value": true,
      "site": "00bf0b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
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
      "00bf1b74",
      "READ",
      [
        "storage",
        "00c9bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1b74",
      "PARAM",
      [
        "storage",
        "00c96928",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf1b78",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf1b74",
      "READ",
      [
        "storage",
        "00c9cb40",
        null,
        "pointer"
      ]
    ],
    [
      "00bf1b74",
      "PARAM",
      [
        "storage",
        "00c978f8",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf1b78",
      "READ",
      [
        "storage",
        "00c9cb48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b88) · [`00bf0b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b64) · [`00bf0b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b70)
- 新版 [`00bf1b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b40.md#insn-00bf1b7c) · [`00bf1b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b40.md#insn-00bf1b58) · [`00bf1b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b40.md#insn-00bf1b64)

~~~diff
- 00bf0b88 ["INT_ADD", "register:40f0:8", ["const:bf0b88:8", "const:4:8"]]
- 00bf0b88 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00bf1b7c ["INT_ADD", "register:40f0:8", ["const:bf1b7c:8", "const:4:8"]]
+ 00bf1b7c ["CALL", null, ["callee:00c58fb0:8"]]
- 00bf0b88 bytes 169d0194
+ 00bf1b7c bytes 0d9d0194
- 00bf0b64 ["INT_ADD", "register:40f0:8", ["const:bf0b64:8", "const:4:8"]]
- 00bf0b64 ["CALL", null, ["callee:00c58f90:8"]]
+ 00bf1b58 ["INT_ADD", "register:40f0:8", ["const:bf1b58:8", "const:4:8"]]
+ 00bf1b58 ["CALL", null, ["callee:00c58f90:8"]]
- 00bf0b64 bytes 179d0194
+ 00bf1b58 bytes 0e9d0194
- 00bf0b70 ["INT_ADD", "register:40f0:8", ["const:bf0b70:8", "const:4:8"]]
- 00bf0b70 ["CALL", null, ["callee:00c5f060:8"]]
+ 00bf1b64 ["INT_ADD", "register:40f0:8", ["const:bf1b64:8", "const:4:8"]]
+ 00bf1b64 ["CALL", null, ["callee:00c5f060:8"]]
- 00bf0b70 bytes 48b50194
+ 00bf1b64 bytes 3fb50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261c310402c7efd34e1535bb52966e01"></a>

### [`00bf2140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md) → [`00bf3134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3134.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf31dc",
      "incomplete_value": false,
      "site": "00bf31e0",
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
            "const:78f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf21e8",
      "incomplete_value": false,
      "site": "00bf21ec",
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
            "const:6b8:8"
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
      "00bf31dc",
      "PARAM",
      [
        "storage",
        "002af6b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf31dc",
      "PARAM",
      [
        "storage",
        "002af78f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf21ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21ec) · [`00bf21b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21b8) · [`00bf21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21e8)
- 新版 [`00bf31e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3134.md#insn-00bf31e0) · [`00bf31ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3134.md#insn-00bf31ac) · [`00bf31dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3134.md#insn-00bf31dc)

~~~diff
- 00bf21ec ["INT_ADD", "register:40f0:8", ["const:bf21ec:8", "const:4:8"]]
- 00bf21ec ["CALL", null, ["callee:00442c90:8"]]
+ 00bf31e0 ["INT_ADD", "register:40f0:8", ["const:bf31e0:8", "const:4:8"]]
+ 00bf31e0 ["CALL", null, ["callee:00442c90:8"]]
- 00bf21ec bytes e141e197
+ 00bf31e0 bytes ac3ee197
- 00bf21b8 ["INT_ADD", "register:40f0:8", ["const:bf21b8:8", "const:4:8"]]
- 00bf21b8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bf31ac ["INT_ADD", "register:40f0:8", ["const:bf31ac:8", "const:4:8"]]
+ 00bf31ac ["CALL", null, ["callee:00c590f0:8"]]
- 00bf21b8 bytes da970194
+ 00bf31ac bytes d1970194
- 00bf21e8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00bf21e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf21e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf21e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf31dc ["COPY", "tmp:0:8", ["const:78f:8"]]
+ 00bf31dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf31dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf31dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf21e8 bytes 00e01a91
+ 00bf31dc bytes 003c1e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422df6cc2b76c807db40496ef505617a"></a>

### [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) → [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) FUN_00bf3968

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`00bf279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md) [`00bf2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md) [`00bf30b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf30b8.md) [`00bf3100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md) [`00bf32ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 17件 [`00bf3790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3790.md) [`00bf3e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3e6c.md) [`00bf40ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40ac.md) [`00bf40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40f4.md) [`00bf42a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf42a0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf3978",
      "incomplete_value": false,
      "site": "00bf397c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf2984",
      "incomplete_value": false,
      "site": "00bf2988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:ecf:8"
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
      "00bf3978",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf3978",
      "PARAM",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md#insn-00bf2988) · [`00bf2984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md#insn-00bf2984)
- 新版 [`00bf397c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md#insn-00bf397c) · [`00bf3978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md#insn-00bf3978)

~~~diff
- 00bf2988 ["INT_ADD", "register:40f0:8", ["const:bf2988:8", "const:4:8"]]
- 00bf2988 ["CALL", null, ["callee:00442c90:8"]]
+ 00bf397c ["INT_ADD", "register:40f0:8", ["const:bf397c:8", "const:4:8"]]
+ 00bf397c ["CALL", null, ["callee:00442c90:8"]]
- 00bf2988 bytes fa3fe197
+ 00bf397c bytes c53ce197
- 00bf2984 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00bf2984 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf2984 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf2984 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf3978 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00bf3978 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf3978 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf3978 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf2984 bytes 003c3b91
+ 00bf3978 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b05074f473301b8710cf871f80803f45"></a>

### [`00bf45ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md) → [`00bf55a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf55a0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00c5f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5650",
      "incomplete_value": false,
      "site": "00bf5654",
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
            "const:78f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf465c",
      "incomplete_value": false,
      "site": "00bf4660",
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
            "const:6b8:8"
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
      "00bf5650",
      "PARAM",
      [
        "storage",
        "002af6b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5650",
      "PARAM",
      [
        "storage",
        "002af78f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf4660) · [`00bf4630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf4630) · [`00bf465c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf465c)
- 新版 [`00bf5654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf55a0.md#insn-00bf5654) · [`00bf5624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf55a0.md#insn-00bf5624) · [`00bf5650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf55a0.md#insn-00bf5650)

~~~diff
- 00bf4660 ["INT_ADD", "register:40f0:8", ["const:bf4660:8", "const:4:8"]]
- 00bf4660 ["CALL", null, ["callee:00442c90:8"]]
+ 00bf5654 ["INT_ADD", "register:40f0:8", ["const:bf5654:8", "const:4:8"]]
+ 00bf5654 ["CALL", null, ["callee:00442c90:8"]]
- 00bf4660 bytes c438e197
+ 00bf5654 bytes 8f35e197
- 00bf4630 ["INT_ADD", "register:40f0:8", ["const:bf4630:8", "const:4:8"]]
- 00bf4630 ["CALL", null, ["callee:00c5f0e0:8"]]
+ 00bf5624 ["INT_ADD", "register:40f0:8", ["const:bf5624:8", "const:4:8"]]
+ 00bf5624 ["CALL", null, ["callee:00c5f0e0:8"]]
- 00bf4630 bytes b8a60194
+ 00bf5624 bytes afa60194
- 00bf465c ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00bf465c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf465c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf465c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf5650 ["COPY", "tmp:0:8", ["const:78f:8"]]
+ 00bf5650 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5650 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5650 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf465c bytes 00e01a91
+ 00bf5650 bytes 003c1e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7615f7fd50fea074c315d7ebb85ff1c2"></a>

### [`00bf4c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md) → [`00bf5c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c00.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b160.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00c5c130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c130.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5c10",
      "incomplete_value": false,
      "site": "00bf5c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c1c",
      "incomplete_value": false,
      "site": "00bf4c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:ecf:8"
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
      "00bf5c10",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5c10",
      "PARAM",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md#insn-00bf4c20) · [`00bf4c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md#insn-00bf4c1c)
- 新版 [`00bf5c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c00.md#insn-00bf5c14) · [`00bf5c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c00.md#insn-00bf5c10)

~~~diff
- 00bf4c20 ["INT_ADD", "register:40f0:8", ["const:bf4c20:8", "const:4:8"]]
- 00bf4c20 ["CALL", null, ["callee:0043bad8:8"]]
+ 00bf5c14 ["INT_ADD", "register:40f0:8", ["const:bf5c14:8", "const:4:8"]]
+ 00bf5c14 ["CALL", null, ["callee:0043bad8:8"]]
- 00bf4c20 bytes e61ae197
+ 00bf5c14 bytes b117e197
- 00bf4c1c ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00bf4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c10 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00bf5c10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4c1c bytes 003c3b91
+ 00bf5c10 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9084804563a034e70ec85b48189d3486"></a>

### [`00bf4c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md) → [`00bf5c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c18.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d520.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`00c5e4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4f0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5c28",
      "incomplete_value": false,
      "site": "00bf5c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c34",
      "incomplete_value": false,
      "site": "00bf4c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:ecf:8"
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
      "00bf5c28",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5c28",
      "PARAM",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md#insn-00bf4c38) · [`00bf4c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md#insn-00bf4c34)
- 新版 [`00bf5c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c18.md#insn-00bf5c2c) · [`00bf5c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c18.md#insn-00bf5c28)

~~~diff
- 00bf4c38 ["INT_ADD", "register:40f0:8", ["const:bf4c38:8", "const:4:8"]]
- 00bf4c38 ["CALL", null, ["callee:00442c90:8"]]
+ 00bf5c2c ["INT_ADD", "register:40f0:8", ["const:bf5c2c:8", "const:4:8"]]
+ 00bf5c2c ["CALL", null, ["callee:00442c90:8"]]
- 00bf4c38 bytes 4e37e197
+ 00bf5c2c bytes 1934e197
- 00bf4c34 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00bf4c34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4c34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4c34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c28 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00bf5c28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf5c28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4c34 bytes 003c3b91
+ 00bf5c28 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782d12b83f5a5373a08cfeae46f807f3"></a>

### [`00bf4c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md) → [`00bf5c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c30.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58660.md)
- 新版 呼出元 1件 [`00c59100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59100.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`004821e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/004821e0.md) [`00bf920c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59630.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5d50",
      "incomplete_value": true,
      "site": "00bf5d50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4d5c",
      "incomplete_value": true,
      "site": "00bf4d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5d58",
      "incomplete_value": true,
      "site": "00bf5d58",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4d64",
      "incomplete_value": true,
      "site": "00bf4d64",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5cfc",
      "incomplete_value": false,
      "site": "00bf5d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4d08",
      "incomplete_value": false,
      "site": "00bf4d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:d72:8"
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
      "00bf5cfc",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5d40",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5d44",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5cfc",
      "PARAM",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf5d40",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf5d44",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4d18) · [`00bf4c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4c8c) · [`00bf4ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4ca8)
- 新版 [`00bf5d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c30.md#insn-00bf5d0c) · [`00bf5c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c30.md#insn-00bf5c80) · [`00bf5c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c30.md#insn-00bf5c9c)

~~~diff
- 00bf4d18 ["INT_ADD", "register:40f0:8", ["const:bf4d18:8", "const:4:8"]]
- 00bf4d18 ["CALL", null, ["callee:004821e0:8"]]
+ 00bf5d0c ["INT_ADD", "register:40f0:8", ["const:bf5d0c:8", "const:4:8"]]
+ 00bf5d0c ["CALL", null, ["callee:004821e0:8"]]
- 00bf4d18 bytes 6a34e297
+ 00bf5d0c bytes 3531e297
- 00bf4c8c ["INT_ADD", "register:40f0:8", ["const:bf4c8c:8", "const:4:8"]]
- 00bf4c8c ["CALL", null, ["callee:00c59160:8"]]
+ 00bf5c80 ["INT_ADD", "register:40f0:8", ["const:bf5c80:8", "const:4:8"]]
+ 00bf5c80 ["CALL", null, ["callee:00c59160:8"]]
- 00bf4c8c bytes 418d0194
+ 00bf5c80 bytes 388d0194
- 00bf4ca8 ["INT_ADD", "register:40f0:8", ["const:bf4ca8:8", "const:4:8"]]
- 00bf4ca8 ["CALL", null, ["callee:00c59630:8"]]
+ 00bf5c9c ["INT_ADD", "register:40f0:8", ["const:bf5c9c:8", "const:4:8"]]
+ 00bf5c9c ["CALL", null, ["callee:00c59630:8"]]
- 00bf4ca8 bytes 6e8e0194
+ 00bf5c9c bytes 658e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e13eb1d70a60689b5770e5e017dfe6f"></a>

### [`00bf4d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md) → [`00bf5d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5d8c.md) _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`004821e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/004821e0.md) [`00bf920c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5e50",
      "incomplete_value": false,
      "site": "00bf5e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4e5c",
      "incomplete_value": false,
      "site": "00bf4e6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:d72:8"
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
      "00bf5e50",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5e50",
      "PARAM",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4e6c) · [`00bf4de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4de8) · [`00bf4e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4e04)
- 新版 [`00bf5e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5d8c.md#insn-00bf5e60) · [`00bf5ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5d8c.md#insn-00bf5ddc) · [`00bf5df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5d8c.md#insn-00bf5df8)

~~~diff
- 00bf4e6c ["INT_ADD", "register:40f0:8", ["const:bf4e6c:8", "const:4:8"]]
- 00bf4e6c ["CALL", null, ["callee:004821e0:8"]]
+ 00bf5e60 ["INT_ADD", "register:40f0:8", ["const:bf5e60:8", "const:4:8"]]
+ 00bf5e60 ["CALL", null, ["callee:004821e0:8"]]
- 00bf4e6c bytes 1534e297
+ 00bf5e60 bytes e030e297
- 00bf4de8 ["INT_ADD", "register:40f0:8", ["const:bf4de8:8", "const:4:8"]]
- 00bf4de8 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf5ddc ["INT_ADD", "register:40f0:8", ["const:bf5ddc:8", "const:4:8"]]
+ 00bf5ddc ["CALL", null, ["callee:00c59160:8"]]
- 00bf4de8 bytes ea8c0194
+ 00bf5ddc bytes e18c0194
- 00bf4e04 ["INT_ADD", "register:40f0:8", ["const:bf4e04:8", "const:4:8"]]
- 00bf4e04 ["CALL", null, ["callee:00c59630:8"]]
+ 00bf5df8 ["INT_ADD", "register:40f0:8", ["const:bf5df8:8", "const:4:8"]]
+ 00bf5df8 ["CALL", null, ["callee:00c59630:8"]]
- 00bf4e04 bytes 178e0194
+ 00bf5df8 bytes 0e8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efaba4d5a0bc0dbcdcaca8b4dd9c61ec"></a>

### [`00bf4eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md) → [`00bf5ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5ea4.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ac0.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a90.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5fa0",
      "incomplete_value": true,
      "site": "00bf5fa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4fac",
      "incomplete_value": true,
      "site": "00bf4fac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5fa4",
      "incomplete_value": true,
      "site": "00bf5fa4",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4fb0",
      "incomplete_value": true,
      "site": "00bf4fb0",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5fe0",
      "incomplete_value": true,
      "site": "00bf5fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4fec",
      "incomplete_value": true,
      "site": "00bf4fec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5f88",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5f8c",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5fc8",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5f88",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf5f8c",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf5fc8",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f0c) · [`00bf4f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f28) · [`00bf4f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f58)
- 新版 [`00bf5f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5ea4.md#insn-00bf5f00) · [`00bf5f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5ea4.md#insn-00bf5f1c) · [`00bf5f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5ea4.md#insn-00bf5f4c)

~~~diff
- 00bf4f0c ["INT_ADD", "register:40f0:8", ["const:bf4f0c:8", "const:4:8"]]
- 00bf4f0c ["CALL", null, ["callee:00c59160:8"]]
+ 00bf5f00 ["INT_ADD", "register:40f0:8", ["const:bf5f00:8", "const:4:8"]]
+ 00bf5f00 ["CALL", null, ["callee:00c59160:8"]]
- 00bf4f0c bytes a18c0194
+ 00bf5f00 bytes 988c0194
- 00bf4f28 ["INT_ADD", "register:40f0:8", ["const:bf4f28:8", "const:4:8"]]
- 00bf4f28 ["CALL", null, ["callee:00c5f100:8"]]
+ 00bf5f1c ["INT_ADD", "register:40f0:8", ["const:bf5f1c:8", "const:4:8"]]
+ 00bf5f1c ["CALL", null, ["callee:00c5f100:8"]]
- 00bf4f28 bytes 82a40194
+ 00bf5f1c bytes 79a40194
- 00bf4f58 ["INT_ADD", "register:40f0:8", ["const:bf4f58:8", "const:4:8"]]
- 00bf4f58 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf5f4c ["INT_ADD", "register:40f0:8", ["const:bf5f4c:8", "const:4:8"]]
+ 00bf5f4c ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf4f58 bytes 72a40194
+ 00bf5f4c bytes 69a40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c636f3c6d4d19aa84d74e2cde912b8be"></a>

### [`00bf501c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md) → [`00bf6010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6010.md) _ZNSt6__ndk15stollERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58300.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58670.md)
- 新版 呼出元 1件 [`00c592d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592d0.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59640.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf610c",
      "incomplete_value": true,
      "site": "00bf610c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5118",
      "incomplete_value": true,
      "site": "00bf5118",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6110",
      "incomplete_value": true,
      "site": "00bf6110",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf511c",
      "incomplete_value": true,
      "site": "00bf511c",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf614c",
      "incomplete_value": true,
      "site": "00bf614c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5158",
      "incomplete_value": true,
      "site": "00bf5158",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf60f4",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf60f8",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6134",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf60f4",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf60f8",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6134",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf5078) · [`00bf5094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf5094) · [`00bf50c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf50c4)
- 新版 [`00bf606c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6010.md#insn-00bf606c) · [`00bf6088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6010.md#insn-00bf6088) · [`00bf60b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6010.md#insn-00bf60b8)

~~~diff
- 00bf5078 ["INT_ADD", "register:40f0:8", ["const:bf5078:8", "const:4:8"]]
- 00bf5078 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf606c ["INT_ADD", "register:40f0:8", ["const:bf606c:8", "const:4:8"]]
+ 00bf606c ["CALL", null, ["callee:00c59160:8"]]
- 00bf5078 bytes 468c0194
+ 00bf606c bytes 3d8c0194
- 00bf5094 ["INT_ADD", "register:40f0:8", ["const:bf5094:8", "const:4:8"]]
- 00bf5094 ["CALL", null, ["callee:00c59640:8"]]
+ 00bf6088 ["INT_ADD", "register:40f0:8", ["const:bf6088:8", "const:4:8"]]
+ 00bf6088 ["CALL", null, ["callee:00c59640:8"]]
- 00bf5094 bytes 778d0194
+ 00bf6088 bytes 6e8d0194
- 00bf50c4 ["INT_ADD", "register:40f0:8", ["const:bf50c4:8", "const:4:8"]]
- 00bf50c4 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf60b8 ["INT_ADD", "register:40f0:8", ["const:bf60b8:8", "const:4:8"]]
+ 00bf60b8 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf50c4 bytes 17a40194
+ 00bf60b8 bytes 0ea40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148a76757a3c9f930096d55cfee26740"></a>

### [`00bf5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md) → [`00bf617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf617c.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58310.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 1件 [`00c592e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592e0.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf627c",
      "incomplete_value": true,
      "site": "00bf627c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5288",
      "incomplete_value": true,
      "site": "00bf5288",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6280",
      "incomplete_value": true,
      "site": "00bf6280",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf528c",
      "incomplete_value": true,
      "site": "00bf528c",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf62bc",
      "incomplete_value": true,
      "site": "00bf62bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf52c8",
      "incomplete_value": true,
      "site": "00bf52c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6264",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6268",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf62a4",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6264",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6268",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf62a4",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf51e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf51e8) · [`00bf5204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf5204) · [`00bf5234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf5234)
- 新版 [`00bf61dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf617c.md#insn-00bf61dc) · [`00bf61f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf617c.md#insn-00bf61f8) · [`00bf6228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf617c.md#insn-00bf6228)

~~~diff
- 00bf51e8 ["INT_ADD", "register:40f0:8", ["const:bf51e8:8", "const:4:8"]]
- 00bf51e8 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf61dc ["INT_ADD", "register:40f0:8", ["const:bf61dc:8", "const:4:8"]]
+ 00bf61dc ["CALL", null, ["callee:00c59160:8"]]
- 00bf51e8 bytes ea8b0194
+ 00bf61dc bytes e18b0194
- 00bf5204 ["INT_ADD", "register:40f0:8", ["const:bf5204:8", "const:4:8"]]
- 00bf5204 ["CALL", null, ["callee:00c5f110:8"]]
+ 00bf61f8 ["INT_ADD", "register:40f0:8", ["const:bf61f8:8", "const:4:8"]]
+ 00bf61f8 ["CALL", null, ["callee:00c5f110:8"]]
- 00bf5204 bytes cfa30194
+ 00bf61f8 bytes c6a30194
- 00bf5234 ["INT_ADD", "register:40f0:8", ["const:bf5234:8", "const:4:8"]]
- 00bf5234 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6228 ["INT_ADD", "register:40f0:8", ["const:bf6228:8", "const:4:8"]]
+ 00bf6228 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5234 bytes bba30194
+ 00bf6228 bytes b2a30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f31501aebfda06028d40e19ce783de6a"></a>

### [`00bf52f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md) → [`00bf62ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf62ec.md) _ZNSt6__ndk14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586b0.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c59680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59680.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59650.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf63c8",
      "incomplete_value": true,
      "site": "00bf63c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf53d4",
      "incomplete_value": true,
      "site": "00bf53d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf63d0",
      "incomplete_value": true,
      "site": "00bf63d0",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf53dc",
      "incomplete_value": true,
      "site": "00bf53dc",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6400",
      "incomplete_value": true,
      "site": "00bf6400",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf540c",
      "incomplete_value": true,
      "site": "00bf540c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf63b8",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf63bc",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf63f0",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf63b8",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf63bc",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf63f0",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf5344) · [`00bf535c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf535c) · [`00bf538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf538c)
- 新版 [`00bf6338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf62ec.md#insn-00bf6338) · [`00bf6350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf62ec.md#insn-00bf6350) · [`00bf6380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf62ec.md#insn-00bf6380)

~~~diff
- 00bf5344 ["INT_ADD", "register:40f0:8", ["const:bf5344:8", "const:4:8"]]
- 00bf5344 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6338 ["INT_ADD", "register:40f0:8", ["const:bf6338:8", "const:4:8"]]
+ 00bf6338 ["CALL", null, ["callee:00c59160:8"]]
- 00bf5344 bytes 938b0194
+ 00bf6338 bytes 8a8b0194
- 00bf535c ["INT_ADD", "register:40f0:8", ["const:bf535c:8", "const:4:8"]]
- 00bf535c ["CALL", null, ["callee:00c59650:8"]]
+ 00bf6350 ["INT_ADD", "register:40f0:8", ["const:bf6350:8", "const:4:8"]]
+ 00bf6350 ["CALL", null, ["callee:00c59650:8"]]
- 00bf535c bytes c98c0194
+ 00bf6350 bytes c08c0194
- 00bf538c ["INT_ADD", "register:40f0:8", ["const:bf538c:8", "const:4:8"]]
- 00bf538c ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6380 ["INT_ADD", "register:40f0:8", ["const:bf6380:8", "const:4:8"]]
+ 00bf6380 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf538c bytes 65a30194
+ 00bf6380 bytes 5ca30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d0592b50fb488f58cef642585669dcc"></a>

### [`00bf5440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md) → [`00bf6434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6434.md) _ZNSt6__ndk14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58320.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00c592f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592f0.md) · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59660.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6510",
      "incomplete_value": true,
      "site": "00bf6510",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf551c",
      "incomplete_value": true,
      "site": "00bf551c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6518",
      "incomplete_value": true,
      "site": "00bf6518",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5524",
      "incomplete_value": true,
      "site": "00bf5524",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6548",
      "incomplete_value": true,
      "site": "00bf6548",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5554",
      "incomplete_value": true,
      "site": "00bf5554",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6500",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6504",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6538",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6500",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6504",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6538",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf548c) · [`00bf54a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf54a4) · [`00bf54d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf54d4)
- 新版 [`00bf6480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6434.md#insn-00bf6480) · [`00bf6498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6434.md#insn-00bf6498) · [`00bf64c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6434.md#insn-00bf64c8)

~~~diff
- 00bf548c ["INT_ADD", "register:40f0:8", ["const:bf548c:8", "const:4:8"]]
- 00bf548c ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6480 ["INT_ADD", "register:40f0:8", ["const:bf6480:8", "const:4:8"]]
+ 00bf6480 ["CALL", null, ["callee:00c59160:8"]]
- 00bf548c bytes 418b0194
+ 00bf6480 bytes 388b0194
- 00bf54a4 ["INT_ADD", "register:40f0:8", ["const:bf54a4:8", "const:4:8"]]
- 00bf54a4 ["CALL", null, ["callee:00c59660:8"]]
+ 00bf6498 ["INT_ADD", "register:40f0:8", ["const:bf6498:8", "const:4:8"]]
+ 00bf6498 ["CALL", null, ["callee:00c59660:8"]]
- 00bf54a4 bytes 7b8c0194
+ 00bf6498 bytes 728c0194
- 00bf54d4 ["INT_ADD", "register:40f0:8", ["const:bf54d4:8", "const:4:8"]]
- 00bf54d4 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf64c8 ["INT_ADD", "register:40f0:8", ["const:bf64c8:8", "const:4:8"]]
+ 00bf64c8 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf54d4 bytes 13a30194
+ 00bf64c8 bytes 0aa30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45eb2dcc91a550783a6a60b5f5cb675b"></a>

### [`00bf5588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md) → [`00bf657c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf657c.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6670",
      "incomplete_value": true,
      "site": "00bf6670",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf567c",
      "incomplete_value": true,
      "site": "00bf567c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6674",
      "incomplete_value": true,
      "site": "00bf6674",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5680",
      "incomplete_value": true,
      "site": "00bf5680",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf66b0",
      "incomplete_value": true,
      "site": "00bf66b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf56bc",
      "incomplete_value": true,
      "site": "00bf56bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6658",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf665c",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6698",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6658",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf665c",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6698",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf55e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf55e0) · [`00bf55f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf55f8) · [`00bf5628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf5628)
- 新版 [`00bf65d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf657c.md#insn-00bf65d4) · [`00bf65ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf657c.md#insn-00bf65ec) · [`00bf661c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf657c.md#insn-00bf661c)

~~~diff
- 00bf55e0 ["INT_ADD", "register:40f0:8", ["const:bf55e0:8", "const:4:8"]]
- 00bf55e0 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf65d4 ["INT_ADD", "register:40f0:8", ["const:bf65d4:8", "const:4:8"]]
+ 00bf65d4 ["CALL", null, ["callee:00c59160:8"]]
- 00bf55e0 bytes ec8a0194
+ 00bf65d4 bytes e38a0194
- 00bf55f8 ["INT_ADD", "register:40f0:8", ["const:bf55f8:8", "const:4:8"]]
- 00bf55f8 ["CALL", null, ["callee:00c5f120:8"]]
+ 00bf65ec ["INT_ADD", "register:40f0:8", ["const:bf65ec:8", "const:4:8"]]
+ 00bf65ec ["CALL", null, ["callee:00c5f120:8"]]
- 00bf55f8 bytes d6a20194
+ 00bf65ec bytes cda20194
- 00bf5628 ["INT_ADD", "register:40f0:8", ["const:bf5628:8", "const:4:8"]]
- 00bf5628 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf661c ["INT_ADD", "register:40f0:8", ["const:bf661c:8", "const:4:8"]]
+ 00bf661c ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5628 bytes bea20194
+ 00bf661c bytes b5a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9e85fd812e5d66c3e25460fb9c6b630"></a>

### [`00bf56ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md) → [`00bf66e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf66e0.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`004821e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/004821e0.md) [`00bf920c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.41% / 新版 92.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6808",
      "incomplete_value": true,
      "site": "00bf6808",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5814",
      "incomplete_value": true,
      "site": "00bf5814",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6810",
      "incomplete_value": true,
      "site": "00bf6810",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf581c",
      "incomplete_value": true,
      "site": "00bf581c",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf67b4",
      "incomplete_value": false,
      "site": "00bf67c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf57c0",
      "incomplete_value": false,
      "site": "00bf57d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:d72:8"
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
      "00bf67b4",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf67f8",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf67fc",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf67b4",
      "PARAM",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf67f8",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf67fc",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf57d0) · [`00bf5740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf5740) · [`00bf575c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf575c)
- 新版 [`00bf67c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf66e0.md#insn-00bf67c4) · [`00bf6734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf66e0.md#insn-00bf6734) · [`00bf6750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf66e0.md#insn-00bf6750)

~~~diff
- 00bf57d0 ["INT_ADD", "register:40f0:8", ["const:bf57d0:8", "const:4:8"]]
- 00bf57d0 ["CALL", null, ["callee:004821e0:8"]]
+ 00bf67c4 ["INT_ADD", "register:40f0:8", ["const:bf67c4:8", "const:4:8"]]
+ 00bf67c4 ["CALL", null, ["callee:004821e0:8"]]
- 00bf57d0 bytes bc31e297
+ 00bf67c4 bytes 872ee297
- 00bf5740 ["INT_ADD", "register:40f0:8", ["const:bf5740:8", "const:4:8"]]
- 00bf5740 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6734 ["INT_ADD", "register:40f0:8", ["const:bf6734:8", "const:4:8"]]
+ 00bf6734 ["CALL", null, ["callee:00c59160:8"]]
- 00bf5740 bytes 948a0194
+ 00bf6734 bytes 8b8a0194
- 00bf575c ["INT_ADD", "register:40f0:8", ["const:bf575c:8", "const:4:8"]]
- 00bf575c ["CALL", null, ["callee:00c5f130:8"]]
+ 00bf6750 ["INT_ADD", "register:40f0:8", ["const:bf6750:8", "const:4:8"]]
+ 00bf6750 ["CALL", null, ["callee:00c5f130:8"]]
- 00bf575c bytes 81a20194
+ 00bf6750 bytes 78a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed80426c28643fe67d291db79061a44"></a>

### [`00bf5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md) → [`00bf6844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6844.md) _ZNSt6__ndk14stolERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`004821e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/004821e0.md) [`00bf920c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf6910",
      "incomplete_value": false,
      "site": "00bf6920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf591c",
      "incomplete_value": false,
      "site": "00bf592c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:d72:8"
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
      "00bf6910",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6910",
      "PARAM",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf592c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf592c) · [`00bf58a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf58a4) · [`00bf58c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf58c0)
- 新版 [`00bf6920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6844.md#insn-00bf6920) · [`00bf6898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6844.md#insn-00bf6898) · [`00bf68b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6844.md#insn-00bf68b4)

~~~diff
- 00bf592c ["INT_ADD", "register:40f0:8", ["const:bf592c:8", "const:4:8"]]
- 00bf592c ["CALL", null, ["callee:004821e0:8"]]
+ 00bf6920 ["INT_ADD", "register:40f0:8", ["const:bf6920:8", "const:4:8"]]
+ 00bf6920 ["CALL", null, ["callee:004821e0:8"]]
- 00bf592c bytes 6531e297
+ 00bf6920 bytes 302ee297
- 00bf58a4 ["INT_ADD", "register:40f0:8", ["const:bf58a4:8", "const:4:8"]]
- 00bf58a4 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6898 ["INT_ADD", "register:40f0:8", ["const:bf6898:8", "const:4:8"]]
+ 00bf6898 ["CALL", null, ["callee:00c59160:8"]]
- 00bf58a4 bytes 3b8a0194
+ 00bf6898 bytes 328a0194
- 00bf58c0 ["INT_ADD", "register:40f0:8", ["const:bf58c0:8", "const:4:8"]]
- 00bf58c0 ["CALL", null, ["callee:00c5f130:8"]]
+ 00bf68b4 ["INT_ADD", "register:40f0:8", ["const:bf68b4:8", "const:4:8"]]
+ 00bf68b4 ["CALL", null, ["callee:00c5f130:8"]]
- 00bf58c0 bytes 28a20194
+ 00bf68b4 bytes 1fa20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9901dc629c46cc6e71b907b1e8f3787"></a>

### [`00bf5970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md) → [`00bf6964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6964.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6a68",
      "incomplete_value": true,
      "site": "00bf6a68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a74",
      "incomplete_value": true,
      "site": "00bf5a74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6a6c",
      "incomplete_value": true,
      "site": "00bf6a6c",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a78",
      "incomplete_value": true,
      "site": "00bf5a78",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6aa8",
      "incomplete_value": true,
      "site": "00bf6aa8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5ab4",
      "incomplete_value": true,
      "site": "00bf5ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6a50",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6a58",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6a90",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6a50",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6a58",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6a90",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf59c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf59c8) · [`00bf59e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf59e4) · [`00bf5a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf5a20)
- 新版 [`00bf69bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6964.md#insn-00bf69bc) · [`00bf69d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6964.md#insn-00bf69d8) · [`00bf6a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6964.md#insn-00bf6a14)

~~~diff
- 00bf59c8 ["INT_ADD", "register:40f0:8", ["const:bf59c8:8", "const:4:8"]]
- 00bf59c8 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf69bc ["INT_ADD", "register:40f0:8", ["const:bf69bc:8", "const:4:8"]]
+ 00bf69bc ["CALL", null, ["callee:00c59160:8"]]
- 00bf59c8 bytes f2890194
+ 00bf69bc bytes e9890194
- 00bf59e4 ["INT_ADD", "register:40f0:8", ["const:bf59e4:8", "const:4:8"]]
- 00bf59e4 ["CALL", null, ["callee:00c5f140:8"]]
+ 00bf69d8 ["INT_ADD", "register:40f0:8", ["const:bf69d8:8", "const:4:8"]]
+ 00bf69d8 ["CALL", null, ["callee:00c5f140:8"]]
- 00bf59e4 bytes e3a10194
+ 00bf69d8 bytes daa10194
- 00bf5a20 ["INT_ADD", "register:40f0:8", ["const:bf5a20:8", "const:4:8"]]
- 00bf5a20 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6a14 ["INT_ADD", "register:40f0:8", ["const:bf6a14:8", "const:4:8"]]
+ 00bf6a14 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5a20 bytes c0a10194
+ 00bf6a14 bytes b7a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2008ba44a305fab2761b08ba374dd3b"></a>

### [`00bf5aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md) → [`00bf6ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ae0.md) _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6be4",
      "incomplete_value": true,
      "site": "00bf6be4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5bf0",
      "incomplete_value": true,
      "site": "00bf5bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6be8",
      "incomplete_value": true,
      "site": "00bf6be8",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5bf4",
      "incomplete_value": true,
      "site": "00bf5bf4",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6c24",
      "incomplete_value": true,
      "site": "00bf6c24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5c30",
      "incomplete_value": true,
      "site": "00bf5c30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6bcc",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6bd4",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6c0c",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6bcc",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6bd4",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6c0c",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b44) · [`00bf5b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b60) · [`00bf5b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b9c)
- 新版 [`00bf6b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ae0.md#insn-00bf6b38) · [`00bf6b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ae0.md#insn-00bf6b54) · [`00bf6b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ae0.md#insn-00bf6b90)

~~~diff
- 00bf5b44 ["INT_ADD", "register:40f0:8", ["const:bf5b44:8", "const:4:8"]]
- 00bf5b44 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6b38 ["INT_ADD", "register:40f0:8", ["const:bf6b38:8", "const:4:8"]]
+ 00bf6b38 ["CALL", null, ["callee:00c59160:8"]]
- 00bf5b44 bytes 93890194
+ 00bf6b38 bytes 8a890194
- 00bf5b60 ["INT_ADD", "register:40f0:8", ["const:bf5b60:8", "const:4:8"]]
- 00bf5b60 ["CALL", null, ["callee:00c5f150:8"]]
+ 00bf6b54 ["INT_ADD", "register:40f0:8", ["const:bf6b54:8", "const:4:8"]]
+ 00bf6b54 ["CALL", null, ["callee:00c5f150:8"]]
- 00bf5b60 bytes 88a10194
+ 00bf6b54 bytes 7fa10194
- 00bf5b9c ["INT_ADD", "register:40f0:8", ["const:bf5b9c:8", "const:4:8"]]
- 00bf5b9c ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6b90 ["INT_ADD", "register:40f0:8", ["const:bf6b90:8", "const:4:8"]]
+ 00bf6b90 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5b9c bytes 61a10194
+ 00bf6b90 bytes 58a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9b62ddacdec77cfcb4f3250329b695"></a>

### [`00bf5c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md) → [`00bf6c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6c5c.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6d64",
      "incomplete_value": true,
      "site": "00bf6d64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5d70",
      "incomplete_value": true,
      "site": "00bf5d70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6d68",
      "incomplete_value": true,
      "site": "00bf6d68",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5d74",
      "incomplete_value": true,
      "site": "00bf5d74",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6da4",
      "incomplete_value": true,
      "site": "00bf6da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5db0",
      "incomplete_value": true,
      "site": "00bf5db0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6d4c",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6d54",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6d8c",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6d4c",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6d54",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6d8c",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5cc4) · [`00bf5ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5ce0) · [`00bf5d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5d1c)
- 新版 [`00bf6cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6c5c.md#insn-00bf6cb8) · [`00bf6cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6c5c.md#insn-00bf6cd4) · [`00bf6d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6c5c.md#insn-00bf6d10)

~~~diff
- 00bf5cc4 ["INT_ADD", "register:40f0:8", ["const:bf5cc4:8", "const:4:8"]]
- 00bf5cc4 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6cb8 ["INT_ADD", "register:40f0:8", ["const:bf6cb8:8", "const:4:8"]]
+ 00bf6cb8 ["CALL", null, ["callee:00c59160:8"]]
- 00bf5cc4 bytes 33890194
+ 00bf6cb8 bytes 2a890194
- 00bf5ce0 ["INT_ADD", "register:40f0:8", ["const:bf5ce0:8", "const:4:8"]]
- 00bf5ce0 ["CALL", null, ["callee:00c5f160:8"]]
+ 00bf6cd4 ["INT_ADD", "register:40f0:8", ["const:bf6cd4:8", "const:4:8"]]
+ 00bf6cd4 ["CALL", null, ["callee:00c5f160:8"]]
- 00bf5ce0 bytes 2ca10194
+ 00bf6cd4 bytes 23a10194
- 00bf5d1c ["INT_ADD", "register:40f0:8", ["const:bf5d1c:8", "const:4:8"]]
- 00bf5d1c ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6d10 ["INT_ADD", "register:40f0:8", ["const:bf6d10:8", "const:4:8"]]
+ 00bf6d10 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5d1c bytes 01a10194
+ 00bf6d10 bytes f8a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9df35b9843d01e30d6e1d67c64b92d89"></a>

### [`00bf5de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md) → [`00bf6ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ddc.md) _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6ec0",
      "incomplete_value": true,
      "site": "00bf6ec0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5ecc",
      "incomplete_value": true,
      "site": "00bf5ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6ec8",
      "incomplete_value": true,
      "site": "00bf6ec8",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5ed4",
      "incomplete_value": true,
      "site": "00bf5ed4",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6ef8",
      "incomplete_value": true,
      "site": "00bf6ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5f04",
      "incomplete_value": true,
      "site": "00bf5f04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6eb0",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6eb4",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf6ee8",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6eb0",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf6eb4",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf6ee8",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e38) · [`00bf5e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e50) · [`00bf5e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e84)
- 新版 [`00bf6e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ddc.md#insn-00bf6e2c) · [`00bf6e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ddc.md#insn-00bf6e44) · [`00bf6e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ddc.md#insn-00bf6e78)

~~~diff
- 00bf5e38 ["INT_ADD", "register:40f0:8", ["const:bf5e38:8", "const:4:8"]]
- 00bf5e38 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6e2c ["INT_ADD", "register:40f0:8", ["const:bf6e2c:8", "const:4:8"]]
+ 00bf6e2c ["CALL", null, ["callee:00c59160:8"]]
- 00bf5e38 bytes d6880194
+ 00bf6e2c bytes cd880194
- 00bf5e50 ["INT_ADD", "register:40f0:8", ["const:bf5e50:8", "const:4:8"]]
- 00bf5e50 ["CALL", null, ["callee:00c5f170:8"]]
+ 00bf6e44 ["INT_ADD", "register:40f0:8", ["const:bf6e44:8", "const:4:8"]]
+ 00bf6e44 ["CALL", null, ["callee:00c5f170:8"]]
- 00bf5e50 bytes d4a00194
+ 00bf6e44 bytes cba00194
- 00bf5e84 ["INT_ADD", "register:40f0:8", ["const:bf5e84:8", "const:4:8"]]
- 00bf5e84 ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6e78 ["INT_ADD", "register:40f0:8", ["const:bf6e78:8", "const:4:8"]]
+ 00bf6e78 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5e84 bytes a7a00194
+ 00bf6e78 bytes 9ea00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62ed58bbf357a767716cc560253edadd"></a>

### [`00bf5f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md) → [`00bf6f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6f34.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7018",
      "incomplete_value": true,
      "site": "00bf7018",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf6024",
      "incomplete_value": true,
      "site": "00bf6024",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7020",
      "incomplete_value": true,
      "site": "00bf7020",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf602c",
      "incomplete_value": true,
      "site": "00bf602c",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7050",
      "incomplete_value": true,
      "site": "00bf7050",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf605c",
      "incomplete_value": true,
      "site": "00bf605c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf7008",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf700c",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf7040",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf7008",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf700c",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf7040",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5f90) · [`00bf5fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5fa8) · [`00bf5fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5fdc)
- 新版 [`00bf6f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6f34.md#insn-00bf6f84) · [`00bf6f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6f34.md#insn-00bf6f9c) · [`00bf6fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6f34.md#insn-00bf6fd0)

~~~diff
- 00bf5f90 ["INT_ADD", "register:40f0:8", ["const:bf5f90:8", "const:4:8"]]
- 00bf5f90 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf6f84 ["INT_ADD", "register:40f0:8", ["const:bf6f84:8", "const:4:8"]]
+ 00bf6f84 ["CALL", null, ["callee:00c59160:8"]]
- 00bf5f90 bytes 80880194
+ 00bf6f84 bytes 77880194
- 00bf5fa8 ["INT_ADD", "register:40f0:8", ["const:bf5fa8:8", "const:4:8"]]
- 00bf5fa8 ["CALL", null, ["callee:00c5f180:8"]]
+ 00bf6f9c ["INT_ADD", "register:40f0:8", ["const:bf6f9c:8", "const:4:8"]]
+ 00bf6f9c ["CALL", null, ["callee:00c5f180:8"]]
- 00bf5fa8 bytes 82a00194
+ 00bf6f9c bytes 79a00194
- 00bf5fdc ["INT_ADD", "register:40f0:8", ["const:bf5fdc:8", "const:4:8"]]
- 00bf5fdc ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf6fd0 ["INT_ADD", "register:40f0:8", ["const:bf6fd0:8", "const:4:8"]]
+ 00bf6fd0 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf5fdc bytes 51a00194
+ 00bf6fd0 bytes 48a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3013ad21d289fdb5219706dd75773905"></a>

### [`00bf6098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md) → [`00bf708c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf708c.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7180",
      "incomplete_value": true,
      "site": "00bf7180",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf618c",
      "incomplete_value": true,
      "site": "00bf618c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7184",
      "incomplete_value": true,
      "site": "00bf7184",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf6190",
      "incomplete_value": true,
      "site": "00bf6190",
      "value": [
        "LOAD",
        "8",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf71c0",
      "incomplete_value": true,
      "site": "00bf71c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf61cc",
      "incomplete_value": true,
      "site": "00bf61cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf7168",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf7170",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf71a8",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf7168",
      "READ",
      [
        "storage",
        "002b9e50",
        null,
        "string"
      ]
    ],
    [
      "00bf7170",
      "READ",
      [
        "storage",
        "002b9e56",
        null,
        "string"
      ]
    ],
    [
      "00bf71a8",
      "READ",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf60e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf60e8) · [`00bf6100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf6100) · [`00bf613c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf613c)
- 新版 [`00bf70dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf708c.md#insn-00bf70dc) · [`00bf70f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf708c.md#insn-00bf70f4) · [`00bf7130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf7/00bf708c.md#insn-00bf7130)

~~~diff
- 00bf60e8 ["INT_ADD", "register:40f0:8", ["const:bf60e8:8", "const:4:8"]]
- 00bf60e8 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf70dc ["INT_ADD", "register:40f0:8", ["const:bf70dc:8", "const:4:8"]]
+ 00bf70dc ["CALL", null, ["callee:00c59160:8"]]
- 00bf60e8 bytes 2a880194
+ 00bf70dc bytes 21880194
- 00bf6100 ["INT_ADD", "register:40f0:8", ["const:bf6100:8", "const:4:8"]]
- 00bf6100 ["CALL", null, ["callee:00c5f190:8"]]
+ 00bf70f4 ["INT_ADD", "register:40f0:8", ["const:bf70f4:8", "const:4:8"]]
+ 00bf70f4 ["CALL", null, ["callee:00c5f190:8"]]
- 00bf6100 bytes 30a00194
+ 00bf70f4 bytes 27a00194
- 00bf613c ["INT_ADD", "register:40f0:8", ["const:bf613c:8", "const:4:8"]]
- 00bf613c ["CALL", null, ["callee:00c5f0f0:8"]]
+ 00bf7130 ["INT_ADD", "register:40f0:8", ["const:bf7130:8", "const:4:8"]]
+ 00bf7130 ["CALL", null, ["callee:00c5f0f0:8"]]
- 00bf613c bytes f99f0194
+ 00bf7130 bytes f09f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c703d54aa9c0c7f1be9e6c9f97d965a"></a>

### [`00bf7e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md) → [`00bf8e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8e44.md) _ZNSt6__ndk110to_wstringEf

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b930.md) [`00c5f1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1b0.md) [`00c5f1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8e80",
      "incomplete_value": true,
      "site": "00bf8e88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7e8c",
      "incomplete_value": true,
      "site": "00bf7e94",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf8e80",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf8ee8",
      "PARAM",
      [
        "storage",
        "00310534",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8e80",
      "READ",
      [
        "storage",
        "002c3310",
        null,
        null
      ]
    ],
    [
      "00bf8ee8",
      "PARAM",
      [
        "storage",
        "00310574",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7e7c) · [`00bf7e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7e8c) · [`00bf7eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7eb4)
- 新版 [`00bf8e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8e44.md#insn-00bf8e70) · [`00bf8e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8e44.md#insn-00bf8e80) · [`00bf8ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8e44.md#insn-00bf8ea8)

~~~diff
- 00bf7e7c ["INT_ADD", "register:40f0:8", ["const:bf7e7c:8", "const:4:8"]]
- 00bf7e7c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf8e70 ["INT_ADD", "register:40f0:8", ["const:bf8e70:8", "const:4:8"]]
+ 00bf8e70 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf7e7c bytes 39800194
+ 00bf8e70 bytes 30800194
- 00bf7e8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 00bf7e8c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7e8c ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7e8c ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf8e80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 00bf8e80 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf8e80 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf8e80 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7e8c bytes 01b1c03d
+ 00bf8e80 bytes 01c5c03d
- 00bf7eb4 ["INT_ADD", "register:40f0:8", ["const:bf7eb4:8", "const:4:8"]]
- 00bf7eb4 ["CALL", null, ["callee:00c5b930:8"]]
+ 00bf8ea8 ["INT_ADD", "register:40f0:8", ["const:bf8ea8:8", "const:4:8"]]
+ 00bf8ea8 ["CALL", null, ["callee:00c5b930:8"]]
- 00bf7eb4 bytes ab8a0194
+ 00bf8ea8 bytes a28a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9aac91cfeefe7fe5bd7be34d3f2977a"></a>

### [`00bf7f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md) → [`00bf8f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8f8c.md) _ZNSt6__ndk110to_wstringEd

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b930.md) [`00c5f1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1b0.md) [`00c5f1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8fc8",
      "incomplete_value": true,
      "site": "00bf8fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7fd4",
      "incomplete_value": true,
      "site": "00bf7fdc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf8fc8",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf902c",
      "PARAM",
      [
        "storage",
        "00310534",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8fc8",
      "READ",
      [
        "storage",
        "002c3310",
        null,
        null
      ]
    ],
    [
      "00bf902c",
      "PARAM",
      [
        "storage",
        "00310574",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7fc4) · [`00bf7fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7fd4) · [`00bf7ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7ffc)
- 新版 [`00bf8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8f8c.md#insn-00bf8fb8) · [`00bf8fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8f8c.md#insn-00bf8fc8) · [`00bf8ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf8/00bf8f8c.md#insn-00bf8ff0)

~~~diff
- 00bf7fc4 ["INT_ADD", "register:40f0:8", ["const:bf7fc4:8", "const:4:8"]]
- 00bf7fc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf8fb8 ["INT_ADD", "register:40f0:8", ["const:bf8fb8:8", "const:4:8"]]
+ 00bf8fb8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf7fc4 bytes e77f0194
+ 00bf8fb8 bytes de7f0194
- 00bf7fd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 00bf7fd4 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7fd4 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7fd4 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf8fc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 00bf8fc8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf8fc8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf8fc8 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7fd4 bytes 01b1c03d
+ 00bf8fc8 bytes 01c5c03d
- 00bf7ffc ["INT_ADD", "register:40f0:8", ["const:bf7ffc:8", "const:4:8"]]
- 00bf7ffc ["CALL", null, ["callee:00c5b930:8"]]
+ 00bf8ff0 ["INT_ADD", "register:40f0:8", ["const:bf8ff0:8", "const:4:8"]]
+ 00bf8ff0 ["CALL", null, ["callee:00c5b930:8"]]
- 00bf7ffc bytes 598a0194
+ 00bf8ff0 bytes 508a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b8f5832b3e05e64ff9fdd7c2b7a36e"></a>

### [`00bf80dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md) → [`00bf90d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf90d0.md) _ZNSt6__ndk110to_wstringEe

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b930.md) [`00c5f1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1b0.md) [`00c5f1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9108",
      "incomplete_value": true,
      "site": "00bf9110",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8114",
      "incomplete_value": true,
      "site": "00bf811c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf9108",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf916c",
      "PARAM",
      [
        "storage",
        "003105a4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf9108",
      "READ",
      [
        "storage",
        "002c3310",
        null,
        null
      ]
    ],
    [
      "00bf916c",
      "PARAM",
      [
        "storage",
        "003105e4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf8104) · [`00bf8114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf8114) · [`00bf813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf813c)
- 新版 [`00bf90f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf90d0.md#insn-00bf90f8) · [`00bf9108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf90d0.md#insn-00bf9108) · [`00bf9130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf90d0.md#insn-00bf9130)

~~~diff
- 00bf8104 ["INT_ADD", "register:40f0:8", ["const:bf8104:8", "const:4:8"]]
- 00bf8104 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf90f8 ["INT_ADD", "register:40f0:8", ["const:bf90f8:8", "const:4:8"]]
+ 00bf90f8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf8104 bytes 977f0194
+ 00bf90f8 bytes 8e7f0194
- 00bf8114 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 00bf8114 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf8114 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf8114 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf9108 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 00bf9108 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf9108 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf9108 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf8114 bytes 01b1c03d
+ 00bf9108 bytes 01c5c03d
- 00bf813c ["INT_ADD", "register:40f0:8", ["const:bf813c:8", "const:4:8"]]
- 00bf813c ["CALL", null, ["callee:00c5b930:8"]]
+ 00bf9130 ["INT_ADD", "register:40f0:8", ["const:bf9130:8", "const:4:8"]]
+ 00bf9130 ["CALL", null, ["callee:00c5b930:8"]]
- 00bf813c bytes 098a0194
+ 00bf9130 bytes 008a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d8d2b71a4ada13f0120f3bb6947eb8"></a>

### [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) → [`00bf920c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md) FUN_00bf920c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00bf4c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md) [`00bf4d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md) [`00bf56ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md) [`00bf5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md) · 呼出先 4件 [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)
- 新版 呼出元 4件 [`00bf5c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5c30.md) [`00bf5d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5d8c.md) [`00bf66e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf66e0.md) [`00bf6844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6844.md) · 呼出先 4件 [`004821e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/004821e0.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c5f0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9224",
      "incomplete_value": false,
      "site": "00bf9230",
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
            "const:606:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8230",
      "incomplete_value": false,
      "site": "00bf823c",
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
            "const:4ae:8"
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
      "00bf9224",
      "PARAM",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9224",
      "PARAM",
      [
        "storage",
        "002a7606",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf823c) · [`00bf8230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf8230) · [`00bf8250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf8250)
- 新版 [`00bf9230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md#insn-00bf9230) · [`00bf9224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md#insn-00bf9224) · [`00bf9244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf920c.md#insn-00bf9244)

~~~diff
- 00bf823c ["INT_ADD", "register:40f0:8", ["const:bf823c:8", "const:4:8"]]
- 00bf823c ["CALL", null, ["callee:004821e0:8"]]
+ 00bf9230 ["INT_ADD", "register:40f0:8", ["const:bf9230:8", "const:4:8"]]
+ 00bf9230 ["CALL", null, ["callee:004821e0:8"]]
- 00bf823c bytes 2127e297
+ 00bf9230 bytes ec23e297
- 00bf8230 ["COPY", "tmp:0:8", ["const:4ae:8"]]
- 00bf8230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf9224 ["COPY", "tmp:0:8", ["const:606:8"]]
+ 00bf9224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf9224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf9224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf8230 bytes 21b81291
+ 00bf9224 bytes 21181891
- 00bf8250 ["INT_ADD", "register:40f0:8", ["const:bf8250:8", "const:4:8"]]
- 00bf8250 ["CALL", null, ["callee:00bf925c:8"]]
+ 00bf9244 ["INT_ADD", "register:40f0:8", ["const:bf9244:8", "const:4:8"]]
+ 00bf9244 ["CALL", null, ["callee:00bf925c:8"]]
- 00bf8250 bytes 06000094
+ 00bf9244 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cebb4e661768a1fb3627370faaa6a921"></a>

### [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) → [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) FUN_00bf925c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`00bf4eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md) [`00bf501c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md) [`00bf5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md) [`00bf52f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md) [`00bf5440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md) · 呼出先 4件 [`00bf82bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf82bc.md) [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 13件 [`00bf5ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5ea4.md) [`00bf6010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6010.md) [`00bf617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf617c.md) [`00bf62ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf62ec.md) [`00bf6434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6434.md) · 呼出先 4件 [`00bf92b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf92b0.md) [`00c38d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9290",
      "incomplete_value": true,
      "site": "00bf9298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf829c",
      "incomplete_value": true,
      "site": "00bf82a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
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
      "definition_site": "00bf9294",
      "incomplete_value": true,
      "site": "00bf9298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf82a0",
      "incomplete_value": true,
      "site": "00bf82a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
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
      "00bf9290",
      "READ",
      [
        "storage",
        "00c9bb88",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9290",
      "PARAM",
      [
        "storage",
        "00c96868",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf9294",
      "READ",
      [
        "storage",
        "00c9bb90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf9290",
      "READ",
      [
        "storage",
        "00c9cb58",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9290",
      "PARAM",
      [
        "storage",
        "00c97838",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf9294",
      "READ",
      [
        "storage",
        "00c9cb60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf82a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf82a4) · [`00bf8280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf8280) · [`00bf828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf828c)
- 新版 [`00bf9298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md#insn-00bf9298) · [`00bf9274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md#insn-00bf9274) · [`00bf9280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md#insn-00bf9280)

~~~diff
- 00bf82a4 ["INT_ADD", "register:40f0:8", ["const:bf82a4:8", "const:4:8"]]
- 00bf82a4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00bf9298 ["INT_ADD", "register:40f0:8", ["const:bf9298:8", "const:4:8"]]
+ 00bf9298 ["CALL", null, ["callee:00c58fb0:8"]]
- 00bf82a4 bytes 4f7f0194
+ 00bf9298 bytes 467f0194
- 00bf8280 ["INT_ADD", "register:40f0:8", ["const:bf8280:8", "const:4:8"]]
- 00bf8280 ["CALL", null, ["callee:00c58f90:8"]]
+ 00bf9274 ["INT_ADD", "register:40f0:8", ["const:bf9274:8", "const:4:8"]]
+ 00bf9274 ["CALL", null, ["callee:00c58f90:8"]]
- 00bf8280 bytes 507f0194
+ 00bf9274 bytes 477f0194
- 00bf828c ["INT_ADD", "register:40f0:8", ["const:bf828c:8", "const:4:8"]]
- 00bf828c ["CALL", null, ["callee:00bf92b0:8"]]
+ 00bf9280 ["INT_ADD", "register:40f0:8", ["const:bf9280:8", "const:4:8"]]
+ 00bf9280 ["CALL", null, ["callee:00bf92b0:8"]]
- 00bf828c bytes 0c000094
+ 00bf9280 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8592930ba0b6a74546a3907d756534fe"></a>

### [`00bf86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md) → [`00bf96a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf96a0.md) FUN_00bf96a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bf87e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf87e0.md) [`00bf88a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf88a8.md) [`00bfaf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf14.md) · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)
- 新版 呼出元 3件 [`00bf97d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf97d4.md) [`00bf989c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf989c.md) [`00bfbf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf08.md) · 呼出先 8件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9710",
      "incomplete_value": false,
      "site": "00bf9724",
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
            "const:f6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf871c",
      "incomplete_value": false,
      "site": "00bf8730",
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
            "const:e9b:8"
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
      "00bf9704",
      "READ",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9710",
      "PARAM",
      [
        "storage",
        "002b7e9b",
        null,
        "string"
      ]
    ],
    [
      "00bf9728",
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
      "00bf9704",
      "READ",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9710",
      "PARAM",
      [
        "storage",
        "002b7f6a",
        null,
        "string"
      ]
    ],
    [
      "00bf9728",
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

- 旧版 [`00bf8730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf8730) · [`00bf86d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf86d0) · [`00bf86ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf86ec)
- 新版 [`00bf9724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf96a0.md#insn-00bf9724) · [`00bf96c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf96a0.md#insn-00bf96c4) · [`00bf96e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf96a0.md#insn-00bf96e0)

~~~diff
- 00bf8730 ["INT_ADD", "register:40f0:8", ["const:bf8730:8", "const:4:8"]]
- 00bf8730 ["CALL", null, ["callee:00c5f1a0:8"]]
+ 00bf9724 ["INT_ADD", "register:40f0:8", ["const:bf9724:8", "const:4:8"]]
+ 00bf9724 ["CALL", null, ["callee:00c5f1a0:8"]]
- 00bf8730 bytes a8960194
+ 00bf9724 bytes 9f960194
- 00bf86d0 ["INT_ADD", "register:40f0:8", ["const:bf86d0:8", "const:4:8"]]
- 00bf86d0 ["CALL", null, ["callee:00c59160:8"]]
+ 00bf96c4 ["INT_ADD", "register:40f0:8", ["const:bf96c4:8", "const:4:8"]]
+ 00bf96c4 ["CALL", null, ["callee:00c59160:8"]]
- 00bf86d0 bytes b07e0194
+ 00bf96c4 bytes a77e0194
- 00bf86ec ["INT_ADD", "register:40f0:8", ["const:bf86ec:8", "const:4:8"]]
- 00bf86ec ["CALL", null, ["callee:00c5f230:8"]]
+ 00bf96e0 ["INT_ADD", "register:40f0:8", ["const:bf96e0:8", "const:4:8"]]
+ 00bf96e0 ["CALL", null, ["callee:00c5f230:8"]]
- 00bf86ec bytes dd960194
+ 00bf96e0 bytes d4960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2edf6b59f10a6b5402bf7400a182e9aa"></a>

### [`00bf8848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md) → [`00bf983c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf983c.md) _ZNSt6__ndk116generic_categoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9870",
      "incomplete_value": false,
      "site": "00bf9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf887c",
      "incomplete_value": false,
      "site": "00bf8880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "definition_site": "00bf9880",
      "incomplete_value": false,
      "site": "00bf9884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf888c",
      "incomplete_value": false,
      "site": "00bf8890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf985c",
      "incomplete_value": false,
      "site": "00bf9868",
      "value": [
        "leaf",
        "const:ca5888:8"
      ]
    },
    "old": {
      "definition_site": "00bf8868",
      "incomplete_value": false,
      "site": "00bf8874",
      "value": [
        "leaf",
        "const:ca48b8:8"
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
      "00bf9850",
      "READ",
      [
        "storage",
        "01127460",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf985c",
      "DATA",
      [
        "storage",
        "00ca48b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9870",
      "PARAM",
      [
        "storage",
        "01127460",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf9850",
      "READ",
      [
        "storage",
        "01128420",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf985c",
      "DATA",
      [
        "storage",
        "00ca5888",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9870",
      "PARAM",
      [
        "storage",
        "01128420",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8880) · [`00bf8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8890) · [`00bf8854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8854)
- 新版 [`00bf9874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf983c.md#insn-00bf9874) · [`00bf9884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf983c.md#insn-00bf9884) · [`00bf9848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf983c.md#insn-00bf9848)

~~~diff
- 00bf8880 ["INT_ADD", "register:40f0:8", ["const:bf8880:8", "const:4:8"]]
- 00bf8880 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bf9874 ["INT_ADD", "register:40f0:8", ["const:bf9874:8", "const:4:8"]]
+ 00bf9874 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bf8880 bytes a87d0194
+ 00bf9874 bytes 9f7d0194
- 00bf8890 ["INT_ADD", "register:40f0:8", ["const:bf8890:8", "const:4:8"]]
- 00bf8890 ["CALL", null, ["callee:00c58f10:8"]]
+ 00bf9884 ["INT_ADD", "register:40f0:8", ["const:bf9884:8", "const:4:8"]]
+ 00bf9884 ["CALL", null, ["callee:00c58f10:8"]]
- 00bf8890 bytes ac7d0194
+ 00bf9884 bytes a37d0194
- 00bf8854 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bf9848 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00bf8854 bytes 682900f0
+ 00bf9848 bytes 682900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145c9a4abba47c1ac36be692efb3568d"></a>

### [`00bf8930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md) → [`00bf9924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9924.md) _ZNSt6__ndk115system_categoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9958",
      "incomplete_value": false,
      "site": "00bf995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8964",
      "incomplete_value": false,
      "site": "00bf8968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "definition_site": "00bf9968",
      "incomplete_value": false,
      "site": "00bf996c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8974",
      "incomplete_value": false,
      "site": "00bf8978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf9944",
      "incomplete_value": false,
      "site": "00bf9950",
      "value": [
        "leaf",
        "const:ca5890:8"
      ]
    },
    "old": {
      "definition_site": "00bf8950",
      "incomplete_value": false,
      "site": "00bf895c",
      "value": [
        "leaf",
        "const:ca48c0:8"
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
      "00bf9938",
      "READ",
      [
        "storage",
        "01127468",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9944",
      "DATA",
      [
        "storage",
        "00ca48c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9958",
      "PARAM",
      [
        "storage",
        "01127468",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf9938",
      "READ",
      [
        "storage",
        "01128428",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9944",
      "DATA",
      [
        "storage",
        "00ca5890",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9958",
      "PARAM",
      [
        "storage",
        "01128428",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf8968) · [`00bf8978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf8978) · [`00bf893c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf893c)
- 新版 [`00bf995c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9924.md#insn-00bf995c) · [`00bf996c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9924.md#insn-00bf996c) · [`00bf9930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9924.md#insn-00bf9930)

~~~diff
- 00bf8968 ["INT_ADD", "register:40f0:8", ["const:bf8968:8", "const:4:8"]]
- 00bf8968 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bf995c ["INT_ADD", "register:40f0:8", ["const:bf995c:8", "const:4:8"]]
+ 00bf995c ["CALL", null, ["callee:00c58ef0:8"]]
- 00bf8968 bytes 6e7d0194
+ 00bf995c bytes 657d0194
- 00bf8978 ["INT_ADD", "register:40f0:8", ["const:bf8978:8", "const:4:8"]]
- 00bf8978 ["CALL", null, ["callee:00c58f10:8"]]
+ 00bf996c ["INT_ADD", "register:40f0:8", ["const:bf996c:8", "const:4:8"]]
+ 00bf996c ["CALL", null, ["callee:00c58f10:8"]]
- 00bf8978 bytes 727d0194
+ 00bf996c bytes 697d0194
- 00bf893c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bf9930 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00bf893c bytes 682900f0
+ 00bf9930 bytes 682900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a862d1b56ca99ed88887650dcc6ccdd1"></a>

### [`00bf8ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md) → [`00bf9aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9aa4.md) FUN_00bf9aa4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00bf89b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf89b8.md) [`00bf8b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8b84.md) [`00bf8d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8d98.md) [`00bf8ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ea4.md) · 呼出先 3件 [`007dcf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dc/007dcf74.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 4件 [`00bf99ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf99ac.md) [`00bf9b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9b78.md) [`00bf9d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9d8c.md) [`00bf9e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9e98.md) · 呼出先 3件 [`007dded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007dd/007dded8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9aec",
      "incomplete_value": false,
      "site": "00bf9af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8af8",
      "incomplete_value": false,
      "site": "00bf8b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:71a:8"
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
      "00bf9aec",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf9aec",
      "PARAM",
      [
        "storage",
        "002bd7f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8b00) · [`00bf8af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8af8) · [`00bf8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8b18)
- 新版 [`00bf9af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9aa4.md#insn-00bf9af4) · [`00bf9aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9aa4.md#insn-00bf9aec) · [`00bf9b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9aa4.md#insn-00bf9b0c)

~~~diff
- 00bf8b00 ["INT_ADD", "register:40f0:8", ["const:bf8b00:8", "const:4:8"]]
- 00bf8b00 ["CALL", null, ["callee:00c59010:8"]]
+ 00bf9af4 ["INT_ADD", "register:40f0:8", ["const:bf9af4:8", "const:4:8"]]
+ 00bf9af4 ["CALL", null, ["callee:00c59010:8"]]
- 00bf8b00 bytes 507d0194
+ 00bf9af4 bytes 477d0194
- 00bf8af8 ["COPY", "tmp:0:8", ["const:71a:8"]]
- 00bf8af8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8af8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8af8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf9aec ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00bf9aec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf9aec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf9aec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf8af8 bytes 21681c91
+ 00bf9aec bytes 21e01f91
- 00bf8b18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bf8b18 ["INT_ADD", "register:40f0:8", ["const:bf8b18:8", "const:4:8"]]
- 00bf8b18 ["CALLIND", null, ["register:0:8"]]
+ 00bf9b0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bf9b0c ["INT_ADD", "register:40f0:8", ["const:bf9b0c:8", "const:4:8"]]
+ 00bf9b0c ["CALLIND", null, ["register:0:8"]]
- 00bf8b18 bytes 20013fd6
+ 00bf9b0c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7e48c2bdfc19aaa7e63f7089ab15f5b"></a>

### [`00bf9124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md) → [`00bfa118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa118.md) FUN_00bfa118

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bf9104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9104.md) · 呼出先 4件 [`00bf90d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e280.md)
- 新版 呼出元 1件 [`00bfa0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa0f8.md) · 呼出先 4件 [`00bfa0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa0c4.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5f250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa160",
      "incomplete_value": true,
      "site": "00bfa168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf916c",
      "incomplete_value": true,
      "site": "00bf9174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
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
      "definition_site": "00bfa164",
      "incomplete_value": true,
      "site": "00bfa168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9170",
      "incomplete_value": true,
      "site": "00bf9174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
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
      "00bfa160",
      "READ",
      [
        "storage",
        "00c9bbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa160",
      "PARAM",
      [
        "storage",
        "00c92c70",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bfa164",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfa160",
      "READ",
      [
        "storage",
        "00c9cb80",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa160",
      "PARAM",
      [
        "storage",
        "00c93c40",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bfa164",
      "READ",
      [
        "storage",
        "00c9cb78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf9174) · [`00bf9148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf9148) · [`00bf915c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf915c)
- 新版 [`00bfa168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa118.md#insn-00bfa168) · [`00bfa13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa118.md#insn-00bfa13c) · [`00bfa150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa118.md#insn-00bfa150)

~~~diff
- 00bf9174 ["INT_ADD", "register:40f0:8", ["const:bf9174:8", "const:4:8"]]
- 00bf9174 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00bfa168 ["INT_ADD", "register:40f0:8", ["const:bfa168:8", "const:4:8"]]
+ 00bfa168 ["CALL", null, ["callee:00c58fb0:8"]]
- 00bf9174 bytes 9b7b0194
+ 00bfa168 bytes 927b0194
- 00bf9148 ["INT_ADD", "register:40f0:8", ["const:bf9148:8", "const:4:8"]]
- 00bf9148 ["CALL", null, ["callee:00c58f90:8"]]
+ 00bfa13c ["INT_ADD", "register:40f0:8", ["const:bfa13c:8", "const:4:8"]]
+ 00bfa13c ["CALL", null, ["callee:00c58f90:8"]]
- 00bf9148 bytes 9e7b0194
+ 00bfa13c bytes 957b0194
- 00bf915c ["INT_ADD", "register:40f0:8", ["const:bf915c:8", "const:4:8"]]
- 00bf915c ["CALL", null, ["callee:00c5f250:8"]]
+ 00bfa150 ["INT_ADD", "register:40f0:8", ["const:bfa150:8", "const:4:8"]]
+ 00bfa150 ["CALL", null, ["callee:00c5f250:8"]]
- 00bf915c bytes 49940194
+ 00bfa150 bytes 40940194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0270ba30ffbca25f4b03346466ce99c"></a>

### [`00bf95f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md) → [`00bfa5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa5ec.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583e0.md) · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c593b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593b0.md) · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa620",
      "incomplete_value": false,
      "site": "00bfa624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf962c",
      "incomplete_value": false,
      "site": "00bf9630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "definition_site": "00bfa630",
      "incomplete_value": false,
      "site": "00bfa634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf963c",
      "incomplete_value": false,
      "site": "00bf9640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bfa60c",
      "incomplete_value": false,
      "site": "00bfa618",
      "value": [
        "leaf",
        "const:ca5898:8"
      ]
    },
    "old": {
      "definition_site": "00bf9618",
      "incomplete_value": false,
      "site": "00bf9624",
      "value": [
        "leaf",
        "const:ca48c8:8"
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
      "00bfa600",
      "READ",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa60c",
      "DATA",
      [
        "storage",
        "00ca48c8",
        null,
        null
      ]
    ],
    [
      "00bfa620",
      "PARAM",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfa600",
      "READ",
      [
        "storage",
        "01128430",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa60c",
      "DATA",
      [
        "storage",
        "00ca5898",
        null,
        null
      ]
    ],
    [
      "00bfa620",
      "PARAM",
      [
        "storage",
        "01128430",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9630) · [`00bf9640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9640) · [`00bf9604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9604)
- 新版 [`00bfa624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa5ec.md#insn-00bfa624) · [`00bfa634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa5ec.md#insn-00bfa634) · [`00bfa5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa5ec.md#insn-00bfa5f8)

~~~diff
- 00bf9630 ["INT_ADD", "register:40f0:8", ["const:bf9630:8", "const:4:8"]]
- 00bf9630 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfa624 ["INT_ADD", "register:40f0:8", ["const:bfa624:8", "const:4:8"]]
+ 00bfa624 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bf9630 bytes 3c7a0194
+ 00bfa624 bytes 337a0194
- 00bf9640 ["INT_ADD", "register:40f0:8", ["const:bf9640:8", "const:4:8"]]
- 00bf9640 ["CALL", null, ["callee:00c58f10:8"]]
+ 00bfa634 ["INT_ADD", "register:40f0:8", ["const:bfa634:8", "const:4:8"]]
+ 00bfa634 ["CALL", null, ["callee:00c58f10:8"]]
- 00bf9640 bytes 407a0194
+ 00bfa634 bytes 377a0194
- 00bf9604 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bfa5f8 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00bf9604 bytes 682900d0
+ 00bfa5f8 bytes 682900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f74062764d7bc20437fd90b0ee5a1a"></a>

### [`00bf9aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md) → [`00bfaaa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaaa0.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58570.md) · 呼出先 3件 [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)
- 新版 呼出元 1件 [`00c59540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59540.md) · 呼出先 3件 [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md)

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
      "definition_site": "00bfab24",
      "incomplete_value": false,
      "site": "00bfab2c",
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
            "const:aa5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9b30",
      "incomplete_value": false,
      "site": "00bf9b38",
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
            "const:9c7:8"
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
      "00bfab24",
      "PARAM",
      [
        "storage",
        "002be9c7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfab24",
      "PARAM",
      [
        "storage",
        "002beaa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9b38) · [`00bf9ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9ad8) · [`00bf9b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9b08)
- 新版 [`00bfab2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaaa0.md#insn-00bfab2c) · [`00bfaacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaaa0.md#insn-00bfaacc) · [`00bfaafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaaa0.md#insn-00bfaafc)

~~~diff
- 00bf9b38 ["INT_ADD", "register:40f0:8", ["const:bf9b38:8", "const:4:8"]]
- 00bf9b38 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfab2c ["INT_ADD", "register:40f0:8", ["const:bfab2c:8", "const:4:8"]]
+ 00bfab2c ["CALL", null, ["callee:00c591c0:8"]]
- 00bf9b38 bytes ae790194
+ 00bfab2c bytes a5790194
- 00bf9ad8 ["INT_ADD", "register:40f0:8", ["const:bf9ad8:8", "const:4:8"]]
- 00bf9ad8 ["CALL", null, ["callee:00c59520:8"]]
+ 00bfaacc ["INT_ADD", "register:40f0:8", ["const:bfaacc:8", "const:4:8"]]
+ 00bfaacc ["CALL", null, ["callee:00c59520:8"]]
- 00bf9ad8 bytes 9e7a0194
+ 00bfaacc bytes 957a0194
- 00bf9b08 ["INT_ADD", "register:40f0:8", ["const:bf9b08:8", "const:4:8"]]
- 00bf9b08 ["CALL", null, ["callee:00c59190:8"]]
+ 00bfaafc ["INT_ADD", "register:40f0:8", ["const:bfaafc:8", "const:4:8"]]
+ 00bfaafc ["CALL", null, ["callee:00c59190:8"]]
- 00bf9b08 bytes ae790194
+ 00bfaafc bytes a5790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e957b5fbf5c4644812453a09236a4cf1"></a>

### [`00bf9d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md) → [`00bfad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad34.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfad64",
      "incomplete_value": true,
      "site": "00bfad64",
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
      "definition_site": "00bf9d70",
      "incomplete_value": true,
      "site": "00bf9d70",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfad58",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00bfad64",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00bfad58",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfad64",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md#insn-00bf9d58) · [`00bf9d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md#insn-00bf9d5c) · [`00bf9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md#insn-00bf9d64)
- 新版 [`00bfad4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad34.md#insn-00bfad4c) · [`00bfad50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad34.md#insn-00bfad50) · [`00bfad58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad34.md#insn-00bfad58)

~~~diff
- 00bf9d58 ["INT_ADD", "register:40f0:8", ["const:bf9d58:8", "const:4:8"]]
- 00bf9d58 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bfad4c ["INT_ADD", "register:40f0:8", ["const:bfad4c:8", "const:4:8"]]
+ 00bfad4c ["CALL", null, ["callee:00c58f30:8"]]
- 00bf9d58 bytes 82780194
+ 00bfad4c bytes 79780194
- 00bf9d5c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00bfad50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bf9d5c bytes 080500b0
+ 00bfad50 bytes 080500b0
- 00bf9d64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 00bf9d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfad58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 00bfad58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf9d64 bytes 089146f9
+ 00bfad58 bytes 087946f9
~~~


<a id="compare-cd5ba5e2ea3b116ace3f476e5d78fbf4"></a>

### [`00bf9d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md) → [`00bfad88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad88.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045aa28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa28.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.11% / 新版 90.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfadf4",
      "incomplete_value": false,
      "site": "00bfadf4",
      "value": [
        "leaf",
        "const:ca5898:8"
      ]
    },
    "old": {
      "definition_site": "00bf9e00",
      "incomplete_value": false,
      "site": "00bf9e00",
      "value": [
        "leaf",
        "const:ca48c8:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfae30",
      "incomplete_value": true,
      "site": "00bfae38",
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
      "definition_site": "00bf9e3c",
      "incomplete_value": true,
      "site": "00bf9e44",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfae4c",
      "incomplete_value": true,
      "site": "00bfae54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9e58",
      "incomplete_value": true,
      "site": "00bf9e60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:d28:8"
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
      "00bfade0",
      "READ",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfadf4",
      "DATA",
      [
        "storage",
        "00ca48c8",
        null,
        null
      ]
    ],
    [
      "00bfae28",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfade0",
      "READ",
      [
        "storage",
        "01128430",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfadf4",
      "DATA",
      [
        "storage",
        "00ca5898",
        null,
        null
      ]
    ],
    [
      "00bfae28",
      "READ",
      [
        "storage",
        "00c9bd00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9e60) · [`00bf9ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9ee8) · [`00bf9ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9ef8)
- 新版 [`00bfae54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad88.md#insn-00bfae54) · [`00bfaedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad88.md#insn-00bfaedc) · [`00bfaeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfad88.md#insn-00bfaeec)

~~~diff
- 00bf9e60 ["INT_ADD", "register:40f0:8", ["const:bf9e60:8", "const:4:8"]]
- 00bf9e60 ["CALL", null, ["callee:00c593d0:8"]]
+ 00bfae54 ["INT_ADD", "register:40f0:8", ["const:bfae54:8", "const:4:8"]]
+ 00bfae54 ["CALL", null, ["callee:00c593d0:8"]]
- 00bf9e60 bytes 68790194
+ 00bfae54 bytes 5f790194
- 00bf9ee8 ["INT_ADD", "register:40f0:8", ["const:bf9ee8:8", "const:4:8"]]
- 00bf9ee8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfaedc ["INT_ADD", "register:40f0:8", ["const:bfaedc:8", "const:4:8"]]
+ 00bfaedc ["CALL", null, ["callee:00c58ef0:8"]]
- 00bf9ee8 bytes 0e780194
+ 00bfaedc bytes 05780194
- 00bf9ef8 ["INT_ADD", "register:40f0:8", ["const:bf9ef8:8", "const:4:8"]]
- 00bf9ef8 ["CALL", null, ["callee:00c58f10:8"]]
+ 00bfaeec ["INT_ADD", "register:40f0:8", ["const:bfaeec:8", "const:4:8"]]
+ 00bfaeec ["CALL", null, ["callee:00c58f10:8"]]
- 00bf9ef8 bytes 12780194
+ 00bfaeec bytes 09780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-408ff6980a277d58c7e1dcc7b9942212"></a>

### [`00bfa124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md) → [`00bfb118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb118.md) FUN_00bfb118

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb140",
      "incomplete_value": true,
      "site": "00bfb140",
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
      "definition_site": "00bfa14c",
      "incomplete_value": true,
      "site": "00bfa14c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb134",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb140",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00bfb134",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb140",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa134) · [`00bfa140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa140) · [`00bfa150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa150)
- 新版 [`00bfb128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb118.md#insn-00bfb128) · [`00bfb134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb118.md#insn-00bfb134) · [`00bfb144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb118.md#insn-00bfb144)

~~~diff
- 00bfa134 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00bfb128 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bfa134 bytes 08050090
+ 00bfb128 bytes 08050090
- 00bfa140 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 00bfa140 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb134 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 00bfb134 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfa140 bytes 089146f9
+ 00bfb134 bytes 087946f9
- 00bfa150 ["INT_ADD", "register:40f0:8", ["const:bfa150:8", "const:4:8"]]
- 00bfa150 ["CALL", null, ["callee:00c59170:8"]]
+ 00bfb144 ["INT_ADD", "register:40f0:8", ["const:bfb144:8", "const:4:8"]]
+ 00bfb144 ["CALL", null, ["callee:00c59170:8"]]
- 00bfa150 bytes 14780194
+ 00bfb144 bytes 0b780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8f4d65a4a1442df25a6e8efc7186c1"></a>

### [`00bfa1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md) → [`00bfb1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1c0.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)
- 新版 呼出元 1件 [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) · 呼出先 2件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb1e4",
      "incomplete_value": false,
      "site": "00bfb1e8",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa1f0",
      "incomplete_value": false,
      "site": "00bfa1f4",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb1e4",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb1e4",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1f4) · [`00bfa1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1d8) · [`00bfa1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1f0)
- 新版 [`00bfb1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1c0.md#insn-00bfb1e8) · [`00bfb1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1c0.md#insn-00bfb1cc) · [`00bfb1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1c0.md#insn-00bfb1e4)

~~~diff
- 00bfa1f4 ["INT_ADD", "register:40f0:8", ["const:bfa1f4:8", "const:4:8"]]
- 00bfa1f4 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb1e8 ["INT_ADD", "register:40f0:8", ["const:bfb1e8:8", "const:4:8"]]
+ 00bfb1e8 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa1f4 bytes ff770194
+ 00bfb1e8 bytes f6770194
- 00bfa1d8 ["INT_ADD", "register:40f0:8", ["const:bfa1d8:8", "const:4:8"]]
- 00bfa1d8 ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb1cc ["INT_ADD", "register:40f0:8", ["const:bfb1cc:8", "const:4:8"]]
+ 00bfb1cc ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa1d8 bytes 66850194
+ 00bfb1cc bytes 5d850194
- 00bfa1f0 ["COPY", "tmp:0:8", ["const:742:8"]]
- 00bfa1f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa1f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa1f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfb1e4 ["COPY", "tmp:0:8", ["const:819:8"]]
+ 00bfb1e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb1e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb1e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa1f0 bytes 21081d91
+ 00bfb1e4 bytes 21642091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ddcc472e99c309bba5a0a2cc4e7aff"></a>

### [`00bfa240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md) → [`00bfb234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb234.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a190.md) · 呼出先 6件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md) [`00c5bf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf50.md) [`00c5bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf60.md) [`00c5bf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf70.md)
- 新版 呼出元 1件 [`00c5b160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b160.md) · 呼出先 6件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5c730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c730.md) [`00c5cf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf20.md) [`00c5cf30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf30.md) [`00c5cf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb2d0",
      "incomplete_value": false,
      "site": "00bfb2d4",
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
            "const:9bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa2dc",
      "incomplete_value": false,
      "site": "00bfa2e0",
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
            "const:867:8"
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
      "00bfb2d0",
      "PARAM",
      [
        "storage",
        "002a8867",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb2d0",
      "PARAM",
      [
        "storage",
        "002a89bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa2e0) · [`00bfa25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa25c) · [`00bfa26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa26c)
- 新版 [`00bfb2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb234.md#insn-00bfb2d4) · [`00bfb250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb234.md#insn-00bfb250) · [`00bfb260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb234.md#insn-00bfb260)

~~~diff
- 00bfa2e0 ["INT_ADD", "register:40f0:8", ["const:bfa2e0:8", "const:4:8"]]
- 00bfa2e0 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb2d4 ["INT_ADD", "register:40f0:8", ["const:bfb2d4:8", "const:4:8"]]
+ 00bfb2d4 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa2e0 bytes c4770194
+ 00bfb2d4 bytes bb770194
- 00bfa25c ["INT_ADD", "register:40f0:8", ["const:bfa25c:8", "const:4:8"]]
- 00bfa25c ["CALL", null, ["callee:00c5cf40:8"]]
+ 00bfb250 ["INT_ADD", "register:40f0:8", ["const:bfb250:8", "const:4:8"]]
+ 00bfb250 ["CALL", null, ["callee:00c5cf40:8"]]
- 00bfa25c bytes 45870194
+ 00bfb250 bytes 3c870194
- 00bfa26c ["INT_ADD", "register:40f0:8", ["const:bfa26c:8", "const:4:8"]]
- 00bfa26c ["CALL", null, ["callee:00c5cf50:8"]]
+ 00bfb260 ["INT_ADD", "register:40f0:8", ["const:bfb260:8", "const:4:8"]]
+ 00bfb260 ["CALL", null, ["callee:00c5cf50:8"]]
- 00bfa26c bytes 45870194
+ 00bfb260 bytes 3c870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5be23e0708695ff42fdb20cdbe568f62"></a>

### [`00bfa304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md) → [`00bfb2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2f8.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)
- 新版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b180.md) · 呼出先 2件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb31c",
      "incomplete_value": false,
      "site": "00bfb320",
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
            "const:616:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa328",
      "incomplete_value": false,
      "site": "00bfa32c",
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
            "const:4be:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb31c",
      "PARAM",
      [
        "storage",
        "002a74be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb31c",
      "PARAM",
      [
        "storage",
        "002a7616",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa32c) · [`00bfa310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa310) · [`00bfa328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa328)
- 新版 [`00bfb320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2f8.md#insn-00bfb320) · [`00bfb304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2f8.md#insn-00bfb304) · [`00bfb31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb2f8.md#insn-00bfb31c)

~~~diff
- 00bfa32c ["INT_ADD", "register:40f0:8", ["const:bfa32c:8", "const:4:8"]]
- 00bfa32c ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb320 ["INT_ADD", "register:40f0:8", ["const:bfb320:8", "const:4:8"]]
+ 00bfb320 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa32c bytes b1770194
+ 00bfb320 bytes a8770194
- 00bfa310 ["INT_ADD", "register:40f0:8", ["const:bfa310:8", "const:4:8"]]
- 00bfa310 ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb304 ["INT_ADD", "register:40f0:8", ["const:bfb304:8", "const:4:8"]]
+ 00bfb304 ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa310 bytes 18850194
+ 00bfb304 bytes 0f850194
- 00bfa328 ["COPY", "tmp:0:8", ["const:4be:8"]]
- 00bfa328 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa328 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa328 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfb31c ["COPY", "tmp:0:8", ["const:616:8"]]
+ 00bfb31c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb31c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb31c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa328 bytes 21f81291
+ 00bfb31c bytes 21581891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c460b0fac493a6d26ebb44095efb12df"></a>

### [`00bfa394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md) → [`00bfb388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb388.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb3cc",
      "incomplete_value": false,
      "site": "00bfb3d0",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa3d8",
      "incomplete_value": false,
      "site": "00bfa3dc",
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
            "const:742:8"
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
      "00bfb3cc",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb3cc",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3dc) · [`00bfa3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3a8) · [`00bfa3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3b4)
- 新版 [`00bfb3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb388.md#insn-00bfb3d0) · [`00bfb39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb388.md#insn-00bfb39c) · [`00bfb3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb388.md#insn-00bfb3a8)

~~~diff
- 00bfa3dc ["INT_ADD", "register:40f0:8", ["const:bfa3dc:8", "const:4:8"]]
- 00bfa3dc ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb3d0 ["INT_ADD", "register:40f0:8", ["const:bfb3d0:8", "const:4:8"]]
+ 00bfb3d0 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa3dc bytes 85770194
+ 00bfb3d0 bytes 7c770194
- 00bfa3a8 ["INT_ADD", "register:40f0:8", ["const:bfa3a8:8", "const:4:8"]]
- 00bfa3a8 ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb39c ["INT_ADD", "register:40f0:8", ["const:bfb39c:8", "const:4:8"]]
+ 00bfb39c ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa3a8 bytes f2840194
+ 00bfb39c bytes e9840194
- 00bfa3b4 ["INT_ADD", "register:40f0:8", ["const:bfa3b4:8", "const:4:8"]]
- 00bfa3b4 ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb3a8 ["INT_ADD", "register:40f0:8", ["const:bfb3a8:8", "const:4:8"]]
+ 00bfb3a8 ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa3b4 bytes f3840194
+ 00bfb3a8 bytes ea840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7d9cf4c56d3b649174963851f8a834"></a>

### [`00bfa3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md) → [`00bfb3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb3dc.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb460",
      "incomplete_value": false,
      "site": "00bfb464",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa46c",
      "incomplete_value": false,
      "site": "00bfa470",
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
            "const:742:8"
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
      "00bfb460",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb460",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa470) · [`00bfa40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa40c) · [`00bfa424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa424)
- 新版 [`00bfb464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb3dc.md#insn-00bfb464) · [`00bfb400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb3dc.md#insn-00bfb400) · [`00bfb418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb3dc.md#insn-00bfb418)

~~~diff
- 00bfa470 ["INT_ADD", "register:40f0:8", ["const:bfa470:8", "const:4:8"]]
- 00bfa470 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb464 ["INT_ADD", "register:40f0:8", ["const:bfb464:8", "const:4:8"]]
+ 00bfb464 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa470 bytes 60770194
+ 00bfb464 bytes 57770194
- 00bfa40c ["INT_ADD", "register:40f0:8", ["const:bfa40c:8", "const:4:8"]]
- 00bfa40c ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb400 ["INT_ADD", "register:40f0:8", ["const:bfb400:8", "const:4:8"]]
+ 00bfb400 ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa40c bytes d9840194
+ 00bfb400 bytes d0840194
- 00bfa424 ["INT_ADD", "register:40f0:8", ["const:bfa424:8", "const:4:8"]]
- 00bfa424 ["CALL", null, ["callee:00c59520:8"]]
+ 00bfb418 ["INT_ADD", "register:40f0:8", ["const:bfb418:8", "const:4:8"]]
+ 00bfb418 ["CALL", null, ["callee:00c59520:8"]]
- 00bfa424 bytes 4b780194
+ 00bfb418 bytes 42780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8345e3777fd66e3d0ed977a304b9e064"></a>

### [`00bfa4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md) → [`00bfb4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb4cc.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5a1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a1b0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb510",
      "incomplete_value": false,
      "site": "00bfb514",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa51c",
      "incomplete_value": false,
      "site": "00bfa520",
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
            "const:742:8"
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
      "00bfb510",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb510",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa520) · [`00bfa4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa4ec) · [`00bfa4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa4fc)
- 新版 [`00bfb514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb4cc.md#insn-00bfb514) · [`00bfb4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb4cc.md#insn-00bfb4e0) · [`00bfb4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb4cc.md#insn-00bfb4f0)

~~~diff
- 00bfa520 ["INT_ADD", "register:40f0:8", ["const:bfa520:8", "const:4:8"]]
- 00bfa520 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb514 ["INT_ADD", "register:40f0:8", ["const:bfb514:8", "const:4:8"]]
+ 00bfb514 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa520 bytes 34770194
+ 00bfb514 bytes 2b770194
- 00bfa4ec ["INT_ADD", "register:40f0:8", ["const:bfa4ec:8", "const:4:8"]]
- 00bfa4ec ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb4e0 ["INT_ADD", "register:40f0:8", ["const:bfb4e0:8", "const:4:8"]]
+ 00bfb4e0 ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa4ec bytes a1840194
+ 00bfb4e0 bytes 98840194
- 00bfa4fc ["INT_ADD", "register:40f0:8", ["const:bfa4fc:8", "const:4:8"]]
- 00bfa4fc ["CALL", null, ["callee:00c5a1b0:8"]]
+ 00bfb4f0 ["INT_ADD", "register:40f0:8", ["const:bfb4f0:8", "const:4:8"]]
+ 00bfb4f0 ["CALL", null, ["callee:00c5a1b0:8"]]
- 00bfa4fc bytes 397b0194
+ 00bfb4f0 bytes 307b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a6791d19712268d8aa665a383c235c"></a>

### [`00bfa548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md) → [`00bfb53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb53c.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb580",
      "incomplete_value": false,
      "site": "00bfb584",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa58c",
      "incomplete_value": false,
      "site": "00bfa590",
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
            "const:742:8"
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
      "00bfb580",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb580",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa590) · [`00bfa55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa55c) · [`00bfa568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa568)
- 新版 [`00bfb584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb53c.md#insn-00bfb584) · [`00bfb550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb53c.md#insn-00bfb550) · [`00bfb55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb53c.md#insn-00bfb55c)

~~~diff
- 00bfa590 ["INT_ADD", "register:40f0:8", ["const:bfa590:8", "const:4:8"]]
- 00bfa590 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb584 ["INT_ADD", "register:40f0:8", ["const:bfb584:8", "const:4:8"]]
+ 00bfb584 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa590 bytes 18770194
+ 00bfb584 bytes 0f770194
- 00bfa55c ["INT_ADD", "register:40f0:8", ["const:bfa55c:8", "const:4:8"]]
- 00bfa55c ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb550 ["INT_ADD", "register:40f0:8", ["const:bfb550:8", "const:4:8"]]
+ 00bfb550 ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa55c bytes 85840194
+ 00bfb550 bytes 7c840194
- 00bfa568 ["INT_ADD", "register:40f0:8", ["const:bfa568:8", "const:4:8"]]
- 00bfa568 ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb55c ["INT_ADD", "register:40f0:8", ["const:bfb55c:8", "const:4:8"]]
+ 00bfb55c ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa568 bytes 86840194
+ 00bfb55c bytes 7d840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b0a45ac57c842c916473afa2187e45"></a>

### [`00bfa59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md) → [`00bfb590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb590.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md) [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md) [`00c596c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596c0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb63c",
      "incomplete_value": false,
      "site": "00bfb640",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa648",
      "incomplete_value": false,
      "site": "00bfa64c",
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
            "const:742:8"
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
      "definition_site": "00bfb648",
      "incomplete_value": false,
      "site": "00bfb650",
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
            "const:e45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa654",
      "incomplete_value": false,
      "site": "00bfa65c",
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
            "const:d7a:8"
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
      "00bfb63c",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ],
    [
      "00bfb648",
      "PARAM",
      [
        "storage",
        "002a3d7a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb63c",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ],
    [
      "00bfb648",
      "PARAM",
      [
        "storage",
        "002a3e45",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa64c) · [`00bfa65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa65c) · [`00bfa5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa5b4)
- 新版 [`00bfb640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb590.md#insn-00bfb640) · [`00bfb650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb590.md#insn-00bfb650) · [`00bfb5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb590.md#insn-00bfb5a8)

~~~diff
- 00bfa64c ["INT_ADD", "register:40f0:8", ["const:bfa64c:8", "const:4:8"]]
- 00bfa64c ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb640 ["INT_ADD", "register:40f0:8", ["const:bfb640:8", "const:4:8"]]
+ 00bfb640 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa64c bytes e9760194
+ 00bfb640 bytes e0760194
- 00bfa65c ["INT_ADD", "register:40f0:8", ["const:bfa65c:8", "const:4:8"]]
- 00bfa65c ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb650 ["INT_ADD", "register:40f0:8", ["const:bfb650:8", "const:4:8"]]
+ 00bfb650 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa65c bytes e5760194
+ 00bfb650 bytes dc760194
- 00bfa5b4 ["INT_ADD", "register:40f0:8", ["const:bfa5b4:8", "const:4:8"]]
- 00bfa5b4 ["CALL", null, ["callee:00c596c0:8"]]
+ 00bfb5a8 ["INT_ADD", "register:40f0:8", ["const:bfb5a8:8", "const:4:8"]]
+ 00bfb5a8 ["CALL", null, ["callee:00c596c0:8"]]
- 00bfa5b4 bytes 4f780194
+ 00bfb5a8 bytes 46780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d8cac4cf95438f85d80c3a9afc5b95"></a>

### [`00bfa704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md) → [`00bfb6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb6f8.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5a1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a1b0.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

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
      "definition_site": "00bfb760",
      "incomplete_value": false,
      "site": "00bfb764",
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
            "const:819:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa76c",
      "incomplete_value": false,
      "site": "00bfa770",
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
            "const:742:8"
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
      "00bfb760",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb760",
      "PARAM",
      [
        "storage",
        "002b1819",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa770) · [`00bfa718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa718) · [`00bfa734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa734)
- 新版 [`00bfb764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb6f8.md#insn-00bfb764) · [`00bfb70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb6f8.md#insn-00bfb70c) · [`00bfb728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb6f8.md#insn-00bfb728)

~~~diff
- 00bfa770 ["INT_ADD", "register:40f0:8", ["const:bfa770:8", "const:4:8"]]
- 00bfa770 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb764 ["INT_ADD", "register:40f0:8", ["const:bfb764:8", "const:4:8"]]
+ 00bfb764 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa770 bytes a0760194
+ 00bfb764 bytes 97760194
- 00bfa718 ["INT_ADD", "register:40f0:8", ["const:bfa718:8", "const:4:8"]]
- 00bfa718 ["CALL", null, ["callee:00c5c740:8"]]
+ 00bfb70c ["INT_ADD", "register:40f0:8", ["const:bfb70c:8", "const:4:8"]]
+ 00bfb70c ["CALL", null, ["callee:00c5c740:8"]]
- 00bfa718 bytes 16840194
+ 00bfb70c bytes 0d840194
- 00bfa734 ["INT_ADD", "register:40f0:8", ["const:bfa734:8", "const:4:8"]]
- 00bfa734 ["CALL", null, ["callee:00c5c750:8"]]
+ 00bfb728 ["INT_ADD", "register:40f0:8", ["const:bfb728:8", "const:4:8"]]
+ 00bfb728 ["CALL", null, ["callee:00c5c750:8"]]
- 00bfa734 bytes 13840194
+ 00bfb728 bytes 0a840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b708f8d1d1c45ef2efed6787e635c534"></a>

### [`00bfa7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md) → [`00bfb794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb794.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58240.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d710.md)
- 新版 呼出元 1件 [`00c59210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59210.md) · 呼出先 2件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5e6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e6e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb7d8",
      "incomplete_value": false,
      "site": "00bfb7dc",
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
            "const:3e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa7e4",
      "incomplete_value": false,
      "site": "00bfa7e8",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb7d8",
      "PARAM",
      [
        "storage",
        "002a628b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb7d8",
      "PARAM",
      [
        "storage",
        "002a63e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7e8) · [`00bfa7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7c0) · [`00bfa7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7e4)
- 新版 [`00bfb7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb794.md#insn-00bfb7dc) · [`00bfb7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb794.md#insn-00bfb7b4) · [`00bfb7d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb794.md#insn-00bfb7d8)

~~~diff
- 00bfa7e8 ["INT_ADD", "register:40f0:8", ["const:bfa7e8:8", "const:4:8"]]
- 00bfa7e8 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb7dc ["INT_ADD", "register:40f0:8", ["const:bfb7dc:8", "const:4:8"]]
+ 00bfb7dc ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa7e8 bytes 82760194
+ 00bfb7dc bytes 79760194
- 00bfa7c0 ["INT_ADD", "register:40f0:8", ["const:bfa7c0:8", "const:4:8"]]
- 00bfa7c0 ["CALL", null, ["callee:00c5e6e0:8"]]
+ 00bfb7b4 ["INT_ADD", "register:40f0:8", ["const:bfb7b4:8", "const:4:8"]]
+ 00bfb7b4 ["CALL", null, ["callee:00c5e6e0:8"]]
- 00bfa7c0 bytes d48b0194
+ 00bfb7b4 bytes cb8b0194
- 00bfa7e4 ["COPY", "tmp:0:8", ["const:28b:8"]]
- 00bfa7e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa7e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa7e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfb7d8 ["COPY", "tmp:0:8", ["const:3e3:8"]]
+ 00bfb7d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb7d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb7d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa7e4 bytes 212c0a91
+ 00bfb7d8 bytes 218c0f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1d6a1f9e4e37083ffb856431a10e0aa"></a>

### [`00bfa7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md) → [`00bfb7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb7e0.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585e0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5e350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e350.md)
- 新版 呼出元 1件 [`00c595b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595b0.md) · 呼出先 2件 [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5f320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f320.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb820",
      "incomplete_value": false,
      "site": "00bfb824",
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
            "const:5bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa82c",
      "incomplete_value": false,
      "site": "00bfa830",
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
            "const:4ef:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb820",
      "PARAM",
      [
        "storage",
        "002ae4ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb820",
      "PARAM",
      [
        "storage",
        "002ae5bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa830) · [`00bfa808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa808) · [`00bfa82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa82c)
- 新版 [`00bfb824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb7e0.md#insn-00bfb824) · [`00bfb7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb7e0.md#insn-00bfb7fc) · [`00bfb820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb7e0.md#insn-00bfb820)

~~~diff
- 00bfa830 ["INT_ADD", "register:40f0:8", ["const:bfa830:8", "const:4:8"]]
- 00bfa830 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb824 ["INT_ADD", "register:40f0:8", ["const:bfb824:8", "const:4:8"]]
+ 00bfb824 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa830 bytes 70760194
+ 00bfb824 bytes 67760194
- 00bfa808 ["INT_ADD", "register:40f0:8", ["const:bfa808:8", "const:4:8"]]
- 00bfa808 ["CALL", null, ["callee:00c5f320:8"]]
+ 00bfb7fc ["INT_ADD", "register:40f0:8", ["const:bfb7fc:8", "const:4:8"]]
+ 00bfb7fc ["CALL", null, ["callee:00c5f320:8"]]
- 00bfa808 bytes d28e0194
+ 00bfb7fc bytes c98e0194
- 00bfa82c ["COPY", "tmp:0:8", ["const:4ef:8"]]
- 00bfa82c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa82c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa82c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfb820 ["COPY", "tmp:0:8", ["const:5bc:8"]]
+ 00bfb820 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb820 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfb820 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa82c bytes 21bc1391
+ 00bfb820 bytes 21f01691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164d35eebc888765829384a6e847550d"></a>

### [`00bfa8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md) → [`00bfb8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb8d4.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) · 呼出先 3件 [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c591d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591d0.md) · 呼出先 3件 [`00bfb958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb934",
      "incomplete_value": true,
      "site": "00bfb934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa940",
      "incomplete_value": true,
      "site": "00bfa940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "definition_site": "00bfb910",
      "incomplete_value": false,
      "site": "00bfb914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa91c",
      "incomplete_value": false,
      "site": "00bfa920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00bfb924",
      "incomplete_value": false,
      "site": "00bfb928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa930",
      "incomplete_value": false,
      "site": "00bfa934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00bfb8f0",
      "READ",
      [
        "storage",
        "01127488",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb8f8",
      "READ",
      [
        "storage",
        "01127480",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb8f8",
      "DATA",
      [
        "storage",
        "01127478",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfb8f0",
      "READ",
      [
        "storage",
        "01128448",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb8f8",
      "READ",
      [
        "storage",
        "01128440",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb8f8",
      "DATA",
      [
        "storage",
        "01128438",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa920) · [`00bfa934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa934) · [`00bfa940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa940)
- 新版 [`00bfb914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb8d4.md#insn-00bfb914) · [`00bfb928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb8d4.md#insn-00bfb928) · [`00bfb934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb8d4.md#insn-00bfb934)

~~~diff
- 00bfa920 ["INT_ADD", "register:40f0:8", ["const:bfa920:8", "const:4:8"]]
- 00bfa920 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfb914 ["INT_ADD", "register:40f0:8", ["const:bfb914:8", "const:4:8"]]
+ 00bfb914 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bfa920 bytes 80750194
+ 00bfb914 bytes 77750194
- 00bfa934 ["INT_ADD", "register:40f0:8", ["const:bfa934:8", "const:4:8"]]
- 00bfa934 ["CALL", null, ["callee:00bfb958:8"]]
+ 00bfb928 ["INT_ADD", "register:40f0:8", ["const:bfb928:8", "const:4:8"]]
+ 00bfb928 ["CALL", null, ["callee:00bfb958:8"]]
- 00bfa934 bytes 0c000094
+ 00bfb928 bytes 0c000094
- 00bfa940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00bfa940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00bfb934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:440:8"]]
+ 00bfb934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bfa940 bytes 934202f9
+ 00bfb934 bytes 932202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac12e5e1c399d6ed514ffa3799b7234"></a>

### [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) → [`00bfb958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md) FUN_00bfb958

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md) · 呼出先 3件 [`00bfad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`00bfb8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb8d4.md) · 呼出先 3件 [`00bfbd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd0c.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5b3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b3a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "definition_site": "00bfb968",
      "incomplete_value": false,
      "site": "00bfb96c",
      "value": [
        "leaf",
        "const:bfbd0c:8"
      ]
    },
    "old": {
      "definition_site": "00bfa974",
      "incomplete_value": false,
      "site": "00bfa978",
      "value": [
        "leaf",
        "const:bfad18:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb984",
      "incomplete_value": false,
      "site": "00bfb988",
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
            "const:e6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa990",
      "incomplete_value": false,
      "site": "00bfa994",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb968",
      "PARAM",
      [
        "storage",
        "00bfad18",
        null,
        null
      ]
    ],
    [
      "00bfb984",
      "PARAM",
      [
        "storage",
        "002a3da3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb968",
      "PARAM",
      [
        "storage",
        "00bfbd0c",
        null,
        null
      ]
    ],
    [
      "00bfb984",
      "PARAM",
      [
        "storage",
        "002a3e6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa978) · [`00bfa994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa994) · [`00bfa974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa974)
- 新版 [`00bfb96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md#insn-00bfb96c) · [`00bfb988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md#insn-00bfb988) · [`00bfb968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb958.md#insn-00bfb968)

~~~diff
- 00bfa978 ["INT_ADD", "register:40f0:8", ["const:bfa978:8", "const:4:8"]]
- 00bfa978 ["CALL", null, ["callee:00c5b3a0:8"]]
+ 00bfb96c ["INT_ADD", "register:40f0:8", ["const:bfb96c:8", "const:4:8"]]
+ 00bfb96c ["CALL", null, ["callee:00c5b3a0:8"]]
- 00bfa978 bytes 967e0194
+ 00bfb96c bytes 8d7e0194
- 00bfa994 ["INT_ADD", "register:40f0:8", ["const:bfa994:8", "const:4:8"]]
- 00bfa994 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfb988 ["INT_ADD", "register:40f0:8", ["const:bfb988:8", "const:4:8"]]
+ 00bfb988 ["CALL", null, ["callee:00c591c0:8"]]
- 00bfa994 bytes 17760194
+ 00bfb988 bytes 0e760194
- 00bfa974 ["COPY", "register:4008:8", ["const:bfad18:8"]]
+ 00bfb968 ["COPY", "register:4008:8", ["const:bfbd0c:8"]]
- 00bfa974 bytes 211d0010
+ 00bfb968 bytes 211d0010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aaff7df5e9c60622f2ed1c325015594"></a>

### [`00bface8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md) → [`00bfbcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcdc.md) FUN_00bfbcdc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfaa64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00bfba58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfba58.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfbcec",
      "incomplete_value": false,
      "site": "00bfbcf0",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfacf8",
      "incomplete_value": false,
      "site": "00bfacfc",
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
            "const:f8c:8"
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
      "00bfbcec",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfbcec",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfacfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md#insn-00bfacfc) · [`00bfacf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md#insn-00bfacf4) · [`00bfacf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md#insn-00bfacf8)
- 新版 [`00bfbcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcdc.md#insn-00bfbcf0) · [`00bfbce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcdc.md#insn-00bfbce8) · [`00bfbcec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcdc.md#insn-00bfbcec)

~~~diff
- 00bfacfc ["INT_ADD", "register:40f0:8", ["const:bfacfc:8", "const:4:8"]]
- 00bfacfc ["CALL", null, ["callee:0043bad8:8"]]
+ 00bfbcf0 ["INT_ADD", "register:40f0:8", ["const:bfbcf0:8", "const:4:8"]]
+ 00bfbcf0 ["CALL", null, ["callee:0043bad8:8"]]
- 00bfacfc bytes af02e197
+ 00bfbcf0 bytes 7affe097
- 00bfacf4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00bfbce8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00bfacf4 bytes e0b5ffb0
+ 00bfbce8 bytes e0b5ffb0
- 00bfacf8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00bfacf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfacf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfacf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfbcec ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00bfbcec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfbcec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfbcec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfacf8 bytes 00303e91
+ 00bfbcec bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7255158982946e1a46255efd89c0599c"></a>

### [`00bfad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md) → [`00bfbcf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcf4.md) FUN_00bfbcf4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00bfbb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbb54.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfbd04",
      "incomplete_value": false,
      "site": "00bfbd08",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfad10",
      "incomplete_value": false,
      "site": "00bfad14",
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
            "const:f8c:8"
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
      "00bfbd04",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfbd04",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfad14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md#insn-00bfad14) · [`00bfad0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md#insn-00bfad0c) · [`00bfad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md#insn-00bfad10)
- 新版 [`00bfbd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcf4.md#insn-00bfbd08) · [`00bfbd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcf4.md#insn-00bfbd00) · [`00bfbd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbcf4.md#insn-00bfbd04)

~~~diff
- 00bfad14 ["INT_ADD", "register:40f0:8", ["const:bfad14:8", "const:4:8"]]
- 00bfad14 ["CALL", null, ["callee:0043bad8:8"]]
+ 00bfbd08 ["INT_ADD", "register:40f0:8", ["const:bfbd08:8", "const:4:8"]]
+ 00bfbd08 ["CALL", null, ["callee:0043bad8:8"]]
- 00bfad14 bytes a902e197
+ 00bfbd08 bytes 74ffe097
- 00bfad0c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00bfbd00 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00bfad0c bytes e0b5ffb0
+ 00bfbd00 bytes e0b5ffb0
- 00bfad10 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00bfad10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfad10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfad10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfbd04 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00bfbd04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfbd04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfbd04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfad10 bytes 00303e91
+ 00bfbd04 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40e860a6d9d2af79d377de913bb4456a"></a>

### [`00bfad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md) → [`00bfbd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd44.md) _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58470.md) · 呼出先 4件 [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6e0.md)
- 新版 呼出元 1件 [`00c59440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59440.md) · 呼出先 4件 [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5e6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfbda0",
      "incomplete_value": false,
      "site": "00bfbdb0",
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
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfadac",
      "incomplete_value": false,
      "site": "00bfadbc",
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
            "const:a33:8"
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
      "00bfbda0",
      "PARAM",
      [
        "storage",
        "002b4a33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfbda0",
      "PARAM",
      [
        "storage",
        "002b4b11",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfadbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfadbc) · [`00bfad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfad80) · [`00bfada0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfada0)
- 新版 [`00bfbdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd44.md#insn-00bfbdb0) · [`00bfbd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd44.md#insn-00bfbd74) · [`00bfbd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbd44.md#insn-00bfbd94)

~~~diff
- 00bfadbc ["INT_ADD", "register:40f0:8", ["const:bfadbc:8", "const:4:8"]]
- 00bfadbc ["CALL", null, ["callee:00c59150:8"]]
+ 00bfbdb0 ["INT_ADD", "register:40f0:8", ["const:bfbdb0:8", "const:4:8"]]
+ 00bfbdb0 ["CALL", null, ["callee:00c59150:8"]]
- 00bfadbc bytes f1740194
+ 00bfbdb0 bytes e8740194
- 00bfad80 ["INT_ADD", "register:40f0:8", ["const:bfad80:8", "const:4:8"]]
- 00bfad80 ["CALL", null, ["callee:00c5e6b0:8"]]
+ 00bfbd74 ["INT_ADD", "register:40f0:8", ["const:bfbd74:8", "const:4:8"]]
+ 00bfbd74 ["CALL", null, ["callee:00c5e6b0:8"]]
- 00bfad80 bytes 588a0194
+ 00bfbd74 bytes 4f8a0194
- 00bfada0 ["INT_ADD", "register:40f0:8", ["const:bfada0:8", "const:4:8"]]
- 00bfada0 ["CALL", null, ["callee:00c59160:8"]]
+ 00bfbd94 ["INT_ADD", "register:40f0:8", ["const:bfbd94:8", "const:4:8"]]
+ 00bfbd94 ["CALL", null, ["callee:00c59160:8"]]
- 00bfada0 bytes fc740194
+ 00bfbd94 bytes f3740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d156ec223852fadaf2b9312b98f432e"></a>

### [`00bfae18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md) → [`00bfbe0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbe0c.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58480.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d720.md)
- 新版 呼出元 1件 [`00c59450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59450.md) · 呼出先 3件 [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c591c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591c0.md) [`00c5e6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e6f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfbe88",
      "incomplete_value": false,
      "site": "00bfbe8c",
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
            "const:dbd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfae94",
      "incomplete_value": false,
      "site": "00bfae98",
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
            "const:cee:8"
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
      "definition_site": "00bfbe94",
      "incomplete_value": false,
      "site": "00bfbe9c",
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
            "const:51c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaea0",
      "incomplete_value": false,
      "site": "00bfaea8",
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
            "const:44f:8"
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
      "00bfbe88",
      "PARAM",
      [
        "storage",
        "002b8cee",
        null,
        "string"
      ]
    ],
    [
      "00bfbe94",
      "PARAM",
      [
        "storage",
        "002ac44f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfbe88",
      "PARAM",
      [
        "storage",
        "002b8dbd",
        null,
        "string"
      ]
    ],
    [
      "00bfbe94",
      "PARAM",
      [
        "storage",
        "002ac51c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfae98) · [`00bfaea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfaea8) · [`00bfae3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfae3c)
- 新版 [`00bfbe8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbe0c.md#insn-00bfbe8c) · [`00bfbe9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbe0c.md#insn-00bfbe9c) · [`00bfbe30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbe0c.md#insn-00bfbe30)

~~~diff
- 00bfae98 ["INT_ADD", "register:40f0:8", ["const:bfae98:8", "const:4:8"]]
- 00bfae98 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfbe8c ["INT_ADD", "register:40f0:8", ["const:bfbe8c:8", "const:4:8"]]
+ 00bfbe8c ["CALL", null, ["callee:00c591c0:8"]]
- 00bfae98 bytes d6740194
+ 00bfbe8c bytes cd740194
- 00bfaea8 ["INT_ADD", "register:40f0:8", ["const:bfaea8:8", "const:4:8"]]
- 00bfaea8 ["CALL", null, ["callee:00c591c0:8"]]
+ 00bfbe9c ["INT_ADD", "register:40f0:8", ["const:bfbe9c:8", "const:4:8"]]
+ 00bfbe9c ["CALL", null, ["callee:00c591c0:8"]]
- 00bfaea8 bytes d2740194
+ 00bfbe9c bytes c9740194
- 00bfae3c ["INT_ADD", "register:40f0:8", ["const:bfae3c:8", "const:4:8"]]
- 00bfae3c ["CALL", null, ["callee:00c59160:8"]]
+ 00bfbe30 ["INT_ADD", "register:40f0:8", ["const:bfbe30:8", "const:4:8"]]
+ 00bfbe30 ["CALL", null, ["callee:00c59160:8"]]
- 00bfae3c bytes d5740194
+ 00bfbe30 bytes cc740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a68be5f8a530b45ab4ba4746ccd23c"></a>

### [`00bfaf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md) → [`00bfbf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf7c.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfbfb0",
      "incomplete_value": false,
      "site": "00bfbfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfafbc",
      "incomplete_value": false,
      "site": "00bfafc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "definition_site": "00bfbfc0",
      "incomplete_value": false,
      "site": "00bfbfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfafcc",
      "incomplete_value": false,
      "site": "00bfafd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bfbf9c",
      "incomplete_value": false,
      "site": "00bfbfa8",
      "value": [
        "leaf",
        "const:ca58a0:8"
      ]
    },
    "old": {
      "definition_site": "00bfafa8",
      "incomplete_value": false,
      "site": "00bfafb4",
      "value": [
        "leaf",
        "const:ca48d0:8"
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
      "00bfbf90",
      "READ",
      [
        "storage",
        "01127490",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbf9c",
      "DATA",
      [
        "storage",
        "00ca48d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbfb0",
      "PARAM",
      [
        "storage",
        "01127490",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfbf90",
      "READ",
      [
        "storage",
        "01128450",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbf9c",
      "DATA",
      [
        "storage",
        "00ca58a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbfb0",
      "PARAM",
      [
        "storage",
        "01128450",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfafc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfafc0) · [`00bfafd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfafd0) · [`00bfaf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfaf94)
- 新版 [`00bfbfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf7c.md#insn-00bfbfb4) · [`00bfbfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf7c.md#insn-00bfbfc4) · [`00bfbf88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf7c.md#insn-00bfbf88)

~~~diff
- 00bfafc0 ["INT_ADD", "register:40f0:8", ["const:bfafc0:8", "const:4:8"]]
- 00bfafc0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfbfb4 ["INT_ADD", "register:40f0:8", ["const:bfbfb4:8", "const:4:8"]]
+ 00bfbfb4 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bfafc0 bytes d8730194
+ 00bfbfb4 bytes cf730194
- 00bfafd0 ["INT_ADD", "register:40f0:8", ["const:bfafd0:8", "const:4:8"]]
- 00bfafd0 ["CALL", null, ["callee:00c58f10:8"]]
+ 00bfbfc4 ["INT_ADD", "register:40f0:8", ["const:bfbfc4:8", "const:4:8"]]
+ 00bfbfc4 ["CALL", null, ["callee:00c58f10:8"]]
- 00bfafd0 bytes dc730194
+ 00bfbfc4 bytes d3730194
- 00bfaf94 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bfbf88 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00bfaf94 bytes 682900b0
+ 00bfbf88 bytes 682900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5499547402809f3f1281c5930bd49d82"></a>

### [`00bfb190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md) → [`00bfc184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc184.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc198",
      "incomplete_value": true,
      "site": "00bfc19c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb1a4",
      "incomplete_value": true,
      "site": "00bfb1a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
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
      "00bfc198",
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc198",
      "PARAM",
      [
        "storage",
        "01127498",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bfc198",
      "READ",
      [
        "storage",
        "00c9cb98",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc198",
      "PARAM",
      [
        "storage",
        "01128458",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md#insn-00bfb1a8) · [`00bfb19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md#insn-00bfb19c) · [`00bfb1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md#insn-00bfb1a4)
- 新版 [`00bfc19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc184.md#insn-00bfc19c) · [`00bfc190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc184.md#insn-00bfc190) · [`00bfc198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc184.md#insn-00bfc198)

~~~diff
- 00bfb1a8 ["INT_ADD", "register:40f0:8", ["const:bfb1a8:8", "const:4:8"]]
- 00bfb1a8 ["CALL", null, ["callee:00c54d30:8"]]
+ 00bfc19c ["INT_ADD", "register:40f0:8", ["const:bfc19c:8", "const:4:8"]]
+ 00bfc19c ["CALL", null, ["callee:00c54d30:8"]]
- 00bfb1a8 bytes e6620194
+ 00bfc19c bytes e5620194
- 00bfb19c ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 00bfc190 ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00bfb19c bytes 01050090
+ 00bfc190 bytes 01050090
- 00bfb1a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:bc8:8"]]
- 00bfb1a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfc198 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b98:8"]]
+ 00bfc198 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfb1a4 bytes 21e445f9
+ 00bfc198 bytes 21cc45f9
~~~


<a id="compare-ad3bfcaa7a22840ede6674ff5e4236c7"></a>

### [`00bfb1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md) → [`00bfc1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc1ac.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfc5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc5d4.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfc2ac",
      "incomplete_value": false,
      "site": "00bfc2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb2b8",
      "incomplete_value": false,
      "site": "00bfb2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc2b8",
      "incomplete_value": false,
      "site": "00bfc2bc",
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
            "const:632:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb2c4",
      "incomplete_value": false,
      "site": "00bfb2c8",
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
            "const:4da:8"
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
      "00bfc2a8",
      "DATA",
      [
        "storage",
        "011274a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc2ac",
      "WRITE",
      [
        "storage",
        "011274a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc2b8",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfc2a8",
      "DATA",
      [
        "storage",
        "01128460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc2ac",
      "WRITE",
      [
        "storage",
        "01128460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc2b8",
      "PARAM",
      [
        "storage",
        "002a7632",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb2c8) · [`00bfb210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb210) · [`00bfb260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb260)
- 新版 [`00bfc2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc1ac.md#insn-00bfc2bc) · [`00bfc204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc1ac.md#insn-00bfc204) · [`00bfc254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc1ac.md#insn-00bfc254)

~~~diff
- 00bfb2c8 ["INT_ADD", "register:40f0:8", ["const:bfb2c8:8", "const:4:8"]]
- 00bfb2c8 ["CALL", null, ["callee:00bfc5d4:8"]]
+ 00bfc2bc ["INT_ADD", "register:40f0:8", ["const:bfc2bc:8", "const:4:8"]]
+ 00bfc2bc ["CALL", null, ["callee:00bfc5d4:8"]]
- 00bfb2c8 bytes c6000094
+ 00bfc2bc bytes c6000094
- 00bfb210 ["INT_ADD", "register:40f0:8", ["const:bfb210:8", "const:4:8"]]
- 00bfb210 ["CALL", null, ["callee:00c5b140:8"]]
+ 00bfc204 ["INT_ADD", "register:40f0:8", ["const:bfc204:8", "const:4:8"]]
+ 00bfc204 ["CALL", null, ["callee:00c5b140:8"]]
- 00bfb210 bytes d87b0194
+ 00bfc204 bytes cf7b0194
- 00bfb260 ["INT_ADD", "register:40f0:8", ["const:bfb260:8", "const:4:8"]]
- 00bfb260 ["CALL", null, ["callee:00c59130:8"]]
+ 00bfc254 ["INT_ADD", "register:40f0:8", ["const:bfc254:8", "const:4:8"]]
+ 00bfc254 ["CALL", null, ["callee:00c59130:8"]]
- 00bfb260 bytes c0730194
+ 00bfc254 bytes b7730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a83f688a62cb4331ceae4a6b8664fe5f"></a>

### [`00bfb2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md) → [`00bfc2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc2c0.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfc5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc5d4.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfc3c0",
      "incomplete_value": false,
      "site": "00bfc3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb3cc",
      "incomplete_value": false,
      "site": "00bfb3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc3cc",
      "incomplete_value": false,
      "site": "00bfc3d0",
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
            "const:632:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb3d8",
      "incomplete_value": false,
      "site": "00bfb3dc",
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
            "const:4da:8"
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
      "00bfc3bc",
      "DATA",
      [
        "storage",
        "011274a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc3c0",
      "WRITE",
      [
        "storage",
        "011274a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc3cc",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfc3bc",
      "DATA",
      [
        "storage",
        "01128468",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc3c0",
      "WRITE",
      [
        "storage",
        "01128468",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfc3cc",
      "PARAM",
      [
        "storage",
        "002a7632",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb3dc) · [`00bfb324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb324) · [`00bfb374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb374)
- 新版 [`00bfc3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc2c0.md#insn-00bfc3d0) · [`00bfc318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc2c0.md#insn-00bfc318) · [`00bfc368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc2c0.md#insn-00bfc368)

~~~diff
- 00bfb3dc ["INT_ADD", "register:40f0:8", ["const:bfb3dc:8", "const:4:8"]]
- 00bfb3dc ["CALL", null, ["callee:00bfc5d4:8"]]
+ 00bfc3d0 ["INT_ADD", "register:40f0:8", ["const:bfc3d0:8", "const:4:8"]]
+ 00bfc3d0 ["CALL", null, ["callee:00bfc5d4:8"]]
- 00bfb3dc bytes 81000094
+ 00bfc3d0 bytes 81000094
- 00bfb324 ["INT_ADD", "register:40f0:8", ["const:bfb324:8", "const:4:8"]]
- 00bfb324 ["CALL", null, ["callee:00c5b140:8"]]
+ 00bfc318 ["INT_ADD", "register:40f0:8", ["const:bfc318:8", "const:4:8"]]
+ 00bfc318 ["CALL", null, ["callee:00c5b140:8"]]
- 00bfb324 bytes 937b0194
+ 00bfc318 bytes 8a7b0194
- 00bfb374 ["INT_ADD", "register:40f0:8", ["const:bfb374:8", "const:4:8"]]
- 00bfb374 ["CALL", null, ["callee:00c59130:8"]]
+ 00bfc368 ["INT_ADD", "register:40f0:8", ["const:bfc368:8", "const:4:8"]]
+ 00bfc368 ["CALL", null, ["callee:00c59130:8"]]
- 00bfb374 bytes 7b730194
+ 00bfc368 bytes 72730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ca129e2db28e900522c3d9918356d0"></a>

### [`00bfb3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md) → [`00bfc3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc3d4.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bfc5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc5d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

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
      "definition_site": "00bfc4ac",
      "incomplete_value": false,
      "site": "00bfc4b0",
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
            "const:632:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb4b8",
      "incomplete_value": false,
      "site": "00bfb4bc",
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
            "const:4da:8"
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
      "00bfc4ac",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfc4ac",
      "PARAM",
      [
        "storage",
        "002a7632",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb4bc) · [`00bfb434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb434) · [`00bfb460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb460)
- 新版 [`00bfc4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc3d4.md#insn-00bfc4b0) · [`00bfc428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc3d4.md#insn-00bfc428) · [`00bfc454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc3d4.md#insn-00bfc454)

~~~diff
- 00bfb4bc ["INT_ADD", "register:40f0:8", ["const:bfb4bc:8", "const:4:8"]]
- 00bfb4bc ["CALL", null, ["callee:00bfc5d4:8"]]
+ 00bfc4b0 ["INT_ADD", "register:40f0:8", ["const:bfc4b0:8", "const:4:8"]]
+ 00bfc4b0 ["CALL", null, ["callee:00bfc5d4:8"]]
- 00bfb4bc bytes 49000094
+ 00bfc4b0 bytes 49000094
- 00bfb434 ["INT_ADD", "register:40f0:8", ["const:bfb434:8", "const:4:8"]]
- 00bfb434 ["CALL", null, ["callee:00c5b140:8"]]
+ 00bfc428 ["INT_ADD", "register:40f0:8", ["const:bfc428:8", "const:4:8"]]
+ 00bfc428 ["CALL", null, ["callee:00c5b140:8"]]
- 00bfb434 bytes 4f7b0194
+ 00bfc428 bytes 467b0194
- 00bfb460 ["INT_ADD", "register:40f0:8", ["const:bfb460:8", "const:4:8"]]
- 00bfb460 ["CALL", null, ["callee:00c5b140:8"]]
+ 00bfc454 ["INT_ADD", "register:40f0:8", ["const:bfc454:8", "const:4:8"]]
+ 00bfc454 ["CALL", null, ["callee:00c5b140:8"]]
- 00bfb460 bytes 447b0194
+ 00bfc454 bytes 3b7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

