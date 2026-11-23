# v15.7.3 → v15.7.4 · 最優先の変更候補 (76)

[一覧の目次](README.md)

<a id="compare-ac26061834bc271f4c9baa5105bf6e39"></a>

### [`00b862b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b862b8.md) → [`00b862fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b862fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEs

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86358",
      "incomplete_value": true,
      "site": "00b8635c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86314",
      "incomplete_value": true,
      "site": "00b86318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b863a0",
      "incomplete_value": true,
      "site": "00b863a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8635c",
      "incomplete_value": true,
      "site": "00b86360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86358",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86358",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b863a0",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86358",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86358",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b863a0",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b862b8.md#insn-00b86318) · [`00b8635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b862b8.md#insn-00b8635c) · [`00b86360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b862b8.md#insn-00b86360)
- 新版 `00b8635c`（命令位置の公開資料なし） · `00b863a0`（命令位置の公開資料なし） · `00b863a4`（命令位置の公開資料なし）

~~~diff
- 00b86318 ["INT_ADD", "register:40f0:8", ["const:b86318:8", "const:4:8"]]
- 00b86318 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8635c ["INT_ADD", "register:40f0:8", ["const:b8635c:8", "const:4:8"]]
+ 00b8635c ["CALL", null, ["callee:00bdb430:8"]]
- 00b86318 bytes 32540194
+ 00b8635c bytes 35540194
- 00b8635c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b8635c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b863a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b863a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8635c bytes 216046f9
+ 00b863a0 bytes 218846f9
- 00b86360 ["INT_ADD", "register:40f0:8", ["const:b86360:8", "const:4:8"]]
- 00b86360 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b863a4 ["INT_ADD", "register:40f0:8", ["const:b863a4:8", "const:4:8"]]
+ 00b863a4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86360 bytes 20540194
+ 00b863a4 bytes 23540194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1986c676757348d8f9a6ccc53f93429"></a>

### [`00b86470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86470.md) → [`00b864b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b864b4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEt

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86508",
      "incomplete_value": true,
      "site": "00b8650c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b864c4",
      "incomplete_value": true,
      "site": "00b864c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86550",
      "incomplete_value": true,
      "site": "00b86554",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8650c",
      "incomplete_value": true,
      "site": "00b86510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86508",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86508",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86550",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86508",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86508",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86550",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b864c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86470.md#insn-00b864c8) · [`00b8650c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86470.md#insn-00b8650c) · [`00b86510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86470.md#insn-00b86510)
- 新版 `00b8650c`（命令位置の公開資料なし） · `00b86550`（命令位置の公開資料なし） · `00b86554`（命令位置の公開資料なし）

~~~diff
- 00b864c8 ["INT_ADD", "register:40f0:8", ["const:b864c8:8", "const:4:8"]]
- 00b864c8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8650c ["INT_ADD", "register:40f0:8", ["const:b8650c:8", "const:4:8"]]
+ 00b8650c ["CALL", null, ["callee:00bdb430:8"]]
- 00b864c8 bytes c6530194
+ 00b8650c bytes c9530194
- 00b8650c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b8650c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86550 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86550 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8650c bytes 216046f9
+ 00b86550 bytes 218846f9
- 00b86510 ["INT_ADD", "register:40f0:8", ["const:b86510:8", "const:4:8"]]
- 00b86510 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86554 ["INT_ADD", "register:40f0:8", ["const:b86554:8", "const:4:8"]]
+ 00b86554 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86510 bytes b4530194
+ 00b86554 bytes b7530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02255f05e063015f7c2a7fb03eff9196"></a>

### [`00b86600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86600.md) → [`00b86644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86644.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b866a0",
      "incomplete_value": true,
      "site": "00b866a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8665c",
      "incomplete_value": true,
      "site": "00b86660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b866e8",
      "incomplete_value": true,
      "site": "00b866ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b866a4",
      "incomplete_value": true,
      "site": "00b866a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b866a0",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b866a0",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b866e8",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b866a0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b866a0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b866e8",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86600.md#insn-00b86660) · [`00b866a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86600.md#insn-00b866a4) · [`00b866a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86600.md#insn-00b866a8)
- 新版 `00b866a4`（命令位置の公開資料なし） · `00b866e8`（命令位置の公開資料なし） · `00b866ec`（命令位置の公開資料なし）

~~~diff
- 00b86660 ["INT_ADD", "register:40f0:8", ["const:b86660:8", "const:4:8"]]
- 00b86660 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b866a4 ["INT_ADD", "register:40f0:8", ["const:b866a4:8", "const:4:8"]]
+ 00b866a4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86660 bytes 60530194
+ 00b866a4 bytes 63530194
- 00b866a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b866a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b866e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b866e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b866a4 bytes 216046f9
+ 00b866e8 bytes 218846f9
- 00b866a8 ["INT_ADD", "register:40f0:8", ["const:b866a8:8", "const:4:8"]]
- 00b866a8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b866ec ["INT_ADD", "register:40f0:8", ["const:b866ec:8", "const:4:8"]]
+ 00b866ec ["CALL", null, ["callee:00bdb430:8"]]
- 00b866a8 bytes 4e530194
+ 00b866ec bytes 51530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad9d54142b2987fd7d160a37b940dc2"></a>

### [`00b867b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b867b8.md) → [`00b867fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b867fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86850",
      "incomplete_value": true,
      "site": "00b86854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8680c",
      "incomplete_value": true,
      "site": "00b86810",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86898",
      "incomplete_value": true,
      "site": "00b8689c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86854",
      "incomplete_value": true,
      "site": "00b86858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86850",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86850",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86898",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86850",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86850",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86898",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b867b8.md#insn-00b86810) · [`00b86854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b867b8.md#insn-00b86854) · [`00b86858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b867b8.md#insn-00b86858)
- 新版 `00b86854`（命令位置の公開資料なし） · `00b86898`（命令位置の公開資料なし） · `00b8689c`（命令位置の公開資料なし）

~~~diff
- 00b86810 ["INT_ADD", "register:40f0:8", ["const:b86810:8", "const:4:8"]]
- 00b86810 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86854 ["INT_ADD", "register:40f0:8", ["const:b86854:8", "const:4:8"]]
+ 00b86854 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86810 bytes f4520194
+ 00b86854 bytes f7520194
- 00b86854 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b86854 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86898 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86898 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b86854 bytes 216046f9
+ 00b86898 bytes 218846f9
- 00b86858 ["INT_ADD", "register:40f0:8", ["const:b86858:8", "const:4:8"]]
- 00b86858 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8689c ["INT_ADD", "register:40f0:8", ["const:b8689c:8", "const:4:8"]]
+ 00b8689c ["CALL", null, ["callee:00bdb430:8"]]
- 00b86858 bytes e2520194
+ 00b8689c bytes e5520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be8fbc8efa964df4ff376c4c84f097bd"></a>

### [`00b86948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86948.md) → [`00b8698c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8698c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b869e0",
      "incomplete_value": true,
      "site": "00b869e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
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
    "old": {
      "definition_site": "00b8699c",
      "incomplete_value": true,
      "site": "00b869a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:cd8:8"
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
      "definition_site": "00b86a28",
      "incomplete_value": true,
      "site": "00b86a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b869e4",
      "incomplete_value": true,
      "site": "00b869e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b869e0",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b869e0",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86a28",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b869e0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b869e0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86a28",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b869a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86948.md#insn-00b869a0) · [`00b869e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86948.md#insn-00b869e4) · [`00b869e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86948.md#insn-00b869e8)
- 新版 `00b869e4`（命令位置の公開資料なし） · `00b86a28`（命令位置の公開資料なし） · `00b86a2c`（命令位置の公開資料なし）

~~~diff
- 00b869a0 ["INT_ADD", "register:40f0:8", ["const:b869a0:8", "const:4:8"]]
- 00b869a0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b869e4 ["INT_ADD", "register:40f0:8", ["const:b869e4:8", "const:4:8"]]
+ 00b869e4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b869a0 bytes 90520194
+ 00b869e4 bytes 93520194
- 00b869e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b869e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86a28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86a28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b869e4 bytes 216046f9
+ 00b86a28 bytes 218846f9
- 00b869e8 ["INT_ADD", "register:40f0:8", ["const:b869e8:8", "const:4:8"]]
- 00b869e8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86a2c ["INT_ADD", "register:40f0:8", ["const:b86a2c:8", "const:4:8"]]
+ 00b86a2c ["CALL", null, ["callee:00bdb430:8"]]
- 00b869e8 bytes 7e520194
+ 00b86a2c bytes 81520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a2f89283ba3e569074ff9fe2ec9650"></a>

### [`00b86ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86ad8.md) → [`00b86b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86b1c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86b70",
      "incomplete_value": true,
      "site": "00b86b74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86b2c",
      "incomplete_value": true,
      "site": "00b86b30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86bb8",
      "incomplete_value": true,
      "site": "00b86bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86b74",
      "incomplete_value": true,
      "site": "00b86b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86b70",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86b70",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86bb8",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86b70",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86b70",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86bb8",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86ad8.md#insn-00b86b30) · [`00b86b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86ad8.md#insn-00b86b74) · [`00b86b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86ad8.md#insn-00b86b78)
- 新版 `00b86b74`（命令位置の公開資料なし） · `00b86bb8`（命令位置の公開資料なし） · `00b86bbc`（命令位置の公開資料なし）

~~~diff
- 00b86b30 ["INT_ADD", "register:40f0:8", ["const:b86b30:8", "const:4:8"]]
- 00b86b30 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86b74 ["INT_ADD", "register:40f0:8", ["const:b86b74:8", "const:4:8"]]
+ 00b86b74 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86b30 bytes 2c520194
+ 00b86b74 bytes 2f520194
- 00b86b74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b86b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86bb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86bb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b86b74 bytes 216046f9
+ 00b86bb8 bytes 218846f9
- 00b86b78 ["INT_ADD", "register:40f0:8", ["const:b86b78:8", "const:4:8"]]
- 00b86b78 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86bbc ["INT_ADD", "register:40f0:8", ["const:b86bbc:8", "const:4:8"]]
+ 00b86bbc ["CALL", null, ["callee:00bdb430:8"]]
- 00b86b78 bytes 1a520194
+ 00b86bbc bytes 1d520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9a44579e34f9352ea41eabc22142001"></a>

### [`00b86c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86c68.md) → [`00b86cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86cac.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEx

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86d00",
      "incomplete_value": true,
      "site": "00b86d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86cbc",
      "incomplete_value": true,
      "site": "00b86cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86d48",
      "incomplete_value": true,
      "site": "00b86d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86d04",
      "incomplete_value": true,
      "site": "00b86d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86d00",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86d00",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86d48",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86d00",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86d00",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86d48",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86c68.md#insn-00b86cc0) · [`00b86d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86c68.md#insn-00b86d04) · [`00b86d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86c68.md#insn-00b86d08)
- 新版 `00b86d04`（命令位置の公開資料なし） · `00b86d48`（命令位置の公開資料なし） · `00b86d4c`（命令位置の公開資料なし）

~~~diff
- 00b86cc0 ["INT_ADD", "register:40f0:8", ["const:b86cc0:8", "const:4:8"]]
- 00b86cc0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86d04 ["INT_ADD", "register:40f0:8", ["const:b86d04:8", "const:4:8"]]
+ 00b86d04 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86cc0 bytes c8510194
+ 00b86d04 bytes cb510194
- 00b86d04 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b86d04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86d48 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86d48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b86d04 bytes 216046f9
+ 00b86d48 bytes 218846f9
- 00b86d08 ["INT_ADD", "register:40f0:8", ["const:b86d08:8", "const:4:8"]]
- 00b86d08 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86d4c ["INT_ADD", "register:40f0:8", ["const:b86d4c:8", "const:4:8"]]
+ 00b86d4c ["CALL", null, ["callee:00bdb430:8"]]
- 00b86d08 bytes b6510194
+ 00b86d4c bytes b9510194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ed54180e75f63fd1d092c67d9c5f35"></a>

### [`00b86df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86df8.md) → [`00b86e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86e3c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEy

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86e90",
      "incomplete_value": true,
      "site": "00b86e94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86e4c",
      "incomplete_value": true,
      "site": "00b86e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86ed8",
      "incomplete_value": true,
      "site": "00b86edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86e94",
      "incomplete_value": true,
      "site": "00b86e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b86e90",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86e90",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86ed8",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86e90",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86e90",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86ed8",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86df8.md#insn-00b86e50) · [`00b86e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86df8.md#insn-00b86e94) · [`00b86e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86df8.md#insn-00b86e98)
- 新版 `00b86e94`（命令位置の公開資料なし） · `00b86ed8`（命令位置の公開資料なし） · `00b86edc`（命令位置の公開資料なし）

~~~diff
- 00b86e50 ["INT_ADD", "register:40f0:8", ["const:b86e50:8", "const:4:8"]]
- 00b86e50 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86e94 ["INT_ADD", "register:40f0:8", ["const:b86e94:8", "const:4:8"]]
+ 00b86e94 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86e50 bytes 64510194
+ 00b86e94 bytes 67510194
- 00b86e94 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b86e94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86ed8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86ed8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b86e94 bytes 216046f9
+ 00b86ed8 bytes 218846f9
- 00b86e98 ["INT_ADD", "register:40f0:8", ["const:b86e98:8", "const:4:8"]]
- 00b86e98 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b86edc ["INT_ADD", "register:40f0:8", ["const:b86edc:8", "const:4:8"]]
+ 00b86edc ["CALL", null, ["callee:00bdb430:8"]]
- 00b86e98 bytes 52510194
+ 00b86edc bytes 55510194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26769da69515d7096b652e31098694a"></a>

### [`00b86f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86f88.md) → [`00b86fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86fcc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEf

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b87024",
      "incomplete_value": true,
      "site": "00b87028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86fe0",
      "incomplete_value": true,
      "site": "00b86fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b8706c",
      "incomplete_value": true,
      "site": "00b87070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87028",
      "incomplete_value": true,
      "site": "00b8702c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b87024",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b87024",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8706c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b87024",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b87024",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8706c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86f88.md#insn-00b86fe4) · [`00b87028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86f88.md#insn-00b87028) · [`00b8702c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86f88.md#insn-00b8702c)
- 新版 `00b87028`（命令位置の公開資料なし） · `00b8706c`（命令位置の公開資料なし） · `00b87070`（命令位置の公開資料なし）

~~~diff
- 00b86fe4 ["INT_ADD", "register:40f0:8", ["const:b86fe4:8", "const:4:8"]]
- 00b86fe4 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b87028 ["INT_ADD", "register:40f0:8", ["const:b87028:8", "const:4:8"]]
+ 00b87028 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86fe4 bytes ff500194
+ 00b87028 bytes 02510194
- 00b87028 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b87028 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8706c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b8706c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b87028 bytes 216046f9
+ 00b8706c bytes 218846f9
- 00b8702c ["INT_ADD", "register:40f0:8", ["const:b8702c:8", "const:4:8"]]
- 00b8702c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b87070 ["INT_ADD", "register:40f0:8", ["const:b87070:8", "const:4:8"]]
+ 00b87070 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8702c bytes ed500194
+ 00b87070 bytes f0500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c059043073c45079fa461198bc25058f"></a>

### [`00b87120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87120.md) → [`00b87164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87164.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEd

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b871bc",
      "incomplete_value": true,
      "site": "00b871c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87178",
      "incomplete_value": true,
      "site": "00b8717c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b87204",
      "incomplete_value": true,
      "site": "00b87208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b871c0",
      "incomplete_value": true,
      "site": "00b871c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b871bc",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b871bc",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87204",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b871bc",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b871bc",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87204",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87120.md#insn-00b8717c) · [`00b871c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87120.md#insn-00b871c0) · [`00b871c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87120.md#insn-00b871c4)
- 新版 `00b871c0`（命令位置の公開資料なし） · `00b87204`（命令位置の公開資料なし） · `00b87208`（命令位置の公開資料なし）

~~~diff
- 00b8717c ["INT_ADD", "register:40f0:8", ["const:b8717c:8", "const:4:8"]]
- 00b8717c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b871c0 ["INT_ADD", "register:40f0:8", ["const:b871c0:8", "const:4:8"]]
+ 00b871c0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8717c bytes 99500194
+ 00b871c0 bytes 9c500194
- 00b871c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b871c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b87204 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b87204 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b871c0 bytes 216046f9
+ 00b87204 bytes 218846f9
- 00b871c4 ["INT_ADD", "register:40f0:8", ["const:b871c4:8", "const:4:8"]]
- 00b871c4 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b87208 ["INT_ADD", "register:40f0:8", ["const:b87208:8", "const:4:8"]]
+ 00b87208 ["CALL", null, ["callee:00bdb430:8"]]
- 00b871c4 bytes 87500194
+ 00b87208 bytes 8a500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53aecc779c7ea70261d61fd27ae5086c"></a>

### [`00b872b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b872b8.md) → [`00b872fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b872fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b87350",
      "incomplete_value": true,
      "site": "00b87354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8730c",
      "incomplete_value": true,
      "site": "00b87310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b87398",
      "incomplete_value": true,
      "site": "00b8739c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87354",
      "incomplete_value": true,
      "site": "00b87358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b87350",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b87350",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87398",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b87350",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b87350",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87398",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b872b8.md#insn-00b87310) · [`00b87354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b872b8.md#insn-00b87354) · [`00b87358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b872b8.md#insn-00b87358)
- 新版 `00b87354`（命令位置の公開資料なし） · `00b87398`（命令位置の公開資料なし） · `00b8739c`（命令位置の公開資料なし）

~~~diff
- 00b87310 ["INT_ADD", "register:40f0:8", ["const:b87310:8", "const:4:8"]]
- 00b87310 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b87354 ["INT_ADD", "register:40f0:8", ["const:b87354:8", "const:4:8"]]
+ 00b87354 ["CALL", null, ["callee:00bdb430:8"]]
- 00b87310 bytes 34500194
+ 00b87354 bytes 37500194
- 00b87354 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b87354 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b87398 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b87398 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b87354 bytes 216046f9
+ 00b87398 bytes 218846f9
- 00b87358 ["INT_ADD", "register:40f0:8", ["const:b87358:8", "const:4:8"]]
- 00b87358 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8739c ["INT_ADD", "register:40f0:8", ["const:b8739c:8", "const:4:8"]]
+ 00b8739c ["CALL", null, ["callee:00bdb430:8"]]
- 00b87358 bytes 22500194
+ 00b8739c bytes 25500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00834fa9d012532c975c05fcec4b81ea"></a>

### [`00b87448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87448.md) → [`00b8748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8748c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPKv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b874e0",
      "incomplete_value": true,
      "site": "00b874e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8749c",
      "incomplete_value": true,
      "site": "00b874a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b87528",
      "incomplete_value": true,
      "site": "00b8752c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b874e4",
      "incomplete_value": true,
      "site": "00b874e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b874e0",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b874e0",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87528",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b874e0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b874e0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b87528",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b874a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87448.md#insn-00b874a0) · [`00b874e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87448.md#insn-00b874e4) · [`00b874e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87448.md#insn-00b874e8)
- 新版 `00b874e4`（命令位置の公開資料なし） · `00b87528`（命令位置の公開資料なし） · `00b8752c`（命令位置の公開資料なし）

~~~diff
- 00b874a0 ["INT_ADD", "register:40f0:8", ["const:b874a0:8", "const:4:8"]]
- 00b874a0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b874e4 ["INT_ADD", "register:40f0:8", ["const:b874e4:8", "const:4:8"]]
+ 00b874e4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b874a0 bytes d04f0194
+ 00b874e4 bytes d34f0194
- 00b874e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b874e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b87528 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b87528 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b874e4 bytes 216046f9
+ 00b87528 bytes 218846f9
- 00b874e8 ["INT_ADD", "register:40f0:8", ["const:b874e8:8", "const:4:8"]]
- 00b874e8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8752c ["INT_ADD", "register:40f0:8", ["const:b8752c:8", "const:4:8"]]
+ 00b8752c ["CALL", null, ["callee:00bdb430:8"]]
- 00b874e8 bytes be4f0194
+ 00b8752c bytes c14f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c99c9302b67569df459ade943285728"></a>

### [`00b87b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md) → [`00b87bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC1EOS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b87c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md) [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b87c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md) [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b87be4",
      "incomplete_value": true,
      "site": "00b87be4",
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
      "definition_site": "00b87ba0",
      "incomplete_value": true,
      "site": "00b87ba0",
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
      "definition_site": "00b87c10",
      "incomplete_value": true,
      "site": "00b87c14",
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
      "definition_site": "00b87bcc",
      "incomplete_value": true,
      "site": "00b87bd0",
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
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b87bdc",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b87be4",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b87c04",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b87bdc",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b87be4",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00b87c04",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md#insn-00b87b98) · [`00b87ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md#insn-00b87ba4) · [`00b87bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md#insn-00b87bc0)
- 新版 `00b87bdc`（命令位置の公開資料なし） · `00b87be8`（命令位置の公開資料なし） · `00b87c04`（命令位置の公開資料なし）

~~~diff
- 00b87b98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a00:8"]]
- 00b87b98 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b87bdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
+ 00b87bdc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b87b98 bytes b50245f9
+ 00b87bdc bytes b52a45f9
- 00b87ba4 ["INT_ADD", "register:40f0:8", ["const:b87ba4:8", "const:4:8"]]
- 00b87ba4 ["CALL", null, ["callee:00bdd950:8"]]
+ 00b87be8 ["INT_ADD", "register:40f0:8", ["const:b87be8:8", "const:4:8"]]
+ 00b87be8 ["CALL", null, ["callee:00bdd950:8"]]
- 00b87ba4 bytes 57570194
+ 00b87be8 bytes 5a570194
- 00b87bc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00b87bc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b87c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00b87c04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b87bc0 bytes 08c146f9
+ 00b87c04 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5941fe149788c6259ad9fdf564ec55e6"></a>

### [`00b887d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md) → [`00b8881c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc060.md) · 呼出先 6件 [`00b47d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 1件 [`00bdc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) · 呼出先 6件 [`00b47d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.89% / 新版 86.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b88840",
      "incomplete_value": true,
      "site": "00b88840",
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
      "definition_site": "00b887fc",
      "incomplete_value": true,
      "site": "00b887fc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b88864",
      "incomplete_value": true,
      "site": "00b88868",
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
      "definition_site": "00b88820",
      "incomplete_value": true,
      "site": "00b88824",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8888c",
      "incomplete_value": true,
      "site": "00b88890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88848",
      "incomplete_value": true,
      "site": "00b8884c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b88838",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b88840",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b88854",
      "READ",
      [
        "storage",
        "00c1ba80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b88838",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b88840",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00b88854",
      "READ",
      [
        "storage",
        "00c1bad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8884c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md#insn-00b8884c) · [`00b88868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md#insn-00b88868) · [`00b88878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md#insn-00b88878)
- 新版 `00b88890`（命令位置の公開資料なし） · `00b888ac`（命令位置の公開資料なし） · `00b888bc`（命令位置の公開資料なし）

~~~diff
- 00b8884c ["INT_ADD", "register:40f0:8", ["const:b8884c:8", "const:4:8"]]
- 00b8884c ["CALL", null, ["callee:00be0270:8"]]
+ 00b88890 ["INT_ADD", "register:40f0:8", ["const:b88890:8", "const:4:8"]]
+ 00b88890 ["CALL", null, ["callee:00be0270:8"]]
- 00b8884c bytes 755e0194
+ 00b88890 bytes 785e0194
- 00b88868 ["INT_ADD", "register:40f0:8", ["const:b88868:8", "const:4:8"]]
- 00b88868 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b888ac ["INT_ADD", "register:40f0:8", ["const:b888ac:8", "const:4:8"]]
+ 00b888ac ["CALL", null, ["callee:00bdd980:8"]]
- 00b88868 bytes 32540194
+ 00b888ac bytes 35540194
- 00b88878 ["INT_ADD", "register:40f0:8", ["const:b88878:8", "const:4:8"]]
- 00b88878 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b888bc ["INT_ADD", "register:40f0:8", ["const:b888bc:8", "const:4:8"]]
+ 00b888bc ["CALL", null, ["callee:00bdb430:8"]]
- 00b88878 bytes da4a0194
+ 00b888bc bytes dd4a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8905e759f0500e03b2f6bbf408edc93"></a>

### [`00b888fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b888fc.md) → [`00b88940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88940.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1EOS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.06% / 新版 94.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b88968",
      "incomplete_value": true,
      "site": "00b88968",
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
      "definition_site": "00b88924",
      "incomplete_value": true,
      "site": "00b88924",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b8899c",
      "incomplete_value": true,
      "site": "00b889a4",
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
      "definition_site": "00b88958",
      "incomplete_value": true,
      "site": "00b88960",
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
      "00b8895c",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b88968",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b88994",
      "READ",
      [
        "storage",
        "00c1ba80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8895c",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b88968",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00b88994",
      "READ",
      [
        "storage",
        "00c1bad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b888fc.md#insn-00b88918) · [`00b88928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b888fc.md#insn-00b88928) · [`00b88950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b888fc.md#insn-00b88950)
- 新版 `00b8895c`（命令位置の公開資料なし） · `00b8896c`（命令位置の公開資料なし） · `00b88994`（命令位置の公開資料なし）

~~~diff
- 00b88918 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00b88918 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8895c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 00b8895c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b88918 bytes 080145f9
+ 00b8895c bytes 082945f9
- 00b88928 ["INT_ADD", "register:40f0:8", ["const:b88928:8", "const:4:8"]]
- 00b88928 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b8896c ["INT_ADD", "register:40f0:8", ["const:b8896c:8", "const:4:8"]]
+ 00b8896c ["CALL", null, ["callee:00bdd980:8"]]
- 00b88928 bytes 02540194
+ 00b8896c bytes 05540194
- 00b88950 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a80:8"]]
- 00b88950 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b88994 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ad0:8"]]
+ 00b88994 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b88950 bytes 4a4145f9
+ 00b88994 bytes 4a6945f9
~~~


<a id="compare-d6fa3157680cd15f5b44d78674495f2a"></a>

### [`00b88a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md) → [`00b88ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc080.md) · 呼出先 5件 [`00b47d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47d08.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be0230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md)
- 新版 呼出元 1件 [`00bdc0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0d0.md) · 呼出先 5件 [`00b47d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

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
      "definition_site": "00b88af8",
      "incomplete_value": true,
      "site": "00b88afc",
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
      "definition_site": "00b88ab4",
      "incomplete_value": true,
      "site": "00b88ab8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b88b64",
      "incomplete_value": true,
      "site": "00b88b64",
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
      "definition_site": "00b88b20",
      "incomplete_value": true,
      "site": "00b88b20",
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
      "00b88af0",
      "READ",
      [
        "storage",
        "00c1ba80",
        null,
        "pointer"
      ]
    ],
    [
      "00b88afc",
      "DATA",
      [
        "storage",
        "00c11308",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b88b1c",
      "READ",
      [
        "storage",
        "00c11320",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b88af0",
      "READ",
      [
        "storage",
        "00c1bad0",
        null,
        "pointer"
      ]
    ],
    [
      "00b88afc",
      "DATA",
      [
        "storage",
        "00c11358",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b88b1c",
      "READ",
      [
        "storage",
        "00c11370",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md#insn-00b88afc) · [`00b88aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md#insn-00b88aac) · [`00b88ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md#insn-00b88ac4)
- 新版 `00b88b40`（命令位置の公開資料なし） · `00b88af0`（命令位置の公開資料なし） · `00b88b08`（命令位置の公開資料なし）

~~~diff
- 00b88afc ["INT_ADD", "register:40f0:8", ["const:b88afc:8", "const:4:8"]]
- 00b88afc ["CALL", null, ["callee:00bdef90:8"]]
+ 00b88b40 ["INT_ADD", "register:40f0:8", ["const:b88b40:8", "const:4:8"]]
+ 00b88b40 ["CALL", null, ["callee:00bdef90:8"]]
- 00b88afc bytes 11590194
+ 00b88b40 bytes 14590194
- 00b88aac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a80:8"]]
- 00b88aac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b88af0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad0:8"]]
+ 00b88af0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b88aac bytes 084145f9
+ 00b88af0 bytes 086945f9
- 00b88ac4 ["INT_ADD", "register:40f0:8", ["const:b88ac4:8", "const:4:8"]]
- 00b88ac4 ["CALL", null, ["callee:00be0280:8"]]
+ 00b88b08 ["INT_ADD", "register:40f0:8", ["const:b88b08:8", "const:4:8"]]
+ 00b88b08 ["CALL", null, ["callee:00be0280:8"]]
- 00b88ac4 bytes db5d0194
+ 00b88b08 bytes de5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f146cc38077330765e520b22d9aef2e1"></a>

### [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) → [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) FUN_00b88f5c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b88500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md) [`00b885b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md) [`00b8866c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8866c.md) [`00b8871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8871c.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00b88544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md) [`00b885f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md) [`00b886b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md) [`00b88760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 84.42% / 新版 84.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b88f98",
      "incomplete_value": false,
      "site": "00b88f9c",
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
            "const:5d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88f54",
      "incomplete_value": false,
      "site": "00b88f58",
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
            "const:663:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b88fa8",
      "incomplete_value": false,
      "site": "00b88fac",
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
            "const:995:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88f64",
      "incomplete_value": false,
      "site": "00b88f68",
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
            "const:a22:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b88fb8",
      "incomplete_value": false,
      "site": "00b88fbc",
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
            "const:19c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88f74",
      "incomplete_value": false,
      "site": "00b88f78",
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
            "const:111:8"
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
      "00b88f7c",
      "DATA",
      [
        "storage",
        "002978bc",
        null,
        null
      ]
    ],
    [
      "00b88f84",
      "DATA",
      [
        "storage",
        "002facd8",
        "switchD_00b88f48::switchdataD_002facd8",
        "byte"
      ]
    ],
    [
      "00b88f98",
      "DATA",
      [
        "storage",
        "00293663",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b88f7c",
      "DATA",
      [
        "storage",
        "0029782f",
        null,
        null
      ]
    ],
    [
      "00b88f84",
      "DATA",
      [
        "storage",
        "002facd8",
        "switchD_00b88f8c::switchdataD_002facd8",
        "byte"
      ]
    ],
    [
      "00b88f98",
      "DATA",
      [
        "storage",
        "002935d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md#insn-00b88f74) · [`00b88f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md#insn-00b88f84) · [`00b88fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md#insn-00b88fb4)
- 新版 `00b88fb8`（命令位置の公開資料なし） · `00b88fc8`（命令位置の公開資料なし） · `00b88ff8`（命令位置の公開資料なし）

~~~diff
- 00b88f74 ["COPY", "tmp:0:8", ["const:111:8"]]
- 00b88f74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b88f74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b88f74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b88fb8 ["COPY", "tmp:0:8", ["const:19c:8"]]
+ 00b88fb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88fb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88fb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b88f74 bytes 00440491
+ 00b88fb8 bytes 00700691
- 00b88f84 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00b88f84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b88f84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b88f84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b88fc8 ["COPY", "tmp:0:8", ["const:a5b:8"]]
+ 00b88fc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88fc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88fc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b88f84 bytes 00a02b91
+ 00b88fc8 bytes 006c2991
- 00b88fb4 ["COPY", "tmp:0:8", ["const:25d:8"]]
- 00b88fb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b88fb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b88fb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b88ff8 ["COPY", "tmp:0:8", ["const:25b:8"]]
+ 00b88ff8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88ff8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b88ff8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b88fb4 bytes 00740991
+ 00b88ff8 bytes 006c0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-983984f8779359eea0e41d3d341c9e5c"></a>

### [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) → [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) FUN_00b890e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 71件 [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) [`00b8d680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md) [`00b8deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md) [`00b90af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md) [`00b911d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md) · 呼出先 4件 [`00bbb0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0b8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be1430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1430.md)
- 新版 呼出元 71件 [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) [`00b9121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md) · 呼出先 4件 [`00bbb0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0fc.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be1480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1480.md)

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
      "definition_site": "00b89114",
      "incomplete_value": true,
      "site": "00b8911c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b890d0",
      "incomplete_value": true,
      "site": "00b890d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
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
      "definition_site": "00b89118",
      "incomplete_value": true,
      "site": "00b8911c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b890d4",
      "incomplete_value": true,
      "site": "00b890d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
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
      "00b89114",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b89114",
      "PARAM",
      [
        "storage",
        "00c16b90",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b89118",
      "READ",
      [
        "storage",
        "00c1bce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b89114",
      "READ",
      [
        "storage",
        "00c1bd30",
        null,
        "pointer"
      ]
    ],
    [
      "00b89114",
      "PARAM",
      [
        "storage",
        "00c16be0",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b89118",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b890d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md#insn-00b890d8) · [`00b890b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md#insn-00b890b8) · [`00b890c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md#insn-00b890c0)
- 新版 `00b8911c`（命令位置の公開資料なし） · `00b890fc`（命令位置の公開資料なし） · `00b89104`（命令位置の公開資料なし）

~~~diff
- 00b890d8 ["INT_ADD", "register:40f0:8", ["const:b890d8:8", "const:4:8"]]
- 00b890d8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b8911c ["INT_ADD", "register:40f0:8", ["const:b8911c:8", "const:4:8"]]
+ 00b8911c ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b890d8 bytes e6470194
+ 00b8911c bytes e9470194
- 00b890b8 ["INT_ADD", "register:40f0:8", ["const:b890b8:8", "const:4:8"]]
- 00b890b8 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b890fc ["INT_ADD", "register:40f0:8", ["const:b890fc:8", "const:4:8"]]
+ 00b890fc ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b890b8 bytes e6470194
+ 00b890fc bytes e9470194
- 00b890c0 ["INT_ADD", "register:40f0:8", ["const:b890c0:8", "const:4:8"]]
- 00b890c0 ["CALL", null, ["callee:00be1480:8"]]
+ 00b89104 ["INT_ADD", "register:40f0:8", ["const:b89104:8", "const:4:8"]]
+ 00b89104 ["CALL", null, ["callee:00be1480:8"]]
- 00b890c0 bytes dc600194
+ 00b89104 bytes df600194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95fd07bc26048d71e3f9a6b5de030b11"></a>

### [`00b89148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89148.md) → [`00b8918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8918c.md) FUN_00b8918c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b891c0",
      "incomplete_value": true,
      "site": "00b891c0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8917c",
      "incomplete_value": true,
      "site": "00b8917c",
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
            "const:40:8"
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
      "definition_site": "00b891b8",
      "incomplete_value": true,
      "site": "00b891c8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89174",
      "incomplete_value": true,
      "site": "00b89184",
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
            "const:18:8"
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
      "definition_site": "00b891c4",
      "incomplete_value": true,
      "site": "00b891cc",
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
      "definition_site": "00b89180",
      "incomplete_value": true,
      "site": "00b89188",
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
      "00b891a8",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00b891ac",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b891c0",
      "DATA",
      [
        "storage",
        "00c13468",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b891a8",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b891ac",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b891c0",
      "DATA",
      [
        "storage",
        "00c134b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89148.md#insn-00b89164) · [`00b89168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89148.md#insn-00b89168) · [`00b89170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89148.md#insn-00b89170)
- 新版 `00b891a8`（命令位置の公開資料なし） · `00b891ac`（命令位置の公開資料なし）

~~~diff
- 00b89164 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 00b89164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b891a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a0:8"]]
+ 00b891a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b89164 bytes 082942f9
+ 00b891a8 bytes 085142f9
- 00b89168 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b89168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b891ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b891ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b89168 bytes 29c146f9
+ 00b891ac bytes 29e946f9
- 00b89170 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00b89170 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a120858af76dacaa24aa79da54f5744f"></a>

### [`00b891cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b891cc.md) → [`00b89210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89210.md) FUN_00b89210

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b89230",
      "incomplete_value": true,
      "site": "00b89244",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b891ec",
      "incomplete_value": true,
      "site": "00b89200",
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
            "const:18:8"
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
      "definition_site": "00b89250",
      "incomplete_value": true,
      "site": "00b89250",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8920c",
      "incomplete_value": true,
      "site": "00b8920c",
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
            "const:40:8"
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
      "definition_site": "00b89254",
      "incomplete_value": true,
      "site": "00b89258",
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
      "definition_site": "00b89210",
      "incomplete_value": true,
      "site": "00b89214",
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
      "00b89224",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00b89240",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b89244",
      "DATA",
      [
        "storage",
        "00c13440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b89224",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b89240",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b89244",
      "DATA",
      [
        "storage",
        "00c13490",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b891e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b891cc.md#insn-00b891e0) · [`00b891fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b891cc.md#insn-00b891fc) · [`00b89220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b891cc.md#insn-00b89220)
- 新版 `00b89224`（命令位置の公開資料なし） · `00b89240`（命令位置の公開資料なし） · `00b89264`（命令位置の公開資料なし）

~~~diff
- 00b891e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 00b891e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b89224 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a0:8"]]
+ 00b89224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b891e0 bytes 082942f9
+ 00b89224 bytes 085142f9
- 00b891fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b891fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b89240 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b89240 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b891fc bytes 29c146f9
+ 00b89240 bytes 29e946f9
- 00b89220 ["INT_ADD", "register:40f0:8", ["const:b89220:8", "const:4:8"]]
- 00b89220 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b89264 ["INT_ADD", "register:40f0:8", ["const:b89264:8", "const:4:8"]]
+ 00b89264 ["CALL", null, ["callee:00bdb060:8"]]
- 00b89220 bytes 7c470194
+ 00b89264 bytes 7f470194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59049eeb30ad3e993e9fcfdae71f8d53"></a>

### [`00b89250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89250.md) → [`00b89294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89294.md) FUN_00b89294

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b892b4",
      "incomplete_value": true,
      "site": "00b892c8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89270",
      "incomplete_value": true,
      "site": "00b89284",
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
            "const:18:8"
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
      "definition_site": "00b892d4",
      "incomplete_value": true,
      "site": "00b892d4",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89290",
      "incomplete_value": true,
      "site": "00b89290",
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
            "const:40:8"
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
      "definition_site": "00b892d8",
      "incomplete_value": true,
      "site": "00b892dc",
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
      "definition_site": "00b89294",
      "incomplete_value": true,
      "site": "00b89298",
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
      "00b892a8",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00b892c4",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b892c8",
      "DATA",
      [
        "storage",
        "00c13440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b892a8",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b892c4",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b892c8",
      "DATA",
      [
        "storage",
        "00c13490",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89250.md#insn-00b89264) · [`00b89280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89250.md#insn-00b89280) · [`00b892a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89250.md#insn-00b892a4)
- 新版 `00b892a8`（命令位置の公開資料なし） · `00b892c4`（命令位置の公開資料なし） · `00b892e8`（命令位置の公開資料なし）

~~~diff
- 00b89264 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 00b89264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b892a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a0:8"]]
+ 00b892a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b89264 bytes 082942f9
+ 00b892a8 bytes 085142f9
- 00b89280 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b89280 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b892c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b892c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b89280 bytes 29c146f9
+ 00b892c4 bytes 29e946f9
- 00b892a4 ["INT_ADD", "register:40f0:8", ["const:b892a4:8", "const:4:8"]]
- 00b892a4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b892e8 ["INT_ADD", "register:40f0:8", ["const:b892e8:8", "const:4:8"]]
+ 00b892e8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b892a4 bytes 5b470194
+ 00b892e8 bytes 5e470194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999ff807c0849b9daa856dd8e6facdc4"></a>

### [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) → [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) FUN_00b89320

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b898c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b898c4.md) · 呼出先 11件 [`00b89728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89728.md) [`00b897d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b897d0.md) [`00b89988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89988.md) [`00b8a01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a01c.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00b89908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md) · 呼出先 11件 [`00b8976c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8976c.md) [`00b89814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89814.md) [`00b899cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899cc.md) [`00b8a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.07% / 新版 64.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 16件, `store_value` 11件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b89354",
      "incomplete_value": false,
      "site": "00b8935c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89310",
      "incomplete_value": false,
      "site": "00b89318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b89364",
      "incomplete_value": false,
      "site": "00b8936c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89320",
      "incomplete_value": false,
      "site": "00b89328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b89368",
      "incomplete_value": true,
      "site": "00b89380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89324",
      "incomplete_value": true,
      "site": "00b8933c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b89348",
      "PARAM",
      [
        "storage",
        "010a2580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8935c",
      "WRITE",
      [
        "storage",
        "010a2580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8935c",
      "DATA",
      [
        "storage",
        "00c13668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b89348",
      "PARAM",
      [
        "storage",
        "010a25c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8935c",
      "WRITE",
      [
        "storage",
        "010a25c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8935c",
      "DATA",
      [
        "storage",
        "00c136b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md#insn-00b89344) · [`00b8936c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md#insn-00b8936c) · [`00b8939c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md#insn-00b8939c)
- 新版 `00b89388`（命令位置の公開資料なし） · `00b893b0`（命令位置の公開資料なし） · `00b893e0`（命令位置の公開資料なし）

~~~diff
- 00b89344 ["INT_ADD", "register:40f0:8", ["const:b89344:8", "const:4:8"]]
- 00b89344 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b89388 ["INT_ADD", "register:40f0:8", ["const:b89388:8", "const:4:8"]]
+ 00b89388 ["CALL", null, ["callee:00bdd980:8"]]
- 00b89344 bytes 7b510194
+ 00b89388 bytes 7e510194
- 00b8936c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf0:8"]]
- 00b8936c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b893b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d40:8"]]
+ 00b893b0 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8936c bytes b57a46f9
+ 00b893b0 bytes b5a246f9
- 00b8939c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00b8939c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b8939c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b8939c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b893e0 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00b893e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b893e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b893e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b8939c bytes 73c21791
+ 00b893e0 bytes 73c21891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6048b633b210bdd81fd4526707766be8"></a>

### [`00b89728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89728.md) → [`00b8976c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8976c.md) FUN_00b8976c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) · 呼出先 4件 [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 4件 [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b89794",
      "incomplete_value": false,
      "site": "00b897a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89750",
      "incomplete_value": false,
      "site": "00b8975c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b897b4",
      "incomplete_value": true,
      "site": "00b897b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89770",
      "incomplete_value": true,
      "site": "00b89774",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b897a0",
      "DATA",
      [
        "storage",
        "00c13700",
        null,
        "undefined *"
      ]
    ],
    [
      "00b897b4",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00b897b4",
      "PARAM",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b897a0",
      "DATA",
      [
        "storage",
        "00c13750",
        null,
        "undefined *"
      ]
    ],
    [
      "00b897b4",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b897b4",
      "PARAM",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89728.md#insn-00b89774) · [`00b89748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89728.md#insn-00b89748) · [`00b89750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89728.md#insn-00b89750)
- 新版 `00b897b8`（命令位置の公開資料なし） · `00b8978c`（命令位置の公開資料なし） · `00b89794`（命令位置の公開資料なし）

~~~diff
- 00b89774 ["INT_ADD", "register:40f0:8", ["const:b89774:8", "const:4:8"]]
- 00b89774 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b897b8 ["INT_ADD", "register:40f0:8", ["const:b897b8:8", "const:4:8"]]
+ 00b897b8 ["CALL", null, ["callee:00bdb430:8"]]
- 00b89774 bytes 1b470194
+ 00b897b8 bytes 1e470194
- 00b89748 ["INT_ADD", "register:40f0:8", ["const:b89748:8", "const:4:8"]]
- 00b89748 ["CALL", null, ["callee:00bdb3a0:8"]]
+ 00b8978c ["INT_ADD", "register:40f0:8", ["const:b8978c:8", "const:4:8"]]
+ 00b8978c ["CALL", null, ["callee:00bdb3a0:8"]]
- 00b89748 bytes 02470194
+ 00b8978c bytes 05470194
- 00b89750 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00b89750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b89750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b89750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b89794 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00b89794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b89794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b89794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b89750 bytes 08011c91
+ 00b89794 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf29d4bb112f0761ca4f3173597fc44"></a>

### [`00b897d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b897d0.md) → [`00b89814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89814.md) FUN_00b89814

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) · 呼出先 4件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1390.md)
- 新版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 4件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be13e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13e0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8983c",
      "incomplete_value": false,
      "site": "00b89848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b897f8",
      "incomplete_value": false,
      "site": "00b89804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "definition_site": "00b8985c",
      "incomplete_value": true,
      "site": "00b89860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89818",
      "incomplete_value": true,
      "site": "00b8981c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00b89848",
      "DATA",
      [
        "storage",
        "00c13830",
        null,
        "undefined *"
      ]
    ],
    [
      "00b8985c",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b8985c",
      "PARAM",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b89848",
      "DATA",
      [
        "storage",
        "00c13880",
        null,
        "undefined *"
      ]
    ],
    [
      "00b8985c",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00b8985c",
      "PARAM",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8981c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b897d0.md#insn-00b8981c) · [`00b897f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b897d0.md#insn-00b897f0) · [`00b897f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b897d0.md#insn-00b897f8)
- 新版 `00b89860`（命令位置の公開資料なし） · `00b89834`（命令位置の公開資料なし） · `00b8983c`（命令位置の公開資料なし）

~~~diff
- 00b8981c ["INT_ADD", "register:40f0:8", ["const:b8981c:8", "const:4:8"]]
- 00b8981c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b89860 ["INT_ADD", "register:40f0:8", ["const:b89860:8", "const:4:8"]]
+ 00b89860 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8981c bytes f1460194
+ 00b89860 bytes f4460194
- 00b897f0 ["INT_ADD", "register:40f0:8", ["const:b897f0:8", "const:4:8"]]
- 00b897f0 ["CALL", null, ["callee:00be13e0:8"]]
+ 00b89834 ["INT_ADD", "register:40f0:8", ["const:b89834:8", "const:4:8"]]
+ 00b89834 ["CALL", null, ["callee:00be13e0:8"]]
- 00b897f0 bytes e85e0194
+ 00b89834 bytes eb5e0194
- 00b897f8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00b897f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b897f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b897f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b8983c ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00b8983c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8983c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8983c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b897f8 bytes 08c12091
+ 00b8983c bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dbcb0233bcc2bb4679c20d2ae16d27a"></a>

### [`00b898c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b898c4.md) → [`00b89908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md) _ZNSt6__ndk18ios_base4InitC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be14a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14a0.md) · 呼出先 5件 [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) [`00b89878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89878.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00be14f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14f0.md) · 呼出先 5件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) [`00b898bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b898bc.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

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
      "definition_site": "00b8993c",
      "incomplete_value": false,
      "site": "00b89940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b898f8",
      "incomplete_value": false,
      "site": "00b898fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "definition_site": "00b89950",
      "incomplete_value": false,
      "site": "00b89964",
      "value": [
        "leaf",
        "const:b898bc:8"
      ]
    },
    "old": {
      "definition_site": "00b8990c",
      "incomplete_value": false,
      "site": "00b89920",
      "value": [
        "leaf",
        "const:b89878:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b89958",
      "incomplete_value": false,
      "site": "00b89964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89914",
      "incomplete_value": false,
      "site": "00b89920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00b89920",
      "READ",
      [
        "storage",
        "010a2808",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8993c",
      "PARAM",
      [
        "storage",
        "010a2808",
        null,
        "undefined1"
      ]
    ],
    [
      "00b89950",
      "PARAM",
      [
        "storage",
        "00b89878",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b89920",
      "READ",
      [
        "storage",
        "010a2848",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8993c",
      "PARAM",
      [
        "storage",
        "010a2848",
        null,
        "undefined1"
      ]
    ],
    [
      "00b89950",
      "PARAM",
      [
        "storage",
        "00b898bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b898fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b898c4.md#insn-00b898fc) · [`00b89920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b898c4.md#insn-00b89920) · [`00b898d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b898c4.md#insn-00b898d8)
- 新版 `00b89940`（命令位置の公開資料なし） · `00b89964`（命令位置の公開資料なし） · `00b8991c`（命令位置の公開資料なし）

~~~diff
- 00b898fc ["INT_ADD", "register:40f0:8", ["const:b898fc:8", "const:4:8"]]
- 00b898fc ["CALL", null, ["callee:00bdb000:8"]]
+ 00b89940 ["INT_ADD", "register:40f0:8", ["const:b89940:8", "const:4:8"]]
+ 00b89940 ["CALL", null, ["callee:00bdb000:8"]]
- 00b898fc bytes ad450194
+ 00b89940 bytes b0450194
- 00b89920 ["INT_ADD", "register:40f0:8", ["const:b89920:8", "const:4:8"]]
- 00b89920 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00b89964 ["INT_ADD", "register:40f0:8", ["const:b89964:8", "const:4:8"]]
+ 00b89964 ["CALL", null, ["callee:00bdafe0:8"]]
- 00b89920 bytes 9c450194
+ 00b89964 bytes 9f450194
- 00b898d8 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00b898d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b898d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b898d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b8991c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00b8991c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8991c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8991c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b898d8 bytes 08212091
+ 00b8991c bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a85bb9373f57581e90d6c15708625b9"></a>

### [`00b89988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89988.md) → [`00b899cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899cc.md) FUN_00b899cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) · 呼出先 2件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 2件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b89a44",
      "incomplete_value": false,
      "site": "00b89a48",
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
            "const:2c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89a00",
      "incomplete_value": false,
      "site": "00b89a04",
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
            "const:23e:8"
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
      "00b899e8",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00b899e8",
      "PARAM",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00b89a44",
      "PARAM",
      [
        "storage",
        "002a523e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b899e8",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b899e8",
      "PARAM",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00b89a44",
      "PARAM",
      [
        "storage",
        "002a52c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89988.md#insn-00b89a04) · [`00b899a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89988.md#insn-00b899a4) · [`00b899ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89988.md#insn-00b899ac)
- 新版 `00b89a48`（命令位置の公開資料なし） · `00b899e8`（命令位置の公開資料なし） · `00b899f0`（命令位置の公開資料なし）

~~~diff
- 00b89a04 ["INT_ADD", "register:40f0:8", ["const:b89a04:8", "const:4:8"]]
- 00b89a04 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b89a48 ["INT_ADD", "register:40f0:8", ["const:b89a48:8", "const:4:8"]]
+ 00b89a48 ["CALL", null, ["callee:00be0fb0:8"]]
- 00b89a04 bytes 575d0194
+ 00b89a48 bytes 5a5d0194
- 00b899a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:a60:8"]]
- 00b899a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b899e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ab0:8"]]
+ 00b899e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b899a4 bytes 213045f9
+ 00b899e8 bytes 215845f9
- 00b899ac ["INT_ADD", "register:40f0:8", ["const:b899ac:8", "const:4:8"]]
- 00b899ac ["CALL", null, ["callee:00bdb430:8"]]
+ 00b899f0 ["INT_ADD", "register:40f0:8", ["const:b899f0:8", "const:4:8"]]
+ 00b899f0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b899ac bytes 8d460194
+ 00b899f0 bytes 90460194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7741e87fdd0747dbe1d80fd9d5e5a123"></a>

### [`00b89d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d1c.md) → [`00b89d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d60.md) FUN_00b89d60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b89d8c",
      "incomplete_value": true,
      "site": "00b89d90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89d48",
      "incomplete_value": true,
      "site": "00b89d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b89d8c",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00b89d8c",
      "PARAM",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b89d8c",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b89d8c",
      "PARAM",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d1c.md#insn-00b89d4c) · [`00b89d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d1c.md#insn-00b89d3c) · [`00b89d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d1c.md#insn-00b89d48)
- 新版 `00b89d90`（命令位置の公開資料なし） · `00b89d80`（命令位置の公開資料なし） · `00b89d8c`（命令位置の公開資料なし）

~~~diff
- 00b89d4c ["INT_ADD", "register:40f0:8", ["const:b89d4c:8", "const:4:8"]]
- 00b89d4c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b89d90 ["INT_ADD", "register:40f0:8", ["const:b89d90:8", "const:4:8"]]
+ 00b89d90 ["CALL", null, ["callee:00bdb430:8"]]
- 00b89d4c bytes a5450194
+ 00b89d90 bytes a8450194
- 00b89d3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89d3c ["INT_ADD", "register:40f0:8", ["const:b89d3c:8", "const:4:8"]]
- 00b89d3c ["CALLIND", null, ["register:0:8"]]
+ 00b89d80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89d80 ["INT_ADD", "register:40f0:8", ["const:b89d80:8", "const:4:8"]]
+ 00b89d80 ["CALLIND", null, ["register:0:8"]]
- 00b89d3c bytes 00013fd6
+ 00b89d80 bytes 00013fd6
- 00b89d48 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:a60:8"]]
- 00b89d48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b89d8c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ab0:8"]]
+ 00b89d8c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b89d48 bytes 213045f9
+ 00b89d8c bytes 215845f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09dde328d1efbcb2f988ea019b6aa770"></a>

### [`00b8a01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a01c.md) → [`00b8a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md) FUN_00b8a060

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b892dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b892dc.md) · 呼出先 2件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 2件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

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
      "definition_site": "00b8a07c",
      "incomplete_value": true,
      "site": "00b8a084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a038",
      "incomplete_value": true,
      "site": "00b8a040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "00b8a0d8",
      "incomplete_value": false,
      "site": "00b8a0dc",
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
            "const:2c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a094",
      "incomplete_value": false,
      "site": "00b8a098",
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
            "const:23e:8"
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
      "00b8a07c",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a07c",
      "PARAM",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8a0d8",
      "PARAM",
      [
        "storage",
        "002a523e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8a07c",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a07c",
      "PARAM",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8a0d8",
      "PARAM",
      [
        "storage",
        "002a52c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a01c.md#insn-00b8a040) · [`00b8a098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a01c.md#insn-00b8a098) · [`00b8a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a01c.md#insn-00b8a038)
- 新版 `00b8a084`（命令位置の公開資料なし） · `00b8a0dc`（命令位置の公開資料なし） · `00b8a07c`（命令位置の公開資料なし）

~~~diff
- 00b8a040 ["INT_ADD", "register:40f0:8", ["const:b8a040:8", "const:4:8"]]
- 00b8a040 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8a084 ["INT_ADD", "register:40f0:8", ["const:b8a084:8", "const:4:8"]]
+ 00b8a084 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8a040 bytes e8440194
+ 00b8a084 bytes eb440194
- 00b8a098 ["INT_ADD", "register:40f0:8", ["const:b8a098:8", "const:4:8"]]
- 00b8a098 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b8a0dc ["INT_ADD", "register:40f0:8", ["const:b8a0dc:8", "const:4:8"]]
+ 00b8a0dc ["CALL", null, ["callee:00be0fb0:8"]]
- 00b8a098 bytes b25b0194
+ 00b8a0dc bytes b55b0194
- 00b8a038 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d28:8"]]
- 00b8a038 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8a07c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d78:8"]]
+ 00b8a07c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8a038 bytes 219446f9
+ 00b8a07c bytes 21bc46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffd75686abfdfdee0f81f61c2649cd51"></a>

### [`00b8a3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a3a8.md) → [`00b8a3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3ec.md) FUN_00b8a3ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8a418",
      "incomplete_value": true,
      "site": "00b8a41c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a3d4",
      "incomplete_value": true,
      "site": "00b8a3d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "00b8a418",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a418",
      "PARAM",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8a418",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a418",
      "PARAM",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a3a8.md#insn-00b8a3d8) · [`00b8a3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a3a8.md#insn-00b8a3c8) · [`00b8a3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a3a8.md#insn-00b8a3d4)
- 新版 `00b8a41c`（命令位置の公開資料なし） · `00b8a40c`（命令位置の公開資料なし） · `00b8a418`（命令位置の公開資料なし）

~~~diff
- 00b8a3d8 ["INT_ADD", "register:40f0:8", ["const:b8a3d8:8", "const:4:8"]]
- 00b8a3d8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8a41c ["INT_ADD", "register:40f0:8", ["const:b8a41c:8", "const:4:8"]]
+ 00b8a41c ["CALL", null, ["callee:00bdb430:8"]]
- 00b8a3d8 bytes 02440194
+ 00b8a41c bytes 05440194
- 00b8a3c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a3c8 ["INT_ADD", "register:40f0:8", ["const:b8a3c8:8", "const:4:8"]]
- 00b8a3c8 ["CALLIND", null, ["register:0:8"]]
+ 00b8a40c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a40c ["INT_ADD", "register:40f0:8", ["const:b8a40c:8", "const:4:8"]]
+ 00b8a40c ["CALLIND", null, ["register:0:8"]]
- 00b8a3c8 bytes 00013fd6
+ 00b8a40c bytes 00013fd6
- 00b8a3d4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d28:8"]]
- 00b8a3d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8a418 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d78:8"]]
+ 00b8a418 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8a3d4 bytes 219446f9
+ 00b8a418 bytes 21bc46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-408c466a6a9b818379566e7f796ca80b"></a>

### [`00b8a670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a670.md) → [`00b8a6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a6b4.md) _INIT_2

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b89954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89954.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00be14a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b89998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89998.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00be14f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8a6cc",
      "incomplete_value": false,
      "site": "00b8a6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a688",
      "incomplete_value": false,
      "site": "00b8a68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "00b8a6cc",
      "PARAM",
      [
        "storage",
        "010a2578",
        null,
        null
      ]
    ],
    [
      "00b8a6dc",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a6e0",
      "READ",
      [
        "storage",
        "00c1bd30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8a6cc",
      "PARAM",
      [
        "storage",
        "010a25b8",
        null,
        null
      ]
    ],
    [
      "00b8a6dc",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8a6e0",
      "READ",
      [
        "storage",
        "00c1bd80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a670.md#insn-00b8a68c) · [`00b8a684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a670.md#insn-00b8a684) · [`00b8a698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a670.md#insn-00b8a698)
- 新版 `00b8a6d0`（命令位置の公開資料なし） · `00b8a6c8`（命令位置の公開資料なし） · `00b8a6dc`（命令位置の公開資料なし）

~~~diff
- 00b8a68c ["INT_ADD", "register:40f0:8", ["const:b8a68c:8", "const:4:8"]]
- 00b8a68c ["CALL", null, ["callee:00be14f0:8"]]
+ 00b8a6d0 ["INT_ADD", "register:40f0:8", ["const:b8a6d0:8", "const:4:8"]]
+ 00b8a6d0 ["CALL", null, ["callee:00be14f0:8"]]
- 00b8a68c bytes 855b0194
+ 00b8a6d0 bytes 885b0194
- 00b8a684 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00b8a684 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b8a684 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b8a684 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b8a6c8 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00b8a6c8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b8a6c8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b8a6c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b8a684 bytes 73e21591
+ 00b8a6c8 bytes 73e21691
- 00b8a698 ["COPY", "register:4010:8", ["const:be5f80:8"]]
+ 00b8a6dc ["COPY", "register:4010:8", ["const:be5fd0:8"]]
- 00b8a698 bytes 42c72d10
+ 00b8a6dc bytes a2c72d10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3503421369c158e8793af6a3adb2cb72"></a>

### [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) → [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8aaa0",
      "incomplete_value": true,
      "site": "00b8aaa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b8aa5c",
      "incomplete_value": true,
      "site": "00b8aa5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8ab18",
      "incomplete_value": true,
      "site": "00b8ab18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8aad4",
      "incomplete_value": true,
      "site": "00b8aad4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b8aaa8",
      "incomplete_value": true,
      "site": "00b8aaac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b8aa64",
      "incomplete_value": true,
      "site": "00b8aa68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b8aa98",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8aaa0",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8aaa4",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8aa98",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b8aaa0",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8aaa4",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8aa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md#insn-00b8aa4c) · [`00b8aa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md#insn-00b8aa90) · [`00b8aab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md#insn-00b8aab8)
- 新版 `00b8aa90`（命令位置の公開資料なし） · `00b8aad4`（命令位置の公開資料なし） · `00b8aafc`（命令位置の公開資料なし）

~~~diff
- 00b8aa4c ["INT_ADD", "register:40f0:8", ["const:b8aa4c:8", "const:4:8"]]
- 00b8aa4c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b8aa90 ["INT_ADD", "register:40f0:8", ["const:b8aa90:8", "const:4:8"]]
+ 00b8aa90 ["CALL", null, ["callee:00bdb420:8"]]
- 00b8aa4c bytes 61420194
+ 00b8aa90 bytes 64420194
- 00b8aa90 ["INT_ADD", "register:40f0:8", ["const:b8aa90:8", "const:4:8"]]
- 00b8aa90 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b8aad4 ["INT_ADD", "register:40f0:8", ["const:b8aad4:8", "const:4:8"]]
+ 00b8aad4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b8aa90 bytes 00590194
+ 00b8aad4 bytes 03590194
- 00b8aab8 ["INT_ADD", "register:40f0:8", ["const:b8aab8:8", "const:4:8"]]
- 00b8aab8 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b8aafc ["INT_ADD", "register:40f0:8", ["const:b8aafc:8", "const:4:8"]]
+ 00b8aafc ["CALL", null, ["callee:00bdb440:8"]]
- 00b8aab8 bytes 4e420194
+ 00b8aafc bytes 51420194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b35b8af7e05908cea787b61384b0d8ba"></a>

### [`00b8d680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md) → [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8d710",
      "incomplete_value": true,
      "site": "00b8d710",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b8d6cc",
      "incomplete_value": true,
      "site": "00b8d6cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b8db8c",
      "incomplete_value": true,
      "site": "00b8db8c",
      "value": [
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
    "old": {
      "definition_site": "00b8db48",
      "incomplete_value": true,
      "site": "00b8db48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b8d718",
      "incomplete_value": true,
      "site": "00b8d71c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b8d6d4",
      "incomplete_value": true,
      "site": "00b8d6d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b8d708",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8d710",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8d714",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8d708",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b8d710",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8d714",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md#insn-00b8d6bc) · [`00b8d700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md#insn-00b8d700) · [`00b8d740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md#insn-00b8d740)
- 新版 `00b8d700`（命令位置の公開資料なし） · `00b8d744`（命令位置の公開資料なし） · `00b8d784`（命令位置の公開資料なし）

~~~diff
- 00b8d6bc ["INT_ADD", "register:40f0:8", ["const:b8d6bc:8", "const:4:8"]]
- 00b8d6bc ["CALL", null, ["callee:00bdb420:8"]]
+ 00b8d700 ["INT_ADD", "register:40f0:8", ["const:b8d700:8", "const:4:8"]]
+ 00b8d700 ["CALL", null, ["callee:00bdb420:8"]]
- 00b8d6bc bytes 45370194
+ 00b8d700 bytes 48370194
- 00b8d700 ["INT_ADD", "register:40f0:8", ["const:b8d700:8", "const:4:8"]]
- 00b8d700 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b8d744 ["INT_ADD", "register:40f0:8", ["const:b8d744:8", "const:4:8"]]
+ 00b8d744 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b8d700 bytes e44d0194
+ 00b8d744 bytes e74d0194
- 00b8d740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8d740 ["INT_ADD", "register:40f0:8", ["const:b8d740:8", "const:4:8"]]
- 00b8d740 ["CALLIND", null, ["register:0:8"]]
+ 00b8d784 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8d784 ["INT_ADD", "register:40f0:8", ["const:b8d784:8", "const:4:8"]]
+ 00b8d784 ["CALLIND", null, ["register:0:8"]]
- 00b8d740 bytes 00013fd6
+ 00b8d784 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-018d1fee63ff6f06ab869eb2a8847b6b"></a>

### [`00b8de28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8de28.md) → [`00b8de6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8de6c.md) _ZNSt6__ndk16__clocEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b8dec8",
      "incomplete_value": true,
      "site": "00b8dec8",
      "value": [
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
    "old": {
      "definition_site": "00b8de84",
      "incomplete_value": true,
      "site": "00b8de84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00b8dea8",
      "incomplete_value": false,
      "site": "00b8deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8de64",
      "incomplete_value": false,
      "site": "00b8de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "definition_site": "00b8deb8",
      "incomplete_value": false,
      "site": "00b8dec4",
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
            "const:70e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8de74",
      "incomplete_value": false,
      "site": "00b8de80",
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
            "const:683:8"
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
      "00b8de88",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8de90",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8dea8",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b8de88",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8de90",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8dea8",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8de3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8de28.md#insn-00b8de3c) · [`00b8de4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8de28.md#insn-00b8de4c) · [`00b8de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8de28.md#insn-00b8de68)
- 新版 `00b8de80`（命令位置の公開資料なし） · `00b8de90`（命令位置の公開資料なし） · `00b8deac`（命令位置の公開資料なし）

~~~diff
- 00b8de3c ["COPY", "tmp:0:8", ["const:958:8"]]
- 00b8de3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b8de3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b8de3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b8de80 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00b8de80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8de80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b8de80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b8de3c bytes 08612591
+ 00b8de80 bytes 08612691
- 00b8de4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
- 00b8de4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8de90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b8de90 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8de4c bytes 60aa44f9
+ 00b8de90 bytes 60ca44f9
- 00b8de68 ["INT_ADD", "register:40f0:8", ["const:b8de68:8", "const:4:8"]]
- 00b8de68 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b8deac ["INT_ADD", "register:40f0:8", ["const:b8deac:8", "const:4:8"]]
+ 00b8deac ["CALL", null, ["callee:00bdb000:8"]]
- 00b8de68 bytes 52340194
+ 00b8deac bytes 55340194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e20300b31bce5c7fbe14957f3ff3ce99"></a>

### [`00b8deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md) → [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8df78",
      "incomplete_value": true,
      "site": "00b8df78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8df34",
      "incomplete_value": true,
      "site": "00b8df34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8dff0",
      "incomplete_value": true,
      "site": "00b8dff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8dfac",
      "incomplete_value": true,
      "site": "00b8dfac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b8df80",
      "incomplete_value": true,
      "site": "00b8df84",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b8df3c",
      "incomplete_value": true,
      "site": "00b8df40",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b8df70",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8df78",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8df7c",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8df70",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b8df78",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8df7c",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8df24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md#insn-00b8df24) · [`00b8df68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md#insn-00b8df68) · [`00b8df90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md#insn-00b8df90)
- 新版 `00b8df68`（命令位置の公開資料なし） · `00b8dfac`（命令位置の公開資料なし） · `00b8dfd4`（命令位置の公開資料なし）

~~~diff
- 00b8df24 ["INT_ADD", "register:40f0:8", ["const:b8df24:8", "const:4:8"]]
- 00b8df24 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b8df68 ["INT_ADD", "register:40f0:8", ["const:b8df68:8", "const:4:8"]]
+ 00b8df68 ["CALL", null, ["callee:00bdb420:8"]]
- 00b8df24 bytes 2b350194
+ 00b8df68 bytes 2e350194
- 00b8df68 ["INT_ADD", "register:40f0:8", ["const:b8df68:8", "const:4:8"]]
- 00b8df68 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b8dfac ["INT_ADD", "register:40f0:8", ["const:b8dfac:8", "const:4:8"]]
+ 00b8dfac ["CALL", null, ["callee:00be0ee0:8"]]
- 00b8df68 bytes ca4b0194
+ 00b8dfac bytes cd4b0194
- 00b8df90 ["INT_ADD", "register:40f0:8", ["const:b8df90:8", "const:4:8"]]
- 00b8df90 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b8dfd4 ["INT_ADD", "register:40f0:8", ["const:b8dfd4:8", "const:4:8"]]
+ 00b8dfd4 ["CALL", null, ["callee:00bdb440:8"]]
- 00b8df90 bytes 18350194
+ 00b8dfd4 bytes 1b350194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1463aa1ee95305a573514ebb6971ed13"></a>

### [`00b90af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md) → [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b90b84",
      "incomplete_value": true,
      "site": "00b90b84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b90b40",
      "incomplete_value": true,
      "site": "00b90b40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b90ff4",
      "incomplete_value": true,
      "site": "00b90ff4",
      "value": [
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
    "old": {
      "definition_site": "00b90fb0",
      "incomplete_value": true,
      "site": "00b90fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b90bb0",
      "incomplete_value": true,
      "site": "00b90bb8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b90b6c",
      "incomplete_value": true,
      "site": "00b90b74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "00b90b7c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b90b84",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b90b88",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b90b7c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b90b84",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b90b88",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md#insn-00b90b30) · [`00b90b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md#insn-00b90b74) · [`00b90bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md#insn-00b90bb4)
- 新版 `00b90b74`（命令位置の公開資料なし） · `00b90bb8`（命令位置の公開資料なし） · `00b90bf8`（命令位置の公開資料なし）

~~~diff
- 00b90b30 ["INT_ADD", "register:40f0:8", ["const:b90b30:8", "const:4:8"]]
- 00b90b30 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b90b74 ["INT_ADD", "register:40f0:8", ["const:b90b74:8", "const:4:8"]]
+ 00b90b74 ["CALL", null, ["callee:00bdb420:8"]]
- 00b90b30 bytes 282a0194
+ 00b90b74 bytes 2b2a0194
- 00b90b74 ["INT_ADD", "register:40f0:8", ["const:b90b74:8", "const:4:8"]]
- 00b90b74 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b90bb8 ["INT_ADD", "register:40f0:8", ["const:b90bb8:8", "const:4:8"]]
+ 00b90bb8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b90b74 bytes c7400194
+ 00b90bb8 bytes ca400194
- 00b90bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b90bb4 ["INT_ADD", "register:40f0:8", ["const:b90bb4:8", "const:4:8"]]
- 00b90bb4 ["CALLIND", null, ["register:0:8"]]
+ 00b90bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b90bf8 ["INT_ADD", "register:40f0:8", ["const:b90bf8:8", "const:4:8"]]
+ 00b90bf8 ["CALLIND", null, ["register:0:8"]]
- 00b90bb4 bytes 00013fd6
+ 00b90bf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78ccfc747ce5679a2569094f46aed933"></a>

### [`00b911d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md) → [`00b9121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_prepERNS_8ios_baseEPcRcS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b91254",
      "incomplete_value": true,
      "site": "00b9125c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b91210",
      "incomplete_value": true,
      "site": "00b91218",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b912d4",
      "incomplete_value": true,
      "site": "00b912dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91290",
      "incomplete_value": true,
      "site": "00b91298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b91264",
      "incomplete_value": true,
      "site": "00b91268",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b91220",
      "incomplete_value": true,
      "site": "00b91224",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b91254",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9125c",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91260",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b91254",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b9125c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91260",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md#insn-00b91208) · [`00b91244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md#insn-00b91244) · [`00b9124c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md#insn-00b9124c)
- 新版 `00b9124c`（命令位置の公開資料なし） · `00b91288`（命令位置の公開資料なし） · `00b91290`（命令位置の公開資料なし）

~~~diff
- 00b91208 ["INT_ADD", "register:40f0:8", ["const:b91208:8", "const:4:8"]]
- 00b91208 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9124c ["INT_ADD", "register:40f0:8", ["const:b9124c:8", "const:4:8"]]
+ 00b9124c ["CALL", null, ["callee:00bdb420:8"]]
- 00b91208 bytes 72280194
+ 00b9124c bytes 75280194
- 00b91244 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:df0:8"]]
- 00b91244 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b91288 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e40:8"]]
+ 00b91288 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b91244 bytes 00f846f9
+ 00b91288 bytes 002047f9
- 00b9124c ["INT_ADD", "register:40f0:8", ["const:b9124c:8", "const:4:8"]]
- 00b9124c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b91290 ["INT_ADD", "register:40f0:8", ["const:b91290:8", "const:4:8"]]
+ 00b91290 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9124c bytes 113f0194
+ 00b91290 bytes 143f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69d6353f36a8f2351ab7e9fc2c336d5d"></a>

### [`00b915ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b915ec.md) → [`00b91630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91630.md) _ZNSt6__ndk19__num_getIcE17__stage2_int_prepERNS_8ios_baseEPcRc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b91664",
      "incomplete_value": true,
      "site": "00b9166c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b91620",
      "incomplete_value": true,
      "site": "00b91628",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
      "definition_site": "00b916e4",
      "incomplete_value": true,
      "site": "00b916ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b916a0",
      "incomplete_value": true,
      "site": "00b916a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b91674",
      "incomplete_value": true,
      "site": "00b91678",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b91630",
      "incomplete_value": true,
      "site": "00b91634",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b91664",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9166c",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91670",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b91664",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b9166c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91670",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b915ec.md#insn-00b91618) · [`00b91654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b915ec.md#insn-00b91654) · [`00b9165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b915ec.md#insn-00b9165c)
- 新版 `00b9165c`（命令位置の公開資料なし） · `00b91698`（命令位置の公開資料なし） · `00b916a0`（命令位置の公開資料なし）

~~~diff
- 00b91618 ["INT_ADD", "register:40f0:8", ["const:b91618:8", "const:4:8"]]
- 00b91618 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9165c ["INT_ADD", "register:40f0:8", ["const:b9165c:8", "const:4:8"]]
+ 00b9165c ["CALL", null, ["callee:00bdb420:8"]]
- 00b91618 bytes 6e270194
+ 00b9165c bytes 71270194
- 00b91654 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:df0:8"]]
- 00b91654 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b91698 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e40:8"]]
+ 00b91698 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b91654 bytes 00f846f9
+ 00b91698 bytes 002047f9
- 00b9165c ["INT_ADD", "register:40f0:8", ["const:b9165c:8", "const:4:8"]]
- 00b9165c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b916a0 ["INT_ADD", "register:40f0:8", ["const:b916a0:8", "const:4:8"]]
+ 00b916a0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9165c bytes 0d3e0194
+ 00b916a0 bytes 103e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97749e6d1fc79454fa8af23016b6dcaf"></a>

### [`00b9176c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b9176c.md) → [`00b917b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b917b0.md) _ZNSt6__ndk19__num_getIwE19__stage2_float_prepERNS_8ios_baseEPwRwS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1570.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b917e8",
      "incomplete_value": true,
      "site": "00b917f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b917a4",
      "incomplete_value": true,
      "site": "00b917ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b91868",
      "incomplete_value": true,
      "site": "00b91870",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91824",
      "incomplete_value": true,
      "site": "00b9182c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b917f8",
      "incomplete_value": true,
      "site": "00b917fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b917b4",
      "incomplete_value": true,
      "site": "00b917b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b917e8",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b917f0",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b917f4",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b917e8",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b917f0",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b917f4",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9179c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b9176c.md#insn-00b9179c) · [`00b917d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b9176c.md#insn-00b917d8) · [`00b917e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b9176c.md#insn-00b917e0)
- 新版 `00b917e0`（命令位置の公開資料なし） · `00b9181c`（命令位置の公開資料なし） · `00b91824`（命令位置の公開資料なし）

~~~diff
- 00b9179c ["INT_ADD", "register:40f0:8", ["const:b9179c:8", "const:4:8"]]
- 00b9179c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b917e0 ["INT_ADD", "register:40f0:8", ["const:b917e0:8", "const:4:8"]]
+ 00b917e0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9179c bytes 0d270194
+ 00b917e0 bytes 10270194
- 00b917d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cc0:8"]]
- 00b917d8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9181c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d10:8"]]
+ 00b9181c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b917d8 bytes 006046f9
+ 00b9181c bytes 008846f9
- 00b917e0 ["INT_ADD", "register:40f0:8", ["const:b917e0:8", "const:4:8"]]
- 00b917e0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b91824 ["INT_ADD", "register:40f0:8", ["const:b91824:8", "const:4:8"]]
+ 00b91824 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b917e0 bytes ac3d0194
+ 00b91824 bytes af3d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6dafac164cb5c1bf5f76183a7829b58"></a>

### [`00b91b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91b6c.md) → [`00b91bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91bb0.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1550.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b91be4",
      "incomplete_value": true,
      "site": "00b91bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91ba0",
      "incomplete_value": true,
      "site": "00b91ba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00b91c64",
      "incomplete_value": true,
      "site": "00b91c6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91c20",
      "incomplete_value": true,
      "site": "00b91c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b91bf4",
      "incomplete_value": true,
      "site": "00b91bf8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b91bb0",
      "incomplete_value": true,
      "site": "00b91bb4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b91be4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b91bec",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91bf0",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b91be4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b91bec",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91bf0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91b6c.md#insn-00b91b98) · [`00b91bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91b6c.md#insn-00b91bd4) · [`00b91bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91b6c.md#insn-00b91bdc)
- 新版 `00b91bdc`（命令位置の公開資料なし） · `00b91c18`（命令位置の公開資料なし） · `00b91c20`（命令位置の公開資料なし）

~~~diff
- 00b91b98 ["INT_ADD", "register:40f0:8", ["const:b91b98:8", "const:4:8"]]
- 00b91b98 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b91bdc ["INT_ADD", "register:40f0:8", ["const:b91bdc:8", "const:4:8"]]
+ 00b91bdc ["CALL", null, ["callee:00bdb420:8"]]
- 00b91b98 bytes 0e260194
+ 00b91bdc bytes 11260194
- 00b91bd4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cc0:8"]]
- 00b91bd4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b91c18 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d10:8"]]
+ 00b91c18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b91bd4 bytes 006046f9
+ 00b91c18 bytes 008846f9
- 00b91bdc ["INT_ADD", "register:40f0:8", ["const:b91bdc:8", "const:4:8"]]
- 00b91bdc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b91c20 ["INT_ADD", "register:40f0:8", ["const:b91c20:8", "const:4:8"]]
+ 00b91c20 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b91bdc bytes ad3c0194
+ 00b91c20 bytes b03c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca74e51e145adb7e1bb38a1c800590c4"></a>

### [`00b91cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91cec.md) → [`00b91d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91d30.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b91d98",
      "incomplete_value": true,
      "site": "00b91d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91d54",
      "incomplete_value": true,
      "site": "00b91d54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b91da0",
      "incomplete_value": true,
      "site": "00b91da4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b91d5c",
      "incomplete_value": true,
      "site": "00b91d60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b91dc4",
      "incomplete_value": true,
      "site": "00b91dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91d80",
      "incomplete_value": true,
      "site": "00b91d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
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
      "00b91d90",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00b91d98",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91d9c",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b91d90",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00b91d98",
      "DATA",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b91d9c",
      "READ",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91cec.md#insn-00b91d44) · [`00b91d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91cec.md#insn-00b91d88) · [`00b91db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91cec.md#insn-00b91db0)
- 新版 `00b91d88`（命令位置の公開資料なし） · `00b91dcc`（命令位置の公開資料なし） · `00b91df4`（命令位置の公開資料なし）

~~~diff
- 00b91d44 ["INT_ADD", "register:40f0:8", ["const:b91d44:8", "const:4:8"]]
- 00b91d44 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b91d88 ["INT_ADD", "register:40f0:8", ["const:b91d88:8", "const:4:8"]]
+ 00b91d88 ["CALL", null, ["callee:00bdb420:8"]]
- 00b91d44 bytes a3250194
+ 00b91d88 bytes a6250194
- 00b91d88 ["INT_ADD", "register:40f0:8", ["const:b91d88:8", "const:4:8"]]
- 00b91d88 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b91dcc ["INT_ADD", "register:40f0:8", ["const:b91dcc:8", "const:4:8"]]
+ 00b91dcc ["CALL", null, ["callee:00be0ee0:8"]]
- 00b91d88 bytes 423c0194
+ 00b91dcc bytes 453c0194
- 00b91db0 ["INT_ADD", "register:40f0:8", ["const:b91db0:8", "const:4:8"]]
- 00b91db0 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b91df4 ["INT_ADD", "register:40f0:8", ["const:b91df4:8", "const:4:8"]]
+ 00b91df4 ["CALL", null, ["callee:00bdb440:8"]]
- 00b91db0 bytes 90250194
+ 00b91df4 bytes 93250194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5801f123a727bb322305a2ee9d2c48d8"></a>

### [`00b91ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md) → [`00b91f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md) FUN_00b91f10

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b91ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ebc.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b91f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f00.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b9210c",
      "incomplete_value": true,
      "site": "00b9210c",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b920c8",
      "incomplete_value": true,
      "site": "00b920c8",
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
            "const:950:8"
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
      "definition_site": "00b91ff0",
      "incomplete_value": true,
      "site": "00b92008",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b91fac",
      "incomplete_value": true,
      "site": "00b91fc4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b920ec",
      "incomplete_value": false,
      "site": "00b920f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b920a8",
      "incomplete_value": false,
      "site": "00b920ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b91fe4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b91ff0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b920ec",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b91fe4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b91ff0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b920ec",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md#insn-00b91fc4) · [`00b92084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md#insn-00b92084) · [`00b920ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91ecc.md#insn-00b920ac)
- 新版 `00b92008`（命令位置の公開資料なし） · `00b920c8`（命令位置の公開資料なし） · `00b920f0`（命令位置の公開資料なし）

~~~diff
- 00b91fc4 ["INT_ADD", "register:40f0:8", ["const:b91fc4:8", "const:4:8"]]
- 00b91fc4 ["CALL", null, ["callee:00b93334:8"]]
+ 00b92008 ["INT_ADD", "register:40f0:8", ["const:b92008:8", "const:4:8"]]
+ 00b92008 ["CALL", null, ["callee:00b93334:8"]]
- 00b91fc4 bytes cb040094
+ 00b92008 bytes cb040094
- 00b92084 ["INT_ADD", "register:40f0:8", ["const:b92084:8", "const:4:8"]]
- 00b92084 ["CALL", null, ["callee:00436790:8"]]
+ 00b920c8 ["INT_ADD", "register:40f0:8", ["const:b920c8:8", "const:4:8"]]
+ 00b920c8 ["CALL", null, ["callee:00436790:8"]]
- 00b92084 bytes c391e297
+ 00b920c8 bytes b291e297
- 00b920ac ["INT_ADD", "register:40f0:8", ["const:b920ac:8", "const:4:8"]]
- 00b920ac ["CALL", null, ["callee:00bdb000:8"]]
+ 00b920f0 ["INT_ADD", "register:40f0:8", ["const:b920f0:8", "const:4:8"]]
+ 00b920f0 ["CALL", null, ["callee:00bdb000:8"]]
- 00b920ac bytes c1230194
+ 00b920f0 bytes c4230194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30bd58b8fc7e385b139099175547660a"></a>

### [`00b92118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md) → [`00b9215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md) FUN_00b9215c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b92108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92108.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b9214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9214c.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92358",
      "incomplete_value": true,
      "site": "00b92358",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92314",
      "incomplete_value": true,
      "site": "00b92314",
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
            "const:950:8"
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
      "definition_site": "00b9223c",
      "incomplete_value": true,
      "site": "00b92254",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b921f8",
      "incomplete_value": true,
      "site": "00b92210",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b92338",
      "incomplete_value": false,
      "site": "00b9233c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b922f4",
      "incomplete_value": false,
      "site": "00b922f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b92230",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9223c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92338",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b92230",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9223c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92338",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md#insn-00b92210) · [`00b922d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md#insn-00b922d0) · [`00b922f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92118.md#insn-00b922f8)
- 新版 `00b92254`（命令位置の公開資料なし） · `00b92314`（命令位置の公開資料なし） · `00b9233c`（命令位置の公開資料なし）

~~~diff
- 00b92210 ["INT_ADD", "register:40f0:8", ["const:b92210:8", "const:4:8"]]
- 00b92210 ["CALL", null, ["callee:00b93334:8"]]
+ 00b92254 ["INT_ADD", "register:40f0:8", ["const:b92254:8", "const:4:8"]]
+ 00b92254 ["CALL", null, ["callee:00b93334:8"]]
- 00b92210 bytes 38040094
+ 00b92254 bytes 38040094
- 00b922d0 ["INT_ADD", "register:40f0:8", ["const:b922d0:8", "const:4:8"]]
- 00b922d0 ["CALL", null, ["callee:00436790:8"]]
+ 00b92314 ["INT_ADD", "register:40f0:8", ["const:b92314:8", "const:4:8"]]
+ 00b92314 ["CALL", null, ["callee:00436790:8"]]
- 00b922d0 bytes 3091e297
+ 00b92314 bytes 1f91e297
- 00b922f8 ["INT_ADD", "register:40f0:8", ["const:b922f8:8", "const:4:8"]]
- 00b922f8 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b9233c ["INT_ADD", "register:40f0:8", ["const:b9233c:8", "const:4:8"]]
+ 00b9233c ["CALL", null, ["callee:00bdb000:8"]]
- 00b922f8 bytes 2e230194
+ 00b9233c bytes 31230194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165b9b84448e6115e5c6d500a8b99bbf"></a>

### [`00b92364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md) → [`00b923a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md) FUN_00b923a8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b92354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92354.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b92398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92398.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92588",
      "incomplete_value": true,
      "site": "00b92588",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92544",
      "incomplete_value": true,
      "site": "00b92544",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9246c",
      "incomplete_value": true,
      "site": "00b92484",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b92428",
      "incomplete_value": true,
      "site": "00b92440",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b92568",
      "incomplete_value": false,
      "site": "00b9256c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92524",
      "incomplete_value": false,
      "site": "00b92528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b92460",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9246c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92568",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b92460",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9246c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92568",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md#insn-00b92440) · [`00b92500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md#insn-00b92500) · [`00b92528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92364.md#insn-00b92528)
- 新版 `00b92484`（命令位置の公開資料なし） · `00b92544`（命令位置の公開資料なし） · `00b9256c`（命令位置の公開資料なし）

~~~diff
- 00b92440 ["INT_ADD", "register:40f0:8", ["const:b92440:8", "const:4:8"]]
- 00b92440 ["CALL", null, ["callee:00b93334:8"]]
+ 00b92484 ["INT_ADD", "register:40f0:8", ["const:b92484:8", "const:4:8"]]
+ 00b92484 ["CALL", null, ["callee:00b93334:8"]]
- 00b92440 bytes ac030094
+ 00b92484 bytes ac030094
- 00b92500 ["INT_ADD", "register:40f0:8", ["const:b92500:8", "const:4:8"]]
- 00b92500 ["CALL", null, ["callee:00436790:8"]]
+ 00b92544 ["INT_ADD", "register:40f0:8", ["const:b92544:8", "const:4:8"]]
+ 00b92544 ["CALL", null, ["callee:00436790:8"]]
- 00b92500 bytes a490e297
+ 00b92544 bytes 9390e297
- 00b92528 ["INT_ADD", "register:40f0:8", ["const:b92528:8", "const:4:8"]]
- 00b92528 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b9256c ["INT_ADD", "register:40f0:8", ["const:b9256c:8", "const:4:8"]]
+ 00b9256c ["CALL", null, ["callee:00bdb000:8"]]
- 00b92528 bytes a2220194
+ 00b9256c bytes a5220194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53c61ccc53a49f07c9a3cc07e7f915b"></a>

### [`00b92594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md) → [`00b925d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md) FUN_00b925d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b92584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92584.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b925c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b927b8",
      "incomplete_value": true,
      "site": "00b927b8",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92774",
      "incomplete_value": true,
      "site": "00b92774",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9269c",
      "incomplete_value": true,
      "site": "00b926b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b92658",
      "incomplete_value": true,
      "site": "00b92670",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b92798",
      "incomplete_value": false,
      "site": "00b9279c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92754",
      "incomplete_value": false,
      "site": "00b92758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b92690",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9269c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92798",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b92690",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9269c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92798",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md#insn-00b92670) · [`00b92730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md#insn-00b92730) · [`00b92758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92594.md#insn-00b92758)
- 新版 `00b926b4`（命令位置の公開資料なし） · `00b92774`（命令位置の公開資料なし） · `00b9279c`（命令位置の公開資料なし）

~~~diff
- 00b92670 ["INT_ADD", "register:40f0:8", ["const:b92670:8", "const:4:8"]]
- 00b92670 ["CALL", null, ["callee:00b93334:8"]]
+ 00b926b4 ["INT_ADD", "register:40f0:8", ["const:b926b4:8", "const:4:8"]]
+ 00b926b4 ["CALL", null, ["callee:00b93334:8"]]
- 00b92670 bytes 20030094
+ 00b926b4 bytes 20030094
- 00b92730 ["INT_ADD", "register:40f0:8", ["const:b92730:8", "const:4:8"]]
- 00b92730 ["CALL", null, ["callee:00436790:8"]]
+ 00b92774 ["INT_ADD", "register:40f0:8", ["const:b92774:8", "const:4:8"]]
+ 00b92774 ["CALL", null, ["callee:00436790:8"]]
- 00b92730 bytes 1890e297
+ 00b92774 bytes 0790e297
- 00b92758 ["INT_ADD", "register:40f0:8", ["const:b92758:8", "const:4:8"]]
- 00b92758 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b9279c ["INT_ADD", "register:40f0:8", ["const:b9279c:8", "const:4:8"]]
+ 00b9279c ["CALL", null, ["callee:00bdb000:8"]]
- 00b92758 bytes 16220194
+ 00b9279c bytes 19220194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a27462e35b062882aa5328850966e5a"></a>

### [`00b927c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md) → [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) FUN_00b92808

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b927b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927b4.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00b927f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b927f8.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.09% / 新版 91.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92b4c",
      "incomplete_value": false,
      "site": "00b92b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92b08",
      "incomplete_value": false,
      "site": "00b92b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92b8c",
      "incomplete_value": false,
      "site": "00b92b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92b48",
      "incomplete_value": false,
      "site": "00b92b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92bc4",
      "incomplete_value": true,
      "site": "00b92bc4",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92b80",
      "incomplete_value": true,
      "site": "00b92b80",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b92908",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b92914",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92958",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b92908",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b92914",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92958",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md#insn-00b92938) · [`00b92970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md#insn-00b92970) · [`00b9299c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b927c4.md#insn-00b9299c)
- 新版 `00b9297c`（命令位置の公開資料なし） · `00b929b4`（命令位置の公開資料なし） · `00b929e0`（命令位置の公開資料なし）

~~~diff
- 00b92938 ["INT_ADD", "register:40f0:8", ["const:b92938:8", "const:4:8"]]
- 00b92938 ["CALL", null, ["callee:00b93334:8"]]
+ 00b9297c ["INT_ADD", "register:40f0:8", ["const:b9297c:8", "const:4:8"]]
+ 00b9297c ["CALL", null, ["callee:00b93334:8"]]
- 00b92938 bytes 6e020094
+ 00b9297c bytes 6e020094
- 00b92970 ["INT_ADD", "register:40f0:8", ["const:b92970:8", "const:4:8"]]
- 00b92970 ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b929b4 ["INT_ADD", "register:40f0:8", ["const:b929b4:8", "const:4:8"]]
+ 00b929b4 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b92970 bytes 6f300094
+ 00b929b4 bytes 6f300094
- 00b9299c ["INT_ADD", "register:40f0:8", ["const:b9299c:8", "const:4:8"]]
- 00b9299c ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b929e0 ["INT_ADD", "register:40f0:8", ["const:b929e0:8", "const:4:8"]]
+ 00b929e0 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b9299c bytes 64300094
+ 00b929e0 bytes 64300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0acf4d5254cdc9df407f2833b0b8c676"></a>

### [`00b92c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md) → [`00b92c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md) FUN_00b92c98

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b92c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c44.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00b92c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c88.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.02% / 新版 91.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b92fd4",
      "incomplete_value": false,
      "site": "00b92fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92f90",
      "incomplete_value": false,
      "site": "00b92f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b93014",
      "incomplete_value": false,
      "site": "00b93014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92fd0",
      "incomplete_value": false,
      "site": "00b92fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b9304c",
      "incomplete_value": true,
      "site": "00b9304c",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93008",
      "incomplete_value": true,
      "site": "00b93008",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b92d94",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b92d9c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92de4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b92d94",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b92d9c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b92de4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md#insn-00b92d6c) · [`00b92dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md#insn-00b92dc4) · [`00b92dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b92/00b92c54.md#insn-00b92dfc)
- 新版 `00b92db0`（命令位置の公開資料なし） · `00b92e08`（命令位置の公開資料なし） · `00b92e40`（命令位置の公開資料なし）

~~~diff
- 00b92d6c ["INT_ADD", "register:40f0:8", ["const:b92d6c:8", "const:4:8"]]
- 00b92d6c ["CALL", null, ["callee:00b93334:8"]]
+ 00b92db0 ["INT_ADD", "register:40f0:8", ["const:b92db0:8", "const:4:8"]]
+ 00b92db0 ["CALL", null, ["callee:00b93334:8"]]
- 00b92d6c bytes 61010094
+ 00b92db0 bytes 61010094
- 00b92dc4 ["INT_ADD", "register:40f0:8", ["const:b92dc4:8", "const:4:8"]]
- 00b92dc4 ["CALL", null, ["callee:00b93334:8"]]
+ 00b92e08 ["INT_ADD", "register:40f0:8", ["const:b92e08:8", "const:4:8"]]
+ 00b92e08 ["CALL", null, ["callee:00b93334:8"]]
- 00b92dc4 bytes 4b010094
+ 00b92e08 bytes 4b010094
- 00b92dfc ["INT_ADD", "register:40f0:8", ["const:b92dfc:8", "const:4:8"]]
- 00b92dfc ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b92e40 ["INT_ADD", "register:40f0:8", ["const:b92e40:8", "const:4:8"]]
+ 00b92e40 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b92dfc bytes 4c2f0094
+ 00b92e40 bytes 4c2f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b33d41bbf9987b4ccf198b385802eb"></a>

### [`00b930cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b930cc.md) → [`00b93110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93110.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPKv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b93204",
      "incomplete_value": true,
      "site": "00b93204",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b931c0",
      "incomplete_value": true,
      "site": "00b931c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b932f4",
      "incomplete_value": true,
      "site": "00b932f4",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b932b0",
      "incomplete_value": true,
      "site": "00b932b0",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9320c",
      "incomplete_value": true,
      "site": "00b93210",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b931c8",
      "incomplete_value": true,
      "site": "00b931cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b9313c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93154",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b9315c",
      "PARAM",
      [
        "storage",
        "00296777",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b9313c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93154",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b9315c",
      "PARAM",
      [
        "storage",
        "002966ea",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9312c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b930cc.md#insn-00b9312c) · [`00b931f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b930cc.md#insn-00b931f0) · [`00b93294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b930cc.md#insn-00b93294)
- 新版 `00b93170`（命令位置の公開資料なし） · `00b93234`（命令位置の公開資料なし） · `00b932d8`（命令位置の公開資料なし）

~~~diff
- 00b9312c ["INT_ADD", "register:40f0:8", ["const:b9312c:8", "const:4:8"]]
- 00b9312c ["CALL", null, ["callee:00b93334:8"]]
+ 00b93170 ["INT_ADD", "register:40f0:8", ["const:b93170:8", "const:4:8"]]
+ 00b93170 ["CALL", null, ["callee:00b93334:8"]]
- 00b9312c bytes 71000094
+ 00b93170 bytes 71000094
- 00b931f0 ["INT_ADD", "register:40f0:8", ["const:b931f0:8", "const:4:8"]]
- 00b931f0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b93234 ["INT_ADD", "register:40f0:8", ["const:b93234:8", "const:4:8"]]
+ 00b93234 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b931f0 bytes 28370194
+ 00b93234 bytes 2b370194
- 00b93294 ["INT_ADD", "register:40f0:8", ["const:b93294:8", "const:4:8"]]
- 00b93294 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b932d8 ["INT_ADD", "register:40f0:8", ["const:b932d8:8", "const:4:8"]]
+ 00b932d8 ["CALL", null, ["callee:00bdb000:8"]]
- 00b93294 bytes 471f0194
+ 00b932d8 bytes 4a1f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb784924f0cbe430023ccec291b7d601"></a>

### [`00b93420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93420.md) → [`00b93464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b934cc",
      "incomplete_value": true,
      "site": "00b934cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93488",
      "incomplete_value": true,
      "site": "00b93488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b934d4",
      "incomplete_value": true,
      "site": "00b934d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b93490",
      "incomplete_value": true,
      "site": "00b93494",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b934f8",
      "incomplete_value": true,
      "site": "00b93500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b934b4",
      "incomplete_value": true,
      "site": "00b934bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
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
      "00b934c4",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00b934cc",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b934d0",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b934c4",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00b934cc",
      "DATA",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b934d0",
      "READ",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93420.md#insn-00b93478) · [`00b934bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93420.md#insn-00b934bc) · [`00b934e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93420.md#insn-00b934e4)
- 新版 `00b934bc`（命令位置の公開資料なし） · `00b93500`（命令位置の公開資料なし） · `00b93528`（命令位置の公開資料なし）

~~~diff
- 00b93478 ["INT_ADD", "register:40f0:8", ["const:b93478:8", "const:4:8"]]
- 00b93478 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b934bc ["INT_ADD", "register:40f0:8", ["const:b934bc:8", "const:4:8"]]
+ 00b934bc ["CALL", null, ["callee:00bdb420:8"]]
- 00b93478 bytes d61f0194
+ 00b934bc bytes d91f0194
- 00b934bc ["INT_ADD", "register:40f0:8", ["const:b934bc:8", "const:4:8"]]
- 00b934bc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b93500 ["INT_ADD", "register:40f0:8", ["const:b93500:8", "const:4:8"]]
+ 00b93500 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b934bc bytes 75360194
+ 00b93500 bytes 78360194
- 00b934e4 ["INT_ADD", "register:40f0:8", ["const:b934e4:8", "const:4:8"]]
- 00b934e4 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b93528 ["INT_ADD", "register:40f0:8", ["const:b93528:8", "const:4:8"]]
+ 00b93528 ["CALL", null, ["callee:00bdb440:8"]]
- 00b934e4 bytes c31f0194
+ 00b93528 bytes c61f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec3330c2a21edfa6e8b03c1aa65e44d"></a>

### [`00b93600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md) → [`00b93644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md) FUN_00b93644

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b935f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b935f0.md) · 呼出先 8件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b93634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93634.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b93840",
      "incomplete_value": true,
      "site": "00b93840",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b937fc",
      "incomplete_value": true,
      "site": "00b937fc",
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
            "const:950:8"
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
      "definition_site": "00b93724",
      "incomplete_value": true,
      "site": "00b9373c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b936e0",
      "incomplete_value": true,
      "site": "00b936f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93820",
      "incomplete_value": false,
      "site": "00b93824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b937dc",
      "incomplete_value": false,
      "site": "00b937e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b93718",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93724",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93820",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b93718",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93724",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93820",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b936f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md#insn-00b936f8) · [`00b937b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md#insn-00b937b8) · [`00b937e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93600.md#insn-00b937e0)
- 新版 `00b9373c`（命令位置の公開資料なし） · `00b937fc`（命令位置の公開資料なし） · `00b93824`（命令位置の公開資料なし）

~~~diff
- 00b936f8 ["INT_ADD", "register:40f0:8", ["const:b936f8:8", "const:4:8"]]
- 00b936f8 ["CALL", null, ["callee:00b93334:8"]]
+ 00b9373c ["INT_ADD", "register:40f0:8", ["const:b9373c:8", "const:4:8"]]
+ 00b9373c ["CALL", null, ["callee:00b93334:8"]]
- 00b936f8 bytes fefeff97
+ 00b9373c bytes fefeff97
- 00b937b8 ["INT_ADD", "register:40f0:8", ["const:b937b8:8", "const:4:8"]]
- 00b937b8 ["CALL", null, ["callee:00b94a74:8"]]
+ 00b937fc ["INT_ADD", "register:40f0:8", ["const:b937fc:8", "const:4:8"]]
+ 00b937fc ["CALL", null, ["callee:00b94a74:8"]]
- 00b937b8 bytes 9e040094
+ 00b937fc bytes 9e040094
- 00b937e0 ["INT_ADD", "register:40f0:8", ["const:b937e0:8", "const:4:8"]]
- 00b937e0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b93824 ["INT_ADD", "register:40f0:8", ["const:b93824:8", "const:4:8"]]
+ 00b93824 ["CALL", null, ["callee:00bdb000:8"]]
- 00b937e0 bytes f41d0194
+ 00b93824 bytes f71d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94069a97aa5ea2d4464d4f705bcd83b8"></a>

### [`00b9384c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md) → [`00b93890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md) FUN_00b93890

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b9383c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9383c.md) · 呼出先 8件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b93880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93880.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b93a8c",
      "incomplete_value": true,
      "site": "00b93a8c",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93a48",
      "incomplete_value": true,
      "site": "00b93a48",
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
            "const:950:8"
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
      "definition_site": "00b93970",
      "incomplete_value": true,
      "site": "00b93988",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b9392c",
      "incomplete_value": true,
      "site": "00b93944",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93a6c",
      "incomplete_value": false,
      "site": "00b93a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93a28",
      "incomplete_value": false,
      "site": "00b93a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b93964",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93970",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93a6c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b93964",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93970",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93a6c",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md#insn-00b93944) · [`00b93a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md#insn-00b93a04) · [`00b93a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b9384c.md#insn-00b93a2c)
- 新版 `00b93988`（命令位置の公開資料なし） · `00b93a48`（命令位置の公開資料なし） · `00b93a70`（命令位置の公開資料なし）

~~~diff
- 00b93944 ["INT_ADD", "register:40f0:8", ["const:b93944:8", "const:4:8"]]
- 00b93944 ["CALL", null, ["callee:00b93334:8"]]
+ 00b93988 ["INT_ADD", "register:40f0:8", ["const:b93988:8", "const:4:8"]]
+ 00b93988 ["CALL", null, ["callee:00b93334:8"]]
- 00b93944 bytes 6bfeff97
+ 00b93988 bytes 6bfeff97
- 00b93a04 ["INT_ADD", "register:40f0:8", ["const:b93a04:8", "const:4:8"]]
- 00b93a04 ["CALL", null, ["callee:00b94a74:8"]]
+ 00b93a48 ["INT_ADD", "register:40f0:8", ["const:b93a48:8", "const:4:8"]]
+ 00b93a48 ["CALL", null, ["callee:00b94a74:8"]]
- 00b93a04 bytes 0b040094
+ 00b93a48 bytes 0b040094
- 00b93a2c ["INT_ADD", "register:40f0:8", ["const:b93a2c:8", "const:4:8"]]
- 00b93a2c ["CALL", null, ["callee:00bdb000:8"]]
+ 00b93a70 ["INT_ADD", "register:40f0:8", ["const:b93a70:8", "const:4:8"]]
+ 00b93a70 ["CALL", null, ["callee:00bdb000:8"]]
- 00b93a2c bytes 611d0194
+ 00b93a70 bytes 641d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4c67761e9a54527e230b5c26a2640c5"></a>

### [`00b93a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md) → [`00b93adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md) FUN_00b93adc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b93a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a88.md) · 呼出先 8件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b93acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93acc.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b93cbc",
      "incomplete_value": true,
      "site": "00b93cbc",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93c78",
      "incomplete_value": true,
      "site": "00b93c78",
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
            "const:950:8"
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
      "definition_site": "00b93ba0",
      "incomplete_value": true,
      "site": "00b93bb8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b93b5c",
      "incomplete_value": true,
      "site": "00b93b74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93c9c",
      "incomplete_value": false,
      "site": "00b93ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93c58",
      "incomplete_value": false,
      "site": "00b93c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b93b94",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93ba0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93c9c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b93b94",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93ba0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93c9c",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md#insn-00b93b74) · [`00b93c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md#insn-00b93c34) · [`00b93c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93a98.md#insn-00b93c5c)
- 新版 `00b93bb8`（命令位置の公開資料なし） · `00b93c78`（命令位置の公開資料なし） · `00b93ca0`（命令位置の公開資料なし）

~~~diff
- 00b93b74 ["INT_ADD", "register:40f0:8", ["const:b93b74:8", "const:4:8"]]
- 00b93b74 ["CALL", null, ["callee:00b93334:8"]]
+ 00b93bb8 ["INT_ADD", "register:40f0:8", ["const:b93bb8:8", "const:4:8"]]
+ 00b93bb8 ["CALL", null, ["callee:00b93334:8"]]
- 00b93b74 bytes dffdff97
+ 00b93bb8 bytes dffdff97
- 00b93c34 ["INT_ADD", "register:40f0:8", ["const:b93c34:8", "const:4:8"]]
- 00b93c34 ["CALL", null, ["callee:00b94a74:8"]]
+ 00b93c78 ["INT_ADD", "register:40f0:8", ["const:b93c78:8", "const:4:8"]]
+ 00b93c78 ["CALL", null, ["callee:00b94a74:8"]]
- 00b93c34 bytes 7f030094
+ 00b93c78 bytes 7f030094
- 00b93c5c ["INT_ADD", "register:40f0:8", ["const:b93c5c:8", "const:4:8"]]
- 00b93c5c ["CALL", null, ["callee:00bdb000:8"]]
+ 00b93ca0 ["INT_ADD", "register:40f0:8", ["const:b93ca0:8", "const:4:8"]]
+ 00b93ca0 ["CALL", null, ["callee:00bdb000:8"]]
- 00b93c5c bytes d51c0194
+ 00b93ca0 bytes d81c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-857090a755862da2a552114ee018b033"></a>

### [`00b93cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md) → [`00b93d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md) FUN_00b93d0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b93cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cb8.md) · 呼出先 8件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 1件 [`00b93cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93cfc.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b93eec",
      "incomplete_value": true,
      "site": "00b93eec",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93ea8",
      "incomplete_value": true,
      "site": "00b93ea8",
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
            "const:950:8"
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
      "definition_site": "00b93dd0",
      "incomplete_value": true,
      "site": "00b93de8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "old": {
      "definition_site": "00b93d8c",
      "incomplete_value": true,
      "site": "00b93da4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b93ecc",
      "incomplete_value": false,
      "site": "00b93ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93e88",
      "incomplete_value": false,
      "site": "00b93e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00b93dc4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93dd0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93ecc",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b93dc4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b93dd0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b93ecc",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md#insn-00b93da4) · [`00b93e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md#insn-00b93e64) · [`00b93e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93cc8.md#insn-00b93e8c)
- 新版 `00b93de8`（命令位置の公開資料なし） · `00b93ea8`（命令位置の公開資料なし） · `00b93ed0`（命令位置の公開資料なし）

~~~diff
- 00b93da4 ["INT_ADD", "register:40f0:8", ["const:b93da4:8", "const:4:8"]]
- 00b93da4 ["CALL", null, ["callee:00b93334:8"]]
+ 00b93de8 ["INT_ADD", "register:40f0:8", ["const:b93de8:8", "const:4:8"]]
+ 00b93de8 ["CALL", null, ["callee:00b93334:8"]]
- 00b93da4 bytes 53fdff97
+ 00b93de8 bytes 53fdff97
- 00b93e64 ["INT_ADD", "register:40f0:8", ["const:b93e64:8", "const:4:8"]]
- 00b93e64 ["CALL", null, ["callee:00b94a74:8"]]
+ 00b93ea8 ["INT_ADD", "register:40f0:8", ["const:b93ea8:8", "const:4:8"]]
+ 00b93ea8 ["CALL", null, ["callee:00b94a74:8"]]
- 00b93e64 bytes f3020094
+ 00b93ea8 bytes f3020094
- 00b93e8c ["INT_ADD", "register:40f0:8", ["const:b93e8c:8", "const:4:8"]]
- 00b93e8c ["CALL", null, ["callee:00bdb000:8"]]
+ 00b93ed0 ["INT_ADD", "register:40f0:8", ["const:b93ed0:8", "const:4:8"]]
+ 00b93ed0 ["CALL", null, ["callee:00bdb000:8"]]
- 00b93e8c bytes 491c0194
+ 00b93ed0 bytes 4c1c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-033588bddbd0c9b7e2561e7504e97e54"></a>

### [`00b93ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md) → [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) FUN_00b93f3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b93ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ee8.md) · 呼出先 12件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00b93f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f2c.md) · 呼出先 12件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.09% / 新版 91.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b94280",
      "incomplete_value": false,
      "site": "00b94280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9423c",
      "incomplete_value": false,
      "site": "00b9423c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b942c0",
      "incomplete_value": false,
      "site": "00b942c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9427c",
      "incomplete_value": false,
      "site": "00b9427c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b942f8",
      "incomplete_value": true,
      "site": "00b942f8",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b942b4",
      "incomplete_value": true,
      "site": "00b942b4",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b9403c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b94048",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b9408c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b9403c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b94048",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b9408c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md#insn-00b94014) · [`00b9406c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md#insn-00b9406c) · [`00b940a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b93ef8.md#insn-00b940a4)
- 新版 `00b94058`（命令位置の公開資料なし） · `00b940b0`（命令位置の公開資料なし） · `00b940e8`（命令位置の公開資料なし）

~~~diff
- 00b94014 ["INT_ADD", "register:40f0:8", ["const:b94014:8", "const:4:8"]]
- 00b94014 ["CALL", null, ["callee:00b93334:8"]]
+ 00b94058 ["INT_ADD", "register:40f0:8", ["const:b94058:8", "const:4:8"]]
+ 00b94058 ["CALL", null, ["callee:00b93334:8"]]
- 00b94014 bytes b7fcff97
+ 00b94058 bytes b7fcff97
- 00b9406c ["INT_ADD", "register:40f0:8", ["const:b9406c:8", "const:4:8"]]
- 00b9406c ["CALL", null, ["callee:00b93334:8"]]
+ 00b940b0 ["INT_ADD", "register:40f0:8", ["const:b940b0:8", "const:4:8"]]
+ 00b940b0 ["CALL", null, ["callee:00b93334:8"]]
- 00b9406c bytes a1fcff97
+ 00b940b0 bytes a1fcff97
- 00b940a4 ["INT_ADD", "register:40f0:8", ["const:b940a4:8", "const:4:8"]]
- 00b940a4 ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b940e8 ["INT_ADD", "register:40f0:8", ["const:b940e8:8", "const:4:8"]]
+ 00b940e8 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b940a4 bytes a22a0094
+ 00b940e8 bytes a22a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a12fba88d0ff75ea6c27c06ff4672db"></a>

### [`00b94388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md) → [`00b943cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md) FUN_00b943cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b94378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94378.md) · 呼出先 12件 [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00b943bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943bc.md) · 呼出先 12件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.02% / 新版 91.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b94708",
      "incomplete_value": false,
      "site": "00b94708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b946c4",
      "incomplete_value": false,
      "site": "00b946c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b94748",
      "incomplete_value": false,
      "site": "00b94748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b94704",
      "incomplete_value": false,
      "site": "00b94704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b94780",
      "incomplete_value": true,
      "site": "00b94780",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9473c",
      "incomplete_value": true,
      "site": "00b9473c",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b944c8",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b944d0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94518",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b944c8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b944d0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94518",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b944a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md#insn-00b944a0) · [`00b944f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md#insn-00b944f8) · [`00b94530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94388.md#insn-00b94530)
- 新版 `00b944e4`（命令位置の公開資料なし） · `00b9453c`（命令位置の公開資料なし） · `00b94574`（命令位置の公開資料なし）

~~~diff
- 00b944a0 ["INT_ADD", "register:40f0:8", ["const:b944a0:8", "const:4:8"]]
- 00b944a0 ["CALL", null, ["callee:00b93334:8"]]
+ 00b944e4 ["INT_ADD", "register:40f0:8", ["const:b944e4:8", "const:4:8"]]
+ 00b944e4 ["CALL", null, ["callee:00b93334:8"]]
- 00b944a0 bytes 94fbff97
+ 00b944e4 bytes 94fbff97
- 00b944f8 ["INT_ADD", "register:40f0:8", ["const:b944f8:8", "const:4:8"]]
- 00b944f8 ["CALL", null, ["callee:00b93334:8"]]
+ 00b9453c ["INT_ADD", "register:40f0:8", ["const:b9453c:8", "const:4:8"]]
+ 00b9453c ["CALL", null, ["callee:00b93334:8"]]
- 00b944f8 bytes 7efbff97
+ 00b9453c bytes 7efbff97
- 00b94530 ["INT_ADD", "register:40f0:8", ["const:b94530:8", "const:4:8"]]
- 00b94530 ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b94574 ["INT_ADD", "register:40f0:8", ["const:b94574:8", "const:4:8"]]
+ 00b94574 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b94530 bytes 7f290094
+ 00b94574 bytes 7f290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113c43088deba54dcfb81ba08730ccba"></a>

### [`00b94800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94800.md) → [`00b94844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94844.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPKv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b932f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b93/00b932f0.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9493c",
      "incomplete_value": true,
      "site": "00b9493c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b948f8",
      "incomplete_value": true,
      "site": "00b948f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b94a34",
      "incomplete_value": true,
      "site": "00b94a34",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b949f0",
      "incomplete_value": true,
      "site": "00b949f0",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b94944",
      "incomplete_value": true,
      "site": "00b94948",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b94900",
      "incomplete_value": true,
      "site": "00b94904",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b94874",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9488c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94894",
      "PARAM",
      [
        "storage",
        "00296777",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b94874",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9488c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94894",
      "PARAM",
      [
        "storage",
        "002966ea",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94800.md#insn-00b94864) · [`00b948e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94800.md#insn-00b948e8) · [`00b9492c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94800.md#insn-00b9492c)
- 新版 `00b948a8`（命令位置の公開資料なし） · `00b9492c`（命令位置の公開資料なし） · `00b94970`（命令位置の公開資料なし）

~~~diff
- 00b94864 ["INT_ADD", "register:40f0:8", ["const:b94864:8", "const:4:8"]]
- 00b94864 ["CALL", null, ["callee:00b93334:8"]]
+ 00b948a8 ["INT_ADD", "register:40f0:8", ["const:b948a8:8", "const:4:8"]]
+ 00b948a8 ["CALL", null, ["callee:00b93334:8"]]
- 00b94864 bytes a3faff97
+ 00b948a8 bytes a3faff97
- 00b948e8 ["INT_ADD", "register:40f0:8", ["const:b948e8:8", "const:4:8"]]
- 00b948e8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9492c ["INT_ADD", "register:40f0:8", ["const:b9492c:8", "const:4:8"]]
+ 00b9492c ["CALL", null, ["callee:00bdb420:8"]]
- 00b948e8 bytes ba1a0194
+ 00b9492c bytes bd1a0194
- 00b9492c ["INT_ADD", "register:40f0:8", ["const:b9492c:8", "const:4:8"]]
- 00b9492c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b94970 ["INT_ADD", "register:40f0:8", ["const:b94970:8", "const:4:8"]]
+ 00b94970 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9492c bytes 59310194
+ 00b94970 bytes 5c310194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751b841601527b4a0a163b2ec4493fe9"></a>

### [`00b94c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94c30.md) → [`00b94c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94c74.md) _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1590.md) · 呼出先 4件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be15e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15e0.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b94cbc",
      "incomplete_value": true,
      "site": "00b94cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b94c78",
      "incomplete_value": true,
      "site": "00b94c78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b94d24",
      "incomplete_value": true,
      "site": "00b94d24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b94ce0",
      "incomplete_value": true,
      "site": "00b94ce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b94cc8",
      "incomplete_value": true,
      "site": "00b94ccc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b94c84",
      "incomplete_value": true,
      "site": "00b94c88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b94ca4",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b94cbc",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b94cc4",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b94ca4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b94cbc",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b94cc4",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94c30.md#insn-00b94c60) · [`00b94cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94c30.md#insn-00b94cb0) · [`00b94d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94c30.md#insn-00b94d14)
- 新版 `00b94ca4`（命令位置の公開資料なし） · `00b94cf4`（命令位置の公開資料なし） · `00b94d58`（命令位置の公開資料なし）

~~~diff
- 00b94c60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:df0:8"]]
- 00b94c60 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b94ca4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e40:8"]]
+ 00b94ca4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b94c60 bytes b5fa46f9
+ 00b94ca4 bytes b52247f9
- 00b94cb0 ["INT_ADD", "register:40f0:8", ["const:b94cb0:8", "const:4:8"]]
- 00b94cb0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b94cf4 ["INT_ADD", "register:40f0:8", ["const:b94cf4:8", "const:4:8"]]
+ 00b94cf4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b94cb0 bytes 78300194
+ 00b94cf4 bytes 7b300194
- 00b94d14 ["INT_ADD", "register:40f0:8", ["const:b94d14:8", "const:4:8"]]
- 00b94d14 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b94d58 ["INT_ADD", "register:40f0:8", ["const:b94d58:8", "const:4:8"]]
+ 00b94d58 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b94d14 bytes 5f300194
+ 00b94d58 bytes 62300194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e2ff3c288f057db02f2a0856027bfb"></a>

### [`00b95024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95024.md) → [`00b95068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95068.md) _ZNSt6__ndk19__num_putIcE23__widen_and_group_floatEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15a0.md) · 呼出先 7件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be15f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15f0.md) · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b950b0",
      "incomplete_value": true,
      "site": "00b950b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9506c",
      "incomplete_value": true,
      "site": "00b9506c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b95118",
      "incomplete_value": true,
      "site": "00b95118",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b950d4",
      "incomplete_value": true,
      "site": "00b950d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b952bc",
      "incomplete_value": true,
      "site": "00b952bc",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95278",
      "incomplete_value": true,
      "site": "00b95278",
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
            "const:950:8"
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
      "00b95098",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b950b0",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b950b8",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b95098",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b950b0",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b950b8",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95024.md#insn-00b95054) · [`00b950a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95024.md#insn-00b950a4) · [`00b95108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95024.md#insn-00b95108)
- 新版 `00b95098`（命令位置の公開資料なし） · `00b950e8`（命令位置の公開資料なし） · `00b9514c`（命令位置の公開資料なし）

~~~diff
- 00b95054 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:df0:8"]]
- 00b95054 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b95098 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:e40:8"]]
+ 00b95098 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b95054 bytes d6fa46f9
+ 00b95098 bytes d62247f9
- 00b950a4 ["INT_ADD", "register:40f0:8", ["const:b950a4:8", "const:4:8"]]
- 00b950a4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b950e8 ["INT_ADD", "register:40f0:8", ["const:b950e8:8", "const:4:8"]]
+ 00b950e8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b950a4 bytes 7b2f0194
+ 00b950e8 bytes 7e2f0194
- 00b95108 ["INT_ADD", "register:40f0:8", ["const:b95108:8", "const:4:8"]]
- 00b95108 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9514c ["INT_ADD", "register:40f0:8", ["const:b9514c:8", "const:4:8"]]
+ 00b9514c ["CALL", null, ["callee:00be0ee0:8"]]
- 00b95108 bytes 622f0194
+ 00b9514c bytes 652f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-897dfc1b6608a0bc98aeb350d0de5c0e"></a>

### [`00b9561c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b9561c.md) → [`00b95660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95660.md) _ZNSt6__ndk19__num_putIwE21__widen_and_group_intEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15b0.md) · 呼出先 4件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be1600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1600.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b956a8",
      "incomplete_value": true,
      "site": "00b956a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95664",
      "incomplete_value": true,
      "site": "00b95664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b95710",
      "incomplete_value": true,
      "site": "00b95710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b956cc",
      "incomplete_value": true,
      "site": "00b956cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b956b4",
      "incomplete_value": true,
      "site": "00b956b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b95670",
      "incomplete_value": true,
      "site": "00b95674",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b95690",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b956a8",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b956b0",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b95690",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b956a8",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b956b0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9564c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b9561c.md#insn-00b9564c) · [`00b9569c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b9561c.md#insn-00b9569c) · [`00b95700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b9561c.md#insn-00b95700)
- 新版 `00b95690`（命令位置の公開資料なし） · `00b956e0`（命令位置の公開資料なし） · `00b95744`（命令位置の公開資料なし）

~~~diff
- 00b9564c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc0:8"]]
- 00b9564c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b95690 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d10:8"]]
+ 00b95690 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9564c bytes d66246f9
+ 00b95690 bytes d68a46f9
- 00b9569c ["INT_ADD", "register:40f0:8", ["const:b9569c:8", "const:4:8"]]
- 00b9569c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b956e0 ["INT_ADD", "register:40f0:8", ["const:b956e0:8", "const:4:8"]]
+ 00b956e0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9569c bytes fd2d0194
+ 00b956e0 bytes 002e0194
- 00b95700 ["INT_ADD", "register:40f0:8", ["const:b95700:8", "const:4:8"]]
- 00b95700 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b95744 ["INT_ADD", "register:40f0:8", ["const:b95744:8", "const:4:8"]]
+ 00b95744 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b95700 bytes e42d0194
+ 00b95744 bytes e72d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d751169cbc910e01d91949e082cb5f2"></a>

### [`00b95a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95a18.md) → [`00b95a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95a5c.md) _ZNSt6__ndk19__num_putIwE23__widen_and_group_floatEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15c0.md) · 呼出先 7件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be1610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1610.md) · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.71% / 新版 96.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b95aa4",
      "incomplete_value": true,
      "site": "00b95aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95a60",
      "incomplete_value": true,
      "site": "00b95a60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b95b0c",
      "incomplete_value": true,
      "site": "00b95b0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95ac8",
      "incomplete_value": true,
      "site": "00b95ac8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b95ca8",
      "incomplete_value": true,
      "site": "00b95ca8",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95c64",
      "incomplete_value": true,
      "site": "00b95c64",
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
            "const:950:8"
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
      "00b95a8c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b95aa4",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b95aac",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b95a8c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b95aa4",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b95aac",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95a18.md#insn-00b95a48) · [`00b95a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95a18.md#insn-00b95a98) · [`00b95afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b95/00b95a18.md#insn-00b95afc)
- 新版 `00b95a8c`（命令位置の公開資料なし） · `00b95adc`（命令位置の公開資料なし） · `00b95b40`（命令位置の公開資料なし）

~~~diff
- 00b95a48 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc0:8"]]
- 00b95a48 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b95a8c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d10:8"]]
+ 00b95a8c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b95a48 bytes d66246f9
+ 00b95a8c bytes d68a46f9
- 00b95a98 ["INT_ADD", "register:40f0:8", ["const:b95a98:8", "const:4:8"]]
- 00b95a98 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b95adc ["INT_ADD", "register:40f0:8", ["const:b95adc:8", "const:4:8"]]
+ 00b95adc ["CALL", null, ["callee:00be0ee0:8"]]
- 00b95a98 bytes fe2c0194
+ 00b95adc bytes 012d0194
- 00b95afc ["INT_ADD", "register:40f0:8", ["const:b95afc:8", "const:4:8"]]
- 00b95afc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b95b40 ["INT_ADD", "register:40f0:8", ["const:b95b40:8", "const:4:8"]]
+ 00b95b40 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b95afc bytes e52c0194
+ 00b95b40 bytes e82c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e195f5f4ac86e48dc9aa6efa97930a"></a>

### [`00b96010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96010.md) → [`00b96054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96054.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKcSC_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8d0.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.67% / 新版 99.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b960a8",
      "incomplete_value": true,
      "site": "00b960b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96064",
      "incomplete_value": true,
      "site": "00b9606c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b960b8",
      "incomplete_value": true,
      "site": "00b960bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b96074",
      "incomplete_value": true,
      "site": "00b96078",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b960dc",
      "incomplete_value": true,
      "site": "00b960e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96098",
      "incomplete_value": true,
      "site": "00b960a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b960a8",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b960b0",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b960b4",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b960a8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b960b0",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b960b4",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96010.md#insn-00b9605c) · [`00b960a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96010.md#insn-00b960a0) · [`00b960c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96010.md#insn-00b960c8)
- 新版 `00b960a0`（命令位置の公開資料なし） · `00b960e4`（命令位置の公開資料なし） · `00b9610c`（命令位置の公開資料なし）

~~~diff
- 00b9605c ["INT_ADD", "register:40f0:8", ["const:b9605c:8", "const:4:8"]]
- 00b9605c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b960a0 ["INT_ADD", "register:40f0:8", ["const:b960a0:8", "const:4:8"]]
+ 00b960a0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9605c bytes dd140194
+ 00b960a0 bytes e0140194
- 00b960a0 ["INT_ADD", "register:40f0:8", ["const:b960a0:8", "const:4:8"]]
- 00b960a0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b960e4 ["INT_ADD", "register:40f0:8", ["const:b960e4:8", "const:4:8"]]
+ 00b960e4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b960a0 bytes 7c2b0194
+ 00b960e4 bytes 7f2b0194
- 00b960c8 ["INT_ADD", "register:40f0:8", ["const:b960c8:8", "const:4:8"]]
- 00b960c8 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b9610c ["INT_ADD", "register:40f0:8", ["const:b9610c:8", "const:4:8"]]
+ 00b9610c ["CALL", null, ["callee:00bdb440:8"]]
- 00b960c8 bytes ca140194
+ 00b9610c bytes cd140194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff69b605a266bc9a5de44053cbe162f2"></a>

### [`00b965c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md) → [`00b96608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b96648",
      "incomplete_value": true,
      "site": "00b96650",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96604",
      "incomplete_value": true,
      "site": "00b9660c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b96658",
      "incomplete_value": true,
      "site": "00b9665c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b96614",
      "incomplete_value": true,
      "site": "00b96618",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b96678",
      "incomplete_value": true,
      "site": "00b96680",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96634",
      "incomplete_value": true,
      "site": "00b9663c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b96648",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b96650",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96654",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b96648",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b96650",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96654",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9663c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md#insn-00b9663c) · [`00b965fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md#insn-00b965fc) · [`00b96604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md#insn-00b96604)
- 新版 `00b96680`（命令位置の公開資料なし） · `00b96640`（命令位置の公開資料なし） · `00b96648`（命令位置の公開資料なし）

~~~diff
- 00b9663c ["INT_ADD", "register:40f0:8", ["const:b9663c:8", "const:4:8"]]
- 00b9663c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b96680 ["INT_ADD", "register:40f0:8", ["const:b96680:8", "const:4:8"]]
+ 00b96680 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9663c bytes 152a0194
+ 00b96680 bytes 182a0194
- 00b965fc ["INT_ADD", "register:40f0:8", ["const:b965fc:8", "const:4:8"]]
- 00b965fc ["CALL", null, ["callee:00bdb420:8"]]
+ 00b96640 ["INT_ADD", "register:40f0:8", ["const:b96640:8", "const:4:8"]]
+ 00b96640 ["CALL", null, ["callee:00bdb420:8"]]
- 00b965fc bytes 75130194
+ 00b96640 bytes 78130194
- 00b96604 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:df0:8"]]
- 00b96604 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b96648 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e40:8"]]
+ 00b96648 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b96604 bytes 18fb46f9
+ 00b96648 bytes 182347f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d0a2ffe5375c931d9616d021947383"></a>

### [`00b967d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md) → [`00b9681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9685c",
      "incomplete_value": true,
      "site": "00b96864",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96818",
      "incomplete_value": true,
      "site": "00b96820",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9686c",
      "incomplete_value": true,
      "site": "00b96870",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b96828",
      "incomplete_value": true,
      "site": "00b9682c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9688c",
      "incomplete_value": true,
      "site": "00b96894",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96848",
      "incomplete_value": true,
      "site": "00b96850",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b9685c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b96864",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96868",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b9685c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b96864",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96868",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md#insn-00b96850) · [`00b96810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md#insn-00b96810) · [`00b96818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md#insn-00b96818)
- 新版 `00b96894`（命令位置の公開資料なし） · `00b96854`（命令位置の公開資料なし） · `00b9685c`（命令位置の公開資料なし）

~~~diff
- 00b96850 ["INT_ADD", "register:40f0:8", ["const:b96850:8", "const:4:8"]]
- 00b96850 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b96894 ["INT_ADD", "register:40f0:8", ["const:b96894:8", "const:4:8"]]
+ 00b96894 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b96850 bytes 90290194
+ 00b96894 bytes 93290194
- 00b96810 ["INT_ADD", "register:40f0:8", ["const:b96810:8", "const:4:8"]]
- 00b96810 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b96854 ["INT_ADD", "register:40f0:8", ["const:b96854:8", "const:4:8"]]
+ 00b96854 ["CALL", null, ["callee:00bdb420:8"]]
- 00b96810 bytes f0120194
+ 00b96854 bytes f3120194
- 00b96818 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:df0:8"]]
- 00b96818 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9685c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e40:8"]]
+ 00b9685c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b96818 bytes 18fb46f9
+ 00b9685c bytes 182347f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d58c697652ee2b4cf7571c4ab086f32"></a>

### [`00b969dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md) → [`00b96a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b96a5c",
      "incomplete_value": true,
      "site": "00b96a64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96a18",
      "incomplete_value": true,
      "site": "00b96a20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b96a6c",
      "incomplete_value": true,
      "site": "00b96a70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b96a28",
      "incomplete_value": true,
      "site": "00b96a2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b96a90",
      "incomplete_value": true,
      "site": "00b96a98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96a4c",
      "incomplete_value": true,
      "site": "00b96a54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b96a5c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b96a64",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96a68",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b96a5c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b96a64",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96a68",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md#insn-00b96a10) · [`00b96a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md#insn-00b96a54) · [`00b96a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b969dc.md#insn-00b96a7c)
- 新版 `00b96a54`（命令位置の公開資料なし） · `00b96a98`（命令位置の公開資料なし） · `00b96ac0`（命令位置の公開資料なし）

~~~diff
- 00b96a10 ["INT_ADD", "register:40f0:8", ["const:b96a10:8", "const:4:8"]]
- 00b96a10 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b96a54 ["INT_ADD", "register:40f0:8", ["const:b96a54:8", "const:4:8"]]
+ 00b96a54 ["CALL", null, ["callee:00bdb420:8"]]
- 00b96a10 bytes 70120194
+ 00b96a54 bytes 73120194
- 00b96a54 ["INT_ADD", "register:40f0:8", ["const:b96a54:8", "const:4:8"]]
- 00b96a54 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b96a98 ["INT_ADD", "register:40f0:8", ["const:b96a98:8", "const:4:8"]]
+ 00b96a98 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b96a54 bytes 0f290194
+ 00b96a98 bytes 12290194
- 00b96a7c ["INT_ADD", "register:40f0:8", ["const:b96a7c:8", "const:4:8"]]
- 00b96a7c ["CALL", null, ["callee:00bdb440:8"]]
+ 00b96ac0 ["INT_ADD", "register:40f0:8", ["const:b96ac0:8", "const:4:8"]]
+ 00b96ac0 ["CALL", null, ["callee:00bdb440:8"]]
- 00b96a7c bytes 5d120194
+ 00b96ac0 bytes 60120194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584bd01a420de5025e4e650ef073d770"></a>

### [`00b96b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md) → [`00b96ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) [`00b979f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b979f8.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.76% / 新版 99.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b96bfc",
      "incomplete_value": true,
      "site": "00b96bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96bb8",
      "incomplete_value": true,
      "site": "00b96bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b96c04",
      "incomplete_value": true,
      "site": "00b96c08",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b96bc0",
      "incomplete_value": true,
      "site": "00b96bc4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b96c28",
      "incomplete_value": true,
      "site": "00b96c30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b96be4",
      "incomplete_value": true,
      "site": "00b96bec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b96bf4",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b96bfc",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96c00",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b96bf4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b96bfc",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b96c00",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md#insn-00b96ba8) · [`00b96bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md#insn-00b96bec) · [`00b96c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96b60.md#insn-00b96c14)
- 新版 `00b96bec`（命令位置の公開資料なし） · `00b96c30`（命令位置の公開資料なし） · `00b96c58`（命令位置の公開資料なし）

~~~diff
- 00b96ba8 ["INT_ADD", "register:40f0:8", ["const:b96ba8:8", "const:4:8"]]
- 00b96ba8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b96bec ["INT_ADD", "register:40f0:8", ["const:b96bec:8", "const:4:8"]]
+ 00b96bec ["CALL", null, ["callee:00bdb420:8"]]
- 00b96ba8 bytes 0a120194
+ 00b96bec bytes 0d120194
- 00b96bec ["INT_ADD", "register:40f0:8", ["const:b96bec:8", "const:4:8"]]
- 00b96bec ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b96c30 ["INT_ADD", "register:40f0:8", ["const:b96c30:8", "const:4:8"]]
+ 00b96c30 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b96bec bytes a9280194
+ 00b96c30 bytes ac280194
- 00b96c14 ["INT_ADD", "register:40f0:8", ["const:b96c14:8", "const:4:8"]]
- 00b96c14 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b96c58 ["INT_ADD", "register:40f0:8", ["const:b96c58:8", "const:4:8"]]
+ 00b96c58 ["CALL", null, ["callee:00bdb440:8"]]
- 00b96c14 bytes f7110194
+ 00b96c58 bytes fa110194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06727054a906af891ec4c22cb76644c"></a>

### [`00b97d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97d3c.md) → [`00b97d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97d80.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKwSC_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be15f0.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.68% / 新版 99.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b97dd4",
      "incomplete_value": true,
      "site": "00b97ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97d90",
      "incomplete_value": true,
      "site": "00b97d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b97de4",
      "incomplete_value": true,
      "site": "00b97de8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b97da0",
      "incomplete_value": true,
      "site": "00b97da4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97e08",
      "incomplete_value": true,
      "site": "00b97e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97dc4",
      "incomplete_value": true,
      "site": "00b97dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b97dd4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b97ddc",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b97de0",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b97dd4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b97ddc",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b97de0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97d3c.md#insn-00b97d88) · [`00b97dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97d3c.md#insn-00b97dcc) · [`00b97df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b97/00b97d3c.md#insn-00b97df4)
- 新版 `00b97dcc`（命令位置の公開資料なし） · `00b97e10`（命令位置の公開資料なし） · `00b97e38`（命令位置の公開資料なし）

~~~diff
- 00b97d88 ["INT_ADD", "register:40f0:8", ["const:b97d88:8", "const:4:8"]]
- 00b97d88 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b97dcc ["INT_ADD", "register:40f0:8", ["const:b97dcc:8", "const:4:8"]]
+ 00b97dcc ["CALL", null, ["callee:00bdb420:8"]]
- 00b97d88 bytes 920d0194
+ 00b97dcc bytes 950d0194
- 00b97dcc ["INT_ADD", "register:40f0:8", ["const:b97dcc:8", "const:4:8"]]
- 00b97dcc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b97e10 ["INT_ADD", "register:40f0:8", ["const:b97e10:8", "const:4:8"]]
+ 00b97e10 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b97dcc bytes 31240194
+ 00b97e10 bytes 34240194
- 00b97df4 ["INT_ADD", "register:40f0:8", ["const:b97df4:8", "const:4:8"]]
- 00b97df4 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b97e38 ["INT_ADD", "register:40f0:8", ["const:b97e38:8", "const:4:8"]]
+ 00b97e38 ["CALL", null, ["callee:00bdb440:8"]]
- 00b97df4 bytes 7f0d0194
+ 00b97e38 bytes 820d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353a2614eb202911ce6cb7acf20edfac"></a>

### [`00b9830c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9830c.md) → [`00b98350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98390",
      "incomplete_value": true,
      "site": "00b98398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9834c",
      "incomplete_value": true,
      "site": "00b98354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b983a0",
      "incomplete_value": true,
      "site": "00b983a4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9835c",
      "incomplete_value": true,
      "site": "00b98360",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b983c0",
      "incomplete_value": true,
      "site": "00b983c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9837c",
      "incomplete_value": true,
      "site": "00b98384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b98390",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98398",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b9839c",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b98390",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b98398",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b9839c",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9830c.md#insn-00b98384) · [`00b98344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9830c.md#insn-00b98344) · [`00b9834c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b9830c.md#insn-00b9834c)
- 新版 `00b983c8`（命令位置の公開資料なし） · `00b98388`（命令位置の公開資料なし） · `00b98390`（命令位置の公開資料なし）

~~~diff
- 00b98384 ["INT_ADD", "register:40f0:8", ["const:b98384:8", "const:4:8"]]
- 00b98384 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b983c8 ["INT_ADD", "register:40f0:8", ["const:b983c8:8", "const:4:8"]]
+ 00b983c8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b98384 bytes c3220194
+ 00b983c8 bytes c6220194
- 00b98344 ["INT_ADD", "register:40f0:8", ["const:b98344:8", "const:4:8"]]
- 00b98344 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b98388 ["INT_ADD", "register:40f0:8", ["const:b98388:8", "const:4:8"]]
+ 00b98388 ["CALL", null, ["callee:00bdb420:8"]]
- 00b98344 bytes 230c0194
+ 00b98388 bytes 260c0194
- 00b9834c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:cc0:8"]]
- 00b9834c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b98390 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d10:8"]]
+ 00b98390 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9834c bytes 186346f9
+ 00b98390 bytes 188b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b19a9035036f95acc0332c935bf5028"></a>

### [`00b98520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98520.md) → [`00b98564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b985a4",
      "incomplete_value": true,
      "site": "00b985ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98560",
      "incomplete_value": true,
      "site": "00b98568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b985b4",
      "incomplete_value": true,
      "site": "00b985b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b98570",
      "incomplete_value": true,
      "site": "00b98574",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b985d4",
      "incomplete_value": true,
      "site": "00b985dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98590",
      "incomplete_value": true,
      "site": "00b98598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b985a4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b985ac",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b985b0",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b985a4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b985ac",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b985b0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98520.md#insn-00b98598) · [`00b98558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98520.md#insn-00b98558) · [`00b98560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98520.md#insn-00b98560)
- 新版 `00b985dc`（命令位置の公開資料なし） · `00b9859c`（命令位置の公開資料なし） · `00b985a4`（命令位置の公開資料なし）

~~~diff
- 00b98598 ["INT_ADD", "register:40f0:8", ["const:b98598:8", "const:4:8"]]
- 00b98598 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b985dc ["INT_ADD", "register:40f0:8", ["const:b985dc:8", "const:4:8"]]
+ 00b985dc ["CALL", null, ["callee:00be0ee0:8"]]
- 00b98598 bytes 3e220194
+ 00b985dc bytes 41220194
- 00b98558 ["INT_ADD", "register:40f0:8", ["const:b98558:8", "const:4:8"]]
- 00b98558 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9859c ["INT_ADD", "register:40f0:8", ["const:b9859c:8", "const:4:8"]]
+ 00b9859c ["CALL", null, ["callee:00bdb420:8"]]
- 00b98558 bytes 9e0b0194
+ 00b9859c bytes a10b0194
- 00b98560 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:cc0:8"]]
- 00b98560 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b985a4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d10:8"]]
+ 00b985a4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98560 bytes 186346f9
+ 00b985a4 bytes 188b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac77371d75e0fd50467463118d8f65c"></a>

### [`00b98724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md) → [`00b98768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b987a4",
      "incomplete_value": true,
      "site": "00b987ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98760",
      "incomplete_value": true,
      "site": "00b98768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b987b4",
      "incomplete_value": true,
      "site": "00b987b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b98770",
      "incomplete_value": true,
      "site": "00b98774",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b987d8",
      "incomplete_value": true,
      "site": "00b987e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98794",
      "incomplete_value": true,
      "site": "00b9879c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b987a4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b987ac",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b987b0",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b987a4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b987ac",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b987b0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md#insn-00b98758) · [`00b9879c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md#insn-00b9879c) · [`00b987c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b98724.md#insn-00b987c4)
- 新版 `00b9879c`（命令位置の公開資料なし） · `00b987e0`（命令位置の公開資料なし） · `00b98808`（命令位置の公開資料なし）

~~~diff
- 00b98758 ["INT_ADD", "register:40f0:8", ["const:b98758:8", "const:4:8"]]
- 00b98758 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9879c ["INT_ADD", "register:40f0:8", ["const:b9879c:8", "const:4:8"]]
+ 00b9879c ["CALL", null, ["callee:00bdb420:8"]]
- 00b98758 bytes 1e0b0194
+ 00b9879c bytes 210b0194
- 00b9879c ["INT_ADD", "register:40f0:8", ["const:b9879c:8", "const:4:8"]]
- 00b9879c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b987e0 ["INT_ADD", "register:40f0:8", ["const:b987e0:8", "const:4:8"]]
+ 00b987e0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9879c bytes bd210194
+ 00b987e0 bytes c0210194
- 00b987c4 ["INT_ADD", "register:40f0:8", ["const:b987c4:8", "const:4:8"]]
- 00b987c4 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b98808 ["INT_ADD", "register:40f0:8", ["const:b98808:8", "const:4:8"]]
+ 00b98808 ["CALL", null, ["callee:00bdb440:8"]]
- 00b987c4 bytes 0b0b0194
+ 00b98808 bytes 0e0b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2525d38ca0d05518c7dd5a0e02184906"></a>

### [`00b988a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md) → [`00b988ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b8e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e13c.md) [`00b9973c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b9973c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.75% / 新版 99.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b98944",
      "incomplete_value": true,
      "site": "00b98944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98900",
      "incomplete_value": true,
      "site": "00b98900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9894c",
      "incomplete_value": true,
      "site": "00b98950",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b98908",
      "incomplete_value": true,
      "site": "00b9890c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98970",
      "incomplete_value": true,
      "site": "00b98978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9892c",
      "incomplete_value": true,
      "site": "00b98934",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b9893c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b98944",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b98948",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b9893c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b98944",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b98948",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b988f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md#insn-00b988f0) · [`00b98934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md#insn-00b98934) · [`00b9895c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b98/00b988a8.md#insn-00b9895c)
- 新版 `00b98934`（命令位置の公開資料なし） · `00b98978`（命令位置の公開資料なし） · `00b989a0`（命令位置の公開資料なし）

~~~diff
- 00b988f0 ["INT_ADD", "register:40f0:8", ["const:b988f0:8", "const:4:8"]]
- 00b988f0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b98934 ["INT_ADD", "register:40f0:8", ["const:b98934:8", "const:4:8"]]
+ 00b98934 ["CALL", null, ["callee:00bdb420:8"]]
- 00b988f0 bytes b80a0194
+ 00b98934 bytes bb0a0194
- 00b98934 ["INT_ADD", "register:40f0:8", ["const:b98934:8", "const:4:8"]]
- 00b98934 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b98978 ["INT_ADD", "register:40f0:8", ["const:b98978:8", "const:4:8"]]
+ 00b98978 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b98934 bytes 57210194
+ 00b98978 bytes 5a210194
- 00b9895c ["INT_ADD", "register:40f0:8", ["const:b9895c:8", "const:4:8"]]
- 00b9895c ["CALL", null, ["callee:00bdb440:8"]]
+ 00b989a0 ["INT_ADD", "register:40f0:8", ["const:b989a0:8", "const:4:8"]]
+ 00b989a0 ["CALL", null, ["callee:00bdb440:8"]]
- 00b9895c bytes a50a0194
+ 00b989a0 bytes a80a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a3fb941b99d41934142db13a2aa318"></a>

### [`00b99a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99a98.md) → [`00b99adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99adc.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE3putES4_RNS_8ios_baseEcPK2tmPKcSC_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8e0.md) · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 1件 [`00bdd930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd930.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.39% / 新版 99.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99b2c",
      "incomplete_value": true,
      "site": "00b99b34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b99ae8",
      "incomplete_value": true,
      "site": "00b99af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b99b3c",
      "incomplete_value": true,
      "site": "00b99b40",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b99af8",
      "incomplete_value": true,
      "site": "00b99afc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99b5c",
      "incomplete_value": true,
      "site": "00b99b64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b99b18",
      "incomplete_value": true,
      "site": "00b99b20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b99b2c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b99b34",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b99b38",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b99b2c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b99b34",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b99b38",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99a98.md#insn-00b99b20) · [`00b99ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99a98.md#insn-00b99ae0) · [`00b99ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99a98.md#insn-00b99ae8)
- 新版 `00b99b64`（命令位置の公開資料なし） · `00b99b24`（命令位置の公開資料なし） · `00b99b2c`（命令位置の公開資料なし）

~~~diff
- 00b99b20 ["INT_ADD", "register:40f0:8", ["const:b99b20:8", "const:4:8"]]
- 00b99b20 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b99b64 ["INT_ADD", "register:40f0:8", ["const:b99b64:8", "const:4:8"]]
+ 00b99b64 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b99b20 bytes dc1c0194
+ 00b99b64 bytes df1c0194
- 00b99ae0 ["INT_ADD", "register:40f0:8", ["const:b99ae0:8", "const:4:8"]]
- 00b99ae0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b99b24 ["INT_ADD", "register:40f0:8", ["const:b99b24:8", "const:4:8"]]
+ 00b99b24 ["CALL", null, ["callee:00bdb420:8"]]
- 00b99ae0 bytes 3c060194
+ 00b99b24 bytes 3f060194
- 00b99ae8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:df0:8"]]
- 00b99ae8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99b2c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e40:8"]]
+ 00b99b2c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b99ae8 bytes 7bfb46f9
+ 00b99b2c bytes 7b2347f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5311c22094da7d558d282028f26ff825"></a>

### [`00b99e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e78.md) → [`00b99ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99ebc.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE3putES4_RNS_8ios_baseEwPK2tmPKwSC_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99f0c",
      "incomplete_value": true,
      "site": "00b99f14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b99ec8",
      "incomplete_value": true,
      "site": "00b99ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b99f1c",
      "incomplete_value": true,
      "site": "00b99f20",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b99ed8",
      "incomplete_value": true,
      "site": "00b99edc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99f3c",
      "incomplete_value": true,
      "site": "00b99f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b99ef8",
      "incomplete_value": true,
      "site": "00b99f00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00b99f0c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f14",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b99f18",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b99f0c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f14",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00b99f18",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e78.md#insn-00b99f00) · [`00b99ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e78.md#insn-00b99ec0) · [`00b99ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b99/00b99e78.md#insn-00b99ec8)
- 新版 `00b99f44`（命令位置の公開資料なし） · `00b99f04`（命令位置の公開資料なし） · `00b99f0c`（命令位置の公開資料なし）

~~~diff
- 00b99f00 ["INT_ADD", "register:40f0:8", ["const:b99f00:8", "const:4:8"]]
- 00b99f00 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b99f44 ["INT_ADD", "register:40f0:8", ["const:b99f44:8", "const:4:8"]]
+ 00b99f44 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b99f00 bytes e41b0194
+ 00b99f44 bytes e71b0194
- 00b99ec0 ["INT_ADD", "register:40f0:8", ["const:b99ec0:8", "const:4:8"]]
- 00b99ec0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b99f04 ["INT_ADD", "register:40f0:8", ["const:b99f04:8", "const:4:8"]]
+ 00b99f04 ["CALL", null, ["callee:00bdb420:8"]]
- 00b99ec0 bytes 44050194
+ 00b99f04 bytes 47050194
- 00b99ec8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:cc0:8"]]
- 00b99ec8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99f0c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d10:8"]]
+ 00b99f0c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b99ec8 bytes 7b6346f9
+ 00b99f0c bytes 7b8b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fff5c329319ceb31babcbfa726483720"></a>

### [`00b9a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a8fc.md) → [`00b9a940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9a988",
      "incomplete_value": true,
      "site": "00b9a988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9a944",
      "incomplete_value": true,
      "site": "00b9a944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9a99c",
      "incomplete_value": true,
      "site": "00b9a9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9a958",
      "incomplete_value": true,
      "site": "00b9a960",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9a9ac",
      "incomplete_value": true,
      "site": "00b9a9b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9a968",
      "incomplete_value": true,
      "site": "00b9a96c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9a970",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9a988",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9a99c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9a970",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9a988",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9a99c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a8fc.md#insn-00b9a950) · [`00b9a988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a8fc.md#insn-00b9a988) · [`00b9a994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9a8fc.md#insn-00b9a994)
- 新版 `00b9a994`（命令位置の公開資料なし） · `00b9a9cc`（命令位置の公開資料なし） · `00b9a9d8`（命令位置の公開資料なし）

~~~diff
- 00b9a950 ["INT_ADD", "register:40f0:8", ["const:b9a950:8", "const:4:8"]]
- 00b9a950 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9a994 ["INT_ADD", "register:40f0:8", ["const:b9a994:8", "const:4:8"]]
+ 00b9a994 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9a950 bytes a0020194
+ 00b9a994 bytes a3020194
- 00b9a988 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00b9a9cc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00b9a988 bytes e23b0f10
+ 00b9a9cc bytes e23b0f10
- 00b9a994 ["INT_ADD", "register:40f0:8", ["const:b9a994:8", "const:4:8"]]
- 00b9a994 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9a9d8 ["INT_ADD", "register:40f0:8", ["const:b9a9d8:8", "const:4:8"]]
+ 00b9a9d8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9a994 bytes 3f190194
+ 00b9a9d8 bytes 42190194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4038cd9201730b3312993ff6464f4a08"></a>

### [`00b9ac48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac48.md) → [`00b9ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md) _ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIcEERNS_10unique_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1650.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md)
- 新版 呼出元 1件 [`00be16a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16a0.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9adf8",
      "incomplete_value": true,
      "site": "00b9ae00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9adb4",
      "incomplete_value": true,
      "site": "00b9adbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9b0d4",
      "incomplete_value": true,
      "site": "00b9b0d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9b090",
      "incomplete_value": true,
      "site": "00b9b094",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9b10c",
      "incomplete_value": true,
      "site": "00b9b110",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9b0c8",
      "incomplete_value": true,
      "site": "00b9b0cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b9adf8",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9ae00",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9b01c",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9adf8",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9ae00",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9b01c",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9b090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac48.md#insn-00b9b090) · [`00b9b110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac48.md#insn-00b9b110) · [`00b9acbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac48.md#insn-00b9acbc)
- 新版 `00b9b0d4`（命令位置の公開資料なし） · `00b9b154`（命令位置の公開資料なし） · `00b9ad00`（命令位置の公開資料なし）

~~~diff
- 00b9b090 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
- 00b9b090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9b0d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 00b9b0d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9b090 bytes 087547f9
+ 00b9b0d4 bytes 089d47f9
- 00b9b110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9b110 ["INT_ADD", "register:40f0:8", ["const:b9b110:8", "const:4:8"]]
- 00b9b110 ["CALLIND", null, ["register:0:8"]]
+ 00b9b154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9b154 ["INT_ADD", "register:40f0:8", ["const:b9b154:8", "const:4:8"]]
+ 00b9b154 ["CALLIND", null, ["register:0:8"]]
- 00b9b110 bytes 00013fd6
+ 00b9b154 bytes 00013fd6
- 00b9acbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9acbc ["INT_ADD", "register:40f0:8", ["const:b9acbc:8", "const:4:8"]]
- 00b9acbc ["CALLIND", null, ["register:0:8"]]
+ 00b9ad00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9ad00 ["INT_ADD", "register:40f0:8", ["const:b9ad00:8", "const:4:8"]]
+ 00b9ad00 ["CALLIND", null, ["register:0:8"]]
- 00b9acbc bytes 00013fd6
+ 00b9ad00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4a12f2221ad5196d4a98423ff12913"></a>

### [`00b9be50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md) → [`00b9be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIcS3_NS_9allocato

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00b9c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c110.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00b9c154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9bedc",
      "incomplete_value": true,
      "site": "00b9bedc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9be98",
      "incomplete_value": true,
      "site": "00b9be98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9bef8",
      "incomplete_value": true,
      "site": "00b9bef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9beb4",
      "incomplete_value": true,
      "site": "00b9beb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9bf00",
      "incomplete_value": true,
      "site": "00b9bf04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9bebc",
      "incomplete_value": true,
      "site": "00b9bec0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9bec4",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9bedc",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9bef0",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9bec4",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9bedc",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9bef0",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9bea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md#insn-00b9bea4) · [`00b9bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md#insn-00b9bedc) · [`00b9bee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9b/00b9be50.md#insn-00b9bee8)
- 新版 `00b9bee8`（命令位置の公開資料なし） · `00b9bf20`（命令位置の公開資料なし） · `00b9bf2c`（命令位置の公開資料なし）

~~~diff
- 00b9bea4 ["INT_ADD", "register:40f0:8", ["const:b9bea4:8", "const:4:8"]]
- 00b9bea4 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9bee8 ["INT_ADD", "register:40f0:8", ["const:b9bee8:8", "const:4:8"]]
+ 00b9bee8 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9bea4 bytes 4bfd0094
+ 00b9bee8 bytes 4efd0094
- 00b9bedc ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00b9bf20 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00b9bedc bytes 42910e10
+ 00b9bf20 bytes 42910e10
- 00b9bee8 ["INT_ADD", "register:40f0:8", ["const:b9bee8:8", "const:4:8"]]
- 00b9bee8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9bf2c ["INT_ADD", "register:40f0:8", ["const:b9bf2c:8", "const:4:8"]]
+ 00b9bf2c ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9bee8 bytes ea130194
+ 00b9bf2c bytes ed130194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27968f268d0f930c6c72005b2f4ab49b"></a>

### [`00b9c798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c798.md) → [`00b9c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9c824",
      "incomplete_value": true,
      "site": "00b9c824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9c7e0",
      "incomplete_value": true,
      "site": "00b9c7e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9c838",
      "incomplete_value": true,
      "site": "00b9c840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9c7f4",
      "incomplete_value": true,
      "site": "00b9c7fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9c848",
      "incomplete_value": true,
      "site": "00b9c84c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9c804",
      "incomplete_value": true,
      "site": "00b9c808",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9c80c",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9c824",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9c838",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9c80c",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9c824",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9c838",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c798.md#insn-00b9c7ec) · [`00b9c824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c798.md#insn-00b9c824) · [`00b9c830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9c798.md#insn-00b9c830)
- 新版 `00b9c830`（命令位置の公開資料なし） · `00b9c868`（命令位置の公開資料なし） · `00b9c874`（命令位置の公開資料なし）

~~~diff
- 00b9c7ec ["INT_ADD", "register:40f0:8", ["const:b9c7ec:8", "const:4:8"]]
- 00b9c7ec ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9c830 ["INT_ADD", "register:40f0:8", ["const:b9c830:8", "const:4:8"]]
+ 00b9c830 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9c7ec bytes f9fa0094
+ 00b9c830 bytes fcfa0094
- 00b9c824 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00b9c868 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00b9c824 bytes 02470e10
+ 00b9c868 bytes 02470e10
- 00b9c830 ["INT_ADD", "register:40f0:8", ["const:b9c830:8", "const:4:8"]]
- 00b9c830 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9c874 ["INT_ADD", "register:40f0:8", ["const:b9c874:8", "const:4:8"]]
+ 00b9c874 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9c830 bytes 98110194
+ 00b9c874 bytes 9b110194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5884ecb803d387be10e2591eed35a5a"></a>

### [`00b9cae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9cae0.md) → [`00b9cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md) _ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIwEERNS_10unique_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1680.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00be16d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16d0.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9ccb4",
      "incomplete_value": true,
      "site": "00b9ccbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9cc70",
      "incomplete_value": true,
      "site": "00b9cc78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9cf78",
      "incomplete_value": true,
      "site": "00b9cf80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9cf34",
      "incomplete_value": true,
      "site": "00b9cf3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9cfcc",
      "incomplete_value": true,
      "site": "00b9cfd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9cf88",
      "incomplete_value": true,
      "site": "00b9cf8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b9ccb4",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9ccbc",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9cec0",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9ccb4",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9ccbc",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9cec0",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9cef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9cae0.md#insn-00b9cef8) · [`00b9d0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9cae0.md#insn-00b9d0f4) · [`00b9cb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9c/00b9cae0.md#insn-00b9cb68)
- 新版 `00b9cf3c`（命令位置の公開資料なし） · `00b9d138`（命令位置の公開資料なし） · `00b9cbac`（命令位置の公開資料なし）

~~~diff
- 00b9cef8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d50:8"]]
- 00b9cef8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9cf3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:da0:8"]]
+ 00b9cf3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9cef8 bytes 29a946f9
+ 00b9cf3c bytes 29d146f9
- 00b9d0f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9d0f4 ["INT_ADD", "register:40f0:8", ["const:b9d0f4:8", "const:4:8"]]
- 00b9d0f4 ["CALLIND", null, ["register:0:8"]]
+ 00b9d138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9d138 ["INT_ADD", "register:40f0:8", ["const:b9d138:8", "const:4:8"]]
+ 00b9d138 ["CALLIND", null, ["register:0:8"]]
- 00b9d0f4 bytes 00013fd6
+ 00b9d138 bytes 00013fd6
- 00b9cb68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9cb68 ["INT_ADD", "register:40f0:8", ["const:b9cb68:8", "const:4:8"]]
- 00b9cb68 ["CALLIND", null, ["register:0:8"]]
+ 00b9cbac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b9cbac ["INT_ADD", "register:40f0:8", ["const:b9cbac:8", "const:4:8"]]
+ 00b9cbac ["CALLIND", null, ["register:0:8"]]
- 00b9cb68 bytes 00013fd6
+ 00b9cbac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b027408537a2f1a89bb71ad9507efb"></a>

### [`00b9de0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md) → [`00b9de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIwS3_NS_9allocato

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9a/00b9ac40.md) [`00b9e138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e138.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00b9e17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9de98",
      "incomplete_value": true,
      "site": "00b9de98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9de54",
      "incomplete_value": true,
      "site": "00b9de54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9deb4",
      "incomplete_value": true,
      "site": "00b9deb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9de70",
      "incomplete_value": true,
      "site": "00b9de70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9debc",
      "incomplete_value": true,
      "site": "00b9dec0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9de78",
      "incomplete_value": true,
      "site": "00b9de7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9de80",
      "READ",
      [
        "storage",
        "00c1bd50",
        null,
        "pointer"
      ]
    ],
    [
      "00b9de98",
      "DATA",
      [
        "storage",
        "00b9ac40",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9deac",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b9de80",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9de98",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00b9deac",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9de60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md#insn-00b9de60) · [`00b9de98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md#insn-00b9de98) · [`00b9dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9d/00b9de0c.md#insn-00b9dea4)
- 新版 `00b9dea4`（命令位置の公開資料なし） · `00b9dedc`（命令位置の公開資料なし） · `00b9dee8`（命令位置の公開資料なし）

~~~diff
- 00b9de60 ["INT_ADD", "register:40f0:8", ["const:b9de60:8", "const:4:8"]]
- 00b9de60 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9dea4 ["INT_ADD", "register:40f0:8", ["const:b9dea4:8", "const:4:8"]]
+ 00b9dea4 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9de60 bytes 5cf50094
+ 00b9dea4 bytes 5ff50094
- 00b9de98 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00b9dedc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00b9de98 bytes 62930d10
+ 00b9dedc bytes 62930d10
- 00b9dea4 ["INT_ADD", "register:40f0:8", ["const:b9dea4:8", "const:4:8"]]
- 00b9dea4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9dee8 ["INT_ADD", "register:40f0:8", ["const:b9dee8:8", "const:4:8"]]
+ 00b9dee8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9dea4 bytes fb0b0194
+ 00b9dee8 bytes fe0b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce102af4f71eb1d6e4c2932c43250b2"></a>

### [`00b9e680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md) → [`00b9e6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEce

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9e79c",
      "incomplete_value": true,
      "site": "00b9e7a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9e758",
      "incomplete_value": true,
      "site": "00b9e760",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b9ea64",
      "incomplete_value": true,
      "site": "00b9ea64",
      "value": [
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
    "old": {
      "definition_site": "00b9ea20",
      "incomplete_value": true,
      "site": "00b9ea20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9e7ac",
      "incomplete_value": true,
      "site": "00b9e7b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9e768",
      "incomplete_value": true,
      "site": "00b9e76c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9e6f8",
      "PARAM",
      [
        "storage",
        "002a1099",
        null,
        "string"
      ]
    ],
    [
      "00b9e72c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9e734",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b9e6f8",
      "PARAM",
      [
        "storage",
        "002a1124",
        null,
        "string"
      ]
    ],
    [
      "00b9e72c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9e734",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9e6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md#insn-00b9e6d0) · [`00b9e708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md#insn-00b9e708) · [`00b9e750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9e680.md#insn-00b9e750)
- 新版 `00b9e714`（命令位置の公開資料なし） · `00b9e74c`（命令位置の公開資料なし） · `00b9e794`（命令位置の公開資料なし）

~~~diff
- 00b9e6d0 ["INT_ADD", "register:40f0:8", ["const:b9e6d0:8", "const:4:8"]]
- 00b9e6d0 ["CALL", null, ["callee:00be1100:8"]]
+ 00b9e714 ["INT_ADD", "register:40f0:8", ["const:b9e714:8", "const:4:8"]]
+ 00b9e714 ["CALL", null, ["callee:00be1100:8"]]
- 00b9e6d0 bytes 780a0194
+ 00b9e714 bytes 7b0a0194
- 00b9e708 ["INT_ADD", "register:40f0:8", ["const:b9e708:8", "const:4:8"]]
- 00b9e708 ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b9e74c ["INT_ADD", "register:40f0:8", ["const:b9e74c:8", "const:4:8"]]
+ 00b9e74c ["CALL", null, ["callee:00b9eb70:8"]]
- 00b9e708 bytes 09010094
+ 00b9e74c bytes 09010094
- 00b9e750 ["INT_ADD", "register:40f0:8", ["const:b9e750:8", "const:4:8"]]
- 00b9e750 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9e794 ["INT_ADD", "register:40f0:8", ["const:b9e794:8", "const:4:8"]]
+ 00b9e794 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9e750 bytes 20f30094
+ 00b9e794 bytes 23f30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593968f2eae8474b51a7546606ec206f"></a>

### [`00b9f278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f278.md) → [`00b9f2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f2bc.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEcRKNS_12basic_stringIcS3_NS_9allocatorIc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.47% / 新版 99.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9f30c",
      "incomplete_value": true,
      "site": "00b9f30c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9f2c8",
      "incomplete_value": true,
      "site": "00b9f2c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9f314",
      "incomplete_value": true,
      "site": "00b9f318",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9f2d0",
      "incomplete_value": true,
      "site": "00b9f2d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9f338",
      "incomplete_value": true,
      "site": "00b9f340",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00b9f2f4",
      "incomplete_value": true,
      "site": "00b9f2fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
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
      "00b9f304",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b9f30c",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b9f310",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b9f304",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b9f30c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00b9f310",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9f2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f278.md#insn-00b9f2b8) · [`00b9f2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f278.md#insn-00b9f2fc) · [`00b9f2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f278.md#insn-00b9f2c0)
- 新版 `00b9f2fc`（命令位置の公開資料なし） · `00b9f340`（命令位置の公開資料なし） · `00b9f304`（命令位置の公開資料なし）

~~~diff
- 00b9f2b8 ["INT_ADD", "register:40f0:8", ["const:b9f2b8:8", "const:4:8"]]
- 00b9f2b8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9f2fc ["INT_ADD", "register:40f0:8", ["const:b9f2fc:8", "const:4:8"]]
+ 00b9f2fc ["CALL", null, ["callee:00bdb420:8"]]
- 00b9f2b8 bytes 46f00094
+ 00b9f2fc bytes 49f00094
- 00b9f2fc ["INT_ADD", "register:40f0:8", ["const:b9f2fc:8", "const:4:8"]]
- 00b9f2fc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b9f340 ["INT_ADD", "register:40f0:8", ["const:b9f340:8", "const:4:8"]]
+ 00b9f340 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b9f2fc bytes e5060194
+ 00b9f340 bytes e8060194
- 00b9f2c0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:df0:8"]]
- 00b9f2c0 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b9f304 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e40:8"]]
+ 00b9f304 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9f2c0 bytes f7fa46f9
+ 00b9f304 bytes f72247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b13de8b458e8c39cea1bfb2ab0ac1e0c"></a>

### [`00b9f5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f5fc.md) → [`00b9f640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f640.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00b9eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9e/00b9eb2c.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9f718",
      "incomplete_value": true,
      "site": "00b9f720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9f6d4",
      "incomplete_value": true,
      "site": "00b9f6dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b9f9ec",
      "incomplete_value": true,
      "site": "00b9f9ec",
      "value": [
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
    "old": {
      "definition_site": "00b9f9a8",
      "incomplete_value": true,
      "site": "00b9f9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b9f728",
      "incomplete_value": true,
      "site": "00b9f72c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9f6e4",
      "incomplete_value": true,
      "site": "00b9f6e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "00b9f674",
      "PARAM",
      [
        "storage",
        "002a1099",
        null,
        "string"
      ]
    ],
    [
      "00b9f6a8",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9f6b0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b9f674",
      "PARAM",
      [
        "storage",
        "002a1124",
        null,
        "string"
      ]
    ],
    [
      "00b9f6a8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b9f6b0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f5fc.md#insn-00b9f64c) · [`00b9f684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f5fc.md#insn-00b9f684) · [`00b9f6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b9f/00b9f5fc.md#insn-00b9f6cc)
- 新版 `00b9f690`（命令位置の公開資料なし） · `00b9f6c8`（命令位置の公開資料なし） · `00b9f710`（命令位置の公開資料なし）

~~~diff
- 00b9f64c ["INT_ADD", "register:40f0:8", ["const:b9f64c:8", "const:4:8"]]
- 00b9f64c ["CALL", null, ["callee:00be1100:8"]]
+ 00b9f690 ["INT_ADD", "register:40f0:8", ["const:b9f690:8", "const:4:8"]]
+ 00b9f690 ["CALL", null, ["callee:00be1100:8"]]
- 00b9f64c bytes 99060194
+ 00b9f690 bytes 9c060194
- 00b9f684 ["INT_ADD", "register:40f0:8", ["const:b9f684:8", "const:4:8"]]
- 00b9f684 ["CALL", null, ["callee:00b9eb70:8"]]
+ 00b9f6c8 ["INT_ADD", "register:40f0:8", ["const:b9f6c8:8", "const:4:8"]]
+ 00b9f6c8 ["CALL", null, ["callee:00b9eb70:8"]]
- 00b9f684 bytes 2afdff97
+ 00b9f6c8 bytes 2afdff97
- 00b9f6cc ["INT_ADD", "register:40f0:8", ["const:b9f6cc:8", "const:4:8"]]
- 00b9f6cc ["CALL", null, ["callee:00bdb420:8"]]
+ 00b9f710 ["INT_ADD", "register:40f0:8", ["const:b9f710:8", "const:4:8"]]
+ 00b9f710 ["CALL", null, ["callee:00bdb420:8"]]
- 00b9f6cc bytes 41ef0094
+ 00b9f710 bytes 44ef0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bda45561aa79ae4f59cf552bd0683a61"></a>

### [`00ba0160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0160.md) → [`00ba01a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00b94a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b94/00b94a30.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba01f4",
      "incomplete_value": true,
      "site": "00ba01f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba01b0",
      "incomplete_value": true,
      "site": "00ba01b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba01fc",
      "incomplete_value": true,
      "site": "00ba0200",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba01b8",
      "incomplete_value": true,
      "site": "00ba01bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba0220",
      "incomplete_value": true,
      "site": "00ba0228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba01dc",
      "incomplete_value": true,
      "site": "00ba01e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
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
      "00ba01ec",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba01f4",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba01f8",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba01ec",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00ba01f4",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba01f8",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0160.md#insn-00ba01a0) · [`00ba01e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0160.md#insn-00ba01e4) · [`00ba01a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba0160.md#insn-00ba01a8)
- 新版 `00ba01e4`（命令位置の公開資料なし） · `00ba0228`（命令位置の公開資料なし） · `00ba01ec`（命令位置の公開資料なし）

~~~diff
- 00ba01a0 ["INT_ADD", "register:40f0:8", ["const:ba01a0:8", "const:4:8"]]
- 00ba01a0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00ba01e4 ["INT_ADD", "register:40f0:8", ["const:ba01e4:8", "const:4:8"]]
+ 00ba01e4 ["CALL", null, ["callee:00bdb420:8"]]
- 00ba01a0 bytes 8cec0094
+ 00ba01e4 bytes 8fec0094
- 00ba01e4 ["INT_ADD", "register:40f0:8", ["const:ba01e4:8", "const:4:8"]]
- 00ba01e4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba0228 ["INT_ADD", "register:40f0:8", ["const:ba0228:8", "const:4:8"]]
+ 00ba0228 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba01e4 bytes 2b030194
+ 00ba0228 bytes 2e030194
- 00ba01a8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:cc0:8"]]
- 00ba01a8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba01ec ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d10:8"]]
+ 00ba01ec ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba01a8 bytes f76246f9
+ 00ba01ec bytes f78a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6475d14dfeac148a2858a9534e2916c5"></a>

### [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) → [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) FUN_00ba082c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba2c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md) · 呼出先 12件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba2cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md) · 呼出先 12件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 24.28% / 新版 24.28%

CFGの説明率　旧版 3.67% / 新版 3.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 19件, `store_condition` 4件, `store_destination` 8件, `store_value` 5件, `unresolved_branch_alignment` 159件, `unresolved_call_alignment` 115件, `unresolved_store_alignment` 178件

アドレスに依存する影響 `call_argument_candidate` 16件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0898"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba0824",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba0894",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba089c",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ba0868",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba08d8",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba08e0",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba0824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md#insn-00ba0824) · [`00ba0898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md#insn-00ba0898) · [`00ba08a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md#insn-00ba08a4)

~~~diff
- 00ba0824 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba0824 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba0824 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba0824 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba0824 bytes 092000a9
- 00ba0898 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ba0898 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba0898 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00ba0898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba0898 bytes 19a001a9
- 00ba08a4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00ba08a4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba08a4 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00ba08a4 ["COPY", "tmp:3:8", ["register:40b0:8"]]
- 00ba08a4 bytes c87e00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3dc98e058ca5e81ceff3a9386109761"></a>

### [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) → [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) FUN_00ba261c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba8048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md) [`00ba8180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md)
- 新版 呼出元 2件 [`00ba808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba808c.md) [`00ba81c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba264c",
      "incomplete_value": false,
      "site": "00ba264c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2608",
      "incomplete_value": false,
      "site": "00ba2608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00ba27f8",
      "incomplete_value": true,
      "site": "00ba27f8",
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
      "definition_site": "00ba27b4",
      "incomplete_value": true,
      "site": "00ba27b4",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2834",
      "incomplete_value": true,
      "site": "00ba2838",
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
      "definition_site": "00ba27f0",
      "incomplete_value": true,
      "site": "00ba27f4",
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
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba264c",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba26dc",
      "READ",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba26e4",
      "READ",
      [
        "storage",
        "010a2a98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba264c",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba26dc",
      "READ",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba26e4",
      "READ",
      [
        "storage",
        "010a2ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md#insn-00ba2770) · [`00ba28dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md#insn-00ba28dc) · [`00ba295c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md#insn-00ba295c)
- 新版 `00ba27b4`（命令位置の公開資料なし） · `00ba2920`（命令位置の公開資料なし） · `00ba29a0`（命令位置の公開資料なし）

~~~diff
- 00ba2770 ["INT_ADD", "register:40f0:8", ["const:ba2770:8", "const:4:8"]]
- 00ba2770 ["CALL", null, ["callee:00ba2fb8:8"]]
+ 00ba27b4 ["INT_ADD", "register:40f0:8", ["const:ba27b4:8", "const:4:8"]]
+ 00ba27b4 ["CALL", null, ["callee:00ba2fb8:8"]]
- 00ba2770 bytes 01020094
+ 00ba27b4 bytes 01020094
- 00ba28dc ["INT_ADD", "register:40f0:8", ["const:ba28dc:8", "const:4:8"]]
- 00ba28dc ["CALL", null, ["callee:00be1890:8"]]
+ 00ba2920 ["INT_ADD", "register:40f0:8", ["const:ba2920:8", "const:4:8"]]
+ 00ba2920 ["CALL", null, ["callee:00be1890:8"]]
- 00ba28dc bytes d9fb0094
+ 00ba2920 bytes dcfb0094
- 00ba295c ["INT_ADD", "register:40f0:8", ["const:ba295c:8", "const:4:8"]]
- 00ba295c ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba29a0 ["INT_ADD", "register:40f0:8", ["const:ba29a0:8", "const:4:8"]]
+ 00ba29a0 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba295c bytes a5e10094
+ 00ba29a0 bytes a8e10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d95aa7a2ca0e15de59d72fc166b2546d"></a>

### [`00ba2c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md) → [`00ba2cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md) _ZNSt6__ndk16locale7classicEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md) · 呼出先 3件 [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00be18d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18d0.md) · 呼出先 3件 [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba2d3c",
      "incomplete_value": false,
      "site": "00ba2d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2cf8",
      "incomplete_value": false,
      "site": "00ba2cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "00ba2d10",
      "incomplete_value": false,
      "site": "00ba2d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2ccc",
      "incomplete_value": false,
      "site": "00ba2cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "definition_site": "00ba2d28",
      "incomplete_value": false,
      "site": "00ba2d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2ce4",
      "incomplete_value": false,
      "site": "00ba2ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "00ba2cec",
      "READ",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba2cf8",
      "DATA",
      [
        "storage",
        "010a2a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba2d10",
      "PARAM",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba2cec",
      "READ",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba2cf8",
      "DATA",
      [
        "storage",
        "010a2ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba2d10",
      "PARAM",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md#insn-00ba2ca4) · [`00ba2cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md#insn-00ba2cb4) · [`00ba2cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md#insn-00ba2cd0)
- 新版 `00ba2ce8`（命令位置の公開資料なし） · `00ba2cf8`（命令位置の公開資料なし） · `00ba2d14`（命令位置の公開資料なし）

~~~diff
- 00ba2ca4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00ba2ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba2ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba2ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba2ce8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00ba2ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba2ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba2ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba2ca4 bytes 08812a91
+ 00ba2ce8 bytes 08812b91
- 00ba2cb4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00ba2cb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ba2cb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ba2cb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ba2cf8 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00ba2cf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ba2cf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ba2cf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ba2cb4 bytes 00602a91
+ 00ba2cf8 bytes 00602b91
- 00ba2cd0 ["INT_ADD", "register:40f0:8", ["const:ba2cd0:8", "const:4:8"]]
- 00ba2cd0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba2d14 ["INT_ADD", "register:40f0:8", ["const:ba2d14:8", "const:4:8"]]
+ 00ba2d14 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba2cd0 bytes b8e00094
+ 00ba2d14 bytes bbe00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6d25bf318e9b2af5043731a4c29ecc"></a>

### [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) → [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) FUN_00ba2d60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2d84",
      "incomplete_value": true,
      "site": "00ba2d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2d40",
      "incomplete_value": true,
      "site": "00ba2d44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba2d90",
      "incomplete_value": true,
      "site": "00ba2d94",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba2d4c",
      "incomplete_value": true,
      "site": "00ba2d50",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba2db8",
      "incomplete_value": true,
      "site": "00ba2dbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2d74",
      "incomplete_value": true,
      "site": "00ba2d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
      "00ba2d84",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2d88",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2d8c",
      "READ",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2d84",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2d88",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2d8c",
      "READ",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md#insn-00ba2d78) · [`00ba2d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md#insn-00ba2d40) · [`00ba2d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md#insn-00ba2d68)
- 新版 `00ba2dbc`（命令位置の公開資料なし） · `00ba2d84`（命令位置の公開資料なし） · `00ba2dac`（命令位置の公開資料なし）

~~~diff
- 00ba2d78 ["INT_ADD", "register:40f0:8", ["const:ba2d78:8", "const:4:8"]]
- 00ba2d78 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba2dbc ["INT_ADD", "register:40f0:8", ["const:ba2dbc:8", "const:4:8"]]
+ 00ba2dbc ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba2d78 bytes 46f80094
+ 00ba2dbc bytes 49f80094
- 00ba2d40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ba2d40 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2d84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00ba2d84 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2d40 bytes 949a42f9
+ 00ba2d84 bytes 94c242f9
- 00ba2d68 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba2dac ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba2d68 bytes e21c0b10
+ 00ba2dac bytes e21c0b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a56fe1cb3c194a5077681eeb02ed1ff"></a>

### [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) → [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) FUN_00ba2e8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2eb0",
      "incomplete_value": true,
      "site": "00ba2eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2e6c",
      "incomplete_value": true,
      "site": "00ba2e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba2ebc",
      "incomplete_value": true,
      "site": "00ba2ec0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba2e78",
      "incomplete_value": true,
      "site": "00ba2e7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba2ee4",
      "incomplete_value": true,
      "site": "00ba2ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2ea0",
      "incomplete_value": true,
      "site": "00ba2ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "00ba2eb0",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2eb4",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2eb8",
      "READ",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2eb0",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2eb4",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2eb8",
      "READ",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md#insn-00ba2ea4) · [`00ba2e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md#insn-00ba2e6c) · [`00ba2e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md#insn-00ba2e94)
- 新版 `00ba2ee8`（命令位置の公開資料なし） · `00ba2eb0`（命令位置の公開資料なし） · `00ba2ed8`（命令位置の公開資料なし）

~~~diff
- 00ba2ea4 ["INT_ADD", "register:40f0:8", ["const:ba2ea4:8", "const:4:8"]]
- 00ba2ea4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba2ee8 ["INT_ADD", "register:40f0:8", ["const:ba2ee8:8", "const:4:8"]]
+ 00ba2ee8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba2ea4 bytes fbf70094
+ 00ba2ee8 bytes fef70094
- 00ba2e6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
- 00ba2e6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2eb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00ba2eb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2e6c bytes 94c646f9
+ 00ba2eb0 bytes 94ee46f9
- 00ba2e94 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba2ed8 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba2e94 bytes 82130b10
+ 00ba2ed8 bytes 82130b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130f908423406c9828e3cba8b8c28e1e"></a>

### [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) → [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) FUN_00ba2fb8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2fdc",
      "incomplete_value": true,
      "site": "00ba2fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00ba2f98",
      "incomplete_value": true,
      "site": "00ba2f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba2fe8",
      "incomplete_value": true,
      "site": "00ba2fec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba2fa4",
      "incomplete_value": true,
      "site": "00ba2fa8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3010",
      "incomplete_value": true,
      "site": "00ba3014",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "old": {
      "definition_site": "00ba2fcc",
      "incomplete_value": true,
      "site": "00ba2fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:df0:8"
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
      "00ba2fdc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2fe0",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2fe4",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2fdc",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2fe0",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2fe4",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md#insn-00ba2fd0) · [`00ba2f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md#insn-00ba2f98) · [`00ba2fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md#insn-00ba2fc0)
- 新版 `00ba3014`（命令位置の公開資料なし） · `00ba2fdc`（命令位置の公開資料なし） · `00ba3004`（命令位置の公開資料なし）

~~~diff
- 00ba2fd0 ["INT_ADD", "register:40f0:8", ["const:ba2fd0:8", "const:4:8"]]
- 00ba2fd0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3014 ["INT_ADD", "register:40f0:8", ["const:ba3014:8", "const:4:8"]]
+ 00ba3014 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba2fd0 bytes b0f70094
+ 00ba3014 bytes b3f70094
- 00ba2f98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00ba2f98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2fdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e40:8"]]
+ 00ba2fdc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2f98 bytes 94fa46f9
+ 00ba2fdc bytes 942247f9
- 00ba2fc0 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3004 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba2fc0 bytes 220a0b10
+ 00ba3004 bytes 220a0b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76b42f4fd6a375a1eed161a35e293531"></a>

### [`00ba30a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md) → [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md) FUN_00ba30e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3108",
      "incomplete_value": true,
      "site": "00ba310c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba30c4",
      "incomplete_value": true,
      "site": "00ba30c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3114",
      "incomplete_value": true,
      "site": "00ba3118",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba30d0",
      "incomplete_value": true,
      "site": "00ba30d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba313c",
      "incomplete_value": true,
      "site": "00ba3140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba30f8",
      "incomplete_value": true,
      "site": "00ba30fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ba3108",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba310c",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3110",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3108",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00ba310c",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3110",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba30fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md#insn-00ba30fc) · [`00ba30c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md#insn-00ba30c4) · [`00ba30ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md#insn-00ba30ec)
- 新版 `00ba3140`（命令位置の公開資料なし） · `00ba3108`（命令位置の公開資料なし） · `00ba3130`（命令位置の公開資料なし）

~~~diff
- 00ba30fc ["INT_ADD", "register:40f0:8", ["const:ba30fc:8", "const:4:8"]]
- 00ba30fc ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3140 ["INT_ADD", "register:40f0:8", ["const:ba3140:8", "const:4:8"]]
+ 00ba3140 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba30fc bytes 65f70094
+ 00ba3140 bytes 68f70094
- 00ba30c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00ba30c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3108 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00ba3108 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba30c4 bytes 946246f9
+ 00ba3108 bytes 948a46f9
- 00ba30ec ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3130 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba30ec bytes c2000b10
+ 00ba3130 bytes c2000b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6aa60292e0c50031627b727aa137f23"></a>

### [`00ba31cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba31cc.md) → [`00ba3210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3210.md) FUN_00ba3210

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3234",
      "incomplete_value": true,
      "site": "00ba3238",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba31f0",
      "incomplete_value": true,
      "site": "00ba31f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3240",
      "incomplete_value": true,
      "site": "00ba3244",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba31fc",
      "incomplete_value": true,
      "site": "00ba3200",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3268",
      "incomplete_value": true,
      "site": "00ba326c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3224",
      "incomplete_value": true,
      "site": "00ba3228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ba3234",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3238",
      "DATA",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba323c",
      "READ",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3234",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3238",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba323c",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba31cc.md#insn-00ba3228) · [`00ba31f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba31cc.md#insn-00ba31f0) · [`00ba3218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba31cc.md#insn-00ba3218)
- 新版 `00ba326c`（命令位置の公開資料なし） · `00ba3234`（命令位置の公開資料なし） · `00ba325c`（命令位置の公開資料なし）

~~~diff
- 00ba3228 ["INT_ADD", "register:40f0:8", ["const:ba3228:8", "const:4:8"]]
- 00ba3228 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba326c ["INT_ADD", "register:40f0:8", ["const:ba326c:8", "const:4:8"]]
+ 00ba326c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3228 bytes 1af70094
+ 00ba326c bytes 1df70094
- 00ba31f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
- 00ba31f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3234 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab0:8"]]
+ 00ba3234 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba31f0 bytes 943245f9
+ 00ba3234 bytes 945a45f9
- 00ba3218 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba325c ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3218 bytes 62f70a10
+ 00ba325c bytes 62f70a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e5e3e9b5d29647763c951bf81dab537"></a>

### [`00ba32f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba32f8.md) → [`00ba333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba333c.md) FUN_00ba333c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3360",
      "incomplete_value": true,
      "site": "00ba3364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba331c",
      "incomplete_value": true,
      "site": "00ba3320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba336c",
      "incomplete_value": true,
      "site": "00ba3370",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3328",
      "incomplete_value": true,
      "site": "00ba332c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3394",
      "incomplete_value": true,
      "site": "00ba3398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3350",
      "incomplete_value": true,
      "site": "00ba3354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00ba3360",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3364",
      "DATA",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3368",
      "READ",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3360",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3364",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3368",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba32f8.md#insn-00ba3354) · [`00ba331c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba32f8.md#insn-00ba331c) · [`00ba3344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba32f8.md#insn-00ba3344)
- 新版 `00ba3398`（命令位置の公開資料なし） · `00ba3360`（命令位置の公開資料なし） · `00ba3388`（命令位置の公開資料なし）

~~~diff
- 00ba3354 ["INT_ADD", "register:40f0:8", ["const:ba3354:8", "const:4:8"]]
- 00ba3354 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3398 ["INT_ADD", "register:40f0:8", ["const:ba3398:8", "const:4:8"]]
+ 00ba3398 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3354 bytes cff60094
+ 00ba3398 bytes d2f60094
- 00ba331c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00ba331c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3360 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
+ 00ba3360 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba331c bytes 949646f9
+ 00ba3360 bytes 94be46f9
- 00ba3344 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3388 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3344 bytes 02ee0a10
+ 00ba3388 bytes 02ee0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-169e29c7930d6ae1a758c81861ff521a"></a>

### [`00ba3424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3424.md) → [`00ba3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3468.md) FUN_00ba3468

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba348c",
      "incomplete_value": true,
      "site": "00ba3490",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3448",
      "incomplete_value": true,
      "site": "00ba344c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3498",
      "incomplete_value": true,
      "site": "00ba349c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3454",
      "incomplete_value": true,
      "site": "00ba3458",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba34c0",
      "incomplete_value": true,
      "site": "00ba34c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba347c",
      "incomplete_value": true,
      "site": "00ba3480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "00ba348c",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3490",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3494",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba348c",
      "READ",
      [
        "storage",
        "00c1bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3490",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3494",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3424.md#insn-00ba3480) · [`00ba3448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3424.md#insn-00ba3448) · [`00ba3470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3424.md#insn-00ba3470)
- 新版 `00ba34c4`（命令位置の公開資料なし） · `00ba348c`（命令位置の公開資料なし） · `00ba34b4`（命令位置の公開資料なし）

~~~diff
- 00ba3480 ["INT_ADD", "register:40f0:8", ["const:ba3480:8", "const:4:8"]]
- 00ba3480 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba34c4 ["INT_ADD", "register:40f0:8", ["const:ba34c4:8", "const:4:8"]]
+ 00ba34c4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3480 bytes 84f60094
+ 00ba34c4 bytes 87f60094
- 00ba3448 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
- 00ba3448 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba348c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df8:8"]]
+ 00ba348c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3448 bytes 94d646f9
+ 00ba348c bytes 94fe46f9
- 00ba3470 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba34b4 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3470 bytes a2e40a10
+ 00ba34b4 bytes a2e40a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6c23b37d73df982ae9d39fcb863b271"></a>

### [`00ba3550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3550.md) → [`00ba3594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md) FUN_00ba3594

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba35b8",
      "incomplete_value": true,
      "site": "00ba35bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3574",
      "incomplete_value": true,
      "site": "00ba3578",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba35c4",
      "incomplete_value": true,
      "site": "00ba35c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3580",
      "incomplete_value": true,
      "site": "00ba3584",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba35ec",
      "incomplete_value": true,
      "site": "00ba35f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba35a8",
      "incomplete_value": true,
      "site": "00ba35ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
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
      "00ba35b8",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba35bc",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba35c0",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba35b8",
      "READ",
      [
        "storage",
        "00c1be08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba35bc",
      "DATA",
      [
        "storage",
        "010a2b60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba35c0",
      "READ",
      [
        "storage",
        "010a2b60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba35ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3550.md#insn-00ba35ac) · [`00ba3574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3550.md#insn-00ba3574) · [`00ba359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3550.md#insn-00ba359c)
- 新版 `00ba35f0`（命令位置の公開資料なし） · `00ba35b8`（命令位置の公開資料なし） · `00ba35e0`（命令位置の公開資料なし）

~~~diff
- 00ba35ac ["INT_ADD", "register:40f0:8", ["const:ba35ac:8", "const:4:8"]]
- 00ba35ac ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba35f0 ["INT_ADD", "register:40f0:8", ["const:ba35f0:8", "const:4:8"]]
+ 00ba35f0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba35ac bytes 39f60094
+ 00ba35f0 bytes 3cf60094
- 00ba3574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
- 00ba3574 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba35b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
+ 00ba35b8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3574 bytes 94de46f9
+ 00ba35b8 bytes 940647f9
- 00ba359c ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba35e0 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba359c bytes 42db0a10
+ 00ba35e0 bytes 42db0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fccf8fc9866e084780899f379beeaf7"></a>

### [`00ba367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba367c.md) → [`00ba36c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba36c0.md) FUN_00ba36c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba36e4",
      "incomplete_value": true,
      "site": "00ba36e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba36a0",
      "incomplete_value": true,
      "site": "00ba36a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba36f0",
      "incomplete_value": true,
      "site": "00ba36f4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba36ac",
      "incomplete_value": true,
      "site": "00ba36b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3718",
      "incomplete_value": true,
      "site": "00ba371c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba36d4",
      "incomplete_value": true,
      "site": "00ba36d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
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
      "00ba36e4",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba36e8",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba36ec",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba36e4",
      "READ",
      [
        "storage",
        "00c1be18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba36e8",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba36ec",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba36d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba367c.md#insn-00ba36d8) · [`00ba36a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba367c.md#insn-00ba36a0) · [`00ba36c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba367c.md#insn-00ba36c8)
- 新版 `00ba371c`（命令位置の公開資料なし） · `00ba36e4`（命令位置の公開資料なし） · `00ba370c`（命令位置の公開資料なし）

~~~diff
- 00ba36d8 ["INT_ADD", "register:40f0:8", ["const:ba36d8:8", "const:4:8"]]
- 00ba36d8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba371c ["INT_ADD", "register:40f0:8", ["const:ba371c:8", "const:4:8"]]
+ 00ba371c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba36d8 bytes eef50094
+ 00ba371c bytes f1f50094
- 00ba36a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc8:8"]]
- 00ba36a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba36e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e18:8"]]
+ 00ba36e4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba36a0 bytes 94e646f9
+ 00ba36e4 bytes 940e47f9
- 00ba36c8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba370c ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba36c8 bytes e2d10a10
+ 00ba370c bytes e2d10a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d9096f7983ba5c1779cece167d90212"></a>

### [`00ba37a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba37a8.md) → [`00ba37ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba37ec.md) FUN_00ba37ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3810",
      "incomplete_value": true,
      "site": "00ba3814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba37cc",
      "incomplete_value": true,
      "site": "00ba37d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba381c",
      "incomplete_value": true,
      "site": "00ba3820",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba37d8",
      "incomplete_value": true,
      "site": "00ba37dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3844",
      "incomplete_value": true,
      "site": "00ba3848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3800",
      "incomplete_value": true,
      "site": "00ba3804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "00ba3810",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3814",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3818",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3810",
      "READ",
      [
        "storage",
        "00c1be28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3814",
      "DATA",
      [
        "storage",
        "010a2b70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3818",
      "READ",
      [
        "storage",
        "010a2b70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba37a8.md#insn-00ba3804) · [`00ba37cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba37a8.md#insn-00ba37cc) · [`00ba37f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba37a8.md#insn-00ba37f4)
- 新版 `00ba3848`（命令位置の公開資料なし） · `00ba3810`（命令位置の公開資料なし） · `00ba3838`（命令位置の公開資料なし）

~~~diff
- 00ba3804 ["INT_ADD", "register:40f0:8", ["const:ba3804:8", "const:4:8"]]
- 00ba3804 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3848 ["INT_ADD", "register:40f0:8", ["const:ba3848:8", "const:4:8"]]
+ 00ba3848 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3804 bytes a3f50094
+ 00ba3848 bytes a6f50094
- 00ba37cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
- 00ba37cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00ba3810 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba37cc bytes 94ee46f9
+ 00ba3810 bytes 941647f9
- 00ba37f4 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3838 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba37f4 bytes 82c80a10
+ 00ba3838 bytes 82c80a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f2278ffed191fd0a45683bb0bae94c"></a>

### [`00ba38d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba38d4.md) → [`00ba3918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3918.md) FUN_00ba3918

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba393c",
      "incomplete_value": true,
      "site": "00ba3940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba38f8",
      "incomplete_value": true,
      "site": "00ba38fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3948",
      "incomplete_value": true,
      "site": "00ba394c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3904",
      "incomplete_value": true,
      "site": "00ba3908",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3970",
      "incomplete_value": true,
      "site": "00ba3974",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba392c",
      "incomplete_value": true,
      "site": "00ba3930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
      "00ba393c",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3940",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3944",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba393c",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3940",
      "DATA",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3944",
      "READ",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba38d4.md#insn-00ba3930) · [`00ba38f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba38d4.md#insn-00ba38f8) · [`00ba3920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba38d4.md#insn-00ba3920)
- 新版 `00ba3974`（命令位置の公開資料なし） · `00ba393c`（命令位置の公開資料なし） · `00ba3964`（命令位置の公開資料なし）

~~~diff
- 00ba3930 ["INT_ADD", "register:40f0:8", ["const:ba3930:8", "const:4:8"]]
- 00ba3930 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3974 ["INT_ADD", "register:40f0:8", ["const:ba3974:8", "const:4:8"]]
+ 00ba3974 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3930 bytes 58f50094
+ 00ba3974 bytes 5bf50094
- 00ba38f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00ba38f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba393c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00ba393c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba38f8 bytes 949e46f9
+ 00ba393c bytes 94c646f9
- 00ba3920 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3964 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3920 bytes 22bf0a10
+ 00ba3964 bytes 22bf0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca28945769a4d898c66e976d8b179a8"></a>

### [`00ba3a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3a00.md) → [`00ba3a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3a44.md) FUN_00ba3a44

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3a68",
      "incomplete_value": true,
      "site": "00ba3a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3a24",
      "incomplete_value": true,
      "site": "00ba3a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3a74",
      "incomplete_value": true,
      "site": "00ba3a78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3a30",
      "incomplete_value": true,
      "site": "00ba3a34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3a9c",
      "incomplete_value": true,
      "site": "00ba3aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3a58",
      "incomplete_value": true,
      "site": "00ba3a5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "00ba3a68",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3a6c",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3a70",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3a68",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3a6c",
      "DATA",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3a70",
      "READ",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3a00.md#insn-00ba3a5c) · [`00ba3a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3a00.md#insn-00ba3a24) · [`00ba3a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3a00.md#insn-00ba3a4c)
- 新版 `00ba3aa0`（命令位置の公開資料なし） · `00ba3a68`（命令位置の公開資料なし） · `00ba3a90`（命令位置の公開資料なし）

~~~diff
- 00ba3a5c ["INT_ADD", "register:40f0:8", ["const:ba3a5c:8", "const:4:8"]]
- 00ba3a5c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3aa0 ["INT_ADD", "register:40f0:8", ["const:ba3aa0:8", "const:4:8"]]
+ 00ba3aa0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3a5c bytes 0df50094
+ 00ba3aa0 bytes 10f50094
- 00ba3a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00ba3a24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3a68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
+ 00ba3a68 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3a24 bytes 94a646f9
+ 00ba3a68 bytes 94ce46f9
- 00ba3a4c ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3a90 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3a4c bytes c2b50a10
+ 00ba3a90 bytes c2b50a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dd8aa73014880262e190cad768d632d"></a>

### [`00ba3b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3b2c.md) → [`00ba3b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3b70.md) FUN_00ba3b70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3b94",
      "incomplete_value": true,
      "site": "00ba3b98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3b50",
      "incomplete_value": true,
      "site": "00ba3b54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3ba0",
      "incomplete_value": true,
      "site": "00ba3ba4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3b5c",
      "incomplete_value": true,
      "site": "00ba3b60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3bc8",
      "incomplete_value": true,
      "site": "00ba3bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3b84",
      "incomplete_value": true,
      "site": "00ba3b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
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
      "00ba3b94",
      "READ",
      [
        "storage",
        "00c1bd60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3b98",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3b9c",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3b94",
      "READ",
      [
        "storage",
        "00c1bdb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3b98",
      "DATA",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3b9c",
      "READ",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3b2c.md#insn-00ba3b88) · [`00ba3b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3b2c.md#insn-00ba3b50) · [`00ba3b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3b2c.md#insn-00ba3b78)
- 新版 `00ba3bcc`（命令位置の公開資料なし） · `00ba3b94`（命令位置の公開資料なし） · `00ba3bbc`（命令位置の公開資料なし）

~~~diff
- 00ba3b88 ["INT_ADD", "register:40f0:8", ["const:ba3b88:8", "const:4:8"]]
- 00ba3b88 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3bcc ["INT_ADD", "register:40f0:8", ["const:ba3bcc:8", "const:4:8"]]
+ 00ba3bcc ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3b88 bytes c2f40094
+ 00ba3bcc bytes c5f40094
- 00ba3b50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d60:8"]]
- 00ba3b50 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3b94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00ba3b94 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3b50 bytes 94b246f9
+ 00ba3b94 bytes 94da46f9
- 00ba3b78 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3bbc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3b78 bytes 62ac0a10
+ 00ba3bbc bytes 62ac0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa8ee8951a53c9da8848e6d35389d581"></a>

### [`00ba3c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3c58.md) → [`00ba3c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3c9c.md) FUN_00ba3c9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1890.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be18e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3ccc",
      "incomplete_value": true,
      "site": "00ba3ccc",
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
      "definition_site": "00ba3c88",
      "incomplete_value": true,
      "site": "00ba3c88",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba3cbc",
      "READ",
      [
        "storage",
        "00c1bf18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3ccc",
      "DATA",
      [
        "storage",
        "00c15608",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba3cbc",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3ccc",
      "DATA",
      [
        "storage",
        "00c15658",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3c58.md#insn-00ba3c78) · [`00ba3c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3c58.md#insn-00ba3c7c) · [`00ba3c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3c58.md#insn-00ba3c80)
- 新版 `00ba3cbc`（命令位置の公開資料なし）

~~~diff
- 00ba3c78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 00ba3c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3cbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 00ba3cbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3c78 bytes 088d47f9
+ 00ba3cbc bytes 08b547f9
- 00ba3c7c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3c7c bytes f50300aa
- 00ba3c80 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba3c80 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a9e2548d73991b90caf29382c9b6ff2"></a>

### [`00ba3d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3d3c.md) → [`00ba3d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3d80.md) FUN_00ba3d80

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3da4",
      "incomplete_value": true,
      "site": "00ba3da8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3d60",
      "incomplete_value": true,
      "site": "00ba3d64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3db0",
      "incomplete_value": true,
      "site": "00ba3db4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3d6c",
      "incomplete_value": true,
      "site": "00ba3d70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba3dd8",
      "incomplete_value": true,
      "site": "00ba3ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3d94",
      "incomplete_value": true,
      "site": "00ba3d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
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
      "00ba3da4",
      "READ",
      [
        "storage",
        "00c1bd58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3da8",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3dac",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3da4",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3da8",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3dac",
      "READ",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3d3c.md#insn-00ba3d98) · [`00ba3d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3d3c.md#insn-00ba3d60) · [`00ba3d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3d3c.md#insn-00ba3d88)
- 新版 `00ba3ddc`（命令位置の公開資料なし） · `00ba3da4`（命令位置の公開資料なし） · `00ba3dcc`（命令位置の公開資料なし）

~~~diff
- 00ba3d98 ["INT_ADD", "register:40f0:8", ["const:ba3d98:8", "const:4:8"]]
- 00ba3d98 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3ddc ["INT_ADD", "register:40f0:8", ["const:ba3ddc:8", "const:4:8"]]
+ 00ba3ddc ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3d98 bytes 3ef40094
+ 00ba3ddc bytes 41f40094
- 00ba3d60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
- 00ba3d60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00ba3da4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3d60 bytes 94ae46f9
+ 00ba3da4 bytes 94d646f9
- 00ba3d88 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3dcc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3d88 bytes e29b0a10
+ 00ba3dcc bytes e29b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce54127ff3a94fdc93e7f486035604a1"></a>

### [`00ba3e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md) → [`00ba3eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3eac.md) FUN_00ba3eac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18a0.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be18f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3edc",
      "incomplete_value": true,
      "site": "00ba3edc",
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
      "definition_site": "00ba3e98",
      "incomplete_value": true,
      "site": "00ba3e98",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba3ecc",
      "READ",
      [
        "storage",
        "00c1bf20",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3edc",
      "DATA",
      [
        "storage",
        "00c15690",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba3ecc",
      "READ",
      [
        "storage",
        "00c1bf70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3edc",
      "DATA",
      [
        "storage",
        "00c156e0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md#insn-00ba3e88) · [`00ba3e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md#insn-00ba3e8c) · [`00ba3e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md#insn-00ba3e90)
- 新版 `00ba3ecc`（命令位置の公開資料なし）

~~~diff
- 00ba3e88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 00ba3e88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3ecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 00ba3ecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3e88 bytes 089147f9
+ 00ba3ecc bytes 08b947f9
- 00ba3e8c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3e8c bytes f50300aa
- 00ba3e90 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba3e90 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

