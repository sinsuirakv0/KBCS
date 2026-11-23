# v15.7.3 → v15.7.4 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-c41bacfa6246340462e4588f3c39509f"></a>

### [`00b6a620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md) → [`00b6a664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a6b4",
      "incomplete_value": false,
      "site": "00b6a6b8",
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
      "definition_site": "00b6a670",
      "incomplete_value": false,
      "site": "00b6a674",
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
      "definition_site": "00b6a710",
      "incomplete_value": true,
      "site": "00b6a72c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6a6cc",
      "incomplete_value": true,
      "site": "00b6a6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a714",
      "incomplete_value": true,
      "site": "00b6a72c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b6a6d0",
      "incomplete_value": true,
      "site": "00b6a6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6a698",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a69c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a7a0"
      ]
    ],
    [
      "00b6a6b4",
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
      "00b6a698",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a69c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a7e4"
      ]
    ],
    [
      "00b6a6b4",
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

- 旧版 [`00b6a674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md#insn-00b6a674) · [`00b6a6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md#insn-00b6a6e8) · [`00b6a758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md#insn-00b6a758)
- 新版 [`00b6a6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a6b8) · [`00b6a72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a72c) · [`00b6a79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a664.md#insn-00b6a79c)

~~~diff
- 00b6a674 ["INT_ADD", "register:40f0:8", ["const:b6a674:8", "const:4:8"]]
- 00b6a674 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a6b8 ["INT_ADD", "register:40f0:8", ["const:b6a6b8:8", "const:4:8"]]
+ 00b6a6b8 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a674 bytes afce0194
+ 00b6a6b8 bytes b2ce0194
- 00b6a6e8 ["INT_ADD", "register:40f0:8", ["const:b6a6e8:8", "const:4:8"]]
- 00b6a6e8 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a72c ["INT_ADD", "register:40f0:8", ["const:b6a72c:8", "const:4:8"]]
+ 00b6a72c ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a6e8 bytes 82cd0194
+ 00b6a72c bytes 85cd0194
- 00b6a758 ["INT_ADD", "register:40f0:8", ["const:b6a758:8", "const:4:8"]]
- 00b6a758 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a79c ["INT_ADD", "register:40f0:8", ["const:b6a79c:8", "const:4:8"]]
+ 00b6a79c ["CALL", null, ["callee:00bde180:8"]]
- 00b6a758 bytes 76ce0194
+ 00b6a79c bytes 79ce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adfd6595a647bc17f607c4b6b981dc4"></a>

### [`00b6a7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md) → [`00b6a828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a87c",
      "incomplete_value": false,
      "site": "00b6a880",
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
      "definition_site": "00b6a838",
      "incomplete_value": false,
      "site": "00b6a83c",
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
      "definition_site": "00b6a8d8",
      "incomplete_value": true,
      "site": "00b6a8ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6a894",
      "incomplete_value": true,
      "site": "00b6a8a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a8dc",
      "incomplete_value": true,
      "site": "00b6a8ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a898",
      "incomplete_value": true,
      "site": "00b6a8a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6a85c",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a87c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6a8d8",
      "READ",
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
      "00b6a85c",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a87c",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b6a8d8",
      "READ",
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

- 旧版 [`00b6a83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md#insn-00b6a83c) · [`00b6a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md#insn-00b6a8a8) · [`00b6a8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md#insn-00b6a8d4)
- 新版 [`00b6a880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a880) · [`00b6a8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a8ec) · [`00b6a918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6a828.md#insn-00b6a918)

~~~diff
- 00b6a83c ["INT_ADD", "register:40f0:8", ["const:b6a83c:8", "const:4:8"]]
- 00b6a83c ["CALL", null, ["callee:00bde180:8"]]
+ 00b6a880 ["INT_ADD", "register:40f0:8", ["const:b6a880:8", "const:4:8"]]
+ 00b6a880 ["CALL", null, ["callee:00bde180:8"]]
- 00b6a83c bytes 3dce0194
+ 00b6a880 bytes 40ce0194
- 00b6a8a8 ["INT_ADD", "register:40f0:8", ["const:b6a8a8:8", "const:4:8"]]
- 00b6a8a8 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6a8ec ["INT_ADD", "register:40f0:8", ["const:b6a8ec:8", "const:4:8"]]
+ 00b6a8ec ["CALL", null, ["callee:00bddd40:8"]]
- 00b6a8a8 bytes 12cd0194
+ 00b6a8ec bytes 15cd0194
- 00b6a8d4 ["INT_ADD", "register:40f0:8", ["const:b6a8d4:8", "const:4:8"]]
- 00b6a8d4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6a918 ["INT_ADD", "register:40f0:8", ["const:b6a918:8", "const:4:8"]]
+ 00b6a918 ["CALL", null, ["callee:0047495c:8"]]
- 00b6a8d4 bytes 2228e497
+ 00b6a918 bytes 1128e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b6d783c9e4b9478d2d4083247d280e"></a>

### [`00b6aaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md) → [`00b6aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b6cabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00b6cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ab6c",
      "incomplete_value": false,
      "site": "00b6ab80",
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
            "const:19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ab28",
      "incomplete_value": false,
      "site": "00b6ab3c",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ab90",
      "incomplete_value": false,
      "site": "00b6ab94",
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
            "const:7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ab4c",
      "incomplete_value": false,
      "site": "00b6ab50",
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
            "const:fef:8"
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
      "00b6ab30",
      "READ",
      [
        "storage",
        "00c1bbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ab30",
      "PARAM",
      [
        "storage",
        "00b6cabc",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00b6ab6c",
      "PARAM",
      [
        "storage",
        "002a8f7f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ab30",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ab30",
      "PARAM",
      [
        "storage",
        "00b6cb00",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00b6ab6c",
      "PARAM",
      [
        "storage",
        "002a9019",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ab0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab0c) · [`00b6ab3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab3c) · [`00b6ab50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab50)
- 新版 [`00b6ab50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab50) · [`00b6ab80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab80) · [`00b6ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aae8.md#insn-00b6ab94)

~~~diff
- 00b6ab0c ["INT_ADD", "register:40f0:8", ["const:b6ab0c:8", "const:4:8"]]
- 00b6ab0c ["CALL", null, ["callee:00bddf80:8"]]
+ 00b6ab50 ["INT_ADD", "register:40f0:8", ["const:b6ab50:8", "const:4:8"]]
+ 00b6ab50 ["CALL", null, ["callee:00bddf80:8"]]
- 00b6ab0c bytes 09cd0194
+ 00b6ab50 bytes 0ccd0194
- 00b6ab3c ["INT_ADD", "register:40f0:8", ["const:b6ab3c:8", "const:4:8"]]
- 00b6ab3c ["CALL", null, ["callee:00be0dd0:8"]]
+ 00b6ab80 ["INT_ADD", "register:40f0:8", ["const:b6ab80:8", "const:4:8"]]
+ 00b6ab80 ["CALL", null, ["callee:00be0dd0:8"]]
- 00b6ab3c bytes 91d80194
+ 00b6ab80 bytes 94d80194
- 00b6ab50 ["INT_ADD", "register:40f0:8", ["const:b6ab50:8", "const:4:8"]]
- 00b6ab50 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6ab94 ["INT_ADD", "register:40f0:8", ["const:b6ab94:8", "const:4:8"]]
+ 00b6ab94 ["CALL", null, ["callee:00bde180:8"]]
- 00b6ab50 bytes 78cd0194
+ 00b6ab94 bytes 7bcd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660704537c4c3438d83796db01eff3da"></a>

### [`00b6acec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md) → [`00b6ad30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ad3c",
      "incomplete_value": false,
      "site": "00b6ad40",
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
            "const:7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6acf8",
      "incomplete_value": false,
      "site": "00b6acfc",
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
            "const:fef:8"
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
      "00b6ad3c",
      "PARAM",
      [
        "storage",
        "002a3fef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ad3c",
      "PARAM",
      [
        "storage",
        "002a407a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6acfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md#insn-00b6acfc) · [`00b6acf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md#insn-00b6acf4) · [`00b6acf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md#insn-00b6acf8)
- 新版 [`00b6ad40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad40) · [`00b6ad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad38) · [`00b6ad3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad30.md#insn-00b6ad3c)

~~~diff
- 00b6acfc ["INT_ADD", "register:40f0:8", ["const:b6acfc:8", "const:4:8"]]
- 00b6acfc ["CALL", null, ["callee:00bde180:8"]]
+ 00b6ad40 ["INT_ADD", "register:40f0:8", ["const:b6ad40:8", "const:4:8"]]
+ 00b6ad40 ["CALL", null, ["callee:00bde180:8"]]
- 00b6acfc bytes 0dcd0194
+ 00b6ad40 bytes 10cd0194
- 00b6acf4 ["COPY", "register:4000:8", ["const:2a3000:8"]]
+ 00b6ad38 ["COPY", "register:4000:8", ["const:2a4000:8"]]
- 00b6acf4 bytes c0b9ffb0
+ 00b6ad38 bytes c0b9ffd0
- 00b6acf8 ["COPY", "tmp:0:8", ["const:fef:8"]]
- 00b6acf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6acf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6acf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad3c ["COPY", "tmp:0:8", ["const:7a:8"]]
+ 00b6ad3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6acf8 bytes 00bc3f91
+ 00b6ad3c bytes 00e80191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6876581fd24bb35ad869267475b01fea"></a>

### [`00b6ad38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md) → [`00b6ad7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ada8",
      "incomplete_value": false,
      "site": "00b6adac",
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
      "definition_site": "00b6ad64",
      "incomplete_value": false,
      "site": "00b6ad68",
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
      "00b6ada8",
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
      "00b6ada8",
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

- 旧版 [`00b6ad68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad68) · [`00b6ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad54) · [`00b6ad64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad64)
- 新版 [`00b6adac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6adac) · [`00b6ad98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6ad98) · [`00b6ada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ad7c.md#insn-00b6ada8)

~~~diff
- 00b6ad68 ["INT_ADD", "register:40f0:8", ["const:b6ad68:8", "const:4:8"]]
- 00b6ad68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6adac ["INT_ADD", "register:40f0:8", ["const:b6adac:8", "const:4:8"]]
+ 00b6adac ["CALL", null, ["callee:00bde180:8"]]
- 00b6ad68 bytes f2cc0194
+ 00b6adac bytes f5cc0194
- 00b6ad54 ["INT_ADD", "register:40f0:8", ["const:b6ad54:8", "const:4:8"]]
- 00b6ad54 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6ad98 ["INT_ADD", "register:40f0:8", ["const:b6ad98:8", "const:4:8"]]
+ 00b6ad98 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6ad54 bytes 8fcd0194
+ 00b6ad98 bytes 92cd0194
- 00b6ad64 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6ad64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ad64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ad64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6ada8 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6ada8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ada8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ada8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ad64 bytes 00303991
+ 00b6ada8 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e82ffb659a6d4ce38340a896268a17"></a>

### [`00b6addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md) → [`00b6ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md) · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 1件 [`00be0e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e40.md) · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ae50",
      "incomplete_value": false,
      "site": "00b6ae54",
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
      "definition_site": "00b6ae0c",
      "incomplete_value": false,
      "site": "00b6ae10",
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
      "definition_site": "00b6ae84",
      "incomplete_value": false,
      "site": "00b6ae88",
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
      "definition_site": "00b6ae40",
      "incomplete_value": false,
      "site": "00b6ae44",
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
      "00b6ae50",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6ae84",
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
      "00b6ae50",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "00b6ae84",
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

- 旧版 [`00b6ae10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6ae10) · [`00b6ae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6ae44) · [`00b6adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6adfc)
- 新版 [`00b6ae54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae54) · [`00b6ae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae88) · [`00b6ae40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6ae20.md#insn-00b6ae40)

~~~diff
- 00b6ae10 ["INT_ADD", "register:40f0:8", ["const:b6ae10:8", "const:4:8"]]
- 00b6ae10 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6ae54 ["INT_ADD", "register:40f0:8", ["const:b6ae54:8", "const:4:8"]]
+ 00b6ae54 ["CALL", null, ["callee:00bde180:8"]]
- 00b6ae10 bytes c8cc0194
+ 00b6ae54 bytes cbcc0194
- 00b6ae44 ["INT_ADD", "register:40f0:8", ["const:b6ae44:8", "const:4:8"]]
- 00b6ae44 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6ae88 ["INT_ADD", "register:40f0:8", ["const:b6ae88:8", "const:4:8"]]
+ 00b6ae88 ["CALL", null, ["callee:00bde180:8"]]
- 00b6ae44 bytes bbcc0194
+ 00b6ae88 bytes becc0194
- 00b6adfc ["INT_ADD", "register:40f0:8", ["const:b6adfc:8", "const:4:8"]]
- 00b6adfc ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6ae40 ["INT_ADD", "register:40f0:8", ["const:b6ae40:8", "const:4:8"]]
+ 00b6ae40 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6adfc bytes 65cd0194
+ 00b6ae40 bytes 68cd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b23f6cbae21bfc4b28cd518deb3fa9"></a>

### [`00b6aeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md) → [`00b6aef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6af1c",
      "incomplete_value": false,
      "site": "00b6af20",
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
      "definition_site": "00b6aed8",
      "incomplete_value": false,
      "site": "00b6aedc",
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
      "00b6af1c",
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
      "00b6af1c",
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

- 旧版 [`00b6aedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aedc) · [`00b6aec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aec8) · [`00b6aed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aed8)
- 新版 [`00b6af20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af20) · [`00b6af0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af0c) · [`00b6af1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6aef4.md#insn-00b6af1c)

~~~diff
- 00b6aedc ["INT_ADD", "register:40f0:8", ["const:b6aedc:8", "const:4:8"]]
- 00b6aedc ["CALL", null, ["callee:00bde180:8"]]
+ 00b6af20 ["INT_ADD", "register:40f0:8", ["const:b6af20:8", "const:4:8"]]
+ 00b6af20 ["CALL", null, ["callee:00bde180:8"]]
- 00b6aedc bytes 95cc0194
+ 00b6af20 bytes 98cc0194
- 00b6aec8 ["INT_ADD", "register:40f0:8", ["const:b6aec8:8", "const:4:8"]]
- 00b6aec8 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6af0c ["INT_ADD", "register:40f0:8", ["const:b6af0c:8", "const:4:8"]]
+ 00b6af0c ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6aec8 bytes 32cd0194
+ 00b6af0c bytes 35cd0194
- 00b6aed8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6aed8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6aed8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6aed8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6af1c ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6af1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6aed8 bytes 00303991
+ 00b6af1c bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15bcbd96f662182eef7d3d5bed3b2899"></a>

### [`00b6af1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md) → [`00b6af60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6af88",
      "incomplete_value": false,
      "site": "00b6af8c",
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
      "definition_site": "00b6af44",
      "incomplete_value": false,
      "site": "00b6af48",
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
      "00b6af88",
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
      "00b6af88",
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

- 旧版 [`00b6af48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af48) · [`00b6af34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af34) · [`00b6af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af44)
- 新版 [`00b6af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af8c) · [`00b6af78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af78) · [`00b6af88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6af60.md#insn-00b6af88)

~~~diff
- 00b6af48 ["INT_ADD", "register:40f0:8", ["const:b6af48:8", "const:4:8"]]
- 00b6af48 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6af8c ["INT_ADD", "register:40f0:8", ["const:b6af8c:8", "const:4:8"]]
+ 00b6af8c ["CALL", null, ["callee:00bde180:8"]]
- 00b6af48 bytes 7acc0194
+ 00b6af8c bytes 7dcc0194
- 00b6af34 ["INT_ADD", "register:40f0:8", ["const:b6af34:8", "const:4:8"]]
- 00b6af34 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6af78 ["INT_ADD", "register:40f0:8", ["const:b6af78:8", "const:4:8"]]
+ 00b6af78 ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6af34 bytes 17cd0194
+ 00b6af78 bytes 1acd0194
- 00b6af44 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6af44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6af44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6af44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6af88 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6af88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6af44 bytes 00303991
+ 00b6af88 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2ddf342f3de50d077cd0b70feeb926c"></a>

### [`00b6af90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md) → [`00b6afd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md) _ZN8firebase4auth17PhoneAuthProviderD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0970.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 1件 [`00be09c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09c0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6affc",
      "incomplete_value": false,
      "site": "00b6b000",
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
      "definition_site": "00b6afb8",
      "incomplete_value": false,
      "site": "00b6afbc",
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
      "00b6affc",
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
      "00b6affc",
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

- 旧版 [`00b6afbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afbc) · [`00b6afa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afa8) · [`00b6afb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afb8)
- 新版 [`00b6b000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6b000) · [`00b6afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6afec) · [`00b6affc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6a/00b6afd4.md#insn-00b6affc)

~~~diff
- 00b6afbc ["INT_ADD", "register:40f0:8", ["const:b6afbc:8", "const:4:8"]]
- 00b6afbc ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b000 ["INT_ADD", "register:40f0:8", ["const:b6b000:8", "const:4:8"]]
+ 00b6b000 ["CALL", null, ["callee:00bde180:8"]]
- 00b6afbc bytes 5dcc0194
+ 00b6b000 bytes 60cc0194
- 00b6afa8 ["INT_ADD", "register:40f0:8", ["const:b6afa8:8", "const:4:8"]]
- 00b6afa8 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6afec ["INT_ADD", "register:40f0:8", ["const:b6afec:8", "const:4:8"]]
+ 00b6afec ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6afa8 bytes facc0194
+ 00b6afec bytes fdcc0194
- 00b6afb8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6afb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6afb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6afb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6affc ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6affc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6affc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6affc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6afb8 bytes 00303991
+ 00b6affc bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56057d226a1a6832cd611c1ccc229ab0"></a>

### [`00b6b000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md) → [`00b6b044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6b05c",
      "incomplete_value": true,
      "site": "00b6b060",
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
      "definition_site": "00b6b018",
      "incomplete_value": true,
      "site": "00b6b01c",
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
      "definition_site": "00b6b084",
      "incomplete_value": false,
      "site": "00b6b088",
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
      "definition_site": "00b6b040",
      "incomplete_value": false,
      "site": "00b6b044",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b09c",
      "incomplete_value": true,
      "site": "00b6b0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6b058",
      "incomplete_value": true,
      "site": "00b6b068",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6b054",
      "READ",
      [
        "storage",
        "00c1bbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b060",
      "DATA",
      [
        "storage",
        "00c12748",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b084",
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
      "00b6b054",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b060",
      "DATA",
      [
        "storage",
        "00c12798",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b084",
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

- 旧版 [`00b6b024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b024) · [`00b6b044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b044) · [`00b6b068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b068)
- 新版 [`00b6b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b068) · [`00b6b088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b088) · [`00b6b0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b044.md#insn-00b6b0ac)

~~~diff
- 00b6b024 ["INT_ADD", "register:40f0:8", ["const:b6b024:8", "const:4:8"]]
- 00b6b024 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6b068 ["INT_ADD", "register:40f0:8", ["const:b6b068:8", "const:4:8"]]
+ 00b6b068 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6b024 bytes f3bf0194
+ 00b6b068 bytes f6bf0194
- 00b6b044 ["INT_ADD", "register:40f0:8", ["const:b6b044:8", "const:4:8"]]
- 00b6b044 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b088 ["INT_ADD", "register:40f0:8", ["const:b6b088:8", "const:4:8"]]
+ 00b6b088 ["CALL", null, ["callee:00bde180:8"]]
- 00b6b044 bytes 3bcc0194
+ 00b6b088 bytes 3ecc0194
- 00b6b068 ["INT_ADD", "register:40f0:8", ["const:b6b068:8", "const:4:8"]]
- 00b6b068 ["CALL", null, ["callee:0056681c:8"]]
+ 00b6b0ac ["INT_ADD", "register:40f0:8", ["const:b6b0ac:8", "const:4:8"]]
+ 00b6b0ac ["CALL", null, ["callee:0056681c:8"]]
- 00b6b068 bytes edede797
+ 00b6b0ac bytes dcede797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f02e6215681df3c71a612d7e7780e87"></a>

### [`00b6b094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md) → [`00b6b0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6b0f0",
      "incomplete_value": true,
      "site": "00b6b0f4",
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
      "definition_site": "00b6b0ac",
      "incomplete_value": true,
      "site": "00b6b0b0",
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
      "definition_site": "00b6b108",
      "incomplete_value": false,
      "site": "00b6b10c",
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
      "definition_site": "00b6b0c4",
      "incomplete_value": false,
      "site": "00b6b0c8",
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
      "definition_site": "00b6b120",
      "incomplete_value": true,
      "site": "00b6b12c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b0dc",
      "incomplete_value": true,
      "site": "00b6b0e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6b0e8",
      "READ",
      [
        "storage",
        "00c1bbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b0f4",
      "DATA",
      [
        "storage",
        "00c12748",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b108",
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
      "00b6b0e8",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b0f4",
      "DATA",
      [
        "storage",
        "00c12798",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b108",
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

- 旧版 [`00b6b0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0a4) · [`00b6b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0c8) · [`00b6b0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0e8)
- 新版 [`00b6b0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b0e8) · [`00b6b10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b10c) · [`00b6b12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b0d8.md#insn-00b6b12c)

~~~diff
- 00b6b0a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
- 00b6b0a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6b0e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
+ 00b6b0e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6b0a4 bytes 08e145f9
+ 00b6b0e8 bytes 080946f9
- 00b6b0c8 ["INT_ADD", "register:40f0:8", ["const:b6b0c8:8", "const:4:8"]]
- 00b6b0c8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b10c ["INT_ADD", "register:40f0:8", ["const:b6b10c:8", "const:4:8"]]
+ 00b6b10c ["CALL", null, ["callee:00bde180:8"]]
- 00b6b0c8 bytes 1acc0194
+ 00b6b10c bytes 1dcc0194
- 00b6b0e8 ["INT_ADD", "register:40f0:8", ["const:b6b0e8:8", "const:4:8"]]
- 00b6b0e8 ["CALL", null, ["callee:00551e14:8"]]
+ 00b6b12c ["INT_ADD", "register:40f0:8", ["const:b6b12c:8", "const:4:8"]]
+ 00b6b12c ["CALL", null, ["callee:00551e14:8"]]
- 00b6b0e8 bytes 4b9be797
+ 00b6b12c bytes 3a9be797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6408ccdb52bf4296d7d57b303f8ffc"></a>

### [`00b6b12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md) → [`00b6b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b1dc",
      "incomplete_value": true,
      "site": "00b6b1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6b198",
      "incomplete_value": true,
      "site": "00b6b1b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b1e8",
      "incomplete_value": true,
      "site": "00b6b1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b1a4",
      "incomplete_value": true,
      "site": "00b6b1b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
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
      "definition_site": "00b6b284",
      "incomplete_value": true,
      "site": "00b6b290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b240",
      "incomplete_value": true,
      "site": "00b6b24c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
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
      "00b6b1dc",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1e8",
      "READ",
      [
        "storage",
        "010a1840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b284",
      "READ",
      [
        "storage",
        "010a1858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6b1dc",
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1e8",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b284",
      "READ",
      [
        "storage",
        "010a1898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b1b0) · [`00b6b1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b1f4) · [`00b6b208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b208)
- 新版 [`00b6b1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b1f4) · [`00b6b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b238) · [`00b6b24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b170.md#insn-00b6b24c)

~~~diff
- 00b6b1b0 ["INT_ADD", "register:40f0:8", ["const:b6b1b0:8", "const:4:8"]]
- 00b6b1b0 ["CALL", null, ["callee:0056681c:8"]]
+ 00b6b1f4 ["INT_ADD", "register:40f0:8", ["const:b6b1f4:8", "const:4:8"]]
+ 00b6b1f4 ["CALL", null, ["callee:0056681c:8"]]
- 00b6b1b0 bytes 9bede797
+ 00b6b1f4 bytes 8aede797
- 00b6b1f4 ["INT_ADD", "register:40f0:8", ["const:b6b1f4:8", "const:4:8"]]
- 00b6b1f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b238 ["INT_ADD", "register:40f0:8", ["const:b6b238:8", "const:4:8"]]
+ 00b6b238 ["CALL", null, ["callee:00bde180:8"]]
- 00b6b1f4 bytes cfcb0194
+ 00b6b238 bytes d2cb0194
- 00b6b208 ["INT_ADD", "register:40f0:8", ["const:b6b208:8", "const:4:8"]]
- 00b6b208 ["CALL", null, ["callee:00bde740:8"]]
+ 00b6b24c ["INT_ADD", "register:40f0:8", ["const:b6b24c:8", "const:4:8"]]
+ 00b6b24c ["CALL", null, ["callee:00bde740:8"]]
- 00b6b208 bytes 3acd0194
+ 00b6b24c bytes 3dcd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccfda0989dbd1733a225806f9ab65629"></a>

### [`00b6b64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md) → [`00b6b690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b708",
      "incomplete_value": true,
      "site": "00b6b720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6b6c4",
      "incomplete_value": true,
      "site": "00b6b6dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b70c",
      "incomplete_value": true,
      "site": "00b6b720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b6c8",
      "incomplete_value": true,
      "site": "00b6b6dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b778",
      "incomplete_value": false,
      "site": "00b6b77c",
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
      "definition_site": "00b6b734",
      "incomplete_value": false,
      "site": "00b6b738",
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
      "00b6b6b8",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6b708",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b70c",
      "READ",
      [
        "storage",
        "010a18a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6b6b8",
      "READ",
      [
        "storage",
        "010a19f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6b708",
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b70c",
      "READ",
      [
        "storage",
        "010a18e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b6dc) · [`00b6b738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b738) · [`00b6b7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b7a0)
- 新版 [`00b6b720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b720) · [`00b6b77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b77c) · [`00b6b7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b690.md#insn-00b6b7e4)

~~~diff
- 00b6b6dc ["INT_ADD", "register:40f0:8", ["const:b6b6dc:8", "const:4:8"]]
- 00b6b6dc ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6b720 ["INT_ADD", "register:40f0:8", ["const:b6b720:8", "const:4:8"]]
+ 00b6b720 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6b6dc bytes 85c90194
+ 00b6b720 bytes 88c90194
- 00b6b738 ["INT_ADD", "register:40f0:8", ["const:b6b738:8", "const:4:8"]]
- 00b6b738 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b77c ["INT_ADD", "register:40f0:8", ["const:b6b77c:8", "const:4:8"]]
+ 00b6b77c ["CALL", null, ["callee:00bde180:8"]]
- 00b6b738 bytes 7eca0194
+ 00b6b77c bytes 81ca0194
- 00b6b7a0 ["INT_ADD", "register:40f0:8", ["const:b6b7a0:8", "const:4:8"]]
- 00b6b7a0 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b6b7e4 ["INT_ADD", "register:40f0:8", ["const:b6b7e4:8", "const:4:8"]]
+ 00b6b7e4 ["CALL", null, ["callee:00bdde40:8"]]
- 00b6b7a0 bytes 94c90194
+ 00b6b7e4 bytes 97c90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3d518b9638747312ae5213f0431528"></a>

### [`00b6b868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md) → [`00b6b8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b8ec",
      "incomplete_value": false,
      "site": "00b6b8f0",
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
      "definition_site": "00b6b8a8",
      "incomplete_value": false,
      "site": "00b6b8ac",
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
      "00b6b8ec",
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
      "00b6b8ec",
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

- 旧版 [`00b6b8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b8ac) · [`00b6b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b898) · [`00b6b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b8a8)
- 新版 [`00b6b8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b8f0) · [`00b6b8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b8dc) · [`00b6b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md#insn-00b6b8ec)

~~~diff
- 00b6b8ac ["INT_ADD", "register:40f0:8", ["const:b6b8ac:8", "const:4:8"]]
- 00b6b8ac ["CALL", null, ["callee:00bde180:8"]]
+ 00b6b8f0 ["INT_ADD", "register:40f0:8", ["const:b6b8f0:8", "const:4:8"]]
+ 00b6b8f0 ["CALL", null, ["callee:00bde180:8"]]
- 00b6b8ac bytes 21ca0194
+ 00b6b8f0 bytes 24ca0194
- 00b6b898 ["INT_ADD", "register:40f0:8", ["const:b6b898:8", "const:4:8"]]
- 00b6b898 ["CALL", null, ["callee:00bde3e0:8"]]
+ 00b6b8dc ["INT_ADD", "register:40f0:8", ["const:b6b8dc:8", "const:4:8"]]
+ 00b6b8dc ["CALL", null, ["callee:00bde3e0:8"]]
- 00b6b898 bytes beca0194
+ 00b6b8dc bytes c1ca0194
- 00b6b8a8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b6b8a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6b8a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6b8a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6b8ec ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b6b8ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6b8ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6b8ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6b8a8 bytes 00303991
+ 00b6b8ec bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85df31a8ea851f32fe64a6aa15f71229"></a>

### [`00b6ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6ba04.md) → [`00b6ba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

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
      "definition_site": "00b6baf0",
      "incomplete_value": false,
      "site": "00b6baf4",
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
      "definition_site": "00b6baac",
      "incomplete_value": false,
      "site": "00b6bab0",
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
      "00b6baf0",
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
      "00b6baf0",
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

- 旧版 [`00b6bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6ba04.md#insn-00b6bab0) · [`00b6ba3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6ba04.md#insn-00b6ba3c) · [`00b6ba50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6ba04.md#insn-00b6ba50)
- 新版 [`00b6baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6baf4) · [`00b6ba80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6ba80) · [`00b6ba94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6ba48.md#insn-00b6ba94)

~~~diff
- 00b6bab0 ["INT_ADD", "register:40f0:8", ["const:b6bab0:8", "const:4:8"]]
- 00b6bab0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6baf4 ["INT_ADD", "register:40f0:8", ["const:b6baf4:8", "const:4:8"]]
+ 00b6baf4 ["CALL", null, ["callee:00bde180:8"]]
- 00b6bab0 bytes a0c90194
+ 00b6baf4 bytes a3c90194
- 00b6ba3c ["INT_ADD", "register:40f0:8", ["const:b6ba3c:8", "const:4:8"]]
- 00b6ba3c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6ba80 ["INT_ADD", "register:40f0:8", ["const:b6ba80:8", "const:4:8"]]
+ 00b6ba80 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6ba3c bytes 6dbd0194
+ 00b6ba80 bytes 70bd0194
- 00b6ba50 ["INT_ADD", "register:40f0:8", ["const:b6ba50:8", "const:4:8"]]
- 00b6ba50 ["CALL", null, ["callee:00be0e40:8"]]
+ 00b6ba94 ["INT_ADD", "register:40f0:8", ["const:b6ba94:8", "const:4:8"]]
+ 00b6ba94 ["CALL", null, ["callee:00be0e40:8"]]
- 00b6ba50 bytes e8d40194
+ 00b6ba94 bytes ebd40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-390eb0956d2f1cc41cdbc674a631fc32"></a>

### [`00b6c2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md) → [`00b6c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md) FUN_00b6c310

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00b6bf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bf28.md) [`00b6c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c50c.md) [`00b6c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c7e4.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0e0.md)
- 新版 呼出元 3件 [`00b6bf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf6c.md) [`00b6c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c550.md) [`00b6c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c828.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6c36c",
      "incomplete_value": true,
      "site": "00b6c384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6c328",
      "incomplete_value": true,
      "site": "00b6c340",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6c370",
      "incomplete_value": true,
      "site": "00b6c384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c32c",
      "incomplete_value": true,
      "site": "00b6c340",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
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
      "definition_site": "00b6c3e4",
      "incomplete_value": true,
      "site": "00b6c3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c3a0",
      "incomplete_value": true,
      "site": "00b6c3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6c36c",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c370",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c3e4",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6c36c",
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c370",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c3e4",
      "READ",
      [
        "storage",
        "010a1910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c2fc) · [`00b6c340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c340) · [`00b6c3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c3b0)
- 新版 [`00b6c340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c340) · [`00b6c384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c384) · [`00b6c3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c310.md#insn-00b6c3f4)

~~~diff
- 00b6c2fc ["INT_ADD", "register:40f0:8", ["const:b6c2fc:8", "const:4:8"]]
- 00b6c2fc ["CALL", null, ["callee:00bde200:8"]]
+ 00b6c340 ["INT_ADD", "register:40f0:8", ["const:b6c340:8", "const:4:8"]]
+ 00b6c340 ["CALL", null, ["callee:00bde200:8"]]
- 00b6c2fc bytes adc70194
+ 00b6c340 bytes b0c70194
- 00b6c340 ["INT_ADD", "register:40f0:8", ["const:b6c340:8", "const:4:8"]]
- 00b6c340 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b6c384 ["INT_ADD", "register:40f0:8", ["const:b6c384:8", "const:4:8"]]
+ 00b6c384 ["CALL", null, ["callee:00bddd40:8"]]
- 00b6c340 bytes 6cc60194
+ 00b6c384 bytes 6fc60194
- 00b6c3b0 ["INT_ADD", "register:40f0:8", ["const:b6c3b0:8", "const:4:8"]]
- 00b6c3b0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6c3f4 ["INT_ADD", "register:40f0:8", ["const:b6c3f4:8", "const:4:8"]]
+ 00b6c3f4 ["CALL", null, ["callee:0047495c:8"]]
- 00b6c3b0 bytes 6b21e497
+ 00b6c3f4 bytes 5a21e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-402303c9cd3abadbf38d08f642b39726"></a>

### [`00b6cae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md) → [`00b6cb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d80.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0dd0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b6cb90",
      "incomplete_value": false,
      "site": "00b6cb94",
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
    "old": {
      "definition_site": "00b6cb4c",
      "incomplete_value": false,
      "site": "00b6cb50",
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
            "const:4f4:8"
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
      "00b6cb90",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6cb90",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb50) · [`00b6cb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb94) · [`00b6cb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb14)
- 新版 [`00b6cb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md#insn-00b6cb94) · [`00b6cbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md#insn-00b6cbd8) · [`00b6cb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6cb2c.md#insn-00b6cb58)

~~~diff
- 00b6cb50 ["INT_ADD", "register:40f0:8", ["const:b6cb50:8", "const:4:8"]]
- 00b6cb50 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6cb94 ["INT_ADD", "register:40f0:8", ["const:b6cb94:8", "const:4:8"]]
+ 00b6cb94 ["CALL", null, ["callee:00bde180:8"]]
- 00b6cb50 bytes 78c50194
+ 00b6cb94 bytes 7bc50194
- 00b6cb94 ["INT_ADD", "register:40f0:8", ["const:b6cb94:8", "const:4:8"]]
- 00b6cb94 ["CALL", null, ["callee:00bde010:8"]]
+ 00b6cbd8 ["INT_ADD", "register:40f0:8", ["const:b6cbd8:8", "const:4:8"]]
+ 00b6cbd8 ["CALL", null, ["callee:00bde010:8"]]
- 00b6cb94 bytes 0bc50194
+ 00b6cbd8 bytes 0ec50194
- 00b6cb14 ["INT_ADD", "register:40f0:8", ["const:b6cb14:8", "const:4:8"]]
- 00b6cb14 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b6cb58 ["INT_ADD", "register:40f0:8", ["const:b6cb58:8", "const:4:8"]]
+ 00b6cb58 ["CALL", null, ["callee:00bddc20:8"]]
- 00b6cb14 bytes 2fc40194
+ 00b6cb58 bytes 32c40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5877c9fec5771cfe772e0927df19f620"></a>

### [`00b6d2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md) → [`00b6d330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d70.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0dc0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b6d39c",
      "incomplete_value": false,
      "site": "00b6d3a0",
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
    "old": {
      "definition_site": "00b6d358",
      "incomplete_value": false,
      "site": "00b6d35c",
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
            "const:4f4:8"
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
      "00b6d39c",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6d39c",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d35c) · [`00b6d320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d320) · [`00b6d32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d32c)
- 新版 [`00b6d3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d3a0) · [`00b6d364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d364) · [`00b6d370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d330.md#insn-00b6d370)

~~~diff
- 00b6d35c ["INT_ADD", "register:40f0:8", ["const:b6d35c:8", "const:4:8"]]
- 00b6d35c ["CALL", null, ["callee:00bde180:8"]]
+ 00b6d3a0 ["INT_ADD", "register:40f0:8", ["const:b6d3a0:8", "const:4:8"]]
+ 00b6d3a0 ["CALL", null, ["callee:00bde180:8"]]
- 00b6d35c bytes 75c30194
+ 00b6d3a0 bytes 78c30194
- 00b6d320 ["INT_ADD", "register:40f0:8", ["const:b6d320:8", "const:4:8"]]
- 00b6d320 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b6d364 ["INT_ADD", "register:40f0:8", ["const:b6d364:8", "const:4:8"]]
+ 00b6d364 ["CALL", null, ["callee:00bddc20:8"]]
- 00b6d320 bytes 2cc20194
+ 00b6d364 bytes 2fc20194
- 00b6d32c ["INT_ADD", "register:40f0:8", ["const:b6d32c:8", "const:4:8"]]
- 00b6d32c ["CALL", null, ["callee:00bde000:8"]]
+ 00b6d370 ["INT_ADD", "register:40f0:8", ["const:b6d370:8", "const:4:8"]]
+ 00b6d370 ["CALL", null, ["callee:00bde000:8"]]
- 00b6d32c bytes 21c30194
+ 00b6d370 bytes 24c30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da3df706827caccc05d67de97c6e53c"></a>

### [`00b6d4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md) → [`00b6d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6d51c",
      "incomplete_value": true,
      "site": "00b6d51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d4d8",
      "incomplete_value": true,
      "site": "00b6d4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d504",
      "incomplete_value": true,
      "site": "00b6d504",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d4c0",
      "incomplete_value": true,
      "site": "00b6d4c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d4c0"
      ],
      [
        "FALL_THROUGH",
        "00b6d504"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d504",
      "incomplete_value": true,
      "site": "00b6d51c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d4c0",
      "incomplete_value": true,
      "site": "00b6d4d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d500",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d51c",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d500",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d51c",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4d8) · [`00b6d4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4bc) · [`00b6d4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4d0)
- 新版 [`00b6d51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d51c) · [`00b6d500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d500) · [`00b6d514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d4f0.md#insn-00b6d514)

~~~diff
- 00b6d4d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d51c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d51c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d4d8 bytes 60de04f9
+ 00b6d51c bytes 60fe04f9
- 00b6d4bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d4bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d500 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d500 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d4bc bytes 68de44f9
+ 00b6d500 bytes 68fe44f9
- 00b6d4d0 ["INT_ADD", "register:40f0:8", ["const:b6d4d0:8", "const:4:8"]]
- 00b6d4d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d514 ["INT_ADD", "register:40f0:8", ["const:b6d514:8", "const:4:8"]]
+ 00b6d514 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d4d0 bytes dcc20194
+ 00b6d514 bytes dfc20194
~~~


<a id="compare-17a1a9ef370d4ab5293b4e23b46646a7"></a>

### [`00b6d4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md) → [`00b6d530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6d55c",
      "incomplete_value": true,
      "site": "00b6d55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d518",
      "incomplete_value": true,
      "site": "00b6d518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d544",
      "incomplete_value": true,
      "site": "00b6d544",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d500",
      "incomplete_value": true,
      "site": "00b6d500",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d500"
      ],
      [
        "FALL_THROUGH",
        "00b6d544"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d544",
      "incomplete_value": true,
      "site": "00b6d55c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d500",
      "incomplete_value": true,
      "site": "00b6d518",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d540",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d55c",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d540",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d55c",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md#insn-00b6d518) · [`00b6d4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md#insn-00b6d4fc) · [`00b6d510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md#insn-00b6d510)
- 新版 [`00b6d55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d55c) · [`00b6d540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d540) · [`00b6d554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d530.md#insn-00b6d554)

~~~diff
- 00b6d518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d55c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d55c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d518 bytes 60de04f9
+ 00b6d55c bytes 60fe04f9
- 00b6d4fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d4fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d540 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d4fc bytes 68de44f9
+ 00b6d540 bytes 68fe44f9
- 00b6d510 ["INT_ADD", "register:40f0:8", ["const:b6d510:8", "const:4:8"]]
- 00b6d510 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d554 ["INT_ADD", "register:40f0:8", ["const:b6d554:8", "const:4:8"]]
+ 00b6d554 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d510 bytes ccc20194
+ 00b6d554 bytes cfc20194
~~~


<a id="compare-347b7af046d6a772d19c48eec9e65a33"></a>

### [`00b6d52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md) → [`00b6d570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6d5a0",
      "incomplete_value": true,
      "site": "00b6d5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d55c",
      "incomplete_value": true,
      "site": "00b6d55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d540",
      "incomplete_value": true,
      "site": "00b6d540",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d540"
      ],
      [
        "FALL_THROUGH",
        "00b6d584"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d5a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d540",
      "incomplete_value": true,
      "site": "00b6d55c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d580",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d5a0",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d580",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d5a0",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d55c) · [`00b6d53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d53c) · [`00b6d554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d554)
- 新版 [`00b6d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d5a0) · [`00b6d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d580) · [`00b6d598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d570.md#insn-00b6d598)

~~~diff
- 00b6d55c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d55c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d55c bytes 60de04f9
+ 00b6d5a0 bytes 60fe04f9
- 00b6d53c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d53c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d53c bytes 68de44f9
+ 00b6d580 bytes 68fe44f9
- 00b6d554 ["INT_ADD", "register:40f0:8", ["const:b6d554:8", "const:4:8"]]
- 00b6d554 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
+ 00b6d598 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d554 bytes bbc20194
+ 00b6d598 bytes bec20194
~~~


<a id="compare-7ba41fd72340bb9f0328631c577ce1ea"></a>

### [`00b6d570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md) → [`00b6d5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6d5e4",
      "incomplete_value": true,
      "site": "00b6d5e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d5a0",
      "incomplete_value": true,
      "site": "00b6d5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d5c8",
      "incomplete_value": true,
      "site": "00b6d5c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d584"
      ],
      [
        "FALL_THROUGH",
        "00b6d5c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d5c8",
      "incomplete_value": true,
      "site": "00b6d5e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d5a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d5c4",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d5e4",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d5c4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d5e4",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d5a0) · [`00b6d580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d580) · [`00b6d598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d598)
- 新版 [`00b6d5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5e4) · [`00b6d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5c4) · [`00b6d5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d5b4.md#insn-00b6d5dc)

~~~diff
- 00b6d5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d5e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d5e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d5a0 bytes 60de04f9
+ 00b6d5e4 bytes 60fe04f9
- 00b6d580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 00b6d580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d5c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
+ 00b6d5c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d580 bytes 68de44f9
+ 00b6d5c4 bytes 68fe44f9
- 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
- 00b6d598 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d5dc ["INT_ADD", "register:40f0:8", ["const:b6d5dc:8", "const:4:8"]]
+ 00b6d5dc ["CALL", null, ["callee:00bde090:8"]]
- 00b6d598 bytes aac20194
+ 00b6d5dc bytes adc20194
~~~


<a id="compare-76505de588ac66ab3876d69b3b9924bd"></a>

### [`00b6d5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md) → [`00b6d604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6d65c",
      "incomplete_value": true,
      "site": "00b6d65c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d618",
      "incomplete_value": true,
      "site": "00b6d618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "definition_site": "00b6d638",
      "incomplete_value": true,
      "site": "00b6d644",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d5f4",
      "incomplete_value": true,
      "site": "00b6d600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b8:8"
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
      "00b6d618",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d638",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d65c",
      "WRITE",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d618",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d638",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d65c",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d5d4) · [`00b6d600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d600) · [`00b6d618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d618)
- 新版 [`00b6d618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d618) · [`00b6d644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d644) · [`00b6d65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d604.md#insn-00b6d65c)

~~~diff
- 00b6d5d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9c0:8"]]
- 00b6d5d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6d5d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6d618 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a00:8"]]
+ 00b6d618 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d618 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6d5d4 bytes a8026739
+ 00b6d618 bytes a8026839
- 00b6d600 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d600 ["INT_ADD", "register:40f0:8", ["const:b6d600:8", "const:4:8"]]
- 00b6d600 ["CALLIND", null, ["register:0:8"]]
+ 00b6d644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d644 ["INT_ADD", "register:40f0:8", ["const:b6d644:8", "const:4:8"]]
+ 00b6d644 ["CALLIND", null, ["register:0:8"]]
- 00b6d600 bytes 00013fd6
+ 00b6d644 bytes 00013fd6
- 00b6d618 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d618 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9c0:8"]]
- 00b6d618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6d65c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6d65c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a00:8"]]
+ 00b6d65c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d618 bytes a0022739
+ 00b6d65c bytes a0022839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d59761df86fbcdfde624979c44a1b67"></a>

### [`00b6d62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md) → [`00b6d670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6d6ac",
      "incomplete_value": true,
      "site": "00b6d6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d668",
      "incomplete_value": true,
      "site": "00b6d668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "definition_site": "00b6d6cc",
      "incomplete_value": true,
      "site": "00b6d6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d688",
      "incomplete_value": true,
      "site": "00b6d688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d688",
      "incomplete_value": true,
      "site": "00b6d688",
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
      "definition_site": "00b6d644",
      "incomplete_value": true,
      "site": "00b6d644",
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
      "00b6d684",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d690",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d6ac",
      "WRITE",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d684",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d690",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d6ac",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d640) · [`00b6d668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d668) · [`00b6d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d684)
- 新版 [`00b6d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d684) · [`00b6d6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d6ac) · [`00b6d6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d670.md#insn-00b6d6c8)

~~~diff
- 00b6d640 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6d640 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6d684 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d640 bytes 81de44f9
+ 00b6d684 bytes 81fe44f9
- 00b6d668 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d668 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d668 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9c0:8"]]
- 00b6d668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6d6ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6d6ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6d6ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a00:8"]]
+ 00b6d6ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d668 bytes bf022739
+ 00b6d6ac bytes bf022839
- 00b6d684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d684 ["INT_ADD", "register:40f0:8", ["const:b6d684:8", "const:4:8"]]
- 00b6d684 ["CALLIND", null, ["register:0:8"]]
+ 00b6d6c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d6c8 ["INT_ADD", "register:40f0:8", ["const:b6d6c8:8", "const:4:8"]]
+ 00b6d6c8 ["CALLIND", null, ["register:0:8"]]
- 00b6d684 bytes 00013fd6
+ 00b6d6c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3e983bf1952852218cc0eabc86dc412"></a>

### [`00b6d69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md) → [`00b6d6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6d720",
      "incomplete_value": true,
      "site": "00b6d720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6dc",
      "incomplete_value": true,
      "site": "00b6d6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d6fc",
      "incomplete_value": true,
      "site": "00b6d6fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6b8",
      "incomplete_value": true,
      "site": "00b6d6b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d6b8"
      ],
      [
        "FALL_THROUGH",
        "00b6d6fc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d6fc",
      "incomplete_value": true,
      "site": "00b6d720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6b8",
      "incomplete_value": true,
      "site": "00b6d6dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d6f4",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d720",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d734",
      "PARAM",
      [
        "storage",
        "00c127e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6d6f4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d720",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d734",
      "PARAM",
      [
        "storage",
        "00c12838",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md#insn-00b6d6dc) · [`00b6d6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md#insn-00b6d6b0) · [`00b6d6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md#insn-00b6d6d4)
- 新版 [`00b6d720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d720) · [`00b6d6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d6f4) · [`00b6d718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md#insn-00b6d718)

~~~diff
- 00b6d6dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6d6dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6d720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d6dc bytes 80de04f9
+ 00b6d720 bytes 80fe04f9
- 00b6d6b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6d6b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d6f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6d6f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d6b0 bytes 81de44f9
+ 00b6d6f4 bytes 81fe44f9
- 00b6d6d4 ["INT_ADD", "register:40f0:8", ["const:b6d6d4:8", "const:4:8"]]
- 00b6d6d4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d718 ["INT_ADD", "register:40f0:8", ["const:b6d718:8", "const:4:8"]]
+ 00b6d718 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d6d4 bytes 5bc20194
+ 00b6d718 bytes 5ec20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ea2dd91ce2219f6736ece81b6b2699"></a>

### [`00b6d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d70c.md) → [`00b6d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6d76c",
      "incomplete_value": false,
      "site": "00b6d770",
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
      "definition_site": "00b6d728",
      "incomplete_value": false,
      "site": "00b6d72c",
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
      "definition_site": "00b6d77c",
      "incomplete_value": true,
      "site": "00b6d788",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6d738",
      "incomplete_value": true,
      "site": "00b6d744",
      "value": [
        "LOAD",
        "8",
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
      "00b6d76c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6d77c",
      "DATA",
      [
        "storage",
        "010a19c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d76c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6d77c",
      "DATA",
      [
        "storage",
        "010a1a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d70c.md#insn-00b6d72c) · [`00b6d728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d70c.md#insn-00b6d728) · [`00b6d734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d70c.md#insn-00b6d734)
- 新版 [`00b6d770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d770) · [`00b6d76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d76c) · [`00b6d778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d750.md#insn-00b6d778)

~~~diff
- 00b6d72c ["INT_ADD", "register:40f0:8", ["const:b6d72c:8", "const:4:8"]]
- 00b6d72c ["CALL", null, ["callee:00bde180:8"]]
+ 00b6d770 ["INT_ADD", "register:40f0:8", ["const:b6d770:8", "const:4:8"]]
+ 00b6d770 ["CALL", null, ["callee:00bde180:8"]]
- 00b6d72c bytes 81c20194
+ 00b6d770 bytes 84c20194
- 00b6d728 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6d728 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d728 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d728 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6d76c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6d76c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d76c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d76c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6d728 bytes 00501791
+ 00b6d76c bytes 001c1591
- 00b6d734 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00b6d734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6d778 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00b6d778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6d734 bytes 08212791
+ 00b6d778 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976511ee4af2403133caea4c50ff9471"></a>

### [`00b6d748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md) → [`00b6d78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6d7cc",
      "incomplete_value": true,
      "site": "00b6d7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d788",
      "incomplete_value": true,
      "site": "00b6d788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6d7a8",
      "incomplete_value": true,
      "site": "00b6d7a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d764",
      "incomplete_value": true,
      "site": "00b6d764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6d764"
      ],
      [
        "FALL_THROUGH",
        "00b6d7a8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6d7a8",
      "incomplete_value": true,
      "site": "00b6d7cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d764",
      "incomplete_value": true,
      "site": "00b6d788",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6d7a0",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d7cc",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d7e4",
      "PARAM",
      [
        "storage",
        "010a19d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d7a0",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d7cc",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d7e4",
      "PARAM",
      [
        "storage",
        "010a1a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d788) · [`00b6d75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d75c) · [`00b6d780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d780)
- 新版 [`00b6d7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7cc) · [`00b6d7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7a0) · [`00b6d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md#insn-00b6d7c4)

~~~diff
- 00b6d788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6d788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6d7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d788 bytes 80de04f9
+ 00b6d7cc bytes 80fe04f9
- 00b6d75c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6d75c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d7a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6d7a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d75c bytes 81de44f9
+ 00b6d7a0 bytes 81fe44f9
- 00b6d780 ["INT_ADD", "register:40f0:8", ["const:b6d780:8", "const:4:8"]]
- 00b6d780 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d7c4 ["INT_ADD", "register:40f0:8", ["const:b6d7c4:8", "const:4:8"]]
+ 00b6d7c4 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d780 bytes 30c20194
+ 00b6d7c4 bytes 33c20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb536050fa81d89ae967513959b32b7d"></a>

### [`00b6d7b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md) → [`00b6d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6d818",
      "incomplete_value": false,
      "site": "00b6d81c",
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
      "definition_site": "00b6d7d4",
      "incomplete_value": false,
      "site": "00b6d7d8",
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
      "definition_site": "00b6d828",
      "incomplete_value": true,
      "site": "00b6d834",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6d7e4",
      "incomplete_value": true,
      "site": "00b6d7f0",
      "value": [
        "LOAD",
        "8",
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
      "00b6d818",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6d828",
      "DATA",
      [
        "storage",
        "010a19d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d818",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6d828",
      "DATA",
      [
        "storage",
        "010a1a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7d8) · [`00b6d7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7d4) · [`00b6d7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7e0)
- 新版 [`00b6d81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d81c) · [`00b6d818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d818) · [`00b6d824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md#insn-00b6d824)

~~~diff
- 00b6d7d8 ["INT_ADD", "register:40f0:8", ["const:b6d7d8:8", "const:4:8"]]
- 00b6d7d8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6d81c ["INT_ADD", "register:40f0:8", ["const:b6d81c:8", "const:4:8"]]
+ 00b6d81c ["CALL", null, ["callee:00bde180:8"]]
- 00b6d7d8 bytes 56c20194
+ 00b6d81c bytes 59c20194
- 00b6d7d4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6d7d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d7d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d7d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6d818 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6d818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6d7d4 bytes 00fc1991
+ 00b6d818 bytes 00c81791
- 00b6d7e0 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00b6d7e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d7e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6d824 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00b6d824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6d7e0 bytes 08412791
+ 00b6d824 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1614e73fcd74ef9a8176b8281a633aa"></a>

### [`00b6d7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md) → [`00b6d838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00b6d864",
      "incomplete_value": true,
      "site": "00b6d864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d820",
      "incomplete_value": true,
      "site": "00b6d820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6d84c",
      "incomplete_value": true,
      "site": "00b6d84c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d808",
      "incomplete_value": true,
      "site": "00b6d808",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d858",
      "incomplete_value": false,
      "site": "00b6d85c",
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
      "definition_site": "00b6d814",
      "incomplete_value": false,
      "site": "00b6d818",
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
      "00b6d848",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d858",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d864",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d848",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d858",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d864",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d818) · [`00b6d820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d820) · [`00b6d804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d804)
- 新版 [`00b6d85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d85c) · [`00b6d864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d864) · [`00b6d848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d838.md#insn-00b6d848)

~~~diff
- 00b6d818 ["INT_ADD", "register:40f0:8", ["const:b6d818:8", "const:4:8"]]
- 00b6d818 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d85c ["INT_ADD", "register:40f0:8", ["const:b6d85c:8", "const:4:8"]]
+ 00b6d85c ["CALL", null, ["callee:00bde090:8"]]
- 00b6d818 bytes 0ac20194
+ 00b6d85c bytes 0dc20194
- 00b6d820 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d820 bytes 60ee04f9
+ 00b6d864 bytes 600e05f9
- 00b6d804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d848 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d848 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d804 bytes 68ee44f9
+ 00b6d848 bytes 680e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1051de46c026d085ef755b379abb9472"></a>

### [`00b6d834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md) → [`00b6d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6d8a4",
      "incomplete_value": true,
      "site": "00b6d8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d860",
      "incomplete_value": true,
      "site": "00b6d860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6d88c",
      "incomplete_value": true,
      "site": "00b6d88c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d848",
      "incomplete_value": true,
      "site": "00b6d848",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d894",
      "incomplete_value": false,
      "site": "00b6d89c",
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
      "definition_site": "00b6d850",
      "incomplete_value": false,
      "site": "00b6d858",
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
      "00b6d888",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d894",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d8a4",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d888",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d894",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d8a4",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d858) · [`00b6d860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d860) · [`00b6d844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d844)
- 新版 [`00b6d89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d89c) · [`00b6d8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d8a4) · [`00b6d888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d878.md#insn-00b6d888)

~~~diff
- 00b6d858 ["INT_ADD", "register:40f0:8", ["const:b6d858:8", "const:4:8"]]
- 00b6d858 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d89c ["INT_ADD", "register:40f0:8", ["const:b6d89c:8", "const:4:8"]]
+ 00b6d89c ["CALL", null, ["callee:00bde090:8"]]
- 00b6d858 bytes fac10194
+ 00b6d89c bytes fdc10194
- 00b6d860 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d8a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d860 bytes 60ee04f9
+ 00b6d8a4 bytes 600e05f9
- 00b6d844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d844 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d844 bytes 68ee44f9
+ 00b6d888 bytes 680e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cce1f6775de6874afbb751a77ab059c5"></a>

### [`00b6d874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md) → [`00b6d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6d8e8",
      "incomplete_value": true,
      "site": "00b6d8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d8a4",
      "incomplete_value": true,
      "site": "00b6d8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6d8cc",
      "incomplete_value": true,
      "site": "00b6d8cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d888",
      "incomplete_value": true,
      "site": "00b6d888",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d8d8",
      "incomplete_value": false,
      "site": "00b6d8e0",
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
      "definition_site": "00b6d894",
      "incomplete_value": false,
      "site": "00b6d89c",
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
      "00b6d8c8",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d8d8",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d8e8",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d8c8",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d8d8",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d8e8",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md#insn-00b6d89c) · [`00b6d8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md#insn-00b6d8a4) · [`00b6d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md#insn-00b6d884)
- 新版 [`00b6d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8e0) · [`00b6d8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8e8) · [`00b6d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8b8.md#insn-00b6d8c8)

~~~diff
- 00b6d89c ["INT_ADD", "register:40f0:8", ["const:b6d89c:8", "const:4:8"]]
- 00b6d89c ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d8e0 ["INT_ADD", "register:40f0:8", ["const:b6d8e0:8", "const:4:8"]]
+ 00b6d8e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d89c bytes e9c10194
+ 00b6d8e0 bytes ecc10194
- 00b6d8a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d8a4 bytes 60ee04f9
+ 00b6d8e8 bytes 600e05f9
- 00b6d884 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d8c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d8c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d884 bytes 68ee44f9
+ 00b6d8c8 bytes 680e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0bff58ae05af70153570830d5c59f33"></a>

### [`00b6d8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md) → [`00b6d8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6d92c",
      "incomplete_value": true,
      "site": "00b6d92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d8e8",
      "incomplete_value": true,
      "site": "00b6d8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6d910",
      "incomplete_value": true,
      "site": "00b6d910",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d8cc",
      "incomplete_value": true,
      "site": "00b6d8cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6d918",
      "incomplete_value": false,
      "site": "00b6d924",
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
      "definition_site": "00b6d8d4",
      "incomplete_value": false,
      "site": "00b6d8e0",
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
      "00b6d90c",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d918",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d92c",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d90c",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d918",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d92c",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8e0) · [`00b6d8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8e8) · [`00b6d8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8c8)
- 新版 [`00b6d924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d924) · [`00b6d92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d92c) · [`00b6d90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md#insn-00b6d90c)

~~~diff
- 00b6d8e0 ["INT_ADD", "register:40f0:8", ["const:b6d8e0:8", "const:4:8"]]
- 00b6d8e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6d924 ["INT_ADD", "register:40f0:8", ["const:b6d924:8", "const:4:8"]]
+ 00b6d924 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d8e0 bytes d8c10194
+ 00b6d924 bytes dbc10194
- 00b6d8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d92c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d92c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d8e8 bytes 60ee04f9
+ 00b6d92c bytes 600e05f9
- 00b6d8c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b6d8c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b6d90c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d8c8 bytes 68ee44f9
+ 00b6d90c bytes 680e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09669c8238f4d9aa150fb15e19fa0c8"></a>

### [`00b6d908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md) → [`00b6d94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6d9a4",
      "incomplete_value": true,
      "site": "00b6d9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d960",
      "incomplete_value": true,
      "site": "00b6d960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "definition_site": "00b6d980",
      "incomplete_value": true,
      "site": "00b6d98c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d93c",
      "incomplete_value": true,
      "site": "00b6d948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
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
      "00b6d960",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d980",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d9a4",
      "WRITE",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d960",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d980",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d9a4",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d91c) · [`00b6d948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d948) · [`00b6d960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d960)
- 新版 [`00b6d960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d960) · [`00b6d98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d98c) · [`00b6d9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md#insn-00b6d9a4)

~~~diff
- 00b6d91c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9e0:8"]]
- 00b6d91c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6d91c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6d960 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a20:8"]]
+ 00b6d960 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d960 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6d91c bytes a8826739
+ 00b6d960 bytes a8826839
- 00b6d948 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d948 ["INT_ADD", "register:40f0:8", ["const:b6d948:8", "const:4:8"]]
- 00b6d948 ["CALLIND", null, ["register:0:8"]]
+ 00b6d98c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d98c ["INT_ADD", "register:40f0:8", ["const:b6d98c:8", "const:4:8"]]
+ 00b6d98c ["CALLIND", null, ["register:0:8"]]
- 00b6d948 bytes 00013fd6
+ 00b6d98c bytes 00013fd6
- 00b6d960 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d960 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9e0:8"]]
- 00b6d960 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6d9a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6d9a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a20:8"]]
+ 00b6d9a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d960 bytes a0822739
+ 00b6d9a4 bytes a0822839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0c28a123d51e47339334fd0e23e31c"></a>

### [`00b6d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d974.md) → [`00b6d9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d9b8.md) _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6d9f4",
      "incomplete_value": true,
      "site": "00b6d9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d9b0",
      "incomplete_value": true,
      "site": "00b6d9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "definition_site": "00b6da14",
      "incomplete_value": true,
      "site": "00b6da14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d9d0",
      "incomplete_value": true,
      "site": "00b6d9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6d9d0",
      "incomplete_value": true,
      "site": "00b6d9d0",
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
      "definition_site": "00b6d98c",
      "incomplete_value": true,
      "site": "00b6d98c",
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
      "00b6d9cc",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d9d8",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d9f4",
      "WRITE",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d9cc",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d9d8",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d9f4",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d974.md#insn-00b6d988) · [`00b6d9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d974.md#insn-00b6d9b0) · [`00b6d9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d974.md#insn-00b6d9cc)
- 新版 [`00b6d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d9b8.md#insn-00b6d9cc) · [`00b6d9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d9b8.md#insn-00b6d9f4) · [`00b6da10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d9b8.md#insn-00b6da10)

~~~diff
- 00b6d988 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d8:8"]]
- 00b6d988 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d9cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b6d9cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d988 bytes 81ee44f9
+ 00b6d9cc bytes 810e45f9
- 00b6d9b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d9b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d9b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9e0:8"]]
- 00b6d9b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6d9f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6d9f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6d9f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a20:8"]]
+ 00b6d9f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d9b0 bytes bf822739
+ 00b6d9f4 bytes bf822839
- 00b6d9cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d9cc ["INT_ADD", "register:40f0:8", ["const:b6d9cc:8", "const:4:8"]]
- 00b6d9cc ["CALLIND", null, ["register:0:8"]]
+ 00b6da10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6da10 ["INT_ADD", "register:40f0:8", ["const:b6da10:8", "const:4:8"]]
+ 00b6da10 ["CALLIND", null, ["register:0:8"]]
- 00b6d9cc bytes 00013fd6
+ 00b6da10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3266162c6fac2be9912575190b41b612"></a>

### [`00b6d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md) → [`00b6da28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b6da68",
      "incomplete_value": true,
      "site": "00b6da68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6da24",
      "incomplete_value": true,
      "site": "00b6da24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6da4c",
      "incomplete_value": false,
      "site": "00b6da60",
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
      "definition_site": "00b6da08",
      "incomplete_value": false,
      "site": "00b6da1c",
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
      "00b6da3c",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6da4c",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6da68",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6da3c",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6da4c",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6da68",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6da1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md#insn-00b6da1c) · [`00b6da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md#insn-00b6da24) · [`00b6d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md#insn-00b6d9f8)
- 新版 [`00b6da60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da60) · [`00b6da68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da68) · [`00b6da3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da28.md#insn-00b6da3c)

~~~diff
- 00b6da1c ["INT_ADD", "register:40f0:8", ["const:b6da1c:8", "const:4:8"]]
- 00b6da1c ["CALL", null, ["callee:00bde090:8"]]
+ 00b6da60 ["INT_ADD", "register:40f0:8", ["const:b6da60:8", "const:4:8"]]
+ 00b6da60 ["CALL", null, ["callee:00bde090:8"]]
- 00b6da1c bytes 89c10194
+ 00b6da60 bytes 8cc10194
- 00b6da24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d8:8"]]
- 00b6da24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6da68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b6da68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6da24 bytes 80ee04f9
+ 00b6da68 bytes 800e05f9
- 00b6d9f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d8:8"]]
- 00b6d9f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6da3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b6da3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d9f8 bytes 81ee44f9
+ 00b6da3c bytes 810e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548965f26082ae28e7284c990c8d73dc"></a>

### [`00b6da54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da54.md) → [`00b6da98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da98.md) _ZN8firebase4auth4user11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6dab4",
      "incomplete_value": false,
      "site": "00b6dab8",
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
      "definition_site": "00b6da70",
      "incomplete_value": false,
      "site": "00b6da74",
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
      "00b6dab4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6dac4",
      "DATA",
      [
        "storage",
        "010a19e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dab4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6dac4",
      "DATA",
      [
        "storage",
        "010a1a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6da74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da54.md#insn-00b6da74) · [`00b6da70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da54.md#insn-00b6da70) · [`00b6da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da54.md#insn-00b6da7c)
- 新版 [`00b6dab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da98.md#insn-00b6dab8) · [`00b6dab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da98.md#insn-00b6dab4) · [`00b6dac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6da98.md#insn-00b6dac0)

~~~diff
- 00b6da74 ["INT_ADD", "register:40f0:8", ["const:b6da74:8", "const:4:8"]]
- 00b6da74 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6dab8 ["INT_ADD", "register:40f0:8", ["const:b6dab8:8", "const:4:8"]]
+ 00b6dab8 ["CALL", null, ["callee:00bde180:8"]]
- 00b6da74 bytes afc10194
+ 00b6dab8 bytes b2c10194
- 00b6da70 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6da70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6da70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6da70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6dab4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6dab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6dab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6dab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6da70 bytes 00501791
+ 00b6dab4 bytes 001c1591
- 00b6da7c ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00b6da7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6da7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6da7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6dac0 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00b6dac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6dac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6dac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6da7c bytes 08a12791
+ 00b6dac0 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd0e64510810235602f3959cd8b3e55"></a>

### [`00b6da90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md) → [`00b6dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6db14",
      "incomplete_value": true,
      "site": "00b6db14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dad0",
      "incomplete_value": true,
      "site": "00b6dad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00b6daf0",
      "incomplete_value": true,
      "site": "00b6daf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6daac",
      "incomplete_value": true,
      "site": "00b6daac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6daf8",
      "incomplete_value": false,
      "site": "00b6db0c",
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
      "definition_site": "00b6dab4",
      "incomplete_value": false,
      "site": "00b6dac8",
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
      "00b6dae8",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6daf8",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6db14",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dae8",
      "READ",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6daf8",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6db14",
      "WRITE",
      [
        "storage",
        "010a1a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md#insn-00b6dac8) · [`00b6dad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md#insn-00b6dad0) · [`00b6daa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md#insn-00b6daa4)
- 新版 [`00b6db0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6db0c) · [`00b6db14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6db14) · [`00b6dae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md#insn-00b6dae8)

~~~diff
- 00b6dac8 ["INT_ADD", "register:40f0:8", ["const:b6dac8:8", "const:4:8"]]
- 00b6dac8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6db0c ["INT_ADD", "register:40f0:8", ["const:b6db0c:8", "const:4:8"]]
+ 00b6db0c ["CALL", null, ["callee:00bde090:8"]]
- 00b6dac8 bytes 5ec10194
+ 00b6db0c bytes 61c10194
- 00b6dad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d8:8"]]
- 00b6dad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6db14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b6db14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dad0 bytes 80ee04f9
+ 00b6db14 bytes 800e05f9
- 00b6daa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d8:8"]]
- 00b6daa4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dae8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b6dae8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6daa4 bytes 81ee44f9
+ 00b6dae8 bytes 810e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d3287ec98cfcce3a09ff5858a9e07d"></a>

### [`00b6db00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md) → [`00b6db44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6db60",
      "incomplete_value": false,
      "site": "00b6db64",
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
      "definition_site": "00b6db1c",
      "incomplete_value": false,
      "site": "00b6db20",
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
      "definition_site": "00b6db70",
      "incomplete_value": true,
      "site": "00b6db7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6db2c",
      "incomplete_value": true,
      "site": "00b6db38",
      "value": [
        "LOAD",
        "8",
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
      "00b6db60",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6db70",
      "DATA",
      [
        "storage",
        "010a1a60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6db60",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6db70",
      "DATA",
      [
        "storage",
        "010a1aa0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6db20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md#insn-00b6db20) · [`00b6db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md#insn-00b6db1c) · [`00b6db28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md#insn-00b6db28)
- 新版 [`00b6db64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db64) · [`00b6db60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db60) · [`00b6db6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db44.md#insn-00b6db6c)

~~~diff
- 00b6db20 ["INT_ADD", "register:40f0:8", ["const:b6db20:8", "const:4:8"]]
- 00b6db20 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6db64 ["INT_ADD", "register:40f0:8", ["const:b6db64:8", "const:4:8"]]
+ 00b6db64 ["CALL", null, ["callee:00bde180:8"]]
- 00b6db20 bytes 84c10194
+ 00b6db64 bytes 87c10194
- 00b6db1c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6db1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6db1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6db1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6db60 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6db60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6db60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6db60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6db1c bytes 00fc1991
+ 00b6db60 bytes 00c81791
- 00b6db28 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00b6db28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6db28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6db28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6db6c ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00b6db6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6db6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6db6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6db28 bytes 08812991
+ 00b6db6c bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0ebf5a63034e699a60931c5079c3f9"></a>

### [`00b6db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db3c.md) → [`00b6db80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db80.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00b6dbac",
      "incomplete_value": true,
      "site": "00b6dbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6db68",
      "incomplete_value": true,
      "site": "00b6db68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "definition_site": "00b6dba0",
      "incomplete_value": false,
      "site": "00b6dba4",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6db5c",
      "incomplete_value": false,
      "site": "00b6db60",
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
            "const:65:8"
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
      "00b6db90",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dba0",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dbac",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6db90",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dba0",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6dbac",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6db60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db3c.md#insn-00b6db60) · [`00b6db68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db3c.md#insn-00b6db68) · [`00b6db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db3c.md#insn-00b6db4c)
- 新版 [`00b6dba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db80.md#insn-00b6dba4) · [`00b6dbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db80.md#insn-00b6dbac) · [`00b6db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6db80.md#insn-00b6db90)

~~~diff
- 00b6db60 ["INT_ADD", "register:40f0:8", ["const:b6db60:8", "const:4:8"]]
- 00b6db60 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6dba4 ["INT_ADD", "register:40f0:8", ["const:b6dba4:8", "const:4:8"]]
+ 00b6dba4 ["CALL", null, ["callee:00bde090:8"]]
- 00b6db60 bytes 38c10194
+ 00b6dba4 bytes 3bc10194
- 00b6db68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6db68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dbac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dbac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6db68 bytes 603605f9
+ 00b6dbac bytes 605605f9
- 00b6db4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6db4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6db90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6db90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6db4c bytes 683645f9
+ 00b6db90 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a5458435088756b4a6e24463911700"></a>

### [`00b6db7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md) → [`00b6dbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6dbec",
      "incomplete_value": true,
      "site": "00b6dbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dba8",
      "incomplete_value": true,
      "site": "00b6dba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "definition_site": "00b6dbd4",
      "incomplete_value": true,
      "site": "00b6dbd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6db90",
      "incomplete_value": true,
      "site": "00b6db90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6dbdc",
      "incomplete_value": false,
      "site": "00b6dbe4",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6db98",
      "incomplete_value": false,
      "site": "00b6dba0",
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
            "const:65:8"
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
      "00b6dbd0",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dbdc",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dbec",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dbd0",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dbdc",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6dbec",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md#insn-00b6dba0) · [`00b6dba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md#insn-00b6dba8) · [`00b6db8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md#insn-00b6db8c)
- 新版 [`00b6dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbe4) · [`00b6dbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbec) · [`00b6dbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dbc0.md#insn-00b6dbd0)

~~~diff
- 00b6dba0 ["INT_ADD", "register:40f0:8", ["const:b6dba0:8", "const:4:8"]]
- 00b6dba0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6dbe4 ["INT_ADD", "register:40f0:8", ["const:b6dbe4:8", "const:4:8"]]
+ 00b6dbe4 ["CALL", null, ["callee:00bde090:8"]]
- 00b6dba0 bytes 28c10194
+ 00b6dbe4 bytes 2bc10194
- 00b6dba8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6dba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dbec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dbec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dba8 bytes 603605f9
+ 00b6dbec bytes 605605f9
- 00b6db8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6db8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dbd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dbd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6db8c bytes 683645f9
+ 00b6dbd0 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b59238faf7ad5acfa7eb8a54f56822c4"></a>

### [`00b6dbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md) → [`00b6dc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6dc30",
      "incomplete_value": true,
      "site": "00b6dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dbec",
      "incomplete_value": true,
      "site": "00b6dbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "definition_site": "00b6dc14",
      "incomplete_value": true,
      "site": "00b6dc14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dbd0",
      "incomplete_value": true,
      "site": "00b6dbd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6dc20",
      "incomplete_value": false,
      "site": "00b6dc28",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dbdc",
      "incomplete_value": false,
      "site": "00b6dbe4",
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
            "const:65:8"
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
      "00b6dc10",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc20",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dc30",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dc10",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc20",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6dc30",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md#insn-00b6dbe4) · [`00b6dbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md#insn-00b6dbec) · [`00b6dbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md#insn-00b6dbcc)
- 新版 [`00b6dc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc28) · [`00b6dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc30) · [`00b6dc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc00.md#insn-00b6dc10)

~~~diff
- 00b6dbe4 ["INT_ADD", "register:40f0:8", ["const:b6dbe4:8", "const:4:8"]]
- 00b6dbe4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6dc28 ["INT_ADD", "register:40f0:8", ["const:b6dc28:8", "const:4:8"]]
+ 00b6dc28 ["CALL", null, ["callee:00bde090:8"]]
- 00b6dbe4 bytes 17c10194
+ 00b6dc28 bytes 1ac10194
- 00b6dbec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6dbec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dbec bytes 603605f9
+ 00b6dc30 bytes 605605f9
- 00b6dbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6dbcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dc10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dbcc bytes 683645f9
+ 00b6dc10 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a0c83c732f9502de9e2fe97ca04625"></a>

### [`00b6dc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md) → [`00b6dc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6dc74",
      "incomplete_value": true,
      "site": "00b6dc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc30",
      "incomplete_value": true,
      "site": "00b6dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "definition_site": "00b6dc58",
      "incomplete_value": true,
      "site": "00b6dc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc14",
      "incomplete_value": true,
      "site": "00b6dc14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6dc60",
      "incomplete_value": false,
      "site": "00b6dc6c",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc1c",
      "incomplete_value": false,
      "site": "00b6dc28",
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
            "const:65:8"
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
      "00b6dc54",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc60",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dc74",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dc54",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc60",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6dc74",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md#insn-00b6dc28) · [`00b6dc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md#insn-00b6dc30) · [`00b6dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md#insn-00b6dc10)
- 新版 [`00b6dc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc6c) · [`00b6dc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc74) · [`00b6dc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc44.md#insn-00b6dc54)

~~~diff
- 00b6dc28 ["INT_ADD", "register:40f0:8", ["const:b6dc28:8", "const:4:8"]]
- 00b6dc28 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6dc6c ["INT_ADD", "register:40f0:8", ["const:b6dc6c:8", "const:4:8"]]
+ 00b6dc6c ["CALL", null, ["callee:00bde090:8"]]
- 00b6dc28 bytes 06c10194
+ 00b6dc6c bytes 09c10194
- 00b6dc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6dc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dc30 bytes 603605f9
+ 00b6dc74 bytes 605605f9
- 00b6dc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b6dc10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b6dc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dc10 bytes 683645f9
+ 00b6dc54 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4fe4018809a55301bb61363516643ea"></a>

### [`00b6dc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md) → [`00b6dc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6dcec",
      "incomplete_value": true,
      "site": "00b6dcec",
      "value": [
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
      "definition_site": "00b6dca8",
      "incomplete_value": true,
      "site": "00b6dca8",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6dcc8",
      "incomplete_value": true,
      "site": "00b6dcd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc84",
      "incomplete_value": true,
      "site": "00b6dc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a68:8"
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
      "00b6dca8",
      "READ",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dcc8",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dcec",
      "WRITE",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dca8",
      "READ",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dcc8",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dcec",
      "WRITE",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md#insn-00b6dc64) · [`00b6dc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md#insn-00b6dc90) · [`00b6dca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md#insn-00b6dca8)
- 新版 [`00b6dca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md#insn-00b6dca8) · [`00b6dcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md#insn-00b6dcd4) · [`00b6dcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dc94.md#insn-00b6dcec)

~~~diff
- 00b6dc64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
- 00b6dc64 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6dc64 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6dca8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b6dca8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dca8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6dc64 bytes a8c26939
+ 00b6dca8 bytes a8c26a39
- 00b6dc90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dc90 ["INT_ADD", "register:40f0:8", ["const:b6dc90:8", "const:4:8"]]
- 00b6dc90 ["CALLIND", null, ["register:0:8"]]
+ 00b6dcd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6dcd4 ["INT_ADD", "register:40f0:8", ["const:b6dcd4:8", "const:4:8"]]
+ 00b6dcd4 ["CALLIND", null, ["register:0:8"]]
- 00b6dc90 bytes 00013fd6
+ 00b6dcd4 bytes 00013fd6
- 00b6dca8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6dca8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a70:8"]]
- 00b6dca8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6dcec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6dcec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b6dcec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6dca8 bytes a0c22939
+ 00b6dcec bytes a0c22a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10160c76f3dd2597e6c36d4d99868d11"></a>

### [`00b6dcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md) → [`00b6dd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6dd3c",
      "incomplete_value": true,
      "site": "00b6dd3c",
      "value": [
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
      "definition_site": "00b6dcf8",
      "incomplete_value": true,
      "site": "00b6dcf8",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6dd5c",
      "incomplete_value": true,
      "site": "00b6dd5c",
      "value": [
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
      "definition_site": "00b6dd18",
      "incomplete_value": true,
      "site": "00b6dd18",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6dd18",
      "incomplete_value": true,
      "site": "00b6dd18",
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
      "definition_site": "00b6dcd4",
      "incomplete_value": true,
      "site": "00b6dcd4",
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
      "00b6dd14",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd20",
      "READ",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dd3c",
      "WRITE",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dd14",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd20",
      "READ",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dd3c",
      "WRITE",
      [
        "storage",
        "010a1ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dcd0) · [`00b6dcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dcf8) · [`00b6dd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dd14)
- 新版 [`00b6dd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd14) · [`00b6dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd3c) · [`00b6dd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd00.md#insn-00b6dd58)

~~~diff
- 00b6dcd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b6dcd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dd14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b6dd14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dcd0 bytes 813645f9
+ 00b6dd14 bytes 815645f9
- 00b6dcf8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6dcf8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6dcf8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a70:8"]]
- 00b6dcf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6dd3c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6dd3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6dd3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b6dd3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6dcf8 bytes bfc22939
+ 00b6dd3c bytes bfc22a39
- 00b6dd14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dd14 ["INT_ADD", "register:40f0:8", ["const:b6dd14:8", "const:4:8"]]
- 00b6dd14 ["CALLIND", null, ["register:0:8"]]
+ 00b6dd58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6dd58 ["INT_ADD", "register:40f0:8", ["const:b6dd58:8", "const:4:8"]]
+ 00b6dd58 ["CALLIND", null, ["register:0:8"]]
- 00b6dd14 bytes 00013fd6
+ 00b6dd58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cecf5a34570937fbe8ac588a5bf463d"></a>

### [`00b6dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md) → [`00b6dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6ddb0",
      "incomplete_value": true,
      "site": "00b6ddb0",
      "value": [
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
      "definition_site": "00b6dd6c",
      "incomplete_value": true,
      "site": "00b6dd6c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6dd8c",
      "incomplete_value": true,
      "site": "00b6dd8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dd48",
      "incomplete_value": true,
      "site": "00b6dd48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6dd48"
      ],
      [
        "FALL_THROUGH",
        "00b6dd8c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6dd8c",
      "incomplete_value": true,
      "site": "00b6ddb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dd48",
      "incomplete_value": true,
      "site": "00b6dd6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6dd84",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd94",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6ddb0",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dd84",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd94",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6ddb0",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md#insn-00b6dd6c) · [`00b6dd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md#insn-00b6dd40) · [`00b6dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md#insn-00b6dd50)
- 新版 [`00b6ddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6ddb0) · [`00b6dd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6dd84) · [`00b6dd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dd70.md#insn-00b6dd94)

~~~diff
- 00b6dd6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b6dd6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6ddb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b6ddb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dd6c bytes 803605f9
+ 00b6ddb0 bytes 805605f9
- 00b6dd40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b6dd40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dd84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b6dd84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dd40 bytes 813645f9
+ 00b6dd84 bytes 815645f9
- 00b6dd50 ["COPY", "tmp:0:8", ["const:65:8"]]
- 00b6dd50 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b6dd50 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b6dd50 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b6dd94 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00b6dd94 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b6dd94 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b6dd94 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b6dd50 bytes 63940191
+ 00b6dd94 bytes 63c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146c3546e9282b1d9ede4d9ebed643fe"></a>

### [`00b6dd9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md) → [`00b6dde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dde0.md) _ZN8firebase4auth8userinfo11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6ddfc",
      "incomplete_value": true,
      "site": "00b6de00",
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
      "definition_site": "00b6ddb8",
      "incomplete_value": true,
      "site": "00b6ddbc",
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
      "definition_site": "00b6de0c",
      "incomplete_value": true,
      "site": "00b6de18",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6ddc8",
      "incomplete_value": true,
      "site": "00b6ddd4",
      "value": [
        "LOAD",
        "8",
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
      "00b6ddfc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6de0c",
      "DATA",
      [
        "storage",
        "010a1a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6ddfc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6de0c",
      "DATA",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md#insn-00b6ddbc) · [`00b6ddb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md#insn-00b6ddb8) · [`00b6ddc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md#insn-00b6ddc4)
- 新版 [`00b6de00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dde0.md#insn-00b6de00) · [`00b6ddfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dde0.md#insn-00b6ddfc) · [`00b6de08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dde0.md#insn-00b6de08)

~~~diff
- 00b6ddbc ["INT_ADD", "register:40f0:8", ["const:b6ddbc:8", "const:4:8"]]
- 00b6ddbc ["CALL", null, ["callee:00bde180:8"]]
+ 00b6de00 ["INT_ADD", "register:40f0:8", ["const:b6de00:8", "const:4:8"]]
+ 00b6de00 ["CALL", null, ["callee:00bde180:8"]]
- 00b6ddbc bytes ddc00194
+ 00b6de00 bytes e0c00194
- 00b6ddb8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6ddb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ddb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ddb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6ddfc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6ddfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ddfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ddfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ddb8 bytes 00501791
+ 00b6ddfc bytes 001c1591
- 00b6ddc4 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 00b6ddc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6ddc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6ddc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6de08 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00b6de08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6de08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6de08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6ddc4 bytes 08e12991
+ 00b6de08 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cea9f71d0cf94fbfdac71cc70bddd36"></a>

### [`00b6ddd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md) → [`00b6de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6de5c",
      "incomplete_value": true,
      "site": "00b6de5c",
      "value": [
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
      "definition_site": "00b6de18",
      "incomplete_value": true,
      "site": "00b6de18",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6de38",
      "incomplete_value": true,
      "site": "00b6de38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ddf4",
      "incomplete_value": true,
      "site": "00b6ddf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6de40",
      "incomplete_value": false,
      "site": "00b6de54",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ddfc",
      "incomplete_value": false,
      "site": "00b6de10",
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
            "const:65:8"
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
      "00b6de30",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6de40",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6de5c",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6de30",
      "READ",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6de40",
      "PARAM",
      [
        "storage",
        "002a10f0",
        null,
        "string"
      ]
    ],
    [
      "00b6de5c",
      "WRITE",
      [
        "storage",
        "010a1aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6de10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md#insn-00b6de10) · [`00b6de18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md#insn-00b6de18) · [`00b6ddec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md#insn-00b6ddec)
- 新版 [`00b6de54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de54) · [`00b6de5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de5c) · [`00b6de30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de1c.md#insn-00b6de30)

~~~diff
- 00b6de10 ["INT_ADD", "register:40f0:8", ["const:b6de10:8", "const:4:8"]]
- 00b6de10 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6de54 ["INT_ADD", "register:40f0:8", ["const:b6de54:8", "const:4:8"]]
+ 00b6de54 ["CALL", null, ["callee:00bde090:8"]]
- 00b6de10 bytes 8cc00194
+ 00b6de54 bytes 8fc00194
- 00b6de18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b6de18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6de5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b6de5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6de18 bytes 803605f9
+ 00b6de5c bytes 805605f9
- 00b6ddec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b6ddec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6de30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b6de30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ddec bytes 813645f9
+ 00b6de30 bytes 815645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7db2c44c2be028c5b0658716e142f8ae"></a>

### [`00b6de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md) → [`00b6de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6dea8",
      "incomplete_value": false,
      "site": "00b6deac",
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
      "definition_site": "00b6de64",
      "incomplete_value": false,
      "site": "00b6de68",
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
      "definition_site": "00b6deb8",
      "incomplete_value": true,
      "site": "00b6dec4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6de74",
      "incomplete_value": true,
      "site": "00b6de80",
      "value": [
        "LOAD",
        "8",
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
      "00b6dea8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6deb8",
      "DATA",
      [
        "storage",
        "010a1ab0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6dea8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6deb8",
      "DATA",
      [
        "storage",
        "010a1af0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md#insn-00b6de68) · [`00b6de64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md#insn-00b6de64) · [`00b6de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md#insn-00b6de70)
- 新版 [`00b6deac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6deac) · [`00b6dea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6dea8) · [`00b6deb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6de8c.md#insn-00b6deb4)

~~~diff
- 00b6de68 ["INT_ADD", "register:40f0:8", ["const:b6de68:8", "const:4:8"]]
- 00b6de68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6deac ["INT_ADD", "register:40f0:8", ["const:b6deac:8", "const:4:8"]]
+ 00b6deac ["CALL", null, ["callee:00bde180:8"]]
- 00b6de68 bytes b2c00194
+ 00b6deac bytes b5c00194
- 00b6de64 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6de64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6de64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6de64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6dea8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6dea8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6dea8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6dea8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6de64 bytes 00fc1991
+ 00b6dea8 bytes 00c81791
- 00b6de70 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00b6de70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6de70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6de70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6deb4 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00b6deb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6deb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6deb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6de70 bytes 08c12a91
+ 00b6deb4 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-809b5f2a68d46cfc7cd0b1b4bf9934ee"></a>

### [`00b6de84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md) → [`00b6dec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b6def4",
      "incomplete_value": true,
      "site": "00b6def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6deb0",
      "incomplete_value": true,
      "site": "00b6deb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "00b6dedc",
      "incomplete_value": true,
      "site": "00b6dedc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de98",
      "incomplete_value": true,
      "site": "00b6de98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6de98"
      ],
      [
        "FALL_THROUGH",
        "00b6dedc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6dedc",
      "incomplete_value": true,
      "site": "00b6def4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de98",
      "incomplete_value": true,
      "site": "00b6deb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6ded8",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6def4",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6ded8",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6def4",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md#insn-00b6deb0) · [`00b6de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md#insn-00b6de94) · [`00b6dea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md#insn-00b6dea8)
- 新版 [`00b6def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6def4) · [`00b6ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6ded8) · [`00b6deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md#insn-00b6deec)

~~~diff
- 00b6deb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6deb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6def4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6def4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6deb0 bytes 605e05f9
+ 00b6def4 bytes 607e05f9
- 00b6de94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6de94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ded8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6ded8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6de94 bytes 685e45f9
+ 00b6ded8 bytes 687e45f9
- 00b6dea8 ["INT_ADD", "register:40f0:8", ["const:b6dea8:8", "const:4:8"]]
- 00b6dea8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6deec ["INT_ADD", "register:40f0:8", ["const:b6deec:8", "const:4:8"]]
+ 00b6deec ["CALL", null, ["callee:00bde090:8"]]
- 00b6dea8 bytes 66c00194
+ 00b6deec bytes 69c00194
~~~


<a id="compare-a111c845dc045e87916d4ff0bdb3edef"></a>

### [`00b6dec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md) → [`00b6df08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b6df34",
      "incomplete_value": true,
      "site": "00b6df34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6def0",
      "incomplete_value": true,
      "site": "00b6def0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "00b6df1c",
      "incomplete_value": true,
      "site": "00b6df1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ded8",
      "incomplete_value": true,
      "site": "00b6ded8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6ded8"
      ],
      [
        "FALL_THROUGH",
        "00b6df1c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6df1c",
      "incomplete_value": true,
      "site": "00b6df34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ded8",
      "incomplete_value": true,
      "site": "00b6def0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6df18",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df34",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df18",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df34",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6def0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md#insn-00b6def0) · [`00b6ded4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md#insn-00b6ded4) · [`00b6dee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md#insn-00b6dee8)
- 新版 [`00b6df34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df34) · [`00b6df18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df18) · [`00b6df2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df08.md#insn-00b6df2c)

~~~diff
- 00b6def0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6def0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6df34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6df34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6def0 bytes 605e05f9
+ 00b6df34 bytes 607e05f9
- 00b6ded4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6ded4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6df18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6df18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ded4 bytes 685e45f9
+ 00b6df18 bytes 687e45f9
- 00b6dee8 ["INT_ADD", "register:40f0:8", ["const:b6dee8:8", "const:4:8"]]
- 00b6dee8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6df2c ["INT_ADD", "register:40f0:8", ["const:b6df2c:8", "const:4:8"]]
+ 00b6df2c ["CALL", null, ["callee:00bde090:8"]]
- 00b6dee8 bytes 56c00194
+ 00b6df2c bytes 59c00194
~~~


<a id="compare-289809bc0ab3851d56a867b0a1a490c9"></a>

### [`00b6df04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md) → [`00b6df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6df78",
      "incomplete_value": true,
      "site": "00b6df78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df34",
      "incomplete_value": true,
      "site": "00b6df34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df18",
      "incomplete_value": true,
      "site": "00b6df18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6df18"
      ],
      [
        "FALL_THROUGH",
        "00b6df5c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df18",
      "incomplete_value": true,
      "site": "00b6df34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6df58",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df78",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df58",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df78",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df34) · [`00b6df14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df14) · [`00b6df2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df2c)
- 新版 [`00b6df78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df78) · [`00b6df58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df58) · [`00b6df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df48.md#insn-00b6df70)

~~~diff
- 00b6df34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6df34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6df78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6df78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6df34 bytes 605e05f9
+ 00b6df78 bytes 607e05f9
- 00b6df14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6df14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6df58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6df58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6df14 bytes 685e45f9
+ 00b6df58 bytes 687e45f9
- 00b6df2c ["INT_ADD", "register:40f0:8", ["const:b6df2c:8", "const:4:8"]]
- 00b6df2c ["CALL", null, ["callee:00bde090:8"]]
+ 00b6df70 ["INT_ADD", "register:40f0:8", ["const:b6df70:8", "const:4:8"]]
+ 00b6df70 ["CALL", null, ["callee:00bde090:8"]]
- 00b6df2c bytes 45c00194
+ 00b6df70 bytes 48c00194
~~~


<a id="compare-dcac534ecd9290ed2006efe943d9306b"></a>

### [`00b6df48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md) → [`00b6df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6dfbc",
      "incomplete_value": true,
      "site": "00b6dfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df78",
      "incomplete_value": true,
      "site": "00b6df78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "00b6dfa0",
      "incomplete_value": true,
      "site": "00b6dfa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6df5c"
      ],
      [
        "FALL_THROUGH",
        "00b6dfa0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6dfa0",
      "incomplete_value": true,
      "site": "00b6dfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6df9c",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dfbc",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df9c",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dfbc",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df78) · [`00b6df58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df58) · [`00b6df70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df70)
- 新版 [`00b6dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6dfbc) · [`00b6df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6df9c) · [`00b6dfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6df8c.md#insn-00b6dfb4)

~~~diff
- 00b6df78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6df78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dfbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6dfbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6df78 bytes 605e05f9
+ 00b6dfbc bytes 607e05f9
- 00b6df58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00b6df58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6df9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:af8:8"]]
+ 00b6df9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6df58 bytes 685e45f9
+ 00b6df9c bytes 687e45f9
- 00b6df70 ["INT_ADD", "register:40f0:8", ["const:b6df70:8", "const:4:8"]]
- 00b6df70 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6dfb4 ["INT_ADD", "register:40f0:8", ["const:b6dfb4:8", "const:4:8"]]
+ 00b6dfb4 ["CALL", null, ["callee:00bde090:8"]]
- 00b6df70 bytes 34c00194
+ 00b6dfb4 bytes 37c00194
~~~


<a id="compare-b9bd3151979249fe9d7c92ca8579b74f"></a>

### [`00b6df98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md) → [`00b6dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dfdc.md) _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6e034",
      "incomplete_value": true,
      "site": "00b6e034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dff0",
      "incomplete_value": true,
      "site": "00b6dff0",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e010",
      "incomplete_value": true,
      "site": "00b6e01c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfcc",
      "incomplete_value": true,
      "site": "00b6dfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
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
      "00b6dff0",
      "READ",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e010",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e034",
      "WRITE",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dff0",
      "READ",
      [
        "storage",
        "010a1b00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e010",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e034",
      "WRITE",
      [
        "storage",
        "010a1b00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dfac) · [`00b6dfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dfd8) · [`00b6dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dff0)
- 新版 [`00b6dff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dfdc.md#insn-00b6dff0) · [`00b6e01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dfdc.md#insn-00b6e01c) · [`00b6e034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dfdc.md#insn-00b6e034)

~~~diff
- 00b6dfac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ac0:8"]]
- 00b6dfac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6dfac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6dff0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b00:8"]]
+ 00b6dff0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dff0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6dfac bytes a8026b39
+ 00b6dff0 bytes a8026c39
- 00b6dfd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dfd8 ["INT_ADD", "register:40f0:8", ["const:b6dfd8:8", "const:4:8"]]
- 00b6dfd8 ["CALLIND", null, ["register:0:8"]]
+ 00b6e01c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e01c ["INT_ADD", "register:40f0:8", ["const:b6e01c:8", "const:4:8"]]
+ 00b6e01c ["CALLIND", null, ["register:0:8"]]
- 00b6dfd8 bytes 00013fd6
+ 00b6e01c bytes 00013fd6
- 00b6dff0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6dff0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ac0:8"]]
- 00b6dff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6e034 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6e034 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b00:8"]]
+ 00b6e034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6dff0 bytes a0022b39
+ 00b6e034 bytes a0022c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e557654ccd4c14a1b75ee9dd4700701f"></a>

### [`00b6e004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e004.md) → [`00b6e048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6e084",
      "incomplete_value": true,
      "site": "00b6e084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e040",
      "incomplete_value": true,
      "site": "00b6e040",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e0a4",
      "incomplete_value": true,
      "site": "00b6e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e060",
      "incomplete_value": true,
      "site": "00b6e060",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e060",
      "incomplete_value": true,
      "site": "00b6e060",
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
      "definition_site": "00b6e01c",
      "incomplete_value": true,
      "site": "00b6e01c",
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
      "00b6e05c",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e068",
      "READ",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e084",
      "WRITE",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e05c",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e068",
      "READ",
      [
        "storage",
        "010a1b00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e084",
      "WRITE",
      [
        "storage",
        "010a1b00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e004.md#insn-00b6e018) · [`00b6e040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e004.md#insn-00b6e040) · [`00b6e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e004.md#insn-00b6e05c)
- 新版 [`00b6e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e05c) · [`00b6e084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e084) · [`00b6e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e048.md#insn-00b6e0a0)

~~~diff
- 00b6e018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00b6e018 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e05c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
+ 00b6e05c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e018 bytes 815e45f9
+ 00b6e05c bytes 817e45f9
- 00b6e040 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e040 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e040 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ac0:8"]]
- 00b6e040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6e084 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6e084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6e084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b00:8"]]
+ 00b6e084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e040 bytes bf022b39
+ 00b6e084 bytes bf022c39
- 00b6e05c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e05c ["INT_ADD", "register:40f0:8", ["const:b6e05c:8", "const:4:8"]]
- 00b6e05c ["CALLIND", null, ["register:0:8"]]
+ 00b6e0a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e0a0 ["INT_ADD", "register:40f0:8", ["const:b6e0a0:8", "const:4:8"]]
+ 00b6e0a0 ["CALLIND", null, ["register:0:8"]]
- 00b6e05c bytes 00013fd6
+ 00b6e0a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e80f4d3454d413b95c3e75f6d7ed3633"></a>

### [`00b6e074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md) → [`00b6e0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6e0f8",
      "incomplete_value": true,
      "site": "00b6e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e0b4",
      "incomplete_value": true,
      "site": "00b6e0b4",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e0d4",
      "incomplete_value": true,
      "site": "00b6e0d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e090",
      "incomplete_value": true,
      "site": "00b6e090",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6e090"
      ],
      [
        "FALL_THROUGH",
        "00b6e0d4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6e0d4",
      "incomplete_value": true,
      "site": "00b6e0f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e090",
      "incomplete_value": true,
      "site": "00b6e0b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6e0cc",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e0f8",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e10c",
      "PARAM",
      [
        "storage",
        "00c12a10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6e0cc",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e0f8",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e10c",
      "PARAM",
      [
        "storage",
        "00c12a60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e0b4) · [`00b6e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e088) · [`00b6e0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e0ac)
- 新版 [`00b6e0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0f8) · [`00b6e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0cc) · [`00b6e0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e0b8.md#insn-00b6e0f0)

~~~diff
- 00b6e0b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00b6e0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e0f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
+ 00b6e0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e0b4 bytes 805e05f9
+ 00b6e0f8 bytes 807e05f9
- 00b6e088 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00b6e088 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e0cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
+ 00b6e0cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e088 bytes 815e45f9
+ 00b6e0cc bytes 817e45f9
- 00b6e0ac ["INT_ADD", "register:40f0:8", ["const:b6e0ac:8", "const:4:8"]]
- 00b6e0ac ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e0f0 ["INT_ADD", "register:40f0:8", ["const:b6e0f0:8", "const:4:8"]]
+ 00b6e0f0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e0ac bytes e5bf0194
+ 00b6e0f0 bytes e8bf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ffdc65c2f020317f07fb665079a107"></a>

### [`00b6e0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md) → [`00b6e128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6e144",
      "incomplete_value": false,
      "site": "00b6e148",
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
      "definition_site": "00b6e100",
      "incomplete_value": false,
      "site": "00b6e104",
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
      "definition_site": "00b6e154",
      "incomplete_value": true,
      "site": "00b6e160",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e110",
      "incomplete_value": true,
      "site": "00b6e11c",
      "value": [
        "LOAD",
        "8",
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
      "00b6e144",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6e154",
      "DATA",
      [
        "storage",
        "010a1ac8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e144",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6e154",
      "DATA",
      [
        "storage",
        "010a1b08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e104) · [`00b6e100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e100) · [`00b6e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e10c)
- 新版 [`00b6e148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e148) · [`00b6e144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e144) · [`00b6e150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e128.md#insn-00b6e150)

~~~diff
- 00b6e104 ["INT_ADD", "register:40f0:8", ["const:b6e104:8", "const:4:8"]]
- 00b6e104 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6e148 ["INT_ADD", "register:40f0:8", ["const:b6e148:8", "const:4:8"]]
+ 00b6e148 ["CALL", null, ["callee:00bde180:8"]]
- 00b6e104 bytes 0bc00194
+ 00b6e148 bytes 0ec00194
- 00b6e100 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6e100 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e100 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e100 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e144 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6e144 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e144 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e144 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e100 bytes 00501791
+ 00b6e144 bytes 001c1591
- 00b6e10c ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00b6e10c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e10c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e10c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e150 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00b6e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e10c bytes 08212b91
+ 00b6e150 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c08d13a4d3b8667fc422a45ee47ba3"></a>

### [`00b6e120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md) → [`00b6e164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6e1a4",
      "incomplete_value": true,
      "site": "00b6e1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e160",
      "incomplete_value": true,
      "site": "00b6e160",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e180",
      "incomplete_value": true,
      "site": "00b6e180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e13c",
      "incomplete_value": true,
      "site": "00b6e13c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b6e13c"
      ],
      [
        "FALL_THROUGH",
        "00b6e180"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6e180",
      "incomplete_value": true,
      "site": "00b6e1a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e13c",
      "incomplete_value": true,
      "site": "00b6e160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6e178",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1a4",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1bc",
      "PARAM",
      [
        "storage",
        "010a1ad8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6e178",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1a4",
      "WRITE",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1bc",
      "PARAM",
      [
        "storage",
        "010a1b18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md#insn-00b6e160) · [`00b6e134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md#insn-00b6e134) · [`00b6e158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md#insn-00b6e158)
- 新版 [`00b6e1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e1a4) · [`00b6e178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e178) · [`00b6e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e164.md#insn-00b6e19c)

~~~diff
- 00b6e160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00b6e160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e1a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
+ 00b6e1a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e160 bytes 805e05f9
+ 00b6e1a4 bytes 807e05f9
- 00b6e134 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
- 00b6e134 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e178 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:af8:8"]]
+ 00b6e178 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e134 bytes 815e45f9
+ 00b6e178 bytes 817e45f9
- 00b6e158 ["INT_ADD", "register:40f0:8", ["const:b6e158:8", "const:4:8"]]
- 00b6e158 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e19c ["INT_ADD", "register:40f0:8", ["const:b6e19c:8", "const:4:8"]]
+ 00b6e19c ["CALL", null, ["callee:00bde090:8"]]
- 00b6e158 bytes babf0194
+ 00b6e19c bytes bdbf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b136bda650b71d2f987e217fbef96b5d"></a>

### [`00b6e190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md) → [`00b6e1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e1d4.md) _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6e1f0",
      "incomplete_value": false,
      "site": "00b6e1f4",
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
      "definition_site": "00b6e1ac",
      "incomplete_value": false,
      "site": "00b6e1b0",
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
      "00b6e1f0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6e200",
      "DATA",
      [
        "storage",
        "010a1ad8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6e1f0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6e200",
      "DATA",
      [
        "storage",
        "010a1b18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md#insn-00b6e1b0) · [`00b6e1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md#insn-00b6e1ac) · [`00b6e1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md#insn-00b6e1b8)
- 新版 [`00b6e1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e1d4.md#insn-00b6e1f4) · [`00b6e1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e1d4.md#insn-00b6e1f0) · [`00b6e1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e1d4.md#insn-00b6e1fc)

~~~diff
- 00b6e1b0 ["INT_ADD", "register:40f0:8", ["const:b6e1b0:8", "const:4:8"]]
- 00b6e1b0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6e1f4 ["INT_ADD", "register:40f0:8", ["const:b6e1f4:8", "const:4:8"]]
+ 00b6e1f4 ["CALL", null, ["callee:00bde180:8"]]
- 00b6e1b0 bytes e0bf0194
+ 00b6e1f4 bytes e3bf0194
- 00b6e1ac ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6e1ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e1ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e1ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e1f0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6e1f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e1f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e1f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e1ac bytes 00fc1991
+ 00b6e1f0 bytes 00c81791
- 00b6e1b8 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00b6e1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e1b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e1fc ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00b6e1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e1b8 bytes 08612b91
+ 00b6e1fc bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1c7993bf0b343d5bd7632434e9a9ad"></a>

### [`00b6e1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md) → [`00b6e210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e210.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00b6e23c",
      "incomplete_value": true,
      "site": "00b6e23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1f8",
      "incomplete_value": true,
      "site": "00b6e1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e224",
      "incomplete_value": true,
      "site": "00b6e224",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1e0",
      "incomplete_value": true,
      "site": "00b6e1e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e230",
      "incomplete_value": false,
      "site": "00b6e234",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1ec",
      "incomplete_value": false,
      "site": "00b6e1f0",
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
            "const:133:8"
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
      "00b6e220",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e230",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e23c",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e220",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e230",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e23c",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1f0) · [`00b6e1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1f8) · [`00b6e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1dc)
- 新版 [`00b6e234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e210.md#insn-00b6e234) · [`00b6e23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e210.md#insn-00b6e23c) · [`00b6e220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e210.md#insn-00b6e220)

~~~diff
- 00b6e1f0 ["INT_ADD", "register:40f0:8", ["const:b6e1f0:8", "const:4:8"]]
- 00b6e1f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e234 ["INT_ADD", "register:40f0:8", ["const:b6e234:8", "const:4:8"]]
+ 00b6e234 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e1f0 bytes 94bf0194
+ 00b6e234 bytes 97bf0194
- 00b6e1f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e1f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e23c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e23c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e1f8 bytes 607205f9
+ 00b6e23c bytes 609205f9
- 00b6e1dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e1dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e220 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e1dc bytes 687245f9
+ 00b6e220 bytes 689245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8c85c6a514ba4e19275092773ce44c"></a>

### [`00b6e20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e20c.md) → [`00b6e250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00b6e27c",
      "incomplete_value": true,
      "site": "00b6e27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e238",
      "incomplete_value": true,
      "site": "00b6e238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e264",
      "incomplete_value": true,
      "site": "00b6e264",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e220",
      "incomplete_value": true,
      "site": "00b6e220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e26c",
      "incomplete_value": false,
      "site": "00b6e274",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e228",
      "incomplete_value": false,
      "site": "00b6e230",
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
            "const:133:8"
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
      "00b6e260",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e26c",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e27c",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e260",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e26c",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e27c",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e20c.md#insn-00b6e230) · [`00b6e238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e20c.md#insn-00b6e238) · [`00b6e21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e20c.md#insn-00b6e21c)
- 新版 [`00b6e274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e274) · [`00b6e27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e27c) · [`00b6e260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e250.md#insn-00b6e260)

~~~diff
- 00b6e230 ["INT_ADD", "register:40f0:8", ["const:b6e230:8", "const:4:8"]]
- 00b6e230 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e274 ["INT_ADD", "register:40f0:8", ["const:b6e274:8", "const:4:8"]]
+ 00b6e274 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e230 bytes 84bf0194
+ 00b6e274 bytes 87bf0194
- 00b6e238 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e27c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e238 bytes 607205f9
+ 00b6e27c bytes 609205f9
- 00b6e21c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e21c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e260 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e260 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e21c bytes 687245f9
+ 00b6e260 bytes 689245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48dbc80fa5c7b5110d0c222a41f53789"></a>

### [`00b6e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e24c.md) → [`00b6e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6e2c0",
      "incomplete_value": true,
      "site": "00b6e2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e27c",
      "incomplete_value": true,
      "site": "00b6e27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e2a4",
      "incomplete_value": true,
      "site": "00b6e2a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e260",
      "incomplete_value": true,
      "site": "00b6e260",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e2b0",
      "incomplete_value": false,
      "site": "00b6e2b8",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e26c",
      "incomplete_value": false,
      "site": "00b6e274",
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
            "const:133:8"
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
      "00b6e2a0",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2b0",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e2c0",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e2a0",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2b0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e2c0",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e24c.md#insn-00b6e274) · [`00b6e27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e24c.md#insn-00b6e27c) · [`00b6e25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e24c.md#insn-00b6e25c)
- 新版 [`00b6e2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e2b8) · [`00b6e2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e2c0) · [`00b6e2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e290.md#insn-00b6e2a0)

~~~diff
- 00b6e274 ["INT_ADD", "register:40f0:8", ["const:b6e274:8", "const:4:8"]]
- 00b6e274 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e2b8 ["INT_ADD", "register:40f0:8", ["const:b6e2b8:8", "const:4:8"]]
+ 00b6e2b8 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e274 bytes 73bf0194
+ 00b6e2b8 bytes 76bf0194
- 00b6e27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e27c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e2c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e27c bytes 607205f9
+ 00b6e2c0 bytes 609205f9
- 00b6e25c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e25c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e2a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e2a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e25c bytes 687245f9
+ 00b6e2a0 bytes 689245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe2784d048011eb385afa7e9ee2e1989"></a>

### [`00b6e290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md) → [`00b6e2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6e304",
      "incomplete_value": true,
      "site": "00b6e304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2c0",
      "incomplete_value": true,
      "site": "00b6e2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e2e8",
      "incomplete_value": true,
      "site": "00b6e2e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2a4",
      "incomplete_value": true,
      "site": "00b6e2a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e2f0",
      "incomplete_value": false,
      "site": "00b6e2fc",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2ac",
      "incomplete_value": false,
      "site": "00b6e2b8",
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
            "const:133:8"
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
      "00b6e2e4",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2f0",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e304",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e2e4",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2f0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e304",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2b8) · [`00b6e2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2c0) · [`00b6e2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2a0)
- 新版 [`00b6e2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e2fc) · [`00b6e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e304) · [`00b6e2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e2d4.md#insn-00b6e2e4)

~~~diff
- 00b6e2b8 ["INT_ADD", "register:40f0:8", ["const:b6e2b8:8", "const:4:8"]]
- 00b6e2b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e2fc ["INT_ADD", "register:40f0:8", ["const:b6e2fc:8", "const:4:8"]]
+ 00b6e2fc ["CALL", null, ["callee:00bde090:8"]]
- 00b6e2b8 bytes 62bf0194
+ 00b6e2fc bytes 65bf0194
- 00b6e2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e2c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e2c0 bytes 607205f9
+ 00b6e304 bytes 609205f9
- 00b6e2a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
- 00b6e2a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e2e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00b6e2e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e2a0 bytes 687245f9
+ 00b6e2e4 bytes 689245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e41a7985fcb61a1516d92c2b96552b4"></a>

### [`00b6e2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md) → [`00b6e324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6e37c",
      "incomplete_value": true,
      "site": "00b6e37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e338",
      "incomplete_value": true,
      "site": "00b6e338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "definition_site": "00b6e358",
      "incomplete_value": true,
      "site": "00b6e364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e314",
      "incomplete_value": true,
      "site": "00b6e320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae0:8"
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
      "00b6e338",
      "READ",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e358",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e37c",
      "WRITE",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e338",
      "READ",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e358",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e37c",
      "WRITE",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md#insn-00b6e2f4) · [`00b6e320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md#insn-00b6e320) · [`00b6e338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md#insn-00b6e338)
- 新版 [`00b6e338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e338) · [`00b6e364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e364) · [`00b6e37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e324.md#insn-00b6e37c)

~~~diff
- 00b6e2f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ae8:8"]]
- 00b6e2f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6e2f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6e338 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b28:8"]]
+ 00b6e338 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e338 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6e2f4 bytes a8a26b39
+ 00b6e338 bytes a8a26c39
- 00b6e320 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e320 ["INT_ADD", "register:40f0:8", ["const:b6e320:8", "const:4:8"]]
- 00b6e320 ["CALLIND", null, ["register:0:8"]]
+ 00b6e364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e364 ["INT_ADD", "register:40f0:8", ["const:b6e364:8", "const:4:8"]]
+ 00b6e364 ["CALLIND", null, ["register:0:8"]]
- 00b6e320 bytes 00013fd6
+ 00b6e364 bytes 00013fd6
- 00b6e338 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6e338 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ae8:8"]]
- 00b6e338 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6e37c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6e37c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b28:8"]]
+ 00b6e37c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6e338 bytes a0a22b39
+ 00b6e37c bytes a0a22c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc3fcd6cf01e58056757e0c4da597b9"></a>

### [`00b6e34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md) → [`00b6e390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6e3cc",
      "incomplete_value": true,
      "site": "00b6e3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e388",
      "incomplete_value": true,
      "site": "00b6e388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "definition_site": "00b6e3ec",
      "incomplete_value": true,
      "site": "00b6e3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
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
      "definition_site": "00b6e364",
      "incomplete_value": true,
      "site": "00b6e364",
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
      "00b6e3a4",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e3b0",
      "READ",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e3cc",
      "WRITE",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e3a4",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e3b0",
      "READ",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e3cc",
      "WRITE",
      [
        "storage",
        "010a1b28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e360) · [`00b6e388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e388) · [`00b6e3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e3a4)
- 新版 [`00b6e3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3a4) · [`00b6e3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3cc) · [`00b6e3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e390.md#insn-00b6e3e8)

~~~diff
- 00b6e360 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
- 00b6e360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e3a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00b6e3a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e360 bytes 817245f9
+ 00b6e3a4 bytes 819245f9
- 00b6e388 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e388 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e388 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ae8:8"]]
- 00b6e388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6e3cc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6e3cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6e3cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b28:8"]]
+ 00b6e3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e388 bytes bfa22b39
+ 00b6e3cc bytes bfa22c39
- 00b6e3a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e3a4 ["INT_ADD", "register:40f0:8", ["const:b6e3a4:8", "const:4:8"]]
- 00b6e3a4 ["CALLIND", null, ["register:0:8"]]
+ 00b6e3e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e3e8 ["INT_ADD", "register:40f0:8", ["const:b6e3e8:8", "const:4:8"]]
+ 00b6e3e8 ["CALLIND", null, ["register:0:8"]]
- 00b6e3a4 bytes 00013fd6
+ 00b6e3e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309383a92332b4e2f5c424d9c866b4a2"></a>

### [`00b6e3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md) → [`00b6e400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6e440",
      "incomplete_value": true,
      "site": "00b6e440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3fc",
      "incomplete_value": true,
      "site": "00b6e3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e41c",
      "incomplete_value": true,
      "site": "00b6e41c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3d8",
      "incomplete_value": true,
      "site": "00b6e3d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e424",
      "incomplete_value": false,
      "site": "00b6e438",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3e0",
      "incomplete_value": false,
      "site": "00b6e3f4",
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
            "const:133:8"
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
      "00b6e414",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e424",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e440",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e414",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e424",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e440",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md#insn-00b6e3f4) · [`00b6e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md#insn-00b6e3fc) · [`00b6e3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md#insn-00b6e3d0)
- 新版 [`00b6e438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e438) · [`00b6e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e440) · [`00b6e414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e400.md#insn-00b6e414)

~~~diff
- 00b6e3f4 ["INT_ADD", "register:40f0:8", ["const:b6e3f4:8", "const:4:8"]]
- 00b6e3f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e438 ["INT_ADD", "register:40f0:8", ["const:b6e438:8", "const:4:8"]]
+ 00b6e438 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e3f4 bytes 13bf0194
+ 00b6e438 bytes 16bf0194
- 00b6e3fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
- 00b6e3fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00b6e440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e3fc bytes 807205f9
+ 00b6e440 bytes 809205f9
- 00b6e3d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
- 00b6e3d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e414 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00b6e414 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e3d0 bytes 817245f9
+ 00b6e414 bytes 819245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-402b2f612bd0399e3f01243ff8aff11d"></a>

### [`00b6e42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md) → [`00b6e470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6e48c",
      "incomplete_value": false,
      "site": "00b6e490",
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
      "definition_site": "00b6e448",
      "incomplete_value": false,
      "site": "00b6e44c",
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
      "definition_site": "00b6e49c",
      "incomplete_value": true,
      "site": "00b6e4a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e458",
      "incomplete_value": true,
      "site": "00b6e464",
      "value": [
        "LOAD",
        "8",
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
      "00b6e48c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6e49c",
      "DATA",
      [
        "storage",
        "010a1af0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e48c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6e49c",
      "DATA",
      [
        "storage",
        "010a1b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e44c) · [`00b6e448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e448) · [`00b6e454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e454)
- 新版 [`00b6e490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e490) · [`00b6e48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e48c) · [`00b6e498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e470.md#insn-00b6e498)

~~~diff
- 00b6e44c ["INT_ADD", "register:40f0:8", ["const:b6e44c:8", "const:4:8"]]
- 00b6e44c ["CALL", null, ["callee:00bde180:8"]]
+ 00b6e490 ["INT_ADD", "register:40f0:8", ["const:b6e490:8", "const:4:8"]]
+ 00b6e490 ["CALL", null, ["callee:00bde180:8"]]
- 00b6e44c bytes 39bf0194
+ 00b6e490 bytes 3cbf0194
- 00b6e448 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6e448 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e448 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e448 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e48c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b6e48c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e48c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e48c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e448 bytes 00501791
+ 00b6e48c bytes 001c1591
- 00b6e454 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00b6e454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e498 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00b6e498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e454 bytes 08c12b91
+ 00b6e498 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e1970749bb474904bb600e38b1e6fa"></a>

### [`00b6e468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md) → [`00b6e4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6e4ec",
      "incomplete_value": true,
      "site": "00b6e4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e4a8",
      "incomplete_value": true,
      "site": "00b6e4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b6e4c8",
      "incomplete_value": true,
      "site": "00b6e4c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e484",
      "incomplete_value": true,
      "site": "00b6e484",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e4d0",
      "incomplete_value": false,
      "site": "00b6e4e4",
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
            "const:1be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e48c",
      "incomplete_value": false,
      "site": "00b6e4a0",
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
            "const:133:8"
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
      "00b6e4c0",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e4d0",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e4ec",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e4c0",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e4d0",
      "PARAM",
      [
        "storage",
        "0029d1be",
        null,
        "string"
      ]
    ],
    [
      "00b6e4ec",
      "WRITE",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md#insn-00b6e4a0) · [`00b6e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md#insn-00b6e4a8) · [`00b6e47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md#insn-00b6e47c)
- 新版 [`00b6e4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4e4) · [`00b6e4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4ec) · [`00b6e4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md#insn-00b6e4c0)

~~~diff
- 00b6e4a0 ["INT_ADD", "register:40f0:8", ["const:b6e4a0:8", "const:4:8"]]
- 00b6e4a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e4e4 ["INT_ADD", "register:40f0:8", ["const:b6e4e4:8", "const:4:8"]]
+ 00b6e4e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b6e4a0 bytes e8be0194
+ 00b6e4e4 bytes ebbe0194
- 00b6e4a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
- 00b6e4a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e4ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00b6e4ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e4a8 bytes 807205f9
+ 00b6e4ec bytes 809205f9
- 00b6e47c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
- 00b6e47c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e4c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00b6e4c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e47c bytes 817245f9
+ 00b6e4c0 bytes 819245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1875c28fabb880efc793071a05a80ae"></a>

### [`00b6e4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md) → [`00b6e51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6e538",
      "incomplete_value": false,
      "site": "00b6e53c",
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
      "definition_site": "00b6e4f4",
      "incomplete_value": false,
      "site": "00b6e4f8",
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
      "definition_site": "00b6e548",
      "incomplete_value": true,
      "site": "00b6e554",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6e504",
      "incomplete_value": true,
      "site": "00b6e510",
      "value": [
        "LOAD",
        "8",
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
      "00b6e538",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6e548",
      "DATA",
      [
        "storage",
        "010a1b10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6e538",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6e548",
      "DATA",
      [
        "storage",
        "010a1b50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e4f8) · [`00b6e4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e4f4) · [`00b6e500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e500)
- 新版 [`00b6e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e53c) · [`00b6e538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e538) · [`00b6e544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md#insn-00b6e544)

~~~diff
- 00b6e4f8 ["INT_ADD", "register:40f0:8", ["const:b6e4f8:8", "const:4:8"]]
- 00b6e4f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6e53c ["INT_ADD", "register:40f0:8", ["const:b6e53c:8", "const:4:8"]]
+ 00b6e53c ["CALL", null, ["callee:00bde180:8"]]
- 00b6e4f8 bytes 0ebf0194
+ 00b6e53c bytes 11bf0194
- 00b6e4f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b6e4f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e4f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e4f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e538 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6e538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e4f4 bytes 00fc1991
+ 00b6e538 bytes 00c81791
- 00b6e500 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00b6e500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e544 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00b6e544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e500 bytes 08412c91
+ 00b6e544 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81484b0196a55a70b30f375608a308b6"></a>

### [`00b6e514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e514.md) → [`00b6e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c00.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 1件 [`00be0c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c50.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 79.67% / 新版 79.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 12件, `store_condition` 2件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e59c",
      "incomplete_value": true,
      "site": "00b6e59c",
      "value": [
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
    "old": {
      "definition_site": "00b6e558",
      "incomplete_value": true,
      "site": "00b6e558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6e5f4",
      "incomplete_value": true,
      "site": "00b6e5f4",
      "value": [
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
      "definition_site": "00b6e5b0",
      "incomplete_value": true,
      "site": "00b6e5b0",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e64c",
      "incomplete_value": true,
      "site": "00b6e64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e608",
      "incomplete_value": true,
      "site": "00b6e608",
      "value": [
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
      "00b6e570",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e59c",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e5ac",
      "PARAM",
      [
        "storage",
        "00c127e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6e570",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e59c",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e5ac",
      "PARAM",
      [
        "storage",
        "00c12838",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e514.md#insn-00b6e558) · [`00b6e56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e514.md#insn-00b6e56c) · [`00b6e57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e514.md#insn-00b6e57c)
- 新版 [`00b6e59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e59c) · [`00b6e5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e5b0) · [`00b6e5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e558.md#insn-00b6e5c0)

~~~diff
- 00b6e558 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 00b6e558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e59c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
+ 00b6e59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e558 bytes a0de04f9
+ 00b6e59c bytes a0fe04f9
- 00b6e56c ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00b6e56c ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00b6e56c ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00b6e56c ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00b6e5b0 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00b6e5b0 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00b6e5b0 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00b6e5b0 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00b6e56c bytes 84202791
+ 00b6e5b0 bytes 84202891
- 00b6e57c ["INT_ADD", "register:40f0:8", ["const:b6e57c:8", "const:4:8"]]
- 00b6e57c ["CALL", null, ["callee:00bde0b0:8"]]
+ 00b6e5c0 ["INT_ADD", "register:40f0:8", ["const:b6e5c0:8", "const:4:8"]]
+ 00b6e5c0 ["CALL", null, ["callee:00bde0b0:8"]]
- 00b6e57c bytes b9be0194
+ 00b6e5c0 bytes bcbe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e01f9b6ffc0f4aa0978d4e1c9d7fd2b5"></a>

### [`00b6e700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e700.md) → [`00b6e744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c20.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c70.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

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
      "definition_site": "00b6e780",
      "incomplete_value": true,
      "site": "00b6e780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e73c",
      "incomplete_value": true,
      "site": "00b6e73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "definition_site": "00b6e7a0",
      "incomplete_value": true,
      "site": "00b6e7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e75c",
      "incomplete_value": true,
      "site": "00b6e75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00b6e7cc",
      "incomplete_value": true,
      "site": "00b6e7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e788",
      "incomplete_value": true,
      "site": "00b6e788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "00b6e758",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e768",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e780",
      "WRITE",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e758",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e768",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e780",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e700.md#insn-00b6e714) · [`00b6e724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e700.md#insn-00b6e724) · [`00b6e73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e700.md#insn-00b6e73c)
- 新版 [`00b6e758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e758) · [`00b6e768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e768) · [`00b6e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e744.md#insn-00b6e780)

~~~diff
- 00b6e714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00b6e714 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
+ 00b6e758 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e714 bytes 81de44f9
+ 00b6e758 bytes 81fe44f9
- 00b6e724 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9c0:8"]]
- 00b6e724 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6e724 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6e768 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a00:8"]]
+ 00b6e768 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e768 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6e724 bytes a8026739
+ 00b6e768 bytes a8026839
- 00b6e73c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e73c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e73c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9c0:8"]]
- 00b6e73c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6e780 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6e780 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6e780 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a00:8"]]
+ 00b6e780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e73c bytes bf022739
+ 00b6e780 bytes bf022839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca2251aa789e138febe6ae821b03d0bc"></a>

### [`00b6ed38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md) → [`00b6ed7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ed7c.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00b6eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

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
      "definition_site": "00b6ee00",
      "incomplete_value": false,
      "site": "00b6ee04",
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
            "const:3be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6edbc",
      "incomplete_value": false,
      "site": "00b6edc0",
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
            "const:324:8"
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
      "definition_site": "00b6ee0c",
      "incomplete_value": true,
      "site": "00b6ee18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6edc8",
      "incomplete_value": true,
      "site": "00b6edd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c8:8"
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
      "00b6ee00",
      "PARAM",
      [
        "storage",
        "002a6324",
        null,
        "string"
      ]
    ],
    [
      "00b6ee0c",
      "READ",
      [
        "storage",
        "010a19c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6ee00",
      "PARAM",
      [
        "storage",
        "002a63be",
        null,
        "string"
      ]
    ],
    [
      "00b6ee0c",
      "READ",
      [
        "storage",
        "010a1a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ed7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6ed7c) · [`00b6edc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6edc0) · [`00b6edd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6edd4)
- 新版 [`00b6edc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ed7c.md#insn-00b6edc0) · [`00b6ee04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ed7c.md#insn-00b6ee04) · [`00b6ee18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6ed7c.md#insn-00b6ee18)

~~~diff
- 00b6ed7c ["INT_ADD", "register:40f0:8", ["const:b6ed7c:8", "const:4:8"]]
- 00b6ed7c ["CALL", null, ["callee:00bde200:8"]]
+ 00b6edc0 ["INT_ADD", "register:40f0:8", ["const:b6edc0:8", "const:4:8"]]
+ 00b6edc0 ["CALL", null, ["callee:00bde200:8"]]
- 00b6ed7c bytes 0dbd0194
+ 00b6edc0 bytes 10bd0194
- 00b6edc0 ["INT_ADD", "register:40f0:8", ["const:b6edc0:8", "const:4:8"]]
- 00b6edc0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6ee04 ["INT_ADD", "register:40f0:8", ["const:b6ee04:8", "const:4:8"]]
+ 00b6ee04 ["CALL", null, ["callee:00bde180:8"]]
- 00b6edc0 bytes dcbc0194
+ 00b6ee04 bytes dfbc0194
- 00b6edd4 ["INT_ADD", "register:40f0:8", ["const:b6edd4:8", "const:4:8"]]
- 00b6edd4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6ee18 ["INT_ADD", "register:40f0:8", ["const:b6ee18:8", "const:4:8"]]
+ 00b6ee18 ["CALL", null, ["callee:0047495c:8"]]
- 00b6edd4 bytes e216e497
+ 00b6ee18 bytes d116e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cfc9c9364186c4761a39f2a12da650b"></a>

### [`00b6f210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f210.md) → [`00b6f254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f254.md) _ZNK8firebase4auth4User13provider_dataEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc10.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00bddc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc60.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6f324",
      "incomplete_value": true,
      "site": "00b6f340",
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
      "definition_site": "00b6f2e0",
      "incomplete_value": true,
      "site": "00b6f2fc",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6f344",
      "incomplete_value": true,
      "site": "00b6f348",
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
      "definition_site": "00b6f300",
      "incomplete_value": true,
      "site": "00b6f304",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6f7f0",
      "incomplete_value": true,
      "site": "00b6f7f4",
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
      "definition_site": "00b6f7ac",
      "incomplete_value": true,
      "site": "00b6f7b0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6f2b4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f304",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6f30c",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6f2b4",
      "READ",
      [
        "storage",
        "010a1a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f304",
      "READ",
      [
        "storage",
        "00c1bc30",
        null,
        "pointer"
      ]
    ],
    [
      "00b6f30c",
      "READ",
      [
        "storage",
        "00c1bb98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f210.md#insn-00b6f280) · [`00b6f2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f210.md#insn-00b6f2c0) · [`00b6f3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f210.md#insn-00b6f3c8)
- 新版 [`00b6f2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f254.md#insn-00b6f2c4) · [`00b6f304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f254.md#insn-00b6f304) · [`00b6f40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f254.md#insn-00b6f40c)

~~~diff
- 00b6f280 ["INT_ADD", "register:40f0:8", ["const:b6f280:8", "const:4:8"]]
- 00b6f280 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6f2c4 ["INT_ADD", "register:40f0:8", ["const:b6f2c4:8", "const:4:8"]]
+ 00b6f2c4 ["CALL", null, ["callee:0047495c:8"]]
- 00b6f280 bytes b715e497
+ 00b6f2c4 bytes a615e497
- 00b6f2c0 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:be0:8"]]
- 00b6f2c0 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6f304 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:c30:8"]]
+ 00b6f304 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6f2c0 bytes 6bf145f9
+ 00b6f304 bytes 6b1946f9
- 00b6f3c8 ["INT_ADD", "register:40f0:8", ["const:b6f3c8:8", "const:4:8"]]
- 00b6f3c8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6f40c ["INT_ADD", "register:40f0:8", ["const:b6f40c:8", "const:4:8"]]
+ 00b6f40c ["CALL", null, ["callee:0047495c:8"]]
- 00b6f3c8 bytes 6515e497
+ 00b6f40c bytes 5415e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b109ce29967283e4598df997302869d6"></a>

### [`00b6f91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md) → [`00b6f960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f960.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e80.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e50.md)
- 新版 呼出元 1件 [`00be0ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ed0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ea0.md)

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
      "definition_site": "00b6fa70",
      "incomplete_value": false,
      "site": "00b6fa74",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fa2c",
      "incomplete_value": false,
      "site": "00b6fa30",
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
            "const:87d:8"
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
      "00b6fa70",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6fa70",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md#insn-00b6fa30) · [`00b6f98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md#insn-00b6f98c) · [`00b6f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md#insn-00b6f9b0)
- 新版 [`00b6fa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f960.md#insn-00b6fa74) · [`00b6f9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f960.md#insn-00b6f9d0) · [`00b6f9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6f960.md#insn-00b6f9f4)

~~~diff
- 00b6fa30 ["INT_ADD", "register:40f0:8", ["const:b6fa30:8", "const:4:8"]]
- 00b6fa30 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b6fa74 ["INT_ADD", "register:40f0:8", ["const:b6fa74:8", "const:4:8"]]
+ 00b6fa74 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b6fa30 bytes 93c2fd97
+ 00b6fa74 bytes 93c2fd97
- 00b6f98c ["INT_ADD", "register:40f0:8", ["const:b6f98c:8", "const:4:8"]]
- 00b6f98c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b6f9d0 ["INT_ADD", "register:40f0:8", ["const:b6f9d0:8", "const:4:8"]]
+ 00b6f9d0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b6f98c bytes 99ad0194
+ 00b6f9d0 bytes 9cad0194
- 00b6f9b0 ["INT_ADD", "register:40f0:8", ["const:b6f9b0:8", "const:4:8"]]
- 00b6f9b0 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b6f9f4 ["INT_ADD", "register:40f0:8", ["const:b6f9f4:8", "const:4:8"]]
+ 00b6f9f4 ["CALL", null, ["callee:00be0ea0:8"]]
- 00b6f9b0 bytes 28c50194
+ 00b6f9f4 bytes 2bc50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-009ea19d556270c64cac8d2c3f996907"></a>

### [`00b6fd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md) → [`00b6fdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fdc4.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00be0b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b80.md)

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
      "definition_site": "00b6fde0",
      "incomplete_value": true,
      "site": "00b6fde4",
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
      "definition_site": "00b6fd9c",
      "incomplete_value": true,
      "site": "00b6fda0",
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
      "00b6fdd8",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fde4",
      "DATA",
      [
        "storage",
        "00c12b18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b6fdd8",
      "READ",
      [
        "storage",
        "00c1bc30",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fde4",
      "DATA",
      [
        "storage",
        "00c12b68",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md#insn-00b6fd94) · [`00b6fda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md#insn-00b6fda8) · [`00b6fdb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md#insn-00b6fdb8)
- 新版 [`00b6fdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fdc4.md#insn-00b6fdd8) · [`00b6fdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fdc4.md#insn-00b6fdec) · [`00b6fdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fdc4.md#insn-00b6fdfc)

~~~diff
- 00b6fd94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
- 00b6fd94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6fdd8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c30:8"]]
+ 00b6fdd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6fd94 bytes 29f145f9
+ 00b6fdd8 bytes 291946f9
- 00b6fda8 ["INT_ADD", "register:40f0:8", ["const:b6fda8:8", "const:4:8"]]
- 00b6fda8 ["CALL", null, ["callee:00bde200:8"]]
+ 00b6fdec ["INT_ADD", "register:40f0:8", ["const:b6fdec:8", "const:4:8"]]
+ 00b6fdec ["CALL", null, ["callee:00bde200:8"]]
- 00b6fda8 bytes 02b90194
+ 00b6fdec bytes 05b90194
- 00b6fdb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6fdb8 ["INT_ADD", "register:40f0:8", ["const:b6fdb8:8", "const:4:8"]]
- 00b6fdb8 ["CALLIND", null, ["register:0:8"]]
+ 00b6fdfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6fdfc ["INT_ADD", "register:40f0:8", ["const:b6fdfc:8", "const:4:8"]]
+ 00b6fdfc ["CALLIND", null, ["register:0:8"]]
- 00b6fdb8 bytes 00013fd6
+ 00b6fdfc bytes 00013fd6
~~~


<a id="compare-f93e4f2f27de2ac2e70fd4c91e01e615"></a>

### [`00b7000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md) → [`00b70050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b60b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b700dc",
      "incomplete_value": true,
      "site": "00b700f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70098",
      "incomplete_value": true,
      "site": "00b700ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae0:8"
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
      "definition_site": "00b700e0",
      "incomplete_value": true,
      "site": "00b700f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7009c",
      "incomplete_value": true,
      "site": "00b700ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
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
      "definition_site": "00b70114",
      "incomplete_value": true,
      "site": "00b70128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b700d0",
      "incomplete_value": true,
      "site": "00b700e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
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
      "00b700dc",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b700e0",
      "READ",
      [
        "storage",
        "010a1af0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70114",
      "READ",
      [
        "storage",
        "010a1af8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b700dc",
      "READ",
      [
        "storage",
        "010a1b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b700e0",
      "READ",
      [
        "storage",
        "010a1b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70114",
      "READ",
      [
        "storage",
        "010a1b38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b700ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md#insn-00b700ac) · [`00b700e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md#insn-00b700e4) · [`00b7018c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md#insn-00b7018c)
- 新版 [`00b700f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md#insn-00b700f0) · [`00b70128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md#insn-00b70128) · [`00b701d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md#insn-00b701d0)

~~~diff
- 00b700ac ["INT_ADD", "register:40f0:8", ["const:b700ac:8", "const:4:8"]]
- 00b700ac ["CALL", null, ["callee:0056681c:8"]]
+ 00b700f0 ["INT_ADD", "register:40f0:8", ["const:b700f0:8", "const:4:8"]]
+ 00b700f0 ["CALL", null, ["callee:0056681c:8"]]
- 00b700ac bytes dcd9e797
+ 00b700f0 bytes cbd9e797
- 00b700e4 ["INT_ADD", "register:40f0:8", ["const:b700e4:8", "const:4:8"]]
- 00b700e4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b70128 ["INT_ADD", "register:40f0:8", ["const:b70128:8", "const:4:8"]]
+ 00b70128 ["CALL", null, ["callee:0047495c:8"]]
- 00b700e4 bytes 1e12e497
+ 00b70128 bytes 0d12e497
- 00b7018c ["INT_ADD", "register:40f0:8", ["const:b7018c:8", "const:4:8"]]
- 00b7018c ["CALL", null, ["callee:0047495c:8"]]
+ 00b701d0 ["INT_ADD", "register:40f0:8", ["const:b701d0:8", "const:4:8"]]
+ 00b701d0 ["CALL", null, ["callee:0047495c:8"]]
- 00b7018c bytes f411e497
+ 00b701d0 bytes e311e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d40bb073f1a30de90a70d62eabac6e2"></a>

### [`00b7060c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md) → [`00b70650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b7068c",
      "incomplete_value": false,
      "site": "00b70690",
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
            "const:154:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70648",
      "incomplete_value": false,
      "site": "00b7064c",
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
            "const:c9:8"
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
      "00b7068c",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7068c",
      "PARAM",
      [
        "storage",
        "002a5154",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b7064c) · [`00b70648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b70648) · [`00b70658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b70658)
- 新版 [`00b70690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md#insn-00b70690) · [`00b7068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md#insn-00b7068c) · [`00b7069c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md#insn-00b7069c)

~~~diff
- 00b7064c ["INT_ADD", "register:40f0:8", ["const:b7064c:8", "const:4:8"]]
- 00b7064c ["CALL", null, ["callee:00bde180:8"]]
+ 00b70690 ["INT_ADD", "register:40f0:8", ["const:b70690:8", "const:4:8"]]
+ 00b70690 ["CALL", null, ["callee:00bde180:8"]]
- 00b7064c bytes b9b60194
+ 00b70690 bytes bcb60194
- 00b70648 ["COPY", "tmp:0:8", ["const:c9:8"]]
- 00b70648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b70648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b70648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7068c ["COPY", "tmp:0:8", ["const:154:8"]]
+ 00b7068c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7068c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7068c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b70648 bytes 00240391
+ 00b7068c bytes 00500591
- 00b70658 ["INT_ADD", "register:40f0:8", ["const:b70658:8", "const:4:8"]]
- 00b70658 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b7069c ["INT_ADD", "register:40f0:8", ["const:b7069c:8", "const:4:8"]]
+ 00b7069c ["CALL", null, ["callee:00bdde10:8"]]
- 00b70658 bytes dab50194
+ 00b7069c bytes ddb50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3186179e9f600ccadbd1a610908a3a2d"></a>

### [`00b70690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md) → [`00b706d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b706d4.md) _ZN8firebase4auth4User6UnlinkEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b707d0",
      "incomplete_value": true,
      "site": "00b707d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7078c",
      "incomplete_value": true,
      "site": "00b7078c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b70754",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b707cc",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b707d0",
      "DATA",
      [
        "storage",
        "00b64ec0",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b70754",
      "READ",
      [
        "storage",
        "010a1a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b707cc",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b707d0",
      "DATA",
      [
        "storage",
        "00b64f04",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b707d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md#insn-00b707d0) · [`00b706e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md#insn-00b706e4) · [`00b706f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md#insn-00b706f0)
- 新版 [`00b70814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b706d4.md#insn-00b70814) · [`00b70728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b706d4.md#insn-00b70728) · [`00b70734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b706d4.md#insn-00b70734)

~~~diff
- 00b707d0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:b80:8"]]
- 00b707d0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b70814 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:bd0:8"]]
+ 00b70814 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b707d0 bytes 42c045f9
+ 00b70814 bytes 42e845f9
- 00b706e4 ["INT_ADD", "register:40f0:8", ["const:b706e4:8", "const:4:8"]]
- 00b706e4 ["CALL", null, ["callee:00be0c00:8"]]
+ 00b70728 ["INT_ADD", "register:40f0:8", ["const:b70728:8", "const:4:8"]]
+ 00b70728 ["CALL", null, ["callee:00be0c00:8"]]
- 00b706e4 bytes 33c10194
+ 00b70728 bytes 36c10194
- 00b706f0 ["INT_ADD", "register:40f0:8", ["const:b706f0:8", "const:4:8"]]
- 00b706f0 ["CALL", null, ["callee:00bde200:8"]]
+ 00b70734 ["INT_ADD", "register:40f0:8", ["const:b70734:8", "const:4:8"]]
+ 00b70734 ["CALL", null, ["callee:00bde200:8"]]
- 00b706f0 bytes b0b60194
+ 00b70734 bytes b3b60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e2f59180a3aa0857a4748e4897e5490"></a>

### [`00b70898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md) → [`00b708dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b607a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md) [`00b652d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b652d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b607e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md) [`00b65314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00b709d8",
      "incomplete_value": true,
      "site": "00b709d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70994",
      "incomplete_value": true,
      "site": "00b70994",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
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
      "definition_site": "00b70974",
      "incomplete_value": true,
      "site": "00b70984",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70930",
      "incomplete_value": true,
      "site": "00b70940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a28:8"
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
      "definition_site": "00b70a24",
      "incomplete_value": false,
      "site": "00b70a38",
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
            "const:2a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b709e0",
      "incomplete_value": false,
      "site": "00b709f4",
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
            "const:216:8"
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
      "00b70974",
      "READ",
      [
        "storage",
        "010a1a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b709d4",
      "READ",
      [
        "storage",
        "00c1bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00b709d8",
      "DATA",
      [
        "storage",
        "00b652d0",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b70974",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b709d4",
      "READ",
      [
        "storage",
        "00c1bbf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b709d8",
      "DATA",
      [
        "storage",
        "00b65314",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md#insn-00b70940) · [`00b709d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md#insn-00b709d8) · [`00b709f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md#insn-00b709f4)
- 新版 [`00b70984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md#insn-00b70984) · [`00b70a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md#insn-00b70a1c) · [`00b70a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md#insn-00b70a38)

~~~diff
- 00b70940 ["INT_ADD", "register:40f0:8", ["const:b70940:8", "const:4:8"]]
- 00b70940 ["CALL", null, ["callee:0047495c:8"]]
+ 00b70984 ["INT_ADD", "register:40f0:8", ["const:b70984:8", "const:4:8"]]
+ 00b70984 ["CALL", null, ["callee:0047495c:8"]]
- 00b70940 bytes 0710e497
+ 00b70984 bytes f60fe497
- 00b709d8 ["INT_ADD", "register:40f0:8", ["const:b709d8:8", "const:4:8"]]
- 00b709d8 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b70a1c ["INT_ADD", "register:40f0:8", ["const:b70a1c:8", "const:4:8"]]
+ 00b70a1c ["CALL", null, ["callee:00bddf80:8"]]
- 00b709d8 bytes 56b50194
+ 00b70a1c bytes 59b50194
- 00b709f4 ["INT_ADD", "register:40f0:8", ["const:b709f4:8", "const:4:8"]]
- 00b709f4 ["CALL", null, ["callee:00be0be0:8"]]
+ 00b70a38 ["INT_ADD", "register:40f0:8", ["const:b70a38:8", "const:4:8"]]
+ 00b70a38 ["CALL", null, ["callee:00be0be0:8"]]
- 00b709f4 bytes 67c00194
+ 00b70a38 bytes 6ac00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232c80a42477d18d910d88458c2eef97"></a>

### [`00b710a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md) → [`00b710e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b710e8.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b71124",
      "incomplete_value": false,
      "site": "00b71128",
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
            "const:154:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b710e0",
      "incomplete_value": false,
      "site": "00b710e4",
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
            "const:c9:8"
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
      "00b71124",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b71124",
      "PARAM",
      [
        "storage",
        "002a5154",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b710e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md#insn-00b710e4) · [`00b710e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md#insn-00b710e0) · [`00b710f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md#insn-00b710f0)
- 新版 [`00b71128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b710e8.md#insn-00b71128) · [`00b71124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b710e8.md#insn-00b71124) · [`00b71134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b710e8.md#insn-00b71134)

~~~diff
- 00b710e4 ["INT_ADD", "register:40f0:8", ["const:b710e4:8", "const:4:8"]]
- 00b710e4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b71128 ["INT_ADD", "register:40f0:8", ["const:b71128:8", "const:4:8"]]
+ 00b71128 ["CALL", null, ["callee:00bde180:8"]]
- 00b710e4 bytes 13b40194
+ 00b71128 bytes 16b40194
- 00b710e0 ["COPY", "tmp:0:8", ["const:c9:8"]]
- 00b710e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b710e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b710e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b71124 ["COPY", "tmp:0:8", ["const:154:8"]]
+ 00b71124 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b71124 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b71124 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b710e0 bytes 00240391
+ 00b71124 bytes 00500591
- 00b710f0 ["INT_ADD", "register:40f0:8", ["const:b710f0:8", "const:4:8"]]
- 00b710f0 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b71134 ["INT_ADD", "register:40f0:8", ["const:b71134:8", "const:4:8"]]
+ 00b71134 ["CALL", null, ["callee:00bdde10:8"]]
- 00b710f0 bytes 34b30194
+ 00b71134 bytes 37b30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d33390d1bb50cd7443f57d8309572a74"></a>

### [`00b71738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md) → [`00b7177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b7177c.md) _ZNK8firebase4auth4User8metadataEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

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
      "definition_site": "00b717b0",
      "incomplete_value": true,
      "site": "00b717bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7176c",
      "incomplete_value": true,
      "site": "00b71778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a58:8"
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
      "definition_site": "00b717d8",
      "incomplete_value": true,
      "site": "00b717e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71794",
      "incomplete_value": true,
      "site": "00b717a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac8:8"
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
      "00b717b0",
      "READ",
      [
        "storage",
        "010a1a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717d8",
      "READ",
      [
        "storage",
        "010a1ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717e8",
      "READ",
      [
        "storage",
        "010a1ad0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b717b0",
      "READ",
      [
        "storage",
        "010a1a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717d8",
      "READ",
      [
        "storage",
        "010a1b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717e8",
      "READ",
      [
        "storage",
        "010a1b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b71778) · [`00b717a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b717a0) · [`00b71760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b71760)
- 新版 [`00b717bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b7177c.md#insn-00b717bc) · [`00b717e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b7177c.md#insn-00b717e4) · [`00b717a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b7177c.md#insn-00b717a4)

~~~diff
- 00b71778 ["INT_ADD", "register:40f0:8", ["const:b71778:8", "const:4:8"]]
- 00b71778 ["CALL", null, ["callee:0047495c:8"]]
+ 00b717bc ["INT_ADD", "register:40f0:8", ["const:b717bc:8", "const:4:8"]]
+ 00b717bc ["CALL", null, ["callee:0047495c:8"]]
- 00b71778 bytes 790ce497
+ 00b717bc bytes 680ce497
- 00b717a0 ["INT_ADD", "register:40f0:8", ["const:b717a0:8", "const:4:8"]]
- 00b717a0 ["CALL", null, ["callee:0056c6c4:8"]]
+ 00b717e4 ["INT_ADD", "register:40f0:8", ["const:b717e4:8", "const:4:8"]]
+ 00b717e4 ["CALL", null, ["callee:0056c6c4:8"]]
- 00b717a0 bytes c9ebe797
+ 00b717e4 bytes b8ebe797
- 00b71760 ["INT_ADD", "register:40f0:8", ["const:b71760:8", "const:4:8"]]
- 00b71760 ["CALL", null, ["callee:00bde200:8"]]
+ 00b717a4 ["INT_ADD", "register:40f0:8", ["const:b717a4:8", "const:4:8"]]
+ 00b717a4 ["CALL", null, ["callee:00bde200:8"]]
- 00b71760 bytes 94b20194
+ 00b717a4 bytes 97b20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b74df6069edd2bef56a9bfa71abb933"></a>

### [`00b718c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md) → [`00b71908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71908.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00be0b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b80.md)

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
      "definition_site": "00b71924",
      "incomplete_value": true,
      "site": "00b71928",
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
      "definition_site": "00b718e0",
      "incomplete_value": true,
      "site": "00b718e4",
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
      "00b7191c",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b71928",
      "DATA",
      [
        "storage",
        "00c12b18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b7191c",
      "READ",
      [
        "storage",
        "00c1bc30",
        null,
        "pointer"
      ]
    ],
    [
      "00b71928",
      "DATA",
      [
        "storage",
        "00c12b68",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b718d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718d8) · [`00b718ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718ec) · [`00b718fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718fc)
- 新版 [`00b7191c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71908.md#insn-00b7191c) · [`00b71930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71908.md#insn-00b71930) · [`00b71940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71908.md#insn-00b71940)

~~~diff
- 00b718d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
- 00b718d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7191c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c30:8"]]
+ 00b7191c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b718d8 bytes 29f145f9
+ 00b7191c bytes 291946f9
- 00b718ec ["INT_ADD", "register:40f0:8", ["const:b718ec:8", "const:4:8"]]
- 00b718ec ["CALL", null, ["callee:00bde200:8"]]
+ 00b71930 ["INT_ADD", "register:40f0:8", ["const:b71930:8", "const:4:8"]]
+ 00b71930 ["CALL", null, ["callee:00bde200:8"]]
- 00b718ec bytes 31b20194
+ 00b71930 bytes 34b20194
- 00b718fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b718fc ["INT_ADD", "register:40f0:8", ["const:b718fc:8", "const:4:8"]]
- 00b718fc ["CALLIND", null, ["register:0:8"]]
+ 00b71940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b71940 ["INT_ADD", "register:40f0:8", ["const:b71940:8", "const:4:8"]]
+ 00b71940 ["CALLIND", null, ["register:0:8"]]
- 00b718fc bytes 00013fd6
+ 00b71940 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a793595688e8bea9862cf5f21026e811"></a>

### [`00b71940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md) → [`00b71984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71984.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e40.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e90.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b719e8",
      "incomplete_value": false,
      "site": "00b719ec",
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
    "old": {
      "definition_site": "00b719a4",
      "incomplete_value": false,
      "site": "00b719a8",
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
            "const:4f4:8"
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
      "00b719e8",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b719e8",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b719a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b719a8) · [`00b719ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b719ec) · [`00b7196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b7196c)
- 新版 [`00b719ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71984.md#insn-00b719ec) · [`00b71a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71984.md#insn-00b71a30) · [`00b719b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71984.md#insn-00b719b0)

~~~diff
- 00b719a8 ["INT_ADD", "register:40f0:8", ["const:b719a8:8", "const:4:8"]]
- 00b719a8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b719ec ["INT_ADD", "register:40f0:8", ["const:b719ec:8", "const:4:8"]]
+ 00b719ec ["CALL", null, ["callee:00bde180:8"]]
- 00b719a8 bytes e2b10194
+ 00b719ec bytes e5b10194
- 00b719ec ["INT_ADD", "register:40f0:8", ["const:b719ec:8", "const:4:8"]]
- 00b719ec ["CALL", null, ["callee:00bde010:8"]]
+ 00b71a30 ["INT_ADD", "register:40f0:8", ["const:b71a30:8", "const:4:8"]]
+ 00b71a30 ["CALL", null, ["callee:00bde010:8"]]
- 00b719ec bytes 75b10194
+ 00b71a30 bytes 78b10194
- 00b7196c ["INT_ADD", "register:40f0:8", ["const:b7196c:8", "const:4:8"]]
- 00b7196c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b719b0 ["INT_ADD", "register:40f0:8", ["const:b719b0:8", "const:4:8"]]
+ 00b719b0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7196c bytes 99b00194
+ 00b719b0 bytes 9cb00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8be178fc98499d3f98f0ee4fba6106e"></a>

### [`00b71b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md) → [`00b71b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71b60.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e30.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e80.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b71bcc",
      "incomplete_value": false,
      "site": "00b71bd0",
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
    "old": {
      "definition_site": "00b71b88",
      "incomplete_value": false,
      "site": "00b71b8c",
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
            "const:4f4:8"
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
      "00b71bcc",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b71bcc",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b8c) · [`00b71b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b50) · [`00b71b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b5c)
- 新版 [`00b71bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71b60.md#insn-00b71bd0) · [`00b71b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71b60.md#insn-00b71b94) · [`00b71ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71b60.md#insn-00b71ba0)

~~~diff
- 00b71b8c ["INT_ADD", "register:40f0:8", ["const:b71b8c:8", "const:4:8"]]
- 00b71b8c ["CALL", null, ["callee:00bde180:8"]]
+ 00b71bd0 ["INT_ADD", "register:40f0:8", ["const:b71bd0:8", "const:4:8"]]
+ 00b71bd0 ["CALL", null, ["callee:00bde180:8"]]
- 00b71b8c bytes 69b10194
+ 00b71bd0 bytes 6cb10194
- 00b71b50 ["INT_ADD", "register:40f0:8", ["const:b71b50:8", "const:4:8"]]
- 00b71b50 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b71b94 ["INT_ADD", "register:40f0:8", ["const:b71b94:8", "const:4:8"]]
+ 00b71b94 ["CALL", null, ["callee:00bddc20:8"]]
- 00b71b50 bytes 20b00194
+ 00b71b94 bytes 23b00194
- 00b71b5c ["INT_ADD", "register:40f0:8", ["const:b71b5c:8", "const:4:8"]]
- 00b71b5c ["CALL", null, ["callee:00bde000:8"]]
+ 00b71ba0 ["INT_ADD", "register:40f0:8", ["const:b71ba0:8", "const:4:8"]]
+ 00b71ba0 ["CALL", null, ["callee:00bde000:8"]]
- 00b71b5c bytes 15b10194
+ 00b71ba0 bytes 18b10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70e2738bf6964b62f2c3fbf966744af"></a>

### [`00b727b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b727b8.md) → [`00b727fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b727fc.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be0b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b20.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00be0b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b70.md) [`00be0b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b80.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00b72818",
      "incomplete_value": true,
      "site": "00b7281c",
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
      "definition_site": "00b727d4",
      "incomplete_value": true,
      "site": "00b727d8",
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
      "00b72810",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b7281c",
      "DATA",
      [
        "storage",
        "00c12b80",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b72810",
      "READ",
      [
        "storage",
        "00c1bb98",
        null,
        "pointer"
      ]
    ],
    [
      "00b7281c",
      "DATA",
      [
        "storage",
        "00c12bd0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b727cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b727b8.md#insn-00b727cc) · [`00b72818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b727b8.md#insn-00b72818) · [`00b72828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b727b8.md#insn-00b72828)
- 新版 [`00b72810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b727fc.md#insn-00b72810) · [`00b7285c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b727fc.md#insn-00b7285c) · [`00b7286c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b727fc.md#insn-00b7286c)

~~~diff
- 00b727cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b48:8"]]
- 00b727cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b72810 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b98:8"]]
+ 00b72810 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b727cc bytes 29a545f9
+ 00b72810 bytes 29cd45f9
- 00b72818 ["INT_ADD", "register:40f0:8", ["const:b72818:8", "const:4:8"]]
- 00b72818 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b7285c ["INT_ADD", "register:40f0:8", ["const:b7285c:8", "const:4:8"]]
+ 00b7285c ["CALL", null, ["callee:00bdb060:8"]]
- 00b72818 bytes fea10194
+ 00b7285c bytes 01a20194
- 00b72828 ["INT_ADD", "register:40f0:8", ["const:b72828:8", "const:4:8"]]
- 00b72828 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b7286c ["INT_ADD", "register:40f0:8", ["const:b7286c:8", "const:4:8"]]
+ 00b7286c ["CALL", null, ["callee:00bdb060:8"]]
- 00b72828 bytes faa10194
+ 00b7286c bytes fda10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b09fe2aa27d84a2b6db897bdd0f2c1a8"></a>

### [`00b728e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b728e0.md) → [`00b72924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72924.md) _ZNSt6__ndk16chrono12system_clock3nowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6e0.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc860.md)
- 新版 呼出元 1件 [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) · 呼出先 3件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md)

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
      "definition_site": "00b72990",
      "incomplete_value": false,
      "site": "00b72994",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7294c",
      "incomplete_value": false,
      "site": "00b72950",
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
            "const:a5:8"
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
      "00b72990",
      "PARAM",
      [
        "storage",
        "002a40a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b72990",
      "PARAM",
      [
        "storage",
        "002a4130",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b728e0.md#insn-00b72950) · [`00b728f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b728e0.md#insn-00b728f8) · [`00b72940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b728e0.md#insn-00b72940)
- 新版 [`00b72994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72924.md#insn-00b72994) · [`00b7293c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72924.md#insn-00b7293c) · [`00b72984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72924.md#insn-00b72984)

~~~diff
- 00b72950 ["INT_ADD", "register:40f0:8", ["const:b72950:8", "const:4:8"]]
- 00b72950 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b72994 ["INT_ADD", "register:40f0:8", ["const:b72994:8", "const:4:8"]]
+ 00b72994 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b72950 bytes 4ca20194
+ 00b72994 bytes 4fa20194
- 00b728f8 ["INT_ADD", "register:40f0:8", ["const:b728f8:8", "const:4:8"]]
- 00b728f8 ["CALL", null, ["callee:00bdc8b0:8"]]
+ 00b7293c ["INT_ADD", "register:40f0:8", ["const:b7293c:8", "const:4:8"]]
+ 00b7293c ["CALL", null, ["callee:00bdc8b0:8"]]
- 00b728f8 bytes daa70194
+ 00b7293c bytes dda70194
- 00b72940 ["INT_ADD", "register:40f0:8", ["const:b72940:8", "const:4:8"]]
- 00b72940 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b72984 ["INT_ADD", "register:40f0:8", ["const:b72984:8", "const:4:8"]]
+ 00b72984 ["CALL", null, ["callee:00bdb270:8"]]
- 00b72940 bytes 38a20194
+ 00b72984 bytes 3ba20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0126938ede857b23268c5aeb2c3d8676"></a>

### [`00b72994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md) → [`00b729d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb020.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc860.md)
- 新版 呼出元 1件 [`00bdb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb070.md) · 呼出先 3件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md)

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
      "definition_site": "00b72a24",
      "incomplete_value": false,
      "site": "00b72a28",
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
            "const:68a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b729e0",
      "incomplete_value": false,
      "site": "00b729e4",
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
            "const:717:8"
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
      "00b72a24",
      "PARAM",
      [
        "storage",
        "00295717",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b72a24",
      "PARAM",
      [
        "storage",
        "0029568a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b729e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md#insn-00b729e4) · [`00b729ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md#insn-00b729ac) · [`00b729d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md#insn-00b729d4)
- 新版 [`00b72a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b72a28) · [`00b729f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b729f0) · [`00b72a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b72a18)

~~~diff
- 00b729e4 ["INT_ADD", "register:40f0:8", ["const:b729e4:8", "const:4:8"]]
- 00b729e4 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b72a28 ["INT_ADD", "register:40f0:8", ["const:b72a28:8", "const:4:8"]]
+ 00b72a28 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b729e4 bytes 27a20194
+ 00b72a28 bytes 2aa20194
- 00b729ac ["INT_ADD", "register:40f0:8", ["const:b729ac:8", "const:4:8"]]
- 00b729ac ["CALL", null, ["callee:00bdc8b0:8"]]
+ 00b729f0 ["INT_ADD", "register:40f0:8", ["const:b729f0:8", "const:4:8"]]
+ 00b729f0 ["CALL", null, ["callee:00bdc8b0:8"]]
- 00b729ac bytes ada70194
+ 00b729f0 bytes b0a70194
- 00b729d4 ["INT_ADD", "register:40f0:8", ["const:b729d4:8", "const:4:8"]]
- 00b729d4 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b72a18 ["INT_ADD", "register:40f0:8", ["const:b72a18:8", "const:4:8"]]
+ 00b72a18 ["CALL", null, ["callee:00bdb270:8"]]
- 00b729d4 bytes 13a20194
+ 00b72a18 bytes 16a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886d208b03d710c71da05c6d7f1a2fd8"></a>

### [`00b72a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a98.md) → [`00b72adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72adc.md) _ZNSt16nested_exceptionC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f40.md)

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
      "definition_site": "00b72af8",
      "incomplete_value": true,
      "site": "00b72afc",
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
      "definition_site": "00b72ab4",
      "incomplete_value": true,
      "site": "00b72ab8",
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
      "00b72af4",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b72afc",
      "DATA",
      [
        "storage",
        "00c12be0",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b72af4",
      "READ",
      [
        "storage",
        "00c1bc40",
        null,
        "pointer"
      ]
    ],
    [
      "00b72afc",
      "DATA",
      [
        "storage",
        "00c12c30",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a98.md#insn-00b72ab0) · [`00b72abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a98.md#insn-00b72abc)
- 新版 [`00b72af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72adc.md#insn-00b72af4) · [`00b72b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72adc.md#insn-00b72b00)

~~~diff
- 00b72ab0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf0:8"]]
- 00b72ab0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b72af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c40:8"]]
+ 00b72af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b72ab0 bytes 08f945f9
+ 00b72af4 bytes 082146f9
- 00b72abc ["INT_ADD", "register:40f0:8", ["const:b72abc:8", "const:4:8"]]
- 00b72abc ["CALL", null, ["callee:00be0f40:8"]]
+ 00b72b00 ["INT_ADD", "register:40f0:8", ["const:b72b00:8", "const:4:8"]]
+ 00b72b00 ["CALL", null, ["callee:00be0f40:8"]]
- 00b72abc bytes 0db90194
+ 00b72b00 bytes 10b90194
~~~


<a id="compare-61770e62b9539a96e9f62df95238d6e8"></a>

### [`00b72b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b00.md) → [`00b72b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b44.md) _ZNSt16nested_exceptionD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f00.md) · 呼出先 1件 [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`00be0f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f50.md) · 呼出先 1件 [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b72b54",
      "incomplete_value": true,
      "site": "00b72b54",
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
      "definition_site": "00b72b10",
      "incomplete_value": true,
      "site": "00b72b10",
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
      "00b72b4c",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b72b54",
      "DATA",
      [
        "storage",
        "00c12be0",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b72b4c",
      "READ",
      [
        "storage",
        "00c1bc40",
        null,
        "pointer"
      ]
    ],
    [
      "00b72b54",
      "DATA",
      [
        "storage",
        "00c12c30",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b00.md#insn-00b72b08)
- 新版 [`00b72b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b44.md#insn-00b72b4c)

~~~diff
- 00b72b08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf0:8"]]
- 00b72b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b72b4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c40:8"]]
+ 00b72b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b72b08 bytes 08f945f9
+ 00b72b4c bytes 082146f9
~~~


<a id="compare-f304845dd4bb46fcb5e53eedd31c6f71"></a>

### [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md) → [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) FUN_00b73318

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b72bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72bb4.md) · 呼出先 4件 [`00b73328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73328.md) [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00b72bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md) · 呼出先 4件 [`00b7336c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b7336c.md) [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "00b7334c",
      "incomplete_value": true,
      "site": "00b73354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73308",
      "incomplete_value": true,
      "site": "00b73310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
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
      "definition_site": "00b73350",
      "incomplete_value": true,
      "site": "00b73354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7330c",
      "incomplete_value": true,
      "site": "00b73310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c00:8"
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
      "00b7334c",
      "READ",
      [
        "storage",
        "00c1bbf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7334c",
      "PARAM",
      [
        "storage",
        "00c16ab8",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73350",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7334c",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00b7334c",
      "PARAM",
      [
        "storage",
        "00c16b08",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73350",
      "READ",
      [
        "storage",
        "00c1bc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md#insn-00b73310) · [`00b732ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md#insn-00b732ec) · [`00b732f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md#insn-00b732f8)
- 新版 [`00b73354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md#insn-00b73354) · [`00b73330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md#insn-00b73330) · [`00b7333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md#insn-00b7333c)

~~~diff
- 00b73310 ["INT_ADD", "register:40f0:8", ["const:b73310:8", "const:4:8"]]
- 00b73310 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b73354 ["INT_ADD", "register:40f0:8", ["const:b73354:8", "const:4:8"]]
+ 00b73354 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b73310 bytes 589f0194
+ 00b73354 bytes 5b9f0194
- 00b732ec ["INT_ADD", "register:40f0:8", ["const:b732ec:8", "const:4:8"]]
- 00b732ec ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b73330 ["INT_ADD", "register:40f0:8", ["const:b73330:8", "const:4:8"]]
+ 00b73330 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b732ec bytes 599f0194
+ 00b73330 bytes 5c9f0194
- 00b732f8 ["INT_ADD", "register:40f0:8", ["const:b732f8:8", "const:4:8"]]
- 00b732f8 ["CALL", null, ["callee:00b7336c:8"]]
+ 00b7333c ["INT_ADD", "register:40f0:8", ["const:b7333c:8", "const:4:8"]]
+ 00b7333c ["CALL", null, ["callee:00b7336c:8"]]
- 00b732f8 bytes 0c000094
+ 00b7333c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-538f92e96973ebaea97cc70f47ab8c61"></a>

### [`00b736a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736a4.md) → [`00b736e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b736e8.md) _ZSt17__throw_bad_allocv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md) · 呼出先 4件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md)
- 新版 呼出元 1件 [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md) · 呼出先 4件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

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
      "definition_site": "00b73714",
      "incomplete_value": true,
      "site": "00b7371c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b736d0",
      "incomplete_value": true,
      "site": "00b736d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa8:8"
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
      "definition_site": "00b73718",
      "incomplete_value": true,
      "site": "00b7371c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b736d4",
      "incomplete_value": true,
      "site": "00b736d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "00b73714",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b73714",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73718",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b73714",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00b73714",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73718",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b736d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736a4.md#insn-00b736d8) · [`00b736b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736a4.md#insn-00b736b8) · [`00b736c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736a4.md#insn-00b736c0)
- 新版 [`00b7371c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b736e8.md#insn-00b7371c) · [`00b736fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b736e8.md#insn-00b736fc) · [`00b73704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b736e8.md#insn-00b73704)

~~~diff
- 00b736d8 ["INT_ADD", "register:40f0:8", ["const:b736d8:8", "const:4:8"]]
- 00b736d8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b7371c ["INT_ADD", "register:40f0:8", ["const:b7371c:8", "const:4:8"]]
+ 00b7371c ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b736d8 bytes 669e0194
+ 00b7371c bytes 699e0194
- 00b736b8 ["INT_ADD", "register:40f0:8", ["const:b736b8:8", "const:4:8"]]
- 00b736b8 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b736fc ["INT_ADD", "register:40f0:8", ["const:b736fc:8", "const:4:8"]]
+ 00b736fc ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b736b8 bytes 669e0194
+ 00b736fc bytes 699e0194
- 00b736c0 ["INT_ADD", "register:40f0:8", ["const:b736c0:8", "const:4:8"]]
- 00b736c0 ["CALL", null, ["callee:00bdbbf0:8"]]
+ 00b73704 ["INT_ADD", "register:40f0:8", ["const:b73704:8", "const:4:8"]]
+ 00b73704 ["CALL", null, ["callee:00bdbbf0:8"]]
- 00b736c0 bytes 38a10194
+ 00b73704 bytes 3ba10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d9b1b0f49d174e652044b27cd2719c"></a>

### [`00b736dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736dc.md) → [`00b73720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73720.md) _ZNSt11logic_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f40.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00be0f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f90.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "00b73740",
      "incomplete_value": true,
      "site": "00b73744",
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
      "definition_site": "00b736fc",
      "incomplete_value": true,
      "site": "00b73700",
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
      "00b7373c",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b73744",
      "DATA",
      [
        "storage",
        "00c168e0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b7373c",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b73744",
      "DATA",
      [
        "storage",
        "00c16930",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b736f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736dc.md#insn-00b736f8) · [`00b73718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736dc.md#insn-00b73718) · [`00b73724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736dc.md#insn-00b73724)
- 新版 [`00b7373c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73720.md#insn-00b7373c) · [`00b7375c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73720.md#insn-00b7375c) · [`00b73768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73720.md#insn-00b73768)

~~~diff
- 00b736f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
- 00b736f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7373c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c60:8"]]
+ 00b7373c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b736f8 bytes 080946f9
+ 00b7373c bytes 083146f9
- 00b73718 ["INT_ADD", "register:40f0:8", ["const:b73718:8", "const:4:8"]]
- 00b73718 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b7375c ["INT_ADD", "register:40f0:8", ["const:b7375c:8", "const:4:8"]]
+ 00b7375c ["CALL", null, ["callee:00bdb190:8"]]
- 00b73718 bytes 8a9e0194
+ 00b7375c bytes 8d9e0194
- 00b73724 ["INT_ADD", "register:40f0:8", ["const:b73724:8", "const:4:8"]]
- 00b73724 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b73768 ["INT_ADD", "register:40f0:8", ["const:b73768:8", "const:4:8"]]
+ 00b73768 ["CALL", null, ["callee:00bdb040:8"]]
- 00b73724 bytes 339e0194
+ 00b73768 bytes 369e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8407f0aca1c6902136336c212626b5b6"></a>

### [`00b73770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73770.md) → [`00b737b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb090.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "00b737d8",
      "incomplete_value": true,
      "site": "00b737dc",
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
      "definition_site": "00b73794",
      "incomplete_value": true,
      "site": "00b73798",
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
      "00b737d4",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b737dc",
      "DATA",
      [
        "storage",
        "00c168e0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b737d4",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b737dc",
      "DATA",
      [
        "storage",
        "00c16930",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73770.md#insn-00b73790) · [`00b737a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73770.md#insn-00b737a0) · [`00b737ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73770.md#insn-00b737ac)
- 新版 [`00b737d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md#insn-00b737d4) · [`00b737e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md#insn-00b737e4) · [`00b737f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md#insn-00b737f0)

~~~diff
- 00b73790 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
- 00b73790 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b737d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c60:8"]]
+ 00b737d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b73790 bytes 080946f9
+ 00b737d4 bytes 083146f9
- 00b737a0 ["INT_ADD", "register:40f0:8", ["const:b737a0:8", "const:4:8"]]
- 00b737a0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b737e4 ["INT_ADD", "register:40f0:8", ["const:b737e4:8", "const:4:8"]]
+ 00b737e4 ["CALL", null, ["callee:00bdb190:8"]]
- 00b737a0 bytes 689e0194
+ 00b737e4 bytes 6b9e0194
- 00b737ac ["INT_ADD", "register:40f0:8", ["const:b737ac:8", "const:4:8"]]
- 00b737ac ["CALL", null, ["callee:00bdb040:8"]]
+ 00b737f0 ["INT_ADD", "register:40f0:8", ["const:b737f0:8", "const:4:8"]]
+ 00b737f0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b737ac bytes 119e0194
+ 00b737f0 bytes 149e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb713dfec2cfd7f05f98306ae8e5ac8"></a>

### [`00b7388c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7388c.md) → [`00b738d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b738d0.md) _ZNSt13runtime_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f50.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00be0fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fa0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "00b738f0",
      "incomplete_value": true,
      "site": "00b738f4",
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
      "definition_site": "00b738ac",
      "incomplete_value": true,
      "site": "00b738b0",
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
      "00b738ec",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b738f4",
      "DATA",
      [
        "storage",
        "00c16908",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b738ec",
      "READ",
      [
        "storage",
        "00c1bc68",
        null,
        "pointer"
      ]
    ],
    [
      "00b738f4",
      "DATA",
      [
        "storage",
        "00c16958",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b738a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7388c.md#insn-00b738a8) · [`00b738c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7388c.md#insn-00b738c8) · [`00b738d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7388c.md#insn-00b738d4)
- 新版 [`00b738ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b738d0.md#insn-00b738ec) · [`00b7390c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b738d0.md#insn-00b7390c) · [`00b73918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b738d0.md#insn-00b73918)

~~~diff
- 00b738a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 00b738a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b738ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
+ 00b738ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b738a8 bytes 080d46f9
+ 00b738ec bytes 083546f9
- 00b738c8 ["INT_ADD", "register:40f0:8", ["const:b738c8:8", "const:4:8"]]
- 00b738c8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b7390c ["INT_ADD", "register:40f0:8", ["const:b7390c:8", "const:4:8"]]
+ 00b7390c ["CALL", null, ["callee:00bdb190:8"]]
- 00b738c8 bytes 1e9e0194
+ 00b7390c bytes 219e0194
- 00b738d4 ["INT_ADD", "register:40f0:8", ["const:b738d4:8", "const:4:8"]]
- 00b738d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b73918 ["INT_ADD", "register:40f0:8", ["const:b73918:8", "const:4:8"]]
+ 00b73918 ["CALL", null, ["callee:00bdb040:8"]]
- 00b738d4 bytes c79d0194
+ 00b73918 bytes ca9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c58e2fdaa1ed8c7a08f502d59186f22"></a>

### [`00b73920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73920.md) → [`00b73964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73964.md) _ZNSt13runtime_errorC2EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdda30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda30.md) [`00be0f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f70.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00bdda80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda80.md) [`00be0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fc0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "00b73988",
      "incomplete_value": true,
      "site": "00b7398c",
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
      "definition_site": "00b73944",
      "incomplete_value": true,
      "site": "00b73948",
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
      "00b73984",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b7398c",
      "DATA",
      [
        "storage",
        "00c16908",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b73984",
      "READ",
      [
        "storage",
        "00c1bc68",
        null,
        "pointer"
      ]
    ],
    [
      "00b7398c",
      "DATA",
      [
        "storage",
        "00c16958",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73920.md#insn-00b73940) · [`00b73950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73920.md#insn-00b73950) · [`00b7395c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73920.md#insn-00b7395c)
- 新版 [`00b73984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73964.md#insn-00b73984) · [`00b73994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73964.md#insn-00b73994) · [`00b739a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73964.md#insn-00b739a0)

~~~diff
- 00b73940 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 00b73940 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b73984 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
+ 00b73984 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b73940 bytes 080d46f9
+ 00b73984 bytes 083546f9
- 00b73950 ["INT_ADD", "register:40f0:8", ["const:b73950:8", "const:4:8"]]
- 00b73950 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b73994 ["INT_ADD", "register:40f0:8", ["const:b73994:8", "const:4:8"]]
+ 00b73994 ["CALL", null, ["callee:00bdb190:8"]]
- 00b73950 bytes fc9d0194
+ 00b73994 bytes ff9d0194
- 00b7395c ["INT_ADD", "register:40f0:8", ["const:b7395c:8", "const:4:8"]]
- 00b7395c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b739a0 ["INT_ADD", "register:40f0:8", ["const:b739a0:8", "const:4:8"]]
+ 00b739a0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7395c bytes a59d0194
+ 00b739a0 bytes a89d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef20c53ecbe91b77d4e71a7ab7f4a1b"></a>

### [`00b73a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md) → [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) · 呼出先 4件 [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be0f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f70.md)
- 新版 呼出元 1件 [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) · 呼出先 4件 [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fc0.md)

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
      "definition_site": "00b73ab4",
      "incomplete_value": true,
      "site": "00b73abc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73a70",
      "incomplete_value": true,
      "site": "00b73a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "definition_site": "00b73ab8",
      "incomplete_value": true,
      "site": "00b73abc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73a74",
      "incomplete_value": true,
      "site": "00b73a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
      "00b73ab4",
      "READ",
      [
        "storage",
        "00c1bc20",
        null,
        "pointer"
      ]
    ],
    [
      "00b73ab4",
      "PARAM",
      [
        "storage",
        "00c16a60",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73ab8",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b73ab4",
      "READ",
      [
        "storage",
        "00c1bc70",
        null,
        "pointer"
      ]
    ],
    [
      "00b73ab4",
      "PARAM",
      [
        "storage",
        "00c16ab0",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73ab8",
      "READ",
      [
        "storage",
        "00c1bc78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md#insn-00b73a78) · [`00b73a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md#insn-00b73a54) · [`00b73a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md#insn-00b73a60)
- 新版 [`00b73abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md#insn-00b73abc) · [`00b73a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md#insn-00b73a98) · [`00b73aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md#insn-00b73aa4)

~~~diff
- 00b73a78 ["INT_ADD", "register:40f0:8", ["const:b73a78:8", "const:4:8"]]
- 00b73a78 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b73abc ["INT_ADD", "register:40f0:8", ["const:b73abc:8", "const:4:8"]]
+ 00b73abc ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b73a78 bytes 7e9d0194
+ 00b73abc bytes 819d0194
- 00b73a54 ["INT_ADD", "register:40f0:8", ["const:b73a54:8", "const:4:8"]]
- 00b73a54 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b73a98 ["INT_ADD", "register:40f0:8", ["const:b73a98:8", "const:4:8"]]
+ 00b73a98 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b73a54 bytes 7f9d0194
+ 00b73a98 bytes 829d0194
- 00b73a60 ["INT_ADD", "register:40f0:8", ["const:b73a60:8", "const:4:8"]]
- 00b73a60 ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b73aa4 ["INT_ADD", "register:40f0:8", ["const:b73aa4:8", "const:4:8"]]
+ 00b73aa4 ["CALL", null, ["callee:00be0fc0:8"]]
- 00b73a60 bytes 44b50194
+ 00b73aa4 bytes 47b50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-479dc1f32f0e368215ad22393149108a"></a>

### [`00b751f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b751f0.md) → [`00b75234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

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
      "definition_site": "00b752dc",
      "incomplete_value": false,
      "site": "00b752e0",
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
            "const:2c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b75298",
      "incomplete_value": false,
      "site": "00b7529c",
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
            "const:236:8"
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
      "00b752dc",
      "PARAM",
      [
        "storage",
        "0029f236",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b752dc",
      "PARAM",
      [
        "storage",
        "0029f2c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7529c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b751f0.md#insn-00b7529c) · [`00b75268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b751f0.md#insn-00b75268) · [`00b75298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b751f0.md#insn-00b75298)
- 新版 [`00b752e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md#insn-00b752e0) · [`00b752ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md#insn-00b752ac) · [`00b752dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md#insn-00b752dc)

~~~diff
- 00b7529c ["INT_ADD", "register:40f0:8", ["const:b7529c:8", "const:4:8"]]
- 00b7529c ["CALL", null, ["callee:0041fdf0:8"]]
+ 00b752e0 ["INT_ADD", "register:40f0:8", ["const:b752e0:8", "const:4:8"]]
+ 00b752e0 ["CALL", null, ["callee:0041fdf0:8"]]
- 00b7529c bytes d5aae297
+ 00b752e0 bytes c4aae297
- 00b75268 ["INT_ADD", "register:40f0:8", ["const:b75268:8", "const:4:8"]]
- 00b75268 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b752ac ["INT_ADD", "register:40f0:8", ["const:b752ac:8", "const:4:8"]]
+ 00b752ac ["CALL", null, ["callee:00bdb200:8"]]
- 00b75268 bytes d2970194
+ 00b752ac bytes d5970194
- 00b75298 ["COPY", "tmp:0:8", ["const:236:8"]]
- 00b75298 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b75298 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b75298 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b752dc ["COPY", "tmp:0:8", ["const:2c1:8"]]
+ 00b752dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b752dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b752dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b75298 bytes 00d80891
+ 00b752dc bytes 00040b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a72fa6e3d85509f01eaf08dbddd360a"></a>

### [`00b7765c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7765c.md) → [`00b776a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)

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
      "definition_site": "00b77750",
      "incomplete_value": false,
      "site": "00b77754",
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
            "const:2c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7770c",
      "incomplete_value": false,
      "site": "00b77710",
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
            "const:236:8"
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
      "00b77750",
      "PARAM",
      [
        "storage",
        "0029f236",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77750",
      "PARAM",
      [
        "storage",
        "0029f2c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7765c.md#insn-00b77710) · [`00b776e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7765c.md#insn-00b776e0) · [`00b7770c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7765c.md#insn-00b7770c)
- 新版 [`00b77754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b77754) · [`00b77724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b77724) · [`00b77750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b77750)

~~~diff
- 00b77710 ["INT_ADD", "register:40f0:8", ["const:b77710:8", "const:4:8"]]
- 00b77710 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00b77754 ["INT_ADD", "register:40f0:8", ["const:b77754:8", "const:4:8"]]
+ 00b77754 ["CALL", null, ["callee:0041fdf0:8"]]
- 00b77710 bytes b8a1e297
+ 00b77754 bytes a7a1e297
- 00b776e0 ["INT_ADD", "register:40f0:8", ["const:b776e0:8", "const:4:8"]]
- 00b776e0 ["CALL", null, ["callee:00be1050:8"]]
+ 00b77724 ["INT_ADD", "register:40f0:8", ["const:b77724:8", "const:4:8"]]
+ 00b77724 ["CALL", null, ["callee:00be1050:8"]]
- 00b776e0 bytes 48a60194
+ 00b77724 bytes 4ba60194
- 00b7770c ["COPY", "tmp:0:8", ["const:236:8"]]
- 00b7770c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7770c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7770c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b77750 ["COPY", "tmp:0:8", ["const:2c1:8"]]
+ 00b77750 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77750 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77750 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7770c bytes 00d80891
+ 00b77750 bytes 00040b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad6c86de1662f484886b3321ad40575"></a>

### [`00b77cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cbc.md) → [`00b77d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d00.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00bde210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde210.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00b77d10",
      "incomplete_value": false,
      "site": "00b77d14",
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
            "const:24c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77ccc",
      "incomplete_value": false,
      "site": "00b77cd0",
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
            "const:1b2:8"
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
      "00b77d10",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77d10",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cbc.md#insn-00b77cd0) · [`00b77ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cbc.md#insn-00b77ccc)
- 新版 [`00b77d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d00.md#insn-00b77d14) · [`00b77d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d00.md#insn-00b77d10)

~~~diff
- 00b77cd0 ["INT_ADD", "register:40f0:8", ["const:b77cd0:8", "const:4:8"]]
- 00b77cd0 ["CALL", null, ["callee:00418c38:8"]]
+ 00b77d14 ["INT_ADD", "register:40f0:8", ["const:b77d14:8", "const:4:8"]]
+ 00b77d14 ["CALL", null, ["callee:00418c38:8"]]
- 00b77cd0 bytes da83e297
+ 00b77d14 bytes c983e297
- 00b77ccc ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 00b77ccc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b77ccc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b77ccc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b77d10 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 00b77d10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77d10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77d10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b77ccc bytes 00c80691
+ 00b77d10 bytes 00300991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95232ea70e3e80b37cde9089600619fc"></a>

### [`00b77cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cd4.md) → [`00b77d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d18.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0430.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00be0480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0480.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "00b77d28",
      "incomplete_value": false,
      "site": "00b77d2c",
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
            "const:24c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77ce4",
      "incomplete_value": false,
      "site": "00b77ce8",
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
            "const:1b2:8"
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
      "00b77d28",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77d28",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cd4.md#insn-00b77ce8) · [`00b77ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cd4.md#insn-00b77ce4)
- 新版 [`00b77d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d18.md#insn-00b77d2c) · [`00b77d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d18.md#insn-00b77d28)

~~~diff
- 00b77ce8 ["INT_ADD", "register:40f0:8", ["const:b77ce8:8", "const:4:8"]]
- 00b77ce8 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00b77d2c ["INT_ADD", "register:40f0:8", ["const:b77d2c:8", "const:4:8"]]
+ 00b77d2c ["CALL", null, ["callee:0041fdf0:8"]]
- 00b77ce8 bytes 42a0e297
+ 00b77d2c bytes 31a0e297
- 00b77ce4 ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 00b77ce4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b77ce4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b77ce4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b77d28 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 00b77d28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77d28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77d28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b77ce4 bytes 00c80691
+ 00b77d28 bytes 00300991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4fb141d2b5f789d619550581dc7418"></a>

### [`00b77cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md) → [`00b77d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d30.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1c0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6f0.md)
- 新版 呼出元 1件 [`00bdb210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb210.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`00b7b30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb740.md)

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
      "definition_site": "00b77e50",
      "incomplete_value": true,
      "site": "00b77e50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77e0c",
      "incomplete_value": true,
      "site": "00b77e0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
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
      "definition_site": "00b77e58",
      "incomplete_value": true,
      "site": "00b77e58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b77e14",
      "incomplete_value": true,
      "site": "00b77e14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b77dfc",
      "incomplete_value": false,
      "site": "00b77e0c",
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
            "const:ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77db8",
      "incomplete_value": false,
      "site": "00b77dc8",
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
            "const:55:8"
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
      "00b77dfc",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b77e40",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b77e44",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77dfc",
      "PARAM",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b77e40",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b77e44",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md#insn-00b77dc8) · [`00b77d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md#insn-00b77d3c) · [`00b77d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md#insn-00b77d58)
- 新版 [`00b77e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d30.md#insn-00b77e0c) · [`00b77d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d30.md#insn-00b77d80) · [`00b77d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d30.md#insn-00b77d9c)

~~~diff
- 00b77dc8 ["INT_ADD", "register:40f0:8", ["const:b77dc8:8", "const:4:8"]]
- 00b77dc8 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b77e0c ["INT_ADD", "register:40f0:8", ["const:b77e0c:8", "const:4:8"]]
+ 00b77e0c ["CALL", null, ["callee:0045efa8:8"]]
- 00b77dc8 bytes 789ce397
+ 00b77e0c bytes 679ce397
- 00b77d3c ["INT_ADD", "register:40f0:8", ["const:b77d3c:8", "const:4:8"]]
- 00b77d3c ["CALL", null, ["callee:00bdb270:8"]]
+ 00b77d80 ["INT_ADD", "register:40f0:8", ["const:b77d80:8", "const:4:8"]]
+ 00b77d80 ["CALL", null, ["callee:00bdb270:8"]]
- 00b77d3c bytes 398d0194
+ 00b77d80 bytes 3c8d0194
- 00b77d58 ["INT_ADD", "register:40f0:8", ["const:b77d58:8", "const:4:8"]]
- 00b77d58 ["CALL", null, ["callee:00bdb740:8"]]
+ 00b77d9c ["INT_ADD", "register:40f0:8", ["const:b77d9c:8", "const:4:8"]]
+ 00b77d9c ["CALL", null, ["callee:00bdb740:8"]]
- 00b77d58 bytes 668e0194
+ 00b77d9c bytes 698e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

