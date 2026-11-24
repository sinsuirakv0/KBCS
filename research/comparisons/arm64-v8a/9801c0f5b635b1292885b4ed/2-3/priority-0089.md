# v16.0.1 → v16.0.2 · 最優先の変更候補 (89)

[一覧の目次](README.md)

<a id="compare-acec4db87b003ee3dcda973ed70b6f57"></a>

### [`00c2663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2663c.md) → [`00c266d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c266d8.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5ea60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26758",
      "incomplete_value": true,
      "site": "00c26758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c266bc",
      "incomplete_value": true,
      "site": "00c266bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00c26738",
      "incomplete_value": false,
      "site": "00c2673c",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2669c",
      "incomplete_value": false,
      "site": "00c266a0",
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
            "const:ca0:8"
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
      "definition_site": "00c26748",
      "incomplete_value": false,
      "site": "00c26754",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c266ac",
      "incomplete_value": false,
      "site": "00c266b8",
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
            "const:17c:8"
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
      "00c26700",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26708",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c26738",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c26700",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26708",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c26738",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c266a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2663c.md#insn-00c266a0) · [`00c266b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2663c.md#insn-00c266b8) · [`00c266bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2663c.md#insn-00c266bc)
- 新版 `00c2673c`（命令位置の公開資料なし） · `00c26754`（命令位置の公開資料なし） · `00c26758`（命令位置の公開資料なし）

~~~diff
- 00c266a0 ["INT_ADD", "register:40f0:8", ["const:c266a0:8", "const:4:8"]]
- 00c266a0 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2673c ["INT_ADD", "register:40f0:8", ["const:c2673c:8", "const:4:8"]]
+ 00c2673c ["CALL", null, ["callee:00c57f20:8"]]
- 00c266a0 bytes ecc50094
+ 00c2673c bytes f9c50094
- 00c266b8 ["INT_ADD", "register:40f0:8", ["const:c266b8:8", "const:4:8"]]
- 00c266b8 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c26754 ["INT_ADD", "register:40f0:8", ["const:c26754:8", "const:4:8"]]
+ 00c26754 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c266b8 bytes dada0094
+ 00c26754 bytes e7da0094
- 00c266bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00c266bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
+ 00c26758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c266bc bytes 804e06f9
+ 00c26758 bytes 80ce06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d0894a9635dcde4b326946a196d2e6"></a>

### [`00c266e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c266e8.md) → [`00c26784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26784.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEPwPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26810",
      "incomplete_value": true,
      "site": "00c26810",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26774",
      "incomplete_value": true,
      "site": "00c26774",
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
            "const:c98:8"
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
      "00c267e8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c267f0",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c267fc",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c267e8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c267f0",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c267fc",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c266e8.md#insn-00c26774) · [`00c26714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c266e8.md#insn-00c26714) · [`00c26758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c266e8.md#insn-00c26758)
- 新版 `00c26810`（命令位置の公開資料なし） · `00c267b0`（命令位置の公開資料なし） · `00c267f4`（命令位置の公開資料なし）

~~~diff
- 00c26774 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c26774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26810 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
+ 00c26810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26774 bytes c04e06f9
+ 00c26810 bytes c0ce06f9
- 00c26714 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c26714 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26714 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26714 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c267b0 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c267b0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c267b0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c267b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26714 bytes b5823291
+ 00c267b0 bytes b5823691
- 00c26758 ["INT_ADD", "register:40f0:8", ["const:c26758:8", "const:4:8"]]
- 00c26758 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c267f4 ["INT_ADD", "register:40f0:8", ["const:c267f4:8", "const:4:8"]]
+ 00c267f4 ["CALL", null, ["callee:00c57f20:8"]]
- 00c26758 bytes bec50094
+ 00c267f4 bytes cbc50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a71338d915c237e8d2de71ccf9193df"></a>

### [`00c267bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c267bc.md) → [`00c26858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26858.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c268d0",
      "incomplete_value": false,
      "site": "00c268d0",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26834",
      "incomplete_value": false,
      "site": "00c26834",
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
            "const:c98:8"
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
      "definition_site": "00c268ac",
      "incomplete_value": false,
      "site": "00c268b0",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26810",
      "incomplete_value": false,
      "site": "00c26814",
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
            "const:ca0:8"
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
      "definition_site": "00c268bc",
      "incomplete_value": false,
      "site": "00c268c8",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26820",
      "incomplete_value": false,
      "site": "00c2682c",
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
            "const:17c:8"
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
      "00c2687c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268ac",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268bc",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2687c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268ac",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268bc",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c267bc.md#insn-00c26814) · [`00c2682c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c267bc.md#insn-00c2682c) · [`00c26834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c267bc.md#insn-00c26834)
- 新版 `00c268b0`（命令位置の公開資料なし） · `00c268c8`（命令位置の公開資料なし） · `00c268d0`（命令位置の公開資料なし）

~~~diff
- 00c26814 ["INT_ADD", "register:40f0:8", ["const:c26814:8", "const:4:8"]]
- 00c26814 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c268b0 ["INT_ADD", "register:40f0:8", ["const:c268b0:8", "const:4:8"]]
+ 00c268b0 ["CALL", null, ["callee:00c57f20:8"]]
- 00c26814 bytes 8fc50094
+ 00c268b0 bytes 9cc50094
- 00c2682c ["INT_ADD", "register:40f0:8", ["const:c2682c:8", "const:4:8"]]
- 00c2682c ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c268c8 ["INT_ADD", "register:40f0:8", ["const:c268c8:8", "const:4:8"]]
+ 00c268c8 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c2682c bytes 7dda0094
+ 00c268c8 bytes 8ada0094
- 00c26834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00c26834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c268d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c268d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26834 bytes 004d06f9
+ 00c268d0 bytes 00cd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937298a1f288acde30808d65c09abecc"></a>

### [`00c26860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26860.md) → [`00c268fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c268fc.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26988",
      "incomplete_value": true,
      "site": "00c26988",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268ec",
      "incomplete_value": true,
      "site": "00c268ec",
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
            "const:c98:8"
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
      "00c26960",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26968",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26974",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26960",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26968",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26974",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c268ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26860.md#insn-00c268ec) · [`00c2688c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26860.md#insn-00c2688c) · [`00c268d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26860.md#insn-00c268d0)
- 新版 `00c26988`（命令位置の公開資料なし） · `00c26928`（命令位置の公開資料なし） · `00c2696c`（命令位置の公開資料なし）

~~~diff
- 00c268ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c268ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26988 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
+ 00c26988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c268ec bytes c04e06f9
+ 00c26988 bytes c0ce06f9
- 00c2688c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c2688c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c2688c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c2688c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26928 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c26928 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26928 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26928 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c2688c bytes b5823291
+ 00c26928 bytes b5823691
- 00c268d0 ["INT_ADD", "register:40f0:8", ["const:c268d0:8", "const:4:8"]]
- 00c268d0 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2696c ["INT_ADD", "register:40f0:8", ["const:c2696c:8", "const:4:8"]]
+ 00c2696c ["CALL", null, ["callee:00c57f20:8"]]
- 00c268d0 bytes 60c50094
+ 00c2696c bytes 6dc50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69e02e6b2ae026cda7029c7f8a0cbf2"></a>

### [`00c26c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c08.md) → [`00c26ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ca4.md) _ZNSt6__ndk15ctypeIcEC1EPKmbm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26cbc",
      "incomplete_value": true,
      "site": "00c26cc0",
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
      "definition_site": "00c26c20",
      "incomplete_value": true,
      "site": "00c26c24",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26cd0",
      "incomplete_value": true,
      "site": "00c26cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26c34",
      "incomplete_value": true,
      "site": "00c26c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00c26cb0",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c26cc0",
      "DATA",
      [
        "storage",
        "00c93768",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c26cd4",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26cb0",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ],
    [
      "00c26cc0",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c26cd4",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c08.md#insn-00c26c14) · [`00c26c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c08.md#insn-00c26c34)
- 新版 `00c26cb0`（命令位置の公開資料なし） · `00c26cd0`（命令位置の公開資料なし）

~~~diff
- 00c26c14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
- 00c26c14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00c26cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c26c14 bytes 08e546f9
+ 00c26cb0 bytes 084d47f9
- 00c26c34 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00c26c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c26c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c26c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c26cd0 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00c26cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c26cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c26cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c26c34 bytes 08613e91
+ 00c26cd0 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12483800e260921d9c571e0cb3caaa72"></a>

### [`00c26cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26cc0.md) → [`00c26d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d5c.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26dd4",
      "incomplete_value": false,
      "site": "00c26dd4",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26d38",
      "incomplete_value": false,
      "site": "00c26d38",
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
            "const:c98:8"
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
      "definition_site": "00c26db0",
      "incomplete_value": false,
      "site": "00c26db4",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26d14",
      "incomplete_value": false,
      "site": "00c26d18",
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
            "const:ca0:8"
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
      "definition_site": "00c26dc0",
      "incomplete_value": false,
      "site": "00c26dcc",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26d24",
      "incomplete_value": false,
      "site": "00c26d30",
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
            "const:17c:8"
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
      "00c26d7c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26db0",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26dc0",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26d7c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26db0",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26dc0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26cc0.md#insn-00c26d18) · [`00c26d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26cc0.md#insn-00c26d30) · [`00c26d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26cc0.md#insn-00c26d38)
- 新版 `00c26db4`（命令位置の公開資料なし） · `00c26dcc`（命令位置の公開資料なし） · `00c26dd4`（命令位置の公開資料なし）

~~~diff
- 00c26d18 ["INT_ADD", "register:40f0:8", ["const:c26d18:8", "const:4:8"]]
- 00c26d18 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c26db4 ["INT_ADD", "register:40f0:8", ["const:c26db4:8", "const:4:8"]]
+ 00c26db4 ["CALL", null, ["callee:00c57f20:8"]]
- 00c26d18 bytes 4ec40094
+ 00c26db4 bytes 5bc40094
- 00c26d30 ["INT_ADD", "register:40f0:8", ["const:c26d30:8", "const:4:8"]]
- 00c26d30 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c26dcc ["INT_ADD", "register:40f0:8", ["const:c26dcc:8", "const:4:8"]]
+ 00c26dcc ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c26d30 bytes 3cd90094
+ 00c26dcc bytes 49d90094
- 00c26d38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00c26d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26dd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c26dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26d38 bytes 004d06f9
+ 00c26dd4 bytes 00cd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed68bd4b3917849443ca2475cf1fc148"></a>

### [`00c26d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26d64.md) → [`00c26e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26e00.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEPcPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26e8c",
      "incomplete_value": true,
      "site": "00c26e8c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26df0",
      "incomplete_value": true,
      "site": "00c26df0",
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
            "const:c98:8"
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
      "00c26e64",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e6c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e78",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26e64",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e6c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e78",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26d64.md#insn-00c26df0) · [`00c26d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26d64.md#insn-00c26d90) · [`00c26dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26d64.md#insn-00c26dd4)
- 新版 `00c26e8c`（命令位置の公開資料なし） · `00c26e2c`（命令位置の公開資料なし） · `00c26e70`（命令位置の公開資料なし）

~~~diff
- 00c26df0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c26df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26e8c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
+ 00c26e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26df0 bytes c04e06f9
+ 00c26e8c bytes c0ce06f9
- 00c26d90 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c26d90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26d90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26d90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26e2c ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c26e2c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26e2c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26e2c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26d90 bytes b5823291
+ 00c26e2c bytes b5823691
- 00c26dd4 ["INT_ADD", "register:40f0:8", ["const:c26dd4:8", "const:4:8"]]
- 00c26dd4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c26e70 ["INT_ADD", "register:40f0:8", ["const:c26e70:8", "const:4:8"]]
+ 00c26e70 ["CALL", null, ["callee:00c57f20:8"]]
- 00c26dd4 bytes 1fc40094
+ 00c26e70 bytes 2cc40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5854d6765b911ff07b63252edf02f05d"></a>

### [`00c26e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26e38.md) → [`00c26ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ed4.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26f4c",
      "incomplete_value": false,
      "site": "00c26f4c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26eb0",
      "incomplete_value": false,
      "site": "00c26eb0",
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
            "const:c98:8"
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
      "definition_site": "00c26f28",
      "incomplete_value": false,
      "site": "00c26f2c",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26e8c",
      "incomplete_value": false,
      "site": "00c26e90",
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
            "const:ca0:8"
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
      "definition_site": "00c26f38",
      "incomplete_value": true,
      "site": "00c26f44",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26e9c",
      "incomplete_value": true,
      "site": "00c26ea8",
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
            "const:17c:8"
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
      "00c26ef4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f28",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f38",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26ef4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f28",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f38",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26e38.md#insn-00c26e90) · [`00c26ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26e38.md#insn-00c26ea8) · [`00c26eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26e38.md#insn-00c26eb0)
- 新版 `00c26f2c`（命令位置の公開資料なし） · `00c26f44`（命令位置の公開資料なし） · `00c26f4c`（命令位置の公開資料なし）

~~~diff
- 00c26e90 ["INT_ADD", "register:40f0:8", ["const:c26e90:8", "const:4:8"]]
- 00c26e90 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c26f2c ["INT_ADD", "register:40f0:8", ["const:c26f2c:8", "const:4:8"]]
+ 00c26f2c ["CALL", null, ["callee:00c57f20:8"]]
- 00c26e90 bytes f0c30094
+ 00c26f2c bytes fdc30094
- 00c26ea8 ["INT_ADD", "register:40f0:8", ["const:c26ea8:8", "const:4:8"]]
- 00c26ea8 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c26f44 ["INT_ADD", "register:40f0:8", ["const:c26f44:8", "const:4:8"]]
+ 00c26f44 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c26ea8 bytes ded80094
+ 00c26f44 bytes ebd80094
- 00c26eb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00c26eb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26f4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c26f4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26eb0 bytes 004d06f9
+ 00c26f4c bytes 00cd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78f78df575e234136f73e78ca1094cb"></a>

### [`00c26edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26edc.md) → [`00c26f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26f78.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27004",
      "incomplete_value": true,
      "site": "00c27004",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26f68",
      "incomplete_value": true,
      "site": "00c26f68",
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
            "const:c98:8"
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
      "00c26fdc",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26fe4",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26ff0",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26fdc",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26fe4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26ff0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26edc.md#insn-00c26f68) · [`00c26f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26edc.md#insn-00c26f08) · [`00c26f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26edc.md#insn-00c26f4c)
- 新版 `00c27004`（命令位置の公開資料なし） · `00c26fa4`（命令位置の公開資料なし） · `00c26fe8`（命令位置の公開資料なし）

~~~diff
- 00c26f68 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c26f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27004 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
+ 00c27004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26f68 bytes c04e06f9
+ 00c27004 bytes c0ce06f9
- 00c26f08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c26f08 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26f08 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26f08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26fa4 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c26fa4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26fa4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26fa4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26f08 bytes b5823291
+ 00c26fa4 bytes b5823691
- 00c26f4c ["INT_ADD", "register:40f0:8", ["const:c26f4c:8", "const:4:8"]]
- 00c26f4c ["CALL", null, ["callee:00c57f20:8"]]
+ 00c26fe8 ["INT_ADD", "register:40f0:8", ["const:c26fe8:8", "const:4:8"]]
+ 00c26fe8 ["CALL", null, ["callee:00c57f20:8"]]
- 00c26f4c bytes c1c30094
+ 00c26fe8 bytes cec30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9aeaf65073cac443f34c8966ca817d"></a>

### [`00c27198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md) → [`00c27234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md) _ZNSt6__ndk112ctype_bynameIcEC1EPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9c0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 1件 [`00c5ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea90.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2726c",
      "incomplete_value": false,
      "site": "00c2726c",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c271d0",
      "incomplete_value": false,
      "site": "00c271d0",
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
            "const:f98:8"
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
      "definition_site": "00c272ac",
      "incomplete_value": false,
      "site": "00c272bc",
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
            "const:a51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27210",
      "incomplete_value": false,
      "site": "00c27220",
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
            "const:a20:8"
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
      "00c27254",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2726c",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ],
    [
      "00c27270",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c27254",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2726c",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ],
    [
      "00c27270",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c27220) · [`00c271b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c271b8) · [`00c271c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c271c8)
- 新版 `00c272bc`（命令位置の公開資料なし） · `00c27254`（命令位置の公開資料なし） · `00c27264`（命令位置の公開資料なし）

~~~diff
- 00c27220 ["INT_ADD", "register:40f0:8", ["const:c27220:8", "const:4:8"]]
- 00c27220 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c272bc ["INT_ADD", "register:40f0:8", ["const:c272bc:8", "const:4:8"]]
+ 00c272bc ["CALL", null, ["callee:00c259d0:8"]]
- 00c27220 bytes c5f9ff97
+ 00c272bc bytes c5f9ff97
- 00c271b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
- 00c271b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27254 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
+ 00c27254 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c271b8 bytes 29e946f9
+ 00c27254 bytes 295147f9
- 00c271c8 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00c271c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c271c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c271c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c27264 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00c27264 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c27264 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c27264 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c271c8 bytes 4a613e91
+ 00c27264 bytes 4a613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d5606a5179aa452f853c7a23235bb1"></a>

### [`00c27280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md) → [`00c2731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c2731c.md) _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e840.md) [`00c5e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9d0.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c5e910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e910.md) [`00c5eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eaa0.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27334",
      "incomplete_value": true,
      "site": "00c2733c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27298",
      "incomplete_value": true,
      "site": "00c272a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27358",
      "incomplete_value": true,
      "site": "00c27358",
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
      "definition_site": "00c272bc",
      "incomplete_value": true,
      "site": "00c272bc",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c27398",
      "incomplete_value": false,
      "site": "00c273a8",
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
            "const:a51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c272fc",
      "incomplete_value": false,
      "site": "00c2730c",
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
            "const:a20:8"
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
      "00c2733c",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ],
    [
      "00c27348",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c27358",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c2733c",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ],
    [
      "00c27348",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c27358",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c2730c) · [`00c27298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c27298) · [`00c272ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c272ac)
- 新版 `00c273a8`（命令位置の公開資料なし） · `00c27334`（命令位置の公開資料なし） · `00c27348`（命令位置の公開資料なし）

~~~diff
- 00c2730c ["INT_ADD", "register:40f0:8", ["const:c2730c:8", "const:4:8"]]
- 00c2730c ["CALL", null, ["callee:00c58180:8"]]
+ 00c273a8 ["INT_ADD", "register:40f0:8", ["const:c273a8:8", "const:4:8"]]
+ 00c273a8 ["CALL", null, ["callee:00c58180:8"]]
- 00c2730c bytes 69c30094
+ 00c273a8 bytes 76c30094
- 00c27298 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00c27298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c27298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c27298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c27334 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00c27334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c27334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c27334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c27298 bytes 08613e91
+ 00c27334 bytes 08613f91
- 00c272ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00c272ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27348 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c27348 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c272ac bytes 08e946f9
+ 00c27348 bytes 085147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff0c44059b859c6f2a063654a96ff659"></a>

### [`00c27710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md) → [`00c277ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md) _ZNSt6__ndk112ctype_bynameIwEC2EPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9f0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 1件 [`00c5eac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eac0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c277d8",
      "incomplete_value": true,
      "site": "00c277d8",
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
      "definition_site": "00c2773c",
      "incomplete_value": true,
      "site": "00c2773c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c27814",
      "incomplete_value": false,
      "site": "00c27824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:a8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27778",
      "incomplete_value": false,
      "site": "00c27788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00c277cc",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c277d8",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27814",
      "PARAM",
      [
        "storage",
        "002bfae0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c277cc",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c277d8",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27814",
      "PARAM",
      [
        "storage",
        "002bfa8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27788) · [`00c27730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27730) · [`00c27748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27748)
- 新版 `00c27824`（命令位置の公開資料なし） · `00c277cc`（命令位置の公開資料なし） · `00c277e4`（命令位置の公開資料なし）

~~~diff
- 00c27788 ["INT_ADD", "register:40f0:8", ["const:c27788:8", "const:4:8"]]
- 00c27788 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c27824 ["INT_ADD", "register:40f0:8", ["const:c27824:8", "const:4:8"]]
+ 00c27824 ["CALL", null, ["callee:00c259d0:8"]]
- 00c27788 bytes 6bf8ff97
+ 00c27824 bytes 6bf8ff97
- 00c27730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 00c27730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c277cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 00c277cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c27730 bytes 08ed46f9
+ 00c277cc bytes 085547f9
- 00c27748 ["INT_ADD", "register:40f0:8", ["const:c27748:8", "const:4:8"]]
- 00c27748 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c277e4 ["INT_ADD", "register:40f0:8", ["const:c277e4:8", "const:4:8"]]
+ 00c277e4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c27748 bytes b6d60094
+ 00c277e4 bytes c3d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fab65e31aff3c0e51059dfeea8918c"></a>

### [`00c277e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md) → [`00c27884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27884.md) _ZNSt6__ndk112ctype_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e850.md) [`00c5ea10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea10.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c5e920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e920.md) [`00c5eae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eae0.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c278b0",
      "incomplete_value": true,
      "site": "00c278b0",
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
      "definition_site": "00c27814",
      "incomplete_value": true,
      "site": "00c27814",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c278f0",
      "incomplete_value": false,
      "site": "00c27900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:a8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27854",
      "incomplete_value": false,
      "site": "00c27864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00c278a4",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c278b0",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c278f0",
      "PARAM",
      [
        "storage",
        "002bfae0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c278a4",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c278b0",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c278f0",
      "PARAM",
      [
        "storage",
        "002bfa8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27864) · [`00c27808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27808) · [`00c27830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27830)
- 新版 `00c27900`（命令位置の公開資料なし） · `00c278a4`（命令位置の公開資料なし） · `00c278cc`（命令位置の公開資料なし）

~~~diff
- 00c27864 ["INT_ADD", "register:40f0:8", ["const:c27864:8", "const:4:8"]]
- 00c27864 ["CALL", null, ["callee:00c58180:8"]]
+ 00c27900 ["INT_ADD", "register:40f0:8", ["const:c27900:8", "const:4:8"]]
+ 00c27900 ["CALL", null, ["callee:00c58180:8"]]
- 00c27864 bytes 13c20094
+ 00c27900 bytes 20c20094
- 00c27808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 00c27808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c278a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 00c278a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c27808 bytes 08ed46f9
+ 00c278a4 bytes 085547f9
- 00c27830 ["INT_ADD", "register:40f0:8", ["const:c27830:8", "const:4:8"]]
- 00c27830 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c278cc ["INT_ADD", "register:40f0:8", ["const:c278cc:8", "const:4:8"]]
+ 00c278cc ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c27830 bytes 7cd60094
+ 00c278cc bytes 89d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753e2cb55203e76fe0716a69e6d3a4d0"></a>

### [`00c28200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md) → [`00c2829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2829c.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a870.md) [`00c5e7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7f0.md) · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c5a940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a940.md) [`00c5e8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8c0.md) · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c282d8",
      "incomplete_value": true,
      "site": "00c282dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2823c",
      "incomplete_value": true,
      "site": "00c28240",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c28314",
      "incomplete_value": true,
      "site": "00c28314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c28278",
      "incomplete_value": true,
      "site": "00c28278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00c282f4",
      "incomplete_value": false,
      "site": "00c282f8",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c28258",
      "incomplete_value": false,
      "site": "00c2825c",
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
            "const:ca0:8"
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
      "00c282b8",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c282c4",
      "DATA",
      [
        "storage",
        "00c938c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c282d0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c282b8",
      "READ",
      [
        "storage",
        "00c9beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c282c4",
      "DATA",
      [
        "storage",
        "00c93990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c282d0",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2825c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c2825c) · [`00c28278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c28278) · [`00c2821c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c2821c)
- 新版 `00c282f8`（命令位置の公開資料なし） · `00c28314`（命令位置の公開資料なし） · `00c282b8`（命令位置の公開資料なし）

~~~diff
- 00c2825c ["INT_ADD", "register:40f0:8", ["const:c2825c:8", "const:4:8"]]
- 00c2825c ["CALL", null, ["callee:00c57f20:8"]]
+ 00c282f8 ["INT_ADD", "register:40f0:8", ["const:c282f8:8", "const:4:8"]]
+ 00c282f8 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2825c bytes fdbe0094
+ 00c282f8 bytes 0abf0094
- 00c28278 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00c28278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c28314 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
+ 00c28314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c28278 bytes 804e06f9
+ 00c28314 bytes 80ce06f9
- 00c2821c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
- 00c2821c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c282b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
+ 00c282b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2821c bytes 08f146f9
+ 00c282b8 bytes 085947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67257b265477fe2c3edc279a0e6e7d6b"></a>

### [`00c2be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be6c.md) → [`00c2bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf08.md) _ZNSt6__ndk18numpunctIcEC2Em

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e800.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2bf2c",
      "incomplete_value": true,
      "site": "00c2bf2c",
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
      "definition_site": "00c2be90",
      "incomplete_value": true,
      "site": "00c2be90",
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
      "00c2bf14",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2bf2c",
      "DATA",
      [
        "storage",
        "00c93920",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2bf14",
      "READ",
      [
        "storage",
        "00c9beb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2bf2c",
      "DATA",
      [
        "storage",
        "00c939f0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be6c.md#insn-00c2be78)
- 新版 `00c2bf14`（命令位置の公開資料なし）

~~~diff
- 00c2be78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de8:8"]]
- 00c2be78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2bf14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:eb8:8"]]
+ 00c2bf14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2be78 bytes 29f546f9
+ 00c2bf14 bytes 295d47f9
~~~


<a id="compare-1693ec1332da71b5ab20346858c08c4c"></a>

### [`00c2be98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md) → [`00c2bf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf34.md) _ZNSt6__ndk18numpunctIwEC1Em

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e810.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2bf48",
      "incomplete_value": true,
      "site": "00c2bf58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:328:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2beac",
      "incomplete_value": true,
      "site": "00c2bebc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c2bf5c",
      "incomplete_value": true,
      "site": "00c2bf5c",
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
      "definition_site": "00c2bec0",
      "incomplete_value": true,
      "site": "00c2bec0",
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
      "00c2bf44",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2bf48",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2bf5c",
      "DATA",
      [
        "storage",
        "00c93970",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2bf44",
      "READ",
      [
        "storage",
        "00c9bec0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2bf48",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2bf5c",
      "DATA",
      [
        "storage",
        "00c93a40",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md#insn-00c2bea8) · [`00c2beac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md#insn-00c2beac)
- 新版 `00c2bf44`（命令位置の公開資料なし） · `00c2bf48`（命令位置の公開資料なし）

~~~diff
- 00c2bea8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:df0:8"]]
- 00c2bea8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2bf44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
+ 00c2bf44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2bea8 bytes 29f946f9
+ 00c2bf44 bytes 296147f9
- 00c2beac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 00c2beac ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2beac ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2beac ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2bf48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 00c2bf48 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2bf48 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2bf48 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2beac bytes 007541fd
+ 00c2bf48 bytes 009541fd
~~~


<a id="compare-937dfc31d1092b52f89012ced3245b4a"></a>

### [`00c2c070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c070.md) → [`00c2c10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c10c.md) _ZNKSt6__ndk18numpunctIwE11do_truenameEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c11c",
      "incomplete_value": true,
      "site": "00c2c128",
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
                "const:310000:8"
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
    "old": {
      "definition_site": "00c2c080",
      "incomplete_value": true,
      "site": "00c2c08c",
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
                "const:310000:8"
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
      "00c2c11c",
      "READ",
      [
        "storage",
        "00310738",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2c11c",
      "READ",
      [
        "storage",
        "00310778",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c070.md#insn-00c2c078)
- 新版 `00c2c114`（命令位置の公開資料なし）

~~~diff
- 00c2c078 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00c2c078 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c2c078 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c2c078 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c2c114 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00c2c114 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2c114 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2c114 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c2c078 bytes 4ae11c91
+ 00c2c114 bytes 4ae11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c01e451bf1d9d894c444a2174c18ad8"></a>

### [`00c2c174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md) → [`00c2c210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c210.md) _ZNKSt6__ndk18numpunctIwE12do_falsenameEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c238",
      "incomplete_value": true,
      "site": "00c2c24c",
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
                "const:2c2000:8"
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
      "definition_site": "00c2c19c",
      "incomplete_value": true,
      "site": "00c2c1b0",
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
                "const:2c2000:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c244",
      "incomplete_value": true,
      "site": "00c2c250",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:7f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c1a8",
      "incomplete_value": true,
      "site": "00c2c1b4",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:7b4:8"
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
      "00c2c238",
      "READ",
      [
        "storage",
        "002c2530",
        null,
        null
      ]
    ],
    [
      "00c2c244",
      "READ",
      [
        "storage",
        "003107b4",
        null,
        "unicode32"
      ]
    ]
  ],
  "added": [
    [
      "00c2c238",
      "READ",
      [
        "storage",
        "002c2570",
        null,
        null
      ]
    ],
    [
      "00c2c244",
      "READ",
      [
        "storage",
        "003107f4",
        null,
        "unicode32"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md#insn-00c2c18c) · [`00c2c19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md#insn-00c2c19c) · [`00c2c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md#insn-00c2c1a0)
- 新版 `00c2c228`（命令位置の公開資料なし） · `00c2c238`（命令位置の公開資料なし）

~~~diff
- 00c2c18c ["INT_ADD", "register:40f0:8", ["const:c2c18c:8", "const:4:8"]]
- 00c2c18c ["CALL", null, ["callee:00c57f60:8"]]
+ 00c2c228 ["INT_ADD", "register:40f0:8", ["const:c2c228:8", "const:4:8"]]
+ 00c2c228 ["CALL", null, ["callee:00c57f60:8"]]
- 00c2c18c bytes 41af0094
+ 00c2c228 bytes 4eaf0094
- 00c2c19c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 00c2c19c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2c19c ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c19c ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2c238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00c2c238 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c238 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c238 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2c19c bytes 004dc13d
+ 00c2c238 bytes 005dc13d
- 00c2c1a0 ["COPY", "register:4040:8", ["const:310000:8"]]
- 00c2c1a0 bytes 28b7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01adae752a4181d9e0bd2aa5a5ded1e3"></a>

### [`00c2c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md) → [`00c2c264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c264.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c298",
      "incomplete_value": true,
      "site": "00c2c298",
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
      "definition_site": "00c2c1fc",
      "incomplete_value": true,
      "site": "00c2c1fc",
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
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c28c",
      "READ",
      [
        "storage",
        "00c9bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c298",
      "DATA",
      [
        "storage",
        "00c939c0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c28c",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c298",
      "DATA",
      [
        "storage",
        "00c93a90",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md#insn-00c2c1f0) · [`00c2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md#insn-00c2c200)
- 新版 `00c2c28c`（命令位置の公開資料なし） · `00c2c29c`（命令位置の公開資料なし）

~~~diff
- 00c2c1f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
- 00c2c1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c28c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
+ 00c2c28c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c1f0 bytes 08fd46f9
+ 00c2c28c bytes 086547f9
- 00c2c200 ["INT_ADD", "register:40f0:8", ["const:c2c200:8", "const:4:8"]]
- 00c2c200 ["CALL", null, ["callee:00c5ed20:8"]]
+ 00c2c29c ["INT_ADD", "register:40f0:8", ["const:c2c29c:8", "const:4:8"]]
+ 00c2c29c ["CALL", null, ["callee:00c5ed20:8"]]
- 00c2c200 bytes 94ca0094
+ 00c2c29c bytes a1ca0094
~~~


<a id="compare-14698583d795fd7420b524206fb7208d"></a>

### [`00c2c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md) → [`00c2c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md) _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md) · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2c4f0",
      "incomplete_value": false,
      "site": "00c2c500",
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
            "const:96f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c454",
      "incomplete_value": false,
      "site": "00c2c464",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c2ec",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "00c2c4f0",
      "PARAM",
      [
        "storage",
        "002a9940",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2c2ec",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00c2c4f0",
      "PARAM",
      [
        "storage",
        "002a996f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c464) · [`00c2c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c250) · [`00c2c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c258)
- 新版 `00c2c500`（命令位置の公開資料なし） · `00c2c2ec`（命令位置の公開資料なし） · `00c2c2f4`（命令位置の公開資料なし）

~~~diff
- 00c2c464 ["INT_ADD", "register:40f0:8", ["const:c2c464:8", "const:4:8"]]
- 00c2c464 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c2c500 ["INT_ADD", "register:40f0:8", ["const:c2c500:8", "const:4:8"]]
+ 00c2c500 ["CALL", null, ["callee:00c259d0:8"]]
- 00c2c464 bytes 34e5ff97
+ 00c2c500 bytes 34e5ff97
- 00c2c250 ["COPY", "tmp:0:8", ["const:17c:8"]]
- 00c2c250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c2c2ec ["COPY", "tmp:0:8", ["const:1bc:8"]]
+ 00c2c2ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c2ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c2ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c2c250 bytes 21f00591
+ 00c2c2ec bytes 21f00691
- 00c2c258 ["INT_ADD", "register:40f0:8", ["const:c2c258:8", "const:4:8"]]
- 00c2c258 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c2c2f4 ["INT_ADD", "register:40f0:8", ["const:c2c2f4:8", "const:4:8"]]
+ 00c2c2f4 ["CALL", null, ["callee:00c5b920:8"]]
- 00c2c258 bytes 7ebd0094
+ 00c2c2f4 bytes 8bbd0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aafd36dfd2f01b1587c1d04feaee72b0"></a>

### [`00c2c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md) → [`00c2c598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c598.md) _ZNSt6__ndk115numpunct_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e870.md) · 呼出先 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md)
- 新版 呼出元 1件 [`00c5e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e940.md) · 呼出先 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md)

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
      "definition_site": "00c2c5cc",
      "incomplete_value": true,
      "site": "00c2c5cc",
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
      "definition_site": "00c2c530",
      "incomplete_value": true,
      "site": "00c2c530",
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
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c5c0",
      "READ",
      [
        "storage",
        "00c9bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c5cc",
      "DATA",
      [
        "storage",
        "00c939c0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c5c0",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c5cc",
      "DATA",
      [
        "storage",
        "00c93a90",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md#insn-00c2c524) · [`00c2c544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md#insn-00c2c544)
- 新版 `00c2c5c0`（命令位置の公開資料なし） · `00c2c5e0`（命令位置の公開資料なし）

~~~diff
- 00c2c524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
- 00c2c524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
+ 00c2c5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c524 bytes 08fd46f9
+ 00c2c5c0 bytes 086547f9
- 00c2c544 ["INT_ADD", "register:40f0:8", ["const:c2c544:8", "const:4:8"]]
- 00c2c544 ["CALL", null, ["callee:00c5ed20:8"]]
+ 00c2c5e0 ["INT_ADD", "register:40f0:8", ["const:c2c5e0:8", "const:4:8"]]
+ 00c2c5e0 ["CALL", null, ["callee:00c5ed20:8"]]
- 00c2c544 bytes c3c90094
+ 00c2c5e0 bytes d0c90094
~~~


<a id="compare-5760de256ab954bcfd7fc775bd7f5320"></a>

### [`00c2c5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md) → [`00c2c65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c65c.md) _ZNSt6__ndk115numpunct_bynameIwEC1EPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c678",
      "incomplete_value": true,
      "site": "00c2c68c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:328:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c5dc",
      "incomplete_value": true,
      "site": "00c2c5f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c694",
      "incomplete_value": true,
      "site": "00c2c694",
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
      "definition_site": "00c2c5f8",
      "incomplete_value": true,
      "site": "00c2c5f8",
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
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c678",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c684",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c694",
      "DATA",
      [
        "storage",
        "00c93a10",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c678",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c684",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c694",
      "DATA",
      [
        "storage",
        "00c93ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5dc) · [`00c2c5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5e8) · [`00c2c5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5fc)
- 新版 `00c2c678`（命令位置の公開資料なし） · `00c2c684`（命令位置の公開資料なし） · `00c2c698`（命令位置の公開資料なし）

~~~diff
- 00c2c5dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 00c2c5dc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c5dc ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c5dc ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c678 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 00c2c678 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c678 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2c678 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c5dc bytes 007541fd
+ 00c2c678 bytes 009541fd
- 00c2c5e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
- 00c2c5e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c684 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 00c2c684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c5e8 bytes 080147f9
+ 00c2c684 bytes 086947f9
- 00c2c5fc ["INT_ADD", "register:40f0:8", ["const:c2c5fc:8", "const:4:8"]]
- 00c2c5fc ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c2c698 ["INT_ADD", "register:40f0:8", ["const:c2c698:8", "const:4:8"]]
+ 00c2c698 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c2c5fc bytes a1c90094
+ 00c2c698 bytes aec90094
~~~


<a id="compare-0bd840a8f6661c7cee89966e037380b7"></a>

### [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) → [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) _ZNSt6__ndk115numpunct_bynameIwE6__initEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md) · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2c6e8",
      "incomplete_value": false,
      "site": "00c2c6f0",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c64c",
      "incomplete_value": false,
      "site": "00c2c654",
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
            "const:17c:8"
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
      "definition_site": "00c2c834",
      "incomplete_value": false,
      "site": "00c2c844",
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
            "const:75a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c798",
      "incomplete_value": false,
      "site": "00c2c7a8",
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
            "const:7b6:8"
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
      "00c2c6e8",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "00c2c834",
      "PARAM",
      [
        "storage",
        "002b17b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2c6e8",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00c2c834",
      "PARAM",
      [
        "storage",
        "002b175a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c654) · [`00c2c70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c70c) · [`00c2c7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c7a8)
- 新版 `00c2c6f0`（命令位置の公開資料なし） · `00c2c7a8`（命令位置の公開資料なし） · `00c2c844`（命令位置の公開資料なし）

~~~diff
- 00c2c654 ["INT_ADD", "register:40f0:8", ["const:c2c654:8", "const:4:8"]]
- 00c2c654 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c2c6f0 ["INT_ADD", "register:40f0:8", ["const:c2c6f0:8", "const:4:8"]]
+ 00c2c6f0 ["CALL", null, ["callee:00c5b920:8"]]
- 00c2c654 bytes 7fbc0094
+ 00c2c6f0 bytes 8cbc0094
- 00c2c70c ["INT_ADD", "register:40f0:8", ["const:c2c70c:8", "const:4:8"]]
- 00c2c70c ["CALL", null, ["callee:00c580b0:8"]]
+ 00c2c7a8 ["INT_ADD", "register:40f0:8", ["const:c2c7a8:8", "const:4:8"]]
+ 00c2c7a8 ["CALL", null, ["callee:00c580b0:8"]]
- 00c2c70c bytes 35ae0094
+ 00c2c7a8 bytes 42ae0094
- 00c2c7a8 ["INT_ADD", "register:40f0:8", ["const:c2c7a8:8", "const:4:8"]]
- 00c2c7a8 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c2c844 ["INT_ADD", "register:40f0:8", ["const:c2c844:8", "const:4:8"]]
+ 00c2c844 ["CALL", null, ["callee:00c259d0:8"]]
- 00c2c7a8 bytes 63e4ff97
+ 00c2c844 bytes 63e4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e0f3ebe7b4e2b84c678e1a85b891ca1"></a>

### [`00c2c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md) → [`00c2c8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c8cc.md) _ZNSt6__ndk115numpunct_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e880.md) · 呼出先 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md)
- 新版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e950.md) · 呼出先 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c8e8",
      "incomplete_value": true,
      "site": "00c2c8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:328:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c84c",
      "incomplete_value": true,
      "site": "00c2c860",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c904",
      "incomplete_value": true,
      "site": "00c2c904",
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
      "definition_site": "00c2c868",
      "incomplete_value": true,
      "site": "00c2c868",
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
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c8e8",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c8f4",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c904",
      "DATA",
      [
        "storage",
        "00c93a10",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c8e8",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c8f4",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c904",
      "DATA",
      [
        "storage",
        "00c93ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c84c) · [`00c2c858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c858) · [`00c2c87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c87c)
- 新版 `00c2c8e8`（命令位置の公開資料なし） · `00c2c8f4`（命令位置の公開資料なし） · `00c2c918`（命令位置の公開資料なし）

~~~diff
- 00c2c84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 00c2c84c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c84c ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c84c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 00c2c8e8 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c8e8 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2c8e8 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c84c bytes 007541fd
+ 00c2c8e8 bytes 009541fd
- 00c2c858 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
- 00c2c858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c8f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 00c2c8f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c858 bytes 080147f9
+ 00c2c8f4 bytes 086947f9
- 00c2c87c ["INT_ADD", "register:40f0:8", ["const:c2c87c:8", "const:4:8"]]
- 00c2c87c ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c2c918 ["INT_ADD", "register:40f0:8", ["const:c2c918:8", "const:4:8"]]
+ 00c2c918 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c2c87c bytes 01c90094
+ 00c2c918 bytes 0ec90094
~~~


<a id="compare-21824f6ccf6235debf662c0b7fe0ae2f"></a>

### [`00c2ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md) → [`00c2cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2cb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cb68",
      "incomplete_value": false,
      "site": "00c2cb68",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cacc",
      "incomplete_value": false,
      "site": "00c2cacc",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cb58",
      "incomplete_value": false,
      "site": "00c2cb68",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cabc",
      "incomplete_value": false,
      "site": "00c2cacc",
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
            "const:fa8:8"
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
      "definition_site": "00c2cb40",
      "incomplete_value": false,
      "site": "00c2cb44",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2caa4",
      "incomplete_value": false,
      "site": "00c2caa8",
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
            "const:eb0:8"
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
      "00c2cb20",
      "READ",
      [
        "storage",
        "01127eb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb2c",
      "READ",
      [
        "storage",
        "01127ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cb2c",
      "DATA",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2cb20",
      "READ",
      [
        "storage",
        "01127fb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb2c",
      "READ",
      [
        "storage",
        "01127fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cb2c",
      "DATA",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2caa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2caa8) · [`00c2cacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2cacc) · [`00c2cad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2cad0)
- 新版 `00c2cb44`（命令位置の公開資料なし） · `00c2cb68`（命令位置の公開資料なし） · `00c2cb6c`（命令位置の公開資料なし）

~~~diff
- 00c2caa8 ["INT_ADD", "register:40f0:8", ["const:c2caa8:8", "const:4:8"]]
- 00c2caa8 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2cb44 ["INT_ADD", "register:40f0:8", ["const:c2cb44:8", "const:4:8"]]
+ 00c2cb44 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2caa8 bytes eaac0094
+ 00c2cb44 bytes f7ac0094
- 00c2cacc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00c2cacc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2cb68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 00c2cb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2cacc bytes 095507f9
+ 00c2cb68 bytes 09d507f9
- 00c2cad0 ["INT_ADD", "register:40f0:8", ["const:c2cad0:8", "const:4:8"]]
- 00c2cad0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2cb6c ["INT_ADD", "register:40f0:8", ["const:c2cb6c:8", "const:4:8"]]
+ 00c2cb6c ["CALL", null, ["callee:00c57f40:8"]]
- 00c2cad0 bytes e8ac0094
+ 00c2cb6c bytes f5ac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e647e0712348d71919d9f697ef3765d"></a>

### [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) → [`00c2cb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) FUN_00c2cb78

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md) · 呼出先 4件 [`00c35ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c2cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md) · 呼出先 4件 [`00c35c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35c3c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.48% / 新版 71.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 21件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cbac",
      "incomplete_value": false,
      "site": "00c2cbac",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb10",
      "incomplete_value": false,
      "site": "00c2cb10",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cbc4",
      "incomplete_value": false,
      "site": "00c2cbc4",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb28",
      "incomplete_value": false,
      "site": "00c2cb28",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cbf8",
      "incomplete_value": false,
      "site": "00c2cbf8",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb5c",
      "incomplete_value": false,
      "site": "00c2cb5c",
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
            "const:fc0:8"
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
      "00c2cb8c",
      "READ",
      [
        "storage",
        "011280f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb98",
      "READ",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cbac",
      "WRITE",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2cb8c",
      "READ",
      [
        "storage",
        "011281f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb98",
      "READ",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cbac",
      "WRITE",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cb8c) · [`00c2cee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cee4) · [`00c2cf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cf00)
- 新版 `00c2cc28`（命令位置の公開資料なし） · `00c2cf80`（命令位置の公開資料なし） · `00c2cf9c`（命令位置の公開資料なし）

~~~diff
- 00c2cb8c ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00c2cc28 ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00c2cb8c bytes c92700f0
+ 00c2cc28 bytes e9270090
- 00c2cee4 ["INT_ADD", "register:40f0:8", ["const:c2cee4:8", "const:4:8"]]
- 00c2cee4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2cf80 ["INT_ADD", "register:40f0:8", ["const:c2cf80:8", "const:4:8"]]
+ 00c2cf80 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2cee4 bytes dbab0094
+ 00c2cf80 bytes e8ab0094
- 00c2cf00 ["INT_ADD", "register:40f0:8", ["const:c2cf00:8", "const:4:8"]]
- 00c2cf00 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2cf9c ["INT_ADD", "register:40f0:8", ["const:c2cf9c:8", "const:4:8"]]
+ 00c2cf9c ["CALL", null, ["callee:00c57f00:8"]]
- 00c2cf00 bytes ccab0094
+ 00c2cf9c bytes d9ab0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8e820b98bcc313e2f7d86fe94ba2c8"></a>

### [`00c2cf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md) → [`00c2cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d030.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d00c",
      "incomplete_value": true,
      "site": "00c2d00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cf70",
      "incomplete_value": true,
      "site": "00c2cf70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d000",
      "incomplete_value": false,
      "site": "00c2d00c",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cf64",
      "incomplete_value": false,
      "site": "00c2cf70",
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
            "const:100:8"
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
      "definition_site": "00c2cfec",
      "incomplete_value": false,
      "site": "00c2cff0",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cf50",
      "incomplete_value": false,
      "site": "00c2cf54",
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
            "const:ec0:8"
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
      "00c2cfcc",
      "READ",
      [
        "storage",
        "01127ec0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cfd4",
      "READ",
      [
        "storage",
        "01127eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cfd4",
      "DATA",
      [
        "storage",
        "01128100",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2cfcc",
      "READ",
      [
        "storage",
        "01127fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cfd4",
      "READ",
      [
        "storage",
        "01127fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cfd4",
      "DATA",
      [
        "storage",
        "01128200",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf54) · [`00c2cf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf5c) · [`00c2cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf70)
- 新版 `00c2cff0`（命令位置の公開資料なし） · `00c2cff8`（命令位置の公開資料なし） · `00c2d00c`（命令位置の公開資料なし）

~~~diff
- 00c2cf54 ["INT_ADD", "register:40f0:8", ["const:c2cf54:8", "const:4:8"]]
- 00c2cf54 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2cff0 ["INT_ADD", "register:40f0:8", ["const:c2cff0:8", "const:4:8"]]
+ 00c2cff0 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2cf54 bytes bfab0094
+ 00c2cff0 bytes ccab0094
- 00c2cf5c ["INT_ADD", "register:40f0:8", ["const:c2cf5c:8", "const:4:8"]]
- 00c2cf5c ["CALL", null, ["ram:c2cf94:8"]]
+ 00c2cff8 ["INT_ADD", "register:40f0:8", ["const:c2cff8:8", "const:4:8"]]
+ 00c2cff8 ["CALL", null, ["ram:c2d030:8"]]
- 00c2cf5c bytes 0e000094
+ 00c2cff8 bytes 0e000094
- 00c2cf70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb8:8"]]
- 00c2cf70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2d00c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
+ 00c2d00c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2cf70 bytes 685e07f9
+ 00c2d00c bytes 68de07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1f052519bac8358fed23128e4dca38"></a>

### [`00c2d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md) → [`00c2d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md) _ZNKSt6__ndk120__time_get_c_storageIcE8__monthsEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2d2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d360",
      "incomplete_value": false,
      "site": "00c2d360",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d2c4",
      "incomplete_value": false,
      "site": "00c2d2c4",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d350",
      "incomplete_value": false,
      "site": "00c2d360",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d2b4",
      "incomplete_value": false,
      "site": "00c2d2c4",
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
            "const:258:8"
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
      "definition_site": "00c2d338",
      "incomplete_value": false,
      "site": "00c2d33c",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d29c",
      "incomplete_value": false,
      "site": "00c2d2a0",
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
            "const:ed0:8"
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
      "00c2d318",
      "READ",
      [
        "storage",
        "01127ed0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d324",
      "READ",
      [
        "storage",
        "01127ec8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d324",
      "DATA",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2d318",
      "READ",
      [
        "storage",
        "01127fd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d324",
      "READ",
      [
        "storage",
        "01127fc8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d324",
      "DATA",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2a0) · [`00c2d2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2c4) · [`00c2d2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2c8)
- 新版 `00c2d33c`（命令位置の公開資料なし） · `00c2d360`（命令位置の公開資料なし） · `00c2d364`（命令位置の公開資料なし）

~~~diff
- 00c2d2a0 ["INT_ADD", "register:40f0:8", ["const:c2d2a0:8", "const:4:8"]]
- 00c2d2a0 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2d33c ["INT_ADD", "register:40f0:8", ["const:c2d33c:8", "const:4:8"]]
+ 00c2d33c ["CALL", null, ["callee:00c57f20:8"]]
- 00c2d2a0 bytes ecaa0094
+ 00c2d33c bytes f9aa0094
- 00c2d2c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
- 00c2d2c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2d360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
+ 00c2d360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2d2c4 bytes 096507f9
+ 00c2d360 bytes 09e507f9
- 00c2d2c8 ["INT_ADD", "register:40f0:8", ["const:c2d2c8:8", "const:4:8"]]
- 00c2d2c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2d364 ["INT_ADD", "register:40f0:8", ["const:c2d364:8", "const:4:8"]]
+ 00c2d364 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2d2c8 bytes eaaa0094
+ 00c2d364 bytes f7aa0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfb02daba1d554a50378cf03a33e6ebd"></a>

### [`00c2d2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md) → [`00c2d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md) FUN_00c2d370

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md) · 呼出先 4件 [`00c35e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35e80.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c2d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md) · 呼出先 4件 [`00c35f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35f1c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 70.48% / 新版 70.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 45件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d3a4",
      "incomplete_value": false,
      "site": "00c2d3a4",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d308",
      "incomplete_value": false,
      "site": "00c2d308",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d3bc",
      "incomplete_value": false,
      "site": "00c2d3bc",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d320",
      "incomplete_value": false,
      "site": "00c2d320",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d3f4",
      "incomplete_value": false,
      "site": "00c2d3f4",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d358",
      "incomplete_value": false,
      "site": "00c2d358",
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
            "const:270:8"
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
      "00c2d384",
      "READ",
      [
        "storage",
        "01128498",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d390",
      "READ",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d3a4",
      "WRITE",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2d384",
      "READ",
      [
        "storage",
        "01128598",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d390",
      "READ",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d3a4",
      "WRITE",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d350) · [`00c2d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d3b0) · [`00c2d3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d3d8)
- 新版 `00c2d3ec`（命令位置の公開資料なし） · `00c2d44c`（命令位置の公開資料なし） · `00c2d474`（命令位置の公開資料なし）

~~~diff
- 00c2d350 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00c2d350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c2d350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c2d350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c2d3ec ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00c2d3ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2d3ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2d3ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c2d350 bytes 08c10991
+ 00c2d3ec bytes 08c10d91
- 00c2d3b0 ["COPY", "tmp:0:8", ["const:290:8"]]
- 00c2d3b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c2d3b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c2d3b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c2d44c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00c2d44c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d44c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d44c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c2d3b0 bytes 29410a91
+ 00c2d44c bytes 29410e91
- 00c2d3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 00c2d3d8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00c2d3d8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00c2d474 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 00c2d474 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d474 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00c2d3d8 bytes 08814a39
+ 00c2d474 bytes 08814e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7325422d5bafcf7f9c7508ead64e2ad"></a>

### [`00c2d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md) → [`00c2da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md) _ZNKSt6__ndk120__time_get_c_storageIwE8__monthsEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2da28.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dac4.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2daa0",
      "incomplete_value": true,
      "site": "00c2daa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2da04",
      "incomplete_value": true,
      "site": "00c2da04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2da94",
      "incomplete_value": false,
      "site": "00c2daa0",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d9f8",
      "incomplete_value": false,
      "site": "00c2da04",
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
            "const:4a0:8"
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
      "definition_site": "00c2da80",
      "incomplete_value": true,
      "site": "00c2da84",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d9e4",
      "incomplete_value": true,
      "site": "00c2d9e8",
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
            "const:ee0:8"
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
      "00c2da60",
      "READ",
      [
        "storage",
        "01127ee0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2da68",
      "READ",
      [
        "storage",
        "01127ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2da68",
      "DATA",
      [
        "storage",
        "011284a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2da60",
      "READ",
      [
        "storage",
        "01127fe0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2da68",
      "READ",
      [
        "storage",
        "01127fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2da68",
      "DATA",
      [
        "storage",
        "011285a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2d9e8) · [`00c2d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2d9f0) · [`00c2da04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2da04)
- 新版 `00c2da84`（命令位置の公開資料なし） · `00c2da8c`（命令位置の公開資料なし） · `00c2daa0`（命令位置の公開資料なし）

~~~diff
- 00c2d9e8 ["INT_ADD", "register:40f0:8", ["const:c2d9e8:8", "const:4:8"]]
- 00c2d9e8 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2da84 ["INT_ADD", "register:40f0:8", ["const:c2da84:8", "const:4:8"]]
+ 00c2da84 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2d9e8 bytes 1aa90094
+ 00c2da84 bytes 27a90094
- 00c2d9f0 ["INT_ADD", "register:40f0:8", ["const:c2d9f0:8", "const:4:8"]]
- 00c2d9f0 ["CALL", null, ["ram:c2da28:8"]]
+ 00c2da8c ["INT_ADD", "register:40f0:8", ["const:c2da8c:8", "const:4:8"]]
+ 00c2da8c ["CALL", null, ["ram:c2dac4:8"]]
- 00c2d9f0 bytes 0e000094
+ 00c2da8c bytes 0e000094
- 00c2da04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ed8:8"]]
- 00c2da04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2daa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd8:8"]]
+ 00c2daa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2da04 bytes 686e07f9
+ 00c2daa0 bytes 68ee07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef438733699d93787ca472b1cc735008"></a>

### [`00c2df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) → [`00c2dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2dfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2e058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e048",
      "incomplete_value": true,
      "site": "00c2e048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dfac",
      "incomplete_value": true,
      "site": "00c2dfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e020",
      "incomplete_value": false,
      "site": "00c2e024",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df84",
      "incomplete_value": false,
      "site": "00c2df88",
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
            "const:ef0:8"
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
      "definition_site": "00c2e044",
      "incomplete_value": true,
      "site": "00c2e04c",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dfa8",
      "incomplete_value": true,
      "site": "00c2dfb0",
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
            "const:ef0:8"
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
      "00c2e000",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e00c",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e00c",
      "DATA",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e000",
      "READ",
      [
        "storage",
        "01127ff0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e00c",
      "READ",
      [
        "storage",
        "01127fe8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e00c",
      "DATA",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2df88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2df88) · [`00c2dfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2dfac) · [`00c2dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2dfb0)
- 新版 `00c2e024`（命令位置の公開資料なし） · `00c2e048`（命令位置の公開資料なし） · `00c2e04c`（命令位置の公開資料なし）

~~~diff
- 00c2df88 ["INT_ADD", "register:40f0:8", ["const:c2df88:8", "const:4:8"]]
- 00c2df88 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e024 ["INT_ADD", "register:40f0:8", ["const:c2e024:8", "const:4:8"]]
+ 00c2e024 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2df88 bytes b2a70094
+ 00c2e024 bytes bfa70094
- 00c2dfac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
- 00c2dfac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2e048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe8:8"]]
+ 00c2e048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2dfac bytes 097507f9
+ 00c2e048 bytes 09f507f9
- 00c2dfb0 ["INT_ADD", "register:40f0:8", ["const:c2dfb0:8", "const:4:8"]]
- 00c2dfb0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e04c ["INT_ADD", "register:40f0:8", ["const:c2e04c:8", "const:4:8"]]
+ 00c2e04c ["CALL", null, ["callee:00c57f40:8"]]
- 00c2dfb0 bytes b0a70094
+ 00c2e04c bytes bda70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e2ba19b5349e7c6ea596f10a6686aa4"></a>

### [`00c2dfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md) → [`00c2e058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md) FUN_00c2e058

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) · 呼出先 4件 [`00c35f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35f20.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c2dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md) · 呼出先 4件 [`00c35fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35fbc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e08c",
      "incomplete_value": false,
      "site": "00c2e08c",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dff0",
      "incomplete_value": false,
      "site": "00c2dff0",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e0a4",
      "incomplete_value": false,
      "site": "00c2e0a4",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e008",
      "incomplete_value": false,
      "site": "00c2e008",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e0cc",
      "incomplete_value": false,
      "site": "00c2e0cc",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e030",
      "incomplete_value": false,
      "site": "00c2e030",
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
            "const:700:8"
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
      "00c2e06c",
      "READ",
      [
        "storage",
        "01128718",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e078",
      "READ",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e08c",
      "WRITE",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e06c",
      "READ",
      [
        "storage",
        "01128818",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e078",
      "READ",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e08c",
      "WRITE",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e06c) · [`00c2e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e088) · [`00c2e094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e094)
- 新版 `00c2e108`（命令位置の公開資料なし） · `00c2e124`（命令位置の公開資料なし） · `00c2e130`（命令位置の公開資料なし）

~~~diff
- 00c2e06c ["INT_ADD", "register:40f0:8", ["const:c2e06c:8", "const:4:8"]]
- 00c2e06c ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e108 ["INT_ADD", "register:40f0:8", ["const:c2e108:8", "const:4:8"]]
+ 00c2e108 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e06c bytes 79a70094
+ 00c2e108 bytes 86a70094
- 00c2e088 ["INT_ADD", "register:40f0:8", ["const:c2e088:8", "const:4:8"]]
- 00c2e088 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e124 ["INT_ADD", "register:40f0:8", ["const:c2e124:8", "const:4:8"]]
+ 00c2e124 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e088 bytes 6aa70094
+ 00c2e124 bytes 77a70094
- 00c2e094 ["INT_ADD", "register:40f0:8", ["const:c2e094:8", "const:4:8"]]
- 00c2e094 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e130 ["INT_ADD", "register:40f0:8", ["const:c2e130:8", "const:4:8"]]
+ 00c2e130 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2e094 bytes 77a70094
+ 00c2e130 bytes 84a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1a8e8aa0d4eee7feb728b4c444314d9"></a>

### [`00c2e09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md) → [`00c2e138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__am_pmEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2e108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e194",
      "incomplete_value": false,
      "site": "00c2e194",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e0f8",
      "incomplete_value": false,
      "site": "00c2e0f8",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e184",
      "incomplete_value": false,
      "site": "00c2e194",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e0e8",
      "incomplete_value": false,
      "site": "00c2e0f8",
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
            "const:720:8"
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
      "definition_site": "00c2e16c",
      "incomplete_value": false,
      "site": "00c2e170",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e0d0",
      "incomplete_value": false,
      "site": "00c2e0d4",
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
            "const:f00:8"
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
      "00c2e14c",
      "READ",
      [
        "storage",
        "01127f00",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e158",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e158",
      "DATA",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e14c",
      "READ",
      [
        "storage",
        "01128000",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e158",
      "READ",
      [
        "storage",
        "01127ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e158",
      "DATA",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0d4) · [`00c2e0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0f8) · [`00c2e0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0fc)
- 新版 `00c2e170`（命令位置の公開資料なし） · `00c2e194`（命令位置の公開資料なし） · `00c2e198`（命令位置の公開資料なし）

~~~diff
- 00c2e0d4 ["INT_ADD", "register:40f0:8", ["const:c2e0d4:8", "const:4:8"]]
- 00c2e0d4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e170 ["INT_ADD", "register:40f0:8", ["const:c2e170:8", "const:4:8"]]
+ 00c2e170 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e0d4 bytes 5fa70094
+ 00c2e170 bytes 6ca70094
- 00c2e0f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 00c2e0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2e194 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
+ 00c2e194 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2e0f8 bytes 097d07f9
+ 00c2e194 bytes 09fd07f9
- 00c2e0fc ["INT_ADD", "register:40f0:8", ["const:c2e0fc:8", "const:4:8"]]
- 00c2e0fc ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e198 ["INT_ADD", "register:40f0:8", ["const:c2e198:8", "const:4:8"]]
+ 00c2e198 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2e0fc bytes 5da70094
+ 00c2e198 bytes 6aa70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5f5718402a726ab5170c35126a1c5b"></a>

### [`00c2e108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md) → [`00c2e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md) FUN_00c2e1a4

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2e09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md) · 呼出先 4件 [`00c35f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35f6c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c2e138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md) · 呼出先 4件 [`00c36008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36008.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.93% / 新版 71.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e1d8",
      "incomplete_value": true,
      "site": "00c2e1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e13c",
      "incomplete_value": true,
      "site": "00c2e13c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e1f0",
      "incomplete_value": false,
      "site": "00c2e1f0",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e154",
      "incomplete_value": false,
      "site": "00c2e154",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e21c",
      "incomplete_value": false,
      "site": "00c2e21c",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e180",
      "incomplete_value": false,
      "site": "00c2e180",
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
            "const:738:8"
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
      "00c2e1b8",
      "READ",
      [
        "storage",
        "01128750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e1c4",
      "READ",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e1d8",
      "WRITE",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e1b8",
      "READ",
      [
        "storage",
        "01128850",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e1c4",
      "READ",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e1d8",
      "WRITE",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e148) · [`00c2e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e1bc) · [`00c2e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e1d8)
- 新版 `00c2e1e4`（命令位置の公開資料なし） · `00c2e258`（命令位置の公開資料なし） · `00c2e274`（命令位置の公開資料なし）

~~~diff
- 00c2e148 ["COPY", "tmp:0:8", ["const:728:8"]]
- 00c2e148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c2e148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c2e148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c2e1e4 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00c2e1e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e1e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e1e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c2e148 bytes 08a11c91
+ 00c2e1e4 bytes 08a12091
- 00c2e1bc ["INT_ADD", "register:40f0:8", ["const:c2e1bc:8", "const:4:8"]]
- 00c2e1bc ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e258 ["INT_ADD", "register:40f0:8", ["const:c2e258:8", "const:4:8"]]
+ 00c2e258 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e1bc bytes 25a70094
+ 00c2e258 bytes 32a70094
- 00c2e1d8 ["INT_ADD", "register:40f0:8", ["const:c2e1d8:8", "const:4:8"]]
- 00c2e1d8 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e274 ["INT_ADD", "register:40f0:8", ["const:c2e274:8", "const:4:8"]]
+ 00c2e274 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e1d8 bytes 16a70094
+ 00c2e274 bytes 23a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1519d55f8c6bc951fd97c8dd12a8ca49"></a>

### [`00c2e1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md) → [`00c2e288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e288.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__xEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e2bc",
      "incomplete_value": false,
      "site": "00c2e2c0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e220",
      "incomplete_value": false,
      "site": "00c2e224",
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
            "const:f08:8"
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
      "definition_site": "00c2e2d4",
      "incomplete_value": true,
      "site": "00c2e2e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e238",
      "incomplete_value": true,
      "site": "00c2e244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
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
      "definition_site": "00c2e2d0",
      "incomplete_value": false,
      "site": "00c2e2e0",
      "value": [
        "leaf",
        "const:ca48e0:8"
      ]
    },
    "old": {
      "definition_site": "00c2e234",
      "incomplete_value": false,
      "site": "00c2e244",
      "value": [
        "leaf",
        "const:ca4810:8"
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
      "00c2e29c",
      "READ",
      [
        "storage",
        "01127f08",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e2a8",
      "DATA",
      [
        "storage",
        "00ca4810",
        null,
        null
      ]
    ],
    [
      "00c2e2bc",
      "PARAM",
      [
        "storage",
        "01127f08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e29c",
      "READ",
      [
        "storage",
        "01128008",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e2a8",
      "DATA",
      [
        "storage",
        "00ca48e0",
        null,
        null
      ]
    ],
    [
      "00c2e2bc",
      "PARAM",
      [
        "storage",
        "01128008",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e224) · [`00c2e244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e244) · [`00c2e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e250)
- 新版 `00c2e2c0`（命令位置の公開資料なし） · `00c2e2e0`（命令位置の公開資料なし） · `00c2e2ec`（命令位置の公開資料なし）

~~~diff
- 00c2e224 ["INT_ADD", "register:40f0:8", ["const:c2e224:8", "const:4:8"]]
- 00c2e224 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e2c0 ["INT_ADD", "register:40f0:8", ["const:c2e2c0:8", "const:4:8"]]
+ 00c2e2c0 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e224 bytes 0ba70094
+ 00c2e2c0 bytes 18a70094
- 00c2e244 ["INT_ADD", "register:40f0:8", ["const:c2e244:8", "const:4:8"]]
- 00c2e244 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e2e0 ["INT_ADD", "register:40f0:8", ["const:c2e2e0:8", "const:4:8"]]
+ 00c2e2e0 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e244 bytes fba60094
+ 00c2e2e0 bytes 08a70094
- 00c2e250 ["INT_ADD", "register:40f0:8", ["const:c2e250:8", "const:4:8"]]
- 00c2e250 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e2ec ["INT_ADD", "register:40f0:8", ["const:c2e2ec:8", "const:4:8"]]
+ 00c2e2ec ["CALL", null, ["callee:00c57f40:8"]]
- 00c2e250 bytes 08a70094
+ 00c2e2ec bytes 15a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8962f0fb342fea27513e18dac9c92006"></a>

### [`00c2e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md) → [`00c2e2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__xEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e330",
      "incomplete_value": false,
      "site": "00c2e334",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e294",
      "incomplete_value": false,
      "site": "00c2e298",
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
            "const:f28:8"
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
      "definition_site": "00c2e340",
      "incomplete_value": false,
      "site": "00c2e34c",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e2a4",
      "incomplete_value": false,
      "site": "00c2e2b0",
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
            "const:f10:8"
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
      "definition_site": "00c2e348",
      "incomplete_value": false,
      "site": "00c2e34c",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e2ac",
      "incomplete_value": false,
      "site": "00c2e2b0",
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
            "const:768:8"
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
      "00c2e30c",
      "READ",
      [
        "storage",
        "01127f28",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "01127f10",
        null,
        null
      ]
    ],
    [
      "00c2e330",
      "PARAM",
      [
        "storage",
        "01127f28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e30c",
      "READ",
      [
        "storage",
        "01128028",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "01128010",
        null,
        null
      ]
    ],
    [
      "00c2e330",
      "PARAM",
      [
        "storage",
        "01128028",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e298) · [`00c2e2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e2b0) · [`00c2e2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e2cc)
- 新版 `00c2e334`（命令位置の公開資料なし） · `00c2e34c`（命令位置の公開資料なし） · `00c2e368`（命令位置の公開資料なし）

~~~diff
- 00c2e298 ["INT_ADD", "register:40f0:8", ["const:c2e298:8", "const:4:8"]]
- 00c2e298 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e334 ["INT_ADD", "register:40f0:8", ["const:c2e334:8", "const:4:8"]]
+ 00c2e334 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e298 bytes eea60094
+ 00c2e334 bytes fba60094
- 00c2e2b0 ["INT_ADD", "register:40f0:8", ["const:c2e2b0:8", "const:4:8"]]
- 00c2e2b0 ["CALL", null, ["callee:00c2c130:8"]]
+ 00c2e34c ["INT_ADD", "register:40f0:8", ["const:c2e34c:8", "const:4:8"]]
+ 00c2e34c ["CALL", null, ["callee:00c2c130:8"]]
- 00c2e2b0 bytes 79f7ff97
+ 00c2e34c bytes 79f7ff97
- 00c2e2cc ["INT_ADD", "register:40f0:8", ["const:c2e2cc:8", "const:4:8"]]
- 00c2e2cc ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e368 ["INT_ADD", "register:40f0:8", ["const:c2e368:8", "const:4:8"]]
+ 00c2e368 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e2cc bytes d9a60094
+ 00c2e368 bytes e6a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e0eec12c7140ffe8dabcffd59674f5"></a>

### [`00c2e2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md) → [`00c2e394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e394.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__XEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e3c8",
      "incomplete_value": false,
      "site": "00c2e3cc",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e32c",
      "incomplete_value": false,
      "site": "00c2e330",
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
            "const:f30:8"
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
      "definition_site": "00c2e3e0",
      "incomplete_value": true,
      "site": "00c2e3ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e344",
      "incomplete_value": true,
      "site": "00c2e350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
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
      "definition_site": "00c2e3dc",
      "incomplete_value": false,
      "site": "00c2e3ec",
      "value": [
        "leaf",
        "const:ca48f8:8"
      ]
    },
    "old": {
      "definition_site": "00c2e340",
      "incomplete_value": false,
      "site": "00c2e350",
      "value": [
        "leaf",
        "const:ca4828:8"
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
      "00c2e3a8",
      "READ",
      [
        "storage",
        "01127f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e3b4",
      "DATA",
      [
        "storage",
        "00ca4828",
        null,
        null
      ]
    ],
    [
      "00c2e3c8",
      "PARAM",
      [
        "storage",
        "01127f30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e3a8",
      "READ",
      [
        "storage",
        "01128030",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e3b4",
      "DATA",
      [
        "storage",
        "00ca48f8",
        null,
        null
      ]
    ],
    [
      "00c2e3c8",
      "PARAM",
      [
        "storage",
        "01128030",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e330) · [`00c2e350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e350) · [`00c2e35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e35c)
- 新版 `00c2e3cc`（命令位置の公開資料なし） · `00c2e3ec`（命令位置の公開資料なし） · `00c2e3f8`（命令位置の公開資料なし）

~~~diff
- 00c2e330 ["INT_ADD", "register:40f0:8", ["const:c2e330:8", "const:4:8"]]
- 00c2e330 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e3cc ["INT_ADD", "register:40f0:8", ["const:c2e3cc:8", "const:4:8"]]
+ 00c2e3cc ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e330 bytes c8a60094
+ 00c2e3cc bytes d5a60094
- 00c2e350 ["INT_ADD", "register:40f0:8", ["const:c2e350:8", "const:4:8"]]
- 00c2e350 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e3ec ["INT_ADD", "register:40f0:8", ["const:c2e3ec:8", "const:4:8"]]
+ 00c2e3ec ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e350 bytes b8a60094
+ 00c2e3ec bytes c5a60094
- 00c2e35c ["INT_ADD", "register:40f0:8", ["const:c2e35c:8", "const:4:8"]]
- 00c2e35c ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e3f8 ["INT_ADD", "register:40f0:8", ["const:c2e3f8:8", "const:4:8"]]
+ 00c2e3f8 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2e35c bytes c5a60094
+ 00c2e3f8 bytes d2a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7739c54b875542a28bf80527a8458ee9"></a>

### [`00c2e364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md) → [`00c2e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__XEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e43c",
      "incomplete_value": false,
      "site": "00c2e440",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3a0",
      "incomplete_value": false,
      "site": "00c2e3a4",
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
            "const:f50:8"
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
      "definition_site": "00c2e44c",
      "incomplete_value": false,
      "site": "00c2e458",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3b0",
      "incomplete_value": false,
      "site": "00c2e3bc",
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
            "const:f38:8"
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
      "definition_site": "00c2e454",
      "incomplete_value": false,
      "site": "00c2e458",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3b8",
      "incomplete_value": false,
      "site": "00c2e3bc",
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
            "const:5d8:8"
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
      "00c2e418",
      "READ",
      [
        "storage",
        "01127f50",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e424",
      "DATA",
      [
        "storage",
        "01127f38",
        null,
        null
      ]
    ],
    [
      "00c2e43c",
      "PARAM",
      [
        "storage",
        "01127f50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e418",
      "READ",
      [
        "storage",
        "01128050",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e424",
      "DATA",
      [
        "storage",
        "01128038",
        null,
        null
      ]
    ],
    [
      "00c2e43c",
      "PARAM",
      [
        "storage",
        "01128050",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3a4) · [`00c2e3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3bc) · [`00c2e3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3d8)
- 新版 `00c2e440`（命令位置の公開資料なし） · `00c2e458`（命令位置の公開資料なし） · `00c2e474`（命令位置の公開資料なし）

~~~diff
- 00c2e3a4 ["INT_ADD", "register:40f0:8", ["const:c2e3a4:8", "const:4:8"]]
- 00c2e3a4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e440 ["INT_ADD", "register:40f0:8", ["const:c2e440:8", "const:4:8"]]
+ 00c2e440 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e3a4 bytes aba60094
+ 00c2e440 bytes b8a60094
- 00c2e3bc ["INT_ADD", "register:40f0:8", ["const:c2e3bc:8", "const:4:8"]]
- 00c2e3bc ["CALL", null, ["callee:00c2c130:8"]]
+ 00c2e458 ["INT_ADD", "register:40f0:8", ["const:c2e458:8", "const:4:8"]]
+ 00c2e458 ["CALL", null, ["callee:00c2c130:8"]]
- 00c2e3bc bytes 36f7ff97
+ 00c2e458 bytes 36f7ff97
- 00c2e3d8 ["INT_ADD", "register:40f0:8", ["const:c2e3d8:8", "const:4:8"]]
- 00c2e3d8 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e474 ["INT_ADD", "register:40f0:8", ["const:c2e474:8", "const:4:8"]]
+ 00c2e474 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e3d8 bytes 96a60094
+ 00c2e474 bytes a3a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a040cc9724ff5b6bbc6fd0d9d6ff59a4"></a>

### [`00c2e404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md) → [`00c2e4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e4a0.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e4d4",
      "incomplete_value": false,
      "site": "00c2e4d8",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e438",
      "incomplete_value": false,
      "site": "00c2e43c",
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
            "const:f58:8"
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
      "definition_site": "00c2e4ec",
      "incomplete_value": true,
      "site": "00c2e4f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e450",
      "incomplete_value": true,
      "site": "00c2e45c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
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
      "definition_site": "00c2e4e8",
      "incomplete_value": false,
      "site": "00c2e4f8",
      "value": [
        "leaf",
        "const:ca4910:8"
      ]
    },
    "old": {
      "definition_site": "00c2e44c",
      "incomplete_value": false,
      "site": "00c2e45c",
      "value": [
        "leaf",
        "const:ca4840:8"
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
      "00c2e4b4",
      "READ",
      [
        "storage",
        "01127f58",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e4c0",
      "DATA",
      [
        "storage",
        "00ca4840",
        null,
        "string"
      ]
    ],
    [
      "00c2e4d4",
      "PARAM",
      [
        "storage",
        "01127f58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e4b4",
      "READ",
      [
        "storage",
        "01128058",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e4c0",
      "DATA",
      [
        "storage",
        "00ca4910",
        null,
        "string"
      ]
    ],
    [
      "00c2e4d4",
      "PARAM",
      [
        "storage",
        "01128058",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e43c) · [`00c2e45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e45c) · [`00c2e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e410)
- 新版 `00c2e4d8`（命令位置の公開資料なし） · `00c2e4f8`（命令位置の公開資料なし） · `00c2e4ac`（命令位置の公開資料なし）

~~~diff
- 00c2e43c ["INT_ADD", "register:40f0:8", ["const:c2e43c:8", "const:4:8"]]
- 00c2e43c ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e4d8 ["INT_ADD", "register:40f0:8", ["const:c2e4d8:8", "const:4:8"]]
+ 00c2e4d8 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e43c bytes 85a60094
+ 00c2e4d8 bytes 92a60094
- 00c2e45c ["INT_ADD", "register:40f0:8", ["const:c2e45c:8", "const:4:8"]]
- 00c2e45c ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e4f8 ["INT_ADD", "register:40f0:8", ["const:c2e4f8:8", "const:4:8"]]
+ 00c2e4f8 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e45c bytes 75a60094
+ 00c2e4f8 bytes 82a60094
- 00c2e410 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00c2e4ac ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00c2e410 bytes c82700b0
+ 00c2e4ac bytes c82700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7dea4650008249f86f410e9bf1f7ca3"></a>

### [`00c2e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md) → [`00c2e50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__cEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e548",
      "incomplete_value": false,
      "site": "00c2e54c",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e4ac",
      "incomplete_value": false,
      "site": "00c2e4b0",
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
            "const:f78:8"
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
      "definition_site": "00c2e558",
      "incomplete_value": false,
      "site": "00c2e564",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e4bc",
      "incomplete_value": false,
      "site": "00c2e4c8",
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
            "const:f60:8"
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
      "definition_site": "00c2e560",
      "incomplete_value": false,
      "site": "00c2e564",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e4c4",
      "incomplete_value": false,
      "site": "00c2e4c8",
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
            "const:658:8"
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
      "00c2e524",
      "READ",
      [
        "storage",
        "01127f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e530",
      "DATA",
      [
        "storage",
        "01127f60",
        null,
        null
      ]
    ],
    [
      "00c2e548",
      "PARAM",
      [
        "storage",
        "01127f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e524",
      "READ",
      [
        "storage",
        "01128078",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e530",
      "DATA",
      [
        "storage",
        "01128060",
        null,
        null
      ]
    ],
    [
      "00c2e548",
      "PARAM",
      [
        "storage",
        "01128078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4b0) · [`00c2e4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4c8) · [`00c2e4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4e4)
- 新版 `00c2e54c`（命令位置の公開資料なし） · `00c2e564`（命令位置の公開資料なし） · `00c2e580`（命令位置の公開資料なし）

~~~diff
- 00c2e4b0 ["INT_ADD", "register:40f0:8", ["const:c2e4b0:8", "const:4:8"]]
- 00c2e4b0 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e54c ["INT_ADD", "register:40f0:8", ["const:c2e54c:8", "const:4:8"]]
+ 00c2e54c ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e4b0 bytes 68a60094
+ 00c2e54c bytes 75a60094
- 00c2e4c8 ["INT_ADD", "register:40f0:8", ["const:c2e4c8:8", "const:4:8"]]
- 00c2e4c8 ["CALL", null, ["callee:00c2c130:8"]]
+ 00c2e564 ["INT_ADD", "register:40f0:8", ["const:c2e564:8", "const:4:8"]]
+ 00c2e564 ["CALL", null, ["callee:00c2c130:8"]]
- 00c2e4c8 bytes f3f6ff97
+ 00c2e564 bytes f3f6ff97
- 00c2e4e4 ["INT_ADD", "register:40f0:8", ["const:c2e4e4:8", "const:4:8"]]
- 00c2e4e4 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e580 ["INT_ADD", "register:40f0:8", ["const:c2e580:8", "const:4:8"]]
+ 00c2e580 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e4e4 bytes 53a60094
+ 00c2e580 bytes 60a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aca26e83f4df5f511366b541227a968"></a>

### [`00c2e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md) → [`00c2e5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e5ac.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__rEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e5e0",
      "incomplete_value": false,
      "site": "00c2e5e4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e544",
      "incomplete_value": false,
      "site": "00c2e548",
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
            "const:f80:8"
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
      "definition_site": "00c2e5f8",
      "incomplete_value": true,
      "site": "00c2e604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e55c",
      "incomplete_value": true,
      "site": "00c2e568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
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
      "definition_site": "00c2e5f4",
      "incomplete_value": false,
      "site": "00c2e604",
      "value": [
        "leaf",
        "const:ca4928:8"
      ]
    },
    "old": {
      "definition_site": "00c2e558",
      "incomplete_value": false,
      "site": "00c2e568",
      "value": [
        "leaf",
        "const:ca4858:8"
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
      "00c2e5c0",
      "READ",
      [
        "storage",
        "01127f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e5cc",
      "DATA",
      [
        "storage",
        "00ca4858",
        null,
        null
      ]
    ],
    [
      "00c2e5e0",
      "PARAM",
      [
        "storage",
        "01127f80",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e5c0",
      "READ",
      [
        "storage",
        "01128080",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e5cc",
      "DATA",
      [
        "storage",
        "00ca4928",
        null,
        null
      ]
    ],
    [
      "00c2e5e0",
      "PARAM",
      [
        "storage",
        "01128080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e548) · [`00c2e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e568) · [`00c2e574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e574)
- 新版 `00c2e5e4`（命令位置の公開資料なし） · `00c2e604`（命令位置の公開資料なし） · `00c2e610`（命令位置の公開資料なし）

~~~diff
- 00c2e548 ["INT_ADD", "register:40f0:8", ["const:c2e548:8", "const:4:8"]]
- 00c2e548 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e5e4 ["INT_ADD", "register:40f0:8", ["const:c2e5e4:8", "const:4:8"]]
+ 00c2e5e4 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e548 bytes 42a60094
+ 00c2e5e4 bytes 4fa60094
- 00c2e568 ["INT_ADD", "register:40f0:8", ["const:c2e568:8", "const:4:8"]]
- 00c2e568 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e604 ["INT_ADD", "register:40f0:8", ["const:c2e604:8", "const:4:8"]]
+ 00c2e604 ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e568 bytes 32a60094
+ 00c2e604 bytes 3fa60094
- 00c2e574 ["INT_ADD", "register:40f0:8", ["const:c2e574:8", "const:4:8"]]
- 00c2e574 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2e610 ["INT_ADD", "register:40f0:8", ["const:c2e610:8", "const:4:8"]]
+ 00c2e610 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2e574 bytes 3fa60094
+ 00c2e610 bytes 4ca60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d070d7c3fd754685cbcd0e2e0cab8a"></a>

### [`00c2e57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md) → [`00c2e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__rEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e654",
      "incomplete_value": false,
      "site": "00c2e658",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e5b8",
      "incomplete_value": false,
      "site": "00c2e5bc",
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
            "const:fa0:8"
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
      "definition_site": "00c2e664",
      "incomplete_value": false,
      "site": "00c2e670",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e5c8",
      "incomplete_value": false,
      "site": "00c2e5d4",
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
            "const:f88:8"
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
      "definition_site": "00c2e66c",
      "incomplete_value": false,
      "site": "00c2e670",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e5d0",
      "incomplete_value": false,
      "site": "00c2e5d4",
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
            "const:500:8"
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
      "00c2e630",
      "READ",
      [
        "storage",
        "01127fa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e63c",
      "DATA",
      [
        "storage",
        "01127f88",
        null,
        null
      ]
    ],
    [
      "00c2e654",
      "PARAM",
      [
        "storage",
        "01127fa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e630",
      "READ",
      [
        "storage",
        "011280a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e63c",
      "DATA",
      [
        "storage",
        "01128088",
        null,
        null
      ]
    ],
    [
      "00c2e654",
      "PARAM",
      [
        "storage",
        "011280a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5bc) · [`00c2e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5d4) · [`00c2e5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5f0)
- 新版 `00c2e658`（命令位置の公開資料なし） · `00c2e670`（命令位置の公開資料なし） · `00c2e68c`（命令位置の公開資料なし）

~~~diff
- 00c2e5bc ["INT_ADD", "register:40f0:8", ["const:c2e5bc:8", "const:4:8"]]
- 00c2e5bc ["CALL", null, ["callee:00c57f20:8"]]
+ 00c2e658 ["INT_ADD", "register:40f0:8", ["const:c2e658:8", "const:4:8"]]
+ 00c2e658 ["CALL", null, ["callee:00c57f20:8"]]
- 00c2e5bc bytes 25a60094
+ 00c2e658 bytes 32a60094
- 00c2e5d4 ["INT_ADD", "register:40f0:8", ["const:c2e5d4:8", "const:4:8"]]
- 00c2e5d4 ["CALL", null, ["callee:00c2c130:8"]]
+ 00c2e670 ["INT_ADD", "register:40f0:8", ["const:c2e670:8", "const:4:8"]]
+ 00c2e670 ["CALL", null, ["callee:00c2c130:8"]]
- 00c2e5d4 bytes b0f6ff97
+ 00c2e670 bytes b0f6ff97
- 00c2e5f0 ["INT_ADD", "register:40f0:8", ["const:c2e5f0:8", "const:4:8"]]
- 00c2e5f0 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c2e68c ["INT_ADD", "register:40f0:8", ["const:c2e68c:8", "const:4:8"]]
+ 00c2e68c ["CALL", null, ["callee:00c57f00:8"]]
- 00c2e5f0 bytes 10a60094
+ 00c2e68c bytes 1da60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da6096948d691317429de20fd0f66666"></a>

### [`00c2e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md) → [`00c2e6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e6b8.md) _ZNSt6__ndk110__time_getC1EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5eca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eca0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 1件 [`00c5ed70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed70.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e70c",
      "incomplete_value": false,
      "site": "00c2e71c",
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
            "const:12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e670",
      "incomplete_value": false,
      "site": "00c2e680",
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
            "const:fd2:8"
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
      "00c2e70c",
      "PARAM",
      [
        "storage",
        "002b6fd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2e70c",
      "PARAM",
      [
        "storage",
        "002b7012",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e680) · [`00c2e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e640) · [`00c2e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e668)
- 新版 `00c2e71c`（命令位置の公開資料なし） · `00c2e6dc`（命令位置の公開資料なし） · `00c2e704`（命令位置の公開資料なし）

~~~diff
- 00c2e680 ["INT_ADD", "register:40f0:8", ["const:c2e680:8", "const:4:8"]]
- 00c2e680 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c2e71c ["INT_ADD", "register:40f0:8", ["const:c2e71c:8", "const:4:8"]]
+ 00c2e71c ["CALL", null, ["callee:00c259d0:8"]]
- 00c2e680 bytes addcff97
+ 00c2e71c bytes addcff97
- 00c2e640 ["INT_ADD", "register:40f0:8", ["const:c2e640:8", "const:4:8"]]
- 00c2e640 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c2e6dc ["INT_ADD", "register:40f0:8", ["const:c2e6dc:8", "const:4:8"]]
+ 00c2e6dc ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c2e640 bytes f8ba0094
+ 00c2e6dc bytes 05bb0094
- 00c2e668 ["INT_ADD", "register:40f0:8", ["const:c2e668:8", "const:4:8"]]
- 00c2e668 ["CALL", null, ["callee:0043de18:8"]]
+ 00c2e704 ["INT_ADD", "register:40f0:8", ["const:c2e704:8", "const:4:8"]]
+ 00c2e704 ["CALL", null, ["callee:0043de18:8"]]
- 00c2e668 bytes dc3de097
+ 00c2e704 bytes c53de097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd76dd3cc6b31c11ef3d618554dbbbe0"></a>

### [`00c2e6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md) → [`00c2e780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e780.md) _ZNSt6__ndk110__time_getC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecb0.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed80.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e7d8",
      "incomplete_value": false,
      "site": "00c2e7e8",
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
            "const:12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e73c",
      "incomplete_value": false,
      "site": "00c2e74c",
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
            "const:fd2:8"
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
      "00c2e7d8",
      "PARAM",
      [
        "storage",
        "002b6fd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2e7d8",
      "PARAM",
      [
        "storage",
        "002b7012",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e74c) · [`00c2e718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e718) · [`00c2e738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e738)
- 新版 `00c2e7e8`（命令位置の公開資料なし） · `00c2e7b4`（命令位置の公開資料なし） · `00c2e7d4`（命令位置の公開資料なし）

~~~diff
- 00c2e74c ["INT_ADD", "register:40f0:8", ["const:c2e74c:8", "const:4:8"]]
- 00c2e74c ["CALL", null, ["callee:00c58180:8"]]
+ 00c2e7e8 ["INT_ADD", "register:40f0:8", ["const:c2e7e8:8", "const:4:8"]]
+ 00c2e7e8 ["CALL", null, ["callee:00c58180:8"]]
- 00c2e74c bytes 59a60094
+ 00c2e7e8 bytes 66a60094
- 00c2e718 ["INT_ADD", "register:40f0:8", ["const:c2e718:8", "const:4:8"]]
- 00c2e718 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c2e7b4 ["INT_ADD", "register:40f0:8", ["const:c2e7b4:8", "const:4:8"]]
+ 00c2e7b4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c2e718 bytes c2ba0094
+ 00c2e7b4 bytes cfba0094
- 00c2e738 ["COPY", "register:4000:8", ["const:2b6000:8"]]
+ 00c2e7d4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00c2e738 bytes 40b4ff90
+ 00c2e7d4 bytes 40b4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a7a8fd33c00fff0374e129ef63ae5d"></a>

### [`00c2e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md) → [`00c2e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md) _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecd0.md) · 呼出先 3件 [`00c2ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md) [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c5eda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eda0.md) · 呼出先 3件 [`00c2ee28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md) [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e870",
      "incomplete_value": true,
      "site": "00c2e888",
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
                "const:2c2000:8"
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
      "definition_site": "00c2e7d4",
      "incomplete_value": true,
      "site": "00c2e7ec",
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
                "const:2c2000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e88c",
      "incomplete_value": true,
      "site": "00c2e8a0",
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
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e7f0",
      "incomplete_value": true,
      "site": "00c2e804",
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
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2e870",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00c2e88c",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2e870",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ],
    [
      "00c2e88c",
      "READ",
      [
        "storage",
        "002c2c20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e7d4) · [`00c2e7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e7f0) · [`00c2e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e82c)
- 新版 `00c2e870`（命令位置の公開資料なし） · `00c2e88c`（命令位置の公開資料なし） · `00c2e8c8`（命令位置の公開資料なし）

~~~diff
- 00c2e7d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d0:8"]]
- 00c2e7d4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e7d4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e7d4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2e870 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:710:8"]]
+ 00c2e870 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2e870 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2e870 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e7d4 bytes 20b5c13d
+ 00c2e870 bytes 20c5c13d
- 00c2e7f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
- 00c2e7f0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e7f0 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e7f0 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2e88c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
+ 00c2e88c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2e88c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2e88c ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e7f0 bytes 20f9c23d
+ 00c2e88c bytes 2009c33d
- 00c2e82c ["INT_ADD", "register:40f0:8", ["const:c2e82c:8", "const:4:8"]]
- 00c2e82c ["CALL", null, ["callee:00c5e730:8"]]
+ 00c2e8c8 ["INT_ADD", "register:40f0:8", ["const:c2e8c8:8", "const:4:8"]]
+ 00c2e8c8 ["CALL", null, ["callee:00c5e730:8"]]
- 00c2e82c bytes 8dbf0094
+ 00c2e8c8 bytes 9abf0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbdb4f8cd05e287e1b88c73bde4bbef"></a>

### [`00c2f09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md) → [`00c2f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md) _ZNSt6__ndk118__time_get_storageIwE9__analyzeEcRKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ece0.md) · 呼出先 8件 [`00c30744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5edb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edb0.md) · 呼出先 8件 [`00c307e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2f168",
      "incomplete_value": true,
      "site": "00c2f1b0",
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
                "const:2c2000:8"
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
      "definition_site": "00c2f0cc",
      "incomplete_value": true,
      "site": "00c2f114",
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
                "const:2c2000:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2f174",
      "incomplete_value": true,
      "site": "00c2f1b0",
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
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2f0d8",
      "incomplete_value": true,
      "site": "00c2f114",
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
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
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
      "definition_site": "00c3078c",
      "incomplete_value": false,
      "site": "00c30790",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c306f0",
      "incomplete_value": false,
      "site": "00c306f4",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2f168",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00c2f174",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ],
    [
      "00c3078c",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2f168",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ],
    [
      "00c2f174",
      "READ",
      [
        "storage",
        "002c2c20",
        null,
        null
      ]
    ],
    [
      "00c3078c",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c306f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md#insn-00c306f4) · [`00c2f0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md#insn-00c2f0cc) · [`00c2f0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md#insn-00c2f0d0)
- 新版 `00c30790`（命令位置の公開資料なし） · `00c2f168`（命令位置の公開資料なし）

~~~diff
- 00c306f4 ["INT_ADD", "register:40f0:8", ["const:c306f4:8", "const:4:8"]]
- 00c306f4 ["CALL", null, ["callee:00c5e080:8"]]
+ 00c30790 ["INT_ADD", "register:40f0:8", ["const:c30790:8", "const:4:8"]]
+ 00c30790 ["CALL", null, ["callee:00c5e080:8"]]
- 00c306f4 bytes 2fb60094
+ 00c30790 bytes 3cb60094
- 00c2f0cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6d0:8"]]
- 00c2f0cc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2f0cc ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2f0cc ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2f168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:710:8"]]
+ 00c2f168 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2f168 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2f168 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2f0cc bytes 00b5c13d
+ 00c2f168 bytes 00c5c13d
- 00c2f0d0 ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 00c2f0d0 bytes 88b4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c359bf492be11832946504d3bc61bd5"></a>

### [`00c30ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md) → [`00c30d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30d84.md) _ZNSt6__ndk118__time_get_storageIwE4initERKNS_5ctypeIwEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed00.md) · 呼出先 8件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md)
- 新版 呼出元 1件 [`00c5edd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edd0.md) · 呼出先 8件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md) [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c30e0c",
      "incomplete_value": false,
      "site": "00c30e14",
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
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30d70",
      "incomplete_value": false,
      "site": "00c30d78",
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
            "const:801:8"
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
      "definition_site": "00c30f6c",
      "incomplete_value": false,
      "site": "00c30f70",
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
            "const:4c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30ed0",
      "incomplete_value": false,
      "site": "00c30ed4",
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
            "const:51d:8"
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
      "definition_site": "00c31254",
      "incomplete_value": false,
      "site": "00c31258",
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
            "const:dcd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c311b8",
      "incomplete_value": false,
      "site": "00c311bc",
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
            "const:e1a:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c30e0c",
      "PARAM",
      [
        "storage",
        "002b2801",
        null,
        null
      ]
    ],
    [
      "00c30f6c",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ],
    [
      "00c310f4",
      "PARAM",
      [
        "storage",
        "002af747",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c30e0c",
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        null
      ]
    ],
    [
      "00c30f6c",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ],
    [
      "00c310f4",
      "PARAM",
      [
        "storage",
        "002af6eb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c30d78) · [`00c30ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c30ed4) · [`00c311bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c311bc)
- 新版 `00c30e14`（命令位置の公開資料なし） · `00c30f70`（命令位置の公開資料なし） · `00c31258`（命令位置の公開資料なし）

~~~diff
- 00c30d78 ["INT_ADD", "register:40f0:8", ["const:c30d78:8", "const:4:8"]]
- 00c30d78 ["CALL", null, ["callee:00c5e730:8"]]
+ 00c30e14 ["INT_ADD", "register:40f0:8", ["const:c30e14:8", "const:4:8"]]
+ 00c30e14 ["CALL", null, ["callee:00c5e730:8"]]
- 00c30d78 bytes 3ab60094
+ 00c30e14 bytes 47b60094
- 00c30ed4 ["INT_ADD", "register:40f0:8", ["const:c30ed4:8", "const:4:8"]]
- 00c30ed4 ["CALL", null, ["callee:00c5e730:8"]]
+ 00c30f70 ["INT_ADD", "register:40f0:8", ["const:c30f70:8", "const:4:8"]]
+ 00c30f70 ["CALL", null, ["callee:00c5e730:8"]]
- 00c30ed4 bytes e3b50094
+ 00c30f70 bytes f0b50094
- 00c311bc ["INT_ADD", "register:40f0:8", ["const:c311bc:8", "const:4:8"]]
- 00c311bc ["CALL", null, ["callee:00c5e730:8"]]
+ 00c31258 ["INT_ADD", "register:40f0:8", ["const:c31258:8", "const:4:8"]]
+ 00c31258 ["CALL", null, ["callee:00c5e730:8"]]
- 00c311bc bytes 29b50094
+ 00c31258 bytes 36b50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0e7bed7179a437368ccb5dc2c07c44"></a>

### [`00c31760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md) → [`00c317fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c317fc.md) _ZNSt6__ndk118__time_get_storageIcEC1EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31844",
      "incomplete_value": false,
      "site": "00c31848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c317a8",
      "incomplete_value": false,
      "site": "00c317ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31864",
      "incomplete_value": true,
      "site": "00c31868",
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
      "definition_site": "00c317c8",
      "incomplete_value": true,
      "site": "00c317cc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3187c",
      "incomplete_value": true,
      "site": "00c31880",
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
      "definition_site": "00c317e0",
      "incomplete_value": true,
      "site": "00c317e4",
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
      "00c31848",
      "DATA",
      [
        "storage",
        "00c95ca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3185c",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31868",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c31848",
      "DATA",
      [
        "storage",
        "00c95d70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3185c",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31868",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c31780) · [`00c31790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c31790) · [`00c317a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c317a0)
- 新版 `00c3181c`（命令位置の公開資料なし） · `00c3182c`（命令位置の公開資料なし） · `00c3183c`（命令位置の公開資料なし）

~~~diff
- 00c31780 ["INT_ADD", "register:40f0:8", ["const:c31780:8", "const:4:8"]]
- 00c31780 ["CALL", null, ["callee:00c5ed70:8"]]
+ 00c3181c ["INT_ADD", "register:40f0:8", ["const:c3181c:8", "const:4:8"]]
+ 00c3181c ["CALL", null, ["callee:00c5ed70:8"]]
- 00c31780 bytes 48b50094
+ 00c3181c bytes 55b50094
- 00c31790 ["INT_ADD", "register:40f0:8", ["const:c31790:8", "const:4:8"]]
- 00c31790 ["CALL", null, ["callee:00c58160:8"]]
+ 00c3182c ["INT_ADD", "register:40f0:8", ["const:c3182c:8", "const:4:8"]]
+ 00c3182c ["CALL", null, ["callee:00c58160:8"]]
- 00c31790 bytes 409a0094
+ 00c3182c bytes 4d9a0094
- 00c317a0 ["INT_ADD", "register:40f0:8", ["const:c317a0:8", "const:4:8"]]
- 00c317a0 ["CALL", null, ["callee:00c5ea90:8"]]
+ 00c3183c ["INT_ADD", "register:40f0:8", ["const:c3183c:8", "const:4:8"]]
+ 00c3183c ["CALL", null, ["callee:00c5ea90:8"]]
- 00c317a0 bytes 88b40094
+ 00c3183c bytes 95b40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b64f25232d7f41515c8d0bda66dcf9a"></a>

### [`00c31a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md) → [`00c31adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31adc.md) _ZNSt6__ndk112ctype_bynameIcED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9e0.md) [`00c5ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed10.md) · 呼出先 3件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 2件 [`00c5eab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eab0.md) [`00c5ede0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ede0.md) · 呼出先 3件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31afc",
      "incomplete_value": true,
      "site": "00c31b00",
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
      "definition_site": "00c31a60",
      "incomplete_value": true,
      "site": "00c31a64",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31b14",
      "incomplete_value": true,
      "site": "00c31b18",
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
      "definition_site": "00c31a78",
      "incomplete_value": true,
      "site": "00c31a7c",
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
      "00c31af4",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31b00",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c31b0c",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c31af4",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31b00",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c31b0c",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a58) · [`00c31a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a68) · [`00c31a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a70)
- 新版 `00c31af4`（命令位置の公開資料なし） · `00c31b04`（命令位置の公開資料なし） · `00c31b0c`（命令位置の公開資料なし）

~~~diff
- 00c31a58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00c31a58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c31af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c31af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c31a58 bytes 08e946f9
+ 00c31af4 bytes 085147f9
- 00c31a68 ["INT_ADD", "register:40f0:8", ["const:c31a68:8", "const:4:8"]]
- 00c31a68 ["CALL", null, ["callee:00c5d2a0:8"]]
+ 00c31b04 ["INT_ADD", "register:40f0:8", ["const:c31b04:8", "const:4:8"]]
+ 00c31b04 ["CALL", null, ["callee:00c5d2a0:8"]]
- 00c31a68 bytes daad0094
+ 00c31b04 bytes e7ad0094
- 00c31a70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
- 00c31a70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c31b0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00c31b0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c31a70 bytes 08e546f9
+ 00c31b0c bytes 084d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5625ab0432ef76f43c4ae1d0f71a3413"></a>

### [`00c31aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md) → [`00c31b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31b44.md) _ZNSt6__ndk118__time_get_storageIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e890.md) · 呼出先 7件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9d0.md)
- 新版 呼出元 1件 [`00c5e960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e960.md) · 呼出先 7件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eaa0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31b8c",
      "incomplete_value": false,
      "site": "00c31b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31af0",
      "incomplete_value": false,
      "site": "00c31af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31bac",
      "incomplete_value": true,
      "site": "00c31bb0",
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
      "definition_site": "00c31b10",
      "incomplete_value": true,
      "site": "00c31b14",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31bc4",
      "incomplete_value": true,
      "site": "00c31bc8",
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
      "definition_site": "00c31b28",
      "incomplete_value": true,
      "site": "00c31b2c",
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
      "00c31b90",
      "DATA",
      [
        "storage",
        "00c95ca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31ba4",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31bb0",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c31b90",
      "DATA",
      [
        "storage",
        "00c95d70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31ba4",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31bb0",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ac8) · [`00c31ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ad8) · [`00c31ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ae8)
- 新版 `00c31b64`（命令位置の公開資料なし） · `00c31b74`（命令位置の公開資料なし） · `00c31b84`（命令位置の公開資料なし）

~~~diff
- 00c31ac8 ["INT_ADD", "register:40f0:8", ["const:c31ac8:8", "const:4:8"]]
- 00c31ac8 ["CALL", null, ["callee:00c5ed80:8"]]
+ 00c31b64 ["INT_ADD", "register:40f0:8", ["const:c31b64:8", "const:4:8"]]
+ 00c31b64 ["CALL", null, ["callee:00c5ed80:8"]]
- 00c31ac8 bytes 7ab40094
+ 00c31b64 bytes 87b40094
- 00c31ad8 ["INT_ADD", "register:40f0:8", ["const:c31ad8:8", "const:4:8"]]
- 00c31ad8 ["CALL", null, ["callee:00c58160:8"]]
+ 00c31b74 ["INT_ADD", "register:40f0:8", ["const:c31b74:8", "const:4:8"]]
+ 00c31b74 ["CALL", null, ["callee:00c58160:8"]]
- 00c31ad8 bytes 6e990094
+ 00c31b74 bytes 7b990094
- 00c31ae8 ["INT_ADD", "register:40f0:8", ["const:c31ae8:8", "const:4:8"]]
- 00c31ae8 ["CALL", null, ["callee:00c5eaa0:8"]]
+ 00c31b84 ["INT_ADD", "register:40f0:8", ["const:c31b84:8", "const:4:8"]]
+ 00c31b84 ["CALL", null, ["callee:00c5eaa0:8"]]
- 00c31ae8 bytes bab30094
+ 00c31b84 bytes c7b30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c1e951dac2a4e0bcd765b9a152a4340"></a>

### [`00c31d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md) → [`00c31e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31e24.md) _ZNSt6__ndk118__time_get_storageIwEC1EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9f0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md) [`00c5eca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eca0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5eac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eac0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md) [`00c5ed70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31e6c",
      "incomplete_value": false,
      "site": "00c31e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31dd0",
      "incomplete_value": false,
      "site": "00c31dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31e8c",
      "incomplete_value": true,
      "site": "00c31e90",
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
      "definition_site": "00c31df0",
      "incomplete_value": true,
      "site": "00c31df4",
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
      "00c31e70",
      "DATA",
      [
        "storage",
        "00c95d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31e84",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c31e90",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c31e70",
      "DATA",
      [
        "storage",
        "00c95df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31e84",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c31e90",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31da8) · [`00c31db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31db8) · [`00c31dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31dc8)
- 新版 `00c31e44`（命令位置の公開資料なし） · `00c31e54`（命令位置の公開資料なし） · `00c31e64`（命令位置の公開資料なし）

~~~diff
- 00c31da8 ["INT_ADD", "register:40f0:8", ["const:c31da8:8", "const:4:8"]]
- 00c31da8 ["CALL", null, ["callee:00c5ed70:8"]]
+ 00c31e44 ["INT_ADD", "register:40f0:8", ["const:c31e44:8", "const:4:8"]]
+ 00c31e44 ["CALL", null, ["callee:00c5ed70:8"]]
- 00c31da8 bytes beb30094
+ 00c31e44 bytes cbb30094
- 00c31db8 ["INT_ADD", "register:40f0:8", ["const:c31db8:8", "const:4:8"]]
- 00c31db8 ["CALL", null, ["callee:00c58160:8"]]
+ 00c31e54 ["INT_ADD", "register:40f0:8", ["const:c31e54:8", "const:4:8"]]
+ 00c31e54 ["CALL", null, ["callee:00c58160:8"]]
- 00c31db8 bytes b6980094
+ 00c31e54 bytes c3980094
- 00c31dc8 ["INT_ADD", "register:40f0:8", ["const:c31dc8:8", "const:4:8"]]
- 00c31dc8 ["CALL", null, ["callee:00c5eac0:8"]]
+ 00c31e64 ["INT_ADD", "register:40f0:8", ["const:c31e64:8", "const:4:8"]]
+ 00c31e64 ["CALL", null, ["callee:00c5eac0:8"]]
- 00c31dc8 bytes 0ab30094
+ 00c31e64 bytes 17b30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8946ceee0f796e20f99f501602a6e4"></a>

### [`00c32088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md) → [`00c32124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32124.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8a0.md) · 呼出先 6件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md) [`00c5ea10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea10.md) [`00c5ecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecb0.md)
- 新版 呼出元 1件 [`00c5e970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e970.md) · 呼出先 6件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md) [`00c5eae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eae0.md) [`00c5ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3216c",
      "incomplete_value": false,
      "site": "00c32170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c320d0",
      "incomplete_value": false,
      "site": "00c320d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3218c",
      "incomplete_value": true,
      "site": "00c32190",
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
      "definition_site": "00c320f0",
      "incomplete_value": true,
      "site": "00c320f4",
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
      "00c32170",
      "DATA",
      [
        "storage",
        "00c95d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32184",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c32190",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c32170",
      "DATA",
      [
        "storage",
        "00c95df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32184",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c32190",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c320a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320a8) · [`00c320b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320b8) · [`00c320c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320c8)
- 新版 `00c32144`（命令位置の公開資料なし） · `00c32154`（命令位置の公開資料なし） · `00c32164`（命令位置の公開資料なし）

~~~diff
- 00c320a8 ["INT_ADD", "register:40f0:8", ["const:c320a8:8", "const:4:8"]]
- 00c320a8 ["CALL", null, ["callee:00c5ed80:8"]]
+ 00c32144 ["INT_ADD", "register:40f0:8", ["const:c32144:8", "const:4:8"]]
+ 00c32144 ["CALL", null, ["callee:00c5ed80:8"]]
- 00c320a8 bytes 02b30094
+ 00c32144 bytes 0fb30094
- 00c320b8 ["INT_ADD", "register:40f0:8", ["const:c320b8:8", "const:4:8"]]
- 00c320b8 ["CALL", null, ["callee:00c58160:8"]]
+ 00c32154 ["INT_ADD", "register:40f0:8", ["const:c32154:8", "const:4:8"]]
+ 00c32154 ["CALL", null, ["callee:00c58160:8"]]
- 00c320b8 bytes f6970094
+ 00c32154 bytes 03980094
- 00c320c8 ["INT_ADD", "register:40f0:8", ["const:c320c8:8", "const:4:8"]]
- 00c320c8 ["CALL", null, ["callee:00c5eae0:8"]]
+ 00c32164 ["INT_ADD", "register:40f0:8", ["const:c32164:8", "const:4:8"]]
+ 00c32164 ["CALL", null, ["callee:00c5eae0:8"]]
- 00c320c8 bytes 52b20094
+ 00c32164 bytes 5fb20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b9951582c77f159072bbd94b0580f6b"></a>

### [`00c3293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md) → [`00c329d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c329d8.md) _ZNSt6__ndk110__time_putC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8b0.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5e980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e980.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32a30",
      "incomplete_value": false,
      "site": "00c32a40",
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
            "const:835:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32994",
      "incomplete_value": false,
      "site": "00c329a4",
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
            "const:804:8"
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
      "00c32a30",
      "PARAM",
      [
        "storage",
        "002b2804",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c32a30",
      "PARAM",
      [
        "storage",
        "002b2835",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c329a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c329a4) · [`00c32970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c32970) · [`00c32994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c32994)
- 新版 `00c32a40`（命令位置の公開資料なし） · `00c32a0c`（命令位置の公開資料なし） · `00c32a30`（命令位置の公開資料なし）

~~~diff
- 00c329a4 ["INT_ADD", "register:40f0:8", ["const:c329a4:8", "const:4:8"]]
- 00c329a4 ["CALL", null, ["callee:00c58180:8"]]
+ 00c32a40 ["INT_ADD", "register:40f0:8", ["const:c32a40:8", "const:4:8"]]
+ 00c32a40 ["CALL", null, ["callee:00c58180:8"]]
- 00c329a4 bytes c3950094
+ 00c32a40 bytes d0950094
- 00c32970 ["INT_ADD", "register:40f0:8", ["const:c32970:8", "const:4:8"]]
- 00c32970 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c32a0c ["INT_ADD", "register:40f0:8", ["const:c32a0c:8", "const:4:8"]]
+ 00c32a0c ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c32970 bytes 2caa0094
+ 00c32a0c bytes 39aa0094
- 00c32994 ["COPY", "tmp:0:8", ["const:804:8"]]
- 00c32994 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c32994 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c32994 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c32a30 ["COPY", "tmp:0:8", ["const:835:8"]]
+ 00c32a30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c32a30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c32a30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c32994 bytes 00102091
+ 00c32a30 bytes 00d42091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf206c17827508e2c91bb2d0778811b"></a>

### [`00c329d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md) → [`00c32a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32a74.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md) · 呼出先 4件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 1件 [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md) · 呼出先 4件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c32af0",
      "incomplete_value": true,
      "site": "00c32af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32a54",
      "incomplete_value": true,
      "site": "00c32a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c32aa8",
      "incomplete_value": true,
      "site": "00c32aac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00c32a0c",
      "incomplete_value": true,
      "site": "00c32a10",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32ad0",
      "incomplete_value": false,
      "site": "00c32ad4",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32a34",
      "incomplete_value": false,
      "site": "00c32a38",
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
            "const:ca0:8"
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
      "00c32a94",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c32aa4",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c32ad0",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c32a94",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c32aa4",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c32ad0",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a38) · [`00c32a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a50) · [`00c32a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a54)
- 新版 `00c32ad4`（命令位置の公開資料なし） · `00c32aec`（命令位置の公開資料なし） · `00c32af0`（命令位置の公開資料なし）

~~~diff
- 00c32a38 ["INT_ADD", "register:40f0:8", ["const:c32a38:8", "const:4:8"]]
- 00c32a38 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c32ad4 ["INT_ADD", "register:40f0:8", ["const:c32ad4:8", "const:4:8"]]
+ 00c32ad4 ["CALL", null, ["callee:00c57f20:8"]]
- 00c32a38 bytes 06950094
+ 00c32ad4 bytes 13950094
- 00c32a50 ["INT_ADD", "register:40f0:8", ["const:c32a50:8", "const:4:8"]]
- 00c32a50 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c32aec ["INT_ADD", "register:40f0:8", ["const:c32aec:8", "const:4:8"]]
+ 00c32aec ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c32a50 bytes f4a90094
+ 00c32aec bytes 01aa0094
- 00c32a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
- 00c32a54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c32af0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
+ 00c32af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c32a54 bytes a04e06f9
+ 00c32af0 bytes a0ce06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2563ce7fd27af3cea90129117868c0e5"></a>

### [`00c32a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md) → [`00c32b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md) _ZNSt6__ndk117moneypunct_bynameIcLb0EE4initEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8d0.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md)
- 新版 呼出元 1件 [`00c5e9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9a0.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32e48",
      "incomplete_value": false,
      "site": "00c32e58",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32dac",
      "incomplete_value": false,
      "site": "00c32dbc",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c32e48",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c32e48",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32dbc) · [`00c32ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32ab0) · [`00c32ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32ac0)
- 新版 `00c32e58`（命令位置の公開資料なし） · `00c32b4c`（命令位置の公開資料なし） · `00c32b5c`（命令位置の公開資料なし）

~~~diff
- 00c32dbc ["INT_ADD", "register:40f0:8", ["const:c32dbc:8", "const:4:8"]]
- 00c32dbc ["CALL", null, ["callee:00c259d0:8"]]
+ 00c32e58 ["INT_ADD", "register:40f0:8", ["const:c32e58:8", "const:4:8"]]
+ 00c32e58 ["CALL", null, ["callee:00c259d0:8"]]
- 00c32dbc bytes decaff97
+ 00c32e58 bytes decaff97
- 00c32ab0 ["INT_ADD", "register:40f0:8", ["const:c32ab0:8", "const:4:8"]]
- 00c32ab0 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c32b4c ["INT_ADD", "register:40f0:8", ["const:c32b4c:8", "const:4:8"]]
+ 00c32b4c ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c32ab0 bytes dca90094
+ 00c32b4c bytes e9a90094
- 00c32ac0 ["INT_ADD", "register:40f0:8", ["const:c32ac0:8", "const:4:8"]]
- 00c32ac0 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c32b5c ["INT_ADD", "register:40f0:8", ["const:c32b5c:8", "const:4:8"]]
+ 00c32b5c ["CALL", null, ["callee:00c5e640:8"]]
- 00c32ac0 bytes acae0094
+ 00c32b5c bytes b9ae0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a0c0fac7db95f68cce0a39907f0562a"></a>

### [`00c33780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md) → [`00c3381c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md) _ZNSt6__ndk117moneypunct_bynameIwLb0EE4initEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8f0.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md)
- 新版 呼出元 1件 [`00c5e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9c0.md) · 呼出先 17件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33ed4",
      "incomplete_value": false,
      "site": "00c33ed8",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33e38",
      "incomplete_value": false,
      "site": "00c33e3c",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33eec",
      "incomplete_value": true,
      "site": "00c33efc",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33e50",
      "incomplete_value": true,
      "site": "00c33e60",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33f18",
      "incomplete_value": false,
      "site": "00c33f1c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33e7c",
      "incomplete_value": false,
      "site": "00c33e80",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c33ed4",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ],
    [
      "00c33eec",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ],
    [
      "00c33f18",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c33ed4",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ],
    [
      "00c33eec",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ],
    [
      "00c33f18",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c33e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e3c) · [`00c33e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e60) · [`00c33e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e80)
- 新版 `00c33ed8`（命令位置の公開資料なし） · `00c33efc`（命令位置の公開資料なし） · `00c33f1c`（命令位置の公開資料なし）

~~~diff
- 00c33e3c ["INT_ADD", "register:40f0:8", ["const:c33e3c:8", "const:4:8"]]
- 00c33e3c ["CALL", null, ["callee:00c5e080:8"]]
+ 00c33ed8 ["INT_ADD", "register:40f0:8", ["const:c33ed8:8", "const:4:8"]]
+ 00c33ed8 ["CALL", null, ["callee:00c5e080:8"]]
- 00c33e3c bytes 5da80094
+ 00c33ed8 bytes 6aa80094
- 00c33e60 ["INT_ADD", "register:40f0:8", ["const:c33e60:8", "const:4:8"]]
- 00c33e60 ["CALL", null, ["callee:00c259d0:8"]]
+ 00c33efc ["INT_ADD", "register:40f0:8", ["const:c33efc:8", "const:4:8"]]
+ 00c33efc ["CALL", null, ["callee:00c259d0:8"]]
- 00c33e60 bytes b5c6ff97
+ 00c33efc bytes b5c6ff97
- 00c33e80 ["INT_ADD", "register:40f0:8", ["const:c33e80:8", "const:4:8"]]
- 00c33e80 ["CALL", null, ["callee:00c5e080:8"]]
+ 00c33f1c ["INT_ADD", "register:40f0:8", ["const:c33f1c:8", "const:4:8"]]
+ 00c33f1c ["CALL", null, ["callee:00c5e080:8"]]
- 00c33e80 bytes 4ca80094
+ 00c33f1c bytes 59a80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8bace0a5a1c2dad25b6e1ddcf8455f"></a>

### [`00c3447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md) → [`00c34518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md) _ZNSt6__ndk117moneypunct_bynameIwLb1EE4initEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e900.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md)
- 新版 呼出元 1件 [`00c5e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9d0.md) · 呼出先 17件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34bd0",
      "incomplete_value": false,
      "site": "00c34bd4",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34b34",
      "incomplete_value": false,
      "site": "00c34b38",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34be8",
      "incomplete_value": false,
      "site": "00c34bf8",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34b4c",
      "incomplete_value": false,
      "site": "00c34b5c",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34c14",
      "incomplete_value": false,
      "site": "00c34c18",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34b78",
      "incomplete_value": false,
      "site": "00c34b7c",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c34bd0",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ],
    [
      "00c34be8",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ],
    [
      "00c34c14",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c34bd0",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ],
    [
      "00c34be8",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ],
    [
      "00c34c14",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b38) · [`00c34b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b5c) · [`00c34b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b7c)
- 新版 `00c34bd4`（命令位置の公開資料なし） · `00c34bf8`（命令位置の公開資料なし） · `00c34c18`（命令位置の公開資料なし）

~~~diff
- 00c34b38 ["INT_ADD", "register:40f0:8", ["const:c34b38:8", "const:4:8"]]
- 00c34b38 ["CALL", null, ["callee:00c5e080:8"]]
+ 00c34bd4 ["INT_ADD", "register:40f0:8", ["const:c34bd4:8", "const:4:8"]]
+ 00c34bd4 ["CALL", null, ["callee:00c5e080:8"]]
- 00c34b38 bytes 1ea50094
+ 00c34bd4 bytes 2ba50094
- 00c34b5c ["INT_ADD", "register:40f0:8", ["const:c34b5c:8", "const:4:8"]]
- 00c34b5c ["CALL", null, ["callee:00c259d0:8"]]
+ 00c34bf8 ["INT_ADD", "register:40f0:8", ["const:c34bf8:8", "const:4:8"]]
+ 00c34bf8 ["CALL", null, ["callee:00c259d0:8"]]
- 00c34b5c bytes 76c3ff97
+ 00c34bf8 bytes 76c3ff97
- 00c34b7c ["INT_ADD", "register:40f0:8", ["const:c34b7c:8", "const:4:8"]]
- 00c34b7c ["CALL", null, ["callee:00c5e080:8"]]
+ 00c34c18 ["INT_ADD", "register:40f0:8", ["const:c34c18:8", "const:4:8"]]
+ 00c34c18 ["CALL", null, ["callee:00c5e080:8"]]
- 00c34b7c bytes 0da50094
+ 00c34c18 bytes 1aa50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d51074f6a52090d9ad8f936b3742708c"></a>

### [`00c34dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md) → [`00c34e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e58.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md) [`00c5eb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb10.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md) [`00c5ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebe0.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c34e80",
      "incomplete_value": true,
      "site": "00c34e84",
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
      "definition_site": "00c34de4",
      "incomplete_value": true,
      "site": "00c34de8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c34ee8",
      "incomplete_value": true,
      "site": "00c34ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34e4c",
      "incomplete_value": true,
      "site": "00c34e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00c34e9c",
      "incomplete_value": true,
      "site": "00c34ea0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00c34e00",
      "incomplete_value": true,
      "site": "00c34e04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "00c34e78",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c34e84",
      "DATA",
      [
        "storage",
        "00c938c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c34e90",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c34e78",
      "READ",
      [
        "storage",
        "00c9beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c34e84",
      "DATA",
      [
        "storage",
        "00c93990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c34e90",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e30) · [`00c34e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e48) · [`00c34e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e4c)
- 新版 `00c34ecc`（命令位置の公開資料なし） · `00c34ee4`（命令位置の公開資料なし） · `00c34ee8`（命令位置の公開資料なし）

~~~diff
- 00c34e30 ["INT_ADD", "register:40f0:8", ["const:c34e30:8", "const:4:8"]]
- 00c34e30 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c34ecc ["INT_ADD", "register:40f0:8", ["const:c34ecc:8", "const:4:8"]]
+ 00c34ecc ["CALL", null, ["callee:00c57f20:8"]]
- 00c34e30 bytes 088c0094
+ 00c34ecc bytes 158c0094
- 00c34e48 ["INT_ADD", "register:40f0:8", ["const:c34e48:8", "const:4:8"]]
- 00c34e48 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c34ee4 ["INT_ADD", "register:40f0:8", ["const:c34ee4:8", "const:4:8"]]
+ 00c34ee4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c34e48 bytes f6a00094
+ 00c34ee4 bytes 03a10094
- 00c34e4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
- 00c34e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c34ee8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
+ 00c34ee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c34e4c bytes a04e06f9
+ 00c34ee8 bytes a0ce06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a79dc738a5e98bada88889154152d43"></a>

### [`00c35440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md) → [`00c354dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md) FUN_00c354dc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c354d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 1件 [`00c35570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35570.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c354fc",
      "incomplete_value": true,
      "site": "00c35500",
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
      "definition_site": "00c35460",
      "incomplete_value": true,
      "site": "00c35464",
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
      "00c354f4",
      "READ",
      [
        "storage",
        "00c9bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c35500",
      "DATA",
      [
        "storage",
        "00c95400",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c354f4",
      "READ",
      [
        "storage",
        "00c9be68",
        null,
        "pointer"
      ]
    ],
    [
      "00c35500",
      "DATA",
      [
        "storage",
        "00c954d0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c35458) · [`00c35488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c35488) · [`00c354a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c354a4)
- 新版 `00c354f4`（命令位置の公開資料なし） · `00c35524`（命令位置の公開資料なし） · `00c35540`（命令位置の公開資料なし）

~~~diff
- 00c35458 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c35458 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c354f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
+ 00c354f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35458 bytes 08cd46f9
+ 00c354f4 bytes 083547f9
- 00c35488 ["INT_ADD", "register:40f0:8", ["const:c35488:8", "const:4:8"]]
- 00c35488 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35524 ["INT_ADD", "register:40f0:8", ["const:c35524:8", "const:4:8"]]
+ 00c35524 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35488 bytes 8a8a0094
+ 00c35524 bytes 978a0094
- 00c354a4 ["INT_ADD", "register:40f0:8", ["const:c354a4:8", "const:4:8"]]
- 00c354a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35540 ["INT_ADD", "register:40f0:8", ["const:c35540:8", "const:4:8"]]
+ 00c35540 ["CALL", null, ["callee:00c57f80:8"]]
- 00c354a4 bytes 838a0094
+ 00c35540 bytes 908a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4aeef311ba5cab757a7a3d16c1d748a"></a>

### [`00c35500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md) → [`00c3559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md) FUN_00c3559c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 1件 [`00c35630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35630.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c355bc",
      "incomplete_value": true,
      "site": "00c355c0",
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
      "definition_site": "00c35520",
      "incomplete_value": true,
      "site": "00c35524",
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
      "00c355b4",
      "READ",
      [
        "storage",
        "00c9bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00c355c0",
      "DATA",
      [
        "storage",
        "00c95488",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c355b4",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00c355c0",
      "DATA",
      [
        "storage",
        "00c95558",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35518) · [`00c35548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35548) · [`00c35564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35564)
- 新版 `00c355b4`（命令位置の公開資料なし） · `00c355e4`（命令位置の公開資料なし） · `00c35600`（命令位置の公開資料なし）

~~~diff
- 00c35518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00c35518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c355b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00c355b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35518 bytes 08d146f9
+ 00c355b4 bytes 083947f9
- 00c35548 ["INT_ADD", "register:40f0:8", ["const:c35548:8", "const:4:8"]]
- 00c35548 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c355e4 ["INT_ADD", "register:40f0:8", ["const:c355e4:8", "const:4:8"]]
+ 00c355e4 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35548 bytes 5a8a0094
+ 00c355e4 bytes 678a0094
- 00c35564 ["INT_ADD", "register:40f0:8", ["const:c35564:8", "const:4:8"]]
- 00c35564 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35600 ["INT_ADD", "register:40f0:8", ["const:c35600:8", "const:4:8"]]
+ 00c35600 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35564 bytes 538a0094
+ 00c35600 bytes 608a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83308dcb28226af2f57ce4be549b7a7"></a>

### [`00c355c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md) → [`00c3565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md) FUN_00c3565c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c35654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 1件 [`00c356f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c356f0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3567c",
      "incomplete_value": true,
      "site": "00c35680",
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
      "definition_site": "00c355e0",
      "incomplete_value": true,
      "site": "00c355e4",
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
      "00c35674",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00c35680",
      "DATA",
      [
        "storage",
        "00c95510",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c35674",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c35680",
      "DATA",
      [
        "storage",
        "00c955e0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c355d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c355d8) · [`00c35608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c35608) · [`00c35624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c35624)
- 新版 `00c35674`（命令位置の公開資料なし） · `00c356a4`（命令位置の公開資料なし） · `00c356c0`（命令位置の公開資料なし）

~~~diff
- 00c355d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
- 00c355d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c35674 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c35674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c355d8 bytes 08d546f9
+ 00c35674 bytes 083d47f9
- 00c35608 ["INT_ADD", "register:40f0:8", ["const:c35608:8", "const:4:8"]]
- 00c35608 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c356a4 ["INT_ADD", "register:40f0:8", ["const:c356a4:8", "const:4:8"]]
+ 00c356a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35608 bytes 2a8a0094
+ 00c356a4 bytes 378a0094
- 00c35624 ["INT_ADD", "register:40f0:8", ["const:c35624:8", "const:4:8"]]
- 00c35624 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c356c0 ["INT_ADD", "register:40f0:8", ["const:c356c0:8", "const:4:8"]]
+ 00c356c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35624 bytes 238a0094
+ 00c356c0 bytes 308a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061d8630bcdbab291efb85a271acdbe9"></a>

### [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) → [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) FUN_00c3596c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) [`00c358e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) [`00c35984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00c3597c",
      "incomplete_value": false,
      "site": "00c35980",
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
    "old": {
      "definition_site": "00c358e0",
      "incomplete_value": false,
      "site": "00c358e4",
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
            "const:f4c:8"
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
      "00c3597c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3597c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c358e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md#insn-00c358e4) · [`00c358e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md#insn-00c358e0)
- 新版 `00c35980`（命令位置の公開資料なし） · `00c3597c`（命令位置の公開資料なし）

~~~diff
- 00c358e4 ["INT_ADD", "register:40f0:8", ["const:c358e4:8", "const:4:8"]]
- 00c358e4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00c35980 ["INT_ADD", "register:40f0:8", ["const:c35980:8", "const:4:8"]]
+ 00c35980 ["CALL", null, ["callee:0043b7b8:8"]]
- 00c358e4 bytes a517e097
+ 00c35980 bytes 8e17e097
- 00c358e0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00c358e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c358e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c358e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c3597c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00c3597c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c3597c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c3597c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c358e0 bytes 00303d91
+ 00c3597c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0d2f478cf4900e580131ff6676df74"></a>

### [`00c35ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md) → [`00c35c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35c3c.md) FUN_00c35c3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c2cb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35c58",
      "incomplete_value": true,
      "site": "00c35c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:1f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35bbc",
      "incomplete_value": true,
      "site": "00c35bc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:f0:8"
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
      "definition_site": "00c35c70",
      "incomplete_value": true,
      "site": "00c35c74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:1d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35bd4",
      "incomplete_value": true,
      "site": "00c35bd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:d8:8"
              ]
            ]
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
      "definition_site": "00c35c88",
      "incomplete_value": true,
      "site": "00c35c8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35bec",
      "incomplete_value": true,
      "site": "00c35bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:c0:8"
              ]
            ]
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
      "00c35c4c",
      "READ",
      [
        "storage",
        "011280e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c35c58",
      "READ",
      [
        "storage",
        "011280f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c35c64",
      "READ",
      [
        "storage",
        "011280c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c35c4c",
      "READ",
      [
        "storage",
        "011281e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c35c58",
      "READ",
      [
        "storage",
        "011281f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c35c64",
      "READ",
      [
        "storage",
        "011281c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bc0) · [`00c35bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bd8) · [`00c35bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bf0)
- 新版 `00c35c5c`（命令位置の公開資料なし） · `00c35c74`（命令位置の公開資料なし） · `00c35c8c`（命令位置の公開資料なし）

~~~diff
- 00c35bc0 ["INT_ADD", "register:40f0:8", ["const:c35bc0:8", "const:4:8"]]
- 00c35bc0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35c5c ["INT_ADD", "register:40f0:8", ["const:c35c5c:8", "const:4:8"]]
+ 00c35c5c ["CALL", null, ["callee:00c57f80:8"]]
- 00c35bc0 bytes bc880094
+ 00c35c5c bytes c9880094
- 00c35bd8 ["INT_ADD", "register:40f0:8", ["const:c35bd8:8", "const:4:8"]]
- 00c35bd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35c74 ["INT_ADD", "register:40f0:8", ["const:c35c74:8", "const:4:8"]]
+ 00c35c74 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35bd8 bytes b6880094
+ 00c35c74 bytes c3880094
- 00c35bf0 ["INT_ADD", "register:40f0:8", ["const:c35bf0:8", "const:4:8"]]
- 00c35bf0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c35c8c ["INT_ADD", "register:40f0:8", ["const:c35c8c:8", "const:4:8"]]
+ 00c35c8c ["CALL", null, ["callee:00c57f80:8"]]
- 00c35bf0 bytes b0880094
+ 00c35c8c bytes bd880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15d7c26b9ed9ed08dadff385f3aa9b79"></a>

### [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) → [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) FUN_00c36054

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 96件 [`00c0788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) [`00c0a534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) [`00c0ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) [`00c0d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) [`00c0e08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md)
- 新版 呼出元 96件 [`00c07928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07928.md) [`00c0a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a5d0.md) [`00c0ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0ae00.md) [`00c0da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0da44.md) [`00c0e128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0e/00c0e128.md) · 呼出先 1件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36078",
      "incomplete_value": true,
      "site": "00c3607c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35fdc",
      "incomplete_value": true,
      "site": "00c35fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "00c36078",
      "READ",
      [
        "storage",
        "00c9be08",
        null,
        "pointer"
      ]
    ],
    [
      "00c36078",
      "PARAM",
      [
        "storage",
        "01127e00",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00c36078",
      "READ",
      [
        "storage",
        "00c9bed8",
        null,
        "pointer"
      ]
    ],
    [
      "00c36078",
      "PARAM",
      [
        "storage",
        "01127f00",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md#insn-00c35fe0) · [`00c35fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md#insn-00c35fdc)
- 新版 `00c3607c`（命令位置の公開資料なし） · `00c36078`（命令位置の公開資料なし）

~~~diff
- 00c35fe0 ["INT_ADD", "register:40f0:8", ["const:c35fe0:8", "const:4:8"]]
- 00c35fe0 ["CALL", null, ["callee:00c53d40:8"]]
+ 00c3607c ["INT_ADD", "register:40f0:8", ["const:c3607c:8", "const:4:8"]]
+ 00c3607c ["CALL", null, ["callee:00c53d40:8"]]
- 00c35fe0 bytes 30770094
+ 00c3607c bytes 31770094
- 00c35fdc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e08:8"]]
- 00c35fdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c36078 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed8:8"]]
+ 00c36078 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35fdc bytes 210447f9
+ 00c36078 bytes 216c47f9
~~~


<a id="compare-73796bd6a352e527021fb92184bf3c58"></a>

### [`00c35ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md) → [`00c36098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36098.md) FUN_00c36098

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c360b8",
      "incomplete_value": true,
      "site": "00c360bc",
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
      "definition_site": "00c3601c",
      "incomplete_value": true,
      "site": "00c36020",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c360d0",
      "incomplete_value": true,
      "site": "00c360d4",
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
      "definition_site": "00c36034",
      "incomplete_value": true,
      "site": "00c36038",
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
      "00c360b0",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c360bc",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c360c8",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c360b0",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c360bc",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c360c8",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c36014) · [`00c36024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c36024) · [`00c3602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c3602c)
- 新版 `00c360b0`（命令位置の公開資料なし） · `00c360c0`（命令位置の公開資料なし） · `00c360c8`（命令位置の公開資料なし）

~~~diff
- 00c36014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00c36014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c360b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c360b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c36014 bytes 08e946f9
+ 00c360b0 bytes 085147f9
- 00c36024 ["INT_ADD", "register:40f0:8", ["const:c36024:8", "const:4:8"]]
- 00c36024 ["CALL", null, ["callee:00c5d2a0:8"]]
+ 00c360c0 ["INT_ADD", "register:40f0:8", ["const:c360c0:8", "const:4:8"]]
+ 00c360c0 ["CALL", null, ["callee:00c5d2a0:8"]]
- 00c36024 bytes 6b9c0094
+ 00c360c0 bytes 789c0094
- 00c3602c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
- 00c3602c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c360c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00c360c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c3602c bytes 08e546f9
+ 00c360c8 bytes 084d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c675aa10c7161681c8f29b13c8eb46de"></a>

### [`00c3606c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md) → [`00c36108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36108.md) FUN_00c36108

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c36128",
      "incomplete_value": true,
      "site": "00c3612c",
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
      "definition_site": "00c3608c",
      "incomplete_value": true,
      "site": "00c36090",
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
      "00c36120",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3612c",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c36120",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3612c",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c36084) · [`00c36094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c36094) · [`00c3609c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c3609c)
- 新版 `00c36120`（命令位置の公開資料なし） · `00c36130`（命令位置の公開資料なし） · `00c36138`（命令位置の公開資料なし）

~~~diff
- 00c36084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 00c36084 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c36120 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 00c36120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c36084 bytes 08ed46f9
+ 00c36120 bytes 085547f9
- 00c36094 ["INT_ADD", "register:40f0:8", ["const:c36094:8", "const:4:8"]]
- 00c36094 ["CALL", null, ["callee:00c5d2a0:8"]]
+ 00c36130 ["INT_ADD", "register:40f0:8", ["const:c36130:8", "const:4:8"]]
+ 00c36130 ["CALL", null, ["callee:00c5d2a0:8"]]
- 00c36094 bytes 4f9c0094
+ 00c36130 bytes 5c9c0094
- 00c3609c ["INT_ADD", "register:40f0:8", ["const:c3609c:8", "const:4:8"]]
- 00c3609c ["CALL", null, ["callee:00c5ead0:8"]]
+ 00c36138 ["INT_ADD", "register:40f0:8", ["const:c36138:8", "const:4:8"]]
+ 00c36138 ["CALL", null, ["callee:00c5ead0:8"]]
- 00c3609c bytes 59a20094
+ 00c36138 bytes 66a20094
~~~


<a id="compare-0147cdcb53cd54159e20a07a4d31c196"></a>

### [`00c3616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md) → [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) FUN_00c36208

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c07f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md) [`00c0b46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c08028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md) [`00c0b508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d220.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36304",
      "incomplete_value": true,
      "site": "00c36304",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36268",
      "incomplete_value": true,
      "site": "00c36268",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36260",
      "incomplete_value": true,
      "site": "00c36270",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c361c4",
      "incomplete_value": true,
      "site": "00c361d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c362e4",
      "incomplete_value": false,
      "site": "00c362e8",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36248",
      "incomplete_value": false,
      "site": "00c3624c",
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
            "const:ca0:8"
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
      "00c36258",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36260",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c362e4",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c36258",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36260",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c362e4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c361b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c361b0) · [`00c361d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c361d4) · [`00c3624c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c3624c)
- 新版 `00c3624c`（命令位置の公開資料なし） · `00c36270`（命令位置の公開資料なし） · `00c362e8`（命令位置の公開資料なし）

~~~diff
- 00c361b0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c361b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c361b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c361b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3624c ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c3624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c361b0 bytes 08813291
+ 00c3624c bytes 08813691
- 00c361d4 ["INT_ADD", "register:40f0:8", ["const:c361d4:8", "const:4:8"]]
- 00c361d4 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36270 ["INT_ADD", "register:40f0:8", ["const:c36270:8", "const:4:8"]]
+ 00c36270 ["CALL", null, ["callee:00c5d220:8"]]
- 00c361d4 bytes df9b0094
+ 00c36270 bytes ec9b0094
- 00c3624c ["INT_ADD", "register:40f0:8", ["const:c3624c:8", "const:4:8"]]
- 00c3624c ["CALL", null, ["callee:00c57f20:8"]]
+ 00c362e8 ["INT_ADD", "register:40f0:8", ["const:c362e8:8", "const:4:8"]]
+ 00c362e8 ["CALL", null, ["callee:00c57f20:8"]]
- 00c3624c bytes 01870094
+ 00c362e8 bytes 0e870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147d9b7d1b27becd767b67b275c89e11"></a>

### [`00c36294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md) → [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) FUN_00c36330

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c083c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md) [`00c0b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c08464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md) [`00c0b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d220.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c3642c",
      "incomplete_value": true,
      "site": "00c3642c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36390",
      "incomplete_value": true,
      "site": "00c36390",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36388",
      "incomplete_value": true,
      "site": "00c36398",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c362ec",
      "incomplete_value": true,
      "site": "00c362fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c3640c",
      "incomplete_value": false,
      "site": "00c36410",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36370",
      "incomplete_value": false,
      "site": "00c36374",
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
            "const:ca0:8"
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
      "00c36380",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36388",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3640c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c36380",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36388",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3640c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c362d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c362d8) · [`00c362fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c362fc) · [`00c36374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c36374)
- 新版 `00c36374`（命令位置の公開資料なし） · `00c36398`（命令位置の公開資料なし） · `00c36410`（命令位置の公開資料なし）

~~~diff
- 00c362d8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c362d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c362d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c362d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c36374 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c36374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c36374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c36374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c362d8 bytes 08813291
+ 00c36374 bytes 08813691
- 00c362fc ["INT_ADD", "register:40f0:8", ["const:c362fc:8", "const:4:8"]]
- 00c362fc ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36398 ["INT_ADD", "register:40f0:8", ["const:c36398:8", "const:4:8"]]
+ 00c36398 ["CALL", null, ["callee:00c5d220:8"]]
- 00c362fc bytes 959b0094
+ 00c36398 bytes a29b0094
- 00c36374 ["INT_ADD", "register:40f0:8", ["const:c36374:8", "const:4:8"]]
- 00c36374 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36410 ["INT_ADD", "register:40f0:8", ["const:c36410:8", "const:4:8"]]
+ 00c36410 ["CALL", null, ["callee:00c57f20:8"]]
- 00c36374 bytes b7860094
+ 00c36410 bytes c4860094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-090e04a8b54f06591d20bcbf34c48547"></a>

### [`00c363bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md) → [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) FUN_00c36458

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md) [`00c0bccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c088a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md) [`00c0bd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36584",
      "incomplete_value": true,
      "site": "00c36584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c364e8",
      "incomplete_value": true,
      "site": "00c364e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c364cc",
      "incomplete_value": true,
      "site": "00c364dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36430",
      "incomplete_value": true,
      "site": "00c36440",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c36564",
      "incomplete_value": false,
      "site": "00c36568",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c364c8",
      "incomplete_value": false,
      "site": "00c364cc",
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
            "const:ca0:8"
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
      "00c364c4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c364cc",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36564",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c364c4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c364cc",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36564",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c36430) · [`00c36440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c36440) · [`00c364cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c364cc)
- 新版 `00c364cc`（命令位置の公開資料なし） · `00c364dc`（命令位置の公開資料なし） · `00c36568`（命令位置の公開資料なし）

~~~diff
- 00c36430 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c98:8"]]
- 00c36430 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c364cc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d98:8"]]
+ 00c364cc ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00c36430 bytes 434f46f9
+ 00c364cc bytes 43cf46f9
- 00c36440 ["INT_ADD", "register:40f0:8", ["const:c36440:8", "const:4:8"]]
- 00c36440 ["CALL", null, ["callee:00c5d230:8"]]
+ 00c364dc ["INT_ADD", "register:40f0:8", ["const:c364dc:8", "const:4:8"]]
+ 00c364dc ["CALL", null, ["callee:00c5d230:8"]]
- 00c36440 bytes 489b0094
+ 00c364dc bytes 559b0094
- 00c364cc ["INT_ADD", "register:40f0:8", ["const:c364cc:8", "const:4:8"]]
- 00c364cc ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36568 ["INT_ADD", "register:40f0:8", ["const:c36568:8", "const:4:8"]]
+ 00c36568 ["CALL", null, ["callee:00c57f20:8"]]
- 00c364cc bytes 61860094
+ 00c36568 bytes 6e860094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdb8326cc49a6e0bb888500d527822e"></a>

### [`00c36514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md) → [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) FUN_00c365b0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md) [`00c0c0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c08cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md) [`00c0c198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c366d8",
      "incomplete_value": true,
      "site": "00c366d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3663c",
      "incomplete_value": true,
      "site": "00c3663c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36624",
      "incomplete_value": true,
      "site": "00c36634",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36588",
      "incomplete_value": true,
      "site": "00c36598",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c366b8",
      "incomplete_value": false,
      "site": "00c366bc",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3661c",
      "incomplete_value": false,
      "site": "00c36620",
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
            "const:ca0:8"
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
      "00c3661c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36624",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c366b8",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3661c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36624",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c366b8",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36598) · [`00c36620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36620) · [`00c36638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36638)
- 新版 `00c36634`（命令位置の公開資料なし） · `00c366bc`（命令位置の公開資料なし） · `00c366d4`（命令位置の公開資料なし）

~~~diff
- 00c36598 ["INT_ADD", "register:40f0:8", ["const:c36598:8", "const:4:8"]]
- 00c36598 ["CALL", null, ["callee:00c5d230:8"]]
+ 00c36634 ["INT_ADD", "register:40f0:8", ["const:c36634:8", "const:4:8"]]
+ 00c36634 ["CALL", null, ["callee:00c5d230:8"]]
- 00c36598 bytes f29a0094
+ 00c36634 bytes ff9a0094
- 00c36620 ["INT_ADD", "register:40f0:8", ["const:c36620:8", "const:4:8"]]
- 00c36620 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c366bc ["INT_ADD", "register:40f0:8", ["const:c366bc:8", "const:4:8"]]
+ 00c366bc ["CALL", null, ["callee:00c57f20:8"]]
- 00c36620 bytes 0c860094
+ 00c366bc bytes 19860094
- 00c36638 ["INT_ADD", "register:40f0:8", ["const:c36638:8", "const:4:8"]]
- 00c36638 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c366d4 ["INT_ADD", "register:40f0:8", ["const:c366d4:8", "const:4:8"]]
+ 00c366d4 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c36638 bytes fa9a0094
+ 00c366d4 bytes 079b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd363f5cc17bdf91f42d33420381823"></a>

### [`00c36668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md) → [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) FUN_00c36704

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c0907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md) [`00c0c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c09118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md) [`00c0c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36820",
      "incomplete_value": true,
      "site": "00c36820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36784",
      "incomplete_value": true,
      "site": "00c36784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36778",
      "incomplete_value": true,
      "site": "00c36788",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366dc",
      "incomplete_value": true,
      "site": "00c366ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c36800",
      "incomplete_value": false,
      "site": "00c36804",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36764",
      "incomplete_value": false,
      "site": "00c36768",
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
            "const:ca0:8"
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
      "00c36770",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36778",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36800",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c36770",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36778",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36800",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c366ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c366ec) · [`00c36768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c36768) · [`00c36780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c36780)
- 新版 `00c36788`（命令位置の公開資料なし） · `00c36804`（命令位置の公開資料なし） · `00c3681c`（命令位置の公開資料なし）

~~~diff
- 00c366ec ["INT_ADD", "register:40f0:8", ["const:c366ec:8", "const:4:8"]]
- 00c366ec ["CALL", null, ["callee:00c5d230:8"]]
+ 00c36788 ["INT_ADD", "register:40f0:8", ["const:c36788:8", "const:4:8"]]
+ 00c36788 ["CALL", null, ["callee:00c5d230:8"]]
- 00c366ec bytes 9d9a0094
+ 00c36788 bytes aa9a0094
- 00c36768 ["INT_ADD", "register:40f0:8", ["const:c36768:8", "const:4:8"]]
- 00c36768 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36804 ["INT_ADD", "register:40f0:8", ["const:c36804:8", "const:4:8"]]
+ 00c36804 ["CALL", null, ["callee:00c57f20:8"]]
- 00c36768 bytes ba850094
+ 00c36804 bytes c7850094
- 00c36780 ["INT_ADD", "register:40f0:8", ["const:c36780:8", "const:4:8"]]
- 00c36780 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c3681c ["INT_ADD", "register:40f0:8", ["const:c3681c:8", "const:4:8"]]
+ 00c3681c ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c36780 bytes a89a0094
+ 00c3681c bytes b59a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2f52d9cfdf11457ca58ff18d5af72d"></a>

### [`00c367b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md) → [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) FUN_00c3684c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c094b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md) [`00c0c95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c09554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md) [`00c0c9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36968",
      "incomplete_value": true,
      "site": "00c36968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c368cc",
      "incomplete_value": true,
      "site": "00c368cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c368c0",
      "incomplete_value": true,
      "site": "00c368d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36824",
      "incomplete_value": true,
      "site": "00c36834",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "definition_site": "00c36948",
      "incomplete_value": false,
      "site": "00c3694c",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c368ac",
      "incomplete_value": false,
      "site": "00c368b0",
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
            "const:ca0:8"
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
      "00c368b8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c368c0",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36948",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c368b8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c368c0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36948",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c36834) · [`00c368b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c368b0) · [`00c368c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c368c8)
- 新版 `00c368d0`（命令位置の公開資料なし） · `00c3694c`（命令位置の公開資料なし） · `00c36964`（命令位置の公開資料なし）

~~~diff
- 00c36834 ["INT_ADD", "register:40f0:8", ["const:c36834:8", "const:4:8"]]
- 00c36834 ["CALL", null, ["callee:00c5d230:8"]]
+ 00c368d0 ["INT_ADD", "register:40f0:8", ["const:c368d0:8", "const:4:8"]]
+ 00c368d0 ["CALL", null, ["callee:00c5d230:8"]]
- 00c36834 bytes 4b9a0094
+ 00c368d0 bytes 589a0094
- 00c368b0 ["INT_ADD", "register:40f0:8", ["const:c368b0:8", "const:4:8"]]
- 00c368b0 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c3694c ["INT_ADD", "register:40f0:8", ["const:c3694c:8", "const:4:8"]]
+ 00c3694c ["CALL", null, ["callee:00c57f20:8"]]
- 00c368b0 bytes 68850094
+ 00c3694c bytes 75850094
- 00c368c8 ["INT_ADD", "register:40f0:8", ["const:c368c8:8", "const:4:8"]]
- 00c368c8 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c36964 ["INT_ADD", "register:40f0:8", ["const:c36964:8", "const:4:8"]]
+ 00c36964 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c368c8 bytes 569a0094
+ 00c36964 bytes 639a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e22fc32150f5658781cfc2210d170379"></a>

### [`00c368f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md) → [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) FUN_00c36994

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c098f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md) [`00c0cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c09990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md) [`00c0ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58680.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36a80",
      "incomplete_value": false,
      "site": "00c36a80",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c369e4",
      "incomplete_value": false,
      "site": "00c369e4",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36a5c",
      "incomplete_value": false,
      "site": "00c36a60",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c369c0",
      "incomplete_value": false,
      "site": "00c369c4",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36a6c",
      "incomplete_value": false,
      "site": "00c36a78",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c369d0",
      "incomplete_value": false,
      "site": "00c369dc",
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
            "const:17c:8"
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
      "00c369d8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36a5c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36a6c",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c369d8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36a5c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36a6c",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c369c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369c4) · [`00c369dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369dc) · [`00c369e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369e4)
- 新版 `00c36a60`（命令位置の公開資料なし） · `00c36a78`（命令位置の公開資料なし） · `00c36a80`（命令位置の公開資料なし）

~~~diff
- 00c369c4 ["INT_ADD", "register:40f0:8", ["const:c369c4:8", "const:4:8"]]
- 00c369c4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36a60 ["INT_ADD", "register:40f0:8", ["const:c36a60:8", "const:4:8"]]
+ 00c36a60 ["CALL", null, ["callee:00c57f20:8"]]
- 00c369c4 bytes 23850094
+ 00c36a60 bytes 30850094
- 00c369dc ["INT_ADD", "register:40f0:8", ["const:c369dc:8", "const:4:8"]]
- 00c369dc ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c36a78 ["INT_ADD", "register:40f0:8", ["const:c36a78:8", "const:4:8"]]
+ 00c36a78 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c369dc bytes 119a0094
+ 00c36a78 bytes 1e9a0094
- 00c369e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00c369e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c36a80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c36a80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c369e4 bytes 004d06f9
+ 00c36a80 bytes 00cd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-248c433a09836cdbe71ab4bb22b9f709"></a>

### [`00c36a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md) → [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) FUN_00c36aac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md) [`00c0d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 2件 [`00c09da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md) [`00c0d234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36b98",
      "incomplete_value": false,
      "site": "00c36b98",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36afc",
      "incomplete_value": false,
      "site": "00c36afc",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36b74",
      "incomplete_value": false,
      "site": "00c36b78",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36ad8",
      "incomplete_value": false,
      "site": "00c36adc",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36b84",
      "incomplete_value": false,
      "site": "00c36b90",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36ae8",
      "incomplete_value": false,
      "site": "00c36af4",
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
            "const:17c:8"
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
      "00c36af0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b74",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b84",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c36af0",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b74",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b84",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36adc) · [`00c36af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36af4) · [`00c36afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36afc)
- 新版 `00c36b78`（命令位置の公開資料なし） · `00c36b90`（命令位置の公開資料なし） · `00c36b98`（命令位置の公開資料なし）

~~~diff
- 00c36adc ["INT_ADD", "register:40f0:8", ["const:c36adc:8", "const:4:8"]]
- 00c36adc ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36b78 ["INT_ADD", "register:40f0:8", ["const:c36b78:8", "const:4:8"]]
+ 00c36b78 ["CALL", null, ["callee:00c57f20:8"]]
- 00c36adc bytes dd840094
+ 00c36b78 bytes ea840094
- 00c36af4 ["INT_ADD", "register:40f0:8", ["const:c36af4:8", "const:4:8"]]
- 00c36af4 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c36b90 ["INT_ADD", "register:40f0:8", ["const:c36b90:8", "const:4:8"]]
+ 00c36b90 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c36af4 bytes cb990094
+ 00c36b90 bytes d8990094
- 00c36afc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00c36afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c36b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c36b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c36afc bytes 004d06f9
+ 00c36b98 bytes 00cd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2410c3eddb4f08b377da0e84f3d28ef6"></a>

### [`00c36b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md) → [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) FUN_00c36bc4

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c0a124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md) [`00c0d5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5ed60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed60.md)
- 新版 呼出元 2件 [`00c0a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md) [`00c0d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5ee30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.07% / 新版 85.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36cbc",
      "incomplete_value": true,
      "site": "00c36cbc",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36c20",
      "incomplete_value": true,
      "site": "00c36c20",
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
            "const:c98:8"
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
      "definition_site": "00c36c9c",
      "incomplete_value": false,
      "site": "00c36ca0",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36c00",
      "incomplete_value": false,
      "site": "00c36c04",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36cac",
      "incomplete_value": false,
      "site": "00c36cb8",
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
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36c10",
      "incomplete_value": false,
      "site": "00c36c1c",
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
            "const:17c:8"
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
      "00c36c10",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36c18",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36c50",
      "READ",
      [
        "storage",
        "002c2f40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c36c10",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36c18",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36c50",
      "READ",
      [
        "storage",
        "002c2f80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36b68) · [`00c36c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36c04) · [`00c36c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36c1c)
- 新版 `00c36c04`（命令位置の公開資料なし） · `00c36ca0`（命令位置の公開資料なし） · `00c36cb8`（命令位置の公開資料なし）

~~~diff
- 00c36b68 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c36b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c36b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c36b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c36c04 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c36c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c36c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c36c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c36b68 bytes 08813291
+ 00c36c04 bytes 08813691
- 00c36c04 ["INT_ADD", "register:40f0:8", ["const:c36c04:8", "const:4:8"]]
- 00c36c04 ["CALL", null, ["callee:00c57f20:8"]]
+ 00c36ca0 ["INT_ADD", "register:40f0:8", ["const:c36ca0:8", "const:4:8"]]
+ 00c36ca0 ["CALL", null, ["callee:00c57f20:8"]]
- 00c36c04 bytes 93840094
+ 00c36ca0 bytes a0840094
- 00c36c1c ["INT_ADD", "register:40f0:8", ["const:c36c1c:8", "const:4:8"]]
- 00c36c1c ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00c36cb8 ["INT_ADD", "register:40f0:8", ["const:c36cb8:8", "const:4:8"]]
+ 00c36cb8 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00c36c1c bytes 81990094
+ 00c36cb8 bytes 8e990094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-904c91a35e427a6bb3f58e1e6b143f66"></a>

### [`00c370ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md) → [`00c37148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37148.md) _ZNSt6__ndk111__call_onceERVmPvPFvS2_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md) · 呼出先 4件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md) [`00c5e1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 1件 [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md) · 呼出先 4件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md) [`00c5e2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3716c",
      "incomplete_value": false,
      "site": "00c37178",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c370d0",
      "incomplete_value": false,
      "site": "00c370dc",
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
            "const:9b0:8"
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
      "definition_site": "00c371f0",
      "incomplete_value": false,
      "site": "00c371f4",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37154",
      "incomplete_value": false,
      "site": "00c37158",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37204",
      "incomplete_value": false,
      "site": "00c37208",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37168",
      "incomplete_value": false,
      "site": "00c3716c",
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
            "const:9b0:8"
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
      "00c3716c",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c37198",
      "PARAM",
      [
        "storage",
        "011289d8",
        null,
        null
      ]
    ],
    [
      "00c3719c",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3716c",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c37198",
      "PARAM",
      [
        "storage",
        "01128ad8",
        null,
        null
      ]
    ],
    [
      "00c3719c",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c370d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c370d0) · [`00c370dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c370dc) · [`00c370f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c370f0)
- 新版 `00c3716c`（命令位置の公開資料なし） · `00c37178`（命令位置の公開資料なし） · `00c3718c`（命令位置の公開資料なし）

~~~diff
- 00c370d0 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00c370d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c370d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c370d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c3716c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00c3716c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c3716c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c3716c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c370d0 bytes 00c02691
+ 00c3716c bytes 00c02a91
- 00c370dc ["INT_ADD", "register:40f0:8", ["const:c370dc:8", "const:4:8"]]
- 00c370dc ["CALL", null, ["callee:00c5b770:8"]]
+ 00c37178 ["INT_ADD", "register:40f0:8", ["const:c37178:8", "const:4:8"]]
+ 00c37178 ["CALL", null, ["callee:00c5b770:8"]]
- 00c370dc bytes 71910094
+ 00c37178 bytes 7e910094
- 00c370f0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00c370f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00c370f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00c370f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00c3718c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00c3718c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c3718c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c3718c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00c370f0 bytes d6622791
+ 00c3718c bytes d6622b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd65ff946ebad0b956f3084ede1e8af"></a>

### [`00c371c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md) → [`00c3725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3725c.md) FUN_00c3725c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3727c",
      "incomplete_value": false,
      "site": "00c37280",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c371e0",
      "incomplete_value": false,
      "site": "00c371e4",
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
            "const:9b0:8"
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
      "definition_site": "00c37290",
      "incomplete_value": false,
      "site": "00c37294",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c371f4",
      "incomplete_value": false,
      "site": "00c371f8",
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
            "const:9b0:8"
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
      "definition_site": "00c3729c",
      "incomplete_value": false,
      "site": "00c372a0",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37200",
      "incomplete_value": false,
      "site": "00c37204",
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
            "const:9d8:8"
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
      "00c3727c",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c37290",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c3729c",
      "PARAM",
      [
        "storage",
        "011289d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3727c",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c37290",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c3729c",
      "PARAM",
      [
        "storage",
        "01128ad8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c371e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c371e4) · [`00c371f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c371f8) · [`00c37204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c37204)
- 新版 `00c37280`（命令位置の公開資料なし） · `00c37294`（命令位置の公開資料なし） · `00c372a0`（命令位置の公開資料なし）

~~~diff
- 00c371e4 ["INT_ADD", "register:40f0:8", ["const:c371e4:8", "const:4:8"]]
- 00c371e4 ["CALL", null, ["callee:00c5b770:8"]]
+ 00c37280 ["INT_ADD", "register:40f0:8", ["const:c37280:8", "const:4:8"]]
+ 00c37280 ["CALL", null, ["callee:00c5b770:8"]]
- 00c371e4 bytes 2f910094
+ 00c37280 bytes 3c910094
- 00c371f8 ["INT_ADD", "register:40f0:8", ["const:c371f8:8", "const:4:8"]]
- 00c371f8 ["CALL", null, ["callee:00c5b780:8"]]
+ 00c37294 ["INT_ADD", "register:40f0:8", ["const:c37294:8", "const:4:8"]]
+ 00c37294 ["CALL", null, ["callee:00c5b780:8"]]
- 00c371f8 bytes 2e910094
+ 00c37294 bytes 3b910094
- 00c37204 ["INT_ADD", "register:40f0:8", ["const:c37204:8", "const:4:8"]]
- 00c37204 ["CALL", null, ["callee:00c5e290:8"]]
+ 00c372a0 ["INT_ADD", "register:40f0:8", ["const:c372a0:8", "const:4:8"]]
+ 00c372a0 ["CALL", null, ["callee:00c5e290:8"]]
- 00c37204 bytes ef9b0094
+ 00c372a0 bytes fc9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b9bffdcb2e960df75b18ff696fe649"></a>

### [`00c372bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md) → [`00c37358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37358.md) _ZNSt6__ndk120__get_collation_nameEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a800.md) · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 1件 [`00c5a8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8d0.md) · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c373bc",
      "incomplete_value": true,
      "site": "00c373c4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37320",
      "incomplete_value": true,
      "site": "00c37328",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "00c37390",
      "READ",
      [
        "storage",
        "00c96148",
        null,
        "pointer"
      ]
    ],
    [
      "00c37390",
      "PARAM",
      [
        "storage",
        "002b700d",
        null,
        "string"
      ]
    ],
    [
      "00c37390",
      "READ",
      [
        "storage",
        "00c95f88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37390",
      "READ",
      [
        "storage",
        "00c96218",
        null,
        "pointer"
      ]
    ],
    [
      "00c37390",
      "PARAM",
      [
        "storage",
        "002b704d",
        null,
        "string"
      ]
    ],
    [
      "00c37390",
      "READ",
      [
        "storage",
        "00c96058",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c372e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c372e4) · [`00c372f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c372f8) · [`00c37318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c37318)
- 新版 `00c37380`（命令位置の公開資料なし） · `00c37394`（命令位置の公開資料なし） · `00c373b4`（命令位置の公開資料なし）

~~~diff
- 00c372e4 ["COPY", "register:40a8:8", ["const:c95dd8:8"]]
+ 00c37380 ["COPY", "register:40a8:8", ["const:c95ea8:8"]]
- 00c372e4 bytes b5572f10
+ 00c37380 bytes 55592f10
- 00c372f8 ["INT_ADD", "register:40f0:8", ["const:c372f8:8", "const:4:8"]]
- 00c372f8 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c37394 ["INT_ADD", "register:40f0:8", ["const:c37394:8", "const:4:8"]]
+ 00c37394 ["CALL", null, ["callee:00c5b920:8"]]
- 00c372f8 bytes 56910094
+ 00c37394 bytes 63910094
- 00c37318 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00c37318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c37318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c37318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c373b4 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00c373b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c373b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c373b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c37318 bytes 08211391
+ 00c373b4 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a08279ef05063aaedc6639cd708942c0"></a>

### [`00c37364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md) → [`00c37400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37400.md) _ZNSt6__ndk115__get_classnameEPKcb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a810.md) · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 1件 [`00c5a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8e0.md) · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c37460",
      "incomplete_value": true,
      "site": "00c37464",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c373c4",
      "incomplete_value": true,
      "site": "00c373c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "00c37438",
      "READ",
      [
        "storage",
        "00c96538",
        null,
        "pointer"
      ]
    ],
    [
      "00c37438",
      "PARAM",
      [
        "storage",
        "002b37ff",
        null,
        "string"
      ]
    ],
    [
      "00c37438",
      "READ",
      [
        "storage",
        "00c964f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37438",
      "READ",
      [
        "storage",
        "00c96608",
        null,
        "pointer"
      ]
    ],
    [
      "00c37438",
      "PARAM",
      [
        "storage",
        "002b3830",
        null,
        "string"
      ]
    ],
    [
      "00c37438",
      "READ",
      [
        "storage",
        "00c965c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c3738c) · [`00c373a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c373a0) · [`00c373c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c373c0)
- 新版 `00c37428`（命令位置の公開資料なし） · `00c3743c`（命令位置の公開資料なし） · `00c3745c`（命令位置の公開資料なし）

~~~diff
- 00c3738c ["COPY", "register:40a8:8", ["const:c964c8:8"]]
+ 00c37428 ["COPY", "register:40a8:8", ["const:c96598:8"]]
- 00c3738c bytes f5892f10
+ 00c37428 bytes 958b2f10
- 00c373a0 ["INT_ADD", "register:40f0:8", ["const:c373a0:8", "const:4:8"]]
- 00c373a0 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c3743c ["INT_ADD", "register:40f0:8", ["const:c3743c:8", "const:4:8"]]
+ 00c3743c ["CALL", null, ["callee:00c5b920:8"]]
- 00c373a0 bytes 2c910094
+ 00c3743c bytes 39910094
- 00c373c0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00c373c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c373c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c373c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3745c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00c3745c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3745c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3745c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c373c0 bytes 08e11691
+ 00c3745c bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aecbc42452af6527d9d76a54bb1377e7"></a>

### [`00c374c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md) → [`00c37564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37564.md) __cxa_bad_cast

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ce0.md) · 呼出先 4件 [`00c37f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f6c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e480.md)
- 新版 呼出元 1件 [`00c59db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59db0.md) · 呼出先 4件 [`00c38008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38008.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e550.md)

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
      "definition_site": "00c37590",
      "incomplete_value": true,
      "site": "00c37598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c374f4",
      "incomplete_value": true,
      "site": "00c374fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
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
      "definition_site": "00c37594",
      "incomplete_value": true,
      "site": "00c37598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c374f8",
      "incomplete_value": true,
      "site": "00c374fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
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
      "00c37590",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00c37590",
      "PARAM",
      [
        "storage",
        "00c96988",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37594",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37590",
      "READ",
      [
        "storage",
        "00c9bc30",
        null,
        "pointer"
      ]
    ],
    [
      "00c37590",
      "PARAM",
      [
        "storage",
        "00c96a58",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37594",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c374fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374fc) · [`00c374dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374dc) · [`00c374e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374e4)
- 新版 `00c37598`（命令位置の公開資料なし） · `00c37578`（命令位置の公開資料なし） · `00c37580`（命令位置の公開資料なし）

~~~diff
- 00c374fc ["INT_ADD", "register:40f0:8", ["const:c374fc:8", "const:4:8"]]
- 00c374fc ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c37598 ["INT_ADD", "register:40f0:8", ["const:c37598:8", "const:4:8"]]
+ 00c37598 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c374fc bytes 85820094
+ 00c37598 bytes 92820094
- 00c374dc ["INT_ADD", "register:40f0:8", ["const:c374dc:8", "const:4:8"]]
- 00c374dc ["CALL", null, ["callee:00c57fc0:8"]]
+ 00c37578 ["INT_ADD", "register:40f0:8", ["const:c37578:8", "const:4:8"]]
+ 00c37578 ["CALL", null, ["callee:00c57fc0:8"]]
- 00c374dc bytes 85820094
+ 00c37578 bytes 92820094
- 00c374e4 ["INT_ADD", "register:40f0:8", ["const:c374e4:8", "const:4:8"]]
- 00c374e4 ["CALL", null, ["callee:00c5e550:8"]]
+ 00c37580 ["INT_ADD", "register:40f0:8", ["const:c37580:8", "const:4:8"]]
+ 00c37580 ["CALL", null, ["callee:00c5e550:8"]]
- 00c374e4 bytes e79b0094
+ 00c37580 bytes f49b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00566f9f77cf43888ae3617e4e8f8d57"></a>

### [`00c37500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md) → [`00c3759c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3759c.md) __cxa_bad_typeid

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c37fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fc8.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c38064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38064.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee40.md)

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
      "definition_site": "00c375c8",
      "incomplete_value": true,
      "site": "00c375d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3752c",
      "incomplete_value": true,
      "site": "00c37534",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00c375cc",
      "incomplete_value": true,
      "site": "00c375d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37530",
      "incomplete_value": true,
      "site": "00c37534",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
      "00c375c8",
      "READ",
      [
        "storage",
        "00c9be18",
        null,
        "pointer"
      ]
    ],
    [
      "00c375c8",
      "PARAM",
      [
        "storage",
        "00c969a0",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c375cc",
      "READ",
      [
        "storage",
        "00c9be20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c375c8",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "00c375c8",
      "PARAM",
      [
        "storage",
        "00c96a70",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c375cc",
      "READ",
      [
        "storage",
        "00c9bef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c37534) · [`00c37514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c37514) · [`00c3751c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c3751c)
- 新版 `00c375d0`（命令位置の公開資料なし） · `00c375b0`（命令位置の公開資料なし） · `00c375b8`（命令位置の公開資料なし）

~~~diff
- 00c37534 ["INT_ADD", "register:40f0:8", ["const:c37534:8", "const:4:8"]]
- 00c37534 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c375d0 ["INT_ADD", "register:40f0:8", ["const:c375d0:8", "const:4:8"]]
+ 00c375d0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c37534 bytes 77820094
+ 00c375d0 bytes 84820094
- 00c37514 ["INT_ADD", "register:40f0:8", ["const:c37514:8", "const:4:8"]]
- 00c37514 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00c375b0 ["INT_ADD", "register:40f0:8", ["const:c375b0:8", "const:4:8"]]
+ 00c375b0 ["CALL", null, ["callee:00c57fc0:8"]]
- 00c37514 bytes 77820094
+ 00c375b0 bytes 84820094
- 00c3751c ["INT_ADD", "register:40f0:8", ["const:c3751c:8", "const:4:8"]]
- 00c3751c ["CALL", null, ["callee:00c5ee40:8"]]
+ 00c375b8 ["INT_ADD", "register:40f0:8", ["const:c375b8:8", "const:4:8"]]
+ 00c375b8 ["CALL", null, ["callee:00c5ee40:8"]]
- 00c3751c bytes 159e0094
+ 00c375b8 bytes 229e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfc1a8f70f3922733770454e71ba8735"></a>

### [`00c37538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md) → [`00c375d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c375d4.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58100.md)

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
      "definition_site": "00c37600",
      "incomplete_value": true,
      "site": "00c37608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37564",
      "incomplete_value": true,
      "site": "00c3756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
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
      "definition_site": "00c37604",
      "incomplete_value": true,
      "site": "00c37608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37568",
      "incomplete_value": true,
      "site": "00c3756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
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
      "00c37600",
      "READ",
      [
        "storage",
        "00c9abd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c37600",
      "PARAM",
      [
        "storage",
        "00c966b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37604",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37600",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c37600",
      "PARAM",
      [
        "storage",
        "00c96780",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37604",
      "READ",
      [
        "storage",
        "00c9aca8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3756c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c3756c) · [`00c3754c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c3754c) · [`00c37554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c37554)
- 新版 `00c37608`（命令位置の公開資料なし） · `00c375e8`（命令位置の公開資料なし） · `00c375f0`（命令位置の公開資料なし）

~~~diff
- 00c3756c ["INT_ADD", "register:40f0:8", ["const:c3756c:8", "const:4:8"]]
- 00c3756c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c37608 ["INT_ADD", "register:40f0:8", ["const:c37608:8", "const:4:8"]]
+ 00c37608 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c3756c bytes 69820094
+ 00c37608 bytes 76820094
- 00c3754c ["INT_ADD", "register:40f0:8", ["const:c3754c:8", "const:4:8"]]
- 00c3754c ["CALL", null, ["callee:00c57fc0:8"]]
+ 00c375e8 ["INT_ADD", "register:40f0:8", ["const:c375e8:8", "const:4:8"]]
+ 00c375e8 ["CALL", null, ["callee:00c57fc0:8"]]
- 00c3754c bytes 69820094
+ 00c375e8 bytes 76820094
- 00c37554 ["INT_ADD", "register:40f0:8", ["const:c37554:8", "const:4:8"]]
- 00c37554 ["CALL", null, ["callee:00c58100:8"]]
+ 00c375f0 ["INT_ADD", "register:40f0:8", ["const:c375f0:8", "const:4:8"]]
+ 00c375f0 ["CALL", null, ["callee:00c58100:8"]]
- 00c37554 bytes b7820094
+ 00c375f0 bytes c4820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5b7ca050acc57d72c89fef3d1994eb7"></a>

### [`00c37570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md) → [`00c3760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md) __cxa_guard_acquire

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) · 呼出先 5件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1d0.md) [`00c5edb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5edb0.md)
- 新版 呼出元 1件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) · 呼出先 5件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2a0.md) [`00c5ee80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c37640",
      "incomplete_value": false,
      "site": "00c3764c",
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
            "const:eb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c375a4",
      "incomplete_value": false,
      "site": "00c375b0",
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
            "const:e76:8"
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
      "definition_site": "00c37648",
      "incomplete_value": false,
      "site": "00c37650",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c375ac",
      "incomplete_value": false,
      "site": "00c375b4",
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
            "const:a08:8"
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
      "definition_site": "00c376d0",
      "incomplete_value": false,
      "site": "00c376d4",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37634",
      "incomplete_value": false,
      "site": "00c37638",
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
            "const:a08:8"
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
      "00c37648",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c3764c",
      "DATA",
      [
        "storage",
        "002b7e76",
        null,
        "string"
      ]
    ],
    [
      "00c37698",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37648",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c3764c",
      "DATA",
      [
        "storage",
        "002b7eb6",
        null,
        "string"
      ]
    ],
    [
      "00c37698",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c375b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c375b4) · [`00c37638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c37638) · [`00c37688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c37688)
- 新版 `00c37650`（命令位置の公開資料なし） · `00c376d4`（命令位置の公開資料なし） · `00c37724`（命令位置の公開資料なし）

~~~diff
- 00c375b4 ["INT_ADD", "register:40f0:8", ["const:c375b4:8", "const:4:8"]]
- 00c375b4 ["CALL", null, ["callee:00c5b770:8"]]
+ 00c37650 ["INT_ADD", "register:40f0:8", ["const:c37650:8", "const:4:8"]]
+ 00c37650 ["CALL", null, ["callee:00c5b770:8"]]
- 00c375b4 bytes 3b900094
+ 00c37650 bytes 48900094
- 00c37638 ["INT_ADD", "register:40f0:8", ["const:c37638:8", "const:4:8"]]
- 00c37638 ["CALL", null, ["callee:00c5b780:8"]]
+ 00c376d4 ["INT_ADD", "register:40f0:8", ["const:c376d4:8", "const:4:8"]]
+ 00c376d4 ["CALL", null, ["callee:00c5b780:8"]]
- 00c37638 bytes 1e900094
+ 00c376d4 bytes 2b900094
- 00c37688 ["INT_ADD", "register:40f0:8", ["const:c37688:8", "const:4:8"]]
- 00c37688 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c37724 ["INT_ADD", "register:40f0:8", ["const:c37724:8", "const:4:8"]]
+ 00c37724 ["CALL", null, ["callee:00c380a8:8"]]
- 00c37688 bytes 61020094
+ 00c37724 bytes 61020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73d13cbfdfe918d29c807ebe3f2ccd14"></a>

### [`00c376b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md) → [`00c37750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md) __cxa_guard_release

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)
- 新版 呼出元 1件 [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37774",
      "incomplete_value": false,
      "site": "00c37778",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c376d8",
      "incomplete_value": false,
      "site": "00c376dc",
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
            "const:a08:8"
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
      "definition_site": "00c3778c",
      "incomplete_value": false,
      "site": "00c37790",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c376f0",
      "incomplete_value": false,
      "site": "00c376f4",
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
            "const:a08:8"
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
      "definition_site": "00c377a0",
      "incomplete_value": false,
      "site": "00c377a4",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37704",
      "incomplete_value": false,
      "site": "00c37708",
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
            "const:a30:8"
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
      "00c37774",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c3778c",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c377a0",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37774",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c3778c",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c377a0",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c376dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c376dc) · [`00c376f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c376f4) · [`00c37708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c37708)
- 新版 `00c37778`（命令位置の公開資料なし） · `00c37790`（命令位置の公開資料なし） · `00c377a4`（命令位置の公開資料なし）

~~~diff
- 00c376dc ["INT_ADD", "register:40f0:8", ["const:c376dc:8", "const:4:8"]]
- 00c376dc ["CALL", null, ["callee:00c5b770:8"]]
+ 00c37778 ["INT_ADD", "register:40f0:8", ["const:c37778:8", "const:4:8"]]
+ 00c37778 ["CALL", null, ["callee:00c5b770:8"]]
- 00c376dc bytes f18f0094
+ 00c37778 bytes fe8f0094
- 00c376f4 ["INT_ADD", "register:40f0:8", ["const:c376f4:8", "const:4:8"]]
- 00c376f4 ["CALL", null, ["callee:00c5b780:8"]]
+ 00c37790 ["INT_ADD", "register:40f0:8", ["const:c37790:8", "const:4:8"]]
+ 00c37790 ["CALL", null, ["callee:00c5b780:8"]]
- 00c376f4 bytes ef8f0094
+ 00c37790 bytes fc8f0094
- 00c37708 ["INT_ADD", "register:40f0:8", ["const:c37708:8", "const:4:8"]]
- 00c37708 ["CALL", null, ["callee:00c5e290:8"]]
+ 00c377a4 ["INT_ADD", "register:40f0:8", ["const:c377a4:8", "const:4:8"]]
+ 00c377a4 ["CALL", null, ["callee:00c5e290:8"]]
- 00c37708 bytes ae9a0094
+ 00c377a4 bytes bb9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03f9facc3f800b3a48a6b194662e29c7"></a>

### [`00c3775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md) → [`00c377f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md) __cxa_guard_abort

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f90.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)
- 新版 呼出元 1件 [`00c58060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58060.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37810",
      "incomplete_value": false,
      "site": "00c37814",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37774",
      "incomplete_value": false,
      "site": "00c37778",
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
            "const:a08:8"
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
      "definition_site": "00c3782c",
      "incomplete_value": false,
      "site": "00c37830",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37790",
      "incomplete_value": false,
      "site": "00c37794",
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
            "const:a08:8"
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
      "definition_site": "00c37840",
      "incomplete_value": false,
      "site": "00c37844",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c377a4",
      "incomplete_value": false,
      "site": "00c377a8",
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
            "const:a30:8"
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
      "00c37810",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c3782c",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c37840",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37810",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c3782c",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c37840",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c37778) · [`00c37794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c37794) · [`00c377a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c377a8)
- 新版 `00c37814`（命令位置の公開資料なし） · `00c37830`（命令位置の公開資料なし） · `00c37844`（命令位置の公開資料なし）

~~~diff
- 00c37778 ["INT_ADD", "register:40f0:8", ["const:c37778:8", "const:4:8"]]
- 00c37778 ["CALL", null, ["callee:00c5b770:8"]]
+ 00c37814 ["INT_ADD", "register:40f0:8", ["const:c37814:8", "const:4:8"]]
+ 00c37814 ["CALL", null, ["callee:00c5b770:8"]]
- 00c37778 bytes ca8f0094
+ 00c37814 bytes d78f0094
- 00c37794 ["INT_ADD", "register:40f0:8", ["const:c37794:8", "const:4:8"]]
- 00c37794 ["CALL", null, ["callee:00c5b780:8"]]
+ 00c37830 ["INT_ADD", "register:40f0:8", ["const:c37830:8", "const:4:8"]]
+ 00c37830 ["CALL", null, ["callee:00c5b780:8"]]
- 00c37794 bytes c78f0094
+ 00c37830 bytes d48f0094
- 00c377a8 ["INT_ADD", "register:40f0:8", ["const:c377a8:8", "const:4:8"]]
- 00c377a8 ["CALL", null, ["callee:00c5e290:8"]]
+ 00c37844 ["INT_ADD", "register:40f0:8", ["const:c37844:8", "const:4:8"]]
+ 00c37844 ["CALL", null, ["callee:00c5e290:8"]]
- 00c377a8 bytes 869a0094
+ 00c37844 bytes 939a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b636a0886661e3d8ca6e38fbb94a477"></a>

### [`00c377f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md) → [`00c37894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md) FUN_00c37894

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c378ac",
      "incomplete_value": false,
      "site": "00c378b0",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37810",
      "incomplete_value": false,
      "site": "00c37814",
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
            "const:a08:8"
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
      "definition_site": "00c378d0",
      "incomplete_value": true,
      "site": "00c378d4",
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
            "const:e7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37834",
      "incomplete_value": true,
      "site": "00c37838",
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
            "const:ec7:8"
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
      "00c378ac",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c378d0",
      "PARAM",
      [
        "storage",
        "002a0ec7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c378ac",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c378d0",
      "PARAM",
      [
        "storage",
        "002a0e7a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37814) · [`00c37838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37838) · [`00c37810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37810)
- 新版 `00c378b0`（命令位置の公開資料なし） · `00c378d4`（命令位置の公開資料なし） · `00c378ac`（命令位置の公開資料なし）

~~~diff
- 00c37814 ["INT_ADD", "register:40f0:8", ["const:c37814:8", "const:4:8"]]
- 00c37814 ["CALL", null, ["callee:00c5b780:8"]]
+ 00c378b0 ["INT_ADD", "register:40f0:8", ["const:c378b0:8", "const:4:8"]]
+ 00c378b0 ["CALL", null, ["callee:00c5b780:8"]]
- 00c37814 bytes a78f0094
+ 00c378b0 bytes b48f0094
- 00c37838 ["INT_ADD", "register:40f0:8", ["const:c37838:8", "const:4:8"]]
- 00c37838 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c378d4 ["INT_ADD", "register:40f0:8", ["const:c378d4:8", "const:4:8"]]
+ 00c378d4 ["CALL", null, ["callee:00c380a8:8"]]
- 00c37838 bytes f5010094
+ 00c378d4 bytes f5010094
- 00c37810 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00c37810 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37810 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37810 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c378ac ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00c378ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37810 bytes 00202891
+ 00c378ac bytes 00202c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e9bb93d1b1f597c86a308d828e30b9"></a>

### [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) → [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) FUN_00c37930

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c378b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378b0.md) [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)
- 新版 呼出元 2件 [`00c3794c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3794c.md) [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37944",
      "incomplete_value": true,
      "site": "00c37948",
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
            "const:e7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c378a8",
      "incomplete_value": true,
      "site": "00c378ac",
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
            "const:ec7:8"
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
      "00c37944",
      "PARAM",
      [
        "storage",
        "002a2ec7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37944",
      "PARAM",
      [
        "storage",
        "002a2e7a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c378ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378ac) · [`00c378a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378a0) · [`00c378a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378a8)
- 新版 `00c37948`（命令位置の公開資料なし） · `00c3793c`（命令位置の公開資料なし） · `00c37944`（命令位置の公開資料なし）

~~~diff
- 00c378ac ["INT_ADD", "register:40f0:8", ["const:c378ac:8", "const:4:8"]]
- 00c378ac ["CALL", null, ["callee:00c380a8:8"]]
+ 00c37948 ["INT_ADD", "register:40f0:8", ["const:c37948:8", "const:4:8"]]
+ 00c37948 ["CALL", null, ["callee:00c380a8:8"]]
- 00c378ac bytes d8010094
+ 00c37948 bytes d8010094
- 00c378a0 ["COPY", "register:0:8", ["register:4000:8"]]
- 00c378a0 ["INT_ADD", "register:40f0:8", ["const:c378a0:8", "const:4:8"]]
- 00c378a0 ["CALLIND", null, ["register:0:8"]]
+ 00c3793c ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c3793c ["INT_ADD", "register:40f0:8", ["const:c3793c:8", "const:4:8"]]
+ 00c3793c ["CALLIND", null, ["register:0:8"]]
- 00c378a0 bytes 00003fd6
+ 00c3793c bytes 00003fd6
- 00c378a8 ["COPY", "tmp:0:8", ["const:ec7:8"]]
- 00c378a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c378a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c378a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37944 ["COPY", "tmp:0:8", ["const:e7a:8"]]
+ 00c37944 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37944 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37944 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c378a8 bytes 001c3b91
+ 00c37944 bytes 00e83991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152d96da46a078c42c9d5a5dd8c59ced"></a>

### [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) → [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) FUN_00c3797c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00c37854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37854.md) [`00c51ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md) [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) [`00c522c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md) [`00c52578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md) · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)
- 新版 呼出元 8件 [`00c378f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378f0.md) [`00c52094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md) [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) [`00c52364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md) [`00c52614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md) · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37990",
      "incomplete_value": false,
      "site": "00c37994",
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
            "const:8f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c378f4",
      "incomplete_value": false,
      "site": "00c378f8",
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
            "const:94f:8"
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
      "00c37990",
      "PARAM",
      [
        "storage",
        "002a894f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37990",
      "PARAM",
      [
        "storage",
        "002a88f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c378f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378f8) · [`00c378ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378ec) · [`00c378f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378f4)
- 新版 `00c37994`（命令位置の公開資料なし） · `00c37988`（命令位置の公開資料なし） · `00c37990`（命令位置の公開資料なし）

~~~diff
- 00c378f8 ["INT_ADD", "register:40f0:8", ["const:c378f8:8", "const:4:8"]]
- 00c378f8 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c37994 ["INT_ADD", "register:40f0:8", ["const:c37994:8", "const:4:8"]]
+ 00c37994 ["CALL", null, ["callee:00c380a8:8"]]
- 00c378f8 bytes c5010094
+ 00c37994 bytes c5010094
- 00c378ec ["COPY", "register:0:8", ["register:4000:8"]]
- 00c378ec ["INT_ADD", "register:40f0:8", ["const:c378ec:8", "const:4:8"]]
- 00c378ec ["CALLIND", null, ["register:0:8"]]
+ 00c37988 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c37988 ["INT_ADD", "register:40f0:8", ["const:c37988:8", "const:4:8"]]
+ 00c37988 ["CALLIND", null, ["register:0:8"]]
- 00c378ec bytes 00003fd6
+ 00c37988 bytes 00003fd6
- 00c378f4 ["COPY", "tmp:0:8", ["const:94f:8"]]
- 00c378f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c378f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c378f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37990 ["COPY", "tmp:0:8", ["const:8f3:8"]]
+ 00c37990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c378f4 bytes 003c2591
+ 00c37990 bytes 00cc2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653f1f079b33a7075612b5a55f0302b7"></a>

### [`00c37924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md) → [`00c379c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md) FUN_00c379c0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c37854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37854.md) [`00c378cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378cc.md) [`00c37ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ac4.md) · 呼出先 6件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c38330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c51e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e54.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 3件 [`00c378f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378f0.md) [`00c37968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37968.md) [`00c37b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b60.md) · 呼出先 6件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c383cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c51ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ef0.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c379e8",
      "incomplete_value": false,
      "site": "00c379ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:faa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3794c",
      "incomplete_value": false,
      "site": "00c37950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:f6a:8"
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
      "definition_site": "00c37a2c",
      "incomplete_value": false,
      "site": "00c37a34",
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
            "const:861:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37990",
      "incomplete_value": false,
      "site": "00c37998",
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
            "const:8bd:8"
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
      "definition_site": "00c37a30",
      "incomplete_value": true,
      "site": "00c37a34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37994",
      "incomplete_value": true,
      "site": "00c37998",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:880:8"
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
      "00c379e8",
      "PARAM",
      [
        "storage",
        "002c1f6a",
        null,
        "string"
      ]
    ],
    [
      "00c37a2c",
      "PARAM",
      [
        "storage",
        "002b08bd",
        null,
        "string"
      ]
    ],
    [
      "00c37a30",
      "READ",
      [
        "storage",
        "00ca4880",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c379e8",
      "PARAM",
      [
        "storage",
        "002c1faa",
        null,
        "string"
      ]
    ],
    [
      "00c37a2c",
      "PARAM",
      [
        "storage",
        "002b0861",
        null,
        "string"
      ]
    ],
    [
      "00c37a30",
      "READ",
      [
        "storage",
        "00ca4950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37950) · [`00c37990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37990) · [`00c37998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37998)
- 新版 `00c379ec`（命令位置の公開資料なし） · `00c37a2c`（命令位置の公開資料なし） · `00c37a34`（命令位置の公開資料なし）

~~~diff
- 00c37950 ["INT_ADD", "register:40f0:8", ["const:c37950:8", "const:4:8"]]
- 00c37950 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c379ec ["INT_ADD", "register:40f0:8", ["const:c379ec:8", "const:4:8"]]
+ 00c379ec ["CALL", null, ["callee:00c380a8:8"]]
- 00c37950 bytes af010094
+ 00c379ec bytes af010094
- 00c37990 ["COPY", "tmp:0:8", ["const:8bd:8"]]
- 00c37990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37a2c ["COPY", "tmp:0:8", ["const:861:8"]]
+ 00c37a2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37a2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37a2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37990 bytes 00f42291
+ 00c37a2c bytes 00842191
- 00c37998 ["INT_ADD", "register:40f0:8", ["const:c37998:8", "const:4:8"]]
- 00c37998 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c37a34 ["INT_ADD", "register:40f0:8", ["const:c37a34:8", "const:4:8"]]
+ 00c37a34 ["CALL", null, ["callee:00c380a8:8"]]
- 00c37998 bytes 9d010094
+ 00c37a34 bytes 9d010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97d7d67e01a4c9f28fe6389aa0a3196"></a>

### [`00c37a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md) → [`00c37b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b0c.md) FUN_00c37b0c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c37840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37840.md) [`00c378b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378b0.md) [`00c37a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a90.md) · 呼出先 1件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 3件 [`00c378dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378dc.md) [`00c3794c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3794c.md) [`00c37b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b2c.md) · 呼出先 1件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37b24",
      "incomplete_value": false,
      "site": "00c37b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37a88",
      "incomplete_value": false,
      "site": "00c37a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c37b20",
      "incomplete_value": false,
      "site": "00c37b24",
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
            "const:86a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37a84",
      "incomplete_value": false,
      "site": "00c37a88",
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
            "const:8c6:8"
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
      "00c37b24",
      "WRITE",
      [
        "storage",
        "00ca4880",
        null,
        "pointer"
      ]
    ],
    [
      "00c37b24",
      "DATA",
      [
        "storage",
        "002b18c6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37b24",
      "WRITE",
      [
        "storage",
        "00ca4950",
        null,
        "pointer"
      ]
    ],
    [
      "00c37b24",
      "DATA",
      [
        "storage",
        "002b186a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a88) · [`00c37a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a84) · [`00c37a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a8c)
- 新版 `00c37b24`（命令位置の公開資料なし） · `00c37b20`（命令位置の公開資料なし） · `00c37b28`（命令位置の公開資料なし）

~~~diff
- 00c37a88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:880:8"]]
- 00c37a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c37b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00c37b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c37a88 bytes 094104f9
+ 00c37b24 bytes 09a904f9
- 00c37a84 ["COPY", "tmp:0:8", ["const:8c6:8"]]
- 00c37a84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c37a84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c37a84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c37b20 ["COPY", "tmp:0:8", ["const:86a:8"]]
+ 00c37b20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c37b20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c37b20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c37a84 bytes 29192391
+ 00c37b20 bytes 29a92191
- 00c37a8c ["INT_ADD", "register:40f0:8", ["const:c37a8c:8", "const:4:8"]]
- 00c37a8c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c37b28 ["INT_ADD", "register:40f0:8", ["const:c37b28:8", "const:4:8"]]
+ 00c37b28 ["CALL", null, ["callee:00c580f0:8"]]
- 00c37a8c bytes 65810094
+ 00c37b28 bytes 72810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60964bc54d7f771979038a6c4ec88243"></a>

### [`00c37b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md) → [`00c37c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c28.md) __cxa_deleted_virtual

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)

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
      "definition_site": "00c37c38",
      "incomplete_value": false,
      "site": "00c37c3c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37b9c",
      "incomplete_value": false,
      "site": "00c37ba0",
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
            "const:da8:8"
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
      "00c37c38",
      "PARAM",
      [
        "storage",
        "002b5da8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37c38",
      "PARAM",
      [
        "storage",
        "002b5de8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md#insn-00c37ba0) · [`00c37b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md#insn-00c37b9c)
- 新版 `00c37c3c`（命令位置の公開資料なし） · `00c37c38`（命令位置の公開資料なし）

~~~diff
- 00c37ba0 ["INT_ADD", "register:40f0:8", ["const:c37ba0:8", "const:4:8"]]
- 00c37ba0 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c37c3c ["INT_ADD", "register:40f0:8", ["const:c37c3c:8", "const:4:8"]]
+ 00c37c3c ["CALL", null, ["callee:00c380a8:8"]]
- 00c37ba0 bytes 1b010094
+ 00c37c3c bytes 1b010094
- 00c37b9c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00c37b9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37b9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37b9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37c38 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00c37c38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37b9c bytes 00a03691
+ 00c37c38 bytes 00a03791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adf48573b502c6a574793c7faf8956f5"></a>

### [`00c37bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bd8.md) → [`00c37c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c74.md) _ZNKSt9exception4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37c7c",
      "incomplete_value": false,
      "site": "00c37c80",
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
            "const:dff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37be0",
      "incomplete_value": false,
      "site": "00c37be4",
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
            "const:e4c:8"
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
      "00c37c7c",
      "DATA",
      [
        "storage",
        "002a3e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37c7c",
      "DATA",
      [
        "storage",
        "002a3dff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bd8.md#insn-00c37be0)
- 新版 `00c37c7c`（命令位置の公開資料なし）

~~~diff
- 00c37be0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00c37be0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37be0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37be0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37c7c ["COPY", "tmp:0:8", ["const:dff:8"]]
+ 00c37c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37be0 bytes 00303991
+ 00c37c7c bytes 00fc3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b09d5231e563b2ecdcaa09148d734d"></a>

### [`00c37c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c14.md) → [`00c37cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cb0.md) _ZNKSt13bad_exception4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37cb8",
      "incomplete_value": false,
      "site": "00c37cbc",
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
            "const:51d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c1c",
      "incomplete_value": false,
      "site": "00c37c20",
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
            "const:579:8"
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
      "00c37cb8",
      "DATA",
      [
        "storage",
        "002ae579",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37cb8",
      "DATA",
      [
        "storage",
        "002ae51d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c14.md#insn-00c37c1c)
- 新版 `00c37cb8`（命令位置の公開資料なし）

~~~diff
- 00c37c1c ["COPY", "tmp:0:8", ["const:579:8"]]
- 00c37c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37cb8 ["COPY", "tmp:0:8", ["const:51d:8"]]
+ 00c37cb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37cb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37cb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37c1c bytes 00e41591
+ 00c37cb8 bytes 00741491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d746b1b37b34289344a50b6a7646553a"></a>

### [`00c37c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c68.md) → [`00c37d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d04.md) _ZNKSt9bad_alloc4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37d0c",
      "incomplete_value": false,
      "site": "00c37d10",
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
            "const:b04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c70",
      "incomplete_value": false,
      "site": "00c37c74",
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
            "const:b60:8"
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
      "00c37d0c",
      "DATA",
      [
        "storage",
        "002aab60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37d0c",
      "DATA",
      [
        "storage",
        "002aab04",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c68.md#insn-00c37c70)
- 新版 `00c37d0c`（命令位置の公開資料なし）

~~~diff
- 00c37c70 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00c37c70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37d0c ["COPY", "tmp:0:8", ["const:b04:8"]]
+ 00c37d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37c70 bytes 00802d91
+ 00c37d0c bytes 00102c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a45321ca5e311df00316eee71b14f832"></a>

### [`00c37cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37cbc.md) → [`00c37d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d58.md) _ZNKSt20bad_array_new_length4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37d60",
      "incomplete_value": false,
      "site": "00c37d64",
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
            "const:1bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37cc4",
      "incomplete_value": false,
      "site": "00c37cc8",
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
            "const:21b:8"
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
      "00c37d60",
      "DATA",
      [
        "storage",
        "002a521b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37d60",
      "DATA",
      [
        "storage",
        "002a51bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37cbc.md#insn-00c37cc4)
- 新版 `00c37d60`（命令位置の公開資料なし）

~~~diff
- 00c37cc4 ["COPY", "tmp:0:8", ["const:21b:8"]]
- 00c37cc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37cc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37cc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37d60 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00c37d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37cc4 bytes 006c0891
+ 00c37d60 bytes 00fc0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca5ea487045b90e371140303e817516"></a>

### [`00c37ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md) → [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) _ZNSt12out_of_rangeD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c57f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f00.md) · 呼出先 3件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 10件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c57fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fd0.md) · 呼出先 3件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00c37d88",
      "incomplete_value": true,
      "site": "00c37d90",
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
      "definition_site": "00c37cec",
      "incomplete_value": true,
      "site": "00c37cf4",
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
      "00c37d80",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00c37d90",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37d80",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00c37d90",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37ce4) · [`00c37cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37cfc) · [`00c37d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37d0c)
- 新版 `00c37d80`（命令位置の公開資料なし） · `00c37d98`（命令位置の公開資料なし） · `00c37da8`（命令位置の公開資料なし）

~~~diff
- 00c37ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00c37ce4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c37d80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
+ 00c37d80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37ce4 bytes 084945f9
+ 00c37d80 bytes 08b145f9
- 00c37cfc ["INT_ADD", "register:40f0:8", ["const:c37cfc:8", "const:4:8"]]
- 00c37cfc ["CALL", null, ["callee:00c53d40:8"]]
+ 00c37d98 ["INT_ADD", "register:40f0:8", ["const:c37d98:8", "const:4:8"]]
+ 00c37d98 ["CALL", null, ["callee:00c53d40:8"]]
- 00c37cfc bytes e96f0094
+ 00c37d98 bytes ea6f0094
- 00c37d0c ["INT_ADD", "register:40f0:8", ["const:c37d0c:8", "const:4:8"]]
- 00c37d0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00c37da8 ["INT_ADD", "register:40f0:8", ["const:c37da8:8", "const:4:8"]]
+ 00c37da8 ["CALL", null, ["callee:00c57f80:8"]]
- 00c37d0c bytes 69800094
+ 00c37da8 bytes 76800094
~~~


<a id="compare-288307eaf14eccd9de62338debe32b72"></a>

### [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) → [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) _ZNSt13runtime_errorD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md) [`00bf0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md) [`00c5a8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8c0.md) [`00c5df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df70.md) · 呼出先 3件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 8件 [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md) [`00bf0b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md) [`00c5a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a990.md) [`00c5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e040.md) · 呼出先 3件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00c37e18",
      "incomplete_value": true,
      "site": "00c37e20",
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
      "definition_site": "00c37d7c",
      "incomplete_value": true,
      "site": "00c37d84",
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
      "00c37e10",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00c37e20",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37e10",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00c37e20",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d74) · [`00c37d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d8c) · [`00c37d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d9c)
- 新版 `00c37e10`（命令位置の公開資料なし） · `00c37e28`（命令位置の公開資料なし） · `00c37e38`（命令位置の公開資料なし）

~~~diff
- 00c37d74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 00c37d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c37e10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
+ 00c37e10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37d74 bytes 084d45f9
+ 00c37e10 bytes 08b545f9
- 00c37d8c ["INT_ADD", "register:40f0:8", ["const:c37d8c:8", "const:4:8"]]
- 00c37d8c ["CALL", null, ["callee:00c53d40:8"]]
+ 00c37e28 ["INT_ADD", "register:40f0:8", ["const:c37e28:8", "const:4:8"]]
+ 00c37e28 ["CALL", null, ["callee:00c53d40:8"]]
- 00c37d8c bytes c56f0094
+ 00c37e28 bytes c66f0094
- 00c37d9c ["INT_ADD", "register:40f0:8", ["const:c37d9c:8", "const:4:8"]]
- 00c37d9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00c37e38 ["INT_ADD", "register:40f0:8", ["const:c37e38:8", "const:4:8"]]
+ 00c37e38 ["CALL", null, ["callee:00c57f80:8"]]
- 00c37d9c bytes 45800094
+ 00c37e38 bytes 52800094
~~~


<a id="compare-98049cba6ba55345a7d319202f3a0174"></a>

### [`00c37ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ffc.md) → [`00c38098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38098.md) _ZNKSt10bad_typeid4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c380a0",
      "incomplete_value": false,
      "site": "00c380a4",
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
            "const:a87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38004",
      "incomplete_value": false,
      "site": "00c38008",
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
            "const:adb:8"
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
      "00c380a0",
      "DATA",
      [
        "storage",
        "002beadb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c380a0",
      "DATA",
      [
        "storage",
        "002bea87",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ffc.md#insn-00c38004)
- 新版 `00c380a0`（命令位置の公開資料なし）

~~~diff
- 00c38004 ["COPY", "tmp:0:8", ["const:adb:8"]]
- 00c38004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c38004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c38004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c380a0 ["COPY", "tmp:0:8", ["const:a87:8"]]
+ 00c380a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c380a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c380a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c38004 bytes 006c2b91
+ 00c380a0 bytes 001c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e57f276f9be2a41b28d8aad474d6391"></a>

### [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) → [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) FUN_00c380a8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`00c37570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md) [`00c376b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md) [`00c3775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md) [`00c377f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md) [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) · 呼出先 10件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md) [`00c5a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a280.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e700.md) [`00c5ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee70.md)
- 新版 呼出元 22件 [`00c3760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md) [`00c37750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md) [`00c377f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md) [`00c37894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md) [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) · 呼出先 10件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5a350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a350.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e7d0.md) [`00c5ef40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c380dc",
      "incomplete_value": false,
      "site": "00c38108",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38040",
      "incomplete_value": false,
      "site": "00c3806c",
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
            "const:e08:8"
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
      "definition_site": "00c38104",
      "incomplete_value": true,
      "site": "00c38108",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38068",
      "incomplete_value": true,
      "site": "00c3806c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38180",
      "incomplete_value": false,
      "site": "00c3818c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c380e4",
      "incomplete_value": false,
      "site": "00c380f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b3c:8"
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
      "00c380dc",
      "PARAM",
      [
        "storage",
        "002c0e08",
        null,
        "string"
      ]
    ],
    [
      "00c38100",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38180",
      "PARAM",
      [
        "storage",
        "002bfb3c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c380dc",
      "PARAM",
      [
        "storage",
        "002c0e48",
        null,
        "string"
      ]
    ],
    [
      "00c38100",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c38180",
      "PARAM",
      [
        "storage",
        "002bfae8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c3806c) · [`00c380f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c380f0) · [`00c38104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c38104)
- 新版 `00c38108`（命令位置の公開資料なし） · `00c3818c`（命令位置の公開資料なし） · `00c381a0`（命令位置の公開資料なし）

~~~diff
- 00c3806c ["INT_ADD", "register:40f0:8", ["const:c3806c:8", "const:4:8"]]
- 00c3806c ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c38108 ["INT_ADD", "register:40f0:8", ["const:c38108:8", "const:4:8"]]
+ 00c38108 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c3806c bytes 6d880094
+ 00c38108 bytes 7a880094
- 00c380f0 ["INT_ADD", "register:40f0:8", ["const:c380f0:8", "const:4:8"]]
- 00c380f0 ["CALL", null, ["callee:00c5ef60:8"]]
+ 00c3818c ["INT_ADD", "register:40f0:8", ["const:c3818c:8", "const:4:8"]]
+ 00c3818c ["CALL", null, ["callee:00c5ef60:8"]]
- 00c380f0 bytes 689b0094
+ 00c3818c bytes 759b0094
- 00c38104 ["INT_ADD", "register:40f0:8", ["const:c38104:8", "const:4:8"]]
- 00c38104 ["CALL", null, ["callee:00c5ef70:8"]]
+ 00c381a0 ["INT_ADD", "register:40f0:8", ["const:c381a0:8", "const:4:8"]]
+ 00c381a0 ["CALL", null, ["callee:00c5ef70:8"]]
- 00c38104 bytes 679b0094
+ 00c381a0 bytes 749b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b937e8c6999613b134c6b7c11341736"></a>

### [`00c38330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md) → [`00c383cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md) FUN_00c383cc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c37924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md) · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 1件 [`00c379c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md) · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38410",
      "incomplete_value": true,
      "site": "00c38414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38374",
      "incomplete_value": true,
      "site": "00c38378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
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
      "definition_site": "00c38400",
      "incomplete_value": true,
      "site": "00c38414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38364",
      "incomplete_value": true,
      "site": "00c38378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e80:8"
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
      "00c383fc",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38400",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "00c38400",
      "PARAM",
      [
        "storage",
        "00c969d0",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c383fc",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c38400",
      "READ",
      [
        "storage",
        "00c9bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00c38400",
      "PARAM",
      [
        "storage",
        "00c96aa0",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38378) · [`00c38360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38360) · [`00c38364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38364)
- 新版 `00c38414`（命令位置の公開資料なし） · `00c383fc`（命令位置の公開資料なし） · `00c38400`（命令位置の公開資料なし）

~~~diff
- 00c38378 ["INT_ADD", "register:40f0:8", ["const:c38378:8", "const:4:8"]]
- 00c38378 ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38414 ["INT_ADD", "register:40f0:8", ["const:c38414:8", "const:4:8"]]
+ 00c38414 ["CALL", null, ["callee:00c586e0:8"]]
- 00c38378 bytes a6800094
+ 00c38414 bytes b3800094
- 00c38360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00c38360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c383fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00c383fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c38360 bytes 083d47f9
+ 00c383fc bytes 08a547f9
- 00c38364 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e80:8"]]
- 00c38364 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38400 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:f50:8"]]
+ 00c38400 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00c38364 bytes 424047f9
+ 00c38400 bytes 42a847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

